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
  *(Canonical 12-Step SOP, Section 0.2 Dynamic Capacity N_open + N_pending <= 3 under Drawdown Defense, Section 0.8 Sovereign Final Boss authority & 43-feed serialized candidate extraction)*
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
For each live position and resting order listed in the authoritative registry above, systematically interrogate:
**"Should I let it run or cut it? Is it still a valid trade?"**
- **Active Open Positions**: 0 Active (100% Cash Solvency, Zero open downside risk).
- **Active Resting Pending Maker Limit Orders**:
  1. `NZDUSD.pi` (Ticket #19447583): SELL_LIMIT 0.12 @ 0.56320 | SL: 0.56388 | TP: 0.56050 | Nominal Risk: $8.16 USD | R:R: 3.97:1. (Price is within 15-20 pips; TP hit +$32.40 restores Equity to $4,776.95 USD and reclaims Hard Statutory Floor).
  2. `BTCUSD.pi` (Ticket #19464650): SELL_LIMIT 0.01 @ 80340.00 | SL: 80563.50 | TP: 79663.50 | Nominal Risk: $2.23 USD | R:R: 3.03:1. (Leaning against $15.48M institutional ask wall at 80,392–80,425).
  3. `SP500.p` (Ticket #19444900): PENDING QUARANTINE / PULLED at 11:55 UTC ahead of 12:30 UTC US Advance GDP q/q and Core PCE print. (Re-evaluate post-event once spreads stabilize).

### Mandatory Candidate Discovery Intent:
You MUST execute the two-step sequential candidate audit across the entire 156-asset universe to propose high-confluence maker limit orders. The core operator intent is **NEVER TO MISS ANY TRADING OPPORTUNITY** across Metals, Indices, FX, and Crypto, while strictly leaning against resting whale armor.

---

## 🔬 3. TWO-STEP SEQUENTIAL CANDIDATE SCANNING PIPELINE (STRICTLY ENFORCED)

```mermaid
flowchart TD
    A["156-Asset Universe (00_MT5_Account_Telemetry)"] --> B["STEP 1: Spread Gate Filter (Hard Gate 1)"]
    B -->|Spread > Threshold| C["IMMEDIATE DISQUALIFICATION (Zero wasted compute)"]
    B -->|Spread <= Threshold| D["PASSED CANDIDATES QUEUE (#001 to #096)"]
    
    subgraph Step2 ["STEP 2: SEQUENTIAL ONE-BY-ONE EXTRACTION LOOP"]
        direction TB
        E["Candidate X: Log Start Banner"] --> F["Extract Telemetry from Parquet Feeds"]
        F --> G["Synthesize Auction + CVD + Whales + Max Pain"]
        G --> H["Formulate Mathematical Trade Setup (or Log Stand-Aside)"]
        H --> I["Persist Dossier: docs/dossiers/SYMBOL_360_DOSSIER.md"]
        I --> J["Log Completion Banner for Candidate X"]
        J --> K{"More Candidates in Queue?"}
        K -->|YES: Advance to X+1| E
        K -->|NO| L["Final Tri-Council Trade Staging Registry"]
    end
    
    D --> E
```

### PROTOCOL EXECUTION RULES:
1. **STEP 1 — SPREAD GATE FILTERING FIRST**:
   - Ingest all 156 assets in `00_MT5_Account_Telemetry.parquet`.
   - Apply Gate 1 Spread Cap: TradFi <= 5.0 bps, Crypto <= 12.0 bps, and Friction (Spread / TP_Distance) <= 15.0%.
   - Immediately disqualify any asset exceeding thresholds (e.g. SOLUSD.p 23.96 bps, XRPUSD.pi 23.25 bps, USWTI.p 5.48 bps, XAGUSD.pi 6.80 bps).
2. **STEP 2 — SEQUENTIAL ONE-BY-ONE PARQUET EXTRACTION**:
   For each passed candidate strictly ONE-BY-ONE:
   - Print banner: `>>> [CANDIDATE X/N: SYMBOL] — STARTING INDIVIDUAL PARQUET EXTRACTION`
   - Extract metrics across all Parquet feeds:
     * `11_Technical`: VWAP, Z-score, RSI-14, ATR-14, EMAs.
     * `20_Auction_Market_Structure`: VAH, VAL, POC, Asian/London extremes, Fib OTE 0.702 / Golden Pocket.
     * `18_CVD*`: 5m, 15m, 1h, 4h delta, z-score, absorption.
     * `26_Aggregated_Footprint_Bar_Metrics`: Imbalances, trapped traders (Drop `imbalance_ratio_pct = 300%` as static constant!).
     * `10_Whale_Orders`: Resting whale walls > $100K, duration > 180s (Inspect BOTH Bids and Asks, avoid one-sided traps!).
     * `9_Liquidation_Max_Pain_24H`: Short/Long Max Pain price and distance.
     * `2_Spot_Netflow_S` vs `2_Future_Netflow`: Spot vs Futures netflow divergence.
   - Formulate Trade Parameters:
     * Entry at Sweep Exhaustion Zone (`VAH + 0.35 * ATR_14` or VAL sweep or OTE).
     * Spread-Padded Stop Loss (`SL_short = Resistance + 1.2 * ATR_14 + 1.5 * Spread_Price`).
     * Take Profit at Opposing Value Boundary / Max Pain.
     * Sizing: Nominal Risk strictly <= $10.00 USD, R:R >= 1.50:1 (target >= 2.0:1).
   - Log completion banner: `<<< [CANDIDATE X/N: SYMBOL] EXTRACTION & DOSSIER COMPLETE. PROCEEDING TO NEXT CANDIDATE...`
   - **Only then advance to the next candidate.**

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
- Active Open Positions: (0 Active — Flat, Solvency 100% Protected)
- Resting Pending Maker Limits:
  * NZDUSD.pi (#19447583): [RETAIN / PURGE / ADJUST] — Distance, VAH protection, and Hard Floor restoration path
  * BTCUSD.pi (#19464650): [RETAIN / PURGE / ADJUST] — $15.48M ask wall persistence, CVD delta absorption
  * SP500.p (#19444900): [POST-EVENT QUARANTINE STATUS] — Re-entry parameters post-US GDP/PCE release

## 2. Step 1: Full 156-Asset Spread Gate Audit Summary
- Total Assets Scanned: 156
- Passed Gate 1 (TradFi <= 5.0 bps, Crypto <= 12.0 bps): X assets
- Disqualified Assets: Y assets (with exact reasons: e.g. SOL 23.96 bps, XRP 23.25 bps, USWTI 5.48 bps)

## 3. Step 2: Sequential Candidate-by-Candidate Extraction & Trade Formulations
(Show the individual extraction log for each top passed candidate sequentially before presenting next candidate)
- Candidate 1: [Symbol] -> Technicals, Auction, CVD, Whales, Formulated Trade Card / Stand Aside
- Candidate 2: [Symbol] -> Technicals, Auction, CVD, Whales, Formulated Trade Card / Stand Aside
...
- Candidate N: [Symbol]

## 4. Solvency Defense & Dynamic Capacity Compliance
- Account Equity: $4,744.55 USD | Hard Floor: $4,775.00 USD | Buffer: $4,795.00 USD
- Capacity Check: N_open + N_pending <= 3 slots | Total Staged Risk <= $30.00 USD
- Stressed Solvency Proof: Equity - Stressed Loss >= $4,775.00 USD Hard Floor.

```json
{{
  "cycle_id": "{cycle_id}",
  "timestamp_utc": "{now_utc}",
  "telemetry_commit_sha": "...",
  "account_solvency": {{
    "balance_usd": 4744.55,
    "equity_usd": 4744.55,
    "hard_capital_floor_usd": 4775.00,
    "operating_buffer_usd": 4795.00,
    "active_positions_count": 0,
    "resting_limits_count": 2,
    "total_staged_nominal_risk_usd": 10.39
  }},
  "active_staged_orders": [
    {{"ticket": 19447583, "symbol": "NZDUSD.pi", "action": "RETAIN", "type": "SELL_LIMIT", "volume": 0.12, "entry": 0.56320, "sl": 0.56388, "tp": 0.56050, "nominal_risk_usd": 8.16, "rr": 3.97}},
    {{"ticket": 19464650, "symbol": "BTCUSD.pi", "action": "RETAIN", "type": "SELL_LIMIT", "volume": 0.01, "entry": 80340.00, "sl": 80563.50, "tp": 79663.50, "nominal_risk_usd": 2.23, "rr": 3.03}}
  ],
  "high_confluence_formulated_trades_standby": [...]
}}
```
[END OF REPORT - CYCLE_ID: {cycle_id}]
"""
  * USDCAD (#19448978): [RETAIN / PURGE / ADJUST] - Support liquidity & spread check
  * BNBUSD (#19448979): [RETAIN / PURGE / ADJUST] - Perp liquidation & funding check
  * XAUUSD (#19457311): [RETAIN / PURGE / ADJUST] - Gold Value Area High sweep at 4064.50
  * NAS100 (#19457516): [RETAIN / PURGE / ADJUST] - Tech index resistance sweep at 29,740.00
  * GBPUSD (#19457518): [RETAIN / PURGE / ADJUST] - Cable London sweep at 1.33480

## 2. Spread-Gated Candidate Screening & 43-Feed Forensics (NEW LIMIT OPPORTUNITIES)
*Search full 156 assets across Metals, Indices, FX, Crypto (specifically including deep studies of Crypto Majors BNB, BTC, ETH, SOL, Equity Indices DJ30, SP500, NAS100, Precious Metals XAU, XAG, and FX Majors EUR, GBP, JPY) to propose high-confluence maker limit orders so the desk never misses an opportunity.*

For EACH screened candidate, you MUST output this exact 7-Pillar Forensic Breakdown directly referencing the 43 Parquet Feeds:

### Candidate [Symbol] (e.g., BTCUSD.pi / BNBUSD.p / DJ30.p / XAUUSD.pi)
- **1. Spread & MT5 Telemetry Gate (`00_MT5_Account_Telemetry`)**: 
  * Live Bid / Ask / Mid quotes, Spread Points & Spread (bps) (Crypto <= 12.0 bps, TradFi <= 5.0 bps).
  * Broker Contract Size, Minimum Lot, Tick Value, and Spread Friction % (`Spread / TP_distance <= 15.0%`).
- **2. Auction Market Structure (`20_Auction_Market_Structure`)**:
  * Daily & Weekly VAH, VAL, POC, Session Bias (Bullish/Bearish/Neutral).
  * Fibonacci Retracement Anchor: Swing High / Low, Golden Pocket [0.618-0.650], 0.702 OTE, 0.786 Invalidation.
  * Auction Regime: Rotational Balance vs Trend Expansion.
- **3. Liquidation Cascades & Max Pain Magnet (`9_Liquidation_Max_Pain 24H/48H/3D/7D`, `8_Exchange_Liquidation_Map 1D/7D`, `14_Hyperdash_Liq_Map`, `14_Liquidation_Matrix`)**:
  * Exact Short Max Pain Price & Volume vs Long Max Pain Price & Volume.
  * Major 1D/7D liquidation cascade pools and magnetic sweep zones to avoid placing stops inside.
- **4. Institutional Whale Armor & Depth Skew (`10_Whale_Orders`, `17_Orderbook`)**:
  * Exact resting whale walls (> $100K USD, duration >= 180s persistence, exact exchange Bybit/Binance/OKX, price, side, notional).
  * Top 20 Orderbook Bid/Ask cumulative depth balance (B/A ratio) and defending armor levels.
- **5. Multi-Timeframe CVD Delta & Footprint Absorption (`18_CVD_30D 5m/15m/1h/4h/ALL`, `25_CoinGlass_Footprint_Signals`, `26_Aggregated_Footprint_Bar_Metrics`)**:
  * Cumulative Taker CVD Delta across 5m, 15m, 1h, 4h and orderflow classification (`BEARISH ABSORPTION`, `AGGRESSIVE BUYING`, `DELTA DIVERGENCE`).
  * Footprint Imbalance counts and institutional absorption price levels.
- **6. Derivatives Skew & Macro Netflows (`5_Funding_Rate`, `5_OI`, `3_Exchanges_LS_Ratio 15M/1H/4H`, `1_Crypto_ETF_Flows`, `2_Spot_Netflow_S`, `2_Future_Netflow`)**:
  * Funding Rate across Binance/OKX/Bybit, Total Open Interest and 1h/4h change.
  * Retail Long/Short ratio skew; Spot vs Futures netflow divergence (e.g. Spot buying + Futures selling).
- **7. Exact Algorithmic Trade Formulation**:
  * Model Selection: Model 1 Extreme Mean Reversion (Sweep Fade) vs Model 2 Fibonacci Prime Trend Pullback.
  * Order Type: Passive Maker `BUY_LIMIT` or `SELL_LIMIT`.
  * Limit Entry Price: Mathematical Sweep Exhaustion Zone (`VAH + 0.35 * ATR_14` or Golden Pocket shelf).
  * Spread-Padded Stop Loss: `Resistance + 1.2 * ATR_14 + 1.5 * Spread_Price` (strictly outside retail sweep pockets and behind defending whale armor).
  * Take Profit Target: Opposing Value Area boundary (VAL/VAH), POC, or Max Pain liquidation cascade.
  * Lot Size & Sizing Math: Sized with exact MT5 tick multiplier so nominal risk is strictly `<= $10.00 USD` (stressed `<= $14.00 USD`).
  * Risk/Reward Ratio: Mathematical R:R (Target: `>= 2.0:1`).

Advance sequentially across all candidates using this exact 7-pillar forensic framework!

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
