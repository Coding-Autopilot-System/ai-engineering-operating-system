# Architecture

AI-OS is designed as a local-first operating model for AI coding agents.

## Reference architecture

```mermaid
flowchart TD
    User[User Goal] --> Router[Task Router]
    Router --> Context[Context Loader]
    Context --> Repo[Repository]
    Context --> Memory[Project Memory]
    Router --> Orchestrator[Loop Orchestrator]
    Orchestrator --> Planner[Planner]
    Orchestrator --> Architect[Architect]
    Orchestrator --> Coder[Coder]
    Orchestrator --> Tester[Tester]
    Orchestrator --> Reviewer[Reviewer]
    Orchestrator --> Writer[Documentation Writer]
    Coder --> Tools[Local Tools]
    Tester --> Tools
    Tools --> Verifiers[Build Test Lint Scan]
    Verifiers --> Gate{Goal Met?}
    Gate -- No --> Orchestrator
    Gate -- Yes --> Done[Done]
```

## Core components

- Task router
- Context loader
- Loop orchestrator
- Specialist agents
- Tool adapters
- Verifier gates
- Memory updater
- Human approval gate

## Design goals

- local-first
- model-agnostic
- auditable
- repeatable
- safe by default
- useful for real repositories
