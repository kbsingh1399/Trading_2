"""
Terminal/Data_Factory/forex_factory_harvester.py
High-Performance Zero-Token Forex Factory Harvester.
Harvests Economic Calendar, Central Bank Rates, Breaking News, and Community Sentiment
directly via the authenticated Edge/Chrome browser tab on CDP (port 9222).
Saves:
  - Data/forex_factory_live.json (full detailed intelligence)
  - Data/forex_factory_summary.json (ultra-compact < 150 token summary for prompts/telemetry)
"""

import asyncio
import json
import logging
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

FULL_OUTPUT_FILE = DATA_DIR / "forex_factory_live.json"
SUMMARY_OUTPUT_FILE = DATA_DIR / "forex_factory_summary.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("ForexFactoryHarvester")

def get_ff_cdp_ws_url() -> str | None:
    """Find the WebSocket debugger URL for the Forex Factory tab."""
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3.0)
        tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            url = t.get("url", "")
            if "forexfactory.com" in url:
                return t.get("webSocketDebuggerUrl")
    except Exception as e:
        logger.error(f"Failed to query CDP tabs: {e}")
    return None

async def evaluate_js(ws, js_code: str) -> dict:
    """Send JavaScript expression to tab via CDP Runtime.evaluate."""
    msg = {
        "id": int(time.time() * 1000) % 1000000,
        "method": "Runtime.evaluate",
        "params": {
            "expression": js_code,
            "awaitPromise": True,
            "returnByValue": True
        }
    }
    try:
        await ws.send(json.dumps(msg))
        resp_raw = await asyncio.wait_for(ws.recv(), timeout=15.0)
        resp = json.loads(resp_raw)
        result = resp.get("result", {}).get("result", {})
        if "value" in result:
            return result["value"]
        if "description" in result:
            logger.warning(f"JS execution error: {result['description']}")
    except asyncio.TimeoutError:
        logger.warning("CDP evaluate_js timed out after 15.0s")
    except Exception as e:
        logger.warning(f"CDP evaluate_js exception: {e}")
    return {}

async def harvest_calendar(ws) -> dict:
    """Harvest high and medium impact calendar events."""
    js = """(async () => {
        try {
            const res = await fetch('/calendar');
            const html = await res.text();
            const start = html.indexOf('window.calendarComponentStates[1] = {');
            if (start === -1) return { error: 'calendarComponentStates not found' };
            const end = html.indexOf('};', start);
            const raw = html.slice(start + 36, end + 1);
            const data = new Function('return (' + raw + ')')();
            const events = [];
            for (const d of (data.days || [])) {
                for (const e of (d.events || [])) {
                    events.push({
                        date: d.date.replace(/<[^>]+>/g, ''),
                        dateline: e.dateline,
                        time: e.timeLabel || '',
                        currency: e.currency || '',
                        impact: e.impactName || '',
                        name: e.name || '',
                        forecast: e.forecast || '',
                        previous: e.previous || '',
                        actual: e.actual || ''
                    });
                }
            }
            const high_med = events.filter(e => e.impact === 'high' || e.impact === 'medium');
            return {
                total_events: events.length,
                high_medium_count: high_med.length,
                events: high_med
            };
        } catch(e) {
            return { error: e.toString() };
        }
    })()"""
    return await evaluate_js(ws, js)

async def harvest_news_and_rates(ws) -> dict:
    """Harvest central bank rates and top breaking news stories."""
    js = """(async () => {
        try {
            const res = await fetch('/news');
            const html = await res.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            
            // Central Bank Rates
            const rates = {};
            const text = doc.body.innerText;
            const ratesMatch = text.match(/Central Bank Rates([\\s\\S]*?)Hot Stories/);
            if (ratesMatch) {
                const tokens = ratesMatch[1].split(/\\s+/).filter(Boolean);
                for (let i = 0; i < tokens.length - 1; i++) {
                    if (tokens[i].includes('%') && tokens[i+1].length === 3 && tokens[i+1] === tokens[i+1].toUpperCase()) {
                        rates[tokens[i+1]] = tokens[i];
                    }
                }
            }
            
            // Breaking / Hot Stories
            const stories = [];
            doc.querySelectorAll('a').forEach(a => {
                if (a.href && a.href.includes('/news/') && !a.href.includes('/hit') && !a.href.includes('/comment/')) {
                    const t = a.innerText.trim();
                    if (t.length > 20 && !stories.some(s => s.headline === t)) {
                        stories.push({
                            headline: t,
                            url: a.href
                        });
                    }
                }
            });
            
            return {
                rates: rates,
                stories: stories.slice(0, 12)
            };
        } catch(e) {
            return { error: e.toString() };
        }
    })()"""
    return await evaluate_js(ws, js)

