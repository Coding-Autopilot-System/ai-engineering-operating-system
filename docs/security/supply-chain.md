# Supply Chain Security

AI-OS treats workflows, dependencies, prompts, and tool access as part of the supply chain.

## Supply chain loop

```mermaid
flowchart TD
    Change[Dependency or workflow change] --> Review[Review diff]
    Review --> Scan[Scan]
    Scan --> Risk[Risk classify]
    Risk --> Approve{Approval needed?}
    Approve -- Yes --> Human[Maintainer review]
    Approve -- No --> Merge[Merge]
    Human --> Merge
    Merge --> Monitor[Monitor alerts]
```

## Controls

- Dependabot configuration
- dependency review workflow
- secret scanning
- CodeQL for future scripts
- protected release workflow
- documented SBOM/provenance guidance
