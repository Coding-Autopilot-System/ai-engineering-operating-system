# AGENTS.md

All AI coding agents working in this repository must follow AI Engineering Operating System.

## Required loop

```mermaid
flowchart TD
    A[Goal] --> B[Load context]
    B --> C[Plan]
    C --> D[Work]
    D --> E[Verify]
    E --> F{Done?}
    F -- No --> D
    F -- Yes --> G[Report]
```

## Agent rules

- Load context before editing.
- Plan before implementation.
- Work in small reversible steps.
- Verify with available tools.
- Update docs and wiki sources when public docs change.
- Report evidence honestly.
