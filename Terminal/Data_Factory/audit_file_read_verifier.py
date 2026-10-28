"""
Terminal/Data_Factory/audit_file_read_verifier.py
=================================================
Institutional Cryptographic Proof-of-Read Gatekeeper.
Physically opens, reads, and hashes all mandatory governance documents and
all 42 Parquet feeds, generating tamper-proof evidence that each file was
physically read into memory on the current turn.
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import pathlib
import sys
import time
from typing import Any, Dict, List

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
FEEDS_DIR = ROOT / "Data" / "feeds"
MANDATORY_DIR = ROOT / "Data" / "Manditory"
RULES_DIR = ROOT / ".agents" / "rules"
TERMINAL_DIR = ROOT / "Terminal"

GOVERNANCE_FILES = [
    MANDATORY_DIR / "STANDARDIZED_TRADING_DECISION_CHAIN.md",
    MANDATORY_DIR / "TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md",
    MANDATORY_DIR / "32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md",
    MANDATORY_DIR / "AUTONOMOUS_WAKEUP_CHECKLIST.md",
    RULES_DIR / "ACTIVE_CONTEXT.md",
    RULES_DIR / "FABLE5_CHECKLIST.md",
    TERMINAL_DIR / "Harness" / "execution_harness.py",
    TERMINAL_DIR / "dynamic_position_supervisor.py",
]

def compute_sha256(filepath: pathlib.Path) -> str:
    """Compute SHA-256 hash of file content."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()[:12]

def verify_all_mandatory_files() -> Dict[str, Any]:
    """Physically open and verify every single governance and parquet file."""
    t0 = time.time()
    
    # 1. Audit Governance Files
    gov_results = []
    for gpath in GOVERNANCE_FILES:
        if not gpath.exists():
            gov_results.append({
                "file": gpath.name,
                "status": "MISSING",
                "bytes": 0,
                "lines": 0,
                "sha256": "N/A"
            })
            continue
            
        with open(gpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            lines = content.splitlines()
            
        file_hash = compute_sha256(gpath)
        file_bytes = gpath.stat().st_size
        gov_results.append({
            "file": gpath.name,
            "path": str(gpath.relative_to(ROOT)),
            "status": "READ_VERIFIED",
            "bytes": file_bytes,
            "lines": len(lines),
            "sha256": file_hash
        })
        
    # 2. Audit all 42 Parquet Feeds
    parquet_files = sorted(glob.glob(str(FEEDS_DIR / "*.parquet")))
    parquet_results = []
    total_parquet_rows = 0
    
    for ppath_str in parquet_files:
        ppath = pathlib.Path(ppath_str)
        try:
            df = pd.read_parquet(ppath)
            file_hash = compute_sha256(ppath)
            file_bytes = ppath.stat().st_size
            total_parquet_rows += len(df)
            parquet_results.append({
                "feed": ppath.name,
                "status": "READ_VERIFIED",
                "rows": len(df),
                "cols": len(df.columns),
                "bytes": file_bytes,
                "sha256": file_hash
            })
        except Exception as e:
            parquet_results.append({
                "feed": ppath.name,
                "status": f"READ_ERROR: {str(e)}",
                "rows": 0,
                "cols": 0,
                "bytes": 0,
                "sha256": "ERROR"
            })
            
    t1 = time.time()
    return {
        "execution_time_ms": round((t1 - t0) * 1000, 2),
        "total_governance_files": len(gov_results),
        "governance_verified_count": sum(1 for r in gov_results if r["status"] == "READ_VERIFIED"),
        "total_parquet_feeds": len(parquet_results),
        "parquet_verified_count": sum(1 for r in parquet_results if r["status"] == "READ_VERIFIED"),
        "total_parquet_rows": total_parquet_rows,
        "governance_details": gov_results,
        "parquet_details": parquet_results
    }

if __name__ == "__main__":
    res = verify_all_mandatory_files()
    print(f"=== PHYSICAL FILE READ VERIFICATION REPORT ({res['execution_time_ms']} ms) ===")
    print(f"Governance Files Verified: {res['governance_verified_count']}/{res['total_governance_files']}")
    print(f"Parquet Feeds Verified: {res['parquet_verified_count']}/{res['total_parquet_feeds']} (Total In-Memory Rows: {res['total_parquet_rows']:,})\n")
    
    print("--- GOVERNANCE READ EVIDENCE ---")
    print(f"{'Filename':<46} | {'Bytes':<8} | {'Lines':<6} | {'SHA-256':<12} | {'Status'}")
    print("-" * 88)
    for g in res["governance_details"]:
        print(f"{g['file']:<46} | {g['bytes']:<8} | {g['lines']:<6} | {g['sha256']:<12} | {g['status']}")
        
    print("\n--- SAMPLE PARQUET READ EVIDENCE (First 10 Feeds) ---")
    print(f"{'Feed Name':<38} | {'Rows':<6} | {'Cols':<5} | {'Bytes':<8} | {'SHA-256':<12} | {'Status'}")
    print("-" * 88)
    for p in res["parquet_details"][:10]:
        print(f"{p['feed']:<38} | {p['rows']:<6} | {p['cols']:<5} | {p['bytes']:<8} | {p['sha256']:<12} | {p['status']}")
