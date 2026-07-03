# Definition of Done

A task is done only when every required gate is satisfied.

## Required checks

- Goal is achieved.
- Acceptance criteria are satisfied.
- Work is implemented in the intended scope.
- Relevant verification was run.
- Security and performance were considered.
- Documentation was updated when behavior changed.
- Wiki navigation was updated when public docs changed.
- Rollback or revert path is known.
- Remaining work is documented.

## Done decision

```mermaid
flowchart TD
    Goal[Goal met?] --> A{Yes?}
    A -- No --> Work[Continue loop]
    A -- Yes --> Verify[Verifiers pass?]
    Verify -- No --> Work
    Verify -- Yes --> Docs[Docs updated?]
    Docs -- No --> Work
    Docs -- Yes --> Risk[Risk acceptable?]
    Risk -- No --> Human[Human review]
    Risk -- Yes --> Done[Done]
```
