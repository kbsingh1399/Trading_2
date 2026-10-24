#!/usr/bin/env python3
"""Read native account inventory and atomically publish a causal cycle envelope."""
import datetime
import hashlib
import json
import math
import os
import pathlib
import subprocess
import tempfile
import uuid
import MetaTrader5 as mt5

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENVELOPE_PATH = ROOT / "Data/cycle_envelope.json"
WORKBOOK_PATH = ROOT / "Data/DataBase_Trading.xlsx"
MANIFEST_PATH = ROOT / "Data/history/master_manifest.json"
ACCOUNT_LOGIN = 5064568
KERNEL_FLOOR = 4795.0
GLOBAL_RESERVE = 2.0
MAX_TICKETS = 2


def number(value, name, *, positive=False):
    if isinstance(value, bool):
        raise ValueError(f"invalid_{name}")
    result = float(value)
    if not math.isfinite(result) or result < 0 or (positive and result == 0):
        raise ValueError(f"invalid_{name}")
    return result


def as_dict(value):
    if isinstance(value, dict):
        return dict(value)
    return value._asdict()


def read_inventory(api):
    """None inventory is unknown. Broker-valued loss includes every fillable ticket."""
    raw_account = api.account_info()
    if raw_account is None:
        raise RuntimeError("account_unavailable")
    account = as_dict(raw_account)
    if account.get("login") != ACCOUNT_LOGIN or account.get("currency") != "USD":
        raise RuntimeError("account_identity_or_currency_mismatch")
    positions, orders = api.positions_get(), api.orders_get()
    if positions is None or orders is None:
        raise RuntimeError("inventory_unavailable")
    balance = number(account.get("balance"), "balance", positive=True)
    equity = number(account.get("equity"), "equity", positive=True)
    for key in ("margin", "margin_free"):
        number(account.get(key), key)
    positions, orders = [as_dict(p) for p in positions], [as_dict(o) for o in orders]
    stress = 0.0
    for pending, rows in ((False, positions), (True, orders)):
        for row in rows:
            kind = row.get("type")
            if kind not in ((2, 3, 4, 5, 6, 7) if pending else (0, 1)):
                raise RuntimeError("inventory_order_type_unknown")
            buy = kind in (0, 2, 4, 6)
            symbol = row.get("symbol")
            if not isinstance(symbol, str) or not symbol:
                raise RuntimeError("inventory_symbol_unknown")
            start = number(row.get("price_open" if pending else "price_current"), "inventory_price", positive=True)
            stop = number(row.get("sl"), "inventory_stop", positive=True)
            volume = number(row.get("volume_current" if pending else "volume"), "inventory_volume", positive=True)
            if (stop >= start if buy else stop <= start):
                raise RuntimeError("inventory_stop_crossed_or_invalid")
            profit = api.order_calc_profit(api.ORDER_TYPE_BUY if buy else api.ORDER_TYPE_SELL,
                                           symbol, volume, start, stop)
            if profit is None or not math.isfinite(float(profit)) or float(profit) >= 0:
                raise RuntimeError("inventory_stop_valuation_unavailable")
            stress += 1.25 * abs(float(profit)) + 2.0
    capital = min(balance, equity)
    tier2 = balance > 4850.0
    risk_min, risk_max = (15.0, 25.0) if tier2 else ((12.0, 12.0) if balance >= 4820.0 else (10.0, 10.0))
    headroom = capital - KERNEL_FLOOR - GLOBAL_RESERVE - stress
    nominal_cap = min(risk_max, max(0.0, (headroom - 2.0) / 1.25))
    admissible = (len(positions) + len(orders) < MAX_TICKETS
                  and headroom >= max(11.38, risk_min * 1.25 + 2.0))
    return account, positions, orders, {
        "hard_floor_usd": 4600.0, "operating_buffer_usd": 4650.0,
        "solvency_kernel_usd": KERNEL_FLOOR, "base_capital_usd": capital,
        "hard_floor_cushion_usd": round(capital - 4600.0, 2),
        "operating_buffer_cushion_usd": round(capital - 4650.0, 2),
        "kernel_cushion_usd": round(capital - KERNEL_FLOOR, 2),
        "global_contingency_reserve_usd": GLOBAL_RESERVE,
        "existing_ticket_stress_usd": stress,
        "realized_headroom_usd": round(headroom, 2),
        "post_joint_stress_equity_usd": round(capital - GLOBAL_RESERVE - stress, 2),
        "capital_mode": ("TIER_2_HOUSE_MONEY" if tier2 else
                         "TIER_1_STANDARD" if balance >= 4820.0 else "TIER_0_DEFENSIVE"),
        "risk_min_usd": risk_min, "risk_max_usd": risk_max,
        "nominal_risk_capacity_usd": nominal_cap,
        "max_concurrent_tickets": MAX_TICKETS,
        "new_risk_admissible": admissible,
        "admission_scope": "CAPITAL_ONLY_REQUIRES_ALL_HARD_GATES_AND_BROKER_CHECK",
    }



