# jimeh's VSCode configuration (vscode-siren)

This is my personal configuration for [VSCode][] and VSCode-based editors like
[Cursor][] and [Windsurf][], and is heavily geared towards recreating the text
editor experience I have in Emacs with [my config][emacs-siren].

The "vscode-siren" nickname is based on the the "Emacs Siren" nickname of my
Emacs config.

Focus has primarily been around using this with Cursor, but does work in
Windsurf and regular VSCode as well.

[VSCode]: https://code.visualstudio.com/
[Cursor]: https://www.cursor.com/
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
default profile of VSCode-based editors, and also manage their installed
extensions via lock files.

```bash
./siren --help
```
```
Usage: siren EDITOR COMMAND [OPTIONS]

Editors:
  cursor, c                   Cursor editor
  vscode, code, vsc, v        Visual Studio Code
  vscode-insiders, vsci, i    Visual Studio Code Insiders
  windsurf, surf, w           Windsurf editor

Commands:
  config, conf             Create symlinks for editor config files
  dump-extensions, dump    Export installed editor extensions to a lock file.
  extensions, ext          Install editor extensions from a lock file.

Options:
  --latest                 When used with the extensions command, installs the
                           latest version of each extension instead of the
                           exact version from the lock file.

Description:
  This script manages editor configuration files and extensions.
  It can create symlinks for settings, keybindings, and snippets,
  as well as dump extension lock files and install extensions from them.
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
