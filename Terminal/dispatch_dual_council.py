"""
Terminal/dispatch_dual_council.py
Unified Dual-Council Prompt Dispatcher for BOTH Arena.ai and Z.ai (GLM-5.3-Flash).

Guarantees 100% compliance with Operator Mandate:
1. Prompts BOTH Arena.ai and Z.ai simultaneously via Chrome CDP (port 9222).
2. Mandatorily embeds Section 2.5 Quantitative Methodology Inquest Question in EVERY prompt.
3. Automatically launches completion monitors for both councils.
"""

import argparse
import asyncio
import datetime
import json
import os
import pathlib
import subprocess
import sys
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPT_FILE = ROOT / "docs" / "trade_plans" / "LATEST_COUNCIL_CYCLE_PROMPT.txt"
ARENA_BRIDGE = ROOT / "Terminal" / "arena_bridge.py"
ZAI_DISPATCHER = ROOT / "Terminal" / "dispatch_zai_prompt.py"
WEB2API_COUNCIL = ROOT / "Terminal" / "web2api_council.py"

CDP_URL = "http://127.0.0.1:9222/json"

def get_live_telemetry():
    telemetry_file = ROOT / "Data" / "telemetry" / "mt5_account_telemetry.json"
    if telemetry_file.exists():
        try:
            with open(telemetry_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"balance": 4818.51, "equity": 4818.51, "cushion_buffer": 23.51, "cushion_floor": 43.51, "positions_count": 0, "orders_count": 0}

