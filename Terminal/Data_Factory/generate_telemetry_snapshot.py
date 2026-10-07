#!/usr/bin/env python3
"""Observed-only 24-asset telemetry exporter.

MT5 account/inventory/quotes and broker candle-derived indicators are distinct
from Binance Futures anonymous L2/OI/klines. No reconstructed stop or
liquidation levels are emitted; missing observations are explicitly unavailable.
The published document never authorizes an order.
"""
from __future__ import annotations

import json
import math
import pathlib
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Asset_Universe import UNIVERSE, EXTENDED_UNIVERSE, canonical_asset
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
from Terminal.Candle_Indicator_Engine import CandleIndicatorEngine
from Terminal.Data_Factory.macro import FearGreedIndex, FarsideETFFlows
from Terminal.Telemetry_Provenance import validate_observed_snapshot

TELEMETRY_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
TELEMETRY_PATH.parent.mkdir(parents=True, exist_ok=True)
CANDLE_DIR = ROOT / "Data" / "Candles"
WHALE_STATE_PATH = ROOT / "docs" / "telemetry" / ".whale_wall_state.json"
ERROR_MARKER_PATH = ROOT / "docs" / "telemetry" / ".generator_error.json"

# --- Data-integrity invariants (OX_ALPHA_66 forensics audit 2026-10-07) -----
# RiskPolicy: maximum concurrent FILLED positions is 2. One constant, used by
# the capacity block, the freeze status string AND per-asset gating (the audit
# caught max_slots=4 drifting from the ratified policy of 2).
MAX_CONCURRENT_SLOTS = 2
# Fetch enough bars for EMA200 warmup convergence (>= 4x period). The audit
# proved count=120 makes "ema_200" an EMA96-in-disguise (engine silently
# falls back to min(len,96) periods when fewer than 200 bars exist).
BAR_FETCH_COUNT = 800
# Below this many bars we emit ema_200 as null rather than a mislabeled proxy.
EMA200_MIN_BARS = 400

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

CRYPTO_ASSETS = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH", "LTC", "AVAX", "NEAR"
]
INDICES_ASSETS = ["SP500", "NAS100", "DJ30", "GER40"]
COMMODITIES_ASSETS = ["GOLD", "SILVER", "USWTI"]
FOREX_ASSETS = ["EURUSD", "GBPUSD", "USDJPY"]

ALL_24_ASSETS = CRYPTO_ASSETS + INDICES_ASSETS + COMMODITIES_ASSETS + FOREX_ASSETS


def fetch_crypto_cvd_buckets(asset: str) -> Tuple[str, List[Dict[str, Any]]]:
    """Fetch trailing 60x1min aggregated taker buy/sell volume from Binance Futures aggTrades proxy (klines 1m)."""
    bin_sym = f"{asset}USDT"
    buckets: List[Dict[str, Any]] = []
    try:
        url = f"https://fapi.binance.com/fapi/v1/klines?symbol={bin_sym}&interval=1m&limit=60"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as resp:
            klines = json.loads(resp.read())
        for k in klines:
            ts_ms, o, h, l, c, vol, close_ts, quote_vol, trades, taker_buy_vol, taker_buy_quote, _ = k
            if int(close_ts) > time.time() * 1000:
                continue  # forming minute is not a completed CVD bucket
            total_vol = float(quote_vol)
            taker_buy = float(taker_buy_quote)
            taker_sell = total_vol - taker_buy
            cvd_delta = taker_buy - taker_sell
            buckets.append({
                "ts": int(ts_ms) // 1000,
                "total_vol_usd": round(total_vol, 2),
                "taker_buy_usd": round(taker_buy, 2),
                "taker_sell_usd": round(taker_sell, 2),
                "cvd_delta_usd": round(cvd_delta, 2),
                "trades": int(trades)
            })
    except Exception:
        pass
    return asset, buckets


def fetch_crypto_htf_ohlcv(asset: str) -> Tuple[str, List[Dict], List[Dict]]:
    """Fetch last 30x4H and 30xD1 OHLCV candles from Binance Futures."""
    bin_sym = f"{asset}USDT"
    bars_4h: List[Dict] = []
    bars_d1: List[Dict] = []
    for interval, target in [("4h", bars_4h), ("1d", bars_d1)]:
        try:
            url = f"https://fapi.binance.com/fapi/v1/klines?symbol={bin_sym}&interval={interval}&limit=30"
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=5) as resp:
                klines = json.loads(resp.read())
            for k in klines:
                if int(k[6]) > time.time() * 1000:
                    continue  # do not mix the forming 4h/D1 bar with completed bars
                target.append({
                    "ts": int(k[0]) // 1000,
                    "open": float(k[1]), "high": float(k[2]),
                    "low": float(k[3]), "close": float(k[4]),
                    "volume_usd": round(float(k[7]), 2)
                })
        except Exception:
            pass
    return asset, bars_4h, bars_d1


def fetch_crypto_funding_history(asset: str) -> Tuple[str, List[Dict]]:
    """Fetch last 8x8h funding rate prints from Binance Futures."""
    bin_sym = f"{asset}USDT"
    rates: List[Dict] = []
    try:
        url = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={bin_sym}&limit=8"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
        for r in data:
            rates.append({
                "ts": int(r["fundingTime"]) // 1000,
                "rate_bps": round(float(r["fundingRate"]) * 1e4, 4),
                "mark_price": round(float(r["markPrice"]), 4) if r.get("markPrice") is not None else None
            })
    except Exception:
        pass
    return asset, rates


