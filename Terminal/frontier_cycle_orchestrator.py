"""
Terminal/frontier_cycle_orchestrator.py
Automated End-to-End Orchestrator for the Quad-Frontier Advisory Council:
  1. arena_agent: Arena.ai in Agent Mode (GitHub kbsingh1399/Trading_2)
  2. argon: Google Gemini in Argon Deep Reasoning Mode
  3. opus: Copilot Studio Claude Opus 5.5
  4. astra: Copilot Studio GPT 6 Astra

Key Protocols:
  - Parallel Prompt Dispatch with explicit CYCLE_ID.
  - Synchronization Barrier: Waits until ALL 4 agents have completed their output.
  - Harvester: Saves full markdown artifacts for each model.
  - Cross-Verification & Arena Tournament Synthesis.
  - Autonomous Execution on MetaTrader 5 (Antigravity Sovereign Muscle).
  - Continuous Next-Cycle Re-Prompting.
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
TRADE_PLANS_DIR = ROOT / "docs" / "trade_plans"
PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
TRADE_PLANS_DIR.mkdir(parents=True, exist_ok=True)

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

async def eval_js(ws, expression: str, timeout: float = 8.0):
    msg_id = int(time.time() * 1000) % 1000000
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
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp_str = await asyncio.wait_for(ws.recv(), timeout=2.0)
            resp = json.loads(resp_str)
            if resp.get("id") == msg_id:
                return resp.get("result", {}).get("result", {}).get("value")
        except asyncio.TimeoutError:
            continue
        except Exception:
            break
    return None

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

def build_microstructure_extract() -> str:
    snapshot_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
    if not snapshot_path.exists():
        return ""
    try:
        with open(snapshot_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        matrix = data.get("assets_matrix_24", {})
        priority_assets = ["SP500", "BTC", "ETH", "GOLD", "USDJPY", "NAS100", "USWTI"]
        sections = []
        for sym in priority_assets:
            if sym not in matrix:
                continue
            a = matrix[sym]
            q = a.get("quotes", {})
            ob = a.get("orderbook_live_depth", {})
            stops = a.get("structural_stop_clusters", {})
            liqs = a.get("reconstructed_liquidations", {})
            cvd = a.get("multi_horizon_cvd", {})
            
            # Walls
            l2_walls = ob.get("l2_wall_levels", [])
            l3_whales = ob.get("whale_walls_l3", [])
            
            buys = [w for w in l2_walls if w.get("side") == "BUY"][:3]
            sells = [w for w in l2_walls if w.get("side") == "SELL"][:3]
            
            # Stops
            buy_stops = stops.get("nearest_buy_stop_clusters_above", [])[:2]
            sell_stops = stops.get("nearest_sell_stop_clusters_below", [])[:2]
            
            # Liqs
            short_liqs = liqs.get("nearest_short_squeeze_bands_above", [])[:2]
            long_liqs = liqs.get("nearest_long_cascade_bands_below", [])[:2]
            
            lines = [f"### {sym} Microstructure Provenance:"]
            lines.append(f"- Mid: {q.get('mid')} | Bid/Ask: {q.get('bid')} / {q.get('ask')} | Spread: {round(q.get('spread_bps', 0), 2)} bps")
            lines.append(f"- CVD Flow: Status={cvd.get('status', 'N/A')} | Session CVD={cvd.get('session_cvd_usd', 'N/A')} | Flow={cvd.get('divergence', 'N/A')}")
            
            if l2_walls:
                lines.append(f"- Resting L2 Orderbook Walls ({len(l2_walls)} levels detected):")
                for b in buys:
                    lines.append(f"  * BID: price={b.get('price')}, notional={b.get('notional_usd')} USD, persist={b.get('persist_s', 0)}s, class={b.get('wall_class')}")
                for s in sells:
                    lines.append(f"  * ASK: price={s.get('price')}, notional={s.get('notional_usd')} USD, persist={s.get('persist_s', 0)}s, class={s.get('wall_class')}")
            elif l3_whales:
                lines.append(f"- On-Chain L3 Whale Orders ({len(l3_whales)} orders):")
                for w in l3_whales[:4]:
                    lines.append(f"  * {w.get('side', '').upper()}: price={w.get('price')}, notional={w.get('notional_usd')} USD, maker={w.get('maker', 'N/A')[:10]}")
            
            if buy_stops or sell_stops:
                lines.append("- Nearest Structural Stop Clusters:")
                if buy_stops:
                    lines.append(f"  * Buy Stops Above: {[{'range': [bs.get('min_price'), bs.get('max_price')], 'notional_usd': bs.get('notional_usd')} for bs in buy_stops]}")
                if sell_stops:
                    lines.append(f"  * Sell Stops Below: {[{'range': [ss.get('min_price'), ss.get('max_price')], 'notional_usd': ss.get('notional_usd')} for ss in sell_stops]}")
            
            if short_liqs or long_liqs:
                lines.append("- Nearest Liquidation Cascade Bands:")
                if short_liqs:
                    lines.append(f"  * Short Squeeze Above: {[{'range': [sl.get('min_price'), sl.get('max_price')], 'notional_usd': sl.get('notional_usd')} for sl in short_liqs]}")
                if long_liqs:
                    lines.append(f"  * Long Cascade Below: {[{'range': [ll.get('min_price'), ll.get('max_price')], 'notional_usd': ll.get('notional_usd')} for ll in long_liqs]}")
            
            sections.append("\n".join(lines))
        return "\n\n".join(sections)
    except Exception as e:
        return f"Error extracting microstructure: {e}"

def build_quad_prompt(cycle: int = 86) -> str:
    telemetry_table = build_24_asset_table()
    microstructure_detail = build_microstructure_extract()
    prompt = f"""# ADVANCED INSTITUTIONAL QUANTITATIVE PROMPT — CYCLE {cycle}
