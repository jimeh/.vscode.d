# Task: Convert CLAUDE.md to AGENTS.md

Convert this project's `CLAUDE.md` into an `AGENTS.md` file, and replace
`CLAUDE.md` with a thin reference to it.

## Steps

1. **Verify preconditions**:
   - Confirm `CLAUDE.md` exists in the project root. If not, abort with an error
     message.
   - Confirm `AGENTS.md` does NOT already exist in the project root. If it does,
     abort — suggest using it directly or removing it first.

2. **Read `CLAUDE.md`** content in full.

3. **Review content for references that need updating**:

   **Filename references**:
   - Headings like `# CLAUDE.md` → `# AGENTS.md`
   - Self-references like "this CLAUDE.md file" → "this AGENTS.md file"
   - Any other mentions of the filename that refer to the file itself and should
     change to reflect the new name

   **Generalize Claude-specific agent language**:
   - The title and opening paragraph often describe the file's purpose in
     Claude-specific terms (e.g., "This file provides guidance to Claude...").
     Rewrite these to be generic (e.g., "This file provides guidance to LLM
     agents...").
   - "Claude" (when referring to the AI agent performing tasks) → "LLM agents"
     or "agents"
   - "Tell Claude to..." → "Instruct agents to..."
   - "Claude should..." → "Agents should..."
   - "When Claude encounters..." → "When agents encounter..."
   - Similar phrasing that assumes a specific AI agent — rewrite to be
     agent-agnostic

   **Do NOT change**:
   - "Claude Code" — it's a proper product name (CLI tool)
   - References to Claude Code features, documentation, or capabilities (e.g.,
     `@`-references, slash commands)
   - "Claude" as part of a filename or path (e.g., `.claude/`, `CLAUDE.md`
     referring to other projects)
   - References to CLAUDE.md that refer to other projects' files or external
     concepts

4. **Write `AGENTS.md`** with the updated content.

5. **Replace `CLAUDE.md`** contents with just:
   ```
   @AGENTS.md
   ```
   This makes Claude Code load `AGENTS.md` via the `@`-reference.

6. **Summary**: Report what was done, including any references that were updated
   in step 3.
