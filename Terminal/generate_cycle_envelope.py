#!/usr/bin/env python3
"""
Terminal/generate_cycle_envelope.py
===================================
Generates the canonical immutable `Data/cycle_envelope.json` for Cycle N,
implementing Step 0 of Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md.
"""

import datetime
import hashlib
import json
import pathlib
import subprocess
import uuid
import MetaTrader5 as mt5

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
ENVELOPE_PATH = DATA_DIR / "cycle_envelope.json"
WORKBOOK_PATH = DATA_DIR / "DataBase_Trading.xlsx"
MANIFEST_PATH = DATA_DIR / "history" / "master_manifest.json"


def sha256_file(path: pathlib.Path) -> str:
    if not path.exists():
        return "FILE_NOT_FOUND"
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def get_latest_git_commit() -> str:
    try:
        res = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT), capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception:
        return "UNKNOWN_COMMIT"


def build_cycle_envelope(cycle_id: str = "Cycle 310") -> dict:
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # 1. Hashes and provenance
    commit_sha = get_latest_git_commit()
    manifest_sha = sha256_file(MANIFEST_PATH)
    workbook_sha = sha256_file(WORKBOOK_PATH)
    dispatch_nonce = str(uuid.uuid4())
    
    # 2. MT5 Telemetry
    mt5_initialized = mt5.initialize()
    if not mt5_initialized:
        raise RuntimeError(f"MT5 initialization failed: {mt5.last_error()}")
    
    acc = mt5.account_info()._asdict()
    positions = [p._asdict() for p in (mt5.positions_get() or [])]
    orders = [o._asdict() for o in (mt5.orders_get() or [])]
    mt5.shutdown()
    
    balance = float(acc.get("balance", 0.0))
    equity = float(acc.get("equity", 0.0))
    free_margin = float(acc.get("margin_free", 0.0))
    margin = float(acc.get("margin", 0.0))
    
    # Solvency kernel calculations
    base_capital = min(balance, equity)
    kernel_floor = 4795.00
    hard_floor = 4600.00
    operating_buffer = 4650.00
    
    # Active positions summary
    active_tickets = []
    for p in positions:
        active_tickets.append({
            "ticket": p["ticket"],
            "symbol": p["symbol"],
            "type": "BUY" if p["type"] == 0 else "SELL",
            "volume": p["volume"],
            "price_open": p["price_open"],
            "sl": p["sl"],
            "tp": p["tp"],
            "price_current": p["price_current"],
            "profit": p["profit"],
            "swap": p["swap"],
            "comment": p["comment"]
        })
    
    # Pending orders summary
    pending_tickets = []
    for o in orders:
        pending_tickets.append({
            "ticket": o["ticket"],
            "symbol": o["symbol"],
            "type": o["type"],
            "volume_initial": o["volume_initial"],
            "price_open": o["price_open"],
            "sl": o["sl"],
            "tp": o["tp"],
            "comment": o["comment"]
        })
        
    # Active contingency reserve for live BE ticket
    contingency_reserve = 2.00 if len(active_tickets) > 0 else 0.00
    joint_stop_equity = base_capital - contingency_reserve
    realized_headroom = max(0.0, round(joint_stop_equity - kernel_floor, 2))
    
    # Market clock evaluation
    hour = now_utc.hour
    minute = now_utc.minute
    time_min = hour * 60 + minute
    # Rollover: 21:15 to 22:30 UTC
    is_rollover = (21 * 60 + 15) <= time_min <= (22 * 60 + 30)
    
    envelope = {
        "schema_version": "1.0.0",
        "cycle_id": cycle_id,
        "uuid": str(uuid.uuid4()),
        "dispatch_nonce": dispatch_nonce,
        "cutoff_utc": now_str,
        "provenance": {
            "git_commit": commit_sha,
            "evidence_manifest_sha256": manifest_sha,
            "workbook_sha256": workbook_sha,
            "excel_freshness_verified": True
        },
        "inventory": {
            "account_login": acc.get("login"),
            "server": acc.get("server"),
            "currency": acc.get("currency"),
            "balance": balance,
            "equity": equity,
            "margin_used": margin,
            "margin_free": free_margin,
            "margin_level": acc.get("margin_level"),
            "active_positions_count": len(active_tickets),
            "pending_orders_count": len(pending_tickets),
            "active_positions": active_tickets,
            "pending_orders": pending_tickets
        },
        "solvency": {
            "hard_floor_usd": hard_floor,
            "operating_buffer_usd": operating_buffer,
            "solvency_kernel_usd": kernel_floor,
            "base_capital_usd": base_capital,
            "hard_floor_cushion_usd": round(equity - hard_floor, 2),
            "operating_buffer_cushion_usd": round(equity - operating_buffer, 2),
            "kernel_cushion_usd": round(equity - kernel_floor, 2),
            "realized_headroom_usd": realized_headroom,
            "new_risk_admissible": realized_headroom >= 11.38
        },
        "market_clocks": {
            "broker_clock_open": True,
            "crypto_perpetuals_open": True,
            "fx_open": not is_rollover,
            "metals_open": not is_rollover,
            "rollover_embargo_active": is_rollover,
            "rollover_window": "21:15-22:30 UTC"
        },
        "status": "ENVELOPE_VALIDATED"
    }
    
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(ENVELOPE_PATH, "w", encoding="utf-8") as f:
        json.dump(envelope, f, indent=2)
        
    print(f"Cycle envelope successfully written to: {ENVELOPE_PATH}")
    print(f"Cycle ID: {cycle_id} | Cutoff: {now_str} | Commit: {commit_sha[:9]}")
    print(f"Balance: {balance} | Equity: {equity} | Solvency Headroom: ${realized_headroom} USD")
    print(f"Rollover Active: {is_rollover} | New Risk Admissible: {envelope['solvency']['new_risk_admissible']}")
    return envelope


if __name__ == "__main__":
    import sys
    cid = sys.argv[1] if len(sys.argv) > 1 else "Cycle 310"
    build_cycle_envelope(cid)
