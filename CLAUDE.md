# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## Project Overview

This is a personal VSCode configuration repository (vscode-siren) that provides
a unified configuration for VSCode-based editors including Cursor, VSCode,
VSCode Insiders, and Windsurf. It focuses on recreating an Emacs-like text
editor experience with custom keybindings, settings, and extensions.

## Key Commands

### Configuration Management

- `./siren <editor> config` - Create symlinks for editor config files
- `./siren <editor> extensions` - Install extensions from lock file
- `./siren <editor> extensions --latest` - Install latest versions of extensions
- `./siren <editor> dump-extensions` - Export installed extensions to lock file

### Makefile Shortcuts

- `make cursor-config` - Configure Cursor editor
- `make cursor-extensions` - Install Cursor extensions
- `make all-config` - Configure all editors
- `make all-extensions` - Install extensions for all editors

### Supported Editors

- `cursor` (c) - Cursor editor
- `vscode` (code, vsc, v) - Visual Studio Code
- `vscode-insiders` (vsci, i) - Visual Studio Code Insiders
- `windsurf` (surf, w) - Windsurf editor

## Architecture

### Core Components

- **siren script** - Main configuration management tool (bash script)
- **settings.json** - VSCode settings configuration
- **keybindings.json** - Custom keybindings (Emacs-inspired)
- **snippets/** - Code snippets for Go and Ruby
- **extensions.*.lock** - Extension lock files for each editor

### Configuration Structure

- Config files are symlinked to appropriate editor directories based on OS
- Extensions are managed via lock files with version pinning
- Cursor uses .vsix installation due to signature verification issues
- Static symlinks for additional files like cspell dictionary and MCP config

### Key Features

- Cross-platform support (macOS/Linux)
- Version-locked extensions with fallback to .vsix downloads
- Automatic backup of existing configurations
- Emacs-inspired keybindings and workflow
- Dark/light theme switching based on system preferences

## Development Guidelines

Based on cursor/user-rules.md:

- Keep line length to 80 characters when possible
- Check Makefile for common project tasks
- Be direct and terse in communication
- Provide code solutions rather than general advice
- Include robust error handling
- Consider cross-platform compatibility
- Respect existing code comments
