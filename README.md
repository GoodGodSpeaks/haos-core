\# HAOS Core – He3lumina Autonomous Operating System



This is the core runtime for HAOS – a self-improving, agent-based research OS for fusion energy.



---



\## 🚀 Structure



```plaintext

agents/

&nbsp; planner/        ← generates concept specs

&nbsp; dummy\_sim/      ← computes derived KPIs from spec

&nbsp; aggregator/     ← collects and reports final outputs



run\_data/         ← stores JSON I/O between agents

shared/json\_schemas/ ← defines validated schemas

configs/          ← runtime configuration templates

tests/            ← pytest logic for all agents

docker/           ← Dockerfiles per simulation type

.github/workflows/← GitHub Actions CI