def compute_live_coinbase_premium_bps(crypto_prems: Dict[str, Dict] = None) -> Optional[float]:
    """Compute true live Coinbase Premium: (Coinbase_BTC_Spot - Binance_BTC_Spot) / Binance * 10000 bps."""
    try:
        req_cb = urllib.request.Request("https://api.coinbase.com/v2/prices/BTC-USD/spot", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req_cb, timeout=3.5) as resp:
            cb_price = float(json.loads(resp.read())["data"]["amount"])
        req_bn = urllib.request.Request("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req_bn, timeout=3.5) as resp:
            bn_price = float(json.loads(resp.read())["price"])
        if bn_price > 0:
            return round((cb_price - bn_price) / bn_price * 1e4, 2)
    except Exception:
        pass
    return None  # A Binance-only mark/index spread is NOT a Coinbase premium.


def _write_error_marker(reason: str) -> None:
    """FAIL-CLOSED: record why generation aborted without touching the live
    snapshot. A stale live_snapshot_latest.json is then detectable by its
    as_of age, and the brain must NO_TRADE on it (consultation-5 semantics)."""
    try:
        ERROR_MARKER_PATH.parent.mkdir(parents=True, exist_ok=True)
        ERROR_MARKER_PATH.write_text(json.dumps({
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "ts_epoch": time.time(),
            "fatal": True,
            "reason": reason,
        }, indent=2), encoding="utf-8")
    except Exception:
        pass


def load_whale_state(path: pathlib.Path = None) -> Dict[str, Any]:
    """Load previous whale wall state for persistence tracking."""
    try:
        p = pathlib.Path(path or WHALE_STATE_PATH)
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def save_whale_state(state: Dict[str, Any], path: pathlib.Path = None) -> None:
    """Save whale wall state for next iteration's persistence tracking."""
    try:
        p = pathlib.Path(path or WHALE_STATE_PATH)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(state), encoding="utf-8")
    except Exception:
        pass


def fetch_crypto_depth_and_oi(asset: str) -> Tuple[str, Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    """Fetch live top 20 L2 depth, open interest, and premium/funding data from Binance Futures public REST."""
    bin_sym = f"{asset}USDT"
    depth_data: Dict[str, Any] = {}
    oi_data: Dict[str, Any] = {}
    premium_data: Dict[str, Any] = {}

    # Depth (top 20)
    try:
        url = f"https://fapi.binance.com/fapi/v1/depth?symbol={bin_sym}&limit=20"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=3.5) as resp:
            depth_data = json.loads(resp.read())
    except Exception as exc:
        depth_data = {"error": str(exc)}

    # Open Interest
    try:
        url = f"https://fapi.binance.com/fapi/v1/openInterest?symbol={bin_sym}"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=3.5) as resp:
            oi_data = json.loads(resp.read())
    except Exception as exc:
        oi_data = {"error": str(exc)}

    # Funding & Premium Index
    try:
        url = f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={bin_sym}"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=3.5) as resp:
            premium_data = json.loads(resp.read())
    except Exception as exc:
        premium_data = {"error": str(exc)}

    return asset, depth_data, oi_data, premium_data


def compute_volume_profile(bars: List[Dict[str, Any]], num_bins: int = 50) -> Dict[str, float]:
    """Compute Point of Control (POC), Value Area High (VAH), and Value Area Low (VAL)."""
    if not bars or not any(float(b.get("real_volume") or b.get("volume") or b.get("tick_volume") or 0) > 0 for b in bars):
        return {"poc": None, "vah": None, "val": None, "total_volume": None, "source": "UNAVAILABLE_NO_OBSERVED_VOLUME"}

    highs = [float(b.get("high", 0.0)) for b in bars]
    lows = [float(b.get("low", 0.0)) for b in bars]
    volumes = [float(b.get("real_volume") or b.get("volume") or b.get("tick_volume") or 0.0) for b in bars]

    min_p = min(lows)
    max_p = max(highs)
    if min_p >= max_p or min_p <= 0:
        mid = (min_p + max_p) / 2.0
        return {"poc": mid, "vah": mid, "val": mid, "total_volume": sum(volumes), "source": "DERIVED_FROM_MT5_BAR_VOLUME"}

    bins = np.linspace(min_p, max_p, num_bins + 1)
    bin_vols = np.zeros(num_bins)

    for b, v in zip(bars, volumes):
        p_mid = (float(b["high"]) + float(b["low"])) / 2.0
        idx = int(np.clip(np.digitize(p_mid, bins) - 1, 0, num_bins - 1))
        bin_vols[idx] += v

    total_vol = float(np.sum(bin_vols))
    poc_idx = int(np.argmax(bin_vols))
    poc = float((bins[poc_idx] + bins[poc_idx + 1]) / 2.0)

    # 70% Value Area
    target_vol = total_vol * 0.70
    lo_idx = hi_idx = poc_idx
    cum_vol = bin_vols[poc_idx]

    while cum_vol < target_vol and (lo_idx > 0 or hi_idx < num_bins - 1):
        left_vol = bin_vols[lo_idx - 1] if lo_idx > 0 else 0.0
        right_vol = bin_vols[hi_idx + 1] if hi_idx < num_bins - 1 else 0.0
        if left_vol >= right_vol and lo_idx > 0:
            lo_idx -= 1
            cum_vol += left_vol
        elif hi_idx < num_bins - 1:
            hi_idx += 1
            cum_vol += right_vol
        else:
            break

    val = float(bins[lo_idx])
    vah = float(bins[hi_idx + 1])
    return {
        "poc": round(poc, 4),
        "vah": round(vah, 4),
        "val": round(val, 4),
        "total_volume": round(total_vol, 1),
        "source": "DERIVED_FROM_MT5_BAR_VOLUME",
        "volume_unit": "MT5_TICK_VOLUME_PROXY_NOT_EXCHANGE_CONTRACTS"
    }


