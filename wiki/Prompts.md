# Prompts

Canonical prompt docs are in prompts.

## Recommended prompts

- prompts/master-system-prompt.md
- prompts/chatgpt-web.md
- prompts/feature.md
- prompts/bugfix.md
- prompts/continuous-improvement.md

## Prompt loop

```mermaid
flowchart TD
    Prompt[Prompt] --> Context[Load context]
    Context --> Loop[Select loop]
    Loop --> Plan[Plan]
    Plan --> Act[Act]
    Act --> Verify[Verify]
    Verify --> Done{Done?}
    Done -- No --> Loop
    Done -- Yes --> Report[Report]
```