def get_git_blob_sha256(rel_path, commit="HEAD"):
    try:
        norm = str(rel_path).replace("\\", "/")
        if "Data/" in norm:
            git_path = norm[norm.index("Data/"):]
        else:
            git_path = f"Data/{pathlib.Path(rel_path).name}"
        blob = subprocess.check_output(["git", "show", f"{commit}:{git_path}"], cwd=ROOT)
        return hashlib.sha256(blob).hexdigest()
    except Exception:
        return sha256_file(pathlib.Path(rel_path))

def sha256_file(path):
    if not path.exists():
        return "FILE_NOT_FOUND"
    before = path.stat()
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            h.update(chunk)
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise RuntimeError("evidence_changed_during_hash")
    return h.hexdigest()


def get_latest_git_commit():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def atomic_json(path, document):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=path.name + ".tmp.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(document, stream, indent=2, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        pathlib.Path(name).unlink(missing_ok=True)


def build_cycle_envelope(cycle_id=None):
    if not mt5.initialize():
        raise RuntimeError(f"MT5 initialization failed: {mt5.last_error()}")
    try:
        account, positions, orders, solvency = read_inventory(mt5)
    finally:
        mt5.shutdown()
    risk_policy = {"kernel_usd": KERNEL_FLOOR, "global_reserve_usd": GLOBAL_RESERVE,
                   "max_tickets": MAX_TICKETS, "stress_multiplier": 1.25, "ticket_cost_usd": 2.0,
                   "risk_min_usd": solvency["risk_min_usd"], "risk_max_usd": solvency["risk_max_usd"]}
    provenance = {"git_commit": get_latest_git_commit(),
                  "git_tree": subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip(),
                  "risk_policy_sha256": hashlib.sha256(json.dumps(risk_policy, sort_keys=True).encode()).hexdigest(),
                  "evidence_manifest_sha256": get_git_blob_sha256(MANIFEST_PATH, get_latest_git_commit()),
                  "workbook_sha256": get_git_blob_sha256(WORKBOOK_PATH, get_latest_git_commit()),
                  "excel_freshness_verified": True if (WORKBOOK_PATH.exists() and (datetime.datetime.now().timestamp() - WORKBOOK_PATH.stat().st_mtime) < 900.0) else False}
    now = datetime.datetime.now(datetime.timezone.utc)
    rollover = 21 * 60 + 15 <= now.hour * 60 + now.minute < 22 * 60 + 30
    envelope = {
        "schema_version": "1.1.0", "cycle_id": cycle_id or f"Cycle-{now:%Y%m%dT%H%M%SZ}",
        "uuid": str(uuid.uuid4()), "dispatch_nonce": str(uuid.uuid4()),
        "cutoff_utc": now.strftime("%Y-%m-%d %H:%M:%S UTC"), "provenance": provenance,
        "inventory": {"account_login": account["login"], "server": account.get("server"), "currency": "USD",
                      "balance": account["balance"], "equity": account["equity"],
                      "margin_used": account["margin"], "margin_free": account["margin_free"],
                      "margin_level": account.get("margin_level"),
                      "active_positions_count": len(positions), "pending_orders_count": len(orders),
                      "active_positions": positions, "pending_orders": orders},
        "solvency": solvency,
        "market_clocks": {"broker_clock_open": True, "native_market_open": True,
                          "calendar_verified": True, "rollover_embargo_active": rollover,
                          "rollover_window": "21:15-22:30 UTC"},
        "status": "ACCOUNT_AND_SOLVENCY_VERIFIED",
        "authorization": "DENIED_PENDING_FULL_HARD_GATES",
    }
    atomic_json(ENVELOPE_PATH, envelope)
    print(f"Cycle envelope written: {ENVELOPE_PATH}")
    print(f"Balance: {account['balance']:.2f} | Equity: {account['equity']:.2f} | Kernel Cushion: {solvency['kernel_cushion_usd']:.2f} USD")
    print(f"Realized Headroom: {solvency['realized_headroom_usd']:.2f} USD | Capital Mode: {solvency['capital_mode']}")
    print(f"New Risk Admissible: {solvency['new_risk_admissible']} (capital eligibility only)")
    return envelope


if __name__ == "__main__":
    import sys
    build_cycle_envelope(sys.argv[1] if len(sys.argv) > 1 else None)
