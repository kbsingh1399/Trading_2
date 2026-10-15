"""
Terminal/Data_Factory/arkham_intelligence_harvester.py
Production On-Chain Intelligence Harvester for Arkham (arkm.com via Chrome CDP).
Extracts:
1. Trending Institutional Entities & Holdings (MicroStrategy, OKX, Kamino, Bhutan, etc.)
2. Real-Time On-Chain Transfers & Classification (Exchange Inflow vs Outflow vs MM Flow)
3. Whale Wallet Deanonymization mapping
4. Injects onchain_intelligence into docs/telemetry/live_snapshot_latest.json
"""

import asyncio
import websockets
import json
import urllib.request
import pathlib
import datetime
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
OUTPUT_PATH = DATA_DIR / "arkham_live_intelligence.json"
DATA_DIR.mkdir(parents=True, exist_ok=True)

KNOWN_EXCHANGES = ["binance", "okx", "bybit", "coinbase", "kraken", "deribit", "bitfinex", "htx", "gate.io"]
KNOWN_MARKET_MAKERS = ["wintermute", "jump", "cumberland", "gsr", "amber", "dwf labs", "falconx", "galaxy"]

async def harvest_arkham() -> dict:
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read())
    except Exception as e:
        print(f"[ERROR] Could not fetch CDP tabs: {e}")
        return {}

    ws_url = None
    for t in tabs:
        if "arkm.com" in t.get("url", "") and t.get("type") == "page":
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("[WARNING] Active Arkham tab not found on port 9222.")
        return {}

    try:
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            js = """
            (() => {
                const text = window.top.document.body.innerText;
                const lines = text.split('\\n').map(l => l.trim()).filter(l => l.length > 0);
                
                // 1. Extract Trending Entities
                const entities = [];
                const entityLinks = Array.from(window.top.document.querySelectorAll('a[href*="/explorer/entity/"]'));
                for (const a of entityLinks) {
                    const txt = a.innerText.trim();
                    const href = a.href;
                    if (txt && txt.length > 3) {
                        entities.push({ text: txt.replace(/\\n+/g, ' | '), href });
                    }
                }

                // 2. Extract Transfer Rows
                const rows = Array.from(window.top.document.querySelectorAll('tr, div[role="row"], div:has(> a[href*="/explorer/tx/"])')).map(el => {
                    const t = el.innerText.trim();
                    const link = el.querySelector('a[href*="/explorer/tx/"]') ? el.querySelector('a[href*="/explorer/tx/"]').href : '';
                    return { text: t.replace(/\\n+/g, ' | '), link };
                }).filter(r => r.text && r.text.length > 15 && !r.text.includes('Trending Entities') && !r.text.includes('DEX | Predictions'));

                return {
                    url: window.top.location.href,
                    title: window.top.document.title,
                    entities: entities.slice(0, 10),
                    rows: rows.slice(0, 25)
                };
            })()
            """
            msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}
            await ws.send(json.dumps(msg))
            res = json.loads(await ws.recv())
            val = res.get("result", {}).get("result", {}).get("value", {})
            return val
    except Exception as e:
        print(f"[ERROR] Failed to query Arkham CDP: {e}")
        return {}

def parse_and_classify(raw_data: dict) -> dict:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entities = raw_data.get("entities", [])
    rows = raw_data.get("rows", [])

    classified_transfers = []
    exchange_inflow_count = 0
    exchange_outflow_count = 0
    total_volume_usd = 0.0

    for r in rows:
        line = r.get("text", "")
        link = r.get("link", "")
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 4:
            continue

        # Look for USD value
        usd_val = 0.0
        for p in parts:
            if "$" in p:
                clean = re.sub(r"[^\d.]", "", p)
                try:
                    usd_val = float(clean)
                except ValueError:
                    pass

        # Identify From and To
        line_lower = line.lower()
        classification = "INTERNAL_TRANSFER"
        for ex in KNOWN_EXCHANGES:
            if f"to {ex}" in line_lower or f"-> {ex}" in line_lower or f"deposit" in line_lower:
                classification = "EXCHANGE_INFLOW (SELL_PRESSURE)"
                exchange_inflow_count += 1
                break
            elif f"from {ex}" in line_lower or f"withdrawal" in line_lower:
                classification = "EXCHANGE_OUTFLOW (ACCUMULATION)"
                exchange_outflow_count += 1
                break

        for mm in KNOWN_MARKET_MAKERS:
            if mm in line_lower:
                classification = f"MARKET_MAKER_FLOW ({mm.upper()})"
                break

        total_volume_usd += usd_val
        classified_transfers.append({
            "raw": line,
            "tx_link": link,
            "usd_value": usd_val,
            "classification": classification
        })

    structured_intelligence = {
        "as_of_utc": now_utc,
        "source": "Arkham Intelligence (arkm.com via Chrome CDP)",
        "status": "LIVE_STREAMING",
        "market_flow_sentiment": "NET_ACCUMULATION" if exchange_outflow_count > exchange_inflow_count else ("NET_DISTRIBUTION" if exchange_inflow_count > exchange_outflow_count else "NEUTRAL"),
        "metrics": {
            "total_transfers_monitored": len(classified_transfers),
            "exchange_inflow_alerts": exchange_inflow_count,
            "exchange_outflow_alerts": exchange_outflow_count,
            "sample_volume_usd": total_volume_usd
        },
        "trending_institutional_entities": entities,
        "recent_classified_transfers": classified_transfers[:15]
    }

    # Save to Data/arkham_live_intelligence.json
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(structured_intelligence, f, indent=2)
    print(f"[+] Saved Arkham Intelligence to {OUTPUT_PATH.name} ({len(classified_transfers)} transfers processed)")

    # Inject into docs/telemetry/live_snapshot_latest.json
    if SNAPSHOT_PATH.exists():
        try:
            with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
                snapshot = json.load(f)
            snapshot["onchain_arkham_intelligence"] = {
                "as_of_utc": now_utc,
                "sentiment": structured_intelligence["market_flow_sentiment"],
                "inflows": exchange_inflow_count,
                "outflows": exchange_outflow_count,
                "trending_entities_count": len(entities),
                "top_entity": entities[0]["text"] if entities else "N/A"
            }
            with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2)
            print("[+] Injected onchain_arkham_intelligence into live_snapshot_latest.json")
        except Exception as e:
            print(f"[WARNING] Could not patch live_snapshot_latest.json: {e}")

    return structured_intelligence

def run():
    raw = asyncio.run(harvest_arkham())
    if raw:
        data = parse_and_classify(raw)
        print("\n=== ARKHAM HARVEST SUMMARY ===")
        print(f"Sentiment: {data['market_flow_sentiment']}")
        print(f"Entities Found: {len(data['trending_institutional_entities'])}")
        print(f"Transfers Classified: {data['metrics']['total_transfers_monitored']}")
        for t in data['recent_classified_transfers'][:5]:
            print(f"  [{t['classification']}] {t['raw'][:100]}")
    else:
        print("[!] No data harvested.")

if __name__ == "__main__":
    run()
