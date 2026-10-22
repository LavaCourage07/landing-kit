---
name: landing-scan
description: Inspect an unfamiliar software repository and produce an evidence-backed project overview, local development guide, directory index, and visual map. Use when onboarding to a codebase, asking how a repository works or runs, or establishing a verified baseline before tracing or changing code. Do not use for a narrow known-file question or as a substitute for implementing an already-understood change.
---

# Landing Scan

Build a bounded, evidence-backed orientation to an unfamiliar repository. Read `../../references/evidence-and-safety.md` before scanning. Read `../../references/dependencies.md` only when checking the map dependency.

## Inputs

Establish the repository root, the user's goal, the requested depth, and whether the result should be returned in chat or written to the repository. If the goal is broad, scan for first-day onboarding rather than attempting exhaustive comprehension.

## Workflow

1. Inspect repository instructions, Git status, top-level structure, README files, manifests, lockfiles, workspace configuration, build files, CI, and existing architecture or development documentation. Preserve all existing changes.
2. Inventory files with bounded searches. Exclude generated output, vendored dependencies, caches, and large binaries unless the task specifically concerns them.
3. Identify languages, frameworks, package/build tools, runtime entry points, applications, tests, and documented commands from direct evidence. Do not treat a dependency declaration as proof that a feature is used at runtime.
4. Determine the components that actually exist—such as UI, API, workers, storage, infrastructure, or external services—from imports, configuration, routes, startup code, or tests. Do not impose a standard architecture.
5. Sample important directories and trace enough references to explain their responsibilities. Mark each material conclusion as confirmed, inferred, or unknown.
6. Invoke `landing-map` when it is available, passing the confirmed findings and evidence. A first scan must include at least a system/context map and a key-directory map. If it cannot be invoked, apply its Mermaid fallback rules and state that the interactive map was not produced.
7. Extract exact setup, run, build, lint, and test commands only from repository evidence. If a command was not executed, label it "documented" or "discovered", not "verified".
8. Report conflicts, stale documentation, missing prerequisites, and focused questions that would unlock further work.

## Output

Provide:

- scope and evidence reviewed;
- project purpose and technical stack;
- actual component boundaries and entry points;
- key-directory and file index with source paths;
- documented versus executed local commands;
- map or map link plus its evidence status;
- confirmed facts, reasoned inferences, and unknowns;
- recommended next step, usually a focused `landing-trace`.

Write files only when the user requested persistent documentation or repository instructions require it. Otherwise return the scan in the response.

## Completion standard

Complete only when the main claims cite repository evidence, important commands are labeled by execution status, both required maps exist in some form, the Git worktree remains protected, and unknowns are explicit. A directory listing alone is not a completed scan.

## Failure and fallback

If the repository is too large, explain the sampling boundary and prioritize entry points and the user's likely task. If source access is incomplete, report the inaccessible area. If Archify is absent or fails, do not install it without approval; produce Mermaid and preserve the failed command or error summary.
