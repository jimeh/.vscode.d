# jimeh's VSCode configuration (vscode-siren)

This is my personal configuration for [VSCode][] and VSCode-based editors like
[Cursor][], [Antigravity][], and [Windsurf][], and is heavily geared towards
recreating the text editor experience I have in Emacs with [my
config][emacs-siren].

The "vscode-siren" nickname is based on the the "Emacs Siren" nickname of my
Emacs config.

Focus has primarily been around using this with Cursor, but does work in
Windsurf and regular VSCode as well.

[Antigravity]: https://antigravity.google/
[Cursor]: https://www.cursor.com/
[VSCode]: https://code.visualstudio.com/
[Windsurf]: https://codeium.com/windsurf
[emacs-siren]: https://github.com/jimeh/.emacs.d

## Features

- **Emacs-ish inspired keybindings** - Based on the configuration from
  [emacs-siren][], which is my personal highly customized Emacs configuration.
- **Modern UI** - Customized window behavior with native macOS tabs, allowing
  for a single-window multi-workspace experience with accompanying keybindings.
- **Automatic dark/light theme switching** - Dark theme (One Dark Pro) and light
  theme (Solarized Light) with automatic switching based on system preferences.
- **Custom snippets** - Some pre-configured snippets for Go and Ruby.

## Installation

Clone this repository to your preferred location:

```bash
git clone https://github.com/jimeh/.vscode.d.git ~/.config/vscode-siren
```

## Setup

The included `siren` script is a helper to symlink configuration files into the
default profile of VSCode-based editors, and manage their installed
extensions via lock files.

```bash
./siren --help
```

```
Usage:
  siren EDITOR COMMAND [OPTIONS]
  siren COMMAND EDITOR [OPTIONS]
  siren config
  siren shared-extensions [--json] [EDITORS...]

Editors:
  antigravity, agy, a         Antigravity editor (prefers OpenVSX)
  cursor, c                   Cursor editor
  kiro, k                     Kiro editor (uses OpenVSX by default)
  vscode, code, vsc, v        Visual Studio Code
  vscode-insiders, vsci, i    Visual Studio Code Insiders
  windsurf, surf, w           Windsurf editor

Commands:
  config, conf             Create symlinks.
                           With editor: full editor + static config.
                           Without editor: static-only symlinks.
  dump-extensions, dump    Export installed extensions to lock file
                           for the specified editor.
  extensions, ext          Install extensions from lock file for the
                           specified editor.
  install                  Install a specific extension id for the
                           specified editor (e.g. ms-python.python).
  shared-extensions, shared
                           Print extensions present in all specified editors.
                           Defaults: cursor, vscode. Use --json for JSON.

Options:
  --latest                 With 'extensions': install latest versions instead
                           of exact lockfile versions. With 'install': install
                           the latest version of the specified extension.
  --force-latest           Force latest behavior where applicable.

Notes:
  - For 'dump', 'extensions', and 'install', the editor may be given as
    arg 1 or arg 2; both orders are supported.
  - Kiro prefers OpenVSX, falling back to VS Marketplace.
```

In examples below, we will be using `cursor` as the editor.

### Symlink config files to Default profile

```bash
./siren cursor config
```

### Install Extensions

This will install all extensions from the `extensions.<EDITOR>.lock` file:

```bash
./siren cursor extensions
```

Or if you want install the latest versions rather than those from the lock file:

```bash
./siren cursor extensions --latest
```

### Update extensions lock file

To dump the current list of installed extensions to a lock file, run:

```bash
./siren cursor dump-extensions
```
