# Task: Convert CLAUDE.md to AGENTS.md

Convert this project's `CLAUDE.md` into an `AGENTS.md` file, and
replace `CLAUDE.md` with a thin reference to it.

## Steps

1. **Verify preconditions**:
   - Confirm `CLAUDE.md` exists in the project root. If not, abort
     with an error message.
   - Confirm `AGENTS.md` does NOT already exist in the project root.
     If it does, abort — suggest using it directly or removing it
     first.

2. **Read `CLAUDE.md`** content in full.

3. **Review content for references that need updating**:
   - Headings like `# CLAUDE.md` → `# AGENTS.md`
   - Self-references like "this CLAUDE.md file" →
     "this AGENTS.md file"
   - Any other mentions of the filename that refer to the file
     itself and should change to reflect the new name
   - Do NOT change references to CLAUDE.md that refer to other
     projects' files, Claude Code documentation, or external
     concepts

4. **Write `AGENTS.md`** with the updated content.

5. **Replace `CLAUDE.md`** contents with just:
   ```
   @AGENTS.md
   ```
   This makes Claude Code load `AGENTS.md` via the `@`-reference.

6. **Summary**: Report what was done, including any references that
   were updated in step 3.