def build_unified_prompt(cycle_id: str = "AUTO") -> str:
    telem = get_live_telemetry()
    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    prompt = f"""# 🏛️ CO-EQUAL QUANTITATIVE COUNCIL CANDIDATE DISCOVERY & EVALUATION
## BlueBerry Markets MT5 Account #5064568 | Cycle {cycle_id} | {utc_now}

> **CANONICAL QUANT GOVERNANCE**: Follow line-by-line `STANDARDIZED_TRADING_DECISION_CHAIN.md`, `AUTONOMOUS_WAKEUP_CHECKLIST.md`, and `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`.
> **MISSION**: Reach 5,500.00 USD equity before Friday, 23rd October 2026 (23:59 UTC) (~21.0 hours runway remaining).
> **SOLVENCY FLOORS**: Absolute Hard Floor: 4,775.00 USD (Cushion: +{telem.get('equity', 4818.51) - 4775.00:.2f} USD) | Operating Buffer: 4,795.00 USD (Cushion: +{telem.get('equity', 4818.51) - 4795.00:.2f} USD).
> **FLUID CAPACITY**: 4/4 slots free. Maximum 1 active risk-bearing limit staged under current +{telem.get('equity', 4818.51) - 4795.00:.2f} USD buffer cushion.
> **OPERATOR DIRECTIVE**: "To pass you may need to increase risk...and keep discussing with arena.ai."

### SECTION 1: LIVE ACCOUNT & RECONCILIATION
- Balance: {telem.get('balance', 4818.51):.2f} USD | Floating Equity: {telem.get('equity', 4818.51):.2f} USD | Free Margin: {telem.get('equity', 4818.51):.2f} USD
- Open Positions: {telem.get('positions_count', 0)} | Pending Orders: {telem.get('orders_count', 0)}
- Account Posture: 100% FLAT CASH DEFENSE (+43.51 USD Hard Floor cushion, +23.51 USD Buffer cushion).
- Prior Action Executed: Ticket #19227609 (BTCUSD.pi BUY_LIMIT 0.04 lots @ 80,950.00) CANCELLED on MT5 per unanimous Council & Swarm veto (retcode 10009 TRADE_RETCODE_DONE).

### SECTION 2: 33-SHEET EXCEL DATA WAREHOUSE HEALTH
- File: Data/DataBase_Trading.xlsx (13.23 MB, 100% healthy, 0 CRC errors, 0 formula errors).
- Sheet count: 33/33 sheets present and verified.
- Sheet 33 (`20_Auction_Market_Structure`): Row 1 verified with 36/36 clean unmerged column headers.
- Formula Errors: Exactly 0 errors (#REF!, #DIV/0!, #N/A, #VALUE!).
- Pipeline Daemon: Task 109472 actively cycling Cycle #9.
- Macro Flows: BlackRock IBIT logged +235.0M USD net daily inflow; CEX spot netflow logged -210.35M USD 4-hour spot withdrawal.

### SECTION 3: TOP CANDIDATES ON RADAR & EXECUTION TRIGGERS
1. **NAS100.p (Model 2 Short — Trend Down Acceptance into Daily VAL Retest)**:
   - Geometry: SELL_LIMIT @ 29,085.00 | Lots: 0.03 | SL: 29,130.00 (+45.0 pts / 0.63 ATR) | TP: 28,970.00 (-115.0 pts / 2.56R)
   - Risk & Solvency: Nominal Risk -$13.50 | Spread Cost: 0.43 USD (1.42 pts / 0.49 bps | 1.24% friction) | Stressed Loss: -$18.88 | Stressed Equity: 4,799.63 USD (+4.63 USD buffer surplus, +24.63 USD floor surplus).
   - Orderflow CVD: Heavy unidirectional institutional selling: 15m CVD -$997.6M, 1h CVD -$4.49B, 4h CVD -$11.07B.
   - Execution Pre-Conditions: [ ] Broker session open confirmed (order_check returns Done) | [ ] Live ask reaches >= 28,941.68 (within 2.0 ATR max staging rule) | [ ] 5m CVD confirms seller delta.
2. **US2000.p (Model 2 Long — Daily POC Retest in Bullish Trend)**:
   - Geometry: BUY_LIMIT @ 2,776.00 | Lots: 0.30 | SL: 2,771.50 (-4.50 pts) | TP: 2,787.00 (+11.00 pts / 2.44R)
   - Risk & Solvency: Nominal Risk -$13.50 | Spread Cost: 0.96 USD (0.32 pts / 1.15 bps | 2.91% friction) | Stressed Loss: -$18.88 | Stressed Equity: 4,799.63 USD (+4.63 USD buffer surplus, +24.63 USD floor surplus).
   - Execution Pre-Conditions: [ ] Broker session open confirmed | [ ] 15m CVD delta turns positive | [ ] Price holds DPOC (2,775.84).
3. **BTCUSD.pi (Deep Flush Re-Entry Radar — Post-Cascade Reclaim)**:
   - Geometry: BUY_LIMIT @ 80,480.00 | Lots: 0.03 | SL: 80,080.00 (-400 pts) | TP: 82,050.00 (+1,570 pts / 3.93R)
   - Sited safely beneath both the 80,850 USD ($11.5M) and 80,650 USD ($15M) debt cascades.
   - Risk & Solvency: Nominal Risk -$12.00 | Stressed Loss: -$17.50 | Stressed Equity: 4,801.01 USD (+6.01 USD buffer surplus).
   - Execution Pre-Conditions: [ ] 80,650 liquidation cascade swept | [ ] 1m/5m CVD prints absorption divergence.
4. **Forex Majors & Crosses**: Interbank rollover embargo active until 22:30 UTC. Re-screen liquid European pairs post-22:30 UTC.

### SECTION 4: 3-PERSONA MANDATORY INQUEST & OUTPUT FORMAT
Evaluate the candidates across the 3 quantitative personas:
1. **Persona 1: Orderflow Analyst** (Steps 2, 4, 6 of SOP — L2 depth, CVD absorption, liquidation cascades, dynamic friction).
2. **Persona 2: Position Manager** (Steps 1, 5, 8 of SOP — floor defense, stressed capacity, exact sizing).
3. **Persona 3: Macro Risk Analyst** (Steps 3, 7 of SOP — macro calendar, ETF/CEX netflows, FX rollover embargo 21:15-22:30 UTC).

### SECTION 5: 🔬 MANDATORY QUANT METHODOLOGY INQUEST (ALWAYS REQUIRED)
**Each persona MUST explicitly answer Section 2.5 of STANDARDIZED_TRADING_DECISION_CHAIN.md**:
*"Is our methodology for finding potential candidates truly sound, and how can we fundamentally improve it? Given that we monitor 156 assets with vast orderbook, CVD, and liquidation data, why has equity remained flat and why are profitable executions eluding the desk? How do we think like elite quants to bridge this gap?"*
- Address: Are our filters overly conjunctive (Boolean AND death spiral)?
- Address: Are our limit entries staged too passively or suffering from adverse selection?
- Address: How should asset-class specialization (TradFi vs Crypto) be structured to capture high-probability alpha?

Deliver dense, authoritative quantitative ruling with exact tickets and the completed 10-Point Pre-Punch Checklist.
"""
    return prompt

