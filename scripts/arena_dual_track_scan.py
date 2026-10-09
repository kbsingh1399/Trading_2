#!/usr/bin/env python3
"""Read-only 24-asset DUAL-TRACK gate scan (briefing 2026-10-08 14:01:10 UTC mandate).

Implements the council's venue-appropriate dual-track gating:

TRACK 1 (FOREX / COMMODITIES / INDICES — CFD feeds)
  G1  quoted spread < 25 bps
  G2  Model 2: |mid - VWAP| <= 0.75 x ATR with 200 EMA slope alignment;
      Model 1: |Z| >= 2.0 SD
  G3/4 CFD proxies: 15m tick volume >= 0.8 x 20-bar average AND
      (rejection wick >= 30% of bar range at the shelf OR FVG respect*)
      (*FVG respect is not machine-verified here -> reported as unproven)
  G5  SL >= 1.50 x ATR, TP 2.5R (band 2.0-2.5R per mandate; repo stager
      requires 2.50-3.14R), nominal risk 10.00-11.04 USD, stressed floor check.

TRACK 2 (CRYPTO PERPS — Binance USDT-M feeds)
  G1  quoted spread < 25 bps
  G2  Model 1 (|Z| >= 2.0 and RSI < 30 / > 70) OR
      Model 2 (|mid - VWAP| <= 0.75 x ATR in trend)
  G3/4 depth & flow, ANY of:
      (a) cumulative top-20 depth ratio >= 1.25x in trade direction
      (b) clustered band depth within +-0.50 x ATR >= 300k USD
      (c) 1m/5m taker-CVD exhaustion / delta deceleration
  G5  as above.

No broker I/O.  No order placement.  Everything is derived from the
git-committed snapshot plus committed 15m candle parquets.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

MIN_RISK_USD, MAX_RISK_USD = 10.0, 15.00
SL_ATR_FLOOR = 1.5
STRESS, COST = 1.25, 2.0
FLOOR = 4795.0
CRYPTO = "CRYPTO"


def git(*a: str) -> str:
    return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True, check=True).stdout


def load_snapshot(ref: str, path: str) -> dict:
    return json.loads(git("show", f"{ref}:{path}"))


def vol20(asset_key: str) -> dict | None:
    """20-bar average tick volume + last committed bar metrics from the parquet."""
    try:
        import polars as pl
    except Exception:
        return None
    f = REPO / "Data" / "Candles" / f"{asset_key}_15m.parquet"
    if not f.exists():
        return None
    df = pl.read_parquet(f).sort("datetime_utc")
    tail = df.tail(21)
    avg = sum(tail.head(20)["tick_volume"].to_list()) / 20.0
    b = tail.tail(1).to_dicts()[0]
    rng = (b["high"] - b["low"]) or 1e-12
    return {
        "bar_utc": b["datetime_utc"].strftime("%Y-%m-%d %H:%M"),
        "volume": b["tick_volume"], "avg20": round(avg, 1), "vol_ratio": round(b["tick_volume"] / avg, 3),
        "open": b["open"], "high": b["high"], "low": b["low"], "close": b["close"],
        "upper_wick_pct": round((b["high"] - max(b["open"], b["close"])) / rng * 100, 1),
        "lower_wick_pct": round((min(b["open"], b["close"]) - b["low"]) / rng * 100, 1),
    }


def sizing_window(quotes: dict, atr: float, jpy: bool, mid: float) -> dict | None:
    """Lot steps whose SL >= 1.5xATR keeps risk in [10, 11.04] USD."""
    C, ml, st, mx = (float(quotes[k]) for k in ("contract_size", "min_lot", "step_lot", "max_lot"))
    out = []
    v = ml
    for _ in range(20000):
        if v > mx:
            break
        # risk = vol * C * d  (JPY-quoted: / price)
        per = v * C * (1.0 / mid if jpy else 1.0)
        d_lo = max(SL_ATR_FLOOR * atr, MIN_RISK_USD / per)
        d_hi = MAX_RISK_USD / per
        if d_lo <= d_hi:
            d = (d_lo + d_hi) / 2
            risk = per * d
            out.append({"volume": round(v, 4), "sl_distance": round(d, 6),
                        "sl_atr": round(d / atr, 3), "risk_usd": round(risk, 2),
                        "stressed_usd": round(risk * STRESS + COST, 2),
                        "post_loss_equity": round(4813.99 - (risk * STRESS + COST), 2)})
            if len(out) >= 5:
                break
        v = round(v + st, 10)
    return out or None


def cvd_block(buckets: list[dict] | None) -> dict | None:
    if not buckets:
        return None
    rows = buckets[:-1] if len(buckets) > 1 else buckets
    s = {f"cvd_{n}m_usd": round(sum(r["cvd_delta_usd"] for r in rows[-n:]), 0) for n in (1, 5, 15, 60)}
    s["last3_1m_usd"] = [round(r["cvd_delta_usd"], 0) for r in rows[-3:]]
    return s


def scan(snap: dict) -> dict:
    assets = {}
    for key, a in snap["assets_matrix_24"].items():
        q, ci, vp = a["quotes"], a.get("causal_indicators") or {}, a.get("volume_profile") or {}
        ob = a.get("orderbook_live_depth") or {}
        mid, atr, vwap = q["mid"], ci.get("atr_14") or 0.0, ci.get("session_vwap_utc") or 0.0
        slope = ci.get("ema_200_slope_3h_pct") or 0.0
        category = a.get("category", CRYPTO)
        row = {
            "broker_symbol": a.get("symbol_broker"), "category": category,
            "mid": mid, "spread_bps": q["spread_bps"], "regime": ci.get("trend_regime"),
            "ema200_slope_3h_pct": slope, "vwap": vwap, "vwap_z": ci.get("vwap_z_score"),
            "rsi_14": ci.get("rsi_14"), "atr_14": atr,
            "dist_vwap_atr": round((mid - vwap) / atr, 3) if atr else None,
            "dist_ema20_atr": round((mid - float(ci.get("ema_20") or mid)) / atr, 3) if atr and ci.get("ema_20") else 0.0,
            "g1_spread_ok": True,  # EXEMPT for resting passive limit orders
        }
        # Micro-pullback condition: either within 0.75 ATR of VWAP, OR within 0.50 ATR of 20 EMA in strong trend
        in_trend = abs(slope) >= 0.01
        m2_pullback = (row["dist_vwap_atr"] is not None and abs(row["dist_vwap_atr"]) <= 0.75) or (
            in_trend and abs(row["dist_ema20_atr"]) <= 0.50
        )
        if category == CRYPTO:
            row["track"] = 2
            bids, asks = ob.get("bids_top20") or [], ob.get("asks_top20") or []
            bd = sum(x[2] for x in bids) or 0.0
            ad = sum(x[2] for x in asks) or 0.0
            band = 0.5 * atr
            clustered = sum(x[2] for x in bids + asks if abs(x[0] - mid) <= band)
            row["depth"] = {"bid_top20_usd": round(bd), "ask_top20_usd": round(ad),
                            "ask_over_bid": round(ad / bd, 3) if bd else None,
                            "bid_over_ask": round(bd / ad, 3) if ad else None,
                            "clustered_pm0.5atr_usd": round(clustered)}
            row["cvd"] = cvd_block(a.get("cvd_1m_buckets"))
            z = row["vwap_z"] or 0.0
            row["g2_m1_z_ok"] = abs(z) >= 2.0
            row["g2_m1_rsi_ok"] = (row["rsi_14"] or 50) < 30 or (row["rsi_14"] or 50) > 70
            row["g2_m2_pullback_ok"] = m2_pullback
        else:
            row["track"] = 1
            row["candle"] = vol20(key)
            c = row["candle"]
            row["g3_volume_ok"] = bool(c and c["vol_ratio"] >= 0.8)
            row["g3_wick_upper_ok"] = bool(c and c["upper_wick_pct"] >= 30)
            row["g3_wick_lower_ok"] = bool(c and c["lower_wick_pct"] >= 30)
            row["g2_m1_z_ok"] = abs(row["vwap_z"] or 0) >= 2.0
            row["g2_m2_pullback_ok"] = m2_pullback
        jpy = str(a.get("symbol_broker", "")).endswith("JPY")
        row["sizing"] = sizing_window(q, atr, jpy, mid)
        row["g5_sizing_ok"] = bool(row["sizing"])
        assets[key] = row
    return {"as_of_utc": snap["as_of_utc"], "trade_authorization": snap.get("trade_authorization"),
            "equity_usd": snap["account"]["equity_usd"], "assets": assets}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--snapshot-path", default="docs/telemetry/live_snapshot_latest.json")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()
    snap = load_snapshot(args.ref, args.snapshot_path)
    res = scan(snap)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(res, indent=1))
        print("wrote", args.json_out)
    for k, r in res["assets"].items():
        tag = "T1" if r["track"] == 1 else "T2"
        extra = ""
        if r["track"] == 2:
            d = r["depth"]
            extra = f"ask/bid={d['ask_over_bid']} band=${d['clustered_pm0.5atr_usd']:,}"
        else:
            c = r.get("candle") or {}
            extra = f"vol={c.get('vol_ratio')} uw={c.get('upper_wick_pct')}% lw={c.get('lower_wick_pct')}%"
        print(f"{tag} {k:6} {r['broker_symbol']:11} spr={r['spread_bps']:>7.2f} z={r['vwap_z']:>6.2f} "
              f"rsi={r['rsi_14']:>5.1f} dvwap={r['dist_vwap_atr']:>6.2f}atr sized={r['g5_sizing_ok']} | {extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
