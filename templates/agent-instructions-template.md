# Agent Instructions Template

Use this file as `AGENTS.md` in a target repository.

## Operating model

Follow AI Engineering Operating System.

```mermaid
flowchart TD
    A[Goal] --> B[Load context]
    B --> C[Select loop]
    C --> D[Plan]
    D --> E[Work]
    E --> F[Verify]
    F --> G{Done?}
    G -- No --> C
    G -- Yes --> H[Report]
```

## Required behavior

- Read repository context before editing.
- Select the appropriate loop.
- Plan before implementation.
- Keep changes small and reversible.
- Run available verifiers.
- Update docs when behavior changes.
- Report evidence honestly.

## Repository-specific commands

```text
Build:
Test:
Lint:
Security:
Docs:
```
