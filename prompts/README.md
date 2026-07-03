# Prompt Templates

## Universal everyday prompt

```text
Execute AI Engineering Operating System from this repository.

Task:
[YOUR TASK]

Load context first.
Select the correct loop.
Plan before implementation.
Verify before declaring completion.
Return to the earliest failing phase when verification fails.
Stop only when Definition of Done passes.
```

## Feature prompt

```text
Use the feature development loop.
Define acceptance criteria first.
Implement in small increments.
Add or update tests.
Update documentation.
```

## Bug fix prompt

```text
Use the bug fix loop.
Reproduce the defect first when possible.
Create a failing test when useful.
Fix the root cause, not only the symptom.
Run regression verification.
```

## CI/CD repair prompt

```text
Use the CI/CD repair loop.
Fetch logs, classify the failure, identify root cause, make the minimal patch, and verify.
```

## Refactoring prompt

```text
Use the refactoring loop.
Do not change behavior unless explicitly requested.
Establish baseline verification before editing.
```
