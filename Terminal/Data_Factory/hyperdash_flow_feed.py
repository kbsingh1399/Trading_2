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
import hashlib
import tempfile
import threading
from collections import Counter
from contextlib import contextmanager
from decimal import Decimal
from pathlib import Path
import logging
import math
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
    """Post JSON to Hyperliquid info endpoint with strict timeout and safe error handling."""
    try:
        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(HL_INFO_URL, data=data_bytes, headers=DEFAULT_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        logger.debug("Hyperliquid POST failed for %s: %s", payload.get("type"), exc)
        return None


_PERSIST_LOCK = threading.RLock()


@contextmanager
def _flow_archive_lock(target: Path):
    """Serialize cooperating writers, including the read/merge/replace operation."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with _PERSIST_LOCK, target.with_name(target.name + ".lock").open("a+b") as lock:
        if lock.seek(0, os.SEEK_END) == 0:
            lock.write(b"0")
            lock.flush()
        deadline = time.monotonic() + 10.0
        while True:
            try:
                lock.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise TimeoutError("Timed out waiting for flow archive writer")
                time.sleep(0.05)
        try:
            yield
        finally:
            lock.seek(0)
            if os.name == "nt":
                msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def _persist_flows_unlocked(records, target_json, target_parquet):
    temporary_paths = []
    previous_parquet = None
    parquet_replaced = False
    try:
        target_parquet.parent.mkdir(parents=True, exist_ok=True)
        for target in (target_json, target_parquet):
            fd, name = tempfile.mkstemp(prefix=target.name + ".tmp.", dir=target.parent)
            os.close(fd)
            temporary_paths.append(Path(name))
        # Telegram and API IDs can have different input types. Both files use strings.
        normalized = [dict(r, msg_id=str(r["msg_id"])) if r.get("msg_id") is not None else dict(r)
                      for r in records]
        temporary_paths[0].write_text(json.dumps(normalized, indent=2, ensure_ascii=False, allow_nan=False), encoding="utf-8")
        pd.DataFrame(normalized).to_parquet(temporary_paths[1], index=False)
        previous_parquet = target_parquet.read_bytes() if target_parquet.exists() else None
        temporary_paths[1].replace(target_parquet)
        parquet_replaced = True
        temporary_paths[0].replace(target_json)
        return True
    except Exception as exc:
        logger.warning("Could not persist updated flow history: %s", exc)
        if parquet_replaced:
            try:
                if previous_parquet is None:
                    target_parquet.unlink()
                else:
                    temporary_paths[1].write_bytes(previous_parquet)
                    temporary_paths[1].replace(target_parquet)
            except OSError as rollback_exc:
                logger.error("Could not restore previous Parquet generation: %s", rollback_exc)
        return False
    finally:
        for path in temporary_paths:
            path.unlink(missing_ok=True)


def atomic_persist_flows(records: List[Dict[str, Any]], json_target: Optional[Path] = None, parquet_target: Optional[Path] = None) -> bool:
    """Replace each file atomically under a writer lock; JSON is the commit point.

    Two paths cannot be replaced as one filesystem transaction. A process crash
    between replacements can leave Parquet ahead of authoritative JSON.
    """
    target_json = json_target or FLOWS_JSON_PATH
    target_parquet = parquet_target or FLOWS_PARQUET_PATH
    try:
        with _flow_archive_lock(target_json):
            return _persist_flows_unlocked(records, target_json, target_parquet)
    except OSError as exc:
        logger.warning("Could not lock flow archive: %s", exc)
        return False


def _record_identity(record):
    msg_id = record.get("msg_id")
    if msg_id is None or not str(msg_id).strip():
        return None
    return (str(record.get("source") or "UNSPECIFIED"),
            str(record.get("coin") or "UNKNOWN").upper(),
            str(record.get("type") or "UNKNOWN"), str(msg_id))


def _unique_records(records):
    seen = set()
    result = []
    for record in records:
        if not isinstance(record, dict):
            continue
        identity = _record_identity(record)
        if identity is not None:
            if identity in seen:
                continue
            seen.add(identity)
        result.append(record)
    return result


def _fill_id(coin, fill, occurrences):
    """Match observed payload multiplicity when a provider supplies no unique ID.

    Indistinguishable fills entering/leaving a rolling response cannot be proven
    distinct. Occurrence ranks preserve the maximum simultaneously visible count.
    """
    raw_tid = fill.get("tid")
    if raw_tid is not None and str(raw_tid).strip() and str(raw_tid) != "None":
        return str(raw_tid)
    if fill.get("time") is None:
        return None
    fingerprint = json.dumps([
        coin, int(fill["time"]), str(Decimal(str(fill["px"])).normalize()),
        str(Decimal(str(fill["sz"])).normalize()), str(fill.get("side") or "").upper(),
        fill.get("hash"), fill.get("users"),
    ], separators=(",", ":"), sort_keys=True)
    digest = hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()
    occurrences[digest] += 1
    return f"FALLBACK_{digest}_{occurrences[digest]}"


def load_raw_flow_history(raise_on_error: bool = False, json_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Load historical flows archive safely.
    
    If raise_on_error is True, raises any disk/parse errors instead of silently
    returning [] to prevent accidental history truncation during sync.
    """
    target = json_path or FLOWS_JSON_PATH
    if not target.exists():
        return []
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
        if not isinstance(data, list) or any(not isinstance(r, dict) for r in data):
            raise ValueError("Flow history must be a list of record objects")
        return data
    except Exception as exc:
        logger.warning("Could not read flow history from %s: %s", target, exc)
        if raise_on_error:
            raise
        return []


def sync_live_api_flows(max_wallets_to_check: int = 8) -> int:
    """Poll native Hyperliquid L1 API for new liquidations and whale fills.
    
    Appends newly discovered records into hyperdash_flows_history.json and .parquet.
    Operates 100% headlessly via REST API without requiring Telegram or a browser.
    Returns the count of newly appended events.
    """
    try:
        records = load_raw_flow_history(raise_on_error=True)
    except Exception as exc:
        logger.error("Aborting flow sync: could not safely read flow history: %s", exc)
        return 0

    existing_ids = {str(r["msg_id"]) for r in records
                    if r.get("msg_id") is not None and r.get("source") == "HYPERLIQUID_L1_NATIVE_API"}
    legacy_liquidation_ids = {str(r["msg_id"]) for r in records
                              if r.get("msg_id") and r.get("type") == "LIQUIDATION"
                              and r.get("source") == "HYPERLIQUID_L1_NATIVE_API"
                              and not r.get("identity_basis")}
    new_events: List[Dict[str, Any]] = []

    # 1. Discover top active whale wallets from existing records
    whale_wallets = []
    for r in reversed(records):
        addr = r.get("wallet_address")
        if isinstance(addr, str) and addr.startswith("0x") and addr not in whale_wallets:
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
            liq_fills = [f for f in fills if isinstance(f, dict) and f.get("liquidation")]
            if not liq_fills:
                continue

            # Each fill has its own identity; later sub-fills cannot disappear into an earlier second.
            occurrences = Counter()
            for fill in liq_fills:
                if fill.get("time") is None:
                    continue
                coin = str(fill.get("coin", "UNKNOWN")).upper()
                side_raw = str(fill.get("side") or "").upper()
                try:
                    avg_px = float(fill.get("px") or 0.0)
                    tot_sz = float(fill.get("sz") or 0.0)
                    t_sec = int(fill["time"]) // 1000
                except (ValueError, TypeError, OverflowError):
                    continue
                # Legacy aggregate rows lack fill IDs; do not recount their covered seconds.
                if f"HL_LIQ_{addr}_{coin}_{t_sec}" in legacy_liquidation_ids:
                    continue
                if side_raw not in ("B", "A") or not all(math.isfinite(x) and x > 0 for x in (avg_px, tot_sz)):
                    continue
                tid = _fill_id(coin, fill, occurrences)
                if tid is None:
                    continue
                event_id = f"HL_LIQ_{addr}_{coin}_{tid}"
                if event_id in existing_ids:
                    continue
                tot_usd = tot_sz * avg_px
                if not math.isfinite(tot_usd):
                    continue
                is_short = side_raw == "B"

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
                    "timestamp_epoch": t_sec,
                    "time_label": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%H:%M"),
                    "date_heading": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%B %d"),
                    "source": "HYPERLIQUID_L1_NATIVE_API",
                    "identity_basis": "NATIVE_TID" if not tid.startswith("FALLBACK_") else "PAYLOAD_MULTIPLICITY",
                }
                new_events.append(record)
                existing_ids.add(event_id)
        except Exception as exc:
            logger.debug("Failed querying userFills for %s: %s", addr, exc)

    # 3. Check recent ticks for large whale executions (>= 50k USD) on primary crypto assets
    # Covers full Binance 11 perpetual universe + primary Hyperliquid perp liquidity
    core_assets = ["BTC", "ETH", "SOL", "NEAR", "DOGE", "XRP", "BNB", "ADA", "TRX", "LINK", "DOT", "LTC", "BCH"]
    fallback_occurrences = Counter()
    for coin in core_assets:
        try:
            trades = _post_json({"type": "recentTrades", "coin": coin}, timeout=2)
            if not isinstance(trades, list):
                continue
            for tr in trades:
                if not isinstance(tr, dict):
                    continue
                try:
                    px = float(tr.get("px") or 0.0)
                    sz = float(tr.get("sz") or 0.0)
                    t_sec = int(tr["time"]) // 1000
                except (ValueError, TypeError, OverflowError, KeyError):
                    continue
                notional = px * sz
                if not all(math.isfinite(x) and x > 0 for x in (px, sz, notional)) or notional < 50_000.0:
                    continue
                side_char = str(tr.get("side") or "").upper()
                if side_char not in ("B", "A"):
                    continue
                side = "BUY" if side_char == "B" else "SELL"
                
                # Occurrence ranks preserve visible identical fills across overlapping polls.
                tid = _fill_id(coin, tr, fallback_occurrences)
                if tid is None:
                    continue

                event_id = f"HL_TRADE_{coin}_{tid}"
                if event_id not in existing_ids:
                    users = tr.get("users", [])
                    user_addr = users[0] if users and isinstance(users, list) else None

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
                        "timestamp_epoch": t_sec,
                        "time_label": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%H:%M"),
                        "date_heading": datetime.fromtimestamp(t_sec, tz=timezone.utc).strftime("%B %d"),
                        "source": "HYPERLIQUID_L1_NATIVE_API",
                        "identity_basis": "NATIVE_TID" if not tid.startswith("FALLBACK_") else "PAYLOAD_MULTIPLICITY",
                    }
                    new_events.append(record)
                    existing_ids.add(event_id)
        except Exception as exc:
            logger.debug("Failed querying recentTrades for %s: %s", coin, exc)

    # Re-read inside the lock: another poll may have committed while API calls ran.
    if not new_events:
        return 0
    try:
        with _flow_archive_lock(FLOWS_JSON_PATH):
            latest = load_raw_flow_history(raise_on_error=True)
            latest_ids = {_record_identity(r) for r in latest}
            appended = [r for r in new_events if _record_identity(r) not in latest_ids]
            if not appended:
                return 0
            all_records = _unique_records(latest + appended)[-10000:]
            if _persist_flows_unlocked(all_records, FLOWS_JSON_PATH, FLOWS_PARQUET_PATH):
                logger.info("Successfully appended %d new API flow events", len(appended))
                return len(appended)
    except Exception as exc:
        logger.warning("Failed to commit flow events: %s", exc)
    return 0


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

    records = _unique_records(load_raw_flow_history())
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
        if not isinstance(r, dict):
            continue
        rtype = str(r.get("type") or "UNKNOWN")
        coin = str(r.get("coin") or "UNKNOWN").upper()
        try:
            notional = float(r.get("notional_usd") or 0.0)
        except (ValueError, TypeError):
            notional = 0.0
        side = str(r.get("side") or "").upper()

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
            if v["liquidations_usd"] > 0 or v["twap_notional_usd"] > 0 or v["whale_trades_usd"] > 0 or v["imminent_liqs_usd"] > 0 or v.get("oi_surges_count", 0) > 0
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
