# Codex marketplace installation result

Date: 2026-10-22

Marketplace source during test: local checkout at `/Users/xinao/Documents/project005/landing-kit`

Plugin source resolved by the marketplace: `https://github.com/LavaCourage07/landing-kit.git`, branch `main`

## Procedure

1. Confirmed no `landing-kit` marketplace or plugin was already configured.
2. Registered the checkout with `codex plugin marketplace add <checkout> --json`.
3. Installed with `codex plugin add landing-kit@landing-kit --json`.
4. Inspected the cached plugin manifest and Skill inventory.
5. Ran Plugin Creator validation against the installed cache.
6. Removed the plugin and marketplace to restore the original local Codex configuration.

## Observed result

- Installed plugin ID: `landing-kit@landing-kit`.
- Installed version: `0.1.0`.
- Installed cache contained `landing-capture`, `landing-change`, `landing-map`, `landing-scan`, `landing-trace`, and `landing-verify`.
- Plugin Creator validation passed on the installed cache.
- Temporary plugin and marketplace removal succeeded.

## Boundary

The catalog was loaded from the local checkout while the plugin itself was fetched from the remote `main` branch. This proves the marketplace entry can resolve and install the remote plugin. After publishing the catalog, a separate clean-machine or clean-profile test should verify the public `LavaCourage07/landing-kit` marketplace-add command end to end.
