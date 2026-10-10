#!/usr/bin/env python3
"""
Terminal/Data_Factory/hyperdash_flow_feed.py
=============================================
Hyperdash Flow Intelligence & On-Chain Orderflow Aggregator.
Consolidates parsed Telegram channel alerts (@hyperdashflows) and native
Hyperliquid L1 blockchain state into an institutional-grade intelligence feed.

Provides structured signals for:
1. Active Institutional TWAPs (Direction, notional USD, duration, $/min rate).
2. Imminent Liquidation Hazards (Near-term liquidation cascades <= 1.5% away).
3. Confirmed Liquidations (Forced buying/selling pressure).
4. Whale Executions & Position Closes (Notionals >= 10M USD and realized PnL).
5. Open Interest & Volume Surges (5m momentum spikes and buy/sell delta).
6. Macro Collateral Movements (Large USDC deposits, withdrawals, and staking flows).
7. Per-Asset Flow Attribution across our trading universe.
"""

from __future__ import annotations

import json
import logging
import os
import pathlib
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

FLOWS_JSON_PATH = ROOT / "Data" / "Hyperdash_Flows" / "hyperdash_flows_history.json"
FLOWS_PARQUET_PATH = ROOT / "Data" / "Hyperdash_Flows" / "hyperdash_flows_history.parquet"

logger = logging.getLogger("HyperdashFlowFeed")


