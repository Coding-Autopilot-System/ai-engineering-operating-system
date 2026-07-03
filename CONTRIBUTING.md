# Contributing

AI-OS contributions must improve clarity, safety, repeatability, or verification.

## Contribution loop

```mermaid
flowchart TD
    Idea[Idea] --> Issue[Open Issue]
    Issue --> Plan[Write Plan]
    Plan --> Approval{Maintainer Approval Needed?}
    Approval -- Yes --> Review[Human Review]
    Approval -- No --> Branch[Create Branch]
    Review --> Branch
    Branch --> Change[Make Small Change]
    Change --> Verify[Run Verifiers]
    Verify --> Pass{Passed?}
    Pass -- No --> Fix[Fix and Re-run]
    Fix --> Verify
    Pass -- Yes --> PR[Open PR]
    PR --> Done[Review and Merge]
```

## Required for PRs

- Clear goal
- Scope and non-goals
- Verification evidence
- Updated docs when behavior changes
- Mermaid diagrams for new workflows
- Human approval for broad governance, release, or security changes

## Canonical source

The `/docs` tree is canonical. Wiki pages are curated navigation pages that point back to canonical docs.
