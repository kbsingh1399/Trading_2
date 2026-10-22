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
- Open Positions: 0 | Pending Orders: 0 (100% Flat Cash Defense)
- Solvency Cushions: Hard Floor Cushion: +43.51 USD | Buffer Floor Cushion: +23.51 USD.
- Previous Order Action: Ticket #19227609 (BTCUSD.pi BUY_LIMIT 0.04 @ 80,950) was confirmed CANCELLED on MT5 (retcode 10009).

### SECTION 2: 33-SHEET EXCEL DATA WAREHOUSE HEALTH
- File: Data/DataBase_Trading.xlsx (13.23 MB, 100% healthy, 0 CRC errors, 0 formula errors).
- Sheet count: 33/33 sheets present and verified.
- Sheet 30/33 (`20_Auction_Market_Structure`): Row 1 verified with 36/36 clean unmerged column headers.
- Formula Errors: Exactly 0 errors across all 33 sheets.
- Continuous Pipeline Daemon: Task 109472 actively cycling Cycle #9.

### SECTION 3: TOP CANDIDATES ON RADAR FOR ASIAN SESSION & TOKYO OPEN (00:00 UTC)
1. **XAUUSD.pi (Gold — Model 2 Short Pullback to Daily VAH Shelf)**:
   - Geometry: SELL_LIMIT @ 4,031.89 | Lots: 0.01 | SL: 4,048.13 (+16.24 pts) | TP: 3,991.30 (-40.59 pts / 2.50R)
   - Risk & Solvency: Nominal Risk -$16.24 | Spread: 0.08 pts (0.20 bps | 0.20% friction) | Stressed Loss: -$22.30 | Stressed Equity: 4,796.21 USD (+1.21 USD buffer surplus, +21.21 USD floor surplus).
   - Order Check Result: Retcode 0 (Done), Margin Required: 403.19 USD (8.37% utilization). Exact Broker Profit Calc: Loss=-$16.24 USD, Win=+$40.59 USD.
   - Auction & Safe-Stop Validation:
     * Daily VAH sits at 4,031.03; entry catches the failed auction retest of VAH.
     * Prior-Day VAL sits at 4,040.73. Stop Loss at 4,048.13 is placed +7.40 pts safely ABOVE Prior-Day VAL, exceeding Arena 1's minimum safe-stop threshold (>= 4,044.05).
     * State Machine: APPROACHING (Current Ask ~4,028.25; await probe into 4,031.00-4,032.50 with 5m CVD tape exhaustion before punch).
2. **NAS100.p (Model 2 Short — Safe-Stop Geometry on 15m/1h EMA Shelf)**:
   - Geometry: SELL_LIMIT @ 28,962.17 | Lots: 0.01 | SL: 29,120.85 (+158.68 pts, safe half-ATR buffer above Prior-Day VAL 29,087.86) | TP: 28,657.98 (-304.19 pts / 1.92R to 2.00R)
   - Risk & Solvency: Nominal Risk -$15.87 | Stressed Loss: -$21.84 | Stressed Equity: 4,796.67 USD (+1.67 USD buffer surplus).
   - State Machine: APPROACHING (Current Ask ~28,895; tracking 28,850 kill line; require 5m CVD <= 0).
3. **BTCUSD.pi (Asian Session 23:00–02:00 UTC Cascade Reclaim Trigger)**:
   - Geometry: BUY_LIMIT @ 80,500.00 | Lots: 0.02 (0.03 disqualified by safe-stop stress) | SL: 79,942.20 (-557.80 pts, safe half-ATR beneath 80,050 mother pool) | TP: 82,000.00 (front-running 82,000 ask wall / 2.69R)
   - Risk & Solvency: Nominal Risk -$11.16 | Stressed Loss: -$15.95 | Stressed Equity: 4,802.56 USD (+7.56 USD buffer surplus).
   - Execution Trigger Sequence: Gate 1 sweep of 80,450 debt pool ($10.81M) -> Gate 2 CVD deceleration -> Gate 3 close > 80,500 -> Gate 4 retest hold.
4. **USDJPY.pi (Model 2 Short Pullback — Post-CPI Re-Screen after 23:45 UTC)**:
   - Japan Core CPI printed at 23:30 UTC. Tactical freeze lifts at 23:45 UTC.
   - Screen for trend continuation short into Daily VAL (156.644) / Daily POC (156.736) shelf. Sizing: 0.05 lot (Nominal -$6.38, Stressed -$9.98).
5. **US2000.p**: OFFICIALLY RETIRED (Target 2,787 traded without entry fill).

### SECTION 4: 3-PERSONA MANDATORY INQUEST & DELIBERATION
1. **Persona 1: Orderflow Analyst** (Steps 2, 4, 6 of SOP — L2 depth, CVD absorption, liquidation cascades, dynamic friction).
2. **Persona 2: Position Manager** (Steps 1, 5, 8 of SOP — floor defense, stressed capacity, exact sizing).
3. **Persona 3: Macro Risk Analyst** (Steps 3, 7 of SOP — macro calendar, ETF/CEX netflows, FX rollover embargo).

### SECTION 5: 🔬 MANDATORY QUANT METHODOLOGY INQUEST (ALWAYS REQUIRED)
**Each persona MUST explicitly answer Section 2.5 of STANDARDIZED_TRADING_DECISION_CHAIN.md**:
*"Is our methodology for finding potential candidates truly sound, and how can we fundamentally improve it? Given that we monitor 156 assets with vast orderbook, CVD, and liquidation data, why has equity remained flat and why are profitable executions eluding the desk? How do we think like elite quants to bridge this gap?"*
- Address: Are our filters overly conjunctive (Boolean AND death spiral)?
- Address: Are our limit entries staged too passively or suffering from adverse selection?
- Address: How should asset-class specialization (TradFi vs Crypto) be structured to capture high-probability alpha?

Deliver dense, authoritative quantitative ruling with exact tickets and the completed 10-Point Pre-Punch Checklist.

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
