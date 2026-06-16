# Swarm-Graph 🕸️
**Deterministic State Orchestration for LLM Ensembles.**

> 📡 **STATUS:** PRODUCTION-READY | **CORE:** MIT | **DAEMON:** BSL 1.1

Vector databases and RAG pipelines are statistical slot machines. They rely on semantic proximity, which degrades linearly as your knowledge base grows. For enterprise AGI, guessing is not an architecture. 

**Swarm-Graph** replaces probabilistic search with **Deterministic Graph Compilation**. Knowledge is stored physically as bidirectional edges in JSON. State is absolute.

## The Enterprise Contrast
Stop building statistical slot machines. Start building deterministic state engines.

*   **Instead of:** Spawning probabilistic sub-agents that hallucinate context boundaries.
*   **Swarm-Graph provides:** Spinning up highly-reliable Intelligence Councils grounded in an absolute, deterministic file-system reality.

*   **Instead of:** Hoping a Vector DB retrieves the right semantic chunks via "black-box" mathematical proximity.
*   **Swarm-Graph provides:** Executing exact path-traversals across a physical JSON Knowledge Graph.

*   **Instead of:** Dealing with silent race conditions when 50 asynchronous agents write to memory simultaneously.
*   **Swarm-Graph provides:** Atomic Semantic Swarm Resolution, guaranteeing absolute state coherence via LLM-aware CRDTs.

## The Open Core Duality

Swarm-Graph operates on a strict physics-based duality:

### 1. Swarm-Graph Core (MIT / Free Forever)
The base compiler is a zero-dependency, atomic script that reads your markdown/code repositories and compiles them into a self-healing `SYSTEM_GRAPH.json`. 
*   **Best for:** Single-agent workflows, CI/CD static generation, synchronous pipelines (1-5 agents).
*   **Result:** 100% hallucination-free context injection.

### 2. Swarm-Graph Daemon (BSL 1.1 / Enterprise)
When you deploy 50+ autonomous subagents, they will simultaneously attempt to mutate the `SYSTEM_GRAPH.json`. The file-system will violently collapse into race conditions. The **Swarm-Graph Daemon** is a Rust-based MCP Server that introduces **Semantic Swarm Concurrency**.
*   **Best for:** High-frequency async swarms, enterprise agentic networks.
*   **Result:** Atomic write-locking, parallel graph traversal, zero-latency state sync.

---

## The Core Compiler (MIT)

The free compiler acts as the single source of truth for your agent's memory.

### Installation
Drop the atomic script into your repository. No `pip install`, no dependencies.

```bash
curl -O https://raw.githubusercontent.com/mentalos/swarm-graph/master/public/swarm_graph_core.py
```

### Usage
Run the compiler before your agent executes its turn:
```bash
python swarm_graph_core.py --target ./knowledge --output SYSTEM_GRAPH.json
```
Your agent now has a deterministic, mathematically verifiable map of the entire system.

---

## The Swarm Daemon (BSL 1.1)

If you are running multi-agent swarms, the free core is not enough. You need the Swarm-Graph Daemon to act as the traffic controller for concurrent state mutations.

### Features
*   **Semantic Write-Locks:** Agent A can mutate `node_x` while Agent B mutates `node_y`. The daemon resolves the graph merge mathematically.
*   **MCP Protocol:** Plugs directly into Claude, OpenAI, and custom orchestrators via Model Context Protocol.
*   **In-Memory Rust Engine:** Sub-millisecond graph query resolution.

### Licensing & Deployment
The Daemon is licensed under BSL 1.1. It is free for non-production environments and early-stage testing. For production deployments with revenue >$1M, an Enterprise License is required.

[Request Enterprise Daemon Access →](https://example.com/swarm-graph-enterprise)

---

## Axioms of the Graph

1. **Zero-Mock:** If it is not in the graph, the agent cannot see it.
2. **Absolute Resonance:** The filesystem is the single source of truth; the graph is its mirror.
3. **Shadow Purity:** All state changes are drafted in memory, verified for schema integrity, and atomically committed.

*Built for the Autonomous Enterprise.*
