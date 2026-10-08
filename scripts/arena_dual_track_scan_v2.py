#!/usr/bin/env python3
"""Arena dual-track scanner v2 — EVOLVED gating (briefings 2026-10-08 15:05:34 / 15:28:25 UTC).

Supersedes v1 (`arena_dual_track_scan.py`, desk commit a48002b) with the evolved mandates:

  * G1 spread is EXEMPT for passive resting limit orders (we provide liquidity).
  * Risk budget expanded to <= 15.00 USD nominal, but the G-1 operating buffer still binds:
        equity 4813.99 - (risk * 1.25 + 2.00) >= 4795.00   ->   risk <= 13.59 USD.
    The scanner uses [10.00, 13.50] as the executable window and reports the 15.00 desk cap.
  * Model 2 = ADAPTIVE MICRO-PULLBACK 0.10 - 0.60 ATR to a geometric shelf:
        20 EMA / 50 EMA / Session VWAP / VAH / VAL / 48h POC / prior 15m swing shelf /
        FVG edge — instead of demanding a full VWAP retest.
  * Model 1 = extreme stretch |Z| >= 2.0 SD with RSI < 30 (long) / > 70 (short).
  * Track 2 depth floor relaxed to >= 150k USD clustered band (desk text: 150k-300k).

Read-only: everything derives from the git-committed snapshot + committed 15m candle
parquets.  No broker I/O, no order placement.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# --- risk envelope (G-1 floor defense) -------------------------------------------------
EQUITY = 4813.99
FLOOR_THRESHOLD = 4795.00
STRESS, COST = 1.25, 2.00
RISK_CEILING_FLOOR = (EQUITY - FLOOR_THRESHOLD - COST) / STRESS      # 13.592
RISK_WINDOW = (10.00, 13.50)                                          # executable window
DESK_CAP = 15.00
SL_ATR_FLOOR = 1.50
TP_R = 2.50

# --- geometry bands --------------------------------------------------------------------
MICRO_PULLBACK_MAX_ATR = 0.60     # briefing: ultra-shallow pullback band
MICRO_PULLBACK_MIN_ATR = 0.10
AT_SHELF_TOL_ATR = 0.05           # price "at" the shelf tolerance
BAND_ATR = 0.50                   # clustered depth band: +-0.50 x ATR
BAND_DEPTH_FLOOR = 150_000.0      # evolved floor (desk text: 150k-300k)
BAND_DEPTH_STRICT = 300_000.0
WALL_FLOOR = 150_000.0

CRYPTO = "CRYPTO"


def git(*a: str) -> str:
    return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True, check=True).stdout


def load_snapshot(ref: str, path: str) -> dict:
    return json.loads(git("show", f"{ref}:{path}"))


# ------------------------------------------------------------------------- candle access
def candles(key: str, n: int = 24) -> list[dict]:
    import polars as pl
    f = REPO / "Data" / "Candles" / f"{key}_15m.parquet"
    if not f.exists():
        return []
    df = pl.read_parquet(f).sort("datetime_utc")
    out = []
    for b in df.tail(n + 20).to_dicts()[-n:]:
        out.append({
            "utc": b["datetime_utc"].strftime("%Y-%m-%d %H:%M"),
            "o": b["open"], "h": b["high"], "l": b["low"], "c": b["close"],
            "v": b["tick_volume"],
        })
    return out


def bar_stats(bars: list[dict]) -> dict | None:
    """Last completed bar: volume ratio vs prior-20 average, wick geometry."""
    if len(bars) < 21:
        return None
    hist, b = bars[-21:-1], bars[-1]
    avg = sum(x["v"] for x in hist) / 20.0
    rng = (b["h"] - b["l"]) or 1e-12
    return {
        "utc": b["utc"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"],
        "avg20": round(avg, 1), "vol_ratio": round(b["v"] / avg, 3) if avg else None,
        "upper_wick_pct": round((b["h"] - max(b["o"], b["c"])) / rng * 100, 1),
        "lower_wick_pct": round((min(b["o"], b["c"]) - b["l"]) / rng * 100, 1),
        "range": round(rng, 6),
    }


# --------------------------------------------------------------------------- book helpers
def _lvl_notional(lv) -> tuple[float, float]:
    if isinstance(lv, dict):
        p = float(lv.get("price") or lv.get("p") or 0)
        n = lv.get("notional_usd") or lv.get("usd")
        if n is None:
            q = float(lv.get("qty") or lv.get("q") or 0)
            n = p * q
        return p, float(n)
    if isinstance(lv, (list, tuple)) and len(lv) >= 2:
        return float(lv[0]), float(lv[0]) * float(lv[1])
    return 0.0, 0.0


def band_depth(levels, mid: float, atr: float, side: str) -> float:
    """Clustered notional within +-0.50 x ATR of mid on the given side."""
    if not levels or not atr:
        return 0.0
    lo, hi = mid - BAND_ATR * atr, mid + BAND_ATR * atr
    tot = 0.0
    for lv in levels:
        p, n = _lvl_notional(lv)
        if lo <= p <= hi:
            tot += n
    return round(tot, 0)


def cvd_block(buckets, as_of_epoch: int | None = None) -> dict | None:
    if not buckets:
        return None
    rows = sorted(buckets, key=lambda r: r.get("ts", 0))
    d = [r.get("cvd_delta_usd", 0.0) for r in rows]
    last = rows[-1].get("ts")
    out = {
        "buckets": len(rows),
        "last_bucket_utc_offset_s": (as_of_epoch - last) if (as_of_epoch and last) else None,
        "sum_last_3m_usd": round(sum(d[-3:]), 0),
        "sum_last_5m_usd": round(sum(d[-5:]), 0),
        "sum_prev_5m_usd": round(sum(d[-10:-5]), 0) if len(d) >= 10 else None,
        "last6_1m_usd": [round(x, 0) for x in d[-6:]],
    }
    l3 = [abs(x) for x in d[-3:]]
    p3 = [abs(x) for x in d[-6:-3]]
    out["abs_decay_3v3"] = round(sum(l3) / (sum(p3) or 1e-12), 3) if len(d) >= 6 else None
    out["decelerating"] = bool(out["abs_decay_3v3"] is not None and out["abs_decay_3v3"] < 0.85)
    out["flipped_positive"] = bool(len(d) >= 2 and d[-1] > 0 and d[-2] <= 0)
    return out


def sizing_options(specs: dict, atr: float, jpy: bool, mid: float) -> list[dict]:
    """Lot steps with SL >= 1.5xATR and nominal risk inside the executable window."""
    try:
        C = float(specs["contract_size"]); ml = float(specs["min_lot"]); st = float(specs["step_lot"])
        mx = float(specs.get("max_lot") or 1000)
    except Exception:
        return []
    lo, hi = RISK_WINDOW
    out, v = [], ml
    for _ in range(20000):
        if v > mx:
            break
        per_price = v * C * (1.0 / mid if jpy else 1.0)      # USD per 1.0 price unit
        d_lo = max(SL_ATR_FLOOR * atr, lo / per_price)
        d_hi = hi / per_price
        if d_lo <= d_hi:
            # tightest admissible stop: the ATR floor (1.5x) unless the risk floor
            # (10.00 USD) forces a wider one -> never the window midpoint.
            d = round(d_lo, 6)
            risk = per_price * d
            out.append({
                "volume": round(v, 4), "sl_distance": d, "sl_atr": round(d / atr, 3),
                "risk_usd": round(risk, 2), "stressed_usd": round(risk * STRESS + COST, 2),
                "post_loss_equity": round(EQUITY - (risk * STRESS + COST), 2),
            })
            if len(out) >= 40:
                break
        v = round(v + st, 10)
    if not out:
        return []
    # prefer the MANDATED 1.50xATR stop (tightest) and, among those, the largest
    # size that still fits the risk window; fall back to the tightest available.
    tight = [o for o in out if o["sl_atr"] <= 1.60]
    pick = max(tight, key=lambda o: o["risk_usd"]) if tight else min(out, key=lambda o: o["sl_atr"])
    return [pick] + [o for o in sorted(out, key=lambda o: o["sl_atr"]) if o is not pick][:5]


# ------------------------------------------------------------------------------- scanner
def scan(snap: dict) -> dict:
    assets, verdicts, candidates = {}, [], []
    as_of = snap.get("as_of_utc")
    acc = snap.get("account", {})
    for key, a in snap["assets_matrix_24"].items():
        q = a["quotes"]; ci = a.get("causal_indicators") or {}; vp = a.get("volume_profile") or {}
        ob = a.get("orderbook_live_depth") or {}
        specs = a.get("execution_specs") or {}
        sym = a.get("symbol_broker", key)
        cat = a.get("category", CRYPTO)
        mid = float(q["mid"]); atr = float(ci.get("atr_14") or 0)
        vwap = float(ci.get("session_vwap_utc") or 0)
        slope = float(ci.get("ema_200_slope_3h_pct") or 0)
        z = ci.get("vwap_z_score"); rsi = ci.get("rsi_14")
        base = sym.split(".")[0]
        jpy = base.endswith("JPY")
        bars = candles(key)
        bs = bar_stats(bars)
        shelves = {
            "ema20": ci.get("ema_20"), "ema50": ci.get("ema_50"), "vwap": vwap,
            "VAH": vp.get("vah"), "VAL": vp.get("val"), "POC": vp.get("poc"),
        }
        if bars:
            shelves["swing_low_2h"] = min(b["l"] for b in bars[-8:])
            shelves["swing_high_2h"] = max(b["h"] for b in bars[-8:])
        row = {
            "symbol": sym, "category": cat, "mid": mid, "atr": atr, "vwap": vwap,
            "z": z, "rsi": rsi, "slope": slope,
            "regime": ci.get("trend_regime"), "spread_bps": q.get("spread_bps"),
            "specs": {k: specs.get(k) for k in ("tick_size", "contract_size", "min_lot", "step_lot")},
            "bar": bs,
            "shelf_dist_atr": {k: (round((float(v) - mid) / atr, 3) if v and atr else None)
                               for k, v in shelves.items()},
            "track": 2 if cat == CRYPTO else 1,
        }
        # ---- geometry: model 2 micro-pullback shelves & model 1 stretch -----------------
        direction = None
        if slope < 0:      # bearish regime -> short the pullback
            cand = {k: d for k, d in row["shelf_dist_atr"].items()
                    if d is not None and -AT_SHELF_TOL_ATR <= d <= MICRO_PULLBACK_MAX_ATR}
            if cand:
                direction = "SHORT"
                row["model"] = "M2"
                row["shelf"] = min(cand, key=lambda k: abs(cand[k]))
                row["shelf_atr"] = cand[row["shelf"]]
        elif slope > 0:    # bullish regime -> buy the pullback
            cand = {k: d for k, d in row["shelf_dist_atr"].items()
                    if d is not None and -MICRO_PULLBACK_MAX_ATR <= d <= AT_SHELF_TOL_ATR}
            if cand:
                direction = "LONG"
                row["model"] = "M2"
                row["shelf"] = max(cand, key=lambda k: -abs(cand[k]))
                row["shelf_atr"] = cand[row["shelf"]]
        if direction is None and z is not None and abs(z) >= 2.0 and rsi is not None:
            if z <= -2.0 and rsi < 30:
                direction, row["model"] = "LONG", "M1"
            elif z >= 2.0 and rsi > 70:
                direction, row["model"] = "SHORT", "M1"
        row["direction"] = direction

        # ---- track-specific orderflow evidence -----------------------------------------
        if cat == CRYPTO:
            bids, asks = ob.get("bids_top20") or [], ob.get("asks_top20") or []
            bd = band_depth(bids, mid, atr, "bid"); ad = band_depth(asks, mid, atr, "ask")
            row["book"] = {
                "bid20": ob.get("top20_bid_depth_usd"), "ask20": ob.get("top20_ask_depth_usd"),
                "skew": ob.get("skew_ratio"), "imb": ob.get("book_imbalance"),
                "band_bid_usd": bd, "band_ask_usd": ad,
                "whales": [w for w in (ob.get("whale_walls_l3") or [])
                           if float(w.get("notional_usd") or 0) >= WALL_FLOOR],
                "wall_levels": ob.get("l2_wall_levels") or [],
            }
            row["cvd"] = cvd_block(a.get("cvd_1m_buckets"), snap.get("as_of_epoch"))
            if direction == "LONG":
                row["flow_a_skew_ok"] = bool((ob.get("skew_ratio") or 0) >= 1.25)
                row["flow_b_band_ok"] = bd >= BAND_DEPTH_FLOOR
                row["flow_b_band_strict_ok"] = bd >= BAND_DEPTH_STRICT
                row["flow_c_cvd_ok"] = bool(row["cvd"] and (row["cvd"]["decelerating"] or row["cvd"]["flipped_positive"]))
            elif direction == "SHORT":
                sk = ob.get("skew_ratio") or 0
                row["flow_a_skew_ok"] = bool(sk and sk <= 0.80)
                row["flow_b_band_ok"] = ad >= BAND_DEPTH_FLOOR
                row["flow_b_band_strict_ok"] = ad >= BAND_DEPTH_STRICT
                row["flow_c_cvd_ok"] = bool(row["cvd"] and not row["cvd"]["decelerating"])
        else:
            if bs and direction == "SHORT":
                row["flow_vol_ok"] = bool(bs["vol_ratio"] and bs["vol_ratio"] >= 0.8)
                row["flow_wick_ok"] = bool(bs["upper_wick_pct"] >= 30)
                row["flow_cvd_ok"] = bool(bs and bs["c"] < bs["o"])
            elif bs and direction == "LONG":
                row["flow_vol_ok"] = bool(bs["vol_ratio"] and bs["vol_ratio"] >= 0.8)
                row["flow_wick_ok"] = bool(bs["lower_wick_pct"] >= 30)
                row["flow_cvd_ok"] = bool(bs and bs["c"] > bs["o"])

        # ---- Gate 5 sizing --------------------------------------------------------------
        row["sizing"] = sizing_options(specs, atr, jpy, mid)
        row["g5_ok"] = bool(row["sizing"])
        assets[key] = row

        # ---- candidate construction ------------------------------------------------------
        if direction and row.get("g5_ok"):
            cand = build_candidate(row, snap)
            if cand:
                cand["gates"] = {
                    "geometry": True,
                    "flow_a": row.get("flow_a_skew_ok"),
                    "flow_b": row.get("flow_b_band_ok"),
                    "flow_c": row.get("flow_c_cvd_ok"),
                    "flow_vol": row.get("flow_vol_ok"),
                    "flow_wick": row.get("flow_wick_ok"),
                }
                cand["gates"]["track"] = "2crypto" if cat == CRYPTO else "1cfd"
                candidates.append(cand)
        verdicts.append({
            "symbol": sym, "track": row["track"], "model": row.get("model"),
            "direction": direction, "shelf": row.get("shelf"), "shelf_atr": row.get("shelf_atr"),
            "z": z, "rsi": rsi, "slope_pct": slope, "spread_bps": q.get("spread_bps"),
            "g5_ok": row["g5_ok"],
            "flow_a": row.get("flow_a_skew_ok"), "flow_b": row.get("flow_b_band_ok"),
            "flow_c": row.get("flow_c_cvd_ok"),
            "flow_vol": row.get("flow_vol_ok"), "flow_wick": row.get("flow_wick_ok"),
        })
    return {"as_of_utc": as_of, "equity": acc.get("equity_usd"), "assets": assets,
            "verdicts": verdicts, "candidates": candidates,
            "envelope": {"risk_window": RISK_WINDOW, "desk_cap": DESK_CAP,
                         "floor_risk_ceiling": round(RISK_CEILING_FLOOR, 3),
                         "micro_pullback_atr": [MICRO_PULLBACK_MIN_ATR, MICRO_PULLBACK_MAX_ATR]}}


def build_candidate(row: dict, snap: dict) -> dict | None:
    import math
    mid, atr = row["mid"], row["atr"]
    if not row.get("sizing"):
        return None
    sz = row["sizing"][len(row["sizing"]) // 2] if len(row["sizing"]) > 1 else row["sizing"][0]
    tick = float(row["specs"].get("tick_size") or 0.0001)
    digits = max(0, int(round(-math.log10(tick)))) if tick else 4
    direction = row["direction"]
    shelf_price = None
    key = row.get("shelf")
    if key and row.get("shelf_dist_atr", {}).get(key) is not None:
        shelf_price = mid + row["shelf_dist_atr"][key] * atr
    if row["model"] == "M2" and direction == "SHORT":
        entry = shelf_price or mid
        sl = entry + sz["sl_distance"]; tp = entry - TP_R * sz["sl_distance"]
    elif row["model"] == "M2" and direction == "LONG":
        entry = shelf_price or mid
        sl = entry - sz["sl_distance"]; tp = entry + TP_R * sz["sl_distance"]
    else:  # Model 1: enter at the wall/market; long flush or short squeeze
        entry = mid
        if direction == "LONG":
            sl = entry - sz["sl_distance"]; tp = entry + TP_R * sz["sl_distance"]
        else:
            sl = entry + sz["sl_distance"]; tp = entry - TP_R * sz["sl_distance"]
    entry = round(entry, digits); sl = round(sl, digits); tp = round(tp, digits)
    risk = abs(entry - sl) * float(row["specs"].get("contract_size") or 1) * sz["volume"]
    jpy = row["symbol"].split(".")[0].endswith("JPY")
    if jpy:
        risk /= entry
    return {
        "symbol": row["symbol"], "track": row["track"], "model": row["model"],
        "direction": direction, "entry": entry, "sl": sl, "tp": tp,
        "volume": sz["volume"], "sl_atr": round(abs(entry - sl) / atr, 3),
        "r_multiple": round(abs(tp - entry) / abs(entry - sl), 3) if entry != sl else None,
        "risk_usd": round(risk, 2), "stressed_usd": round(risk * STRESS + COST, 2),
        "post_loss_equity": round(EQUITY - (risk * STRESS + COST), 2),
        "shelf": row.get("shelf"), "shelf_atr": row.get("shelf_atr"),
        "bar": row.get("bar"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/arena/24eb818b-trading-2")
    ap.add_argument("--snapshot-path", default="docs/telemetry/live_snapshot_latest.json")
    ap.add_argument("--json-out")
    args = ap.parse_args()
    snap = load_snapshot(args.ref, args.snapshot_path)
    res = scan(snap)
    print(f"as_of {res['as_of_utc']} | equity {res['equity']} | envelope {res['envelope']}")
    print(f"{'symbol':12s} {'trk':3s} {'model':5s} {'dir':5s} {'shelf':12s} {'shl@ATR':>8s} "
          f"{'z':>7s} {'rsi':>6s} {'slope%':>8s} {'vol':>5s} {'uw%':>5s} {'lw%':>5s} "
          f"{'skew':>7s} {'band-B':>10s} {'band-A':>10s} {'flw':>12s}")
    for k, v in res["assets"].items():
        b = v.get("bar") or {}
        bk = v.get("book") or {}
        bb = bk.get("band_bid_usd"); ba = bk.get("band_ask_usd")
        bbs = "n/a" if bb is None else format(bb, ",.0f")
        bas = "n/a" if ba is None else format(ba, ",.0f")
        fl = "/".join(str(x) for x in (v.get("flow_a_skew_ok"), v.get("flow_b_band_ok"),
                                       v.get("flow_c_cvd_ok"), v.get("flow_vol_ok"),
                                       v.get("flow_wick_ok")) if x is not None)
        print(f"{v['symbol']:12s} {v['track']:<3d} {str(v.get('model')):5s} {str(v.get('direction')):5s} "
              f"{str(v.get('shelf')):12s} {str(v.get('shelf_atr')):>8s} {str(v.get('z')):>7s} "
              f"{str(v.get('rsi')):>6s} {str(round(v['slope'],4)):>8s} {str(b.get('vol_ratio')):>5s} "
              f"{str(b.get('upper_wick_pct')):>5s} {str(b.get('lower_wick_pct')):>5s} "
              f"{str(bk.get('skew')):>7s} {bbs:>10s} {bas:>10s}  {fl}")
    print("\nCANDIDATES")
    for c in res["candidates"]:
        print(" ", json.dumps(c, default=str))
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(res, indent=1, default=str))
        print("wrote", args.json_out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
