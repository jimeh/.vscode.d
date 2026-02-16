# AGENTS.md

Unified VSCode configuration repo — manages settings, keybindings, extensions,
and tool configs for multiple VSCode-compatible editors via symlinks.

## Key Commands

```bash
./siren <editor> config             # Symlink config files to editor
./siren <editor> extensions         # Install extensions from lock file
./siren <editor> extensions --latest # Install latest extension versions
./siren <editor> dump-extensions    # Export installed extensions to lock file
make all-config                     # Configure all editors
make all-extensions                 # Install extensions for all editors
```

### Supported Editors

antigravity (agy, a), cursor (c), kiro (k), vscode (code, vsc, v),
vscode-insiders (vsci, i), windsurf (surf, w)

## Conventions

- **Config files** are symlinked from this repo into each editor's config dir.
  The siren script handles backup and linking per OS (macOS/Linux).
- **Extension lock files** (`extensions.<editor>.lock`) pin versions in
  `publisher.name@version` format. Dual registry: OpenVSX primary, VS
  Marketplace fallback, `.vsix` download as last resort.
- **settings.json and keybindings.json** are large files (~1200+ lines each)
  organized with `// MARK:` comment sections. Search for `MARK:` to navigate.
- **Keybindings** follow Emacs conventions — heavy use of `ctrl+x` and `ctrl+c`
  chord prefixes.
- **Siren script** (bash): uses `set -o pipefail`, requires bash 4+ (assoc
  arrays), depends on `jq` and `curl`. Functions use `snake_case`.

## Scope

AI agent configurations (CLAUDE.md, commands, skills, cursor rules) are managed
in a separate repo ([jimeh/agentic](https://github.com/jimeh/agentic)). This
repo only handles editor settings, keybindings, extensions, and tool configs
(cspell, harper-ls, MCP).
