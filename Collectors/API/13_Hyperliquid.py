from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ


# Pure Parquet Pipeline

import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional, Tuple


MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Terminal.Api_Client import HyperdashClient
from Terminal.Asset_Universe import COMPLETE_UNIVERSE, canonical_asset

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [13_Hyperliquid] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("13_Hyperliquid")

TARGET_SHEET_NAME = "13_Hyperliquid"
TARGET_INDEX = 21

HL_INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

TOP_WATCHLIST = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "SUI",
    "LINK", "AVAX", "NEAR", "DOT", "LTC", "BCH", "APT"
]

# -------------------------------------------------------------------------
# Table Schemas
# -------------------------------------------------------------------------
SECTION_1_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("signal_market", "Market Identifier", 16, "center"),
    ("dex", "Origin DEX", 12, "center"),
    ("mark_px", "Mark Price ($)", 16, "right"),
    ("change_24h", "24h Chg (%)", 14, "right"),
    ("volume_24h", "24h Volume (USD)", 20, "right"),
    ("open_interest", "Open Interest (Tokens)", 22, "right"),
    ("open_interest_usd", "Open Interest (USD)", 22, "right"),
    ("funding_rate", "1h Funding Rate", 16, "right"),
    ("funding_annualized", "Funding APR (%)", 16, "right"),
    ("max_leverage", "Max Lev", 10, "center"),
    ("sz_decimals", "Decimals", 10, "center"),
]

SECTION_2_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("hl_funding", "Hyperliquid 1h Rate", 18, "right"),
    ("hl_apr", "Hyperliquid APR (%)", 18, "right"),
    ("bin_funding", "Binance Pred. Rate", 18, "right"),
    ("bybit_funding", "Bybit Pred. Rate", 18, "right"),
    ("arb_spread_bps", "Funding Spread (bps)", 18, "right"),
    ("next_time_utc", "Next Funding Time (IST)", 22, "center"),
]

SECTION_3_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("best_bid", "Best Bid ($)", 16, "right"),
    ("best_ask", "Best Ask ($)", 16, "right"),
    ("spread", "Spread ($)", 14, "right"),
    ("spread_bps", "Spread (bps)", 14, "right"),
    ("bid_vol_usd", "Top 20 Bid Vol ($)", 20, "right"),
    ("ask_vol_usd", "Top 20 Ask Vol ($)", 20, "right"),
    ("bid_pct", "Bid Depth (%)", 14, "right"),
    ("ask_pct", "Ask Depth (%)", 14, "right"),
    ("imbalance_state", "Orderbook Microstructure Bias", 28, "center"),
]

SECTION_4_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("time_utc", "Trade Time (IST)", 20, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Aggressor Side", 14, "center"),
    ("price", "Execution Price ($)", 18, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("trade_id", "Transaction ID (TID)", 20, "center"),
    ("user_1", "Participant Wallet 1", 44, "left"),
    ("user_2", "Participant Wallet 2", 44, "left"),
]

SECTION_5_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("pair", "Spot Pair", 16, "center"),
    ("mark_px", "Mark Price ($)", 16, "right"),
    ("change_24h", "24h Chg (%)", 14, "right"),
    ("volume_24h", "24h Volume (USD)", 20, "right"),
    ("circulating_supply", "Circulating Supply", 22, "right"),
    ("fdv_usd", "Fully Diluted Val ($)", 22, "right"),
]


