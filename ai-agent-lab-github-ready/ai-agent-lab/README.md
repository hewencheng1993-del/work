# AI Agent Lab

A small personal project for experimenting with **AI agent workflows**, **LLM application design**, **research automation**, and **structured data analysis**.

This repository is intentionally lightweight. It is used for learning, prototyping, and testing how multiple simple agents can cooperate on a research task.

## What this project demonstrates

The demo implements a small multi-agent-style workflow:

1. **Planner Agent** — breaks a question into research steps.
2. **Evidence Agent** — identifies what information should be collected.
3. **Risk Agent** — checks assumptions and possible failure points.
4. **Summary Agent** — produces a structured final report.

The current version runs locally and does **not** require an API key.

## Why I built it

I am learning how to design practical AI applications around:

- AI agent workflows
- LLM-based research automation
- Multi-agent collaboration
- Structured data analysis
- Evidence and risk checking
- Model inference experiments

My goal is to keep the examples small, understandable, and easy to extend.

## Quick start

Requirements:

- Python 3.10+

Clone or download this repository, then run:

```bash
python main.py
```

You can also provide your own question:

```bash
python main.py "How can AI agents improve data analysis workflows?"
```

The program prints a structured JSON-style research report.

## Example

Input:

```text
How can AI agents improve data analysis workflows?
```

The workflow creates a plan, identifies evidence requirements, checks risks, and generates a concise conclusion.

See:

```text
examples/sample_output.md
```

for an example result.

## Project structure

```text
ai-agent-lab/
├── README.md
├── main.py
├── requirements.txt
├── PROJECT_PLAN.md
├── LICENSE
├── .gitignore
└── examples/
    └── sample_output.md
```

## Current status

This is an **early-stage personal learning project**. The current demo uses deterministic local logic so that the workflow can be tested without external services or credentials.

Future versions may connect the same workflow to open-source language models or hosted inference APIs.

## Planned experiments

I plan to explore:

- Open-source LLM inference
- Agent orchestration patterns
- Tool-using agents
- Retrieval-augmented research workflows
- Evaluation of agent outputs
- GPU-accelerated inference workloads

I am also interested in testing compatible open-source model inference and agent workloads on **AMD GPU infrastructure** when suitable compute resources are available.

## Security and privacy

This repository intentionally contains:

- No API keys
- No tokens or passwords
- No private datasets
- No proprietary trading strategies
- No personal or confidential information

Secrets and local environment files should never be committed.

## License

MIT License. See [LICENSE](LICENSE).

---

This repository reflects personal learning and experimentation. Features and documentation will evolve as new experiments are added.
