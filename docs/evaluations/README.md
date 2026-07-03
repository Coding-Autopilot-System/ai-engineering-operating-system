# Evaluations

Evaluations prove that AI-OS improves work quality instead of only adding process.

## Evaluation loop

```mermaid
flowchart TD
    Task[Task] --> Baseline[Run without AI-OS]
    Baseline --> AIOS[Run with AI-OS]
    AIOS --> Score[Score outcomes]
    Score --> Compare[Compare]
    Compare --> Improve[Improve prompt or loop]
    Improve --> Task
```

## Suggested metrics

- goal completion
- verifier pass rate
- number of recovery loops
- documentation completeness
- security review completeness
- time to usable result
- number of unverified claims
- human approval correctness

## First eval set

- feature documentation task
- bugfix reasoning task
- CI failure triage task
- release checklist task
- wiki sync task
