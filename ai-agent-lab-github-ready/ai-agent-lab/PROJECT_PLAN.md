# Project Plan

## Goal

Build a small, transparent AI-agent experimentation repository that can grow from a local deterministic demo into a real LLM-powered research workflow.

## Milestone 1 — Local workflow

- [x] Define a planner agent
- [x] Define an evidence-checking agent
- [x] Define a risk-review agent
- [x] Define a summary agent
- [x] Produce structured local output
- [x] Keep the demo free of API keys and private data

## Milestone 2 — Model integration

- [ ] Add a provider interface for LLM inference
- [ ] Support one open-source model or hosted inference provider
- [ ] Store prompts separately from orchestration logic
- [ ] Add timeout and error handling

## Milestone 3 — Evaluation

- [ ] Add small test cases
- [ ] Compare single-agent and multi-agent outputs
- [ ] Add evidence-quality checks
- [ ] Record latency and basic resource usage

## Milestone 4 — GPU experiments

- [ ] Test open-source model inference on compatible GPU infrastructure
- [ ] Measure latency and throughput
- [ ] Compare model sizes and quantization settings
- [ ] Document reproducible inference experiments
- [ ] Explore compatible workloads on AMD GPU infrastructure

## Principles

1. Keep experiments reproducible.
2. Do not commit credentials or private data.
3. Clearly distinguish working features from planned work.
4. Prefer measurable results over vague claims.
5. Keep the repository understandable for other developers.
