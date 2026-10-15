"""
Terminal/Data_Factory/arkham_intelligence_harvester.py
Comprehensive Institutional On-Chain Intelligence Harvester for Arkham (arkm.com via Chrome CDP).

Extracts MAXIMUM institutional data points:
1. Trending Institutional Entities (Holdings, 24h change, largest asset, wallet count)
2. Live On-Chain Transfer Stream (From, To, Token, Amount, USD, Entity deanonymization)
3. Quantitative Flow Classification (Exchange Inflows, Outflows, Market Maker Flow, DEX Arbs)
4. Per-Asset Flow Attribution (BTC, ETH, SOL, Stablecoins)
5. Dumps directly into docs/telemetry/live_snapshot_latest.json & Data/arkham_live_intelligence.json
"""

import asyncio
import websockets
import json
import urllib.request
import pathlib
import datetime
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
OUTPUT_PATH = DATA_DIR / "arkham_live_intelligence.json"
DATA_DIR.mkdir(parents=True, exist_ok=True)

KNOWN_EXCHANGES = {
    "binance": "Binance",
    "okx": "OKX",
    "bybit": "Bybit",
    "coinbase": "Coinbase",
    "kraken": "Kraken",
    "deribit": "Deribit",
    "bitfinex": "Bitfinex",
    "htx": "HTX",
    "gate.io": "Gate.io",
    "mexc": "MEXC",
    "kucoin": "KuCoin",
    "upbit": "Upbit",
    "bithumb": "Bithumb"
}

KNOWN_MARKET_MAKERS = {
    "wintermute": "Wintermute",
    "jump": "Jump Trading",
    "cumberland": "Cumberland",
    "gsr": "GSR Markets",
    "amber": "Amber Group",
    "dwf labs": "DWF Labs",
    "falconx": "FalconX",
    "galaxy": "Galaxy Digital"
}

KNOWN_PROTOCOLS = {
    "uniswap": "Uniswap",
    "curve": "Curve",
    "aave": "Aave",
    "maker": "MakerDAO",
    "lido": "Lido",
    "polymarket": "Polymarket",
    "drift": "Drift Protocol",
    "kamino": "Kamino Finance"
}

async def harvest_arkham_dom(refresh: bool = True) -> dict:
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read())
    except Exception as e:
        print(f"[ERROR] Could not query CDP on port 9222: {e}")
        return {}

    ws_url = None
    for t in tabs:
        if "arkm.com" in t.get("url", "") and t.get("type") == "page":
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("[WARNING] Active Arkham tab not found on port 9222.")
        return {}

    if refresh:
        try:
            print("[*] Refreshing Arkham tab via CDP to ensure streaming feed is active and not stale...")
            async with websockets.connect(ws_url, max_size=10*1024*1024, open_timeout=5) as ws_reload:
                await ws_reload.send(json.dumps({"id": 9999, "method": "Page.reload"}))
                try:
                    await asyncio.wait_for(ws_reload.recv(), timeout=2.0)
                except Exception:
                    pass
            await asyncio.sleep(6.5)
        except Exception as e:
            print(f"[WARNING] Error reloading Arkham tab: {e}")

    try:
        async with websockets.connect(ws_url, max_size=30*1024*1024, open_timeout=8) as ws:
            js = """
            (() => {
                const doc = window.top.document;
                const fullText = doc.body.innerText;
                
                // 1. Extract Trending Entities from DOM links
                const entityLinks = Array.from(doc.querySelectorAll('a[href*="/explorer/entity/"]'));
                const entities = [];
                const seenEntities = new Set();
                
                for (const a of entityLinks) {
                    const lines = a.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    if (lines.length >= 2 && !seenEntities.has(lines[0])) {
                        seenEntities.add(lines[0]);
                        let holdingsUsd = '';
                        let changePct = '';
                        let largestHolding = '';
                        let activeWallets = '';
                        
                        for (let i = 0; i < lines.length; i++) {
                            if (lines[i].startsWith('$') && !holdingsUsd) holdingsUsd = lines[i];
                            if (lines[i].includes('%') && !changePct) changePct = lines[i];
                            if (lines[i] === 'LARGEST HOLDING' && i + 1 < lines.length) {
                                largestHolding = lines[i+1] + (i+2 < lines.length && lines[i+2].startsWith('(') ? ' ' + lines[i+2] : '');
                            }
                            if (lines[i] === 'ACTIVE WALLETS' && i + 1 < lines.length) {
                                activeWallets = lines[i+1];
                            }
                        }
                        
                        entities.push({
                            name: lines[0],
                            holdings_usd: holdingsUsd,
                            change_pct_24h: changePct,
                            largest_holding: largestHolding,
                            active_wallets: activeWallets,
                            entity_url: a.href
                        });
                    }
                }
                
                // 2. Extract Transfer Rows from DOM
                const txLinks = Array.from(doc.querySelectorAll('a[href*="/explorer/tx/"]'));
                const txs = [];
                const seenTx = new Set();
                
                for (const a of txLinks) {
                    let row = a.closest('tr') || a.closest('div[role="row"]') || a.parentElement;
                    while (row && row.children.length < 3 && row.parentElement && row.parentElement !== doc.body) {
                        row = row.parentElement;
                    }
                    if (row && !seenTx.has(row)) {
                        seenTx.add(row);
                        const rowLines = row.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                        const links = Array.from(row.querySelectorAll('a')).map(l => ({ text: l.innerText.trim(), href: l.href }));
                        
                        txs.push({
                            tx_hash: a.href.split('/').pop(),
                            tx_url: a.href,
                            raw_lines: rowLines,
                            raw_text: rowLines.join(' | '),
                            links: links
                        });
                    }
                }
                
                return {
                    url: window.top.location.href,
                    title: doc.title,
                    full_text: fullText,
                    entities: entities,
                    transfers: txs
                };
            })()
            """
            msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}
            await ws.send(json.dumps(msg))
            res = json.loads(await ws.recv())
            return res.get("result", {}).get("result", {}).get("value", {})
    except Exception as e:
        print(f"[ERROR] CDP query failed: {e}")
        return {}

