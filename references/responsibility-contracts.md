# Skill responsibility contracts

| Skill | Owns | Delegates to | Must not claim |
| --- | --- | --- | --- |
| `landing-scan` | Broad first orientation, commands, component inventory, initial maps | `landing-map`; suggests `landing-trace` | Exhaustive comprehension or verified commands it did not run |
| `landing-map` | Evidence-backed visual representation and renderer fallback | Installed Archify; Mermaid fallback | Unsupported relationships or interactive output from Mermaid alone |
| `landing-trace` | One behavior's entry-to-result chain and branches | `landing-map` for complex flow | Runtime execution from static references alone |
| `landing-change` | Acceptance, impact, minimal authorized implementation | `landing-trace`, Superpowers, `landing-verify` | Completion before verification or authorization for release actions |
| `landing-verify` | Risk-based checks, diff review, evidence classification | Superpowers practices; recommends `landing-capture` | Passed tests that were skipped or behavior from build success alone |
| `landing-capture` | Minimal durable documentation update | `landing-map`; optional Xiaohei | Speculation as fact or permission to upload private material |

## Routing examples

- “What is this repository and how do I run it?” → `landing-scan`.
- “Draw the actual service dependencies.” → `landing-map`.
- “What happens after this button is clicked?” → `landing-trace`.
- “Add this endpoint without disturbing my local changes.” → `landing-change`.
- “Are these changes really done?” → `landing-verify`.
- “Document what we just confirmed.” → `landing-capture`.

Use the narrowest matching Skill. A complex implementation may intentionally chain several contracts, but a simple question should not trigger the entire lifecycle.
