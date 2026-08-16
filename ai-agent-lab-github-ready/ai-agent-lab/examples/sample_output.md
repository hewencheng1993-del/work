# Sample Output

Example command:

```bash
python main.py "How can AI agents improve data analysis workflows?"
```

Example output (timestamps will vary):

```json
{
  "project": "AI Agent Lab",
  "question": "How can AI agents improve data analysis workflows?",
  "agents": [
    {
      "agent": "Planner Agent",
      "output": [
        "Define the scope of the question.",
        "Identify the main claims that need evidence.",
        "Separate benefits, limitations, and implementation concerns."
      ]
    },
    {
      "agent": "Evidence Agent",
      "output": [
        "Collect primary or authoritative technical documentation where possible.",
        "Look for measurable examples, benchmarks, or reproducible observations.",
        "Separate verified facts from assumptions or opinions."
      ]
    },
    {
      "agent": "Risk Agent",
      "output": [
        "Check for unsupported conclusions or missing counter-evidence.",
        "Watch for stale information, ambiguous definitions, and selection bias."
      ]
    },
    {
      "agent": "Summary Agent",
      "output": [
        "A reliable answer should combine an explicit plan, evidence quality checks, and risk review.",
        "The workflow is designed to be extended later with real LLM inference or external tools."
      ]
    }
  ]
}
```

## Notes

This output is generated locally without calling an external model.

The repository is designed so that future versions can replace the deterministic agent functions with calls to open-source LLMs or inference APIs while keeping the same orchestration structure.
