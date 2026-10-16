"""
Terminal/Data_Factory/arkham_intelligence_harvester.py
Comprehensive Institutional On-Chain Intelligence Harvester for Arkham (arkm.com via Chrome CDP).

Upgraded Architecture:
1. Active Tab Streaming: Live On-Chain Transfer Stream (From, To, Token, Amount, USD, Entity deanonymization)
2. Quantitative Flow Classification: Exchange Inflows, Outflows, Market Maker Flow, DEX Arbs, Whale Alerts >= $50K
3. Trending Institutional Carousel: Portfolios with highest momentum & capital rotation
4. Deep Institutional Entity Registry: Scrapes Top-Tier Funds, Market Makers, Governments & Treasuries
   (BlackRock, Jump Trading, Wintermute, Fidelity, Grayscale, US Government, Binance, FalconX, Cumberland, MicroStrategy)
5. Multi-Asset Flow Attribution: BTC, ETH, SOL, USDT, USDC
6. Direct Injection: docs/telemetry/live_snapshot_latest.json & Data/arkham_institutional_registry.json
"""

import asyncio
import websockets
import json
import urllib.request
import pathlib
import datetime
import re
import sys
import logging

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
OUTPUT_PATH = DATA_DIR / "arkham_live_intelligence.json"
REGISTRY_PATH = DATA_DIR / "arkham_institutional_registry.json"
DATA_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("ArkhamHarvester")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

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
    "kamino": "Kamino Finance",
    "aerodrome": "Aerodrome Finance"
}

# Institutional Roster for Deep Ingestion
INSTITUTIONAL_ROSTER = [
    {"slug": "blackrock", "name": "BlackRock", "category": "ETF_ISSUER_ASSET_MANAGER"},
    {"slug": "jump-trading", "name": "Jump Crypto", "category": "MARKET_MAKER_HFT"},
    {"slug": "wintermute", "name": "Wintermute", "category": "MARKET_MAKER_ALGO"},
    {"slug": "usg", "name": "U.S. Government", "category": "SOVEREIGN_TREASURY"},
    {"slug": "fidelity", "name": "Fidelity Investments", "category": "ETF_ISSUER_ASSET_MANAGER"},
    {"slug": "grayscale", "name": "Grayscale Investments", "category": "ASSET_MANAGER_TRUSTS"},
    {"slug": "binance", "name": "Binance Hot/Cold Reserves", "category": "CENTRALIZED_EXCHANGE"},
    {"slug": "falconx", "name": "FalconX", "category": "PRIME_BROKERAGE_EXECUTION"},
    {"slug": "cumberland", "name": "Cumberland DRW", "category": "OTC_LIQUIDITY_DESK"},
    {"slug": "microstrategy", "name": "MicroStrategy", "category": "CORPORATE_TREASURY"}
]

def parse_financial_number(s: str) -> float:
    """Accurately parse numbers with K, M, B, T abbreviations into raw float values."""
    if not s:
        return 0.0
    s = s.strip().replace(",", "")
    mult = 1.0
    if s.endswith("K") or s.endswith("k"):
        mult = 1_000.0
        s = s[:-1]
    elif s.endswith("M") or s.endswith("m"):
        mult = 1_000_000.0
        s = s[:-1]
    elif s.endswith("B") or s.endswith("b"):
        mult = 1_000_000_000.0
        s = s[:-1]
    elif s.endswith("T") or s.endswith("t"):
        mult = 1_000_000_000_000.0
        s = s[:-1]
    clean = re.sub(r"[^\d.]", "", s)
    try:
        return float(clean) * mult
    except Exception:
        return 0.0

