# Quickstart

Use this page to apply AI-OS to any repository.

## Quickstart loop

```mermaid
flowchart TD
    A[Choose task] --> B[Read AGENTS.md]
    B --> C[Load project context]
    C --> D[Select loop]
    D --> E[Plan]
    E --> F[Work in increments]
    F --> G[Verify]
    G --> H{Done?}
    H -- No --> F
    H -- Yes --> I[Report]
```

## Minimal prompt

```text
Execute AI-OS.
Task: [describe task]
Load context, choose the loop, plan, work, verify, and report evidence.
```

## First repository setup

1. Add `AGENTS.md`.
2. Add project context.
3. Add verifier commands.
4. Add loop-specific prompts.
5. Add CI checks.