async def harvest_trade_flow(ws) -> dict:
    """Harvest live community trades and positioning signals."""
    js = """(async () => {
        try {
            const res = await fetch('/trades');
            const html = await res.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const trades = [];
            doc.querySelectorAll('tr').forEach(tr => {
                const text = tr.innerText.replace(/\\s+/g, ' ').trim();
                if (text.includes('Opened Short') || text.includes('Opened Long') || text.includes('Closed Short') || text.includes('Closed Long')) {
                    trades.push(text);
                }
            });
            return {
                trade_count: trades.length,
                recent_trades: trades.slice(0, 15)
            };
        } catch(e) {
            return { error: e.toString() };
        }
    })()"""
    return await evaluate_js(ws, js)

def parse_rate_string(rate_str: str) -> dict:
    """Parse rate string like '<1.25%', '4.00%', '0.00%' into numeric float and comparator."""
    comparator = "eq"
    clean_str = rate_str.strip()
    if clean_str.startswith("<"):
        comparator = "lt"
        clean_str = clean_str[1:].strip()
    elif clean_str.startswith(">"):
        comparator = "gt"
        clean_str = clean_str[1:].strip()
    clean_str = clean_str.replace("%", "").strip()
    try:
        val = float(clean_str)
    except Exception:
        val = 0.0
    return {"raw": rate_str, "value": val, "comparator": comparator}

async def run_harvester() -> bool:
    """Main execution entry point."""
    ws_url = get_ff_cdp_ws_url()
    if not ws_url:
        logger.error("No active Forex Factory tab found on CDP port 9222.")
        return False
    
    logger.info("Connecting to Forex Factory tab via CDP...")
    try:
        async with websockets.connect(ws_url, max_size=10_000_000, open_timeout=10.0) as ws:
            logger.info("Harvesting Economic Calendar...")
            cal_data = await asyncio.wait_for(harvest_calendar(ws), timeout=15.0)
            
            logger.info("Harvesting Central Bank Rates & Breaking News...")
            news_data = await asyncio.wait_for(harvest_news_and_rates(ws), timeout=15.0)
            
            logger.info("Harvesting Community Trade Flow...")
            trades_data = await asyncio.wait_for(harvest_trade_flow(ws), timeout=15.0)
            
            now_utc = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
            
            raw_rates = news_data.get("rates", {})
            numeric_rates = {ccy: parse_rate_string(r)["value"] for ccy, r in raw_rates.items()}
            
            full_payload = {
                "harvested_at_utc": now_utc,
                "source": "FOREX_FACTORY_LIVE_CDP",
                "central_bank_rates": raw_rates,
                "central_bank_rates_numeric": numeric_rates,
                "high_medium_calendar_events": cal_data.get("events", []),
                "breaking_news_stories": news_data.get("stories", []),
                "community_trade_flow": trades_data.get("recent_trades", [])
            }
            
            FULL_OUTPUT_FILE.write_text(json.dumps(full_payload, indent=2), encoding="utf-8")
            logger.info(f"Full payload saved to {FULL_OUTPUT_FILE} ({len(json.dumps(full_payload))} bytes)")
            
            # Build ultra-compact summary (< 150 tokens)
            upcoming_events = []
            for ev in cal_data.get("events", []):
                if ev.get("impact") in ["high", "medium"]:
                    act = ev.get("actual", "").strip()
                    fc = ev.get("forecast", "").strip()
                    if act and fc:
                        status = f"Act: {act} | F: {fc}"
                    elif act:
                        status = f"Act: {act}"
                    elif fc:
                        status = f"F: {fc}"
                    else:
                        status = "SPEECH/EVENT"
                    upcoming_events.append(f"{ev.get('currency')} {ev.get('name')} ({ev.get('impact').upper()}) [{status}]")
                    if len(upcoming_events) >= 6:
                        break
            
            top_headlines = [s.get("headline", "") for s in news_data.get("stories", [])[:4] if s.get("headline")]
            
            summary_payload = {
                "as_of_utc": now_utc,
                "rates": raw_rates,
                "rates_numeric": numeric_rates,
                "key_events": upcoming_events,
                "top_headlines": top_headlines,
                "sample_retail_flow": [t[:80] for t in trades_data.get("recent_trades", [])[:3]]
            }
            
            SUMMARY_OUTPUT_FILE.write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")
            logger.info(f"Ultra-compact summary saved to {SUMMARY_OUTPUT_FILE} ({len(json.dumps(summary_payload))} bytes)")
            print(f"SUCCESS: Forex Factory harvested cleanly at {now_utc}")
            return True
    except Exception as e:
        logger.error(f"Error during harvest: {e}", exc_info=True)
        return False

if __name__ == "__main__":
    success = asyncio.run(run_harvester())
    sys.exit(0 if success else 1)