async def harvest_arkham_dom(target_min_usd: int = 50000) -> dict:
    """Connect to live Arkham tab via Chrome CDP, ensure >= $50K filter is active, and harvest data."""
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read())
    except Exception as e:
        logger.error("Could not query CDP on port 9222: %s", e)
        return {}

    ws_url = None
    for t in tabs:
        if "arkm.com" in t.get("url", "") and t.get("type") == "page":
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        logger.warning("Active Arkham tab not found on port 9222.")
        return {}

    try:
        async with websockets.connect(ws_url, max_size=30*1024*1024, open_timeout=8) as ws:
            # Step 1: Ensure USD >= $50K filter is applied
            js_filter = f"""
            (() => {{
                const chip = document.querySelector('span[data-filter-chip-type="usd"]');
                const chipText = chip ? chip.innerText : '';
                
                // If chip already has $50K or more, we are good
                if (chipText.includes('50K') || chipText.includes('100K')) {{
                    return {{ filter_status: 'ALREADY_ACTIVE', chip: chipText }};
                }}
                
                // Otherwise, open popover and set to target_min_usd
                const body = chip ? (chip.querySelector('[data-slot="body"]') || chip) : null;
                if (!body) return {{ filter_status: 'CHIP_NOT_FOUND' }};
                body.click();
                
                const minInput = document.querySelector('input[placeholder="Minimum"]');
                if (minInput) {{
                    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    setter.call(minInput, '{target_min_usd}');
                    minInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    minInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    
                    const applyBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Apply');
                    if (applyBtn) {{
                        applyBtn.click();
                        return {{ filter_status: 'APPLIED_NEW', chip: chipText }};
                    }}
                }}
                return {{ filter_status: 'CLICKED_AWAITING_INPUT' }};
            }})()
            """
            msg_filter = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_filter, "returnByValue": True}}
            await ws.send(json.dumps(msg_filter))
            res_filter = json.loads(await ws.recv())
            filter_res = res_filter.get("result", {}).get("result", {}).get("value", {})
            if filter_res.get("filter_status") == "APPLIED_NEW":
                logger.info("Applied new USD >= $%d filter on Arkham tab", target_min_usd)
                await asyncio.sleep(2.0)

            # Step 2: Harvest DOM elements (Entities, Rows, Bitcoin Card)
            js_harvest = """
            (() => {
                const doc = window.top.document;
                
                // 1. Trending Entities
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
                
                // 2. Transfer Rows
                const rows = Array.from(doc.querySelectorAll('div[class*="group/row"]'));
                const txs = [];
                for (const r of rows) {
                    const lines = r.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    const links = Array.from(r.querySelectorAll('a')).map(l => ({ text: l.innerText.trim(), href: l.href }));
                    const txLink = links.find(l => l.href.includes('/explorer/tx/'));
                    txs.push({
                        tx_hash: txLink ? txLink.href.split('/').pop() : '',
                        tx_url: txLink ? txLink.href : '',
                        raw_lines: lines,
                        raw_text: lines.join(' | '),
                        links: links
                    });
                }
                
                // 3. Bitcoin Explorer Widget
                let btcWidget = null;
                const btcLink = doc.querySelector('a[href*="/explorer/token/bitcoin"]');
                if (btcLink) {
                    const btcLines = btcLink.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    btcWidget = { raw_lines: btcLines };
                }
                
                return {
                    url: window.top.location.href,
                    title: doc.title,
                    filter_chip: doc.querySelector('span[data-filter-chip-type="usd"]')?.innerText.replace(/\\n/g, ' ') || '',
                    entities: entities,
                    transfers: txs,
                    btc_widget: btcWidget
                };
            })()
            """
            msg_harvest = {"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_harvest, "returnByValue": True}}
            await ws.send(json.dumps(msg_harvest))
            res_harvest = json.loads(await ws.recv())
            return res_harvest.get("result", {}).get("result", {}).get("value", {})
    except Exception as e:
        logger.error("CDP query failed: %s", e)
        return {}

async def harvest_single_entity_cdp(slug: str) -> dict:
    """Open headless background tab, extract complete portfolio data, and close tab."""
    try:
        url = f"https://arkm.com/explorer/entity/{slug}"
        req = urllib.request.Request(f"http://127.0.0.1:9222/json/new?{url}", method="PUT")
        tab = json.loads(urllib.request.urlopen(req, timeout=5).read())
        tab_id = tab["id"]
        ws_url = tab["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url, max_size=30*1024*1024, open_timeout=8) as ws:
            # wait 4.0s for Next.js hydration
            await asyncio.sleep(4.0)
            js = """(() => {
                const text = document.body.innerText;
                const lines = text.split('\\n').map(l => l.trim()).filter(Boolean);
                
                let entityName = document.title.split('|')[0].trim();
                let addressCount = '';
                let totalBalance = '';
                let change24h = '';
                
                for (let i = 0; i < lines.length; i++) {
                    if (lines[i].includes('Addresses') && !addressCount) {
                        addressCount = lines[i];
                        for (let j = Math.max(0, i - 3); j < Math.min(lines.length, i + 5); j++) {
                            if (lines[j].startsWith('$') && lines[j].length > 5 && !totalBalance) {
                                totalBalance = lines[j];
                                if (j + 1 < lines.length && lines[j+1].includes('%')) {
                                    change24h = lines[j+1];
                                }
                            }
                        }
                    }
                }
                
                const holdings = [];
                const commonTokens = ['BTC', 'ETH', 'SOL', 'USDT', 'USDC', 'BNB', 'XRP', 'DOGE', 'AVAX', 'LINK', 'WBTC', 'CBBTC', 'SUI', 'NEAR'];
                
                for (let i = 0; i < lines.length; i++) {
                    if (commonTokens.includes(lines[i])) {
                        const sym = lines[i];
                        let price = '';
                        let amount = '';
                        let posValue = '';
                        let valChange = '';
                        
                        for (let j = i + 1; j < Math.min(lines.length, i + 9); j++) {
                            const l = lines[j];
                            if (l.startsWith('$') && !price) {
                                price = l;
                            } else if (l.endsWith(sym) && !amount) {
                                amount = l;
                            } else if (l.startsWith('$') && price && !posValue) {
                                posValue = l;
                                if (j + 1 < lines.length && lines[j+1].includes('%')) {
                                    valChange = lines[j+1];
                                }
                            }
                        }
                        if (posValue && !holdings.some(h => h.symbol === sym)) {
                            holdings.push({
                                symbol: sym,
                                price: price,
                                amount: amount,
                                value_usd: posValue,
                                change_24h: valChange
                            });
                        }
                    }
                }
                
                return {
                    slug: window.location.pathname.split('/').pop(),
                    entity_name: entityName,
                    address_count: addressCount,
                    total_portfolio_usd: totalBalance,
                    portfolio_change_24h: change24h,
                    holdings_breakdown: holdings
                };
            })()"""
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            val = res.get("result", {}).get("result", {}).get("value", {})
            
        urllib.request.urlopen(f"http://127.0.0.1:9222/json/close/{tab_id}", timeout=5)
        return val
    except Exception as e:
        logger.error("Failed harvesting entity %s: %s", slug, e)
        return {}

async def harvest_institutional_deep_registry(priority_count: int = 3) -> dict:
    """Cycle through institutional roster and update the institutional registry cache."""
    registry = {}
    if REGISTRY_PATH.exists():
        try:
            with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception:
            registry = {}
            
    # Harvest top priority entities in this pass
    for item in INSTITUTIONAL_ROSTER[:priority_count]:
        slug = item["slug"]
        logger.info("Harvesting deep institutional profile for %s (%s)...", item["name"], slug)
        data = await harvest_single_entity_cdp(slug)
        if data and data.get("total_portfolio_usd"):
            data["category"] = item["category"]
            data["last_updated_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            registry[slug] = data
            logger.info("-> %s: %s (%s) | Wallets: %s", item["name"], data.get("total_portfolio_usd"), data.get("portfolio_change_24h"), data.get("address_count"))
            
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
        
    return registry

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
    if "whale" in low or "exploiter" in low or "treasury" in low or "government" in low:
        return name_or_text, "WHALE_TREASURY"
    return name_or_text, "WALLET"

def parse_arkham_data(raw: dict, institutional_registry: dict = None) -> dict:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entities = raw.get("entities", [])
    raw_txs = raw.get("transfers", [])
    btc_widget = raw.get("btc_widget")
    
    parsed_transfers = []
    exchange_inflows = []
    exchange_outflows = []
    market_maker_flows = []
    whale_alerts = []
    
    asset_flows = {
        "BTC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "ETH": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "SOL": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "USDT": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "USDC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "OTHER": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0}
    }
    
    for tx in raw_txs:
        lines = tx.get("raw_lines", [])
        if len(lines) < 3:
            continue
            
        time_str = lines[0] if lines else "Recent"
        
        # Extract USD value using robust financial multiplier parser
        usd_val = 0.0
        token_sym = "UNKNOWN"
        amount_val = 0.0
        
        for l in lines:
            if l.startswith("$"):
                usd_val = parse_financial_number(l)
                
        for i, l in enumerate(lines):
            cand = l.upper().strip()
            for t_candidate in ["BTC", "CBBTC", "WBTC", "ETH", "WETH", "SOL", "USDT", "USDC", "FDUSD", "DAI", "AERO", "MORPHO", "SPY"]:
                if cand == t_candidate or f" {t_candidate}" in cand:
                    token_sym = t_candidate
                    if i > 0:
                        amount_val = parse_financial_number(lines[i-1])
                    break
            if token_sym != "UNKNOWN":
                break
                
        target_asset = "OTHER"
        if token_sym in ["BTC", "CBBTC", "WBTC"]:
            target_asset = "BTC"
        elif token_sym in ["ETH", "WETH"]:
            target_asset = "ETH"
        elif token_sym == "SOL":
            target_asset = "SOL"
        elif token_sym == "USDT":
            target_asset = "USDT"
        elif token_sym in ["USDC", "FDUSD", "DAI"]:
            target_asset = "USDC"
            
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
            
        flow_tag = "INTERNAL_TRANSFER"
        if to_type == "EXCHANGE" and from_type != "EXCHANGE":
            flow_tag = "EXCHANGE_INFLOW (POTENTIAL_SELL_PRESSURE)"
            exchange_inflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            asset_flows[target_asset]["inflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "EXCHANGE" and to_type != "EXCHANGE":
            flow_tag = "EXCHANGE_OUTFLOW (ACCUMULATION_COLD_STORAGE)"
            exchange_outflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            asset_flows[target_asset]["outflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "MARKET_MAKER" or to_type == "MARKET_MAKER":
            flow_tag = "MARKET_MAKER_ARBITRAGE_PROVISION"
            market_maker_flows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            
        if usd_val >= 50000:
            asset_flows[target_asset]["whale_txs"] += 1
            whale_alerts.append({
                "tx_hash": tx.get("tx_hash"),
                "time": time_str,
                "from": from_entity,
                "to": to_entity,
                "usd_value": usd_val,
                "token": token_sym,
                "asset_bucket": target_asset,
                "flow_tag": flow_tag
            })
            
        parsed_transfers.append({
            "time": time_str,
            "tx_hash": tx.get("tx_hash"),
            "from_entity": from_entity,
            "from_type": from_type,
            "to_entity": to_entity,
            "to_type": to_type,
            "token": token_sym,
            "amount": amount_val,
            "usd_value": usd_val,
            "flow_classification": flow_tag
        })

    total_inflow_usd = sum(x["usd"] for x in exchange_inflows)
    total_outflow_usd = sum(x["usd"] for x in exchange_outflows)
    net_flow_usd = total_outflow_usd - total_inflow_usd
    total_observed_volume = sum(p["usd_value"] for p in parsed_transfers)
    
    if len(exchange_outflows) > len(exchange_inflows) and net_flow_usd >= 0:
        sentiment = "NET_ACCUMULATION (BULLISH_FLOW)"
    elif len(exchange_inflows) > len(exchange_outflows) and net_flow_usd <= 0:
        sentiment = "NET_DISTRIBUTION (BEARISH_FLOW)"
    else:
        sentiment = "NEUTRAL_BALANCED_FLOW"
        
    btc_macro = {}
    if btc_widget and "raw_lines" in btc_widget:
        bl = btc_widget["raw_lines"]
        for i, l in enumerate(bl):
            if l.startswith("$") and "price" not in btc_macro:
                btc_macro["price_usd"] = parse_financial_number(l)
            if l == "24H VOLUME" and i + 1 < len(bl):
                btc_macro["volume_24h_usd"] = parse_financial_number(bl[i+1])
            if l == "MARKET CAP" and i + 1 < len(bl):
                btc_macro["market_cap_usd"] = parse_financial_number(bl[i+1])
            if l == "24H" and i + 1 < len(bl):
                btc_macro["change_24h_pct"] = bl[i+1]
            if l == "7d" and i + 1 < len(bl):
                btc_macro["change_7d_pct"] = bl[i+1]
            if l == "30D" and i + 1 < len(bl):
                btc_macro["change_30d_pct"] = bl[i+1]
                
    structured = {
        "as_of_utc": now_utc,
        "source": "Arkham Intelligence Upgraded Harvester (arkm.com via Chrome CDP)",
        "filter_applied": raw.get("filter_chip", "USD >= $50K"),
        "feed_status": "STREAMING_ACTIVE",
        "market_flow_sentiment": sentiment,
        "aggregate_metrics": {
            "total_transfers_monitored": len(parsed_transfers),
            "total_observed_volume_usd": total_observed_volume,
            "exchange_inflow_events": len(exchange_inflows),
            "exchange_outflow_events": len(exchange_outflows),
            "market_maker_events": len(market_maker_flows),
            "large_whale_alerts_count": len(whale_alerts),
            "total_inflow_volume_usd": total_inflow_usd,
            "total_outflow_volume_usd": total_outflow_usd,
            "net_flow_usd": net_flow_usd
        },
        "bitcoin_macro_explorer": btc_macro,
        "asset_breakdown": asset_flows,
        "trending_institutional_entities": entities,
        "institutional_entities_deep": institutional_registry or {},
        "whale_alerts": whale_alerts[:15],
        "recent_classified_transfers": parsed_transfers[:25]
    }
    
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2)
    logger.info("Saved complete Arkham intelligence to %s", OUTPUT_PATH)
    
    if SNAPSHOT_PATH.exists():
        try:
            with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
                snap = json.load(f)
                
            snap["onchain_arkham_intelligence"] = structured
            
            matrix = snap.get("assets_matrix_24", {})
            for sym, data in matrix.items():
                target_key = "OTHER"
                if "BTC" in sym:
                    target_key = "BTC"
                elif "ETH" in sym:
                    target_key = "ETH"
                elif "SOL" in sym:
                    target_key = "SOL"
                
                if target_key in asset_flows:
                    flow_info = asset_flows[target_key]
                    data["arkham_onchain"] = {
                        "inflow_usd": flow_info["inflow_usd"],
                        "outflow_usd": flow_info["outflow_usd"],
                        "tx_count": flow_info["tx_count"],
                        "whale_txs": flow_info["whale_txs"],
                        "sentiment": "ACCUMULATION" if flow_info["outflow_usd"] > flow_info["inflow_usd"] else ("DISTRIBUTION" if flow_info["inflow_usd"] > flow_info["outflow_usd"] else "NEUTRAL")
                    }
                    
            with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
                json.dump(snap, f, indent=2)
            logger.info("Successfully enriched telemetry snapshot with Arkham on-chain intelligence")
        except Exception as e:
            logger.error("Failed to inject into telemetry snapshot: %s", e)
            
    return structured

def run(deep_scan: bool = True):
    logger.info("Harvesting Arkham On-Chain Intelligence via CDP (min USD >= $50,000)...")
    raw = asyncio.run(harvest_arkham_dom(target_min_usd=50000))
    inst_registry = {}
    if deep_scan:
        logger.info("Initiating Deep Institutional Registry scan...")
        inst_registry = asyncio.run(harvest_institutional_deep_registry(priority_count=3))
        
    if raw:
        data = parse_arkham_data(raw, institutional_registry=inst_registry)
        logger.info(f"=== ARKHAM INSTITUTIONAL HARVEST SUMMARY ===")
        logger.info(f"Filter: {data['filter_applied']} | Feed Status: {data['feed_status']}")
        logger.info(f"Sentiment: {data['market_flow_sentiment']}")
        logger.info(f"Entities: {len(data['trending_institutional_entities'])} | Institutional Profiles Deep: {len(data['institutional_entities_deep'])}")
        logger.info(f"Transfers: {data['aggregate_metrics']['total_transfers_monitored']} | Whale Alerts (>= $50k): {data['aggregate_metrics']['large_whale_alerts_count']}")
        return data
    else:
        logger.warning("Failed to harvest Arkham data.")
        return None

if __name__ == "__main__":
    deep = "--deep" in sys.argv or True
    run(deep_scan=deep)
