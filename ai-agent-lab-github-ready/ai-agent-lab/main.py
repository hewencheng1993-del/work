"""
AI Agent Lab
A minimal local multi-agent workflow for research-style tasks.

This demo intentionally uses only Python's standard library.
No API key or external service is required.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class AgentResult:
    agent: str
    output: list[str]


def planner_agent(question: str) -> AgentResult:
    """Break a question into a small research plan."""
    return AgentResult(
        agent="Planner Agent",
        output=[
            f"Define the scope of the question: {question}",
            "Identify the main claims that need evidence.",
            "Separate benefits, limitations, and implementation concerns.",
            "Prepare a concise conclusion supported by the collected points.",
        ],
    )


def evidence_agent(question: str) -> AgentResult:
    """Describe what evidence should be collected before answering."""
    return AgentResult(
        agent="Evidence Agent",
        output=[
            "Collect primary or authoritative technical documentation where possible.",
            "Look for measurable examples, benchmarks, or reproducible observations.",
            "Separate verified facts from assumptions or opinions.",
            f"Check whether the evidence directly addresses: {question}",
        ],
    )


def risk_agent(question: str) -> AgentResult:
    """Act as a simple red-team / risk reviewer."""
    return AgentResult(
        agent="Risk Agent",
        output=[
            "Check for unsupported conclusions or missing counter-evidence.",
            "Watch for stale information, ambiguous definitions, and selection bias.",
            "Avoid treating correlation as causation.",
            f"State uncertainty explicitly when the evidence for '{question}' is incomplete.",
        ],
    )


def summary_agent(question: str, prior_results: list[AgentResult]) -> AgentResult:
    """Create a compact synthesis from the previous agents."""
    agent_names = ", ".join(result.agent for result in prior_results)
    return AgentResult(
        agent="Summary Agent",
        output=[
            f"Question: {question}",
            f"Inputs reviewed from: {agent_names}.",
            "A reliable answer should combine an explicit plan, evidence quality checks, and risk review.",
            "The workflow is designed to be extended later with real LLM inference or external tools.",
        ],
    )


def run_workflow(question: str) -> dict:
    planner = planner_agent(question)
    evidence = evidence_agent(question)
    risk = risk_agent(question)
    summary = summary_agent(question, [planner, evidence, risk])

    return {
        "project": "AI Agent Lab",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "agents": [asdict(x) for x in [planner, evidence, risk, summary]],
    }


def main() -> None:
    question = (
        " ".join(sys.argv[1:]).strip()
        or "How can AI agents improve data analysis workflows?"
    )
    report = run_workflow(question)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
