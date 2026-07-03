# Branch and Tag Rules

This repository should protect the public operating model through rulesets.

## Recommended `main` rules

- require pull request before merge
- require status checks
- require CODEOWNERS review when available
- block force pushes
- block deletion
- keep history linear if desired

## Recommended tag rules

- protect `v*` release tags
- block tag deletion
- block tag force updates
- require release workflow for public releases

## Approval flow

```mermaid
flowchart TD
    PR[Pull Request] --> Checks[Required checks]
    Checks --> Review[Review]
    Review --> Merge{Merge allowed?}
    Merge -- No --> Rework[Rework]
    Rework --> Checks
    Merge -- Yes --> Main[main]
    Main --> Tag{Release?}
    Tag -- Yes --> Approval[Release approval]
    Tag -- No --> Done[Done]
    Approval --> Release[Release]
```