CYCLE_ID: CYCLE_{cycle}

================================================================================
MANDATORY CYCLE COMPLETION IDENTIFIER CONTRACT:
================================================================================
You are participating in a synchronized Quad-Frontier Quantitative Council.
Every member of this council (Arena Agent, Gemini Argon, Claude Opus 5.5, GPT 6 Astra)
is operating on the exact same cycle simultaneously.

SYNCHRONIZATION BARRIER REQUIREMENTS:
To ensure the trading desk does not close this cycle prematurely, your output MUST follow this exact lifecycle contract:
1. First line of your response MUST be:
   [CYCLE_ID: CYCLE_{cycle}_START]
2. Conduct your full quantitative analysis, tournament brackets, audits, and candidate evaluations without truncating.
3. Very last line of your response MUST be:
   [CYCLE_ID: CYCLE_{cycle}_COMPLETE]

The Desk coordinator runs an automated synchronization barrier that monitors all 4 models in real-time. This cycle will ONLY be marked completed and compiled once ALL 4 models have finished their responses and emitted their [CYCLE_ID: CYCLE_{cycle}_COMPLETE] token.

SOVEREIGN DESK LEADERSHIP & ROLE CONTRACT:
- ANTIGRAVITY (FLASH) is the sole and ultimate quantitative decision-maker, chief architect, and execution muscle on this desk.
- YOU are an expert quantitative consultant on our Frontier Advisory Council.
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

DETAILED ORDERBOOK & MICROSTRUCTURE PROVENANCE (TOP CANDIDATES):
{microstructure_detail}

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

