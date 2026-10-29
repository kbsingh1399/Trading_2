"""
Terminal/dispatch_sovereign_cycle.py
Dispatches a Sovereign Cycle Prompt to BOTH Arena.ai and Z.ai via Chrome CDP (port 9222).
Enforces the SOVEREIGN TRI-COUNCIL PERMANENT STANDING CHARTER and candidate-by-candidate 43-feed thinking chain.
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
CDP_URL = "http://127.0.0.1:9222/json"
ZAI_DISPATCHER = ROOT / "Terminal" / "dispatch_zai_prompt.py"
REGISTRY_FILE = ROOT / "Data" / "Manditory" / "LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md"
CHARTER_FILE = ROOT / "Data" / "Manditory" / "COUNCIL_PERMANENT_STANDING_CHARTER.md"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def build_cycle_prompt(cycle_id: str) -> str:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    registry_text = ""
    if REGISTRY_FILE.exists():
        registry_text = REGISTRY_FILE.read_text(encoding="utf-8").strip()

    prompt = f"""# 👑 [SOVEREIGN CYCLE DISPATCH: {cycle_id}]
**Authority**: Antigravity Sovereign Coordinator (MetaTrader 5 Account #5064568)
**Execution Protocol**: SOVEREIGN TRI-COUNCIL PERMANENT STANDING CHARTER
**Timestamp**: {now_utc}

---

## 📚 1. MANDATORY GOVERNANCE INGESTION GATE
You are bound by the SOVEREIGN TRI-COUNCIL PERMANENT STANDING CHARTER.
Before evaluating ANY candidate asset, proposing ANY trade, or outputting ANY cycle verdict, you MUST systematically fetch, read, and enforce the full suite of canonical governance documents directly via their raw GitHub URLs:

- **1. Standardized Trading Decision Chain**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md
  *(Canonical 12-Step SOP, Section 0.8 Sovereign Final Boss authority, Candidate-by-Candidate 43-feed serialized thinking chain, Dynamic Capacity N_open + N_pending <= 3)*
- **2. Live Portfolio & Order Registry**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md
  *(Authoritative real-time state of live positions, ratchets, resting limit orders, and solvency metrics)*
- **3. Tri-Council Collaborative Ledger**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md
  *(Shared cycle memory eliminating silos, cross-referencing peer verdicts)*
- **4. Top 10 Execution Pitfalls & Autopsy**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md
  *(Elimination of 10 lethal traps: ghost walls, sub-ATR stops inside sweep pockets, unabsorbed CVD waterfalls, random-walk fades, spread friction, rollover traps)*
- **5. 32-Sheet Pitfall Avoidance Questions**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md
  *(Exhaustive 35-feed row-by-row interrogation across all 4 strategic groups)*
- **6. Autonomous Wakeup Checklist**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md
  *(156-asset zero-omission screening across 4 macro clusters: Crypto, FX Majors/Crosses, Metals, Indices)*
- **7. Continuous Kaizen Self-Improvement**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md
  *(Zero context amnesia, self-critique loop, zero regression)*

**Mandatory Pre-Cycle Reading Confirmation Header**:
You MUST begin your report with this exact block:
```markdown
### 📚 Mandatory Pre-Cycle Reading Gate Confirmation
✅ All 7 Mandatory Governance Documents Fetched, Read & Enforced via GitHub:
- [x] STANDARDIZED_TRADING_DECISION_CHAIN.md
- [x] LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md
- [x] TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md
- [x] TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md
- [x] 32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md
- [x] AUTONOMOUS_WAKEUP_CHECKLIST.md
- [x] CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md
```

---

## 🏛️ 2. LIVE PORTFOLIO & RESTING ORDERS TELEMETRY
Current snapshot from `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`:
```markdown
{registry_text}
```

### Mandatory Trade Lifecycle Interrogation:
For each live position and resting order, systematically interrogate:
**"Should I let it run or cut it? Is it still a valid trade?"**
- **AUDUSD.pi** (Ticket #19437063): SELL 0.10 @ 0.70586 | Live SL: 0.70506 (+8.0 pips profit lock) | TP: 0.70368
- **USDJPY.pi** (Ticket #19437494): BUY 0.08 @ 157.620 | Live SL: 157.764 (+14.4 pips profit lock) | TP: 158.050
- **US2000.p** (Ticket #19437498): SELL 0.01 @ 2846.50 | Live SL: 2858.00 (Max nominal risk: 1.15 USD) | TP: 2822.00
- **All 9 Active Resting Limit Orders**:
  1. `EURGBP.pi` (#19439188): SELL_LIMIT 0.10 @ 0.83810 | SL: 0.83880 | TP: 0.83680
  2. `SP500.p` (#19444900): BUY_LIMIT 0.02 @ 7705.50 | SL: 7695.50 | TP: 7728.50
  3. `UKBRENT.p` (#19445579): BUY_LIMIT 0.10 @ 114.45 | SL: 113.90 | TP: 115.80
  4. `NZDUSD.pi` (#19447583): SELL_LIMIT 0.12 @ 0.56320 | SL: 0.56388 | TP: 0.56050
  5. `USDCAD.pi` (#19448978): BUY_LIMIT 0.10 @ 1.39720 | SL: 1.39620 | TP: 1.39920
  6. `BNBUSD.p` (#19448979): SELL_LIMIT 0.70 @ 762.50 | SL: 772.50 | TP: 747.00
  7. `XAUUSD.pi` (#19457311): SELL_LIMIT 0.01 @ 4064.50 | SL: 4088.50 | TP: 3995.00
  8. `NAS100.p` (#19457516): SELL_LIMIT 0.01 @ 29740.00 | SL: 30025.00 | TP: 29230.00
  9. `GBPUSD.pi` (#19457518): SELL_LIMIT 0.08 @ 1.33480 | SL: 1.33640 | TP: 1.33120

### Mandatory Candidate Discovery Intent:
You MUST search the entire 156-asset universe to propose MORE potential high-confluence maker limit orders. The core operator intent is **NEVER TO MISS ANY TRADING OPPORTUNITY** across Metals, Indices, FX, and Crypto, while strictly leaning against resting whale armor.

---

## 🔬 3. SPREAD-GATED SCAN & SERIALIZED 43-FEED FORENSICS (CANDIDATE-BY-CANDIDATE)
1. **Spread Gating**: Evaluate 156 assets across 4 clusters. Cap: <= 12.0 bps for Crypto, <= 5.0 bps for TradFi. Reject any failing asset.
2. **Sequential Forensic Deep Dive**: For EVERY spread-qualified candidate, sequentially extract metrics across ALL 43 Parquet feeds:
   - Orderbook depth & defending whale walls (> 100K USD, > 180s persistence).
   - Liquidation cascades (1D/7D maps, Max Pain 24H/48H/3D/7D, Hyperdash Stops).
   - Multi-timeframe CVD delta absorption (5m, 15m, 1h, 4h).
   - Auction Value Area boundaries (VAH, VAL, POC, Asian/London sweep levels).
3. **Formulate Trade Parameters**: Entry at Sweep Exhaustion Zone (`VAH + 0.35 * ATR_14` or VAL sweep), Spread-Padded Stop Loss (`SL_short = Resistance + 1.2 * ATR_14 + 1.5 * Spread_Price`), Take Profit, and Lot Size strictly bounded by <= 10.00 USD risk.
4. **Advance to the next candidate in identical serialized fashion.**

---

## 📋 4. MANDATORY OUTPUT FORMAT
Return your response structured as follows:

# [COUNCIL REPORT - CYCLE_ID: {cycle_id}]
**Council Seat**: [Arena.ai (Lead Quant) / Z.ai (Adversarial Sentry)]
**Timestamp**: {now_utc}

### 📚 Mandatory Pre-Cycle Reading Gate Confirmation
✅ All 7 Mandatory Governance Documents Fetched, Read & Enforced via GitHub:
- [x] STANDARDIZED_TRADING_DECISION_CHAIN.md
- [x] LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md
- [x] TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md
- [x] TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md
- [x] 32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md
- [x] AUTONOMOUS_WAKEUP_CHECKLIST.md
- [x] CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md

## 1. Trade Lifecycle Interrogation ("Should I let it run or cut it?")
- Position 1 (AUDUSD): [HOLD / CUT] - Detailed justification
- Position 2 (USDJPY): [HOLD / CUT] - Detailed justification
- Position 3 (US2000): [HOLD / CUT] - Detailed justification
- Resting Limits (Order-by-Order Forensic Audit of All 9 Limits):
  * EURGBP (#19439188): [RETAIN / PURGE / ADJUST] - Whale order & orderbook persistence
  * SP500 (#19444900): [RETAIN / PURGE / ADJUST] - Value area & auction structure
  * UKBRENT (#19445579): [RETAIN / PURGE / ADJUST] - Energy support & liquidation band
  * NZDUSD (#19447583): [RETAIN / PURGE / ADJUST] - Resistance sweep & CVD delta
  * USDCAD (#19448978): [RETAIN / PURGE / ADJUST] - Support liquidity & spread check
  * BNBUSD (#19448979): [RETAIN / PURGE / ADJUST] - Perp liquidation & funding check
  * XAUUSD (#19457311): [RETAIN / PURGE / ADJUST] - Gold Value Area High sweep at 4064.50
  * NAS100 (#19457516): [RETAIN / PURGE / ADJUST] - Tech index resistance sweep at 29,740.00
  * GBPUSD (#19457518): [RETAIN / PURGE / ADJUST] - Cable London sweep at 1.33480

## 2. Spread-Gated Candidate Screening & 43-Feed Forensics (NEW LIMIT OPPORTUNITIES)
*Search full 156 assets across Metals, Indices, FX, Crypto to propose MORE potential limit orders so the desk never misses an opportunity.*
### Candidate A: [Symbol]
- Spread Audit: [Pass / Fail] (X.X bps)
- 43-Feed Forensic Synthesis: (Whale Orders, Liquidations, CVD, Auction Value Area)
- Formulated Trade: [BUY_LIMIT / SELL_LIMIT] @ Price | SL: Price | TP: Price | Risk: $X.XX

### Candidate B: [Symbol]
- ... (Same serialized structure)

## 3. Solvency & Risk Vetting
- Capital Floor Defense: Hard Floor $4,775.00 USD | Operating Buffer $4,795.00 USD
- Stressed Loss Verification: Stressed portfolio drawdown strictly within budget.

# [END OF REPORT - CYCLE_ID: {cycle_id}]
"""
    return prompt


async def dispatch_to_arena(prompt: str) -> bool:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode()
        tabs = json.loads(raw)
        arena_ws = None
        for t in tabs:
            if ("arena.ai/agent" in t.get("url", "") or "arena.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl"):
                arena_ws = t["webSocketDebuggerUrl"]
                break
        if not arena_ws:
            print("[DispatchCycle] Error: Arena.ai tab not found on CDP port 9222.")
            return False

        async with websockets.connect(arena_ws, max_size=50_000_000) as ws:
            await ws.send(json.dumps({"id": 101, "method": "Page.bringToFront"}))
            await asyncio.sleep(0.5)

            # Dismiss modal/escape
            await ws.send(json.dumps({"id": 102, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
            await ws.send(json.dumps({"id": 103, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
            await asyncio.sleep(0.2)

            # Dismiss 'Was this task successful?' banner
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

            # Clear ProseMirror
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

            # Insert prompt in chunks
            chunk_size = 2000
            for idx in range(0, len(prompt), chunk_size):
                chunk = prompt[idx:idx + chunk_size]
                await ws.send(json.dumps({"id": 107, "method": "Input.insertText", "params": {"text": chunk}}))
                await asyncio.sleep(0.04)
            await asyncio.sleep(0.5)

            # Click send
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
            print(f"[DispatchCycle] Arena.ai send result: {click_val}")
            if not click_val.get("clicked"):
                await ws.send(json.dumps({"id": 109, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
                await ws.send(json.dumps({"id": 110, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
            return True
    except Exception as e:
        print(f"[DispatchCycle] Arena.ai error: {e}")
        return False


def dispatch_to_zai(prompt_file_path: pathlib.Path) -> bool:
    try:
        proc = subprocess.run(
            [sys.executable, str(ZAI_DISPATCHER), "--file", str(prompt_file_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        print(f"[DispatchCycle] Z.ai output: {proc.stdout.strip()}")
        if proc.stderr:
            print(f"[DispatchCycle] Z.ai stderr: {proc.stderr.strip()}")
        return proc.returncode == 0
    except Exception as e:
        print(f"[DispatchCycle] Z.ai error: {e}")
        return False


async def main():
    parser = argparse.ArgumentParser(description="Dispatch Sovereign Cycle Prompt to Arena.ai & Z.ai")
    parser.add_argument("--cycle", required=True, help="Unique cycle ID (e.g. Cycle_004)")
    args = parser.parse_args()

    cycle_id = args.cycle
    prompt = build_cycle_prompt(cycle_id)

    prompt_file = ROOT / "docs" / "trade_plans" / f"{cycle_id}_DISPATCH_PROMPT.txt"
    latest_file = ROOT / "docs" / "trade_plans" / "LATEST_COUNCIL_CYCLE_PROMPT.txt"
    prompt_file.parent.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt, encoding="utf-8")
    latest_file.write_text(prompt, encoding="utf-8")
    print(f"[DispatchCycle] Prompt written to {prompt_file} ({len(prompt)} chars)")

    # 1. Dispatch to Z.ai
    print(f"[DispatchCycle] Sending prompt to Z.ai for {cycle_id}...")
    z_ok = dispatch_to_zai(prompt_file)

    # 2. Dispatch to Arena.ai
    print(f"[DispatchCycle] Sending prompt to Arena.ai for {cycle_id}...")
    a_ok = await dispatch_to_arena(prompt)

    print(f"[DispatchCycle] Dispatch completed: Z.ai={z_ok}, Arena={a_ok}")
    if not (z_ok and a_ok):
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
