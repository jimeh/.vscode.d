#!/usr/bin/env python3

import argparse
import datetime as dt
import hashlib
import json
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives.padding import PKCS7
except ImportError:
    print("Missing dependency: cryptography", file=sys.stderr)
    print(
        "Run with: uv run --with cryptography state-migrate.py ...",
        file=sys.stderr,
    )
    print("Or install with: python3 -m pip install cryptography", file=sys.stderr)
    sys.exit(1)


SALT = b"saltysalt"
MACOS_ITERATIONS = 1003
IV = b" " * 16


def get_keychain_password(service: str, account: str | None = None) -> bytes:
    cmd = ["security", "find-generic-password", "-w", "-s", service]
    if account:
        cmd.extend(["-a", account])

    try:
        return subprocess.check_output(cmd).rstrip(b"\n")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"Could not read Keychain item for service: {service!r}") from e


def derive_key(keychain_password: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha1",
        keychain_password,
        SALT,
        MACOS_ITERATIONS,
        dklen=16,
    )


def aes_cbc_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    decryptor = Cipher(algorithms.AES(key), modes.CBC(IV)).decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()


def aes_cbc_encrypt(plaintext: bytes, key: bytes) -> bytes:
    padder = PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()

    encryptor = Cipher(algorithms.AES(key), modes.CBC(IV)).encryptor()
    return encryptor.update(padded) + encryptor.finalize()


def _bytes_from_ints(values, label: str) -> bytes:
    data = []
    for index, item in enumerate(values):
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"{label} byte {index} is not an integer")

        if item < 0 or item > 255:
            raise ValueError(f"{label} byte {index} is out of range: {item}")

        data.append(item)

    return bytes(data)


def _bytes_from_byte_object(value: dict, label: str) -> bytes:
    indexes = sorted(int(key) for key in value)
    if indexes != list(range(len(indexes))):
        raise ValueError(f"Unsupported {label} format: sparse byte object")

    return _bytes_from_ints(
        (value[str(index)] for index in indexes),
        label,
    )


def _unsupported_value_error(value) -> ValueError:
    if isinstance(value, dict):
        keys = ", ".join(sorted(str(key) for key in value)[:8])
        suffix = "..." if len(value) > 8 else ""
        return ValueError(f"Unsupported VS Code value object keys: {keys}{suffix}")

    return ValueError(
        f"Unsupported VS Code value format: {type(value).__name__}"
    )


def _decode_vscode_value(value, label: str = "VS Code value") -> bytes:
    if isinstance(value, dict) and value.get("type") == "Buffer":
        return _bytes_from_ints(value["data"], "Buffer data")

    if isinstance(value, dict) and all(str(key).isdecimal() for key in value):
        return _bytes_from_byte_object(value, "Byte object")

    if isinstance(value, list):
        return _bytes_from_ints(value, label)

    if isinstance(value, dict):
        if len(value) == 1:
            key, nested_value = next(iter(value.items()))
            if key in ("data", "value", "bytes", "buffer", "contents"):
                return _decode_vscode_value(nested_value, key)

    raise _unsupported_value_error(value)


def parse_vscode_value(value):
    if isinstance(value, bytes):
        text = value.decode("utf-8")
    else:
        text = value

    parsed = json.loads(text)
    return _decode_vscode_value(parsed)


def try_parse_vscode_value(value) -> bytes | None:
    try:
        return parse_vscode_value(value)
    except ValueError as error:
        if str(error).startswith("Unsupported VS Code value"):
            return None

        raise


def encode_vscode_value(data: bytes) -> str:
    return json.dumps(
        {"type": "Buffer", "data": list(data)},
        separators=(",", ":"),
    )


def decrypt_blob(blob: bytes, key: bytes) -> tuple[bytes, bytes]:
    prefix = blob[:3]
    if prefix not in (b"v10", b"v11"):
        raise ValueError(f"Unsupported encrypted blob prefix: {prefix!r}")

    plaintext = aes_cbc_decrypt(blob[3:], key)
    return prefix, plaintext


def encrypt_blob(plaintext: bytes, key: bytes, prefix: bytes) -> bytes:
    return prefix + aes_cbc_encrypt(plaintext, key)


def is_encrypted_blob(blob: bytes) -> bool:
    return blob[:3] in (b"v10", b"v11")


def fetch_value(db_path: Path, item_key: str) -> str:
    with sqlite3.connect(db_path) as db:
        row = db.execute(
            "SELECT value FROM ItemTable WHERE key = ?",
            (item_key,),
        ).fetchone()

    if not row:
        raise KeyError(f"Key not found in source DB: {item_key}")

    return row[0]


def write_value(db_path: Path, item_key: str, value: str):
    with sqlite3.connect(db_path) as db:
        db.execute(
            "INSERT OR REPLACE INTO ItemTable(key, value) VALUES (?, ?)",
            (item_key, value),
        )
        db.commit()


def main():
    parser = argparse.ArgumentParser(
        description="Re-encrypt selected VS Code SecretStorage rows from one macOS app to another."
    )

    parser.add_argument("--src-db", required=True, type=Path)
    parser.add_argument("--dst-db", required=True, type=Path)

    parser.add_argument("--src-service", default="Code Safe Storage")
    parser.add_argument("--dst-service", required=True)

    parser.add_argument("--src-account")
    parser.add_argument("--dst-account")

    parser.add_argument(
        "--key",
        action="append",
        required=True,
        help='Exact ItemTable key, e.g. secret://{"extensionId":"x.y","key":"token"}',
    )

    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-backup", action="store_true")

    args = parser.parse_args()

    src_db = args.src_db.expanduser()
    dst_db = args.dst_db.expanduser()

    if not src_db.exists():
        raise SystemExit(f"Source DB does not exist: {src_db}")

    if not dst_db.exists():
        raise SystemExit(f"Destination DB does not exist: {dst_db}")

    src_key = derive_key(get_keychain_password(args.src_service, args.src_account))
    dst_key = derive_key(get_keychain_password(args.dst_service, args.dst_account))

    if not args.dry_run and not args.no_backup:
        stamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
        backup = dst_db.with_name(dst_db.name + f".backup-{stamp}")
        shutil.copy2(dst_db, backup)
        print(f"Backed up destination DB: {backup}")

    for item_key in args.key:
        raw_value = fetch_value(src_db, item_key)
        source_blob = try_parse_vscode_value(raw_value)

        if source_blob is None or not is_encrypted_blob(source_blob):
            if args.dry_run:
                print(f"[dry-run] COPY: {item_key} (plain state value)")
            else:
                write_value(dst_db, item_key, raw_value)
                print(f"Copied: {item_key} (plain state value)")

            continue

        prefix, plaintext = decrypt_blob(source_blob, src_key)

        migrated_blob = encrypt_blob(plaintext, dst_key, prefix)

        # Verify our target encryption round-trips before writing.
        _, check_plaintext = decrypt_blob(migrated_blob, dst_key)
        if check_plaintext != plaintext:
            raise RuntimeError(f"Round-trip verification failed for {item_key}")

        if args.dry_run:
            print(f"[dry-run] OK: {item_key} ({len(plaintext)} plaintext bytes)")
        else:
            write_value(dst_db, item_key, encode_vscode_value(migrated_blob))
            print(f"Migrated: {item_key} ({len(plaintext)} plaintext bytes)")

    print("Done. Start the fork and test login state.")


if __name__ == "__main__":
    main()
