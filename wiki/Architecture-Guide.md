# Architecture Guide

Canonical architecture docs are in docs/architecture.

## Overview

```mermaid
flowchart TD
    A[Goal] --> B[Loop Router]
    B --> C[Specialist Agents]
    C --> D[Verification Gates]
    D --> E{Done?}
    E -- No --> B
    E -- Yes --> F[Docs and Memory]
```

## Pages

- docs/architecture/README.md
- docs/architecture/fan-out-fan-in.md
- docs/methodology/continuous-improvement-loop.md
