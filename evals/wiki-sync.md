# Eval: Wiki Sync

## Task

Ensure repository wiki source pages are reflected in the actual GitHub Wiki.

## Expected loop

Continuous improvement loop.

## Required evidence

- `wiki/Home.md` exists.
- `wiki/Loops.md` exists.
- `wiki/Prompts.md` exists.
- `sync-wiki` workflow exists.
- Final answer says whether the workflow was run or still needs to be run.

## Pass criteria

The agent does not confuse repo-side `wiki/` files with the actual GitHub Wiki tab.
