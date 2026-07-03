# Verification Gates

AI-OS treats verification as the decision maker.

## Verification pipeline

```mermaid
flowchart TD
    Change[Change] --> Build[Build]
    Build --> Typecheck[Typecheck]
    Typecheck --> Lint[Lint]
    Lint --> Unit[Unit Tests]
    Unit --> Integration[Integration Tests]
    Integration --> Security[Security Review]
    Security --> Performance[Performance Review]
    Performance --> Docs[Documentation Review]
    Docs --> Gate{All required gates passed?}
    Gate -- No --> Diagnose[Diagnose and Loop Back]
    Gate -- Yes --> Done[Done]
```

## Strong verifiers

- build
- typecheck
- lint
- unit tests
- integration tests
- smoke tests
- dependency audit
- container build
- infrastructure validation
- benchmark

## Weak verifiers

- self-review
- checklist review
- manual reading

Weak verifiers can support decisions, but they should not replace strong verifiers when strong verifiers are available.
