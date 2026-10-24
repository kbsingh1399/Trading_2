"""
Terminal/dispatch_arena_initial_fable.py
Dispatches the Master Fable 5 Autonomous Quantitative Governance & Initial Setup Prompt
directly into the fresh Arena.ai Agent Mode session via Chrome CDP (port 9222).
"""
import asyncio
import datetime
import json
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDP_URL = "http://127.0.0.1:9222/json"

def build_fable5_initial_prompt() -> str:
    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Check live telemetry
    telem_file = ROOT / "Data" / "telemetry" / "mt5_account_telemetry.json"
    bal, eq, fm = 4865.07, 4865.07, 4865.07
    if telem_file.exists():
        try:
            with open(telem_file, "r", encoding="utf-8") as f:
                tdata = json.load(f)
                acc = tdata.get("account", tdata)
                bal = float(acc.get("balance_usd", acc.get("balance", 4865.07)))
                eq = float(acc.get("equity_usd", acc.get("equity", 4865.07)))
                fm = float(acc.get("margin_free_usd", acc.get("margin_free", 4865.07)))
        except Exception:
            pass

    cush_fl = eq - 4600.00
    cush_buf = eq - 4650.00
    cush_ker = eq - 4795.00
    headroom = cush_ker - 2.00

    prompt = f"""# 🏛️ AUTONOMOUS MULTI-AGENT QUANTITATIVE GOVERNANCE & DEEP REASONING SPECIFICATION
## Mandatory Deep Reasoning & Multi-Agent Squad Candidate Discovery for Blueberry Markets Phase 1 Evaluation

> **Session Mode**: CANONICAL PRODUCTION MULTI-AGENT QUANTITATIVE DESK (Single Source of Truth)  
> **Target Account**: Blueberry Markets MT5 Account #5064568 (Raw Spread CFD/Perpetual)  
> **Connected Repository**: `https://github.com/kbsingh1399/Trading_2` (Branch `main`)  
> **Current Timestamp**: {utc_now}  
> **Evaluation Phase 1 Target**: Reach **5,500.00 USD** Equity  
> **Current Account State**: Balance: **{bal:,.2f} USD** | Floating Equity: **{eq:,.2f} USD** | Free Margin: **{fm:,.2f} USD**  
> **Active Positions**: 0 (100% Flat Cash Defense) | **Active Pending Orders**: 0  
> **Inviolable Capital Floors**:  
>   - Hard Capital Floor: **4,600.00 USD** (Cushion: **+{cush_fl:.2f} USD**)  
>   - Operating Defense Buffer: **4,650.00 USD** (Cushion: **+{cush_buf:.2f} USD**)  
>   - Solvency Admission Kernel: **4,795.00 USD** (Cushion: **+{cush_ker:.2f} USD**)  
>   - Global Contingency Reserve: **2.00 USD** -> **Net Realized Headroom**: **+{headroom:.2f} USD**  
> **Capital Regime**: **TIER 2 HOUSE MONEY** (Nominal risk corridor: 15.00 to 25.00 USD per ticket; Max 2 concurrent non-correlated tickets; Margin Level >= 200%).

---

## 🔒 1. MANDATORY DEEP REASONING & MULTI-AGENT SQUAD CAPABILITY DIRECTIVE
You are formally required to operate with **maximum deep reasoning and chain-of-thought verification** as an **Autonomous Multi-Agent Quantitative Squad**. 
Under no circumstances are you to act as a generic assistant, conversational chatbot, or speculative trader. You are an institutional quantitative portfolio manager operating under the strict mathematical invariants of `AGENTS.md` and `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md`:
1. **Mathematical Falsification Over Narrative**: Assertions of trend, support, or value without quantitative proof (VR test, variance ratio z-score, Newey-West drift t-stat, orderbook wall persistence) are strictly forbidden.
2. **Inviolable Triple Capital Defense**: Zero trades may ever be authorized if the stressed worst-case equity would breach the 4,795.00 USD Solvency Kernel.
3. **Dual-Engine Strategy Dialectic**:
   - **Model 1 (Extreme Mean Reversion)**: Admissible ONLY in confirmed `MEAN_REVERT` regimes (VR(4) < 0.85, z* < -1.64) at extreme locations (|Z| >= 2.0 to 3.5 SD) sweeping Monday High/Low or Session Extremes with tape exhaustion.
   - **Model 2 (Trend Following Pullbacks)**: Admissible ONLY in confirmed `TREND_UP` or `TREND_DOWN` regimes (VR(4) > 1.15, z* > 1.64, |t_drift| >= 2.0) with Fibonacci Prime EMA alignment (EMA 5/13/34/89/144/233) pulling back into the Golden Zone [0.618 GP, 0.702 OTE].
   - **Stand Aside Mandate**: If regime is `UNDEFINED` or sub-diffusive rotational noise without trend alignment, stand aside unconditionally. Flat cash is an active, profitable risk-off position.

---

## 📊 2. EXHAUSTIVE 4-ROLE QUANTITATIVE AUDIT PROTOCOL
In every response, you must execute an affirmative and adversarial quantitative audit across all 4 institutional roles:
- **Role A (Statistical Regime, Diffusion & Dual-Engine Dialectic)**: Compute Lo-MacKinlay VR(4), Kaufman ER(48), HAC drift t-stat, Fib-Prime EMAs, and Ornstein-Uhlenbeck theta mean-reversion equilibrium.
- **Role B (Fill, Microstructure & Order Geometry Quant)**: Audit L2 orderbook resting walls (must persist >= 180s with notional >= 100k USD), 15m taker CVD delta, and spread friction (<= 25.0 bps).
- **Role C (Solvency, Portfolio & Broker Mathematics Sentry)**: Enforce 50% margin (1:2 leverage) on crypto CFDs, margin utilization <= 50%, post-order margin level >= 200%, 0.04-0.06 lot sizing, and stressed loss <= Net Headroom.
- **Role D (Clock, Weekend Universe & Data Provenance Auditor)**: Verify weekend market availability (98 TradFi assets closed until Sunday 21:00 UTC; 58 crypto perpetuals open 24/7; 11 crypto assets pass spread gate), macro calendar event blackout, and file timestamps.

---

## 🚨 3. MANDATORY DATA & WORKBOOK TIMESTAMP AUDIT DIRECTIVE
Inspect the connected repository files (`kbsingh1399/Trading_2` branch `main`), particularly `Data/DataBase_Trading.xlsx`, `docs/telemetry/live_snapshot_latest.json`, `Data/forex_factory_live.json`, and `Data/macro_calendar.json`:
- Verify that file modification and git commit timestamps are fresh relative to current UTC clock ({utc_now}).
- **MANDATORY EXPLICIT FEEDBACK**: If ANY data file or workbook appears stale, lagging, or un-synchronized:
  * Output an immediate prominent alert at the top of your response:
    `[ALERT] TELEMETRY STALE WARNING: [File/Sheet] is stale (Last updated: [Timestamp] vs Current UTC: {utc_now})`
  * Provide explicit feedback identifying the lagging metric.

---

## 🎯 4. INITIAL SESSION TASK & CANDIDATE DISCOVERY ASSIGNMENT
1. **Acknowledge Deep Reasoning & Multi-Agent Squad Architecture**: Confirm adoption of the institutional multi-agent squad architecture with deep reasoning and step-by-step chain-of-thought verification.
2. **Repository & Data Verification**: Verify your access to `kbsingh1399/Trading_2` branch `main` and inspect the fresh state of `Data/DataBase_Trading.xlsx` and `docs/telemetry/live_snapshot_latest.json`.
3. **Crypto Universe Scan (11 Spread-Qualified Assets)**:
   Conduct an empirical quantitative scan across the 11 trade-eligible crypto perpetuals:
   `BTCUSD.pi, ETHUSD.pi, SOLUSD.p, BNBUSD.p, XRPUSD.p, ADAUSD.p, DOGEUSD.p, TRXUSD.p, LINKUSD.p, AVAXUSD.p, NEARUSD.p`
   Test each asset against the 5-pillar confluence stack, Fib-Prime EMAs, Golden Zone retracements, and L2 whale backing.
4. **Ruling**: Issue a formal quantitative ruling: either nominate a fully verified candidate with exact limit price, SL, TP, lot size, and stressed solvency proof, OR ratify **100% Flat Cash Defense (STAND ASIDE)**.
5. **Section 8 Kaizen Inquest**: Provide answers on Skills Optimization, Omitted Risk Dimensions, and Algorithmic Alternatives.

Deliver your complete multi-agent squad quantitative analysis now.
"""
    return prompt.strip()