def load_raw_flow_history() -> List[Dict[str, Any]]:
    """Load historical flows archive safely."""
    if not FLOWS_JSON_PATH.exists():
        return []
    try:
        data = json.loads(FLOWS_JSON_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception as exc:
        logger.warning("Could not read hyperdash_flows_history.json: %s", exc)
        return []


def get_hyperdash_flow_intelligence(max_recent_items: int = 50) -> Dict[str, Any]:
    """Aggregate Hyperdash flow records into a high-density intelligence payload.
    
    Designed for zero-latency injection into live_snapshot_latest.json and
    direct evaluation by AI models (Arena.ai / Opus 5.5) and local decision gates.
    """
    records = load_raw_flow_history()
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Categorized buckets
    twaps: List[Dict[str, Any]] = []
    imminent_liqs: List[Dict[str, Any]] = []
    confirmed_liqs: List[Dict[str, Any]] = []
    whale_trades: List[Dict[str, Any]] = []
    position_closes: List[Dict[str, Any]] = []
    oi_surges: List[Dict[str, Any]] = []
    volume_surges: List[Dict[str, Any]] = []
    funding_surges: List[Dict[str, Any]] = []
    collateral_flows: List[Dict[str, Any]] = []
    market_summaries: List[Dict[str, Any]] = []

    # Aggregation accumulators
    total_liq_volume_usd = 0.0
    long_liq_volume_usd = 0.0
    short_liq_volume_usd = 0.0
    total_twap_notional_usd = 0.0
    total_inflow_usd = 0.0
    total_outflow_usd = 0.0
    asset_aggregates: Dict[str, Dict[str, Any]] = {}

    for r in records:
        rtype = r.get("type", "UNKNOWN")
        coin = str(r.get("coin", "UNKNOWN")).upper()
        notional = float(r.get("notional_usd") or 0.0)
        side = r.get("side", "")

        # Per-asset breakdown tracking
        if coin not in asset_aggregates and coin != "UNKNOWN":
            asset_aggregates[coin] = {
                "liquidations_usd": 0.0,
                "imminent_liqs_usd": 0.0,
                "twap_notional_usd": 0.0,
                "whale_trades_usd": 0.0,
                "oi_surges_count": 0,
                "dominant_bias": "NEUTRAL"
            }

        if rtype == "TWAP_STARTED":
            twaps.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "duration_hours": r.get("duration_hours"),
                "rate_usd_per_min": r.get("rate_usd_per_min"),
                "wallet_address": r.get("wallet_address"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading"),
                "impact": "PASSIVE_ACCUMULATION" if side == "BUY" else "PASSIVE_DISTRIBUTION"
            })
            total_twap_notional_usd += notional
            if coin in asset_aggregates:
                asset_aggregates[coin]["twap_notional_usd"] += notional

        elif rtype == "IMMINENT_LIQUIDATION":
            imminent_liqs.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "distance_pct": r.get("distance_pct"),
                "price": r.get("price"),
                "wallet_address": r.get("wallet_address"),
                "market_impact": r.get("market_impact"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })
            if coin in asset_aggregates:
                asset_aggregates[coin]["imminent_liqs_usd"] += notional

        elif rtype == "LIQUIDATION":
            confirmed_liqs.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "price": r.get("price"),
                "wallet_address": r.get("wallet_address"),
                "market_impact": r.get("market_impact"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })
            total_liq_volume_usd += notional
            if "LONG" in side:
                long_liq_volume_usd += notional
            elif "SHORT" in side:
                short_liq_volume_usd += notional
            if coin in asset_aggregates:
                asset_aggregates[coin]["liquidations_usd"] += notional

        elif rtype == "WHALE_TRADE":
            whale_trades.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "price": r.get("price"),
                "wallet_address": r.get("wallet_address"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })
            if coin in asset_aggregates:
                asset_aggregates[coin]["whale_trades_usd"] += notional

        elif rtype == "WHALE_POSITION_CLOSE":
            position_closes.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "realized_pnl_usd": r.get("realized_pnl_usd"),
                "wallet_address": r.get("wallet_address"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })

        elif rtype == "OI_SURGE":
            oi_surges.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "oi_delta_usd": r.get("oi_delta_usd"),
                "timeframe": r.get("timeframe"),
                "surge_multiple": r.get("surge_multiple"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })
            if coin in asset_aggregates:
                asset_aggregates[coin]["oi_surges_count"] += 1

        elif rtype == "VOLUME_SURGE":
            volume_surges.append({
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "avg_volume_usd": r.get("avg_volume_usd"),
                "delta_volume_usd": r.get("delta_volume_usd"),
                "timeframe": r.get("timeframe"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })

        elif rtype == "FUNDING_SURGE":
            funding_surges.append({
                "coin": coin,
                "apr_pct": r.get("apr_pct"),
                "side": r.get("side"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })

        elif rtype in ("LARGE_DEPOSIT", "LARGE_WITHDRAWAL", "STAKING_FLOW"):
            collateral_flows.append({
                "type": rtype,
                "coin": coin,
                "side": side,
                "notional_usd": notional,
                "wallet_address": r.get("wallet_address"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })
            if rtype == "LARGE_DEPOSIT" or "STAKED" in side:
                total_inflow_usd += notional
            elif rtype == "LARGE_WITHDRAWAL" or "UNSTAKE" in side:
                total_outflow_usd += notional

        elif rtype == "MARKET_SUMMARY":
            market_summaries.append({
                "volume_24h_usd": r.get("volume_24h_usd"),
                "liquidations_24h_usd": r.get("liquidations_24h_usd"),
                "open_interest_usd": r.get("open_interest_usd"),
                "time_label": r.get("time_label"),
                "date_heading": r.get("date_heading")
            })

    # Compute dominant bias per asset
    for coin, stats in asset_aggregates.items():
        liq_val = stats["liquidations_usd"]
        imminent_val = stats["imminent_liqs_usd"]
        twap_val = stats["twap_notional_usd"]
        if liq_val > 5_000_000.0 or imminent_val > 5_000_000.0:
            stats["dominant_bias"] = "HIGH_LIQUIDATION_VOLATILITY"
        elif twap_val > 5_000_000.0:
            stats["dominant_bias"] = "INSTITUTIONAL_TWAP_ACCUMULATION"
        elif stats["oi_surges_count"] > 0:
            stats["dominant_bias"] = "AGGRESSIVE_OI_EXPANSION"

    # Overall macro market bias
    if long_liq_volume_usd > short_liq_volume_usd * 1.5:
        macro_tilt = "BEARISH_LONG_FLUSH_PREDOMINATES"
    elif short_liq_volume_usd > long_liq_volume_usd * 1.5:
        macro_tilt = "BULLISH_SHORT_SQUEEZE_PREDOMINATES"
    else:
        macro_tilt = "BALANCED_TWO_SIDED_FLOW"

    return {
        "source": "HYPERDASH_FLOWS_TELEGRAM_AND_HYPERLIQUID_L1_BLOCKCHAIN",
        "protocol": "hyperdash.flow.v1.structured",
        "as_of_utc": now_utc,
        "as_of_epoch": time.time(),
        "summary": {
            "total_alerts_tracked": len(records),
            "total_liquidations_count": len(confirmed_liqs),
            "total_liquidations_volume_usd": round(total_liq_volume_usd, 2),
            "long_liquidations_volume_usd": round(long_liq_volume_usd, 2),
            "short_liquidations_volume_usd": round(short_liq_volume_usd, 2),
            "long_to_short_liq_ratio": round(long_liq_volume_usd / max(short_liq_volume_usd, 1.0), 2),
            "imminent_liquidation_alerts_count": len(imminent_liqs),
            "active_twap_orders_count": len(twaps),
            "total_twap_notional_usd": round(total_twap_notional_usd, 2),
            "whale_trades_count": len(whale_trades),
            "oi_surges_count": len(oi_surges),
            "volume_surges_count": len(volume_surges),
            "collateral_inflows_usd": round(total_inflow_usd, 2),
            "collateral_outflows_usd": round(total_outflow_usd, 2),
            "net_collateral_expansion_usd": round(total_inflow_usd - total_outflow_usd, 2),
            "macro_orderflow_tilt": macro_tilt
        },
        "active_institutional_twaps": twaps[-max_recent_items:],
        "imminent_liquidation_hazards": imminent_liqs[-max_recent_items:],
        "recent_confirmed_liquidations": confirmed_liqs[-max_recent_items:],
        "whale_trades": whale_trades[-max_recent_items:],
        "whale_position_closes": position_closes[-max_recent_items:],
        "open_interest_surges": oi_surges[-max_recent_items:],
        "volume_surges": volume_surges[-max_recent_items:],
        "funding_surges": funding_surges[-max_recent_items:],
        "collateral_and_staking_flows": collateral_flows[-max_recent_items:],
        "market_daily_summaries": market_summaries[-5:],
        "universe_asset_breakdown": {
            k: v for k, v in asset_aggregates.items()
            if v["liquidations_usd"] > 0 or v["twap_notional_usd"] > 0 or v["whale_trades_usd"] > 0 or v["imminent_liqs_usd"] > 0
        }
    }


if __name__ == "__main__":
    import pprint
    data = get_hyperdash_flow_intelligence()
    print("--- HYPERDASH FLOW INTELLIGENCE SUMMARY ---")
    pprint.pprint(data["summary"])
    print("\n--- SAMPLE IMMINENT LIQUIDATION HAZARDS (Top 3) ---")
    pprint.pprint(data["imminent_liquidation_hazards"][:3])
    print("\n--- SAMPLE ACTIVE TWAPs (Top 3) ---")
    pprint.pprint(data["active_institutional_twaps"][:3])
    print("\n--- SAMPLE UNIVERSE ASSET BREAKDOWN (Top 5) ---")
    for asset, info in list(data["universe_asset_breakdown"].items())[:5]:
        print(f"  * {asset:<12}: {info}")
