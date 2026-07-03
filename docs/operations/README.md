# Operations

Operations pages describe how to keep AI-OS healthy after publication.

## Operating loop

```mermaid
flowchart TD
    A[Change] --> B[Run repository verifier]
    B --> C[Run tests]
    C --> D[Sync wiki]
    D --> E[Review platform settings]
    E --> F[Publish or report]
```

## Routine checks

- CI docs workflow is green.
- Wiki sync workflow has run after wiki source changes.
- Open dependency PRs are reviewed.
- Release environment still requires review.
- Repository description and topics match the project purpose.
- README links still work.
