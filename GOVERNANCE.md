# Governance

AI-OS governance is based on explicit goals, human approval gates, verification evidence, and reversible change.

## Governance loop

```mermaid
flowchart TD
    Proposal[Proposal] --> Impact[Impact Analysis]
    Impact --> Risk[Risk Classification]
    Risk --> Plan[Implementation Plan]
    Plan --> Approval{Human Approval Required?}
    Approval -- Yes --> Human[Maintainer Approval]
    Approval -- No --> Implement[Implement]
    Human --> Implement
    Implement --> Verify[Verify]
    Verify --> Pass{Pass?}
    Pass -- No --> Rework[Rework]
    Rework --> Verify
    Pass -- Yes --> Record[Record Decision]
    Record --> Done[Done]
```

## Approval required

- Release process changes
- Security policy changes
- Governance changes
- Breaking changes to master prompt semantics
- Automation that can mutate repositories
- Anything that increases risk or cost

## Decision records

Use ADRs for structural decisions. ADRs must explain context, decision, alternatives, consequences, and rollback.
