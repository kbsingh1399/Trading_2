#!/usr/bin/env python3
"""Read-only 24-asset dual-model (Model 1 mean-reversion / Model 2 trend-pullback) gate scan.

This script performs NO broker I/O, places NO orders and modifies NO telemetry.
It consumes the git-committed v3 telemetry snapshots (docs/telemetry/live_snapshot_latest.json
history) plus the repository's own PersistentWallTracker semantics:

  * wall >= 150,000 USD notional
  * present in every ingested sample for >= 180 s  (sampled continuity only)
  * within 0.8% of mark price

Gates reported per asset:
  G1  spread (bps) vs cap (default 25 bps; per-category defaults below)
  G2  geometry: trend regime + causal pullback distance to Session VWAP in ATR
      (Model 2) or |Z| >= 2.0 and RSI < 30 / > 70 at the +-2 sigma band (Model 1)
  G3  closed taker-CVD confirmation from cvd_1m_buckets (last bucket excluded: may be forming)
  G4  persistent wall located at the candidate entry (repo wall tracker)
  G5  broker geometry: SL >= 1.5 x ATR, TP >= 2.5R, nominal risk in [MIN,MAX] USD,
      stressed post-loss equity >= hard floor + buffer

Anything not observed (L1-only assets) fails closed: UNAVAILABLE is not a pass.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from Terminal.signals.wall_tracker import PersistentWallTracker  # noqa: E402

SNAPSHOT_PATH = "docs/telemetry/live_snapshot_latest.json"

DEFAULT_SPREAD_CAP_BPS = {
    "CRYPTO": 25.0,
    "FOREX": 25.0,
    "INDICES": 25.0,
    "COMMODITIES": 25.0,
}

MIN_RISK_USD = 10.0
MAX_RISK_USD = 11.04          # briefing risk budget (stressed loss <= 15.80 USD)
STRESS_MULT = 1.25
EXEC_COST_USD = 2.0
CUSHION_FLOOR_USD = 4795.0    # hard floor 4775 + mandatory 20 buffer
WALL_MIN_USD = 150_000.0
WALL_MIN_AGE_S = 180.0
WALL_MAX_DIST_PCT = 0.8
APPROACH_ATR = 0.75           # pre-stage precondition: within 0.75 x ATR of entry
WALL_BAND_ATR = 0.25          # entry wall must sit within 0.25 x ATR of the level
SL_ATR_FLOOR = 1.5
SL_ATR_CEIL = 2.5


def git(*args: str, cwd: Path = REPO) -> str:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


def load_git_snapshots(ref: str, limit: int) -> list[dict]:
    shas = git("log", "--format=%H", f"-{limit * 2}", ref).split()
    snaps = []
    for sha in shas:
        subject = git("log", "-1", "--format=%s", sha)
        if "live 1m auto-sync" not in subject:
            continue
        raw = git("show", f"{sha}:{SNAPSHOT_PATH}")
        snaps.append(json.loads(raw))
        if len(snaps) >= limit:
            break
    snaps.sort(key=lambda d: d["as_of_epoch"])
    return snaps


def parse_utc(text: str) -> float:
    dt = datetime.strptime(text, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    return dt.timestamp()


def cvd_sums(buckets: list[dict], *, exclude_last: bool = True) -> dict:
    rows = buckets[:-1] if exclude_last and len(buckets) > 1 else buckets
    out = {}
    for minutes, key in ((1, "cvd_1m"), (5, "cvd_5m"), (15, "cvd_15m"), (60, "cvd_60m")):
        out[key] = sum(float(r.get("cvd_delta_usd") or 0.0) for r in rows[-minutes:])
    return out


def sizing_options(quotes: dict, atr: float) -> list[dict]:
    """Volumes whose SL in [1.5, 2.5] x ATR can land nominal risk in [MIN, MAX]."""
    contract = float(quotes.get("contract_size") or 0)
    min_lot = float(quotes.get("min_lot") or 0)
    step = float(quotes.get("step_lot") or 0)
    max_lot = float(quotes.get("max_lot") or 0)
    if contract <= 0 or step <= 0 or atr <= 0:
        return []
    out = []
    v = min_lot
    guard = 0
    while v <= max_lot and guard < 200_000:
        guard += 1
        lo = v * contract * SL_ATR_FLOOR * atr
        hi = v * contract * SL_ATR_CEIL * atr
        if lo <= MAX_RISK_USD and hi >= MIN_RISK_USD:
            d_min = max(SL_ATR_FLOOR * atr, MIN_RISK_USD / (v * contract))
            d_max = min(SL_ATR_CEIL * atr, MAX_RISK_USD / (v * contract))
            if d_min <= d_max:
                out.append({
                    "volume": round(v, 6),
                    "sl_low": round(d_min, 8),
                    "sl_high": round(d_max, 8),
                    "sl_atr_low": round(d_min / atr, 3),
                    "sl_atr_high": round(d_max / atr, 3),
                })
        v = round(v + step, 10)
        if len(out) >= 4:
            break
    return out


def wall_snapshot(snaps: list[dict], receipt_idx: int, symbol: str, level: float, band_atr: float):
    """Feed samples 0..receipt_idx through the repo tracker and match walls at `level`."""
    tracker = PersistentWallTracker(
        min_size_usd=WALL_MIN_USD,
        min_age_sec=WALL_MIN_AGE_S,
        max_dist_pct=WALL_MAX_DIST_PCT,
    )
    matched_bid, matched_ask = [], []
    for i, snap in enumerate(snaps[: receipt_idx + 1]):
        asset = snap["assets_matrix_24"].get(symbol)
        if not asset:
            continue
        ob = asset.get("orderbook_live_depth") or {}
        if ob.get("source") != "REAL_BINANCE_FUTURES_L2":
            continue
        bids = [[p, q] for p, q, _usd, _cum in (ob.get("bids_top20") or [])]
        asks = [[p, q] for p, q, _usd, _cum in (ob.get("asks_top20") or [])]
        mark = float(ob.get("binance_mid") or asset["quotes"]["mid"])
        tracker.update(symbol, bids, asks, mark_price=mark, timestamp=float(snap["as_of_epoch"]))
        if i != receipt_idx:
            continue
        for wall in tracker.get_persistent_walls(symbol, now=float(snap["as_of_epoch"])):
            if abs(wall.price - level) <= band_atr:
                bucket = matched_bid if wall.side == "bid" else matched_ask
                bucket.append({
                    "price": wall.price,
                    "notional_usd": round(wall.current_notional, 2),
                    "max_notional_usd": round(wall.max_notional, 2),
                    "age_s": round(wall.age(float(snap["as_of_epoch"])), 1),
                })
    return matched_bid, matched_ask


def scan(receipt: dict, history: list[dict], receipt_idx: int, spread_caps: dict) -> dict:
    account = receipt["account"]
    equity = float(account["equity_usd"])
    out = {"as_of_utc": receipt["as_of_utc"], "equity_usd": equity, "assets": {}}
    for symbol, asset in receipt["assets_matrix_24"].items():
        quotes = asset["quotes"]
        ci = asset.get("causal_indicators") or {}
        vp = asset.get("volume_profile") or {}
        ob = asset.get("orderbook_live_depth") or {}
        mid = float(quotes["mid"])
        atr = float(ci.get("atr_14") or 0)
        vwap = float(ci.get("session_vwap_utc") or 0)
        sigma = float(ci.get("session_sigma") or 0)
        z = float(ci.get("vwap_z_score") or 0)
        rsi = float(ci.get("rsi_14") or 0)
        regime = ci.get("trend_regime")
        category = asset.get("category", "CRYPTO")
        cap = spread_caps.get(category, 25.0)
        spread_bps = float(quotes.get("spread_bps") or 0)

        row: dict = {
            "broker_symbol": asset.get("symbol_broker"),
            "category": category,
            "mid": mid, "spread_bps": spread_bps, "regime": regime,
            "vwap": vwap, "vwap_z": z, "rsi_14": rsi, "atr_14": atr,
            "l2_source": ob.get("source", "UNAVAILABLE"),
            "gate1_spread": spread_bps <= cap,
            "gate3_cvd": cvd_sums(asset.get("cvd_1m_buckets") or []),
        }
        # ---------------- Model 2: trend pullback to Session VWAP ----------------
        if atr > 0 and vwap > 0:
            dist_atr = (mid - vwap) / atr
            row["m2"] = {
                "level": round(vwap, 6),
                "distance_atr": round(dist_atr, 3),
                "approach_trigger": round(vwap, 6),
                "direction": "SELL" if (regime or "").upper().startswith("BEAR") else (
                    "BUY" if (regime or "").upper().startswith("BULL") else "NONE"),
                "approach_ok": abs(dist_atr) <= APPROACH_ATR,
            }
            bids, asks = wall_snapshot(history, receipt_idx, symbol, vwap, WALL_BAND_ATR * atr)
            row["m2"]["entry_bid_walls"] = bids
            row["m2"]["entry_ask_walls"] = asks
            # A SELL needs the defending ask shelf; a BUY needs the defending bid shelf.
            direction = row["m2"]["direction"]
            row["m2"]["gate4_wall"] = bool(asks) if direction == "SELL" else (
                bool(bids) if direction == "BUY" else False)
        # ---------------- Model 1: |Z|>=2 extreme reversion ---------------------
        m1_level = vwap - 2.0 * sigma if sigma > 0 else None
        if m1_level:
            dist_atr = (mid - m1_level) / atr if atr > 0 else 0.0
            long_ok = z <= -2.0 and rsi < 30.0
            short_ok = z >= 2.0 and rsi > 70.0
            row["m1"] = {
                "level": round(m1_level, 6),
                "distance_atr": round(dist_atr, 3),
                "oversold_long_ok": long_ok,
                "overbought_short_ok": short_ok,
            }
            bids, asks = wall_snapshot(history, receipt_idx, symbol, m1_level, WALL_BAND_ATR * atr)
            row["m1"]["entry_bid_walls"] = bids
            row["m1"]["entry_ask_walls"] = asks
            row["m1"]["gate4_wall"] = bool(bids) if long_ok else (bool(asks) if short_ok else False)
        # ---------------- Gate 5: sizing ---------------------------------------
        row["sizing"] = sizing_options(quotes, atr)
        if row["sizing"]:
            best = row["sizing"][0]
            nominal = best["volume"] * float(quotes["contract_size"]) * (best["sl_low"] + best["sl_high"]) / 2
            stressed = nominal * STRESS_MULT + EXEC_COST_USD
            row["gate5"] = {
                "example_volume": best["volume"],
                "example_nominal_risk_usd": round(nominal, 2),
                "stress_total_usd": round(stressed, 2),
                "post_loss_equity_usd": round(equity - stressed, 2),
                "floor_ok": equity - stressed >= CUSHION_FLOOR_USD,
            }
        else:
            row["gate5"] = {"example_volume": None, "floor_ok": False}
        out["assets"][symbol] = row
    return out


def verdicts(result: dict) -> dict:
    """Per-asset verdict summary using declared gates only (fail-closed)."""
    lines = {}
    for symbol, row in result["assets"].items():
        reasons = []
        if not row["gate1_spread"]:
            reasons.append(f"G1 spread {row['spread_bps']:.2f} bps > cap")
        if row["l2_source"] != "REAL_BINANCE_FUTURES_L2":
            reasons.append("G3/G4 unavailable (L1-only feed)")
        m2 = row.get("m2", {})
        m1 = row.get("m1", {})
        if m2:
            if not m2["approach_ok"]:
                reasons.append(f"M2 not at approach ({m2['distance_atr']:+.2f} ATR from VWAP)")
            if not m2.get("gate4_wall"):
                reasons.append("M2 no persistent defending wall at VWAP (0.25 ATR band)")
        if m1:
            if not (m1["oversold_long_ok"] or m1["overbought_short_ok"]):
                reasons.append("M1 z/rsi thresholds not both met")
            if not m1.get("gate4_wall"):
                reasons.append("M1 no persistent entry wall within 0.25 ATR of +-2 sigma")
        if not row["gate5"]["floor_ok"]:
            reasons.append("G5 no admissible size in [10.00, 11.04] USD risk")
        lines[symbol] = "PASS" if not reasons else "FAIL: " + "; ".join(reasons)
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ref", default="origin/arena/83d03e3f-trading-2",
                    help="git ref holding the telemetry auto-sync commits")
    ap.add_argument("--decision-utc", default=None,
                    help="receipt time, e.g. '2026-10-08 13:28:18 UTC' (default: newest)")
    ap.add_argument("--history", type=int, default=45, help="snapshots to load for wall persistence")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    snaps = load_git_snapshots(args.ref, args.history)
    if not snaps:
        print("no telemetry snapshots found", file=sys.stderr)
        return 2
    if args.decision_utc:
        target = parse_utc(args.decision_utc)
        idx = max(i for i, s in enumerate(snaps) if s["as_of_epoch"] <= target) if any(
            s["as_of_epoch"] <= target for s in snaps) else 0
    else:
        idx = len(snaps) - 1
    receipt = snaps[idx]
    result = scan(receipt, snaps, idx, DEFAULT_SPREAD_CAP_BPS)
    result["receipt_commit_relative_index"] = idx
    result["history_samples"] = len(snaps)
    result["verdicts"] = verdicts(result)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(result, indent=1))
        print(f"wrote {args.json_out}")
    print(f"receipt {result['as_of_utc']} equity={result['equity_usd']}")
    for symbol, row in result["assets"].items():
        m2 = row.get("m2", {})
        m1 = row.get("m1", {})
        print(f"{symbol:6} {row['broker_symbol']:11} spr={row['spread_bps']:>7.2f}bps "
              f"regime={str(row['regime']):12} z={row['vwap_z']:>6.2f} rsi={row['rsi_14']:>5.1f} "
              f"m2dist={m2.get('distance_atr', ''):>6} m1dist={m1.get('distance_atr', ''):>6} "
              f"| {result['verdicts'][symbol]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
