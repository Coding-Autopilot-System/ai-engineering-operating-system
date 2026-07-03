# Local-first Model Routing Policy

AI-OS prefers local or cheaper models for low-risk work and escalates only when needed.

## Routing loop

```mermaid
flowchart TD
    Task[Task] --> Risk{Risk level}
    Risk -- Low --> Local[Local or small model]
    Risk -- Medium --> Medium[Medium model]
    Risk -- High --> Strong[Strong model]
    Local --> Verify[Verifier]
    Medium --> Verify
    Strong --> Verify
    Verify --> Confidence{Enough confidence?}
    Confidence -- No --> Escalate[Escalate]
    Escalate --> Verify
    Confidence -- Yes --> Done[Done]
```

## Guidance

- Use local models for summaries, search, boilerplate, and formatting.
- Use stronger models for architecture, security, hard debugging, and final review.
- Escalate only when confidence is low or risk is high.