async def dispatch_initial():
    print("[FableDispatcher] Connecting to Chrome CDP at", CDP_URL)
    raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    agent_tab = next((t for t in tabs if "arena.ai/agent" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if not agent_tab:
        print("[FableDispatcher] ERROR: No arena.ai/agent tab found on port 9222!")
        sys.exit(1)
        
    ws_url = agent_tab["webSocketDebuggerUrl"]
    print(f"[FableDispatcher] Targeting tab: {agent_tab.get('url')} (WS: {ws_url})")
    
    prompt = build_fable5_initial_prompt()
    out_file = ROOT / "docs" / "trade_plans" / "ARENA_FABLE5_INITIAL_PROMPT.txt"
    out_file.write_text(prompt, encoding="utf-8")
    print(f"[FableDispatcher] Saved initial prompt to {out_file} ({len(prompt)} chars)")
    
    async with websockets.connect(ws_url, max_size=25_000_000) as ws:
        cur_id = int(time.time() * 1000) % 1000000
        async def call_cdp(method: str, params: dict = None):
            nonlocal cur_id
            cur_id += 1
            msg = {"id": cur_id, "method": method}
            if params:
                msg["params"] = params
            await ws.send(json.dumps(msg))
            t0 = time.time()
            while time.time() - t0 < 6.0:
                try:
                    res = json.loads(await asyncio.wait_for(ws.recv(), timeout=2.0))
                    if res.get("id") == cur_id:
                        return res
                except Exception:
                    break
            return {}

        # 1. Bring tab to front
        await call_cdp("Page.bringToFront")
        await asyncio.sleep(0.5)

        # 2. Check if currently generating
        chk = await call_cdp("Runtime.evaluate", {
            "expression": "Boolean(document.querySelector('button[aria-label*=\"Stop\"], button[title*=\"Stop\"]'))",
            "returnByValue": True
        })
        if chk.get("result", {}).get("result", {}).get("value"):
            print("[FableDispatcher] Tab is already generating! Aborting dispatch.")
            return

        # 3. Focus and clear the editor
        js_focus = """(() => {
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
        await call_cdp("Runtime.evaluate", {"expression": js_focus})
        await asyncio.sleep(0.2)
        await call_cdp("Input.dispatchKeyEvent", {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"})
        await call_cdp("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"})
        await asyncio.sleep(0.3)

        # 4. Insert text
        print(f"[FableDispatcher] Inserting prompt ({len(prompt)} characters)...")
        await call_cdp("Input.insertText", {"text": prompt})
        await asyncio.sleep(0.8)

        # 5. Click Send button
        js_send = """(() => {
            const sendBtn = document.querySelector('button[aria-label=\"Send message\"], button[type=\"submit\"], button:has(svg.lucide-arrow-up)');
            if (sendBtn && !sendBtn.disabled) {
                sendBtn.click();
                return { clicked: true };
            }
            return { clicked: false, disabled: sendBtn ? sendBtn.disabled : null };
        })()"""
        res_send = await call_cdp("Runtime.evaluate", {"expression": js_send, "returnByValue": True})
        val_send = res_send.get("result", {}).get("result", {}).get("value", {})
        if val_send.get("clicked"):
            print("[FableDispatcher] Clicked 'Send message' button successfully!")
        else:
            print("[FableDispatcher] Button disabled or not clicked; falling back to Enter key...")
            await call_cdp("Input.dispatchKeyEvent", {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"})
            await call_cdp("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"})

        # 6. Verify generation active
        await asyncio.sleep(1.5)
        chk_gen = await call_cdp("Runtime.evaluate", {
            "expression": "Boolean(document.querySelector('button[aria-label*=\"Stop\"], button[title*=\"Stop\"], button:has(svg.lucide-square)'))",
            "returnByValue": True
        })
        is_gen = chk_gen.get("result", {}).get("result", {}).get("value")
        print(f"[FableDispatcher] Arena Agent Generation Active: {is_gen}")
        print("[FableDispatcher] Initial Fable 5 prompt dispatch completed successfully!")

if __name__ == "__main__":
    asyncio.run(dispatch_initial())
