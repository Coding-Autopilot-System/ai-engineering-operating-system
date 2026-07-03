# Pipeline Repair Loop

```mermaid
flowchart TD
    A[Pipeline not green] --> B[Read logs]
    B --> C[Classify]
    C --> D[Cause]
    D --> E[Small patch]
    E --> F[Local check]
    F --> G[Pipeline check]
    G --> H{Green?}
    H -- No --> B
    H -- Yes --> I[Done]
```

## Classes

- build
- lint
- test
- dependency
- environment
- permission
- timeout
- configuration

## Evidence

Record the job name, cause, files changed, and verification result.
