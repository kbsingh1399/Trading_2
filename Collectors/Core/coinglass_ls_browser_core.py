#!/usr/bin/env python3
"""
Collectors/Core/coinglass_ls_browser_core.py
============================================
High-Speed In-Memory Browser Extraction Core for Exchanges Long/Short Ratio.

Pulls authentic CoinGlass multi-exchange Long/Short ratios, taker buy/sell
volumes, and exchange-specific derivatives positioning over Edge CDP port 9222.

Coverage:
  - 18 Institutional Perpetual Assets (BTC, ETH, XRP, SOL, BNB, etc.)
  - Multi-exchange aggregated taker buy/sell volume and ratios across 15M, 1H, 4H.
  - Complete 22 ranked exchanges breakdown for BTC (Binance, OKX, Bybit, KuCoin, Gate, etc.).
  - Exchange-specific whale vs retail positioning for Binance, OKX, Bybit, and Gate.
"""

from __future__ import annotations

import asyncio
import datetime
import json
import logging
import pathlib
import sys
import urllib.request
import pandas as pd
import websockets

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DF_DIR = ROOT_DIR / "Terminal" / "Data_Factory"
if str(DF_DIR) not in sys.path:
    sys.path.insert(0, str(DF_DIR))

from parquet_feed_writer import write_parquet_feed

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [CoinGlass_LS_Core] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("CoinGlass_LS_Core")

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

try:
    from asset_registry import asset_registry
    UNIVERSE = asset_registry.get_assets_for_collector("3_Exchanges_LS_Ratio")
except Exception:
    UNIVERSE = [
        "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK",
        "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB",
        "XAUT", "PAXG"
    ]


def fmt_vol(val: float) -> str:
    """Formats numeric volume in institutional USD shorthand."""
    if val is None or val != val:
        return "-"
    abs_v = abs(val)
    if abs_v >= 1e9:
        return f"${abs_v / 1e9:.2f}B"
    elif abs_v >= 1e6:
        return f"${abs_v / 1e6:.2f}M"
    elif abs_v >= 1e3:
        return f"${abs_v / 1e3:.2f}K"
    else:
        return f"${abs_v:.2f}"


