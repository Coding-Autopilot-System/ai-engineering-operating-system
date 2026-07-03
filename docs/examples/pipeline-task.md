# Example: Pipeline Task

## Goal

Repair a failing workflow using AI-OS.

## Loop

Pipeline repair loop.

## Steps

1. Read the failing job name.
2. Read the relevant log section.
3. Classify the failure.
4. Identify the cause.
5. Make the smallest correction.
6. Run the local or workflow check.
7. Report evidence.

## Evidence format

```text
Workflow:
Job:
Failure class:
Cause:
Change:
Verification:
```
