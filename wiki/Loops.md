# Loops

Canonical loop docs are in docs/loops.

## Loop map

```mermaid
flowchart TD
    Task[Task] --> Type{Type}
    Type -- Feature --> Feature[Feature loop]
    Type -- Bug --> Bug[Bug loop]
    Type -- Pipeline --> Pipe[Pipeline loop]
    Type -- Security --> Sec[Security loop]
    Type -- Release --> Rel[Release loop]
    Type -- Improvement --> Improve[Improvement loop]
```

## Pages

- docs/loops/README.md
- docs/loops/feature.md
- docs/loops/bugfix-loop.md
- docs/loops/pipeline-repair.md
- docs/loops/security.md
- docs/loops/release.md
