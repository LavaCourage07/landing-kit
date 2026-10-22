---
name: landing-trace
description: Trace a concrete user-visible behavior, request, event, state change, or failure through an unfamiliar codebase and its tests, data stores, jobs, and external services. Use to understand a cross-layer call chain, locate change points, explain error handling, or assess compatibility risk before implementation. Do not use for broad repository onboarding or unsupported architecture guesses.
---

# Landing Trace

Trace one behavior deeply enough to support a decision. Read `../../references/evidence-and-safety.md` before drawing conclusions.

## Inputs

Pin down the observable behavior or result, a starting clue if available, relevant inputs, expected output, and the depth needed. If the request names only a vague feature, find a real entry point before continuing.

## Workflow

1. Locate the real entry: UI route or event, public API, CLI command, message handler, scheduled job, library call, or test. Cite it.
2. Follow symbol references, imports, registrations, configuration, and tests. Prefer source navigation or exact search over filename assumptions.
3. Record each hop as caller → contract/data → callee, including path and symbol or line when practical.
4. Track transformations, validation, authorization, state ownership, caching, persistence, queues, asynchronous boundaries, and external calls only where they actually exist.
5. Follow success, empty, validation, permission, dependency-failure, retry, timeout, and cancellation paths that matter to the behavior.
6. Identify upstream callers, downstream consumers, compatibility constraints, test coverage, and likely change points. Separate observed runtime behavior from static reachability.
7. Run narrow, read-only or existing tests when useful and authorized. Do not mutate data or start production-facing operations merely to prove a trace.
8. Invoke `landing-map` for a sequence or flow map when three or more meaningful hops or branches would be clearer visually. Pass the evidence ledger, not an inferred narrative.

## Output

Provide:

- trace question and boundary;
- ordered happy-path chain;
- inputs, outputs, and data shape changes;
- state, permission, error, and asynchronous branches;
- file/symbol evidence index;
- tests and runtime observations actually performed;
- likely change points and compatibility risks;
- explicit inferences and unknowns.

## Completion standard

Complete only when the requested behavior is connected from a real entry to its material result, important branches are covered, each key hop has evidence, and static findings are not misreported as runtime proof.

## Failure and fallback

If generated code, reflection, dependency injection, or external services break the static chain, identify the last verified hop and the exact missing evidence. Use configuration and tests as secondary evidence. Ask for runtime access only when it would materially resolve the unknown; never fabricate the hidden segment.