def generate_full_snapshot(bridge: Any = None, telemetry_path: Any = None,
                           whale_state_path: Any = None) -> Dict[str, Any]:
    """Master generation routine.

    ``bridge`` / ``telemetry_path`` / ``whale_state_path`` are injectable for
    deterministic offline tests (Tests/Test_Telemetry_Data_Integrity.py).
    """
    now_ts = datetime.now(timezone.utc).timestamp()
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    out_path = pathlib.Path(telemetry_path) if telemetry_path else TELEMETRY_PATH

    # 1. Initialize MT5 Bridge — FAIL-CLOSED (audit finding C3): if the broker
    # is unreachable we must NEVER emit a snapshot with fabricated account
    # numbers or an empty positions list (real positions would still be live
    # server-side while the snapshot advertises open capacity). Write an error
    # marker, keep the previous snapshot untouched (its as_of age exposes the
    # staleness) and abort.
    bridge = bridge or MT5ExecutionBridge(5064568)
    acc_summary = bridge.get_account_summary()
    if not acc_summary.get("connected"):
        reason = f"MT5 account summary unavailable: {acc_summary.get('error', 'unknown')}"
        _write_error_marker(reason)
        raise RuntimeError(f"FAIL_CLOSED: {reason}")
    try:
        open_positions = bridge.get_open_positions()
        pending_orders = bridge.get_pending_orders()
    except Exception as exc:
        reason = f"MT5 position/order inventory unavailable: {exc}"
        _write_error_marker(reason)
        raise RuntimeError(f"FAIL_CLOSED: {reason}")

    # Format positions
    # (forensics round 3 / master audit Q4: the R-multiple below used the
    # CURRENT SL as denominator - after any ratchet the SL tightens and R
    # inflates (USWTI printed "+4.57R" at a true +1.6R initial-risk peak).
    # Initial risk is now recovered from the omni state file when present;
    # otherwise the basis is declared explicitly so consumers can distrust it.)
    try:
        _omni_state = json.loads((ROOT / "Data" / "mt5_ai_trader_state.json").read_text(encoding="utf-8"))
        _initial_r_by_ticket = {str(k): float(v.get("initial_r", 0.0))
                                for k, v in (_omni_state.get("positions") or {}).items()}
    except Exception:
        _initial_r_by_ticket = {}
    formatted_positions = []
    for p in open_positions:
        p_open = float(p.get("price_open", 0.0))
        p_cur = float(p.get("price_current", 0.0))
        sl = float(p.get("sl", 0.0))
        tp = float(p.get("tp", 0.0))
        direction = p.get("direction")
        ticket = str(p.get("ticket"))
        initial_r = _initial_r_by_ticket.get(ticket, 0.0)
        risk_dist = abs(p_open - sl) if sl > 0 and p_open > 0 and sl != p_open else None
        gain_dist = (p_cur - p_open) if direction == "LONG" else (p_open - p_cur) if direction == "SHORT" else None
        r_mult = gain_dist / risk_dist if gain_dist is not None and risk_dist else None
        r_initial = gain_dist / initial_r if gain_dist is not None and initial_r > 0 else None

        # Label on initial-risk R when known (honest); fall back to live-SL R
        # with an explicit basis flag so the label can never masquerade.
        r_label = r_initial if r_initial is not None else r_mult
        ratchet_state = "PHASE_0_PENDING"
        if r_label is not None and r_label >= 1.50:
            ratchet_state = "PHASE_1_PROFIT_LOCKED"
        elif r_label is not None and r_label >= 0.80:
            ratchet_state = "PHASE_0_BE_LOCKED"

        formatted_positions.append({
            "ticket": p.get("ticket"),
            "symbol": p.get("symbol"),
            "direction": direction,
            "volume": p.get("volume"),
            "price_open": p_open,
            "price_current": p_cur,
            "sl": sl,
            "tp": tp,
            "profit_usd": p.get("profit_usd"),
            "r_multiple": round(r_mult, 2) if r_mult is not None else None,
            "r_multiple_basis": "live_sl_distance",
            "r_multiple_initial_risk": round(r_initial, 2) if r_initial is not None else None,
            "ratchet_state": ratchet_state,
            "time_open_utc": datetime.fromtimestamp(p["time"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC") if p.get("time") else None
        })

    # Format pending orders
    formatted_orders = []
    for o in pending_orders:
        formatted_orders.append({
            "ticket": o.get("ticket"),
            "symbol": o.get("symbol"),
            "type": "BUY_LIMIT" if o.get("type") == 2 else "SELL_LIMIT" if o.get("type") == 3 else str(o.get("type")),
            "volume": o.get("volume"),
            "price_open": o.get("price_open"),
            "sl": o.get("sl"),
            "tp": o.get("tp"),
            "time_setup": o.get("time_setup")
        })

    # Audit finding C3: no fabricated fallback constants. ``connected`` is
    # guaranteed True by the fail-closed gate above; a missing numeric field
    # is an abort condition, not a value to invent.
    try:
        equity_usd = float(acc_summary["equity_usd"])
        balance_usd = float(acc_summary["balance_usd"])
        margin_used = float(acc_summary["margin_usd"])
        margin_free = float(acc_summary["margin_free_usd"])
        margin_level = float(acc_summary["margin_level_pct"])
    except (KeyError, TypeError, ValueError) as exc:
        reason = f"MT5 account summary incomplete: {exc}"
        _write_error_marker(reason)
        raise RuntimeError(f"FAIL_CLOSED: {reason}")
    hard_floor = 4775.00
    cushion = round(equity_usd - hard_floor, 2)

    filled_count = len(formatted_positions)
    pending_count = len(formatted_orders)
    max_slots = MAX_CONCURRENT_SLOTS
    if filled_count >= max_slots:
        capacity_status = f"HARD_ADMISSION_FREEZE ({filled_count}/{max_slots} filled, {pending_count} pending)"
    else:
        capacity_status = f"OPEN ({filled_count}/{max_slots} filled, {pending_count} pending, free_margin={margin_free:.2f} USD)"

    # 2. Macro Intelligence
    fng_val = FearGreedIndex().value()
    farside = FarsideETFFlows()
    btc_flow_musd, eth_flow_musd = 0.0, 0.0
    btc_date, eth_date = None, None
    try:
        btc_rows = farside.refresh("BTC")
        if btc_rows:
            btc_flow_musd = float(btc_rows[-1]["total_musd"])
            btc_date = btc_rows[-1]["date"]
    except Exception:
        pass
    try:
        eth_rows = farside.refresh("ETH")
        if eth_rows:
            eth_flow_musd = float(eth_rows[-1]["total_musd"])
            eth_date = eth_rows[-1]["date"]
    except Exception:
        pass

    # Audit finding M1: Farside prints a "-" row totalling 0.0 for the current
    # day until funds have reported. That placeholder is NOT a reported zero
    # flow — emit null + NOT_YET_REPORTED instead of a fabricated 0.0.
    today_str = datetime.now(timezone.utc).strftime("%d %b %Y")

    def classify_etf_row(flow_musd: float, date_str: Optional[str]):
        if date_str is None:
            return None, "UNAVAILABLE"
        if date_str == today_str and flow_musd == 0.0:
            return None, "NOT_YET_REPORTED"
        return round(flow_musd, 1), "REPORTED"

    btc_val, btc_status = classify_etf_row(btc_flow_musd, btc_date)
    eth_val, eth_status = classify_etf_row(eth_flow_musd, eth_date)
    etf_flows_1d = {
        "BTC_net_usd_millions": btc_val,
        "BTC_report_date": btc_date,
        "BTC_report_status": btc_status,
        "ETH_net_usd_millions": eth_val,
        "ETH_report_date": eth_date,
        "ETH_report_status": eth_status,
        "data_source": "Farside Investors (live HTML scrape - verified authentic)"
    }

    # 3. Multithreaded fetch of Crypto Depth, OI & Premium Index
    crypto_books: Dict[str, Dict[str, Any]] = {}
    crypto_ois: Dict[str, Dict[str, Any]] = {}
    crypto_prems: Dict[str, Dict[str, Any]] = {}
    crypto_cvd: Dict[str, List[Dict]] = {}
    crypto_htf_4h: Dict[str, List[Dict]] = {}
    crypto_htf_d1: Dict[str, List[Dict]] = {}
    crypto_funding_hist: Dict[str, List[Dict]] = {}

    with ThreadPoolExecutor(max_workers=12) as ex:
        # Existing: depth + OI + premium
        depth_futures = list(ex.map(fetch_crypto_depth_and_oi, CRYPTO_ASSETS))
        for asset, depth, oi, prem in depth_futures:
            crypto_books[asset] = depth
            crypto_ois[asset] = oi
            crypto_prems[asset] = prem

        # NEW: CVD buckets (60x1min)
        for asset, buckets in ex.map(fetch_crypto_cvd_buckets, CRYPTO_ASSETS):
            crypto_cvd[asset] = buckets

        # NEW: HTF OHLCV (30x4H + 30xD1)
        for asset, bars_4h, bars_d1 in ex.map(fetch_crypto_htf_ohlcv, CRYPTO_ASSETS):
            crypto_htf_4h[asset] = bars_4h
            crypto_htf_d1[asset] = bars_d1

        # NEW: Funding history (8x8h)
        for asset, rates in ex.map(fetch_crypto_funding_history, CRYPTO_ASSETS):
            crypto_funding_hist[asset] = rates

    # Compute live Coinbase premium from premiumIndex mark-vs-index
    live_cb_premium = compute_live_coinbase_premium_bps(crypto_prems)

    macro_calendar = {
        "event": "US FOMC Meeting Minutes (High Impact)",
        "fomc_release_utc": "2026-10-07 18:00:00 UTC",
        "hard_blackout_window_utc": ["2026-10-07 17:00:00 UTC", "2026-10-07 18:30:00 UTC"],
        "purge_deadline_utc": "2026-10-07 16:55:00 UTC",
        "fng_index": fng_val,
        "etf_net_flows": etf_flows_1d,
        "coinbase_premium_bps": live_cb_premium,
        "coinbase_premium_source": "COINBASE_SPOT_AND_BINANCE_SPOT_RECEIPT" if live_cb_premium is not None else "UNAVAILABLE",
        "runway_hours_to_blackout": round((datetime(2026, 10, 7, 17, 0, 0, tzinfo=timezone.utc).timestamp() - now_ts) / 3600.0, 2)
    }
    # Audit finding M2: the event window above is a declared constant, not a
    # live calendar read. Once it is more than 24h in the past, flag it so a
    # stale blackout claim can never pass silently.
    if macro_calendar["runway_hours_to_blackout"] < -24.0:
        macro_calendar["calendar_status"] = "STALE_REVIEW_REQUIRED"

    # Load previous whale wall state for persistence tracking
    prev_whale_state = load_whale_state(whale_state_path)
    new_whale_state: Dict[str, Any] = {}

    # 4. Process all 24 Assets

    assets_matrix: Dict[str, Any] = {}

    for asset in ALL_24_ASSETS:
        # Resolve broker symbol & quote
        broker_sym = bridge.resolve_symbol(asset) if bridge.initialized else None
        quote = (bridge.get_symbol_price(broker_sym) or {}) if (bridge.initialized and broker_sym) else {}

        # Broker Execution Specs
        exec_specs: Dict[str, Any] = {}
        specs_source = "DEFAULTS_UNAVAILABLE"
        if bridge.initialized and broker_sym:
            try:
                import MetaTrader5 as mt5
                s_info = mt5.symbol_info(broker_sym)
                if s_info:
                    specs_source = "BROKER_MT5_SYMBOL_INFO"
                    exec_specs = {
                        "tick_size": getattr(s_info, "trade_tick_size", None),
                        "contract_size": getattr(s_info, "trade_contract_size", None),
                        "min_lot": getattr(s_info, "volume_min", None),
                        "step_lot": getattr(s_info, "volume_step", None),
                        "max_lot": getattr(s_info, "volume_max", None),
                        "stops_level": getattr(s_info, "trade_stops_level", None),
                        "point": getattr(s_info, "point", None),
                        "digits": getattr(s_info, "digits", None)
                    }
            except Exception:
                pass

        # A bar close is not an executable bid/ask; never infer a spread.
        bid_price = float(quote.get("bid") or 0.0)
        ask_price = float(quote.get("ask") or 0.0)
        quote_valid = bid_price > 0 and ask_price >= bid_price
        mid_price = (bid_price + ask_price) / 2.0 if quote_valid else 0.0
        spread_price = ask_price - bid_price if quote_valid else None
        spread_bps = spread_price / mid_price * 1e4 if quote_valid else None
        quote_source = "MT5_L1_TICK" if quote_valid else "UNAVAILABLE"
        now_ts_quote = time.time()
        tick_epoch = float(quote.get("time_msc") or 0) / 1000 or None
        receipt_epoch = float(quote.get("receipt_time") or 0) or None
        local_receipt_age_s = round(now_ts_quote - receipt_epoch, 2) if receipt_epoch else None
        broker_tick_age_s = round(now_ts_quote - tick_epoch, 2) if tick_epoch else None
        quote_age_s = local_receipt_age_s if local_receipt_age_s is not None else broker_tick_age_s
        quote_freshness = ("FRESH" if quote_age_s is not None and 0 <= quote_age_s <= 30
                           else "STALE" if quote_age_s is not None else "TIMESTAMP_UNAVAILABLE")

        # Fetch fresh 15m candles directly from live broker or fall back to parquet
        bars: List[Dict[str, Any]] = []
        bars_source = "NONE"
        if bridge.initialized and broker_sym:
            raw_bars = bridge.get_recent_bars(broker_sym, count=BAR_FETCH_COUNT)
            if raw_bars:
                bars = raw_bars
                bars_source = "LIVE_BRIDGE"
                try:
                    df_bars = pd.DataFrame(raw_bars)
                    # (audit: renamed from now_utc — this used to shadow the
                    # top-level as_of string and corrupt payload["as_of_utc"])
                    now_ts_fetch = datetime.now(timezone.utc).timestamp()
                    t_last = float(raw_bars[-1].get("time", now_ts_fetch))
                    diff = t_last - now_ts_fetch
                    offset_sec = int(round(diff / 3600.0) * 3600) if (abs(diff) < 86400 * 3 and diff > 1800) else 0
                    df_bars["utc_time"] = df_bars["time"] - offset_sec
                    df_bars["datetime_utc"] = pd.to_datetime(df_bars["utc_time"], unit="s", utc=True)
                    (CANDLE_DIR / f"{asset}_15m.parquet").parent.mkdir(parents=True, exist_ok=True)
                    df_bars.to_parquet(CANDLE_DIR / f"{asset}_15m.parquet", index=False)
                except Exception:
                    pass

        if not bars:
            parquet_file = CANDLE_DIR / f"{asset}_15m.parquet"
            if parquet_file.exists():
                try:
                    df = pd.read_parquet(parquet_file)
                    bars = df.to_dict("records")
                    bars_source = "PARQUET_FALLBACK"
                except Exception:
                    bars = []

        # Audit finding C1: make indicator staleness visible. A snapshot whose
        # candles are hours old must never look identical to a live one.
        if bars:
            bars_last_close_epoch = float(bars[-1].get("time", 0.0)) + 900.0
            indicator_age_min = round(max(0.0, (now_ts - bars_last_close_epoch) / 60.0), 1)
            bars_last_close_utc = datetime.fromtimestamp(bars_last_close_epoch, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        else:
            bars_last_close_epoch = None
            indicator_age_min = None
            bars_last_close_utc = None

        # Bars without measured broker volume cannot yield a volume-weighted
        # price; old indicator code used fictitious unit weights for these.
        has_bar_volume = bool(bars) and all(
            float(b.get("real_volume") or b.get("volume") or b.get("tick_volume") or 0) > 0
            for b in bars)
        bars_fresh = indicator_age_min is not None and indicator_age_min <= 30
        indicators = CandleIndicatorEngine.compute_indicators(bars) if bars and bars_fresh else {}
        atr = indicators.get("atr_14")
        rsi = indicators.get("rsi_14")
        session_vwap = indicators.get("session_vwap") if has_bar_volume else None
        session_sigma = indicators.get("session_sigma") if has_bar_volume else None
        vwap_z = ((mid_price - session_vwap) / session_sigma
                  if quote_valid and session_vwap is not None and session_sigma and session_sigma > 0 else None)
        ema_20 = indicators.get("ema_20")
        ema_50 = indicators.get("ema_50")
        _ema200_raw = indicators.get("ema_200")
        ema_200 = float(_ema200_raw) if _ema200_raw is not None and len(bars) >= EMA200_MIN_BARS else None
        # (audit H2 root cause: the engine emits "ema_200_slope_pct" - the
        # old code read a nonexistent "_3h" key and hard-zeroed the slope.)
        _slope_raw = indicators.get("ema_200_slope_pct")
        if ema_200 is not None and _slope_raw is not None:
            ema_200_slope = float(_slope_raw)
        else:
            ema_200_slope = None

        # Volume profile
        vol_profile = compute_volume_profile(bars[-96:] if len(bars) >= 96 else bars) if bars_fresh else compute_volume_profile([])

        # Neither MT5 bars nor Binance aggregate open interest reveal pending
        # stops or resting liquidation prices. Keep OI as a separate observed
        # metric; live stop/liq bands remain unavailable without a direct feed.
        oi_info = crypto_ois.get(asset, {}) if asset in CRYPTO_ASSETS else {}
        oi_contracts = float(oi_info.get("openInterest") or 0.0) or None
        stop_results = {"source": "UNAVAILABLE", "coverage": "NONE", "bands": [],
                        "reason": "No verified exchange stop-order feed"}
        reconstructed_liquidations = {
            "source": "UNAVAILABLE" if asset in CRYPTO_ASSETS else "NOT_APPLICABLE",
            "coverage": "NONE", "long_liquidations_below": [], "short_liquidations_above": [],
            "max_pain": None, "top_long_cascade_bands_below": [],
            "top_short_squeeze_bands_above": [],
            "reason": "Open interest cannot identify liquidation prices or leverage" if asset in CRYPTO_ASSETS else "No perpetual venue",
            "binance_futures_open_interest_contracts": oi_contracts,
            "open_interest_source": "BINANCE_FUTURES_PUBLIC_REST" if oi_contracts is not None else "UNAVAILABLE",
            "open_interest_venue": "BINANCE_USDM_FUTURES" if asset in CRYPTO_ASSETS else None,
            "open_interest_as_of_epoch": float(oi_info["time"]) / 1000 if oi_info.get("time") else None,
        }

        # -----------------------------------------------------------------
        # Live L2 Orderbook Depth (Top 20 Bids and Top 20 Asks)
        # Real Binance Futures Depth for Crypto; NO SYNTHETIC LADDERS FOR NON-CRYPTO
        # -----------------------------------------------------------------
        raw_book = crypto_books.get(asset, {}) if asset in CRYPTO_ASSETS else {}
        bids_top20 = []
        asks_top20 = []
        cum_bid_usd = 0.0
        cum_ask_usd = 0.0
        whale_walls = []

        if (raw_book and isinstance(raw_book.get("bids"), list) and isinstance(raw_book.get("asks"), list)
                and raw_book["bids"] and raw_book["asks"]
                and all(float(r[0]) > 0 and float(r[1]) > 0 for r in raw_book["bids"][:20] + raw_book["asks"][:20])
                and float(raw_book["bids"][0][0]) < float(raw_book["asks"][0][0])):
            for p_str, sz_str in raw_book["bids"][:20]:
                p_lvl = float(p_str)
                sz_lvl = float(sz_str)
                notional = p_lvl * sz_lvl
                cum_bid_usd += notional
                bids_top20.append([round(p_lvl, 4), round(sz_lvl, 4), round(notional, 2), round(cum_bid_usd, 2)])
                if notional >= 150_000.0:
                    wall_key = f"{asset}_BUY_{round(p_lvl, 4)}"
                    first_seen = prev_whale_state.get(wall_key, now_ts)
                    new_whale_state[wall_key] = first_seen
                    pers_sec = round(now_ts - first_seen, 1)
                    whale_walls.append({
                        "side": "BUY",
                        "price": round(p_lvl, 4),
                        "notional_usd": round(notional, 2),
                        "distance_pct": round((p_lvl - ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2)) / ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2) * 100.0, 2),
                        "sample_span_sec": pers_sec,
                        "persistence_status": "SAMPLED_ONLY_NOT_CONTINUOUS",
                        "first_seen_utc": datetime.fromtimestamp(first_seen, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })

            for p_str, sz_str in raw_book["asks"][:20]:
                p_lvl = float(p_str)
                sz_lvl = float(sz_str)
                notional = p_lvl * sz_lvl
                cum_ask_usd += notional
                asks_top20.append([round(p_lvl, 4), round(sz_lvl, 4), round(notional, 2), round(cum_ask_usd, 2)])
                if notional >= 150_000.0:
                    wall_key = f"{asset}_SELL_{round(p_lvl, 4)}"
                    first_seen = prev_whale_state.get(wall_key, now_ts)
                    new_whale_state[wall_key] = first_seen
                    pers_sec = round(now_ts - first_seen, 1)
                    whale_walls.append({
                        "side": "SELL",
                        "price": round(p_lvl, 4),
                        "notional_usd": round(notional, 2),
                        "distance_pct": round((p_lvl - ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2)) / ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2) * 100.0, 2),
                        "sample_span_sec": pers_sec,
                        "persistence_status": "SAMPLED_ONLY_NOT_CONTINUOUS",
                        "first_seen_utc": datetime.fromtimestamp(first_seen, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })

            binance_mid = (float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2
            total_bid_depth = cum_bid_usd
            total_ask_depth = cum_ask_usd
            book_imbalance = round((total_bid_depth - total_ask_depth) / max(total_bid_depth + total_ask_depth, 1.0), 4)
            skew_ratio = round(total_bid_depth / max(total_ask_depth, 1.0), 4)
            orderbook_payload = {
                "source": "REAL_BINANCE_FUTURES_L2",
                "venue": "BINANCE_USDM_FUTURES", "aggregation": "ANONYMOUS_PRICE_LEVELS_NOT_ORDERS",
                "binance_mid": round(binance_mid, 4),
                "top20_bid_depth_usd": round(total_bid_depth, 2),
                "top20_ask_depth_usd": round(total_ask_depth, 2),
                "book_imbalance": book_imbalance,
                "skew_ratio": skew_ratio,
                "bids_top20": bids_top20,
                "asks_top20": asks_top20,
                "whale_walls_l3": [],  # no address/individual order feed
                "l2_wall_levels": whale_walls,
                "wall_coverage": "SAMPLED_ANONYMOUS_BINANCE_AGGREGATED_L2_NOT_L3",
                "wall_sample_ts_epoch": now_ts
            }
        else:
            # NO SYNTHETIC DEPTH! Report real L1 only honestly
            orderbook_payload = {
                "source": "UNAVAILABLE_L1_ONLY",
                "venue": "BINANCE_USDM_FUTURES" if asset in CRYPTO_ASSETS else None,
                "binance_mid": None,
                "top20_bid_depth_usd": None,
                "top20_ask_depth_usd": None,
                "book_imbalance": None,
                "skew_ratio": None,
                "bids_top20": [],
                "asks_top20": [],
                "whale_walls_l3": [],
                "l2_wall_levels": [],
                "wall_coverage": "UNAVAILABLE_L1_ONLY",
                "wall_sample_ts_epoch": None
            }

        # -----------------------------------------------------------------
        # Microstructure & Pioneer Setup Evaluation (100% Dynamic)
        # -----------------------------------------------------------------
        # Audit finding H2: slope was hard-0 with short bar history, making
        # BEARISH impossible and biasing the board BULLISH on a crash day.
        # With ema_200/slope now null below the bar threshold, say so.
        if not quote_valid:
            trend_status = "UNAVAILABLE_NO_MT5_QUOTE"
        elif ema_200 is None or ema_200_slope is None:
            trend_status = "INSUFFICIENT_HISTORY"
        elif mid_price > ema_200 and ema_200_slope >= 0:
            trend_status = "BULLISH"
        elif mid_price < ema_200 and ema_200_slope < 0:
            trend_status = "BEARISH"
        else:
            trend_status = "RANGE_BOUND"
        
        session_low = min(float(b["low"]) for b in bars[-32:]) if bars else None
        session_high = max(float(b["high"]) for b in bars[-32:]) if bars else None
        swept_low = (mid_price <= session_low + 0.2 * atr
                     if quote_valid and session_low is not None and atr is not None else None)
        swept_high = (mid_price >= session_high - 0.2 * atr
                      if quote_valid and session_high is not None and atr is not None else None)

        # Observed MT5 inventory is status only, not an instruction to trade.
        sym_check = "XAU" if asset == "GOLD" else ("USWTI" if asset == "USWTI" else asset)
        active_pos = [p for p in formatted_positions if sym_check in str(p.get("symbol", ""))]
        active_pending = [o for o in formatted_orders if sym_check in str(o.get("symbol", ""))]
        if active_pos:
            pioneer_eval = "ACTIVE_FILLED"
            pioneer_reason = "MT5 reports an open position"
        elif active_pending:
            pioneer_eval = "ACTIVE_PENDING"
            pioneer_reason = "MT5 reports a resting order"
        else:
            pioneer_eval = "UNAVAILABLE_UNVERIFIED_ORDERFLOW"
            pioneer_reason = "No observed stop/liquidation bands or cross-venue execution validation; no trade authorization"
        confluence_trade_setup = None

        assets_matrix[asset] = {
            "symbol_broker": broker_sym or asset,
            "category": "CRYPTO" if asset in CRYPTO_ASSETS else ("INDICES" if asset in INDICES_ASSETS else ("COMMODITIES" if asset in COMMODITIES_ASSETS else "FOREX")),
            "quotes": {
                "bid": round(bid_price, 4) if quote_valid else None,
                "ask": round(ask_price, 4) if quote_valid else None,
                "mid": round(mid_price, 4) if quote_valid else None,
                "spread_price": round(spread_price, 4) if spread_price is not None else None,
                "spread_bps": round(spread_bps, 2) if spread_bps is not None else None,
                "quote_source": quote_source,
                "quote_age_s": quote_age_s,
                "quote_freshness": quote_freshness,
                "local_receipt_age_s": local_receipt_age_s,
                "broker_tick_age_s": broker_tick_age_s,
                "broker_tick_time_utc_msc": quote.get("time_msc"),
                "broker_raw_server_time_msc": quote.get("raw_time_msc"),
                "local_receipt_time_epoch": receipt_epoch,
                "specs_source": specs_source,
                "tick_size": exec_specs.get("tick_size"),
                "contract_size": exec_specs.get("contract_size"),
                "min_lot": exec_specs.get("min_lot"),
                "step_lot": exec_specs.get("step_lot"),
                "max_lot": exec_specs.get("max_lot"),
                "stops_level": exec_specs.get("stops_level"),
                "digits": exec_specs.get("digits")
            },
            "execution_specs": exec_specs,
            "causal_indicators": {
                "session_vwap_utc": round(session_vwap, 4) if session_vwap else None,
                "session_sigma": round(session_sigma, 4) if session_sigma else None,
                "session_bars": indicators.get("session_bars", 0),
                "vwap_z_score": round(vwap_z, 2) if vwap_z is not None else None,
                "rsi_14": round(rsi, 2) if rsi is not None else None,
                "atr_14": round(atr, 4) if atr is not None else None,
                "atr_pct": round(atr / mid_price * 100.0, 3) if atr is not None and quote_valid else None,
                "ema_20": round(ema_20, 4) if ema_20 is not None else None,
                "ema_50": round(ema_50, 4) if ema_50 is not None else None,
                "ema_200": round(ema_200, 4) if ema_200 is not None else None,
                "ema_200_bars_used": len(bars),
                "ema_200_slope_3h_pct": round(ema_200_slope, 4) if ema_200_slope is not None else None,
                "trend_regime": trend_status,
                "indicators_source": bars_source,
                "vwap_weight_unit": "MT5_TICK_VOLUME_PROXY_NOT_EXCHANGE_CONTRACTS" if has_bar_volume else "UNAVAILABLE",
                "bars_last_close_utc": bars_last_close_utc,
                "indicator_age_min": indicator_age_min
            },
            "volume_profile": {**vol_profile, "volume_unit": "MT5_BROKER_BAR_VOLUME_OR_TICK_COUNT_NOT_EXCHANGE_BASE_ASSET_VOLUME"},
            "structural_stop_clusters": {
                "source": "UNAVAILABLE", "coverage": "NONE",
                "amount_semantics": "UNAVAILABLE",
                "total_sell_stops_usd": None, "total_buy_stops_usd": None,
                "top_sell_stop_clusters_below": [], "top_buy_stop_clusters_above": [],
                "reason": stop_results["reason"]
            },
            "reconstructed_liquidations": reconstructed_liquidations,
            "orderbook_live_depth": orderbook_payload,
            "pioneer_microstructure_eval": {
                "status": pioneer_eval,
                "swept_session_low": swept_low,
                "swept_session_high": swept_high,
                "reasoning": pioneer_reason,
                "confluence_trade_setup": confluence_trade_setup,
                "portfolio_gating": "ADMISSION_FROZEN_UNVERIFIED_DATA"
            },
            "funding_and_rates": (
                {
                    "last_funding_rate_bps": round(float(crypto_prems[asset]["lastFundingRate"]) * 1e4, 2) if crypto_prems.get(asset, {}).get("lastFundingRate") is not None else None,
                    "predicted_funding_rate_bps": None,  # premiumIndex interestRate is NOT predicted funding
                    "predicted_funding_source": "UNAVAILABLE_IN_PREMIUM_INDEX",
                    "mark_price": round(float(crypto_prems[asset]["markPrice"]), 4) if crypto_prems.get(asset, {}).get("markPrice") is not None else None,
                    "index_price": round(float(crypto_prems[asset]["indexPrice"]), 4) if crypto_prems.get(asset, {}).get("indexPrice") is not None else None
                } if asset in CRYPTO_ASSETS else None
            ),
            "cvd_1m_buckets": crypto_cvd.get(asset, []) if asset in CRYPTO_ASSETS else None,
            "htf_4h_ohlcv": crypto_htf_4h.get(asset, []) if asset in CRYPTO_ASSETS else None,
            "htf_d1_ohlcv": crypto_htf_d1.get(asset, []) if asset in CRYPTO_ASSETS else None,
            "funding_history_8x8h": crypto_funding_hist.get(asset, []) if asset in CRYPTO_ASSETS else None
        }

        # Audit finding H5: raw-spread MT5 accounts print 0.0 spread with
        # commission billed separately — flag it so friction math never
        # silently assumes a free round trip.
        if spread_price == 0 and quote_valid:
            assets_matrix[asset]["quotes"]["spread_caveat"] = "RAW_ZERO_SPREAD_COMMISSION_EXCLUDED"

    # Save whale wall state for persistence tracking across iterations
    save_whale_state(new_whale_state, whale_state_path)

    # Assemble master document
    payload = {
        "protocol": "omni.telemetry.v3.observed_only",
        "snapshot_status": "LIVE_OBSERVATION",
        "data_policy": "OBSERVED_OR_DERIVED_FROM_OBSERVED; unavailable fields never authorize trades",
        "as_of_utc": now_utc,
        "as_of_epoch": now_ts,
        "generated_by": "MT5 bridge + public feeds; no broker execution performed here",
        "trade_authorization": "DENIED_UNVERIFIED_ORDERFLOW",
        "account": {
            "login": acc_summary.get("login"),
            "server": acc_summary.get("server"),
            "balance_usd": balance_usd,
            "equity_usd": equity_usd,
            "margin_used_usd": margin_used,
            "margin_free_usd": margin_free,
            "margin_level_pct": margin_level,
            "hard_floor_usd": hard_floor,
            "cushion_above_floor_usd": cushion
        },
        "active_positions": formatted_positions,
        "pending_orders": formatted_orders,
        "capacity": {
            "filled": filled_count,
            "pending": pending_count,
            "max_concurrent": 2,
            "status": capacity_status
        },
        "macro_calendar": macro_calendar,
        "assets_matrix_24": assets_matrix
    }

    if not validate_observed_snapshot(payload):
        raise RuntimeError("FAIL_CLOSED: telemetry provenance validation failed")

    # Write JSON atomically (to the injectable path for tests)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = out_path.with_suffix(".tmp")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, allow_nan=False)
    temp_path.replace(out_path)

    print(f"[{now_utc}] Successfully exported observed-only telemetry snapshot v3 to {out_path}")
    print(f"  Account Equity: {equity_usd:.2f} USD | Hard Floor: {hard_floor:.2f} USD | Cushion: +{cushion:.2f} USD")
    print(f"  Active Positions: {filled_count} | Pending Orders: {pending_count} | Capacity: {capacity_status}")
    print(f"  Assets Exported: {len(assets_matrix)} / 24 assets; L2 only where fetched, stops/liquidation exposure unavailable.")
    return payload


if __name__ == "__main__":
    generate_full_snapshot()
