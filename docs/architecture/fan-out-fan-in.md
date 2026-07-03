# Fan-out and Fan-in Orchestration

AI-OS uses specialist roles to reduce blind spots.

## Pattern

```mermaid
flowchart LR
    Goal[Goal] --> Orchestrator[Orchestrator]
    Orchestrator --> Planner[Planner]
    Orchestrator --> Architect[Architect]
    Orchestrator --> Security[Security]
    Orchestrator --> Tester[Tester]
    Orchestrator --> Writer[Writer]
    Planner --> Merge[Fan-in synthesis]
    Architect --> Merge
    Security --> Merge
    Tester --> Merge
    Writer --> Merge
    Merge --> Plan[Plan]
    Plan --> Human{Human review?}
    Human -- Yes --> Approval[Approval]
    Human -- No --> Execute[Execute]
    Approval --> Execute
```

## Roles

- Planner: scope, steps, dependencies, risks
- Architect: system fit, interfaces, long-term shape
- Security: threat model and approval gates
- Tester: verifiers and evidence
- Writer: docs, examples, wiki, changelog

## Rule

The final plan must synthesize all specialist outputs into one coherent path. Disagreements should be documented as tradeoffs.
