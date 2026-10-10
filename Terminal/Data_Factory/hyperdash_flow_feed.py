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

import urllib.request
import urllib.error
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

FLOWS_JSON_PATH = ROOT / "Data" / "Hyperdash_Flows" / "hyperdash_flows_history.json"
FLOWS_PARQUET_PATH = ROOT / "Data" / "Hyperdash_Flows" / "hyperdash_flows_history.parquet"

HL_INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

logger = logging.getLogger("HyperdashFlowFeed")


def _post_json(payload: dict, timeout: int = 4) -> Any:
    """Post JSON to Hyperliquid info endpoint with strict timeout."""
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HL_INFO_URL, data=data_bytes, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def sync_live_api_flows(max_wallets_to_check: int = 8) -> int:
    """Poll native Hyperliquid L1 API for new liquidations and whale fills.
    
    Appends newly discovered records into hyperdash_flows_history.json and .parquet.
    Operates 100% headlessly via REST API without requiring Telegram or a browser.
    Returns the count of newly appended events.
    """
    records = load_raw_flow_history()
    existing_ids = {str(r.get("msg_id", "")) for r in records if r.get("msg_id")}
    new_events: List[Dict[str, Any]] = []

    # 1. Discover top active whale wallets from existing records
    whale_wallets = []
    for r in reversed(records):
        addr = r.get("wallet_address")
        if addr and addr.startswith("0x") and addr not in whale_wallets:
            whale_wallets.append(addr)
        if len(whale_wallets) >= max_wallets_to_check:
            break

    # 2. Check recent fills for liquidations across active whale wallets
    for addr in whale_wallets:
        try:
            fills = _post_json({"type": "userFills", "user": addr}, timeout=3)
            if not isinstance(fills, list):
                continue
            
            # Filter for liquidation fills
            liq_fills = [f for f in fills if f.get("liquidation")]
            if not liq_fills:
                continue

            # Group liquidation sub-fills by second and coin to reconstruct the full event
            grouped_by_event: Dict[str, List[dict]] = {}
            for f in liq_fills:
                t_sec = int(f.get("time", 0)) // 1000
                coin = str(f.get("coin", "UNKNOWN")).upper()
                event_key = f"{addr}_{coin}_{t_sec}"
                grouped_by_event.setdefault(event_key, []).append(f)

            for event_key, group in grouped_by_event.items():
                event_id = f"HL_LIQ_{event_key}"
                if event_id in existing_ids:
                    continue

                coin = str(group[0].get("coin", "UNKNOWN")).upper()
                tot_sz = sum(float(x.get("sz", 0)) for x in group)
                if tot_sz <= 0:
                    continue
                avg_px = sum(float(x.get("px", 0)) * float(x.get("sz", 0)) for x in group) / tot_sz
                tot_usd = tot_sz * avg_px
                side_raw = group[0].get("side", "")
                is_short = (side_raw == "B") # Short liquidated = buy to cover
                t_sec = int(group[0].get("time", 0)) // 1000

                record = {
                    "type": "LIQUIDATION",
                    "coin": coin,
                    "side": "SHORT_LIQUIDATED" if is_short else "LONG_LIQUIDATED",
                    "market_impact": "BUY_PRESSURE" if is_short else "SELL_PRESSURE",
                    "notional_usd": round(tot_usd, 2),
                    "distance_pct": None,
                    "duration_hours": None,
                    "rate_usd_per_min": None,
                    "price": round(avg_px, 4),
                    "wallet_address": addr,
                    "asset_slug": coin,
                    "raw_text": f"#{coin} Liquidated {'Short' if is_short else 'Long'}: {tot_usd/1e3:.2f}K USD at {avg_px:.4f} USD [API]",
                    "msg_id": event_id,
                    "time_label": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%H:%M"),
                    "date_heading": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%B %d"),
                    "source": "HYPERLIQUID_L1_NATIVE_API"
                }
                new_events.append(record)
                existing_ids.add(event_id)
        except Exception as exc:
            logger.debug("Failed querying userFills for %s: %s", addr, exc)

    # 3. Check recent ticks for large whale executions (>= 50k USD) on primary crypto assets
    core_assets = ["BTC", "ETH", "SOL", "NEAR", "DOGE", "XRP", "BNB"]
    for coin in core_assets:
        try:
            trades = _post_json({"type": "recentTrades", "coin": coin}, timeout=2)
            if not isinstance(trades, list):
                continue
            for tr in trades:
                px = float(tr.get("px", 0))
                sz = float(tr.get("sz", 0))
                notional = px * sz
                tid = str(tr.get("tid", tr.get("time", "")))
                event_id = f"HL_TRADE_{coin}_{tid}"
                if notional >= 50_000.0 and event_id not in existing_ids:
                    t_sec = int(tr.get("time", 0)) // 1000
                    side = "BUY" if tr.get("side") == "B" else "SELL"
                    users = tr.get("users", [])
                    user_addr = users[0] if users else None

                    record = {
                        "type": "WHALE_TRADE",
                        "coin": coin,
                        "side": side,
                        "market_impact": "BUY_PRESSURE" if side == "BUY" else "SELL_PRESSURE",
                        "notional_usd": round(notional, 2),
                        "distance_pct": None,
                        "duration_hours": None,
                        "rate_usd_per_min": None,
                        "price": round(px, 4),
                        "wallet_address": user_addr,
                        "asset_slug": coin,
                        "raw_text": f"#{coin} Whale {side}: {notional/1e3:.2f}K USD at {px:.4f} USD [API]",
                        "msg_id": event_id,
                        "time_label": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%H:%M"),
                        "date_heading": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%B %d"),
                        "source": "HYPERLIQUID_L1_NATIVE_API"
                    }
                    new_events.append(record)
                    existing_ids.add(event_id)
        except Exception as exc:
            logger.debug("Failed querying recentTrades for %s: %s", coin, exc)

    # 4. If new events detected, persist updated history atomically
    if new_events:
        all_records = records + new_events
        try:
            # Atomic write JSON
            tmp_json = FLOWS_JSON_PATH.with_suffix(".tmp")
            tmp_json.write_text(json.dumps(all_records, indent=2, ensure_ascii=False), encoding="utf-8")
            tmp_json.replace(FLOWS_JSON_PATH)

            # Persist Parquet
            df = pd.DataFrame(all_records)
            df.to_parquet(FLOWS_PARQUET_PATH, index=False)
            logger.info("Successfully appended %d new API flow events to history (total: %d)", len(new_events), len(all_records))
        except Exception as exc:
            logger.warning("Could not persist updated flow history: %s", exc)

    return len(new_events)


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
    # 1. Sync live events from native Hyperliquid API
    try:
        sync_live_api_flows()
    except Exception as exc:
        logger.warning("Live API flow sync failed non-fatally: %s", exc)

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
