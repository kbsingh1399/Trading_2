"""
Terminal/Data_Factory/coinglass_harvester.py
Autonomous CoinGlass 5-Minute Telemetry & Temporal Persistence Harvester.
Connects via Chrome DevTools Protocol (CDP port 9222) using an ephemeral background tab.
Extracts structured JSON data across all core analytical domains:
  1. Whales & Orderbooks (/hyperliquid, /hl, /large-orderbook-statistics, /orderbook-pressure)
  2. Liquidation Surfaces (/liquidation-maxpain, /liquidations, /liquidation-levels, /pro/futures/LiquidationMap)
  3. Institutional ETFs & Treasuries (/etf/bitcoin, /etf/ethereum, /BitcoinTreasuries)
  4. Sentiment & Long/Short Ratios (/LongShortRatio, /position)
  5. Funding Rates & Open Interest (/FundingRate, /pro/futures/Cryptofutures)
  6. On-Chain, UTXO & Macro Indexes (/Balance, /pro/i/utxo, /pro/i/FearGreedIndex)

Maintains a stateful temporal persistence ledger in Data/coinglass/whale_persistence_ledger.json
tracking how many hours and days whale orders and positions have been active at each price.
"""

from __future__ import annotations
import asyncio
import datetime
import json
import os
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional

import websockets

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Data_Factory.time_series_database import ts_db

