---
allowed-tools: Bash(git checkout --branch:*), Bash(git branch:*), Bash(git add:*), Bash(git diff:*), Bash(git status:*), Bash(git push:*), Bash(git commit:*), Bash(gh pr create:*)
description: Commit, push, and open a PR, rename branch appropriately if needed
source: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/commit-commands/commands/commit-push-pr.md
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- PR template (if exists): !`cat .github/PULL_REQUEST_TEMPLATE.md 2>/dev/null || echo "No PR template found"`

## Your Task

Based on the above changes:

1. Create a new branch if on main or master. If already on a non-main/master
   branch, check if the branch name looks randomly generated (e.g. UUIDs, hex
   strings, meaningless character sequences, or 1-3 random unrelated words like
   "brave-fox" or "purple-mountain") rather than descriptive of the changes. If
   so, rename it to something that aligns with the changes using:
   `git branch -m <new-name>`.
2. Create a single commit with an appropriate message. If asked to commit only
   staged changes, run `git diff --staged` to see exactly what is staged, and
   base the commit message solely on those changes. Do NOT stage additional
   files. Otherwise, stage all relevant changes.
3. Push the branch to origin
4. Create a pull request using `gh pr create`. If a PR template exists in the
   context above, use it as the base for the PR body and fill in the sections
   appropriately based on the changes.
5. You have the capability to call multiple tools in a single response. You MUST
   do all of the above in a single message. Do not use any other tools or do
   anything else. Do not send any other text or messages besides these tool
   calls.
