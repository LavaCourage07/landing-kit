# Evidence and safety rules

Apply these rules across all Landing Kit skills.

## Evidence classes

- **Confirmed:** directly supported by source, configuration, tests, a successful command, or an observed runtime result.
- **Inferred:** a reasoned conclusion with supporting clues but without direct confirmation. State the reasoning and what would confirm it.
- **Unknown:** material information that is missing, inaccessible, conflicting, or outside the selected scope.

Use paths and symbols for important claims. Use line numbers when stable and helpful, but do not make exact line numbers the only durable reference. A manifest proves declaration, not runtime use. Static reachability proves a possible call path, not that production exercised it.

## Worktree safety

1. Read repository instructions before editing.
2. Inspect Git status and relevant diffs before and after work.
3. Treat all pre-existing changes and untracked files as user work.
4. Do not reset, clean, stash, discard, overwrite, stage, commit, push, deploy, migrate, or delete unless the task authorizes that action.
5. Avoid broad formatting and unrelated cleanup.
6. Ask before dependency installation, destructive operations, external writes, or actions that can expose private source or data.

## Verification language

Distinguish:

- documented command from executed command;
- command success from behavior success;
- mocked/sandboxed evidence from live integration evidence;
- generated artifact from opened or visually inspected artifact;
- skipped test from passed test.

Report exact blockers and the closest safe evidence without calling it equivalent.

## Dependency discovery

Check the host's advertised skills, tools, plugin manager, and current official mechanism. A missing guessed folder is not proof that a dependency is unavailable. Never install a third-party dependency without user approval.
