# CascadeGuard AI

> **An AI System for Cascading Software Failure Prediction, Root Cause Analysis, and Autonomous Strategy Recovery.**

Built under the **GRAVITAS** Engineering Reliability Runtime framework.

---

## Overview

Modern cloud microservices are tightly coupled networks. When one downstream dependency (e.g. database connection pool or 3rd-party payment API) degrades, retry storms, thread starvation, and buffer saturation cascade upstream in seconds, causing total system outages.

**CascadeGuard AI** prevents outages by:
1. **Predicting Cascading Failures**: Multi-metric anomaly detection and graph-based failure probability propagation $P(\text{fail})$ forecasting **Next-to-Fail Components** and **Time-to-Failure (TTF)** horizons before the whole system crashes.
2. **Tracing Blast Paths**: Identifying exact directional blast propagation across the dependency graph.
3. **Automated Root Cause Analysis (RCA)**: Backward topological attribution and temporal correlation isolating the true culprit (e.g. distinguishing between a symptom 504 at the API Gateway vs. a connection pool starvation at the primary PostgreSQL database).
4. **Recovery Strategy Recommendation Matrix**: Multi-Criteria Decision Analysis (MCDA) evaluating 5 operational mitigation strategies (Circuit Breaking, Adaptive Load Shedding, Standby Failover, Graceful Restart, Auto-Scaling) comparing MTTR, system availability, data loss risk, and cost.
5. **Interactive Live Dashboard**: SRE Command Center with real-time SVG dependency graph, chaos injection lab, live server log stream, and interactive strategy simulation.

---

## Architecture

```
[Simulated Server Logs & Telemetry]
              │
              ▼
   [Dependency Graph Topology] ◄──── [Chaos Injection Engine]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
[Cascade Prediction]  [Root Cause Analysis]
(P(fail), TTF, Blast) (Topological Attribution)
    │                   │
    └─────────┬─────────┘
              ▼
  [Recovery Strategy Engine]
(MCDA Tradeoff Optimization)
              │
              ▼
[Interactive Live SRE Dashboard]
```

---

## Quick Start

### 1. Run Tests
Verify system integrity using the test suite:
```bash
python -m pytest tests/ -v
```

### 2. Launch the Application
Start the server and interactive live dashboard:
```bash
python run.py
```
Then navigate to: **`http://127.0.0.1:8000`**

---

## Chaos Failure Scenarios

CascadeGuard AI includes 5 pre-configured real-world chaos engineering failure scenarios:

1. **Database Connection Pool Starvation (`order-db`)**: Simulates 100% connection exhaustion, hanging transactions, caller thread starvation, and upstream 504 timeouts.
2. **Latency Spike & Retry Storm (`payment-gateway`)**: External API spikes to 3500ms; aggressive client retry storm saturates connection buffers.
3. **Redis Cache Avalanche (`redis-cache`)**: Shared cache outage causes cold-miss query stampede on databases.
4. **Memory Leak & GC Thrashing (`auth-service`)**: Heap spikes to 98%, freezing worker threads in garbage collection cycles.
5. **Rate Limit Backpressure (`kafka-bus`)**: Downstream 429 rate limiting triggers worker backpressure, overflowing event queues.