def get_coinglass_tab() -> tuple[str, str, bool]:
    """Finds or opens a CoinGlass LongShortRatio tab on Edge CDP."""
    target = "https://www.coinglass.com/LongShortRatio"
    try:
        res = urllib.request.urlopen("http://localhost:9222/json", timeout=5).read()
        tabs = json.loads(res.decode("utf-8"))
        for t in tabs:
            url = t.get("url", "").lower()
            if "longshortratio" in url:
                log.info(f"Reusing active LongShortRatio tab (ID: {t['id']})")
                return t["id"], t["webSocketDebuggerUrl"], False
    except Exception as e:
        log.warning(f"Failed to query CDP tabs: {e}")

    req = urllib.request.Request(f"http://localhost:9222/json/new?{target}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode("utf-8"))
    log.info(f"Opened dedicated ephemeral LongShortRatio tab (ID: {new_tab['id']})")
    return new_tab["id"], new_tab["webSocketDebuggerUrl"], True


def close_tab(tab_id: str):
    try:
        urllib.request.urlopen(f"http://localhost:9222/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception:
        pass


async def extract_coinglass_ls_data(tf_str: str) -> dict:
    """Extracts raw React Fiber state and active DOM table from CoinGlass."""
    tab_id, ws_url, is_ephemeral = get_coinglass_tab()
    tf_clean = tf_str.lower()

    js_code = f"""(() => {{
        const targetSymbols = new Set({json.dumps(UNIVERSE)});
        const tf = '{tf_clean}';
        
        // 1. Extract the 18 assets from React Fiber table
        let multiAssetList = [];
        const tables = Array.from(document.querySelectorAll('.ant-table'));
        for (let t of tables) {{
            for (let k in t) {{
                if (k.startsWith('__reactFiber')) {{
                    let cur = t[k];
                    while (cur) {{
                        const ds = cur.memoizedProps && (cur.memoizedProps.dataSource || cur.memoizedProps.data);
                        if (ds && Array.isArray(ds) && ds.length > 50) {{
                            const filtered = ds.filter(item => targetSymbols.has(item.symbol));
                            if (filtered.length >= 10) {{
                                multiAssetList = filtered;
                                break;
                            }}
                        }}
                        cur = cur.return;
                    }}
                }}
                if (multiAssetList.length > 0) break;
            }}
            if (multiAssetList.length > 0) break;
        }}
        
        // 2. Extract DOM table for BTC exchanges
        let btcExchanges = [];
        const box = document.querySelector('[class*="LSTableV2"]');
        if (box) {{
            const card = box.closest('.MuiCard-root') || box.parentElement;
            const lines = card.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
            const startIdx = lines.findIndex(l => l.includes('Taker Buy/Sell Volume'));
            if (startIdx !== -1) {{
                let curr = startIdx + 9;
                while (curr < lines.length) {{
                    const rank = lines[curr];
                    if (!/^\\d+$/.test(rank)) break;
                    btcExchanges.push({{
                        rank: rank,
                        exchange: lines[curr + 1],
                        longPct: lines[curr + 2],
                        shortPct: lines[curr + 3],
                        longVol: lines[curr + 5],
                        shortVol: lines[curr + 7]
                    }});
                    curr += 8;
                }}
            }}
        }}
        
        return {{
            multiAssetList: multiAssetList.map(item => ({{
                symbol: item.symbol,
                price: item.price,
                m15LongVolUsd: item.m15LongVolUsd,
                m15ShortVolUsd: item.m15ShortVolUsd,
                m15Ls: item.m15Ls,
                m15LongVolUsdR: item.m15LongVolUsdR,
                m15ShortVolUsdR: item.m15ShortVolUsdR,
                h1LongVolUsd: item.h1LongVolUsd,
                h1ShortVolUsd: item.h1ShortVolUsd,
                h1Ls: item.h1Ls,
                h1LongVolUsdR: item.h1LongVolUsdR,
                h1ShortVolUsdR: item.h1ShortVolUsdR,
                h4LongVolUsd: item.h4LongVolUsd,
                h4ShortVolUsd: item.h4ShortVolUsd,
                h4Ls: item.h4Ls,
                h4LongVolUsdR: item.h4LongVolUsdR,
                h4ShortVolUsdR: item.h4ShortVolUsdR,
                dataMap: item.dataMap || {{}}
            }})),
            btcExchanges: btcExchanges
        }};
    }})()"""

    try:
        async with websockets.connect(ws_url, max_size=25 * 1024 * 1024) as ws:
            if is_ephemeral:
                log.info("Awaiting LongShortRatio page hydration (3.5s)...")
                await asyncio.sleep(3.5)
            msg = {
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {"expression": js_code, "returnByValue": True},
            }
            await ws.send(json.dumps(msg))
            res = json.loads(await ws.recv())
            return res.get("result", {}).get("result", {}).get("value", {})
    finally:
        if is_ephemeral:
            close_tab(tab_id)


async def run_coinglass_ls_harvest(tf: str) -> bool:
    """
    Harvests authentic CoinGlass Long/Short data for a timeframe and writes Parquet.
    tf: '15m', '1h', or '4h'
    """
    tf_clean = tf.lower()
    feed_name = f"3_Exchanges_LS_Ratio_{tf_clean.upper()}"
    now_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        data = await extract_coinglass_ls_data(tf_clean)
        multi_assets = data.get("multiAssetList", [])
        btc_exchanges = data.get("btcExchanges", [])

        if not multi_assets:
            log.error(f"Failed to extract multi-asset data from CoinGlass for {tf_clean}")
            return False

        rows = []
        for item in multi_assets:
            sym = item.get("symbol")

            if tf_clean == "15m":
                l_vol = float(item.get("m15LongVolUsd") or 0.0)
                s_vol = float(item.get("m15ShortVolUsd") or 0.0)
                ls_ratio = float(item.get("m15Ls") or 1.0)
                l_pct_str = f"{float(item.get('m15LongVolUsdR') or 50.0):.2f}%"
                s_pct_str = f"{float(item.get('m15ShortVolUsdR') or 50.0):.2f}%"
            elif tf_clean == "4h":
                l_vol = float(item.get("h4LongVolUsd") or 0.0)
                s_vol = float(item.get("h4ShortVolUsd") or 0.0)
                ls_ratio = float(item.get("h4Ls") or 1.0)
                l_pct_str = f"{float(item.get('h4LongVolUsdR') or 50.0):.2f}%"
                s_pct_str = f"{float(item.get('h4ShortVolUsdR') or 50.0):.2f}%"
            else:  # 1h default
                l_vol = float(item.get("h1LongVolUsd") or 0.0)
                s_vol = float(item.get("h1ShortVolUsd") or 0.0)
                ls_ratio = float(item.get("h1Ls") or 1.0)
                l_pct_str = f"{float(item.get('h1LongVolUsdR') or 50.0):.2f}%"
                s_pct_str = f"{float(item.get('h1ShortVolUsdR') or 50.0):.2f}%"

            tot_vol = l_vol + s_vol

            # 1. Total Aggregated Row
            rows.append({
                "Asset": sym,
                "#": "Total",
                "Exchange": sym,
                "Long_%": l_pct_str,
                "Short_%": s_pct_str,
                "L_S_Ratio": f"{ls_ratio:.2f}",
                "Long_Volume": fmt_vol(l_vol),
                "Short_Volume": fmt_vol(s_vol),
                "Total_Volume": fmt_vol(tot_vol),
                "Timeframe": tf_clean,
                "Timestamp_IST": now_ist,
            })

            dmap = item.get("dataMap", {})

            # If BTC and DOM has 22 exchanges, include full exchange breakdown
            if sym == "BTC" and btc_exchanges and len(btc_exchanges) > 5:
                for ex in btc_exchanges:
                    lp = float(ex["longPct"].replace("%", "")) if "%" in ex["longPct"] else 50.0
                    sp = float(ex["shortPct"].replace("%", "")) if "%" in ex["shortPct"] else 50.0
                    r = (lp / sp) if sp > 0 else 1.0
                    
                    # Compute volume
                    l_str = ex["longVol"].replace("$", "").strip()
                    s_str = ex["shortVol"].replace("$", "").strip()
                    l_val = float(l_str.replace("M","").replace("K","").replace("B","") or 0) * (1e9 if "B" in l_str else (1e6 if "M" in l_str else (1e3 if "K" in l_str else 1.0)))
                    s_val = float(s_str.replace("M","").replace("K","").replace("B","") or 0) * (1e9 if "B" in s_str else (1e6 if "M" in s_str else (1e3 if "K" in s_str else 1.0)))
                    t_val = l_val + s_val

                    rows.append({
                        "Asset": sym,
                        "#": str(ex["rank"]),
                        "Exchange": ex["exchange"],
                        "Long_%": ex["longPct"],
                        "Short_%": ex["shortPct"],
                        "L_S_Ratio": f"{r:.2f}",
                        "Long_Volume": ex["longVol"],
                        "Short_Volume": ex["shortVol"],
                        "Total_Volume": fmt_vol(t_val) if t_val > 0 else "-",
                        "Timeframe": tf_clean,
                        "Timestamp_IST": now_ist,
                    })
            else:
                # Key exchanges: Binance, OKX, Bybit, Gate
                rank_idx = 1
                for ex_name in ["Binance", "OKX", "Bybit", "Gate"]:
                    ex_data = dmap.get(ex_name)
                    if ex_data:
                        tpl = float(ex_data.get("tpl", 50.0))
                        tps = float(ex_data.get("tps", 50.0))
                        tp_ratio = float(ex_data.get("tp", 1.0))
                        rows.append({
                            "Asset": sym,
                            "#": str(rank_idx),
                            "Exchange": ex_name,
                            "Long_%": f"{tpl:.2f}%",
                            "Short_%": f"{tps:.2f}%",
                            "L_S_Ratio": f"{tp_ratio:.2f}",
                            "Long_Volume": "-",
                            "Short_Volume": "-",
                            "Total_Volume": "-",
                            "Timeframe": tf_clean,
                            "Timestamp_IST": now_ist,
                        })
                        rank_idx += 1

                # Binance Whale Positions Row
                b_data = dmap.get("Binance", {})
                if b_data:
                    tpl = float(b_data.get("tpl", 50.0))
                    tps = float(b_data.get("tps", 50.0))
                    tp_ratio = float(b_data.get("tp", 1.0))
                    rows.append({
                        "Asset": sym,
                        "#": str(rank_idx),
                        "Exchange": "Whale Positions",
                        "Long_%": f"{tpl:.2f}%",
                        "Short_%": f"{tps:.2f}%",
                        "L_S_Ratio": f"{tp_ratio:.2f}",
                        "Long_Volume": "-",
                        "Short_Volume": "-",
                        "Total_Volume": "-",
                        "Timeframe": tf_clean,
                        "Timestamp_IST": now_ist,
                    })
                    rank_idx += 1

                    gal = float(b_data.get("gal", 50.0))
                    gas = float(b_data.get("gas", 50.0))
                    ga_ratio = float(b_data.get("ga", 1.0))
                    rows.append({
                        "Asset": sym,
                        "#": str(rank_idx),
                        "Exchange": "Global Accounts",
                        "Long_%": f"{gal:.2f}%",
                        "Short_%": f"{gas:.2f}%",
                        "L_S_Ratio": f"{ga_ratio:.2f}",
                        "Long_Volume": "-",
                        "Short_Volume": "-",
                        "Total_Volume": "-",
                        "Timeframe": tf_clean,
                        "Timestamp_IST": now_ist,
                    })

        df = pd.DataFrame(rows)
        meta = write_parquet_feed(feed_name, df)
        log.info(f"Successfully wrote {feed_name}: {meta.get('status')} ({meta.get('row_count')} rows)")
        return meta.get("status") == "PASS"

    except Exception as e:
        log.error(f"Error harvesting CoinGlass LS data for {tf_clean}: {e}", exc_info=True)
        return False
