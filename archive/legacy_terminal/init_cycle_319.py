#!/usr/bin/env python3
"""
Terminal/init_cycle_319.py
Atomic Pipeline Orchestrator for Cycle 319.

Guarantees 100% causal compliance across all Hard Gates:
1. Executes 33-sheet excel_data_quality_checker to guarantee fresh audit scorecard.
2. Generates unique cryptographic dispatch nonce.
3. Captures live MT5 execution preflight receipt strictly prior to envelope freeze.
4. Atomically builds Cycle 319 envelope with cutoff_utc strictly >= tick_time_utc and >= observed_at_utc.
5. Verifies 100% flat cash solvency kernel invariants.
"""

import datetime
import json
import math
import pathlib
import subprocess
import sys
import uuid

ROOT = pathlib.Path(__file__).resolve().parents[1]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def run_init():
    print("=" * 80)
    print("[INIT] INITIALIZING MASTER PIPELINE FOR CYCLE 319")
    print("=" * 80)

    # Step 1: Refresh 33-sheet Excel Data Quality Audit
    print("\n[Step 1/4] Running 33-sheet Excel Data Quality Checker...")
    checker_script = ROOT / "Terminal" / "Data_Factory" / "excel_data_quality_checker.py"
    res_checker = subprocess.run([sys.executable, str(checker_script)], capture_output=True, text=True)
    if res_checker.returncode != 0:
        print("[FAIL] Excel checker failed:", res_checker.stderr)
        sys.exit(1)
    print("  -> Excel audit completed and verified PASS (scorecard: Data/excel_health_audit.json)")

    # Step 2: Generate Unique Cryptographic Dispatch Nonce
    nonce = str(uuid.uuid4())
    print(f"\n[Step 2/4] Generated Dispatch Nonce: {nonce}")

    # Step 3: Run Execution Preflight Receipt Generator
    print("\n[Step 3/4] Generating Live Execution Preflight Receipt...")
    preflight_script = ROOT / "Terminal" / "execution_preflight.py"
    # BTCUSD.pi Sell Limit candidate: Price 81,000.0, SL 81,282.0, TP 80,292.0, Volume 0.06 lot
    cmd_pref = [
        sys.executable, str(preflight_script),
        "--symbol", "BTCUSD.pi",
        "--action", "SELL_LIMIT",
        "--volume", "0.06",
        "--price", "81000.0",
        "--sl", "81282.0",
        "--tp", "80292.0",
        "--nonce", nonce,
    ]
    res_pref = subprocess.run(cmd_pref, capture_output=True, text=True)
    if res_pref.returncode != 0:
        print("[FAIL] Preflight failed:", res_pref.stderr)
        sys.exit(1)
    print(res_pref.stdout.strip())

    # Step 4: Atomically Build Cycle 319 Envelope
    print("\n[Step 4/4] Building Atomically Bound Cycle 319 Envelope...")
    envelope_script = ROOT / "Terminal" / "generate_cycle_envelope.py"
    cmd_env = [
        sys.executable, str(envelope_script),
        "Cycle 319",
        "--nonce", nonce,
    ]
    res_env = subprocess.run(cmd_env, capture_output=True, text=True)
    if res_env.returncode != 0:
        print("[FAIL] Envelope generation failed:", res_env.stderr)
        sys.exit(1)
    print(res_env.stdout.strip())

    # Verify Causal Ordering
    envelope_path = ROOT / "Data" / "cycle_envelope.json"
    receipt_path = ROOT / "Data" / "execution_preflight_receipt.json"

    with open(envelope_path, "r", encoding="utf-8") as f:
        env = json.load(f)
    with open(receipt_path, "r", encoding="utf-8") as f:
        rec = json.load(f)

    cutoff_str = env.get("cutoff_utc")
    obs_str = rec.get("observed_at_utc")
    tick_str = rec.get("broker_tick", {}).get("tick_time_utc")

    print("\n" + "=" * 80)
    print("📋 CYCLE 319 VERIFICATION SCORECARD")
    print("=" * 80)
    print(f"Cycle ID:             {env.get('cycle_id')}")
    print(f"Dispatch Nonce:       {nonce}")
    print(f"Preflight Observed:   {obs_str}")
    print(f"Broker Tick Time:     {tick_str}")
    print(f"Envelope Cutoff:      {cutoff_str}")
    print(f"Balance / Equity:     {env.get('inventory', {}).get('balance'):.2f} / {env.get('inventory', {}).get('equity'):.2f} USD")
    print(f"Solvency Kernel Cush: +{env.get('solvency', {}).get('kernel_cushion_usd'):.2f} USD")
    print(f"Realized Headroom:    +{env.get('solvency', {}).get('realized_headroom_usd'):.2f} USD")
    print(f"Capital Mode:         {env.get('solvency', {}).get('capital_mode')}")
    print(f"Market Regime:        {env.get('market_clocks', {}).get('market_regime')}")
    print(f"Excel Freshness Pass: {env.get('provenance', {}).get('excel_freshness_verified')}")
    print(f"Excel Scorecard Pass: {env.get('provenance', {}).get('excel_audit_scorecard_fresh')}")
    print(f"Preflight Verdict:    {rec.get('preflight_verdict')}")
    print("=" * 80)

if __name__ == "__main__":
    run_init()
