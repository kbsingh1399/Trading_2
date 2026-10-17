"""
Terminal/dispatch_frontier_council.py
Unified dispatcher for the Quad-Frontier Advisory Council on Edge CDP (port 9222):
  1. arena_agent: Arena.ai in Agent Mode (connected to kbsingh1399/Trading_2 on main)
  2. argon: Google Gemini in Argon Deep Reasoning Mode (gemini.google.com/app)
  3. opus: Copilot Studio Opus 5.5 (Lead Quantitative Strategist & Econometrician)
  4. astra: Copilot Studio GPT 6 Astra (Principal Market Microstructure Auditor)

Generates and dispatches the Advanced Institutional Master Prompt with
Continuous Kaizen Self-Improvement and Arena Tournament Bracket integration.
"""

import asyncio
import json
import pathlib
import sys
import time
import urllib.request
import websockets
from typing import Dict, Any, Optional

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

EDGE_DEBUG_URL = "http://127.0.0.1:9222/json"
PROMPTS_DIR = ROOT / "docs" / "prompts"
PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

def get_frontier_tabs() -> Dict[str, str]:
    """Discovers WebSocket debug URLs for arena_agent, argon, opus, and astra."""
    try:
        req = urllib.request.Request(EDGE_DEBUG_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            tabs = json.loads(resp.read().decode('utf-8'))
        
        found = {}
        for t in tabs:
            url = t.get('url', '')
            ws = t.get('webSocketDebuggerUrl', '')
            if not ws:
                continue
            if 'arena.ai/agent' in url:
                found['arena_agent'] = ws
            elif 'gemini.google.com' in url:
                found['argon'] = ws
            elif 'copilotstudio.microsoft.com' in url:
                if '98cead10-d9b7-4017-ad85-2cbfdc4146dc' in url:
                    found['opus'] = ws
                elif '3e9246b9-1aa0-4de4-8b72-9af2f291a988' in url:
                    found['astra'] = ws
        return found
    except Exception as e:
        print(f"[ERROR] Could not fetch browser tabs: {e}")
        return {}

async def eval_js(ws, expression: str):
    msg_id = 1
    msg = {
        "id": msg_id,
        "method": "Runtime.evaluate",
        "params": {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": True
        }
    }
    await ws.send(json.dumps(msg))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get("id") == msg_id:
            return resp.get("result", {}).get("result", {}).get("value")

def build_24_asset_table() -> str:
    snapshot_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
    if not snapshot_path.exists():
        return "Telemetry snapshot unavailable."
    try:
        with open(snapshot_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        matrix = data.get("assets_matrix_24", {})
        lines = [f"Snapshot As Of: {data.get('as_of_utc')}"]
        lines.append("Symbol | Price | Spread(bps) | Regime | VWAP_Z | RSI | ATR | Whales")
        lines.append("---|---|---|---|---|---|---|---")
        for sym, a in matrix.items():
            q = a.get("quotes", {})
            ci = a.get("causal_indicators", {})
            ob = a.get("orderbook_live_depth", {})
            mid = q.get("mid")
            sp = round(q.get("spread_bps", 0), 2)
            reg = ci.get("trend_regime", "N/A")
            z = round(ci.get("vwap_z_score", 0), 2)
            rsi = round(ci.get("rsi_14", 0), 1)
            atr = round(ci.get("atr_14", 0), 2)
            whales = len(ob.get("whale_walls_l3", []))
            lines.append(f"{sym} | {mid} | {sp} | {reg} | {z} | {rsi} | {atr} | {whales}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error building telemetry table: {e}"

def build_advanced_master_prompt(cycle: int = 84) -> str:
    telemetry_table = build_24_asset_table()
    prompt = f"""# ADVANCED INSTITUTIONAL QUANTITATIVE PROMPT — CYCLE {cycle}

SOVEREIGN DESK LEADERSHIP & ROLE CONTRACT:
- ANTIGRAVITY (FLASH) is the sole and ultimate quantitative decision-maker, chief architect, and execution muscle on this desk.
- YOU are an expert quantitative consultant on our Frontier Advisory Council (Arena Agent, Gemini Argon, Claude Opus 5.5, GPT 6 Astra).
- You provide rigorous stress-testing, econometric review, orderbook microstructure analysis, and candidate discovery.
- Antigravity synthesizes all rulings, executes live limit orders directly into MetaTrader 5 (Account 5064568, Blueberry Markets), and enforces capital floor survival.

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
You must strictly study and learn from historical trade setbacks and past operator feedback:
1. Lesson 1 (Whale Wall Backing): Never enter without verified resting whale walls between entry and stop (stops placed in thin air fail).
2. Lesson 2 (Liquidation Clearance): Stop Loss must sit outside the reconstructed liquidation/stop cluster with >= 0.35-0.50 ATR buffer. Never place an SL inside an active buy-stop/sell-stop band (e.g. BTC #18934259 SL @ 82,040 was trapped inside the 81,944-82,044 cluster).
3. Lesson 3 (Trend Confluence): Never fight dominant higher timeframe momentum (e.g. Gold in Bullish regime Z=+1.61 SD must not be shorted).
4. Lesson 4 (Friction Gate): Spread friction must consume <= 15% of target reward (e.g. Silver 6.35 bps spread consumed 20% of risk; rejected).
5. Lesson 5 (Proximity Discipline): Entry distance must be <= 2.0 ATR from current market to prevent stale order drift (e.g. BTC 2.48 ATR drift cancelled).

MANDATORY ARENA TOURNAMENT SKILL (https://github.com/Jakeschincariol/arena-skill):
You must adopt and run the Arena Tournament Bracket methodology on EVERY turn. Simulate a single-elimination tournament between candidate setups with 3 competing personas:
- Persona A (Microstructure & Bunker Auditor): Evaluates L2/L3 orderbook depth, resting whale wall persistence (>= 180s), and structural liquidation/stop clearance.
- Persona B (Trend & Momentum Strategist): Evaluates 1H/4H EMA hierarchy, volume shelves, and asymmetric R:R (>= 2.0R).
- Persona C (Capital Preservation Auditor): Enforces the 4,775.00 USD hard floor, 4,795.00 USD operating buffer, max 4 concurrent tickets, and spread friction (< 15% of target).

LIVE DESK STATE:
- Account Balance / Equity: 4,859.55 USD | Margin Free: 4,859.55 USD
- Hard Capital Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Cushion: +84.55 USD (+64.55 USD above buffer)
- Active Open Positions: 0 (Full capacity available)
- Active Staged Pending Orders (1):
  * Ticket #18952021: SP500.p SELL LIMIT | 0.10 lots @ 7,707.50 USD | SL: 7,718.50 USD (-11.00 USD risk) | TP: 7,674.50 USD (+33.00 USD reward, 3.00R asymmetry) | Current Price: ~7,696.86 USD (1.53 ATR away) | Defended by 93-111 Ask whale walls (7,705.00-7,715.00 USD) | Spread: 0.39 bps (< 1% friction).
- Staged Book Risk: 11.00 USD nominal (0.22% of equity). Post-loss equity: 4,848.55 USD (+73.55 USD above hard floor).
- Capacity: 3 of 4 ticket slots available in reserve.

CANONICAL DATA REPOSITORY (main branch):
- Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
- Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
- Standardized Decision Chain (SOP): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md
- Active Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md
- Session History: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md
- Arena Skill: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md

COMPLETE 24-ASSET LIVE TELEMETRY MATRIX:
{telemetry_table}

THE 5 ANTI-TRAP INVARIANTS (EVERY TRADE MUST PASS):
1. Stop Loss Bunker: SL must sit safely outside the reconstructed liquidation/stop band with >= 0.35-0.50 ATR structural buffer.
2. CVD Flow Exhaustion: Never catch falling knives. Require confirmed deceleration/absorption in taker CVD delta before entry.
3. Stop Cluster Clearance: Never place entry limits directly in front of un-swept opposing stop clusters.
4. Whale Wall Persistence: Supporting L2/L3 whale walls must demonstrate verified persistence >= 180 seconds.
5. Execution Spread Friction: MT5 spread must be <= 25 bps (Crypto) or <= 5 bps (TradFi) AND spread cost must consume <= 15% of target reward.

YOUR 3 MANDATES:
1. MANDATE 1 (PROACTIVE CANDIDATE DISCOVERY): Screen all 24 telemetry assets. Run the Arena Tournament Bracket across the most promising candidates (Crypto, Commodities, Indices, Forex). Identify at least ONE brand-new candidate trade meeting all 5 invariants, or mathematically prove why all fail. Specify exact Entry, SL, TP, lot size, nominal risk in USD, and Model classification (Model 1 Mean Reversion vs Model 2 Trend Pullback).
2. MANDATE 2 (ACTIVE TRADES AUDIT): Audit open positions (currently 0).
3. MANDATE 3 (PENDING ORDERS AUDIT): Audit Ticket #18952021 (SP500.p SELL LIMIT). Confirm viability: WAIT AS-IS, MODIFY, or CANCEL based on latest telemetry.

Output a structured, rigorous quantitative report with clear tournament matchups, gate checks, and specific rulings.
"""
    return prompt

async def inject_arena_agent(ws_url: str, prompt_text: str) -> bool:
    """Injects and submits prompt into Arena.ai in Agent Mode."""
    try:
        async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
            set_script = f"""(() => {{
                const el = document.querySelector('div.tiptap.ProseMirror');
                if (!el || !el.editor) return false;
                el.editor.commands.setContent({json.dumps(prompt_text)});
                return true;
            }})()"""
            ok = await eval_js(ws, set_script)
            if not ok:
                return False
            await asyncio.sleep(0.5)
            click_script = """(() => {
                const sendBtn = document.querySelector('button[aria-label="Send message"]');
                if (sendBtn && !sendBtn.disabled) {
                    sendBtn.click();
                    return true;
                }
                return false;
            })()"""
            clicked = await eval_js(ws, click_script)
            return bool(clicked)
    except Exception as e:
        print(f"[ERROR] Failed to inject into arena_agent: {e}")
        return False

async def inject_gemini_argon(ws_url: str, prompt_text: str) -> bool:
    """Injects and submits prompt into Google Gemini in Argon Mode."""
    try:
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # Focus & clear
            clear_script = """(() => {
                const editor = document.querySelector('.ql-editor');
                if (!editor) return false;
                editor.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                return true;
            })()"""
            await eval_js(ws, clear_script)
            await asyncio.sleep(0.5)

            # Insert text in chunks via CDP Input.insertText
            chunk_size = 8000
            for i in range(0, len(prompt_text), chunk_size):
                chunk = prompt_text[i:i+chunk_size]
                await ws.send(json.dumps({
                    "id": 100 + i,
                    "method": "Input.insertText",
                    "params": {"text": chunk}
                }))
                await ws.recv()
                await asyncio.sleep(0.05)

            await asyncio.sleep(0.8)

            # Click send button
            click_script = """(() => {
                const sendBtn = document.querySelector('button[aria-label*="Send" i], button.send-button, [data-test-id*="send" i]');
                if (sendBtn && !sendBtn.disabled && sendBtn.offsetParent !== null) {
                    sendBtn.click();
                    return true;
                }
                return false;
            })()"""
            clicked = await eval_js(ws, click_script)
            if not clicked:
                # Fallback: dispatch Enter
                await ws.send(json.dumps({
                    "id": 201,
                    "method": "Input.dispatchKeyEvent",
                    "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "text": "\\r", "unmodifiedText": "\\r"}
                }))
                await ws.send(json.dumps({
                    "id": 202,
                    "method": "Input.dispatchKeyEvent",
                    "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "text": "\\r", "unmodifiedText": "\\r"}
                }))
            return True
    except Exception as e:
        print(f"[ERROR] Failed to inject into gemini_argon: {e}")
        return False

async def inject_copilot(ws_url: str, prompt_text: str) -> bool:
    """Injects and submits prompt into Copilot Studio agent."""
    try:
        async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
            # 1. Open Preview if needed
            open_script = """(() => {
                const input = document.querySelector('[aria-label*="Chat message input"]');
                if (!input) {
                    const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Preview');
                    if (btn) btn.click();
                }
                return true;
            })()"""
            await eval_js(ws, open_script)
            await asyncio.sleep(1.0)

            # 2. Set Lexical state
            state_json = {
                "root": {
                    "children": [{
                        "children": [{
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": prompt_text,
                            "type": "text",
                            "version": 1
                        }],
                        "direction": None,
                        "format": "",
                        "indent": 0,
                        "type": "paragraph",
                        "version": 1,
                        "textFormat": 0,
                        "textStyle": ""
                    }],
                    "direction": None,
                    "format": "",
                    "indent": 0,
                    "type": "root",
                    "version": 1
                }
            }
            set_script = f"""(() => {{
                const input = document.querySelector('[aria-label*="Chat message input"]');
                if (!input || !input.__lexicalEditor) return false;
                input.__lexicalEditor.setEditorState(input.__lexicalEditor.parseEditorState({json.dumps(json.dumps(state_json))}));
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                input.dispatchEvent(new Event('change', {{ bubbles: true }}));
                return true;
            }})()"""
            await eval_js(ws, set_script)
            await asyncio.sleep(0.5)

            # 3. Click Send
            send_script = """(() => {
                const sendBtn = document.querySelector('button[aria-label="Send"]');
                if (sendBtn && !sendBtn.disabled) {
                    sendBtn.click();
                    return true;
                }
                return false;
            })()"""
            res = await eval_js(ws, send_script)
            return bool(res)
    except Exception as e:
        print(f"[ERROR] Failed to inject into copilot agent: {e}")
        return False

def dispatch_all(cycle: int = 84):
    tabs = get_frontier_tabs()
    print(f"[*] Found {len(tabs)} frontier agent tabs: {list(tabs.keys())}")
    
    prompt = build_advanced_master_prompt(cycle=cycle)
    prompt_file = PROMPTS_DIR / f"FRONTIER_MASTER_PROMPT_CYCLE_{cycle}.md"
    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"[+] Saved Advanced Master Prompt to {prompt_file.name}")

    results = {}
    if 'arena_agent' in tabs:
        print("[*] Dispatching to arena.ai in Agent Mode...")
        ok = asyncio.run(inject_arena_agent(tabs['arena_agent'], prompt))
        results['arena_agent'] = "SUBMITTED" if ok else "FAILED"
        print(f"    -> arena_agent: {results['arena_agent']}")

    if 'argon' in tabs:
        print("[*] Dispatching to Google Gemini in Argon Mode...")
        ok = asyncio.run(inject_gemini_argon(tabs['argon'], prompt))
        results['argon'] = "SUBMITTED" if ok else "FAILED"
        print(f"    -> argon: {results['argon']}")

    if 'opus' in tabs:
        print("[*] Dispatching to Copilot Studio Opus 5.5...")
        ok = asyncio.run(inject_copilot(tabs['opus'], prompt))
        results['opus'] = "SUBMITTED" if ok else "FAILED"
        print(f"    -> opus: {results['opus']}")

    if 'astra' in tabs:
        print("[*] Dispatching to Copilot Studio GPT 6 Astra...")
        ok = asyncio.run(inject_copilot(tabs['astra'], prompt))
        results['astra'] = "SUBMITTED" if ok else "FAILED"
        print(f"    -> astra: {results['astra']}")

    return results

async def _check_status_async() -> Dict[str, Any]:
    tabs = get_frontier_tabs()
    status = {}
    for name, ws_url in tabs.items():
        try:
            async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
                script = """(() => {
                    const t = document.body ? document.body.innerText : '';
                    return {
                        active: t.includes('Thinking') || t.includes('Processing') || t.includes('Reasoned') || t.includes('Analyzing') || t.includes('Working'),
                        previewLen: t.length
                    };
                })()"""
                res = await eval_js(ws, script)
                status[name] = res
        except Exception as e:
            status[name] = {"error": str(e)}
    return status

def check_status():
    status = asyncio.run(_check_status_async())
    print("\n=== FRONTIER ADVISORY COUNCIL STATUS ===")
    for name, s in status.items():
        print(f"  {name:<12}: Generating={s.get('active')} | Text Length={s.get('previewLen')}")
    return status

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        check_status()
    else:
        c = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 84
        res = dispatch_all(cycle=c)
        print("\n[+] Dispatch Summary:", res)