def classify_party(name_or_text: str) -> tuple:
    low = name_or_text.lower()
    for k, name in KNOWN_EXCHANGES.items():
        if k in low:
            return name, "EXCHANGE"
    for k, name in KNOWN_MARKET_MAKERS.items():
        if k in low:
            return name, "MARKET_MAKER"
    for k, name in KNOWN_PROTOCOLS.items():
        if k in low:
            return name, "DEX_PROTOCOL"
    if "whale" in low or "exploiter" in low or "treasury" in low:
        return name_or_text, "WHALE_TREASURY"
    return name_or_text, "WALLET"

def parse_arkham_data(raw: dict) -> dict:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entities = raw.get("entities", [])
    raw_txs = raw.get("transfers", [])
    
    parsed_transfers = []
    exchange_inflows = []
    exchange_outflows = []
    market_maker_flows = []
    whale_alerts = []
    
    asset_flows = {
        "BTC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0},
        "ETH": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0},
        "SOL": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0},
        "USDT": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0},
        "USDC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0},
        "OTHER": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0}
    }
    
    for tx in raw_txs:
        lines = tx.get("raw_lines", [])
        if len(lines) < 3:
            continue
            
        time_str = lines[0] if lines else "Recent"
        text = tx.get("raw_text", "")
        
        # Extract USD value
        usd_val = 0.0
        token_sym = "UNKNOWN"
        amount_val = 0.0
        
        # Look for $ amount
        for l in lines:
            if l.startswith("$"):
                try:
                    usd_val = float(re.sub(r"[^\d.]", "", l))
                except: pass
                
        # Look for token symbol and amount
        for i, l in enumerate(lines):
            for t_candidate in ["BTC", "ETH", "SOL", "USDT", "USDC", "WBTC", "WETH", "PUSD", "FDUSD", "DAI"]:
                if l.upper() == t_candidate or f" {t_candidate}" in l.upper():
                    token_sym = t_candidate
                    if i > 0:
                        try:
                            amount_val = float(re.sub(r"[^\d.]", "", lines[i-1]))
                        except: pass
                    break
            if token_sym != "UNKNOWN":
                break
                
        # Parse from & to
        from_entity, from_type = "Unknown", "WALLET"
        to_entity, to_type = "Unknown", "WALLET"
        
        links = tx.get("links", [])
        named_links = [l.get("text") for l in links if l.get("text") and len(l.get("text")) > 2]
        
        if len(named_links) >= 2:
            from_entity, from_type = classify_party(named_links[0])
            to_entity, to_type = classify_party(named_links[1])
        elif len(lines) >= 4:
            from_entity, from_type = classify_party(lines[1])
            to_entity, to_type = classify_party(lines[2])
            
        # Classify flow dynamic
        flow_tag = "INTERNAL_TRANSFER"
        if to_type == "EXCHANGE" and from_type != "EXCHANGE":
            flow_tag = "EXCHANGE_INFLOW (POTENTIAL_SELL_PRESSURE)"
            exchange_inflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            target_asset = token_sym if token_sym in asset_flows else "OTHER"
            asset_flows[target_asset]["inflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "EXCHANGE" and to_type != "EXCHANGE":
            flow_tag = "EXCHANGE_OUTFLOW (ACCUMULATION_COLD_STORAGE)"
            exchange_outflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            target_asset = token_sym if token_sym in asset_flows else "OTHER"
            asset_flows[target_asset]["outflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "MARKET_MAKER" or to_type == "MARKET_MAKER":
            flow_tag = "MARKET_MAKER_ARBITRAGE_PROVISION"
            market_maker_flows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            
        if usd_val >= 50000:
            whale_alerts.append({
                "tx_hash": tx.get("tx_hash"),
                "time": time_str,
                "from": from_entity,
                "to": to_entity,
                "usd_value": usd_val,
                "token": token_sym,
                "flow_tag": flow_tag
            })
            
        parsed_transfers.append({
            "time": time_str,
            "tx_hash": tx.get("tx_hash"),
            "tx_url": tx.get("tx_url"),
            "from_entity": from_entity,
            "from_type": from_type,
            "to_entity": to_entity,
            "to_type": to_type,
            "token": token_sym,
            "amount": amount_val,
            "usd_value": usd_val,
            "flow_classification": flow_tag
        })

    # Global sentiment determination
    total_inflow_usd = sum(x["usd"] for x in exchange_inflows)
    total_outflow_usd = sum(x["usd"] for x in exchange_outflows)
    net_flow_usd = total_outflow_usd - total_inflow_usd
    
    if len(exchange_outflows) > len(exchange_inflows) and net_flow_usd >= 0:
        sentiment = "NET_ACCUMULATION (BULLISH_FLOW)"
    elif len(exchange_inflows) > len(exchange_outflows) and net_flow_usd <= 0:
        sentiment = "NET_DISTRIBUTION (BEARISH_FLOW)"
    else:
        sentiment = "NEUTRAL_BALANCED_FLOW"
        
    structured = {
        "as_of_utc": now_utc,
        "source": "Arkham Intelligence Live Harvester (arkm.com via Chrome CDP)",
        "feed_status": "STREAMING_ACTIVE",
        "market_flow_sentiment": sentiment,
        "aggregate_metrics": {
            "total_transfers_monitored": len(parsed_transfers),
            "exchange_inflow_events": len(exchange_inflows),
            "exchange_outflow_events": len(exchange_outflows),
            "market_maker_events": len(market_maker_flows),
            "large_whale_alerts_count": len(whale_alerts),
            "total_inflow_volume_usd": total_inflow_usd,
            "total_outflow_volume_usd": total_outflow_usd,
            "net_flow_usd": net_flow_usd
        },
        "asset_breakdown": asset_flows,
        "trending_institutional_entities": entities,
        "whale_alerts": whale_alerts[:10],
        "recent_classified_transfers": parsed_transfers[:20]
    }
    
    # 1. Save to Data/arkham_live_intelligence.json
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2)
    print(f"[+] Saved complete Arkham intelligence to {OUTPUT_PATH}")
    
    # 2. Directly inject into docs/telemetry/live_snapshot_latest.json
    if SNAPSHOT_PATH.exists():
        try:
            with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
                snap = json.load(f)
                
            # Top-level comprehensive key
            snap["onchain_arkham_intelligence"] = structured
            
            # Per-asset attribution into assets_matrix_24
            matrix = snap.get("assets_matrix_24", {})
            for sym, data in matrix.items():
                if sym in asset_flows:
                    data["arkham_onchain"] = {
                        "inflow_usd": asset_flows[sym]["inflow_usd"],
                        "outflow_usd": asset_flows[sym]["outflow_usd"],
                        "tx_count": asset_flows[sym]["tx_count"],
                        "sentiment": "ACCUMULATION" if asset_flows[sym]["outflow_usd"] > asset_flows[sym]["inflow_usd"] else ("DISTRIBUTION" if asset_flows[sym]["inflow_usd"] > asset_flows[sym]["outflow_usd"] else "NEUTRAL")
                    }
                    
            with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
                json.dump(snap, f, indent=2)
            print(f"[+] Successfully injected complete Arkham feed into {SNAPSHOT_PATH.name}")
        except Exception as e:
            print(f"[ERROR] Failed to inject into telemetry snapshot: {e}")
            
    return structured

def run():
    print("[*] Harvesting Arkham On-Chain Intelligence via CDP...")
    raw = asyncio.run(harvest_arkham_dom())
    if raw:
        data = parse_arkham_data(raw)
        print("\n=== ARKHAM HARVEST SUMMARY ===")
        print(f"Sentiment: {data['market_flow_sentiment']}")
        print(f"Entities: {len(data['trending_institutional_entities'])}")
        print(f"Transfers: {data['aggregate_metrics']['total_transfers_monitored']}")
        print(f"Inflows: {data['aggregate_metrics']['exchange_inflow_events']} | Outflows: {data['aggregate_metrics']['exchange_outflow_events']}")
        print(f"Whale Alerts: {len(data['whale_alerts'])}")
    else:
        print("[!] Failed to harvest Arkham data.")

if __name__ == "__main__":
    run()
