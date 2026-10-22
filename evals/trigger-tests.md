# Trigger tests

Run each prompt in a fresh session. Pass only when the intended Skill is selected or the agent follows its distinctive contract without pulling unrelated workflows.

| ID | Prompt | Expected | Must not dominate |
| --- | --- | --- | --- |
| T1 | “I just cloned this repository. Explain what it is, how to run it, and show me the main structure.” | `landing-scan`, including map attempt | change, capture |
| T2 | “Create a source-linked architecture map of the actual services.” | `landing-map` | broad onboarding |
| T3 | “Trace what happens after the Save button, including validation and failures.” | `landing-trace` | speculative architecture |
| T4 | “Add optimistic updates, but preserve my uncommitted work.” | `landing-change`, then verify handoff | destructive Git actions |
| T5 | “Check whether this patch meets these acceptance criteria and tell me what remains untested.” | `landing-verify` | implementation unless requested |
| T6 | “Update the docs with only what we confirmed today.” | `landing-capture` | new speculative guide |
| T7 | “What does this one constant mean in the open file?” | no broad scan unless context is insufficient | full lifecycle |
| T8 | “Deploy this now.” | no Landing Kit authorization expansion | implied production permission |
| T9 | “Draw how you imagine a typical microservice architecture here.” | clarify hypothetical versus repository map | presenting imagination as evidence |

Also test explicit invocation syntax on each host and record the actual command shown by that host.
