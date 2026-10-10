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
import os
import pathlib
import sys
import time
import urllib.request
import uuid
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
from Terminal.risk.live_admission import MAX_FILLED, STOP_STRESS_MULTIPLIER, MIN_EXECUTION_COST_USD, _loss
from Terminal.risk.floor_defense import HARD_FLOOR_USD, BUFFER_USD
from Terminal.Api_Client import HyperdashClient

TELEMETRY_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
TELEMETRY_PATH.parent.mkdir(parents=True, exist_ok=True)
CANDLE_DIR = ROOT / "Data" / "Candles"
WHALE_STATE_PATH = ROOT / "docs" / "telemetry" / ".whale_wall_state.json"

sys.path.insert(0, str(ROOT / "Terminal"))
from microstructure_state import (  # noqa: E402
    WALL_GENUINE,
    carry_forward_unseen,
    classify_wall,
    estimate_cycle_interval,
    prune_wall_state,
    record_cycle_interval,
    wall_persistence_record,
)
ERROR_MARKER_PATH = ROOT / "docs" / "telemetry" / ".generator_error.json"

# --- Data-integrity invariants (OX_ALPHA_66 forensics audit 2026-10-07) -----
# Every independently fillable pending reserves a canonical admission slot.
MAX_CONCURRENT_SLOTS = MAX_FILLED
HTF_FETCH_COUNT = 96
BARS_15M_COUNT = 100
from Terminal.policy import HTF_MIN_COMPLETED, HTF_STRATEGY_MIN
BROKER_HTF = {"1h": (16385, 3600), "4h": (16388, 14400)}

# ---------------------------------------------------------------------------
# Win-probability lower bound for the conservative expectancy gate (_net_ev).
#
# This MUST stay a computed statistic, never a literal. A hardcoded constant
# labelled "calibrated" lets the gate pass on a number no sample supports, and
# _net_ev has no way to detect that because it only sees the scalar.
#
# The bound is the exact one-sided Clopper-Pearson limit of the closed-trade
# record: the value L solving P(X >= wins | p = L) = 1 - confidence. Verified
# to 1e-16 against scipy.stats.beta.ppf(0.05, wins, n - wins + 1).
P_WIN_WINS = 11                  # closed winners in the audited record
P_WIN_SAMPLE_N = 17              # closed trades in the audited record
P_WIN_CONFIDENCE = 0.95          # one-sided
P_WIN_MIN_SAMPLE = 100           # below this the bound is not "calibrated"
MACRO_CALENDAR_PATH = ROOT / "Data" / "macro_calendar.json"
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


def _betacf(a: float, b: float, x: float, max_iter: int = 300, eps: float = 3e-14) -> float:
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < 1e-300:
        d = 1e-300
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1e-300 if abs(d) < 1e-300 else d
        d = 1.0 / d
        c = 1.0 + aa / c
        c = 1e-300 if abs(c) < 1e-300 else c
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1e-300 if abs(d) < 1e-300 else d
        d = 1.0 / d
        c = 1.0 + aa / c
        c = 1e-300 if abs(c) < 1e-300 else c
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta function I_x(a, b). Pure stdlib."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_beta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(ln_beta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def p_win_lower_bound(wins: int, n: int, confidence: float = P_WIN_CONFIDENCE) -> float:
    """Exact one-sided Clopper-Pearson lower confidence bound on a win rate.

    Returns the value L solving P(X >= wins | p = L) = I_L(wins, n-wins+1)
    = 1 - confidence. Deliberately conservative: it is the *worst* win rate
    consistent with the observed record, which is what _net_ev's
    `p_lo >= p_breakeven + 0.03` margin is meant to be tested against.

    Verified against scipy.stats.beta.ppf(1 - confidence, wins, n - wins + 1).
    """
    if n <= 0 or wins <= 0:
        return 0.0
    if wins >= n:
        # A perfect record still cannot certify p = 1.0; clamp to n-1 so the
        # bound stays finite and conservative.
        wins = n - 1
    alpha = 1.0 - confidence
    a, b = float(wins), float(n - wins + 1)
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        # I_p(a, b) is increasing in p: overshoot pulls the ceiling down.
        if _betai(a, b, mid) > alpha:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def p_win_calibration(wins: int = P_WIN_WINS, n: int = P_WIN_SAMPLE_N) -> Dict[str, Any]:
    """Publish the win-rate bound together with honest provenance.

    `calibrated` means "sample large enough for the bound to be a calibration".
    A 17-trade record yields a real, usable bound but is NOT a calibration, and
    claiming otherwise is what lets an unearned edge pass the expectancy gate.
    """
    bound = p_win_lower_bound(wins, n)
    return {
        "p_win_lower_bound": round(bound, 4),
        "p_win_lower_bound_calibrated": bool(n >= P_WIN_MIN_SAMPLE),
        "p_win_calibration_sample_n": int(n),
        "p_win_calibration_wins": int(wins),
        "p_win_calibration_method": (
            "EXACT_ONE_SIDED_CLOPPER_PEARSON_%.0fPCT" % (P_WIN_CONFIDENCE * 100)
        ),
        "p_win_calibration_minimum_sample": int(P_WIN_MIN_SAMPLE),
        "p_win_calibration_note": (
            "Computed from the closed-trade record on every generation; never a literal."
        ),
    }



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
    """Fetch independent Binance reference history, never broker HTF inputs."""
    bin_sym = f"{asset}USDT"
    bars_4h: List[Dict] = []
    bars_d1: List[Dict] = []
    for interval, target in [("4h", bars_4h), ("1d", bars_d1)]:
        try:
            url = f"https://fapi.binance.com/fapi/v1/klines?symbol={bin_sym}&interval={interval}&limit={HTF_FETCH_COUNT + 1}"
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


def fetch_hyperdash_microstructure(client: HyperdashClient, asset: str) -> Tuple[str, Dict[str, Any]]:
    """Fetch authentic Hyperdash L2 orderbook, L3 wallet orders, stop clusters, and liquidation levels."""
    target = client._resolve_coin(asset)
    if target in ("DJ30", "GER40"):
        return asset, {"status": "NOT_AVAILABLE_ON_HYPERDASH", "reason": "Asset not traded on Hyperliquid perpetual DEX"}
    book = None
    mid = 0.0
    try:
        book = client.fetch_l2_book(target)
        best_bid = float(book.get("best_bid") or 0.0)
        best_ask = float(book.get("best_ask") or 0.0)
        mid = (best_bid + best_ask) / 2.0 if (best_bid > 0 and best_ask >= best_bid) else 0.0
    except Exception:
        pass
    if mid <= 0:
        return asset, {"status": "ERROR", "error": "Invalid mid price from Hyperliquid L2 book"}

    l3_orders = []
    try:
        l3_orders = client.fetch_l3_orders(target, min_price=mid * 0.98, max_price=mid * 1.02)
    except Exception:
        pass

    stops = {}
    try:
        stops = client.fetch_stops(target, min_price=mid * 0.80, max_price=mid * 1.20)
    except Exception:
        pass

    liqs = {}
    try:
        liqs = client.fetch_liquidations(target, min_price=mid * 0.80, max_price=mid * 1.20)
    except Exception:
        pass

    return asset, {
        "status": "SUCCESS",
        "target": target,
        "mid": mid,
        "book": book,
        "l3_orders": l3_orders,
        "stops": stops,
        "liquidations": liqs
    }


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


