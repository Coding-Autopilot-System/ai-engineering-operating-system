# Agent Compatibility

AI-OS is model- and tool-agnostic.

## Compatible agent types

- ChatGPT web sessions
- Claude Code style local agents
- Codex style coding agents
- Gemini CLI style coding agents
- Copilot coding agent workflows
- MCP-enabled local toolchains
- editor-integrated coding agents

## Compatibility rule

The agent does not need special support for every AI-OS concept. It only needs to follow the loop:

```mermaid
flowchart TD
    A[Load context] --> B[Plan]
    B --> C[Work]
    C --> D[Verify]
    D --> E{Done?}
    E -- No --> B
    E -- Yes --> F[Report]
```

## Minimum support

- read files
- edit files
- explain plan
- run or request checks
- report evidence
