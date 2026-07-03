# Mermaid Diagram Catalog

This catalog documents the AI Engineering Operating System using Mermaid diagrams.

## 1. Full AI-OS lifecycle

```mermaid
flowchart TD
    Goal[User or Issue Goal] --> Context[Load Repository Context]
    Context --> Understand[Understand Goal]
    Understand --> Discover[Discover Existing System]
    Discover --> Analyze[Analyze Impact]
    Analyze --> Plan[Plan Small Reversible Steps]
    Plan --> Design[Design Simple Safe Solution]
    Design --> Risk[Risk Review]
    Risk --> Implement[Implement Increment]
    Implement --> Review[Self Review]
    Review --> Verify[Verification Gates]
    Verify --> Passed{All gates passed?}
    Passed -- No --> Diagnose[Diagnose Failure]
    Diagnose --> Return[Return To Earliest Failing Phase]
    Return --> Analyze
    Passed -- Yes --> Document[Update Documentation]
    Document --> Memory[Update Memory]
    Memory --> Retro[Retrospective]
    Retro --> Done[Done]
```

## 2. Universal loop

```mermaid
flowchart TD
    A[Goal] --> B[Analyze]
    B --> C[Plan]
    C --> D[Implement]
    D --> E[Verify]
    E --> F{Verifier passed?}
    F -- No --> G[Diagnose]
    G --> H[Fix root cause]
    H --> E
    F -- Yes --> I{Goal met?}
    I -- No --> C
    I -- Yes --> J[Complete]
```

## 3. Fan-out and fan-in agents

```mermaid
flowchart LR
    Orchestrator[Orchestrator] --> Planner[Planner]
    Orchestrator --> Architect[Architect]
    Orchestrator --> Coder[Coder]
    Orchestrator --> Tester[Tester]
    Orchestrator --> Reviewer[Reviewer]
    Orchestrator --> Docs[Docs]
    Planner --> FanIn[Fan-in Synthesis]
    Architect --> FanIn
    Coder --> FanIn
    Tester --> FanIn
    Reviewer --> FanIn
    Docs --> FanIn
    FanIn --> Gate{Decision Gate}
    Gate -- Continue --> Orchestrator
    Gate -- Done --> Done[Done]
```

## 4. Feature development loop

```mermaid
flowchart TD
    Story[Feature Goal] --> AC[Acceptance Criteria]
    AC --> Pattern[Find Existing Patterns]
    Pattern --> Design[Design Smallest Change]
    Design --> Tests[Create or Update Tests]
    Tests --> Code[Implement]
    Code --> Verify[Run Verifiers]
    Verify --> Pass{Pass?}
    Pass -- No --> Diagnose[Diagnose and Fix]
    Diagnose --> Code
    Pass -- Yes --> Docs[Update Docs]
    Docs --> PR[Ready for PR]
```

## 5. Bug fix loop

```mermaid
flowchart TD
    Bug[Bug Report] --> Repro[Reproduce]
    Repro --> FailingTest[Create Failing Test]
    FailingTest --> RootCause[Root Cause Analysis]
    RootCause --> Fix[Minimal Fix]
    Fix --> Verify[Run Regression Tests]
    Verify --> Pass{Fixed?}
    Pass -- No --> RootCause
    Pass -- Yes --> Done[Done]
```

## 6. CI/CD repair loop

```mermaid
flowchart TD
    Fail[CI Failure] --> Logs[Fetch Logs]
    Logs --> Classify[Classify Failure]
    Classify --> Cause[Root Cause]
    Cause --> Patch[Minimal Patch]
    Patch --> Local[Verify Locally]
    Local --> CI[Run CI]
    CI --> Pass{Green?}
    Pass -- No --> Logs
    Pass -- Yes --> Done[Done]
```

## 7. Infrastructure loop

```mermaid
flowchart TD
    Goal[Infrastructure Goal] --> Plan[Plan]
    Plan --> Validate[Validate IaC]
    Validate --> Cost[Cost and Risk Review]
    Cost --> Approval{Approval Required?}
    Approval -- Yes --> Human[Human Approval]
    Approval -- No --> ApplyDev[Apply to Dev or Test]
    Human --> ApplyDev
    ApplyDev --> Smoke[Smoke Test]
    Smoke --> Promote{Promote?}
    Promote -- No --> Rollback[Rollback]
    Promote -- Yes --> Done[Done]
```

## 8. Security loop

```mermaid
flowchart TD
    Asset[Asset] --> Boundary[Trust Boundary]
    Boundary --> Threat[Threat]
    Threat --> Control[Security Control]
    Control --> Abuse[Abuse Case Test]
    Abuse --> Pass{Blocked?}
    Pass -- No --> Improve[Improve Control]
    Improve --> Abuse
    Pass -- Yes --> Residual[Document Residual Risk]
    Residual --> Done[Done]
```

## 9. Model routing loop

```mermaid
flowchart TD
    Task[Task] --> Risk{Risk Level}
    Risk -- Low --> Local[Local or Small Model]
    Risk -- Medium --> Medium[Medium Model]
    Risk -- High --> Strong[Strong Model]
    Local --> Verify[Verifier]
    Medium --> Verify
    Strong --> Verify
    Verify --> Confidence{Enough Confidence?}
    Confidence -- No --> Escalate[Escalate Model]
    Escalate --> Verify
    Confidence -- Yes --> Done[Done]
```

## 10. Human approval checkpoint

```mermaid
flowchart TD
    Change[Proposed Change] --> Risk{Risky or irreversible?}
    Risk -- No --> Continue[Continue]
    Risk -- Yes --> Stop[Stop]
    Stop --> Explain[Explain Risk and Rollback]
    Explain --> Approve{Human Approved?}
    Approve -- No --> Alternative[Choose Safer Alternative]
    Approve -- Yes --> Continue
```