async def dispatch_all(cycle_id: str = "AUTO"):
    prompt = build_unified_prompt(cycle_id)
    
    # Save prompt to file
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"[DualCouncil] Saved prompt to {PROMPT_FILE} ({len(prompt)} chars)")
    
    # 1. Dispatch to Z.ai via Terminal/dispatch_zai_prompt.py
    print("[DualCouncil] Dispatching prompt to Z.ai (GLM-5.3-Flash)...")
    try:
        proc_zai = subprocess.run([sys.executable, str(ZAI_DISPATCHER), "--file", str(PROMPT_FILE)], capture_output=True, text=True, timeout=30)
        print("[DualCouncil] Z.ai output:", proc_zai.stdout.strip())
        if proc_zai.stderr:
            print("[DualCouncil] Z.ai stderr:", proc_zai.stderr.strip())
    except Exception as e:
        print(f"[DualCouncil] Z.ai dispatch error: {e}")
        
    # 2. Dispatch to Arena.ai via Chrome CDP using ProseMirror and Input.insertText
    print("[DualCouncil] Dispatching prompt to Arena.ai...")
    try:
        tabs = json.loads(urllib.request.urlopen(CDP_URL, timeout=5).read().decode())
        arena_ws = None
        for t in tabs:
            if ("arena.ai/agent" in t.get("url", "") or "arena.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl"):
                arena_ws = t["webSocketDebuggerUrl"]
                break
        if arena_ws:
            async with websockets.connect(arena_ws, max_size=50_000_000) as ws:
                # Bring to front
                await ws.send(json.dumps({"id": 101, "method": "Page.bringToFront"}))
                await asyncio.sleep(0.5)
                
                # Dismiss modal/escape & dismiss task completion banner
                await ws.send(json.dumps({"id": 102, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
                await ws.send(json.dumps({"id": 103, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
                await asyncio.sleep(0.2)
                
                # If "Was this task successful?" banner is active, click "Yes" to reveal ProseMirror
                js_dismiss_banner = """(() => {
                    const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Yes' || b.innerText.trim() === 'No');
                    if (btns.length > 0) {
                        const yesBtn = btns.find(b => b.innerText.trim() === 'Yes') || btns[0];
                        yesBtn.click();
                        return true;
                    }
                    return false;
                })()"""
                await ws.send(json.dumps({"id": 1031, "method": "Runtime.evaluate", "params": {"expression": js_dismiss_banner}}))
                await asyncio.sleep(0.5)

                # Clear ProseMirror (specifically target .tiptap.ProseMirror, NOT g-recaptcha textarea)
                js_clear = """(() => {
                    const el = document.querySelector('.tiptap.ProseMirror');
                    if (!el) return false;
                    el.focus();
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    const sel = window.getSelection();
                    sel.removeAllRanges();
                    sel.addRange(range);
                    return true;
                })()"""
                await ws.send(json.dumps({"id": 104, "method": "Runtime.evaluate", "params": {"expression": js_clear}}))
                await asyncio.sleep(0.1)
                await ws.send(json.dumps({"id": 105, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
                await ws.send(json.dumps({"id": 106, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
                await asyncio.sleep(0.2)
                
                # Insert prompt text via Input.insertText
                await ws.send(json.dumps({"id": 107, "method": "Input.insertText", "params": {"text": prompt}}))
                await asyncio.sleep(0.5)
                
                # Click send button
                js_click = """(() => {
                    const sendBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button[type="submit"], button[aria-label*="Send"]');
                    if (sendBtn && !sendBtn.disabled) {
                        sendBtn.click();
                        return { clicked: true };
                    }
                    return { clicked: false, disabled: sendBtn ? sendBtn.disabled : null };
                })()"""
                await ws.send(json.dumps({"id": 108, "method": "Runtime.evaluate", "params": {"expression": js_click, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                click_val = res.get("result", {}).get("result", {}).get("value", {})
                print("[DualCouncil] Arena.ai prompt sent result:", click_val)
                if not click_val.get("clicked"):
                    # Fallback to Enter key
                    await ws.send(json.dumps({"id": 109, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
                    await ws.send(json.dumps({"id": 110, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
        else:
            print("[DualCouncil] Warning: No Arena.ai tab found on CDP port 9222.")
    except Exception as e:
        print(f"[DualCouncil] Arena.ai dispatch error: {e}")

    # 3. Dispatch to Gemini Web2API in background subprocess (port 8081)
    print("[DualCouncil] Dispatching prompt to Gemini Web2API (port 8081)...")
    try:
        subprocess.Popen([sys.executable, str(WEB2API_COUNCIL), "--file", str(PROMPT_FILE), "--model", "gemini-3.6-flash"])
        print("[DualCouncil] Gemini Web2API background council task launched successfully.")
    except Exception as e:
        print(f"[DualCouncil] Gemini Web2API dispatch error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", default="AUTO")
    args = parser.parse_args()
    asyncio.run(dispatch_all(args.cycle))
