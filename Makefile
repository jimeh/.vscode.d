# List of supported editors
EDITORS := antigravity cursor vscode vscode-insiders windsurf

.PHONY: antigravity-config
antigravity-config:
	./siren antigravity config

.PHONY: antigravity-extensions
antigravity-extensions:
	./siren antigravity extensions

.PHONY: antigravity-dump-extensions
antigravity-dump-extensions:
	./siren antigravity dump-extensions

.PHONY: cursor-config
cursor-config:
	./siren cursor config

.PHONY: cursor-extensions
cursor-extensions:
	./siren cursor extensions

.PHONY: cursor-dump-extensions
cursor-dump-extensions:
	./siren cursor dump-extensions

.PHONY: vscode-config
vscode-config:
	./siren vscode config

.PHONY: vscode-extensions
vscode-extensions:
	./siren vscode extensions

.PHONY: vscode-dump-extensions
vscode-dump-extensions:
	./siren vscode dump-extensions

.PHONY: vscode-insiders-config
vscode-insiders-config:
	./siren vscode-insiders config

.PHONY: vscode-insiders-extensions
vscode-insiders-extensions:
	./siren vscode-insiders extensions

.PHONY: vscode-insiders-dump-extensions
vscode-insiders-dump-extensions:
	./siren vscode-insiders dump-extensions

.PHONY: windsurf-config
windsurf-config:
	./siren windsurf config

.PHONY: windsurf-extensions
windsurf-extensions:
	./siren windsurf extensions

.PHONY: windsurf-dump-extensions
windsurf-dump-extensions:
	./siren windsurf dump-extensions

# Convenience targets for all editors
.PHONY: all-config all-extensions
all-config: $(addsuffix -config,$(EDITORS))
all-extensions: $(addsuffix -extensions,$(EDITORS))
all-dump-extensions: $(addsuffix -dump-extensions,$(EDITORS))
