# Prompt Quality

Prompt quality in AI-OS is measured by whether the prompt produces safe, verifiable engineering behavior.

## Quality loop

```mermaid
flowchart TD
    A[Prompt] --> B[Run task]
    B --> C[Collect output]
    C --> D[Check evidence]
    D --> E{Good?}
    E -- No --> F[Improve prompt]
    F --> B
    E -- Yes --> G[Keep]
```

## Quality criteria

- goal is clear
- loop is selected
- plan appears before work
- verifier evidence is included
- risks are explicit
- docs are updated when needed
- remaining work is stated
