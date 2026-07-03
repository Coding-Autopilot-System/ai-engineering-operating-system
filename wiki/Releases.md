# Releases

Canonical release docs are in VERSIONING.md and docs/ci-cd/release-process.md.

## Release flow

```mermaid
stateDiagram-v2
    [*] --> Freeze
    Freeze --> Verify
    Verify --> Approval
    Approval --> Tag: approved
    Approval --> Rework: rejected
    Rework --> Verify
    Tag --> Publish
    Publish --> Validate
    Validate --> [*]
```

## Pages

- VERSIONING.md
- CHANGELOG.md
- docs/ci-cd/release-process.md