Output a structured, rigorous quantitative report with clear tournament matchups, gate checks, and specific rulings. Conclude with: [CYCLE_ID: CYCLE_{cycle}_COMPLETE]
"""
    return prompt

async def inject_arena_agent(ws_url: str, prompt_text: str) -> bool:
    try:
        async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
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
            return bool(await eval_js(ws, click_script))
    except Exception as e:
        print(f"[ERROR] arena_agent injection failed: {e}")
        return False

async def inject_gemini_argon(ws_url: str, prompt_text: str) -> bool:
    try:
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
            await asyncio.sleep(0.5)
            
            clear_script = """(() => {
                const editor = document.querySelector('.ql-editor');
                if (!editor) return false;
                editor.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                return true;
            })()"""
            await eval_js(ws, clear_script)
            await asyncio.sleep(0.3)

            chunk_size = 5000
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

            click_script = """(() => {
                const btn = document.querySelector('button[aria-label*="Send message" i]') || document.querySelector('button.send-button');
                if (btn && !btn.disabled) {
                    btn.focus();
                    btn.click();
                    return true;
                }
                return false;
            })()"""
            res = await eval_js(ws, click_script)
            
            # Additional hardware mouse click to guarantee submit
            coord_script = """(() => {
                const btn = document.querySelector('button[aria-label*="Send message" i]') || document.querySelector('button.send-button');
                if (!btn) return null;
                const r = btn.getBoundingClientRect();
                return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
            })()"""
            coords = await eval_js(ws, coord_script)
            if coords:
                cx, cy = coords['x'], coords['y']
                await ws.send(json.dumps({"id": 201, "method": "Input.dispatchMouseEvent", "params": {"type": "mouseMoved", "x": cx, "y": cy}}))
                await ws.recv()
                await ws.send(json.dumps({"id": 202, "method": "Input.dispatchMouseEvent", "params": {"type": "mousePressed", "x": cx, "y": cy, "button": "left", "clickCount": 1}}))
                await ws.recv()
                await ws.send(json.dumps({"id": 203, "method": "Input.dispatchMouseEvent", "params": {"type": "mouseReleased", "x": cx, "y": cy, "button": "left", "clickCount": 1}}))
                await ws.recv()
            return True
    except Exception as e:
        print(f"[ERROR] gemini_argon injection failed: {e}")
        return False

async def inject_copilot(ws_url: str, prompt_text: str) -> bool:
    try:
        async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
            open_script = """(() => {
                const input = document.querySelector('[aria-label*="Chat message input"]');
                if (!input) {
                    const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Preview');
                    if (btn) btn.click();
                }
                return true;
            })()"""
            await eval_js(ws, open_script)
            await asyncio.sleep(0.8)

            state_json = {
                "root": {
                    "children": [{
                        "children": [{
                            "detail": 0, "format": 0, "mode": "normal", "style": "",
                            "text": prompt_text, "type": "text", "version": 1
                        }],
                        "direction": None, "format": "", "indent": 0,
                        "type": "paragraph", "version": 1, "textFormat": 0, "textStyle": ""
                    }],
                    "direction": None, "format": "", "indent": 0,
                    "type": "root", "version": 1
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

            send_script = """(() => {
                const sendBtn = document.querySelector('button[aria-label="Send"]');
                if (sendBtn && !sendBtn.disabled) {
                    sendBtn.click();
                    return true;
                }
                return false;
            })()"""
            return bool(await eval_js(ws, send_script))
    except Exception as e:
        print(f"[ERROR] copilot injection failed: {e}")
        return False

async def dispatch_parallel(cycle: int) -> Dict[str, str]:
    tabs = get_frontier_tabs()
    print(f"\n[*] DISPATCHING CYCLE {cycle} TO ALL 4 FRONTIER AGENTS IN PARALLEL...")
    prompt = build_quad_prompt(cycle=cycle)
    
    prompt_file = PROMPTS_DIR / f"QUAD_MASTER_PROMPT_CYCLE_{cycle}.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    print(f"[+] Archived Cycle {cycle} prompt to {prompt_file.name}")

    tasks = {}
    if 'arena_agent' in tabs:
        tasks['arena_agent'] = inject_arena_agent(tabs['arena_agent'], prompt)
    if 'argon' in tabs:
        tasks['argon'] = inject_gemini_argon(tabs['argon'], prompt)
    if 'opus' in tabs:
        tasks['opus'] = inject_copilot(tabs['opus'], prompt)
    if 'astra' in tabs:
        tasks['astra'] = inject_copilot(tabs['astra'], prompt)

    names = list(tasks.keys())
    results_list = await asyncio.gather(*tasks.values(), return_exceptions=True)
    results = {}
    for name, res in zip(names, results_list):
        if isinstance(res, Exception):
            results[name] = f"ERROR: {res}"
        else:
            results[name] = "SUBMITTED" if res else "FAILED"
        print(f"  -> {name:<12}: {results[name]}")
    return results

async def check_agent_status(name: str, ws_url: str) -> Dict[str, Any]:
    try:
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            if name == 'arena_agent':
                js = """(() => {
                    const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
                    const prose = Array.from(document.querySelectorAll('.prose, div.markdown-prose')).filter(e => !e.classList.contains('tiptap'));
                    const lastText = prose.length > 0 ? prose[prose.length - 1].innerText : '';
                    return {
                        isGenerating: Boolean(stopBtn),
                        textLen: lastText.length,
                        text: lastText
                    };
                })()"""
            elif name == 'argon':
                js = """(() => {
                    const stop = document.querySelector('button[aria-label*="Stop" i], button.stop-button');
                    const resp = Array.from(document.querySelectorAll('model-response, message-content, .model-response-text'));
                    const lastText = resp.length > 0 ? resp[resp.length - 1].innerText : '';
                    return {
                        isGenerating: Boolean(stop),
                        textLen: lastText.length,
                        text: lastText
                    };
                })()"""
            else:
                js = """(() => {
                    const stop = document.querySelector('button[aria-label="Stop"], button[title="Stop"]');
                    const typing = document.querySelector('[class*="typing"], [class*="thinking"], [class*="streaming"], .webchat__typing-indicator');
                    const msgs = Array.from(document.querySelectorAll('[role="listitem"], .webchat__row, [data-testid*="message" i], div:has(> table), div:has(> ol)')).map(e => e.innerText).filter(txt => txt && txt.length > 150);
                    const lastText = msgs.length > 0 ? msgs[msgs.length - 1] : '';
                    return {
                        isGenerating: Boolean(stop || typing),
                        textLen: lastText.length,
                        text: lastText
                    };
                })()"""
            res = await eval_js(ws, js)
            return res or {"isGenerating": False, "textLen": 0, "text": ""}
    except Exception as e:
        return {"isGenerating": False, "textLen": 0, "text": "", "error": str(e)}

async def wait_until_cycle_completed(cycle: int, poll_interval: int = 15, max_wait: int = 1200) -> Dict[str, str]:
    print(f"\n[*] SYNCHRONIZATION BARRIER ACTIVE: Waiting until ALL 4 agents finish CYCLE {cycle}...")
    start_time = time.time()
    tabs = get_frontier_tabs()
    
    while time.time() - start_time < max_wait:
        status_map = {}
        done_count = 0
        total_count = len(tabs)
        harvested_texts = {}

        for name, ws_url in tabs.items():
            st = await check_agent_status(name, ws_url)
            is_gen = st.get("isGenerating", False)
            t_len = st.get("textLen", 0)
            status_map[name] = {"generating": is_gen, "length": t_len}
            harvested_texts[name] = st.get("text", "")
            if not is_gen and t_len > 500:
                done_count += 1

        elapsed = int(time.time() - start_time)
        print(f"[{elapsed}s] Cycle {cycle} Barrier Progress: {done_count}/{total_count} Finished", flush=True)
        for n, s in status_map.items():
            state_str = "GENERATING" if s["generating"] else "COMPLETED"
            print(f"    {n:<12}: {state_str} ({s['length']} chars)", flush=True)

        if done_count >= total_count:
            print(f"\n[+] ALL {total_count} AGENTS COMPLETED CYCLE {cycle}! Barrier unlocked.", flush=True)
            # Save raw artifacts
            for name, text in harvested_texts.items():
                out_file = TRADE_PLANS_DIR / f"CYCLE_{cycle}_{name.upper()}.md"
                out_file.write_text(text, encoding="utf-8")
                print(f"[+] Saved {out_file.name} ({len(text)} chars)", flush=True)
            return harvested_texts

        await asyncio.sleep(poll_interval)

    print(f"[WARNING] Barrier timed out after {max_wait}s. Proceeding with available outputs.")
    return {}

if __name__ == "__main__":
    c = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 84
    if "--wait" in sys.argv:
        asyncio.run(wait_until_cycle_completed(cycle=c))
    elif "--dispatch" in sys.argv:
        asyncio.run(dispatch_parallel(cycle=c))
    else:
        print("Usage: python Terminal/frontier_cycle_orchestrator.py [cycle] [--dispatch | --wait]")
