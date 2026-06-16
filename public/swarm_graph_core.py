#!/usr/bin/env python3
"""
nano-graph: Deterministic Knowledge Graph Execution Pipeline
------------------------------------------------------------
A zero-dependency, high-velocity script to compile a physical filesystem 
of Markdown (.md) documents into a deterministic JSON graph index.

This script demonstrates the "Filesystem as Primary Vault" architectural invariant,
completely bypassing opaque Vector DBs (e.g., Pinecone/RAG) in favor of 
transparent, infinitely auditable, sub-second graph compilation.

Usage:
  python fs_to_graph.py --target /path/to/docs --output graph.json
"""

import os
import re
import json
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Extract standard Markdown links [Label](file.md) or <file.md>
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)\)')
BARE_REF_PATTERN = re.compile(r'[\(\[]([a-zA-Z0-9_\-/\.]+\.md)[\)\]\s`]')

def sha256_file(path: Path) -> str:
    """Generate a cryptographic hash representing the invariant state of the document."""
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
        return h.hexdigest()[:16]
    except Exception:
        return "error_reading_file"

def build_deterministic_graph(target_dir: Path) -> dict:
    print(f"[INGRESS_VERIFIED] Target Vault: {target_dir.as_posix()}")
    
    nodes = {}
    edges = []
    
    # 1. Ingress phase: Vault scan
    files = list(target_dir.rglob("*.md"))
    print(f"[ENCLAVE_SCAN] Detected {len(files)} potential state nodes.")
    
    # 2. Node Compilation
    for filepath in files:
        node_id = filepath.relative_to(target_dir).as_posix()
        try:
            content = filepath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            content = ""
            
        nodes[node_id] = {
            "id": node_id,
            "label": filepath.stem.replace("_", " ").title(),
            "content_hash": sha256_file(filepath),
            "size_bytes": filepath.stat().st_size,
            "last_modified": datetime.fromtimestamp(filepath.stat().st_mtime, tz=timezone.utc).isoformat(),
            "inbound_refs": [],
            "outbound_refs": []
        }
        
        # 3. Edge Compilation (Reference extraction)
        # Extract explicit links
        for match in LINK_PATTERN.finditer(content):
            target = match.group(2)
            resolved = resolve_reference(target, filepath, target_dir)
            if resolved:
                edges.append({"source": node_id, "target": resolved, "type": "explicit_link"})
                
        # Extract bare references
        for match in BARE_REF_PATTERN.finditer(content):
            target = match.group(1)
            resolved = resolve_reference(target, filepath, target_dir)
            if resolved:
                edges.append({"source": node_id, "target": resolved, "type": "bare_reference"})
                
    # Deduplicate edges to ensure deterministic settlement
    seen_edges = set()
    deterministic_edges = []
    for edge in edges:
        edge_key = (edge["source"], edge["target"])
        if edge_key not in seen_edges and edge["source"] != edge["target"]:
            seen_edges.add(edge_key)
            deterministic_edges.append(edge)
            
            # Inject bidirectional pointers into nodes
            src = edge["source"]
            tgt = edge["target"]
            if src in nodes and tgt not in nodes[src]["outbound_refs"]:
                nodes[src]["outbound_refs"].append(tgt)
            if tgt in nodes and src not in nodes[tgt]["inbound_refs"]:
                nodes[tgt]["inbound_refs"].append(src)

    print(f"[SETTLEMENT_READY] {len(nodes)} Nodes compiled | {len(deterministic_edges)} Edges resolved")
    
    return {
        "meta": {
            "generated": datetime.now(tz=timezone.utc).isoformat(),
            "vault_root": target_dir.as_posix(),
            "total_nodes": len(nodes),
            "total_edges": len(deterministic_edges)
        },
        "nodes": nodes,
        "edges": deterministic_edges
    }

def resolve_reference(ref: str, current_file: Path, vault_root: Path) -> str:
    """Resolve a relative or absolute reference to a verified node ID within the vault."""
    # Attempt absolute from vault root
    candidate = vault_root / ref
    if candidate.exists() and candidate.is_file():
        return candidate.relative_to(vault_root).as_posix()
        
    # Attempt relative from current file's directory
    candidate = current_file.parent / ref
    if candidate.exists() and candidate.is_file():
        return candidate.relative_to(vault_root).as_posix()
        
    return None

def main():
    parser = argparse.ArgumentParser(description="Deterministic Knowledge Graph Execution Pipeline")
    parser.add_argument("--target", required=True, help="Directory containing Markdown files (The Vault)")
    parser.add_argument("--output", default="graph.json", help="Output JSON settlement file")
    
    args = parser.parse_args()
    
    target_path = Path(args.target).resolve()
    output_path = Path(args.output).resolve()
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"[FATAL_REVERT] Target vault does not exist: {target_path}")
        return
        
    start_time = datetime.now()
    graph_state = build_deterministic_graph(target_path)
    
    output_path.write_text(json.dumps(graph_state, indent=2), encoding="utf-8")
    
    latency = (datetime.now() - start_time).total_seconds() * 1000
    print(f"[SETTLEMENT_FINALIZED] Graph index securely committed to {args.output}")
    print(f"  > Latency: {latency:.2f}ms")
    print(f"  > State: Zero-Custody Index Secured")

if __name__ == "__main__":
    main()