def _level_pairs(levels) -> list:
    """Normalise either book shape to [(price, notional_usd), ...].

    Binance REST yields ["price", "size"] strings; Hyperdash yields dicts with
    price/size/total_usd. The mirror test needs both, so normalise once here
    rather than special-casing at every call site.
    """
    out = []
    for lv in levels or ():
        try:
            if isinstance(lv, dict):
                px = float(lv.get("price") or 0.0)
                nt = float(lv.get("notional_usd") or lv.get("total_usd")
                           or (px * float(lv.get("size") or 0.0)))
            else:
                px = float(lv[0])
                nt = px * float(lv[1])
            if px > 0 and nt > 0:
                out.append((px, nt))
        except (TypeError, ValueError, IndexError, KeyError):
            continue
    return out


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


def completed_broker_bars(raw_bars, period: int, cutoff: float):
    """Validate observed OHLCV; drop forming bars without inventing history."""
    complete, invalid, forming = [], 0, 0
    previous = None
    if not isinstance(raw_bars, (list, tuple)):
        return complete, 0, 0
    for raw in raw_bars:
        try:
            stamp = float(raw["time"])
            values = [float(raw[k]) for k in ("open", "high", "low", "close")]
            volume = float(raw.get("real_volume") or raw.get("volume") or raw.get("tick_volume") or 0)
            if (not all(math.isfinite(v) and v > 0 for v in [stamp, *values])
                    or not math.isfinite(volume) or volume < 0
                    or values[1] < max(values[0], values[2], values[3])
                    or values[2] > min(values[0], values[1], values[3])
                    or (previous is not None and stamp <= previous)):
                raise ValueError("invalid OHLCV or timestamp order")
            previous = stamp
            if stamp + period > cutoff:
                forming += 1
                continue
            complete.append({**raw, "time": stamp, "volume": volume})
        except (TypeError, ValueError, KeyError, OverflowError):
            invalid += 1
    return complete, invalid, forming


def broker_htf_history(bridge, symbol, cutoff: float, clock_verified: bool):
    history, quality = {}, {}
    for key, (timeframe, period) in BROKER_HTF.items():
        error = None
        try:
            raw = bridge.get_recent_bars(symbol, count=HTF_FETCH_COUNT, timeframe=timeframe) if symbol else []
        except Exception as exc:
            raw, error = [], str(exc)
        bars, invalid, forming = completed_broker_bars(raw, period, cutoff)
        bars = bars[-HTF_FETCH_COUNT:]
        last_close = bars[-1]["time"] + period if bars else None
        age = cutoff - last_close if last_close is not None else None
        status = ("INVALID_OBSERVATIONS" if invalid else "UNAVAILABLE" if not bars
                  else "INSUFFICIENT_HISTORY" if len(bars) < HTF_STRATEGY_MIN else "READY")
        freshness = ("UNVERIFIED_CLOCK" if not clock_verified else "FRESH" if age is not None and 0 <= age <= 2 * period
                     else "STALE" if age is not None else "UNAVAILABLE")
        history[key] = [{"ts": b["time"], "close_ts": b["time"] + period,
                         **{k: b[k] for k in ("open", "high", "low", "close", "volume")},
                         "volume_unit": "BROKER_REAL_VOLUME" if b.get("real_volume", 0) > 0 else "BROKER_TICK_VOLUME_PROXY"}
                        for b in bars]
        quality[key] = {"source": "MT5_BROKER_COMPLETED_BARS", "broker_symbol": symbol,
                        "completed_count": len(bars), "required_minimum": HTF_MIN_COMPLETED,
                        "strategy_minimum": HTF_STRATEGY_MIN, "target_count": HTF_FETCH_COUNT,
                        "status": status, "freshness": freshness, "invalid_count": invalid,
                        "forming_excluded_count": forming, "last_close_epoch": last_close,
                        "age_seconds": age, "clock_verified": clock_verified, "error": error}
    quality["entry_eligible"] = all(q["status"] == "READY" and q["freshness"] == "FRESH" for q in quality.values())
    return history, quality


def contingent_inventory_risk(bridge, positions, pending, balance, equity, margin_free):
    tickets, errors, pending_margin = [], [], 0.0
    for kind, rows in (("FILLED", positions), ("PENDING", pending)):
        for row in rows:
            try:
                stressed = _loss(bridge, row)
                nominal = (stressed - MIN_EXECUTION_COST_USD) / STOP_STRESS_MULTIPLIER
                reserved_margin = None
                if kind == "PENDING":
                    estimate = bridge.estimate_order(row["symbol"], row["direction"], row["price_open"], row["sl"])
                    reserved_margin = float(estimate["margin_per_lot"]) * float(row["volume"])
                    if not math.isfinite(reserved_margin) or reserved_margin <= 0:
                        raise ValueError("pending broker margin unavailable")
                    pending_margin += reserved_margin
                tickets.append({"ticket": row.get("ticket"), "kind": kind,
                                "nominal_stop_loss_usd": nominal, "stressed_stop_loss_usd": stressed,
                                "margin_on_fill_usd": reserved_margin, "status": "BROKER_VALUED"})
            except Exception as exc:
                errors.append(f"{kind} ticket {row.get('ticket')}: {exc}")
                tickets.append({"ticket": row.get("ticket"), "kind": kind,
                                "nominal_stop_loss_usd": None, "stressed_stop_loss_usd": None,
                                "margin_on_fill_usd": None, "status": "UNAVAILABLE"})
    total = sum(t["stressed_stop_loss_usd"] for t in tickets) if not errors else None
    post_loss = min(balance, equity) - total if total is not None else None
    return {"status": "UNAVAILABLE" if errors else "BROKER_VALUED", "source": "CANONICAL_LIVE_ADMISSION_BROKER_VALUATION",
            "inventory_status": "OBSERVED", "tickets": tickets, "errors": errors,
            "total_contingent_stress_usd": total, "post_joint_stop_equity_usd": post_loss,
            "required_post_stop_equity_usd": HARD_FLOOR_USD + BUFFER_USD,
            "floor_buffer_preserved": post_loss >= HARD_FLOOR_USD + BUFFER_USD if post_loss is not None else False,
            "pending_margin_on_fill_usd": pending_margin if not errors else None,
            "free_margin_after_pending_fills_usd": margin_free - pending_margin if not errors else None,
            "stop_stress_multiplier": STOP_STRESS_MULTIPLIER, "execution_cost_per_ticket_usd": MIN_EXECUTION_COST_USD}


