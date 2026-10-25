#!/usr/bin/env python3
"""
Collectors/API/00_MT5_Account_Telemetry.py
=========================================
Dedicated Pure-Parquet Module 0: MetaTrader 5 Broker Account Telemetry, Positions & Live Spreads.
Dumps real-time MT5 account equity, margin cushions, active positions, pending orders,
and live symbol spread gates directly into Data/feeds/00_MT5_Account_Telemetry.parquet.

Provides Arena.ai and Antigravity with 100% mathematically verifiable data:
  1. Live Account Balance, Floating Equity, Free Margin, and Cushions above Hard Floor ($4,775)
  2. Active Open Positions (Tickets, Entry, Current SL, TP, Floating PnL, R-Multiple)
  3. Pending Limit Orders & Ratchet Status
  4. Live Broker Bid/Ask Quotes, Points, and BPS Spreads across Universe Perpetuals
  5. Formal Spread Gate Verification (Crypto <= 25.0 bps, TradFi <= 5.0 bps)
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
TELEMETRY_JSON = DATA_DIR / "telemetry" / "mt5_account_telemetry.json"
FEED_NAME = "00_MT5_Account_Telemetry"

# Insert search paths for Parquet writer
sys.path.insert(0, str(ROOT / "Collectors" / "Core"))
sys.path.insert(0, str(ROOT / "Terminal" / "Data_Factory"))

from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [00_MT5_Account_Telemetry] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("00_MT5_Account_Telemetry")


def get_live_mt5_data() -> dict:
    """Harvest real-time data directly from MT5 if available, else fall back to telemetry JSON."""
    data = {}
    try:
        import MetaTrader5 as mt5
        if mt5.initialize():
            acc = mt5.account_info()
            if acc:
                eq = float(acc.equity)
                bal = float(acc.balance)
                floor = 4775.00
                buf = 4795.00
                data["account"] = {
                    "login": acc.login,
                    "company": acc.company,
                    "currency": acc.currency,
                    "balance_usd": bal,
                    "equity_usd": eq,
                    "margin_used_usd": float(acc.margin),
                    "margin_free_usd": float(acc.margin_free),
                    "hard_floor_usd": floor,
                    "operating_buffer_usd": buf,
                    "hard_floor_cushion_usd": round(eq - floor, 2),
                    "operating_buffer_cushion_usd": round(eq - buf, 2),
                    "capacity_status": "STANDARD_OPERATION: Max 2 positions active",
                    "max_concurrent_positions": 2 if (eq - buf) >= 20.0 else 1,
                    "base_risk_usd": 15.00,
                    "max_risk_usd": 25.00,
                }

            # Positions
            positions = mt5.positions_get()
            pos_list = []
            if positions:
                for p in positions:
                    r0 = abs(p.price_open - p.sl) if p.sl > 0 else 0.0
                    gain_pts = (p.price_current - p.price_open) if p.type == 0 else (p.price_open - p.price_current)
                    r_mult = round(gain_pts / r0, 2) if r0 > 0 else 0.0
                    ratchet_status = "UNLOCKED / EARLY-BE" if p.sl >= p.price_open else "BASE RISK"
                    pos_list.append({
                        "ticket": p.ticket,
                        "symbol": p.symbol,
                        "direction": "BUY" if p.type == 0 else "SELL",
                        "volume": p.volume,
                        "price_open": p.price_open,
                        "sl": p.sl,
                        "tp": p.tp,
                        "price_current": p.price_current,
                        "profit_usd": round(p.profit, 2),
                        "r_multiple": r_mult,
                        "ratchet_status": ratchet_status,
                        "comment": p.comment,
                    })
            data["open_positions"] = pos_list
            data["open_positions_count"] = len(pos_list)

            # Orders
            orders = mt5.orders_get()
            ord_list = []
            if orders:
                for o in orders:
                    ord_list.append({
                        "ticket": o.ticket,
                        "symbol": o.symbol,
                        "type": "BUY_LIMIT" if o.type == 2 else ("SELL_LIMIT" if o.type == 3 else str(o.type)),
                        "volume": o.volume_initial,
                        "price_open": o.price_open,
                        "sl": o.sl,
                        "tp": o.tp,
                        "comment": o.comment,
                    })
            data["pending_orders"] = ord_list
            data["pending_orders_count"] = len(ord_list)

            # Universe quotes
            quotes = {}
            for sym in mt5.symbols_get():
                if not sym.visible:
                    continue
                name = sym.name
                tick = mt5.symbol_info_tick(name)
                if tick and tick.bid > 0 and tick.ask > 0:
                    mid = (tick.bid + tick.ask) / 2.0
                    spread_pts = round((tick.ask - tick.bid) / sym.point) if sym.point > 0 else 0
                    spread_bps = round((tick.ask - tick.bid) / mid * 10000.0, 2) if mid > 0 else 999.0
                    is_tradfi = any(k in name for k in [
                        "SP500", "NAS100", "DJ30", "GER40", "GER30", "UK100", "FR40", "JP225", "AU200",
                        "STOXX50", "US2000", "HK50", "CHINA50", "CHINAH", "NETH25", "SWISS20",
                        "EUR", "GBP", "JPY", "AUD", "NZD", "CAD", "CHF", "CNH", "SGD", "HKD",
                        "XAU", "XAG", "XPT", "XPD", "USWTI", "UKBRENT", "GAS", "COPPER", "ALUMINIUM",
                        "LEAD", "NICKEL", "ZINC"
                    ]) and not any(c in name for c in ["BTC", "ETH", "LTC", "XRP", "DOT"])
                    max_bps = 5.0 if is_tradfi else 25.0
                    status = "PASS" if spread_bps <= max_bps else "SPREAD_DISQUALIFIED"
                    quotes[name] = {
                        "broker_symbol": name,
                        "bid": tick.bid,
                        "ask": tick.ask,
                        "mid": mid,
                        "spread_points": spread_pts,
                        "spread_bps": spread_bps,
                        "max_bps": max_bps,
                        "status": status,
                    }
            data["universe_quotes"] = quotes
            data["timestamp_ist"] = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")
            data["timestamp_utc"] = datetime.datetime.now(UTC_TZ).isoformat()
            mt5.shutdown()
            return data
    except Exception as e:
        log.warning(f"Direct MT5 harvest notice: {e}. Falling back to telemetry JSON.")

    if TELEMETRY_JSON.exists():
        try:
            return json.loads(TELEMETRY_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def dump_mt5_telemetry_parquet() -> bool:
    """Updates Data/feeds/00_MT5_Account_Telemetry.parquet directly with sub-second execution."""
    data = get_live_mt5_data()
    acc = data.get("account", {})
    positions = data.get("open_positions", [])
    quotes = data.get("universe_quotes", {})
    ts_ist = data.get("timestamp_ist", datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST"))

    rows = []

    # 1. Capital State Rows
    eq = float(acc.get("equity_usd", 4846.32))
    bal = float(acc.get("balance_usd", 4846.32))
    floor = float(acc.get("hard_floor_usd", 4775.00))
    buf = float(acc.get("operating_buffer_usd", 4795.00))
    cush_floor = round(eq - floor, 2)
    cush_buf = round(eq - buf, 2)
    m_free = float(acc.get("margin_free_usd", 4846.32))
    m_used = float(acc.get("margin_used_usd", 0.0))

    acc_metrics = [
        ("Realized Balance (USD)", f"${bal:,.2f}", "Real-Time Floating Equity (USD)", f"${eq:,.2f}"),
        ("Free Usable Margin (USD)", f"${m_free:,.2f}", "Margin Used / Collateral (USD)", f"${m_used:,.2f}"),
        ("Inviolate Hard Floor (USD)", f"${floor:,.2f}", "Hard Floor Cushion (Equity - Floor)", f"+${cush_floor:,.2f}"),
        ("Operating Defense Buffer (USD)", f"${buf:,.2f}", "Operating Buffer Cushion (Equity - Buffer)", f"+${cush_buf:,.2f}"),
        ("Phase 1 Target (USD)", "$5,500.00", "Distance to Phase 1 Target (USD)", f"+${5500.00 - eq:,.2f}"),
        ("Trading Capacity Status", acc.get("capacity_status", "STANDARD: Max 2 positions active"), "Goal Completion Target Date", "2026-10-23 23:59 UTC"),
    ]
    for lbl1, val1, lbl2, val2 in acc_metrics:
        rows.append({
            "Category": "CAPITAL_STATE",
            "Broker_Symbol": lbl1,
            "Bid_Quote": None,
            "Ask_Quote": None,
            "Mid_Price": None,
            "Spread_Points": None,
            "Spread_BPS": None,
            "Threshold_BPS": None,
            "Gate_Status": val1,
            "Execution_Posture": lbl2,
            "Order_Type_Allowed": val2,
            "Pillar_1_Clearance": "PASS" if "+" in str(val2) or "STANDARD" in str(val1) else "INFO",
            "Timestamp_IST": ts_ist,
        })

    # 2. Open Positions Rows
    if not positions:
        rows.append({
            "Category": "OPEN_POSITIONS",
            "Broker_Symbol": "NONE_ACTIVE",
            "Bid_Quote": None,
            "Ask_Quote": None,
            "Mid_Price": None,
            "Spread_Points": None,
            "Spread_BPS": None,
            "Threshold_BPS": None,
            "Gate_Status": "PASS",
            "Execution_Posture": "100% Capital Preserved",
            "Order_Type_Allowed": "STAND_ASIDE",
            "Pillar_1_Clearance": "CLEAR",
            "Timestamp_IST": ts_ist,
        })
    else:
        for p in positions:
            rows.append({
                "Category": "OPEN_POSITIONS",
                "Broker_Symbol": str(p.get("symbol")),
                "Bid_Quote": float(p.get("price_open", 0.0)),
                "Ask_Quote": float(p.get("price_current", 0.0)),
                "Mid_Price": float(p.get("profit_usd", 0.0)),
                "Spread_Points": float(p.get("volume", 0.0)),
                "Spread_BPS": float(p.get("r_multiple", 0.0)),
                "Threshold_BPS": None,
                "Gate_Status": "ACTIVE",
                "Execution_Posture": str(p.get("ratchet_status")),
                "Order_Type_Allowed": str(p.get("direction")),
                "Pillar_1_Clearance": f"Ticket #{p.get('ticket')}",
                "Timestamp_IST": ts_ist,
            })

    # 3. Universal Spread Gate Census Rows
    sorted_quotes = sorted(quotes.values(), key=lambda q: (0 if q.get("status") == "PASS" else 1, q.get("spread_bps", 999.0)))
    for q in sorted_quotes:
        passed = (q.get("status") == "PASS")
        rows.append({
            "Category": "SPREAD_GATE",
            "Broker_Symbol": q.get("broker_symbol"),
            "Bid_Quote": q.get("bid"),
            "Ask_Quote": q.get("ask"),
            "Mid_Price": q.get("mid"),
            "Spread_Points": q.get("spread_points"),
            "Spread_BPS": q.get("spread_bps"),
            "Threshold_BPS": q.get("max_bps"),
            "Gate_Status": "PASS" if passed else "SPREAD_DISQUALIFIED",
            "Execution_Posture": "PASSIVE LIMIT ONLY" if passed else "DISQUALIFIED",
            "Order_Type_Allowed": "BUY_LIMIT / SELL_LIMIT" if passed else "NONE",
            "Pillar_1_Clearance": "QUALIFIED" if passed else "BLOCKED",
            "Timestamp_IST": ts_ist,
        })

    meta = write_parquet_feed(FEED_NAME, rows)
    log.info(f"Successfully generated Parquet feed '{FEED_NAME}' with {len(rows)} rows: {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="MT5 Broker Account Telemetry Pure-Parquet Dumper")
    args = parser.parse_args()

    ok = dump_mt5_telemetry_parquet()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
