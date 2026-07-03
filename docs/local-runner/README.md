# Local Runner

The local runner is the future executable layer of AI-OS.

## Runner loop

```mermaid
flowchart TD
    A[Goal] --> B[Load context]
    B --> C[Select loop]
    C --> D[Work step]
    D --> E[Check result]
    E --> F{Pass?}
    F -- No --> G[Feedback]
    G --> D
    F -- Yes --> H[Report]
```

## Minimum responsibilities

- read repository context
- select task loop
- run verifier commands
- capture evidence
- pause at approval gates
- update memory files

## First version

The first version can be a simple command-line wrapper.