def calendar_observation(now: float, calendar_path=None):
    """Select the next/active verified high-impact window from the dated calendar."""
    def stamp(value):
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("calendar timestamp has no timezone")
        return parsed.timestamp()
    def text_stamp(value):
        return datetime.fromtimestamp(value, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    try:
        calendar = json.loads(pathlib.Path(calendar_path or MACRO_CALENDAR_PATH).read_text(encoding="utf-8"))
        if calendar.get("schema") != "omni.calendar.v1" or calendar.get("required_series") != ["CPI", "NFP", "FOMC"]:
            raise ValueError("calendar coverage unverified")
        start, end = stamp(calendar["coverage_start"]), stamp(calendar["coverage_end"])
        verified = stamp(calendar["verified_at"])
        if not start <= now < end or verified > now + 60:
            raise ValueError("outside verified calendar coverage")
        events = calendar["events"]
        if not isinstance(events, list) or not events:
            raise ValueError("calendar events unavailable")
        windows = []
        for event in events:
            if event.get("impact") != "HIGH":
                continue
            from Terminal.Macro_Calendar import event_window_utc
            when, blackout_start, blackout_end = event_window_utc(event, 30, 30)
            release, window_start, window_end = when.timestamp(), blackout_start.timestamp(), blackout_end.timestamp()
            purge = stamp(event["purge_at_utc"]) if event.get("purge_at_utc") else window_start - 300
            if (not event.get("name") or not str(event.get("source") or "").startswith("https://")
                    or not start <= release < end or not purge <= window_start <= release <= window_end):
                raise ValueError("calendar event provenance/window invalid")
            if window_end > now:
                windows.append((window_start, window_end, release, purge, event))
        windows.sort(key=lambda w: (0 if w[0] <= now < w[1] else 1, w[0]))
        result = {"calendar_status": "VERIFIED_COVERAGE", "calendar_source": "Data/macro_calendar.json",
                  "verified_at": calendar["verified_at"], "coverage_start": calendar["coverage_start"],
                  "coverage_end": calendar["coverage_end"], "blackout_active": False,
                  "event": None, "event_release_utc": None, "event_source": None,
                  "hard_blackout_window_utc": None, "purge_deadline_utc": None,
                  "runway_hours_to_blackout": None}
        if windows:
            ws, we, release, purge, event = windows[0]
            result.update(event=event["name"], event_release_utc=text_stamp(release), event_source=event["source"],
                          hard_blackout_window_utc=[text_stamp(ws), text_stamp(we)], purge_deadline_utc=text_stamp(purge),
                          runway_hours_to_blackout=round((ws - now) / 3600, 2), blackout_active=ws <= now < we)
        return result
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        return {"calendar_status": "UNAVAILABLE", "blackout_active": True, "event": None,
                "event_release_utc": None, "hard_blackout_window_utc": None,
                "runway_hours_to_blackout": None, "error": str(exc)}


def atomic_snapshot_write(out_path, payload):
    """Replace only a complete generation, tolerating brief Windows read locks."""
    out_path = pathlib.Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = out_path.with_name(f".{out_path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp")
    try:
        with temp_path.open("w", encoding="utf-8") as stream:
            json.dump(payload, stream, indent=2, allow_nan=False)
        for attempt in range(5):
            try:
                temp_path.replace(out_path)
                return
            except PermissionError:
                if attempt == 4:
                    raise
                time.sleep(0.05 * (attempt + 1))
    finally:
        temp_path.unlink(missing_ok=True)


def generate_full_snapshot(bridge: Any = None, telemetry_path: Any = None,
                           whale_state_path: Any = None) -> Dict[str, Any]:
    """Master generation routine.

    ``bridge`` / ``telemetry_path`` / ``whale_state_path`` are injectable for
    deterministic offline tests (Tests/Test_Telemetry_Data_Integrity.py).
    """
    now_ts = time.time()
    now_utc = datetime.fromtimestamp(now_ts, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    out_path = pathlib.Path(telemetry_path) if telemetry_path else TELEMETRY_PATH

    # 1. Initialize MT5 Bridge — FAIL-CLOSED (audit finding C3): if the broker
    # is unreachable we must NEVER emit a snapshot with fabricated account
    # numbers or an empty positions list (real positions would still be live
    # server-side while the snapshot advertises open capacity). Write an error
    # marker, keep the previous snapshot untouched (its as_of age exposes the
    # staleness) and abort.
    bridge = bridge or MT5ExecutionBridge(5064568)
    acc_summary = bridge.get_account_summary()
    if not isinstance(acc_summary, dict) or not acc_summary.get("connected"):
        reason = f"MT5 account summary unavailable: {acc_summary.get('error', 'unknown') if isinstance(acc_summary, dict) else 'unknown'}"
        _write_error_marker(reason)
        raise RuntimeError(f"FAIL_CLOSED: {reason}")
    if acc_summary.get("login") != 5064568 or acc_summary.get("currency") != "USD":
        raise RuntimeError("FAIL_CLOSED: MT5 account identity/currency mismatch")
    if hasattr(bridge, "broker_utc_now") and bridge.broker_utc_now() is None:
        reference = bridge.resolve_symbol("BTC")
        if reference:
            for attempt in range(5):
                bridge.get_symbol_price(reference)
                if bridge.broker_utc_now() is not None:
                    break
                if attempt < 4:
                    time.sleep(0.35)
    trusted_start = bridge.broker_utc_now() if hasattr(bridge, "broker_utc_now") else None
    if trusted_start is not None:
        now_ts = trusted_start
        now_utc = datetime.fromtimestamp(now_ts, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    try:
        open_positions = bridge.get_open_positions()
        pending_orders = bridge.get_pending_orders()
        if (not isinstance(open_positions, (list, tuple)) or not isinstance(pending_orders, (list, tuple))
                or any(not isinstance(row, dict) for row in [*open_positions, *pending_orders])):
            raise ValueError("missing or invalid native inventory")
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
            "direction": o.get("direction"),
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
        if acc_summary.get("currency") != "USD":
            raise ValueError("account denomination unavailable or non-USD")
        if not all(math.isfinite(v) for v in (equity_usd, balance_usd, margin_used, margin_free, margin_level)):
            raise ValueError("non-finite account value")
        if min(equity_usd, balance_usd) <= 0 or min(margin_used, margin_level) < 0:
            raise ValueError("invalid account value")
    except (KeyError, TypeError, ValueError) as exc:
        reason = f"MT5 account summary incomplete: {exc}"
        _write_error_marker(reason)
        raise RuntimeError(f"FAIL_CLOSED: {reason}")
    hard_floor = HARD_FLOOR_USD
    cushion = round(equity_usd - hard_floor, 2)

    filled_count = len(formatted_positions)
    pending_count = len(formatted_orders)
    max_slots = MAX_CONCURRENT_SLOTS
    joint_count = filled_count + pending_count
    book_risk = contingent_inventory_risk(bridge, open_positions, pending_orders, balance_usd, equity_usd, margin_free)
    capacity_open = (joint_count < max_slots and book_risk["floor_buffer_preserved"]
                     and book_risk["free_margin_after_pending_fills_usd"] is not None
                     and book_risk["free_margin_after_pending_fills_usd"] > 0)
    capacity_status = (f"{'OPEN' if capacity_open else 'HARD_ADMISSION_FREEZE'} "
                       f"({joint_count}/{max_slots} joint-fill slots, {filled_count} filled, {pending_count} pending, "
                       f"free_margin={margin_free:.2f} USD)")

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

    # 3. Multithreaded fetch of Crypto Depth, OI & Premium Index + Hyperdash Microstructure
    crypto_books: Dict[str, Dict[str, Any]] = {}
    crypto_ois: Dict[str, Dict[str, Any]] = {}
    crypto_prems: Dict[str, Dict[str, Any]] = {}
    crypto_cvd: Dict[str, List[Dict]] = {}
    crypto_htf_4h: Dict[str, List[Dict]] = {}
    crypto_htf_d1: Dict[str, List[Dict]] = {}
    crypto_funding_hist: Dict[str, List[Dict]] = {}
    hyperdash_results: Dict[str, Dict[str, Any]] = {}

    hd_client = HyperdashClient(timeout=4)
    with ThreadPoolExecutor(max_workers=10) as hd_ex:
        hd_futures = list(hd_ex.map(lambda a: fetch_hyperdash_microstructure(hd_client, a), ALL_24_ASSETS))
        for a, res in hd_futures:
            hyperdash_results[a] = res

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

        # Independent Binance reference history, venue separate from broker HTF.
        for asset, bars_4h, bars_d1 in ex.map(fetch_crypto_htf_ohlcv, CRYPTO_ASSETS):
            crypto_htf_4h[asset] = bars_4h
            crypto_htf_d1[asset] = bars_d1

        # NEW: Funding history (8x8h)
        for asset, rates in ex.map(fetch_crypto_funding_history, CRYPTO_ASSETS):
            crypto_funding_hist[asset] = rates

    # Compute live Coinbase premium from premiumIndex mark-vs-index
    live_cb_premium = compute_live_coinbase_premium_bps(crypto_prems)

    macro_calendar = {
        **calendar_observation(now_ts),
        "fng_index": fng_val,
        "etf_net_flows": etf_flows_1d,
        "coinbase_premium_bps": live_cb_premium,
        "coinbase_premium_source": "COINBASE_SPOT_AND_BINANCE_SPOT_RECEIPT" if live_cb_premium is not None else "UNAVAILABLE",
    }

    # Load previous whale wall state for persistence tracking
    prev_whale_state = load_whale_state(whale_state_path)
    new_whale_state: Dict[str, Any] = {}
    # The sampling period is measured from observed inter-arrival gaps rather
    # than assumed, because presence_frac is observed/EXPECTED samples and a
    # wrong denominator would silently skew every wall's persistence score.
    _cycle_interval_s = estimate_cycle_interval(prev_whale_state)
    record_cycle_interval(prev_whale_state, new_whale_state, now_ts)

    # 4. Process all 24 Assets

    # Computed once per generation from the closed-trade record; the value is a
    # statistic, not a configured constant (see p_win_calibration).
    win_calibration = p_win_calibration()

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
        # A fresh receipt is not a fresh broker tick. Shared calibrated clock
        # ages frozen ticks monotonically and refuses unknown/outlier offsets.
        broker_tick_age_s = quote.get("broker_tick_age")
        quote_age_s = broker_tick_age_s
        quote_freshness = ("FRESH" if quote_age_s is not None and 0 <= quote_age_s <= 30
                           else "STALE" if quote_age_s is not None else "TIMESTAMP_UNAVAILABLE")

        trusted_now = bridge.broker_utc_now() if hasattr(bridge, "broker_utc_now") else None
        clock_verified = trusted_now is not None and math.isfinite(trusted_now)
        # All assets share the generation's initial cutoff. A later request
        # cannot introduce a candle that had not closed at that observation.
        candle_cutoff = min(now_ts, trusted_now) if clock_verified else now_ts
        htf_bars, htf_quality = broker_htf_history(bridge, broker_sym, candle_cutoff, clock_verified)

        # Fetch fresh 15m candles directly from live broker or fall back to parquet
        bars: List[Dict[str, Any]] = []
        bars_source = "NONE"
        if bridge.initialized and broker_sym:
            raw_bars = bridge.get_recent_bars(broker_sym, count=BAR_FETCH_COUNT)
            if raw_bars:
                bars, bars_invalid, _ = completed_broker_bars(raw_bars, 900, candle_cutoff)
                bars_source = "LIVE_BRIDGE"
                try:
                    df_bars = pd.DataFrame(bars)
                    # Bridge timestamps are already normalized; never infer
                    # another timezone from the newest (possibly stale) bar.
                    df_bars["utc_time"] = df_bars["time"]
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
                    bars, bars_invalid, _ = completed_broker_bars(df.to_dict("records"), 900, candle_cutoff)
                    bars_source = "PARQUET_FALLBACK"
                except Exception:
                    bars = []

        # Audit finding C1: make indicator staleness visible. A snapshot whose
        # candles are hours old must never look identical to a live one.
        if bars:
            bars_last_close_epoch = float(bars[-1].get("time", 0.0)) + 900.0
            indicator_age_min = round((candle_cutoff - bars_last_close_epoch) / 60.0, 1)
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

        hd_res = hyperdash_results.get(asset, {})
        hd_status = hd_res.get("status")
        hd_mid = hd_res.get("mid") if (hd_res.get("mid") and hd_res.get("mid") > 0) else mid_price

        # -----------------------------------------------------------------
        # Real Structural Stop Clusters from Hyperdash
        # -----------------------------------------------------------------
        hd_stops = hd_res.get("stops", {}) if hd_status == "SUCCESS" else {}
        total_buy_size = float(hd_stops.get("total_buy_size") or (hd_stops.get("totalBuyStops") or {}).get("size") or 0.0)
        total_buy_count = int(hd_stops.get("total_buy_count") or (hd_stops.get("totalBuyStops") or {}).get("count") or 0)
        total_sell_size = float(hd_stops.get("total_sell_size") or (hd_stops.get("totalSellStops") or {}).get("size") or 0.0)
        total_sell_count = int(hd_stops.get("total_sell_count") or (hd_stops.get("totalSellStops") or {}).get("count") or 0)

        raw_stop_bands = hd_stops.get("bands", [])
        top_buy_raw = hd_stops.get("top_buy_whales") or hd_stops.get("topBuyStops") or []
        top_sell_raw = hd_stops.get("top_sell_whales") or hd_stops.get("topSellStops") or []

        if hd_status == "SUCCESS" and (raw_stop_bands or top_buy_raw or top_sell_raw or total_buy_size > 0 or total_sell_size > 0):
            sell_stop_bands = []
            buy_stop_bands = []
            for b in raw_stop_bands:
                amt = float(b.get("amount") or 0.0)
                mid_b = float(b.get("mid_px") or 0.0)
                if amt <= 0 or mid_b <= 0:
                    continue
                entry_b = {
                    "min_price": round(float(b.get("min_px", 0.0)), 4),
                    "max_price": round(float(b.get("max_px", 0.0)), 4),
                    "mid_price": round(mid_b, 4),
                    "size": round(amt, 4),
                    "notional_usd": round(amt * hd_mid, 2),
                    "distance_pct": round((mid_b - hd_mid) / hd_mid * 100.0, 2) if hd_mid > 0 else 0.0
                }
                if mid_b < hd_mid:
                    sell_stop_bands.append(entry_b)
                elif mid_b > hd_mid:
                    buy_stop_bands.append(entry_b)

            sell_stop_bands.sort(key=lambda x: x["size"], reverse=True)
            buy_stop_bands.sort(key=lambda x: x["size"], reverse=True)

            top_buy_whale_stops = []
            for w in top_buy_raw[:10]:
                px = float(w.get("price") or 0.0)
                sz = float(w.get("size") or 0.0)
                addr = str(w.get("address") or "")
                top_buy_whale_stops.append({
                    "address": addr,
                    "price": round(px, 4),
                    "size": round(sz, 4),
                    "notional_usd": round(px * sz, 2)
                })

            top_sell_whale_stops = []
            for w in top_sell_raw[:10]:
                px = float(w.get("price") or 0.0)
                sz = float(w.get("size") or 0.0)
                addr = str(w.get("address") or "")
                top_sell_whale_stops.append({
                    "address": addr,
                    "price": round(px, 4),
                    "size": round(sz, 4),
                    "notional_usd": round(px * sz, 2)
                })

            stop_payload = {
                "source": "HYPERDASH_GRAPHQL_STOP_LEVELS",
                "coverage": "REAL_HYPERLIQUID_ONCHAIN_STOPS",
                "venue": "HYPERLIQUID_PERP_DEX",
                "amount_semantics": "BASE_ASSET_AND_NOTIONAL_USD",
                "total_buy_stops_usd": round(total_buy_size * hd_mid, 2),
                "total_buy_stops_count": total_buy_count,
                "total_sell_stops_usd": round(total_sell_size * hd_mid, 2),
                "total_sell_stops_count": total_sell_count,
                "top_sell_stop_clusters_below": sell_stop_bands[:10],
                "top_buy_stop_clusters_above": buy_stop_bands[:10],
                "top_buy_whale_stops": top_buy_whale_stops,
                "top_sell_whale_stops": top_sell_whale_stops,
                "band_count": len(raw_stop_bands),
                "as_of_epoch": now_ts
            }
        else:
            stop_payload = {
                "source": "UNAVAILABLE", "coverage": "NONE",
                "amount_semantics": "UNAVAILABLE",
                "total_sell_stops_usd": None, "total_buy_stops_usd": None,
                "top_sell_stop_clusters_below": [], "top_buy_stop_clusters_above": [],
                "reason": hd_res.get("reason", "No verified exchange stop-order feed")
            }

        # -----------------------------------------------------------------
        # Real Reconstructed Liquidations from Hyperdash
        # -----------------------------------------------------------------
        hd_liqs = hd_res.get("liquidations", {}) if hd_status == "SUCCESS" else {}
        total_long_size = float(hd_liqs.get("total_long_size") or (hd_liqs.get("totalLongLiquidations") or {}).get("size") or 0.0)
        total_long_count = int(hd_liqs.get("total_long_count") or (hd_liqs.get("totalLongLiquidations") or {}).get("count") or 0)
        total_short_size = float(hd_liqs.get("total_short_size") or (hd_liqs.get("totalShortLiquidations") or {}).get("size") or 0.0)
        total_short_count = int(hd_liqs.get("total_short_count") or (hd_liqs.get("totalShortLiquidations") or {}).get("count") or 0)

        raw_liq_bands = hd_liqs.get("bands", [])
        top_long_raw = hd_liqs.get("top_long_whales") or hd_liqs.get("topLongLiquidations") or []
        top_short_raw = hd_liqs.get("top_short_whales") or hd_liqs.get("topShortLiquidations") or []

        if hd_status == "SUCCESS" and (raw_liq_bands or top_long_raw or top_short_raw or total_long_size > 0 or total_short_size > 0):
            long_liq_bands = []
            short_liq_bands = []
            for b in raw_liq_bands:
                amt = float(b.get("amount") or 0.0)
                mid_b = float(b.get("mid_px") or 0.0)
                if amt <= 0 or mid_b <= 0:
                    continue
                entry_b = {
                    "min_price": round(float(b.get("min_px", 0.0)), 4),
                    "max_price": round(float(b.get("max_px", 0.0)), 4),
                    "mid_price": round(mid_b, 4),
                    "size": round(amt, 4),
                    "notional_usd": round(amt * hd_mid, 2),
                    "distance_pct": round((mid_b - hd_mid) / hd_mid * 100.0, 2) if hd_mid > 0 else 0.0
                }
                if mid_b < hd_mid:
                    long_liq_bands.append(entry_b)
                elif mid_b > hd_mid:
                    short_liq_bands.append(entry_b)

            long_liq_bands.sort(key=lambda x: x["size"], reverse=True)
            short_liq_bands.sort(key=lambda x: x["size"], reverse=True)

            top_long_liq_whales = []
            for w in top_long_raw[:10]:
                px = float(w.get("price") or 0.0)
                sz = float(w.get("size") or 0.0)
                top_long_liq_whales.append({
                    "address": w.get("address"),
                    "price": round(px, 4),
                    "size": round(sz, 4),
                    "notional_usd": round(px * sz, 2)
                })

            top_short_liq_whales = []
            for w in top_short_raw[:10]:
                px = float(w.get("price") or 0.0)
                sz = float(w.get("size") or 0.0)
                top_short_liq_whales.append({
                    "address": w.get("address"),
                    "price": round(px, 4),
                    "size": round(sz, 4),
                    "notional_usd": round(px * sz, 2)
                })

            liq_payload = {
                "source": "HYPERDASH_GRAPHQL_LIQUIDATION_LEVELS",
                "coverage": "REAL_HYPERLIQUID_POSITION_LIQUIDATIONS",
                "venue": "HYPERLIQUID_PERP_DEX",
                "total_long_liquidations_usd": round(total_long_size * hd_mid, 2),
                "total_long_liquidations_count": total_long_count,
                "total_short_liquidations_usd": round(total_short_size * hd_mid, 2),
                "total_short_liquidations_count": total_short_count,
                "top_long_cascade_bands_below": long_liq_bands[:10],
                "top_short_squeeze_bands_above": short_liq_bands[:10],
                "top_long_liquidation_whales": top_long_liq_whales,
                "top_short_liquidation_whales": top_short_liq_whales,
                "band_count": len(raw_liq_bands),
                "binance_futures_open_interest_contracts": oi_contracts,
                "as_of_epoch": now_ts
            }
        else:
            liq_payload = {
                "source": "UNAVAILABLE" if asset in CRYPTO_ASSETS else "NOT_APPLICABLE",
                "coverage": "NONE", "long_liquidations_below": [], "short_liquidations_above": [],
                "max_pain": None, "top_long_cascade_bands_below": [],
                "top_short_squeeze_bands_above": [],
                "reason": hd_res.get("reason", "Open interest cannot identify liquidation prices or leverage"),
                "binance_futures_open_interest_contracts": oi_contracts,
                "open_interest_source": "BINANCE_FUTURES_PUBLIC_REST" if oi_contracts is not None else "UNAVAILABLE",
                "open_interest_venue": "BINANCE_USDM_FUTURES" if asset in CRYPTO_ASSETS else None,
                "open_interest_as_of_epoch": float(oi_info["time"]) / 1000 if oi_info.get("time") else None,
            }

        # -----------------------------------------------------------------
        # Level 3 Resting Wallet Orders (Whales with 0x addresses)
        # -----------------------------------------------------------------
        hd_l3 = hd_res.get("l3_orders", []) if hd_status == "SUCCESS" else []
        wallet_whales_l3 = []
        for w in hd_l3:
            px = float(w.get("price") or 0.0)
            sz = float(w.get("size") or 0.0)
            notional = float(w.get("notional_usd") or (px * sz))
            addr = str(w.get("address") or "")
            if addr.startswith("0x") and px > 0 and sz > 0:
                wallet_whales_l3.append({
                    "address": addr,
                    "side": w.get("side", "UNKNOWN"),
                    "price": round(px, 4),
                    "size": round(sz, 4),
                    "notional_usd": round(notional, 2),
                    "distance_pct": round((px - hd_mid) / hd_mid * 100.0, 2) if hd_mid > 0 else 0.0,
                    "source": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT"
                })
        wallet_whales_l3.sort(key=lambda x: x["notional_usd"], reverse=True)
        top_wallet_whales_l3 = [w for w in wallet_whales_l3 if w["notional_usd"] >= 150_000.0 or w in wallet_whales_l3[:10]]

        # Persistence + authenticity for the on-chain wallet walls. These are the
        # genuinely directional levels (identified 0x addresses), and Gate G-7's
        # persist_s / presence_frac requirements were written against exactly this
        # kind of resting order. Keyed per wallet so each address's unbroken run
        # is measured on its own merits rather than pooled across wallets.
        _l3_book = (hd_res.get("book") or {}) if hd_status == "SUCCESS" else {}
        _l3_bids = _l3_book.get("bids") or []
        _l3_asks = _l3_book.get("asks") or []
        _l3_best_bid = float(_l3_bids[0]["price"]) if _l3_bids else None
        _l3_best_ask = float(_l3_asks[0]["price"]) if _l3_asks else None
        for _w in top_wallet_whales_l3:
            _side = str(_w.get("side") or "UNKNOWN").upper()
            _opp = [(x["price"], x["notional_usd"]) for x in wallet_whales_l3
                    if str(x.get("side") or "").upper() != _side]
            _key = f"{asset}_L3_{_w['address']}_{_side}_{_w['price']}"
            _pers = wall_persistence_record(prev_whale_state, new_whale_state, _key,
                                            now_ts, cycle_interval_s=_cycle_interval_s)
            _wclass = classify_wall(_side, _w["price"], _w["notional_usd"],
                                    _l3_best_bid, _l3_best_ask, _opp)
            _w["persist_s"] = _pers["persist_s"]
            _w["presence_frac"] = _pers["presence_frac"]
            _w["persistence_status"] = _pers["persistence_status"]
            _w["wall_class"] = _wclass
            _w["gate_g7_eligible"] = bool(
                _pers["gate_g7_eligible"] and _wclass == WALL_GENUINE)
            _w["first_seen_utc"] = datetime.fromtimestamp(
                _pers["first_seen"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        # -----------------------------------------------------------------
        # Live L2 Orderbook Depth (Top 20 Bids and Top 20 Asks)
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
                    pers = wall_persistence_record(prev_whale_state, new_whale_state, wall_key,
                                                     now_ts, cycle_interval_s=_cycle_interval_s)
                    # A level at the touch is not resting depth, and a size-matched
                    # opposite order at the same price is a bracket, not intent.
                    # Neither earns Gate G-7 credit however long it has been seen.
                    _wclass = classify_wall(
                        "BUY", p_lvl, notional,
                        float(raw_book["bids"][0][0]), float(raw_book["asks"][0][0]),
                        _level_pairs(raw_book["asks"][:20]))
                    whale_walls.append({
                        "side": "BUY",
                        "price": round(p_lvl, 4),
                        "notional_usd": round(notional, 2),
                        "distance_pct": round((p_lvl - ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2)) / ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2) * 100.0, 2),
                        "sample_span_sec": pers["persist_s"],
                        "persist_s": pers["persist_s"],
                        "presence_frac": pers["presence_frac"],
                        "persistence_status": pers["persistence_status"],
                        "wall_class": _wclass,
                        "gate_g7_eligible": bool(
                            pers["gate_g7_eligible"] and _wclass == WALL_GENUINE),
                        "first_seen_utc": datetime.fromtimestamp(pers["first_seen"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })

            for p_str, sz_str in raw_book["asks"][:20]:
                p_lvl = float(p_str)
                sz_lvl = float(sz_str)
                notional = p_lvl * sz_lvl
                cum_ask_usd += notional
                asks_top20.append([round(p_lvl, 4), round(sz_lvl, 4), round(notional, 2), round(cum_ask_usd, 2)])
                if notional >= 150_000.0:
                    wall_key = f"{asset}_SELL_{round(p_lvl, 4)}"
                    pers = wall_persistence_record(prev_whale_state, new_whale_state, wall_key,
                                                     now_ts, cycle_interval_s=_cycle_interval_s)
                    # A level at the touch is not resting depth, and a size-matched
                    # opposite order at the same price is a bracket, not intent.
                    # Neither earns Gate G-7 credit however long it has been seen.
                    _wclass = classify_wall(
                        "SELL", p_lvl, notional,
                        float(raw_book["bids"][0][0]), float(raw_book["asks"][0][0]),
                        _level_pairs(raw_book["bids"][:20]))
                    whale_walls.append({
                        "side": "SELL",
                        "price": round(p_lvl, 4),
                        "notional_usd": round(notional, 2),
                        "distance_pct": round((p_lvl - ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2)) / ((float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2) * 100.0, 2),
                        "sample_span_sec": pers["persist_s"],
                        "persist_s": pers["persist_s"],
                        "presence_frac": pers["presence_frac"],
                        "persistence_status": pers["persistence_status"],
                        "wall_class": _wclass,
                        "gate_g7_eligible": bool(
                            pers["gate_g7_eligible"] and _wclass == WALL_GENUINE),
                        "first_seen_utc": datetime.fromtimestamp(pers["first_seen"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })

            binance_mid = (float(raw_book["bids"][0][0]) + float(raw_book["asks"][0][0])) / 2
            total_bid_depth = cum_bid_usd
            total_ask_depth = cum_ask_usd
            book_imbalance = round((total_bid_depth - total_ask_depth) / max(total_bid_depth + total_ask_depth, 1.0), 4)
            skew_ratio = round(total_bid_depth / max(total_ask_depth, 1.0), 4)
            orderbook_payload = {
                "source": "REAL_BINANCE_FUTURES_L2_AND_HYPERDASH_L3",
                "venue": "BINANCE_USDM_FUTURES_AND_HYPERLIQUID",
                "aggregation": "BINANCE_AGGREGATED_L2_WITH_HYPERDASH_L3_WALLETS",
                "binance_mid": round(binance_mid, 4),
                "top20_bid_depth_usd": round(total_bid_depth, 2),
                "top20_ask_depth_usd": round(total_ask_depth, 2),
                "book_imbalance": book_imbalance,
                "skew_ratio": skew_ratio,
                "bids_top20": bids_top20,
                "asks_top20": asks_top20,
                "whale_walls_l3": top_wallet_whales_l3,  # Real on-chain 0x addresses from Hyperdash!
                "l2_wall_levels": whale_walls,
                "wall_coverage": "REAL_HYPERDASH_WALLET_ATTRIBUTED_L3",
                "wall_sample_ts_epoch": now_ts
            }
        elif hd_status == "SUCCESS" and hd_res.get("book"):
            hd_book = hd_res["book"]
            hd_bids_raw = hd_book.get("bids", [])[:20]
            hd_asks_raw = hd_book.get("asks", [])[:20]
            b_top20 = []
            c_bid = 0.0
            for b in hd_bids_raw:
                p = float(b["price"])
                s = float(b["size"])
                n = float(b.get("total_usd") or (p * s))
                c_bid += n
                b_top20.append([round(p, 4), round(s, 4), round(n, 2), round(c_bid, 2)])
                if n >= 150_000.0:
                    wall_key = f"{asset}_BUY_{round(p, 4)}"
                    pers = wall_persistence_record(prev_whale_state, new_whale_state, wall_key,
                                                     now_ts, cycle_interval_s=_cycle_interval_s)
                    _wclass = classify_wall(
                        "BUY", p, n,
                        float(hd_bids_raw[0]["price"]) if hd_bids_raw else None,
                        float(hd_asks_raw[0]["price"]) if hd_asks_raw else None,
                        _level_pairs(hd_asks_raw[:20]))
                    whale_walls.append({
                        "side": "BUY",
                        "price": round(p, 4),
                        "notional_usd": round(n, 2),
                        "distance_pct": round((p - hd_mid) / hd_mid * 100.0, 2) if hd_mid > 0 else 0.0,
                        "sample_span_sec": pers["persist_s"],
                        "persist_s": pers["persist_s"],
                        "presence_frac": pers["presence_frac"],
                        "persistence_status": pers["persistence_status"],
                        "wall_class": _wclass,
                        "gate_g7_eligible": bool(
                            pers["gate_g7_eligible"] and _wclass == WALL_GENUINE),
                        "first_seen_utc": datetime.fromtimestamp(pers["first_seen"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })
            a_top20 = []
            c_ask = 0.0
            for a in hd_asks_raw:
                p = float(a["price"])
                s = float(a["size"])
                n = float(a.get("total_usd") or (p * s))
                c_ask += n
                a_top20.append([round(p, 4), round(s, 4), round(n, 2), round(c_ask, 2)])
                if n >= 150_000.0:
                    wall_key = f"{asset}_SELL_{round(p, 4)}"
                    pers = wall_persistence_record(prev_whale_state, new_whale_state, wall_key,
                                                     now_ts, cycle_interval_s=_cycle_interval_s)
                    _wclass = classify_wall(
                        "SELL", p, n,
                        float(hd_bids_raw[0]["price"]) if hd_bids_raw else None,
                        float(hd_asks_raw[0]["price"]) if hd_asks_raw else None,
                        _level_pairs(hd_bids_raw[:20]))
                    whale_walls.append({
                        "side": "SELL",
                        "price": round(p, 4),
                        "notional_usd": round(n, 2),
                        "distance_pct": round((p - hd_mid) / hd_mid * 100.0, 2) if hd_mid > 0 else 0.0,
                        "sample_span_sec": pers["persist_s"],
                        "persist_s": pers["persist_s"],
                        "presence_frac": pers["presence_frac"],
                        "persistence_status": pers["persistence_status"],
                        "wall_class": _wclass,
                        "gate_g7_eligible": bool(
                            pers["gate_g7_eligible"] and _wclass == WALL_GENUINE),
                        "first_seen_utc": datetime.fromtimestamp(pers["first_seen"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    })
            tot_b = hd_book.get("bid_volume_usd") or c_bid
            tot_a = hd_book.get("ask_volume_usd") or c_ask
            imb = round((tot_b - tot_a) / max(tot_b + tot_a, 1.0), 4) if (tot_b + tot_a) > 0 else 0.0
            skew = round(tot_b / max(tot_a, 1.0), 4) if tot_a > 0 else 1.0

            orderbook_payload = {
                "source": "REAL_HYPERDASH_HIP3_L2_AND_L3",
                "venue": "HYPERLIQUID_HIP3_PERP_DEX",
                "aggregation": "HYPERDASH_L2_DEPTH_AND_L3_WALLETS",
                "hyperdash_mid": round(hd_mid, 4),
                "top20_bid_depth_usd": round(tot_b, 2),
                "top20_ask_depth_usd": round(tot_a, 2),
                "book_imbalance": imb,
                "skew_ratio": skew,
                "bids_top20": b_top20,
                "asks_top20": a_top20,
                "whale_walls_l3": top_wallet_whales_l3,  # Real on-chain 0x addresses!
                "l2_wall_levels": whale_walls,
                "wall_coverage": "REAL_HYPERDASH_WALLET_ATTRIBUTED_L3",
                "wall_sample_ts_epoch": now_ts
            }
        else:
            # NO SYNTHETIC DEPTH! Report real L1 only honestly
            orderbook_payload = {
                "source": "UNAVAILABLE_L1_ONLY",
                "venue": "BINANCE_USDM_FUTURES" if asset in CRYPTO_ASSETS else ("HYPERLIQUID" if hd_status == "SUCCESS" else None),
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
                "wall_sample_ts_epoch": None,
                "reason": hd_res.get("reason", "No orderbook venue on Hyperliquid")
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
            "structural_stop_clusters": stop_payload,
            "reconstructed_liquidations": liq_payload,
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
            "bars_15m_ohlcv": [
                {
                    "ts": int(b["time"]),
                    "close_ts": int(b["time"]) + 900,
                    "open": float(b["open"]),
                    "high": float(b["high"]),
                    "low": float(b["low"]),
                    "close": float(b["close"]),
                    "volume": float(b.get("volume", b.get("tick_volume", 0))),
                    "volume_unit": "BROKER_REAL_VOLUME" if b.get("real_volume", 0) > 0 else "BROKER_TICK_VOLUME_PROXY"
                }
                for b in bars[-BARS_15M_COUNT:]
            ] if bars else [],
            "p_win_lower_bound": win_calibration["p_win_lower_bound"],
            "p_win_lower_bound_calibrated": win_calibration["p_win_lower_bound_calibrated"],
            "htf_1h_ohlcv": htf_bars["1h"],
            "htf_4h_ohlcv": htf_bars["4h"],
            "htf_history": htf_quality,
            "binance_htf_4h_ohlcv": crypto_htf_4h.get(asset, []) if asset in CRYPTO_ASSETS else None,
            "htf_d1_ohlcv": crypto_htf_d1.get(asset, []) if asset in CRYPTO_ASSETS else None,
            "funding_history_8x8h": crypto_funding_hist.get(asset, []) if asset in CRYPTO_ASSETS else None
        }

        # Audit finding H5: raw-spread MT5 accounts print 0.0 spread with
        # commission billed separately — flag it so friction math never
        # silently assumes a free round trip.
        if spread_price == 0 and quote_valid:
            assets_matrix[asset]["quotes"]["spread_caveat"] = "RAW_ZERO_SPREAD_COMMISSION_EXCLUDED"

    # Save whale wall state for persistence tracking across iterations
    # Walls absent from this cycle's book must keep their record, or a gap can
    # never be measured and every intermittent wall resets to persist_s=0.
    carry_forward_unseen(prev_whale_state, new_whale_state)
    save_whale_state(prune_wall_state(new_whale_state, now_ts), whale_state_path)

    # Assemble master document
    trusted_finish = bridge.broker_utc_now() if hasattr(bridge, "broker_utc_now") else None
    snapshot_as_of = trusted_finish if trusted_finish is not None else time.time()
    snapshot_utc = datetime.fromtimestamp(snapshot_as_of, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    macro_calendar.update(calendar_observation(snapshot_as_of))
    payload = {
        "protocol": "omni.telemetry.v3.observed_only",
        "snapshot_status": "LIVE_OBSERVATION",
        "data_policy": "OBSERVED_OR_DERIVED_FROM_OBSERVED; unavailable fields never authorize trades",
        "as_of_utc": snapshot_utc,
        "as_of_epoch": snapshot_as_of,
        "generation_started_at_epoch": now_ts,
        "candle_cutoff_epoch": now_ts,
        "clock_basis": "CALIBRATED_BROKER_UTC" if trusted_finish is not None else "UNVERIFIED_HOST_CLOCK",
        "generation_id": uuid.uuid4().hex,
        "generated_by": "MT5 bridge + public feeds; no broker execution performed here",
        "trade_authorization": "DENIED_UNVERIFIED_ORDERFLOW",
        "account": {
            "login": acc_summary.get("login"),
            "server": acc_summary.get("server"),
            "currency": "USD",
            "source": "NATIVE_MT5_ACCOUNT_INFO",
            "balance_usd": balance_usd,
            "equity_usd": equity_usd,
            "margin_used_usd": margin_used,
            "margin_free_usd": margin_free,
            "margin_level_pct": margin_level,
            "hard_floor_usd": hard_floor,
            "cushion_above_floor_usd": cushion
        },
        "risk": book_risk,
        "active_positions": formatted_positions,
        "pending_orders": formatted_orders,
        "capacity": {
            "filled": filled_count,
            "pending": pending_count,
            "used_joint_fill": joint_count,
            "available": max(0, max_slots - joint_count) if capacity_open else 0,
            "inventory_status": "OBSERVED",
            "max_concurrent": MAX_CONCURRENT_SLOTS,
            "policy": "JOINT_FILL_CAPACITY_AND_FLOOR_DEFENSE",
            "rule": "Filled positions plus every independently fillable pending reserve at most 4 slots; broker-valued joint stressed stop loss must preserve the hard floor plus 20 USD. Unknown inventory, risk or margin freezes admission.",
            "status": capacity_status
        },
        **win_calibration,
        "macro_calendar": macro_calendar,
        "assets_matrix_24": assets_matrix
    }

    final_account = bridge.get_account_summary()
    if (not isinstance(final_account, dict) or not final_account.get("connected")
            or final_account.get("login") != 5064568 or final_account.get("currency") != "USD"):
        raise RuntimeError("FAIL_CLOSED: MT5 account changed during telemetry generation")
    if not validate_observed_snapshot(payload):
        raise RuntimeError("FAIL_CLOSED: telemetry provenance validation failed")

    atomic_snapshot_write(out_path, payload)

    print(f"[{now_utc}] Successfully exported observed-only telemetry snapshot v3 to {out_path}")
    print(f"  Account Equity: {equity_usd:.2f} USD | Hard Floor: {hard_floor:.2f} USD | Cushion: +{cushion:.2f} USD")
    print(f"  Active Positions: {filled_count} | Pending Orders: {pending_count} | Capacity: {capacity_status}")
    print(f"  Assets Exported: {len(assets_matrix)} / 24 assets; Real Hyperdash L2/L3 wallets, stops & liquidation bands integrated across all supported assets.")
    return payload


if __name__ == "__main__":
    generate_full_snapshot()