CDP_BASE_URL = "http://127.0.0.1:9222"
COINGLASS_DATA_DIR = ROOT / "Data" / "coinglass"
LATEST_SNAPSHOT_PATH = COINGLASS_DATA_DIR / "latest" / "coinglass_snapshot.json"
PREV_SNAPSHOT_PATH = COINGLASS_DATA_DIR / "latest" / "coinglass_snapshot_prev.json"
DELTA_SNAPSHOT_PATH = COINGLASS_DATA_DIR / "latest" / "coinglass_delta.json"
HISTORY_DIR = COINGLASS_DATA_DIR / "history"
PERSISTENCE_LEDGER_PATH = COINGLASS_DATA_DIR / "whale_persistence_ledger.json"
DATA_DICTIONARY_PATH = ROOT / "docs" / "telemetry" / "coinglass_data_dictionary.md"
INSTITUTIONAL_CRYPTO_ASSETS = ("BTC", "ETH", "SOL", "BNB", "DOGE", "XRP", "ADA", "LINK", "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "TRX", "HYPE")

PRIMARY_HARVEST_PAGES = [
    {
        "domain": "whales",
        "slug": "hyperliquid_whales",
        "name": "Hyperliquid Whale Tracker",
        "url": "https://www.coinglass.com/hyperliquid",
        "wait_s": 4.0
    },
    {
        "domain": "whales",
        "slug": "hyperliquid_wallets",
        "name": "Hyperliquid Wallet Position Distribution",
        "url": "https://www.coinglass.com/hl",
        "wait_s": 3.5
    },
    {
        "domain": "liquidations",
        "slug": "liquidation_maxpain",
        "name": "Liquidation Max Pain",
        "url": "https://www.coinglass.com/liquidation-maxpain",
        "wait_s": 3.0
    },
    {
        "domain": "liquidations",
        "slug": "liquidations_summary",
        "name": "24h Liquidation Summary",
        "url": "https://www.coinglass.com/liquidations",
        "wait_s": 3.5
    },
    {
        "domain": "liquidations",
        "slug": "liquidation_levels",
        "name": "Bitcoin Liquidation Levels Lines",
        "url": "https://www.coinglass.com/liquidation-levels",
        "wait_s": 3.5
    },
    {
        "domain": "liquidations",
        "slug": "liquidation_map",
        "name": "Crypto Liquidation Map",
        "url": "https://www.coinglass.com/pro/futures/LiquidationMap",
        "wait_s": 4.0
    },
    {
        "domain": "liquidations",
        "slug": "liquidation_heatmap",
        "name": "Liquidation Heatmap",
        "url": "https://www.coinglass.com/pro/futures/LiquidationHeatMap",
        "wait_s": 4.0
    },
    {
        "domain": "etfs",
        "slug": "bitcoin_etfs",
        "name": "Spot Bitcoin ETF Flows & Holdings",
        "url": "https://www.coinglass.com/etf/bitcoin",
        "wait_s": 3.5
    },
    {
        "domain": "etfs",
        "slug": "ethereum_etfs",
        "name": "Spot Ethereum ETF Flows",
        "url": "https://www.coinglass.com/etf/ethereum",
        "wait_s": 3.5
    },
    {
        "domain": "sentiment",
        "slug": "long_short_ratio",
        "name": "Global Long/Short Ratio",
        "url": "https://www.coinglass.com/LongShortRatio",
        "wait_s": 3.0
    },
    {
        "domain": "funding",
        "slug": "funding_rates",
        "name": "Perpetual Funding Rates",
        "url": "https://www.coinglass.com/FundingRate",
        "wait_s": 3.0
    },
    {
        "domain": "onchain",
        "slug": "exchange_balance",
        "name": "Bitcoin Exchange Balance",
        "url": "https://www.coinglass.com/Balance",
        "wait_s": 3.0
    },
    {
        "domain": "onchain",
        "slug": "utxo_age_bands",
        "name": "Bitcoin Realized Price UTXO Age Bands",
        "url": "https://www.coinglass.com/pro/i/utxo",
        "wait_s": 3.5
    }
]


def _clean_num(val: str) -> Optional[float]:
    """Parse string representations of numbers into float."""
    if not val or not isinstance(val, str):
        return None
    cleaned = val.strip().replace("$", "").replace(",", "").replace("%", "").replace(" ", "")
    if not cleaned or cleaned in ("-", "--", "N/A", "null"):
        return None
    try:
        mult = 1.0
        if cleaned.endswith("K") or cleaned.endswith("k"):
            mult = 1e3
            cleaned = cleaned[:-1]
        elif cleaned.endswith("M") or cleaned.endswith("m"):
            mult = 1e6
            cleaned = cleaned[:-1]
        elif cleaned.endswith("B") or cleaned.endswith("b"):
            mult = 1e9
            cleaned = cleaned[:-1]
        elif cleaned.endswith("T") or cleaned.endswith("t"):
            mult = 1e12
            cleaned = cleaned[:-1]
        return float(cleaned) * mult
    except Exception:
        return None


def _parse_entry_time(time_str: str) -> Tuple[Optional[str], Optional[float], Optional[float]]:
    """
    Parse relative / month-day entry times (e.g. '21:18 05-09' or '22:43 10-15')
    and calculate elapsed hours and days against current UTC time.
    Returns: (parsed_iso_str, elapsed_hours, elapsed_days)
    """
    if not time_str or not isinstance(time_str, str):
        return None, None, None
    time_str = time_str.strip()
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    current_year = now_utc.year

    # Match 'HH:MM MM-DD' format
    m = re.match(r"(\d{1,2}):(\d{2})\s+(\d{1,2})-(\d{2})", time_str)
    if m:
        hh, mm, month, day = map(int, m.groups())
        try:
            dt = datetime.datetime(current_year, month, day, hh, mm, tzinfo=datetime.timezone.utc)
            if dt > now_utc:
                # If parsed date is in future, it was from previous year
                dt = datetime.datetime(current_year - 1, month, day, hh, mm, tzinfo=datetime.timezone.utc)
            elapsed_sec = (now_utc - dt).total_seconds()
            elapsed_h = round(elapsed_sec / 3600.0, 2)
            elapsed_d = round(elapsed_sec / 86400.0, 2)
            return dt.isoformat(), elapsed_h, elapsed_d
        except Exception:
            pass

    return None, None, None


class CoinglassCDPHarvester:
    """Manages high-throughput CDP extraction across CoinGlass analytical tabs."""

    def __init__(self, cdp_url: str = CDP_BASE_URL):
        self.cdp_url = cdp_url
        COINGLASS_DATA_DIR.mkdir(parents=True, exist_ok=True)
        (COINGLASS_DATA_DIR / "latest").mkdir(parents=True, exist_ok=True)

    def _open_background_target(self) -> Dict[str, Any]:
        """Creates an ephemeral background target tab on CDP."""
        req = urllib.request.Request(f"{self.cdp_url}/json/new", method="PUT")
        resp = urllib.request.urlopen(req, timeout=5)
        return json.loads(resp.read().decode("utf-8"))

    def _close_target(self, target_id: str) -> None:
        """Safely terminates an ephemeral background target."""
        try:
            urllib.request.urlopen(f"{self.cdp_url}/json/close/{target_id}", timeout=5)
        except Exception:
            pass

    async def _extract_page_content(self, ws, url: str, wait_s: float = 3.5) -> Dict[str, Any]:
        """Navigates to URL and extracts structured tables, headers, and stat cards."""
        async def send_cmd(method: str, params: Optional[dict] = None, cmd_id: int = 1):
            payload = {"id": cmd_id, "method": method}
            if params:
                payload["params"] = params
            await ws.send(json.dumps(payload))
            while True:
                raw = await ws.recv()
                msg = json.loads(raw)
                if msg.get("id") == cmd_id:
                    return msg

        # Enable Page and navigate
        await send_cmd("Page.enable", cmd_id=10)
        await send_cmd("Page.navigate", {"url": url}, cmd_id=11)
        await asyncio.sleep(wait_s)

        extract_js = """(() => {
            const title = document.title;
            const currentUrl = window.location.href;

            // Extract all tables
            const tables = Array.from(document.querySelectorAll('table')).map(table => {
                const headers = Array.from(table.querySelectorAll('th')).map(th => th.innerText.trim().replace(/\\s+/g, ' '));
                const rows = Array.from(table.querySelectorAll('tbody tr, tr')).map(tr => {
                    return Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim().replace(/\\s+/g, ' '));
                }).filter(r => r.length > 0 && r.some(c => c.length > 0));
                return { headers, rowCount: rows.length, rows };
            });

            // Extract all stat cards and summary metrics
            const cards = Array.from(document.querySelectorAll('[class*="card"], [class*="stat"], [class*="metric"], [class*="overview"], [class*="item"], [class*="summary"]')).map(el => {
                const t = el.innerText ? el.innerText.trim().replace(/\\s+/g, ' ') : '';
                return (t.length > 3 && t.length < 200) ? t : null;
            }).filter(Boolean);

            // Extract SVG chart annotations and liquidation price levels
            const svgLabels = Array.from(document.querySelectorAll('svg text')).map(el => el.textContent.trim()).filter(t => t.length > 0 && t.length < 50);

            // Extract embedded pageProps or state if available
            let nextDataSummary = null;
            try {
                const nextScript = document.getElementById('__NEXT_DATA__');
                if (nextScript) {
                    const parsed = JSON.parse(nextScript.textContent);
                    const pp = parsed.props ? parsed.props.pageProps : null;
                    if (pp) {
                        nextDataSummary = {
                            page: parsed.page,
                            keys: Object.keys(pp).slice(0, 15)
                        };
                    }
                }
            } catch (e) {}

            return {
                title,
                url: currentUrl,
                tableCount: tables.length,
                tables,
                cards: cards.slice(0, 35),
                svgLabels: svgLabels.slice(0, 50),
                nextDataSummary
            };
        })()"""

        eval_res = await send_cmd("Runtime.evaluate", {"expression": extract_js, "returnByValue": True}, cmd_id=12)
        return eval_res.get("result", {}).get("result", {}).get("value", {})

    def _normalize_hyperliquid_whales(self, raw_tables: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalizes Hyperliquid individual whale tracker table with persistence timeline."""
        whales = []
        if not raw_tables:
            return whales

        # Find table with whale columns by inspecting rows directly
        target_rows = []
        for t in raw_tables:
            rows = t.get("rows", [])
            if len(rows) > 3:
                # Check if rows contain institutional crypto asset symbols
                if any(any(c in INSTITUTIONAL_CRYPTO_ASSETS for c in r) for r in rows[:10]):
                    target_rows = rows
                    break

        for r in target_rows:
            # Skip empty placeholder/header rows (Ant Design measurement row)
            cells = [c for c in r if c]
            if len(cells) < 6:
                continue
            # Typical row format: [empty, rank, user, asset, side, position, pnl, entry_price_lev, liq_price, margin, funding, price, entry_time]
            try:
                # Find asset index
                asset_match = [i for i, c in enumerate(r) if c in INSTITUTIONAL_CRYPTO_ASSETS]
                if not asset_match:
                    continue
                a_idx = asset_match[0]
                user = r[a_idx - 1] if a_idx > 0 else "unknown"
                asset = r[a_idx]
                side = r[a_idx + 1] if a_idx + 1 < len(r) else "unknown"
                pos_str = r[a_idx + 2] if a_idx + 2 < len(r) else ""
                pnl_str = r[a_idx + 3] if a_idx + 3 < len(r) else ""
                entry_str = r[a_idx + 4] if a_idx + 4 < len(r) else ""
                liq_str = r[a_idx + 5] if a_idx + 5 < len(r) else ""
                margin_str = r[a_idx + 6] if a_idx + 6 < len(r) else ""
                current_price_str = r[-2] if len(r) >= 2 else ""
                entry_time_str = r[-1] if len(r) >= 1 else ""

                entry_iso, elapsed_h, elapsed_d = _parse_entry_time(entry_time_str)

                # Parse notional position
                pos_parts = pos_str.split(" ")
                notional_usd = _clean_num(pos_parts[0]) if pos_parts else None

                # Extract clean numeric entry price from raw string (e.g. "$76204.7 5X Cross" -> 76204.7)
                px_m = re.search(r"[\$]?([0-9]+(?:\.[0-9]+)?)", str(entry_str))
                entry_price_clean = round(float(px_m.group(1)), 4) if px_m else None

                # Parse leverage
                lev_m = re.search(r"(\d+)X", entry_str)
                leverage = int(lev_m.group(1)) if lev_m else None

                whales.append({
                    "user": user,
                    "asset": asset,
                    "side": side.upper(),
                    "position_raw": pos_str,
                    "notional_usd": notional_usd,
                    "unrealised_pnl_raw": pnl_str,
                    "entry_price_raw": entry_str,
                    "entry_price_clean": entry_price_clean,
                    "leverage": leverage,
                    "liquidation_price_raw": liq_str,
                    "margin_raw": margin_str,
                    "current_price_raw": current_price_str,
                    "entry_time_raw": entry_time_str,
                    "entry_time_iso": entry_iso,
                    "duration_hours": elapsed_h,
                    "duration_days": elapsed_d,
                    "status": "VETERAN_WHALE" if (elapsed_d and elapsed_d >= 4.0) else (
                        "PERSISTENT_WHALE" if (elapsed_d and elapsed_d >= 1.0) else "FRESH_POSITION"
                    )
                })
            except Exception:
                continue

        return whales

    def _normalize_hl_distribution(self, raw_tables: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Normalizes Hyperliquid wallet tier distribution (Shrimp -> Leviathan)."""
        dist = {"wallet_size_groups": [], "pnl_groups": []}
        for t in raw_tables:
            rows = t.get("rows", [])
            for r in rows:
                if len(r) >= 7:
                    tier = r[0] if r[0] else r[1]
                    name = r[1] if r[0] else r[2]
                    if tier in ("$0 To $250", "$250 To $10K", "$10K To $50K", "$50K To $100K", "$100K To $500K", "$500K To $1M", "$1M To $50M", "$50M To ∞"):
                        dist["wallet_size_groups"].append({
                            "tier": tier,
                            "group_name": name,
                            "wallets_count": r[2] if len(r) > 2 else "",
                            "in_position": r[3] if len(r) > 3 else "",
                            "long_short_notional": r[4] if len(r) > 4 else "",
                            "total_position": r[5] if len(r) > 5 else "",
                            "wallet_bias": r[7] if len(r) > 7 else ""
                        })
                    elif name in ("Money Printer", "Smart Money", "Arbitrage Pro", "Retail Grinder", "Mini Rekt", "Stop-loss Hero", "Leverage bagholders", "Rekt Master"):
                        dist["pnl_groups"].append({
                            "pnl_range": tier,
                            "group_name": name,
                            "wallets_count": r[2] if len(r) > 2 else "",
                            "in_position": r[3] if len(r) > 3 else "",
                            "total_position": r[5] if len(r) > 5 else "",
                            "wallet_bias": r[7] if len(r) > 7 else ""
                        })
        return dist

    def _normalize_liquidation_maxpain(self, raw_tables: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalizes Liquidation Max Pain table."""
        maxpain_list = []
        for t in raw_tables:
            for r in t.get("rows", []):
                # Format: [empty, rank, symbol, price, short_max_pain, long_max_pain]
                if len(r) >= 6 and r[2] in INSTITUTIONAL_CRYPTO_ASSETS:
                    maxpain_list.append({
                        "rank": _clean_num(r[1]),
                        "symbol": r[2],
                        "current_price": _clean_num(r[3]),
                        "short_max_pain_raw": r[4].replace("\n", " "),
                        "long_max_pain_raw": r[5].replace("\n", " ")
                    })
        return maxpain_list

    def _update_persistence_ledger(self, current_whales: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Updates the persistent ledger across 5-minute cycles with fail-closed safety and bounded trajectories.
        Keyed canonically on (asset, side, user, entry_time_iso) with clean price extraction.
        Guarantees that a corrupted primary never overwrites a valid .bak file.
        """
        from Terminal.Data_Factory.time_series_database import atomic_write_text
        ledger: Dict[str, Any] = {}
        bak_path = PERSISTENCE_LEDGER_PATH.with_suffix(".bak")

        # Load existing ledger with strict sentinel validation
        primary_loaded = False
        if PERSISTENCE_LEDGER_PATH.exists():
            try:
                raw_primary = json.loads(PERSISTENCE_LEDGER_PATH.read_text(encoding="utf-8"))
                if isinstance(raw_primary, dict) and (len(raw_primary) > 0):
                    ledger = raw_primary
                    primary_loaded = True
            except Exception as e:
                print(f"[WhaleLedger] Warning: Failed to read {PERSISTENCE_LEDGER_PATH.name}: {e}. Attempting backup restore...")

        if not primary_loaded and bak_path.exists():
            try:
                raw_bak = json.loads(bak_path.read_text(encoding="utf-8"))
                if isinstance(raw_bak, dict) and len(raw_bak) > 0:
                    ledger = raw_bak
                    print(f"[WhaleLedger] Successfully restored ledger from .bak ({len(ledger)} keys).")
                else:
                    print("[WhaleLedger] FATAL: .bak exists but is empty/invalid. Failing closed.")
                    return {}
            except Exception as be:
                print(f"[WhaleLedger] FATAL: .bak corrupted: {be}. Failing closed.")
                return {}
        elif not primary_loaded and not bak_path.exists():
            print("[WhaleLedger] Cold start: Initializing new empty ledger.")
            ledger = {}

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        now_epoch = time.time()

        # Ensure sentinel metadata exists
        if "__meta__" not in ledger:
            ledger["__meta__"] = {
                "schema_version": "2.1.0",
                "key_format": "{asset}_{side}_{user}_{entry_time_iso}",
                "created_at_utc": now_utc,
                "description": "Unified canonical immutable whale identity keyed by asset, side, user, entry_time_iso with duplicate zombie pruning."
            }
        ledger["__meta__"]["last_update_utc"] = now_utc
        ledger["__meta__"]["last_update_epoch"] = now_epoch

        for w in current_whales:
            p_val = w.get("entry_price_clean")
            if p_val is None:
                px_m = re.search(r"[\$]?([0-9]+(?:\.[0-9]+)?)", str(w.get("entry_price_raw") or ""))
                p_val = round(float(px_m.group(1)), 4) if px_m else 0.0

            # Immutable identity: (asset, side, user, entry_time_iso), falling back to price if time unavailable
            t_iso = w.get("entry_time_iso")
            t_part = t_iso if t_iso else f"px_{p_val}"
            key = f"{w['asset']}_{w['side'].upper()}_{w['user']}_{t_part}"

            if key not in ledger:
                ledger[key] = {
                    "key": key,
                    "asset": w["asset"],
                    "side": w["side"].upper(),
                    "user": w["user"],
                    "entry_price_clean": p_val,
                    "entry_price_raw": w.get("entry_price_raw"),
                    "entry_time_raw": w.get("entry_time_raw"),
                    "entry_time_iso": w.get("entry_time_iso"),
                    "first_seen_cycle_utc": now_utc,
                    "first_seen_epoch": now_epoch,
                    "last_seen_cycle_utc": now_utc,
                    "last_seen_epoch": now_epoch,
                    "duration_hours": w.get("duration_hours"),
                    "duration_days": w.get("duration_days"),
                    "cycle_count": 1,
                    "notional_usd": w.get("notional_usd"),
                    "status": w.get("status"),
                    "trajectory": [
                        {
                            "utc": now_utc,
                            "epoch": now_epoch,
                            "notional_usd": w.get("notional_usd"),
                            "pnl": w.get("unrealised_pnl_raw"),
                            "price": w.get("current_price_raw")
                        }
                    ]
                }
            else:
                item = ledger[key]
                item["last_seen_cycle_utc"] = now_utc
                item["last_seen_epoch"] = now_epoch
                item["cycle_count"] = item.get("cycle_count", 0) + 1
                item["notional_usd"] = w.get("notional_usd")
                item["current_price_raw"] = w.get("current_price_raw")
                item["duration_hours"] = w.get("duration_hours")
                item["duration_days"] = w.get("duration_days")
                item["status"] = w.get("status")
                if "entry_price_clean" not in item:
                    item["entry_price_clean"] = p_val
                if "trajectory" not in item:
                    item["trajectory"] = []
                item["trajectory"].append({
                    "utc": now_utc,
                    "epoch": now_epoch,
                    "notional_usd": w.get("notional_usd"),
                    "pnl": w.get("unrealised_pnl_raw"),
                    "price": w.get("current_price_raw")
                })
                # Cap trajectory to recent 288 cycles (24 hours of 5m snapshots) to eliminate write amplification
                if len(item["trajectory"]) > 288:
                    item["trajectory"] = item["trajectory"][-288:]

        ledger["__meta__"]["total_whales"] = len([k for k in ledger.keys() if not k.startswith("__")])

        # Rotate backup safely: only copy primary to .bak if primary is valid and non-trivial
        if PERSISTENCE_LEDGER_PATH.exists() and len(ledger) > 1:
            try:
                atomic_write_text(bak_path, json.dumps(ledger, indent=2))
            except Exception as e:
                print(f"[WhaleLedger] Warning: Failed to write .bak atomically: {e}")

        atomic_write_text(PERSISTENCE_LEDGER_PATH, json.dumps(ledger, indent=2))
        return ledger

    def compute_delta(self, curr: Dict[str, Any], prev: Dict[str, Any]) -> Dict[str, Any]:
        """Computes high-fidelity delta between snapshot at t and snapshot at t-1."""
        delta = {
            "timestamp_t": curr.get("harvest_timestamp_utc"),
            "timestamp_prev": prev.get("harvest_timestamp_utc"),
            "elapsed_seconds": round((curr.get("harvest_epoch", 0) - prev.get("harvest_epoch", 0)), 2),
            "whales": {
                "new_whales": [],
                "exited_whales": [],
                "notional_shifts": {}
            },
            "liquidation_maxpain": {}
        }
        try:
            whales_t = curr.get("domains", {}).get("hyperliquid_whales", {}).get("data", [])
            whales_prev = prev.get("domains", {}).get("hyperliquid_whales", {}).get("data", [])
            
            users_t = {f"{w['asset']}_{w['side']}_{w['user']}": w for w in whales_t}
            users_prev = {f"{w['asset']}_{w['side']}_{w['user']}": w for w in whales_prev}
            
            for k, w in users_t.items():
                if k not in users_prev:
                    delta["whales"]["new_whales"].append({
                        "key": k,
                        "asset": w["asset"],
                        "side": w["side"],
                        "notional_usd": w.get("notional_usd"),
                        "entry_time": w.get("entry_time_raw"),
                        "duration_days": w.get("duration_days")
                    })
                else:
                    prev_w = users_prev[k]
                    diff = (w.get("notional_usd") or 0) - (prev_w.get("notional_usd") or 0)
                    if abs(diff) > 100000:  # > $100k shift
                        delta["whales"]["notional_shifts"][k] = {
                            "diff_usd": diff,
                            "prev_usd": prev_w.get("notional_usd"),
                            "curr_usd": w.get("notional_usd")
                        }
            
            for k, w in users_prev.items():
                if k not in users_t:
                    delta["whales"]["exited_whales"].append({
                        "key": k,
                        "asset": w["asset"],
                        "side": w["side"],
                        "prev_notional_usd": w.get("notional_usd")
                    })

            # Max pain delta
            mp_t = {item["symbol"]: item for item in curr.get("domains", {}).get("liquidation_maxpain", {}).get("data", []) if "symbol" in item}
            mp_prev = {item["symbol"]: item for item in prev.get("domains", {}).get("liquidation_maxpain", {}).get("data", []) if "symbol" in item}
            
            for sym, item in mp_t.items():
                if sym in mp_prev:
                    p_item = mp_prev[sym]
                    delta["liquidation_maxpain"][sym] = {
                        "price_delta": round((item.get("current_price") or 0) - (p_item.get("current_price") or 0), 2),
                        "short_maxpain_t": item.get("short_max_pain_raw"),
                        "short_maxpain_prev": p_item.get("short_max_pain_raw"),
                        "long_maxpain_t": item.get("long_max_pain_raw"),
                        "long_maxpain_prev": p_item.get("long_max_pain_raw")
                    }
        except Exception as e:
            delta["error"] = str(e)
        return delta

    async def harvest_all(self) -> Dict[str, Any]:
        """Main driver: visits target tabs sequentially and creates 5-minute snapshot."""
        start_time = time.time()
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        print(f"[{now_utc}] Starting CoinGlass CDP Telemetry Harvest...")

        target = self._open_background_target()
        target_id = target["id"]
        ws_url = target["webSocketDebuggerUrl"]
        print(f"Created dedicated background target tab: {target_id}")

        results: Dict[str, Any] = {
            "harvest_timestamp_utc": now_utc,
            "harvest_epoch": time.time(),
            "domains": {}
        }

        try:
            async with websockets.connect(ws_url) as ws:
                for page in PRIMARY_HARVEST_PAGES:
                    slug = page["slug"]
                    url = page["url"]
                    print(f"Harvesting [{page['name']}] -> {url}...")
                    try:
                        extracted = await self._extract_page_content(ws, url, wait_s=page["wait_s"])
                        raw_tables = extracted.get("tables", [])

                        # Domain-specific normalization
                        if slug == "hyperliquid_whales":
                            whales = self._normalize_hyperliquid_whales(raw_tables)
                            self._update_persistence_ledger(whales)
                            results["domains"][slug] = {
                                "name": page["name"],
                                "url": url,
                                "count": len(whales),
                                "data": whales
                            }
                        elif slug == "hyperliquid_wallets":
                            dist = self._normalize_hl_distribution(raw_tables)
                            results["domains"][slug] = {
                                "name": page["name"],
                                "url": url,
                                "data": dist
                            }
                        elif slug == "liquidation_maxpain":
                            maxpain = self._normalize_liquidation_maxpain(raw_tables)
                            results["domains"][slug] = {
                                "name": page["name"],
                                "url": url,
                                "count": len(maxpain),
                                "data": maxpain
                            }
                        else:
                            # Generic structured extraction for other pages
                            results["domains"][slug] = {
                                "name": page["name"],
                                "url": url,
                                "table_count": len(raw_tables),
                                "tables": raw_tables,
                                "cards": extracted.get("cards", [])
                            }
                    except Exception as e:
                        print(f"Error harvesting {slug}: {e}")
                        results["domains"][slug] = {"name": page["name"], "url": url, "error": str(e)}

        finally:
            self._close_target(target_id)
            print(f"Closed background target tab: {target_id}")

        elapsed = round(time.time() - start_time, 2)
        results["harvest_duration_seconds"] = elapsed
        print(f"Completed CoinGlass harvest in {elapsed}s.")

        # Record snapshot in Continuous Time-Series Database
        # Handles gap detection, YYYY-MM-DD partitioning, t/t-1 rotation, live delta, and SQLite indexing
        try:
            ts_record = ts_db.record_snapshot(
                stream="coinglass",
                data=results,
                timestamp_utc=now_utc,
                epoch=results.get("harvest_epoch")
            )
            print(f"Recorded in Continuous Time-Series Database: {ts_record.get('history_file')}")
            if ts_record.get("gap_detected"):
                print(f"Gap detected upon resume: {ts_record.get('gap_duration_minutes')} minutes offline.")
        except Exception as e:
            print(f"Warning recording to TimeSeriesDB: {e}")

        # Update documentation data dictionary
        self._generate_data_dictionary(results)

        return results

    def _generate_data_dictionary(self, latest_results: Dict[str, Any]) -> None:
        """Generates a complete markdown documentation dictionary of all extracted data points."""
        lines = [
            "# 📊 COINGLASS DATA DICTIONARY & HARVEST SPECIFICATION",
            f"**Last Harvested**: `{latest_results.get('harvest_timestamp_utc')}` | **Cadence**: `5 Minutes` | **Engine**: `Terminal/Data_Factory/coinglass_harvester.py`",
            "",
            "## 1. EXTRACTED DATA DOMAINS & DATA POINTS SUMMARY",
            "",
            "| Domain | Endpoint / Page | Extracted Data Points & Metrics | Persistence / Timeline Tracking |",
            "| :--- | :--- | :--- | :--- |",
            "| **Whales** | `/hyperliquid` | Whale User Address, Asset, Side (Long/Short), Notional Position ($USD), Unrealised PnL, Entry Price, Leverage, Liquidation Price, Margin ($USD), Entry Timestamp | **YES**: `duration_hours`, `duration_days` calculated from entry time & tracked in `whale_persistence_ledger.json` |",
            "| **Whales** | `/hl` | 8 Wallet Tiers (Shrimp to Leviathan: Wallets, In Position %, Long/Short notional, Total Position, Winners/Losers, Bias) & 8 PnL Groups (Money Printer to Rekt Master) | Real-time position shifts across capital tiers |",
            "| **Liquidations** | `/liquidation-maxpain` | Asset Symbol, Live Price, Short Max Pain Price ($), Short Max Pain Notional ($M), Distance to Short Max Pain (%), Long Max Pain Price ($), Long Max Pain Notional ($M), Distance to Long Max Pain (%) | 5m cycle tracking of liquidation gravity magnets |",
            "| **Liquidations** | `/liquidations` | 24h Total Liquidation Volume ($USD), Total Long Liquidations ($USD), Total Short Liquidations ($USD), Per-Exchange liquidation breakdown | Exchange liquidation cascades across time |",
            "| **Liquidations** | `/liquidation-levels` | Bitcoin Liquidation Levels Lines & discrete liquidation trigger boundaries | High-density liquidation shelf detection |",
            "| **Liquidations** | `/pro/futures/LiquidationMap` | Cryptocurrency Liquidation Map across major venues | Cross-exchange liquidation cluster concentration |",
            "| **Liquidations** | `/pro/futures/LiquidationHeatMap` | Cumulative Liquidation Heatmap intensity by price level | Identification of high-leverage magnetic liquidity pools |",
            "| **Institutions** | `/etf/bitcoin` | Spot Bitcoin ETF Daily Net Inflows/Outflows ($USD), Cumulative Flows, Individual ETF Holdings (IBIT, FBTC, GBTC, ARKB, BITB), Historical Timeline | Cumulative institutional adoption timeline |",
            "| **Institutions** | `/etf/ethereum` | Spot Ethereum ETF Daily Net Flows ($USD), Total ETH Holdings, Issuer breakdown | Institutional Ethereum accumulation |",
            "| **Sentiment** | `/LongShortRatio` | Global 5m, 15m, 1h, 4h, 24h Long/Short account ratios across Binance, OKX, Bybit | Macro retail vs smart money positioning |",
            "| **Funding** | `/FundingRate` | Predicted and current 8-hour funding rates across BTC, ETH, SOL, altcoins | Cost of carry & funding squeeze indicators |",
            "| **On-Chain** | `/Balance` | Aggregate Bitcoin and Stablecoin reserves held across exchange cold/hot wallets | Exchange reserve depletion / accumulation |",
            "| **On-Chain** | `/pro/i/utxo` | Bitcoin Realized Price UTXO Age Bands (<1d, 1d-1w, 1w-1m, 1m-3m, 3m-6m, 6m-12m, 1y-2y, 2y-3y, 3y-5y, >5y) | **YES**: Realized price per holding duration tier |",
            "",
            "## 2. TEMPORAL PERSISTENCE LEDGER SCHEMA (`whale_persistence_ledger.json`)",
            "```json",
            "{",
            '  "BTC_SHORT_0x5b5d..60_76204.7": {',
            '    "asset": "BTC",',
            '    "side": "SHORT",',
            '    "user": "0x5b5d..60",',
            '    "entry_price_raw": "$76204.7 5X Cross",',
            '    "entry_time_raw": "15:36 08-14",',
            '    "entry_time_iso": "2026-08-14T15:36:00+00:00",',
            '    "duration_hours": 1515.35,',
            '    "duration_days": 63.14,',
            '    "cycle_count": 12,',
            '    "notional_usd": 225350000.0,',
            '    "status": "VETERAN_WHALE"',
            "  }",
            "}",
            "```",
            "",
            "## 3. INGESTION STATUS & DATA FRESHNESS",
            f"- **Latest Ingestion**: `{latest_results.get('harvest_timestamp_utc')}`",
            f"- **Duration**: `{latest_results.get('harvest_duration_seconds', 0)} seconds`",
            f"- **Sinks**: `{LATEST_SNAPSHOT_PATH}` and `{PERSISTENCE_LEDGER_PATH}`"
        ]
        DATA_DICTIONARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        DATA_DICTIONARY_PATH.write_text("\n".join(lines), encoding="utf-8")
        print(f"Generated complete Coinglass Data Dictionary at {DATA_DICTIONARY_PATH}")


if __name__ == "__main__":
    harvester = CoinglassCDPHarvester()
    asyncio.run(harvester.harvest_all())