def post_hl_api(payload: dict, timeout: int = 8) -> Any:
    """Helper to query Hyperliquid L1 info API."""
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HL_INFO_URL, data=data_bytes, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def harvest_hyperliquid_data() -> Dict[str, Any]:
    """Harvests all 5 sections of native Hyperliquid L1 data."""
    t0 = time.time()
    log.info("Harvesting Hyperliquid L1 native market data...")
    client = HyperdashClient()

    # 1. Complete Perpetual Screener (All Markets)
    all_perps = client.fetch_all_assets()
    log.info(f"Fetched {len(all_perps)} perpetual markets from Hyperliquid.")

    # 2. Predicted Funding Rates
    predicted_fundings_raw = []
    try:
        predicted_fundings_raw = post_hl_api({"type": "predictedFundings"})
        log.info(f"Fetched predicted fundings for {len(predicted_fundings_raw)} markets.")
    except Exception as e:
        log.warning(f"Could not fetch predictedFundings: {e}")

    parsed_funding_cmp = []
    for item in predicted_fundings_raw:
        if not isinstance(item, list) or len(item) < 2:
            continue
        coin = item[0]
        rates_map = {}
        next_ts = None
        for ex_info in item[1]:
            if isinstance(ex_info, list) and len(ex_info) == 2:
                ex_name = ex_info[0]
                details = ex_info[1]
                if isinstance(details, dict):
                    rates_map[ex_name] = float(details.get("fundingRate", 0.0))
                    if not next_ts and details.get("nextFundingTime"):
                        next_ts = details.get("nextFundingTime")

        hl_rate = rates_map.get("HlPerp")
        bin_rate = rates_map.get("BinPerp")
        bybit_rate = rates_map.get("BybitPerp")

        if hl_rate is not None:
            hl_apr = hl_rate * 24 * 365 * 100.0
            # Arb spread in bps against Binance or Bybit
            ref_rate = bin_rate if bin_rate is not None else bybit_rate
            arb_bps = (hl_rate - ref_rate) * 10000.0 if ref_rate is not None else 0.0
            next_dt_str = datetime.datetime.fromtimestamp(next_ts / 1000.0, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M") if next_ts else "N/A"

            parsed_funding_cmp.append({
                "coin": coin,
                "hl_funding": hl_rate,
                "hl_apr": hl_apr,
                "bin_funding": bin_rate,
                "bybit_funding": bybit_rate,
                "arb_spread_bps": arb_bps,
                "next_time_utc": next_dt_str,
            })

    # Sort funding comparison by absolute arb spread
    parsed_funding_cmp.sort(key=lambda x: abs(x.get("arb_spread_bps", 0.0)), reverse=True)

    # 3. Multi-Asset L2 Orderbook Depth & Imbalance Matrix (Top 15 assets)
    l2_depth_matrix = []
    for coin in TOP_WATCHLIST:
        try:
            l2 = client.fetch_l2_book(coin)
            b_vol = l2.get("bid_volume_usd", 0.0)
            a_vol = l2.get("ask_volume_usd", 0.0)
            b_pct = l2.get("bid_pct", 50.0)

            if b_pct >= 60.0:
                imb = "HEAVY BID ACCUMULATION"
            elif b_pct <= 40.0:
                imb = "HEAVY ASK PRESSURE"
            else:
                imb = "BALANCED BOOK"

            l2_depth_matrix.append({
                "coin": coin,
                "best_bid": l2.get("best_bid"),
                "best_ask": l2.get("best_ask"),
                "spread": l2.get("spread"),
                "spread_bps": l2.get("spread_bps"),
                "bid_vol_usd": b_vol,
                "ask_vol_usd": a_vol,
                "bid_pct": b_pct,
                "ask_pct": 100.0 - b_pct,
                "imbalance_state": imb,
            })
        except Exception as e:
            log.warning(f"Could not fetch L2 book for {coin}: {e}")

    # 4. Recent Tick Trades Tape (BTC, ETH, SOL, HYPE)
    recent_tape = []
    for coin in ("BTC", "ETH", "SOL", "HYPE"):
        try:
            trades = post_hl_api({"type": "recentTrades", "coin": coin})
            for t in (trades or []):
                t_side = "BUY" if t.get("side") == "B" else "SELL"
                px = float(t.get("px", 0.0))
                sz = float(t.get("sz", 0.0))
                users = t.get("users", [])
                u1 = users[0] if len(users) > 0 else ""
                u2 = users[1] if len(users) > 1 else ""
                t_time = datetime.datetime.fromtimestamp(t.get("time", 0) / 1000.0, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

                recent_tape.append({
                    "time_utc": t_time,
                    "time_raw": t.get("time", 0),
                    "coin": coin,
                    "side": t_side,
                    "price": px,
                    "size": sz,
                    "notional_usd": px * sz,
                    "trade_id": str(t.get("tid", t.get("hash", ""))),
                    "user_1": u1,
                    "user_2": u2,
                })
        except Exception as e:
            log.warning(f"Could not fetch recent trades for {coin}: {e}")

    # Sort tape chronologically descending
    recent_tape.sort(key=lambda x: x.get("time_raw", 0), reverse=True)

    # 5. Spot Market Ecosystem Overview
    spot_markets = []
    try:
        spot_raw = post_hl_api({"type": "spotMetaAndAssetCtxs"})
        if spot_raw and len(spot_raw) == 2:
            meta_u = spot_raw[0].get("universe", [])
            ctxs = spot_raw[1]
            ctx_map = {c.get("coin"): c for c in ctxs}

            for pair_info in meta_u:
                pair_name = pair_info.get("name")
                c_data = ctx_map.get(pair_name, {})
                mark_px = float(c_data.get("markPx") or 0.0)
                if mark_px <= 0:
                    continue
                vlm = float(c_data.get("dayNtlVlm") or 0.0)
                prev_px = float(c_data.get("prevDayPx") or 0.0)
                chg = ((mark_px - prev_px) / prev_px * 100.0) if prev_px > 0 else 0.0
                circ_supply = float(c_data.get("circulatingSupply") or 0.0)
                fdv = circ_supply * mark_px if circ_supply > 0 else None

                spot_markets.append({
                    "pair": pair_name,
                    "mark_px": mark_px,
                    "change_24h": chg,
                    "volume_24h": vlm,
                    "circulating_supply": circ_supply,
                    "fdv_usd": fdv,
                })
            # Sort spot markets by 24h volume descending
            spot_markets.sort(key=lambda x: x.get("volume_24h", 0.0), reverse=True)
            log.info(f"Fetched {len(spot_markets)} active spot markets from Hyperliquid.")
    except Exception as e:
        log.warning(f"Could not fetch spot markets: {e}")

    log.info(f"Hyperliquid harvest completed in {time.time() - t0:.2f}s.")
    return {
        "perpetuals": all_perps,
        "funding_cmp": parsed_funding_cmp,
        "l2_depth": l2_depth_matrix,
        "trades_tape": recent_tape,
        "spot_markets": spot_markets,
    }


def dump_hyperliquid_to_parquet(data: dict, sheet_name: str = TARGET_SHEET_NAME) -> bool:
    rows = []
    ts_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")

    # 1. Perps markets
    for p in data.get("perps", []):
        rows.append({
            "Section": "PERP_MARKETS",
            "Asset": p.get("coin"),
            "Price": float(p.get("mark_px", 0.0)),
            "Change_24h": float(p.get("change_24h", 0.0)),
            "Volume_24h_USD": float(p.get("volume_24h", 0.0)),
            "Open_Interest_USD": float(p.get("open_interest_usd", 0.0)),
            "Funding_Rate": float(p.get("funding_rate", 0.0)),
            "Detail": f"Max Lev: {p.get('max_leverage', 0)}x",
            "Timestamp_IST": ts_ist,
        })

    # 2. Funding comparison
    for f in data.get("funding_cmp", []):
        rows.append({
            "Section": "FUNDING_ARBITRAGE",
            "Asset": f.get("coin"),
            "Price": None,
            "Change_24h": f.get("arb_spread_bps"),
            "Volume_24h_USD": None,
            "Open_Interest_USD": None,
            "Funding_Rate": f.get("hl_funding"),
            "Detail": f"HL: {f.get('hl_apr', 0.0):.2f}% APR | Next: {f.get('next_time_utc')}",
            "Timestamp_IST": ts_ist,
        })

    meta = write_parquet_feed(sheet_name, rows)
    log.info(f"Successfully dumped {len(rows)} Hyperliquid rows into Parquet feed '{sheet_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperliquid L1 Native Market Data Pure-Parquet Dumper")
    parser.add_argument("--sheet", default=TARGET_SHEET_NAME, help="Target feed name")
    args = parser.parse_args()

    t_start = time.time()
    log.info(f"Starting Hyperliquid L1 module for feed '{args.sheet}'...")
    harvest_data = harvest_hyperliquid_data()
    success = dump_hyperliquid_to_parquet(harvest_data, sheet_name=args.sheet)

    if success:
        log.info(f"Hyperliquid module completed successfully in {time.time() - t_start:.2f}s.")
        sys.exit(0)
    else:
        log.error("Hyperliquid module failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
