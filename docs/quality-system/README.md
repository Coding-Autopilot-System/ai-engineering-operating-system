# Quality System

AI-OS quality is based on evidence, not confidence.

## Quality loop

```mermaid
flowchart TD
    A[Change] --> B[Structure check]
    B --> C[Link check]
    C --> D[Diagram check]
    D --> E[Policy check]
    E --> F{Pass?}
    F -- No --> G[Improve]
    G --> B
    F -- Yes --> H[Ready]
```

## Quality gates

- required files exist
- Markdown files have titles
- key docs include Mermaid diagrams
- relative links resolve
- work-marker text is not left in docs
- CI can run the verifier
