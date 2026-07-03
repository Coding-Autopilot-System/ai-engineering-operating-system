# AI Engineering Operating System (AI-OS)

> Prompt once. Verify everything. Loop until the goal is achieved.

AI Engineering Operating System is a public methodology and documentation framework for turning AI coding agents into disciplined software engineering systems.

It defines reusable SDLC loops, Mermaid diagrams, verification gates, model routing, memory rules, human approval checkpoints, and continuous improvement workflows for local-first AI development.

## Why this exists

Most AI coding workflows still behave like ad-hoc chats. AI-OS turns that into an auditable engineering process:

1. set a clear goal
2. fan out to specialist roles
3. produce a plan
4. ask for human approval when risk is meaningful
5. implement in small reversible steps
6. verify using strong gates
7. update docs, memory, wiki, and roadmap
8. repeat until no valuable improvement remains

## Start here

- [Master operating manual](docs/ai-os/master-operating-manual.md)
- [Continuous improvement loop](docs/methodology/continuous-improvement-loop.md)
- [Mermaid diagram catalog](docs/diagrams/README.md)
- [Loop catalog](docs/loops/README.md)
- [Verification gates](docs/verifiers/README.md)
- [Prompt templates](prompts/README.md)
- [ChatGPT web operating prompt](prompts/chatgpt-web.md)
- [Wiki home](wiki/Home.md)

## Everyday prompt

```text
Execute AI Engineering Operating System from this repository.

Task:
[YOUR TASK HERE]

Load context first.
Select the right loop.
Fan out analysis to specialist roles.
Create a plan before implementation.
Ask for human approval before risky or broad changes.
Implement approved work in small reversible steps.
Verify before declaring completion.
Return to the earliest failing phase when verification fails.
Update docs and memory.
Stop only when the Definition of Done passes.
```

## Repository purpose

This repository documents the instructions, diagrams, and operating model I use when working with AI coding agents and ChatGPT web sessions.

The goal is to make AI-assisted development visible, repeatable, auditable, and production-oriented.

## Current maturity target

AI-OS is moving from methodology showcase to production-grade open framework. The next milestones are governance, full wiki, CI quality gates, security posture, release process, examples, and self-improvement automation.
