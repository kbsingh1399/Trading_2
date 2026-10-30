import asyncio
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single, post_prompt_to_zai

sys.stdout.reconfigure(encoding='utf-8')

# Load the 93 examined assets from Step 2
with open(ROOT / 'docs' / 'trade_plans' / 'CYCLE_030_DOSSIER_FORENSICS_ALL_93.json', 'r', encoding='utf-8') as f:
    forensics = json.load(f)

# Group by sector
by_sector = {}
for item in forensics:
    sec = item['sector']
    if sec not in by_sector: by_sector[sec] = []
    by_sector[sec].append(item)

def format_sector_table(items):
    lines = ["| Symbol | Bid / Ask | Spread (bps) | VAH | VAL | POC | Section 10 Setup | Posture |",
             "|---|---|---|---|---|---|---|---|"]
    for i in items:
        sym = i['symbol']
        quote = f"{i['bid']} / {i['ask']}"
        spread = f"{i['spread_bps']:.2f}"
        vah, val, poc = i['vah'], i['val'], i['poc']
        if i['decision'] == 'PASSIVE_MAKER_LIMIT_ARMED':
            card = f"Short @ {i['entry_short']} (SL: {i['sl_short']}, TP: {i['tp_short']})"
        else:
            card = "Stand Aside"
        lines.append(f"| `{sym}` | {quote} | {spread} | {vah} | {val} | {poc} | {card} | **`{i['decision']}`** |")
    return "\n".join(lines)

def build_cycle_030_prompt():
    crypto_tbl = format_sector_table(by_sector.get('Crypto Perpetuals & CFDs', []))
    metals_tbl = format_sector_table(by_sector.get('Precious & Industrial Metals', []))
    indices_tbl = format_sector_table(by_sector.get('Equity Indices', []))
    energy_tbl = format_sector_table(by_sector.get('Energy & Commodities', []))
    # For FX, show top 20 tightest spreads to keep prompt size efficient
    fx_items = sorted(by_sector.get('Forex Majors & Crosses', []), key=lambda x: x['spread_bps'])[:20]
    fx_tbl = format_sector_table(fx_items)

    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & UNIVERSE REVIEW: Cycle_030
**Seat #1: Antigravity Autonomous Lead | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (IST)**: 2026-10-30 14:25:00 IST | **Cycle ID**: `Cycle_030`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Hard Solvency Floor**: **4,775.00 USD** (Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Deficit: **-31.77 USD**)
- **Capital Regime**: **`TIER_0_DEFENSIVE` (FAIL-CLOSED)**
- **New Market Risk Capacity**: **0.00 USD** (Zero new market orders admitted)
- **Dynamic Portfolio Capacity**: $N_{{open}} + N_{{pending}} \\le 3$
- **Broker Actions Executed**:
  * **Ticket #19489155 (BTCUSD.pi)**: **CANCELLED ON MT5** (retcode 10009). R:R was 1.517R (< 2.5R mandate).
  * **Ticket #19489157 (BNBUSD.p)**: **CANCELLED ON MT5** (retcode 10009). R:R was 1.195R (< 2.5R mandate).
- **Active Running Positions**: **0 ACTIVE**
- **Remaining Live Resting Pending Orders (Exactly 3 Tickets, Risk = 26.90 USD)**:
  1. `#19489158`: `XAUUSD.pi` SELL_LIMIT @ 4,040.50 | SL: 4,049.50 | TP: 4,018.00 | Risk: 9.00 USD | R:R = 2.500
  2. `#19489159`: `NAS100.p` SELL_LIMIT @ 29,535.00 | SL: 29,620.00 | TP: 29,320.00 | Risk: 8.50 USD | R:R = 2.529
  3. `#19489160`: `DJ30.p` SELL_LIMIT @ 52,638.00 | SL: 52,732.00 | TP: 52,402.00 | Risk: 9.40 USD | R:R = 2.511

---

## 🔬 2. STEP 1 & STEP 2 DOSSIER FORENSICS ACROSS ALL ELIGIBLE SECTORS
All 400 dossiers refreshed at 14:23:35 IST directly from 43 Parquet feeds via Sovereign Dossier Engine v3.3.

### 🪙 Crypto Perpetuals & CFDs (All 11 Assets):
{crypto_tbl}

### 🥇 Precious & Industrial Metals (All 9 Assets):
{metals_tbl}

### 📈 Global Equity Indices (All 13 Assets):
{indices_tbl}

### 🛢️ Energy & Commodities (All 2 Assets):
{energy_tbl}

### 💱 Forex Majors & Crosses (Top 20 of 58 Assets):
{fx_tbl}

---

## 📋 MANDATORY INSTRUCTIONS & DELIVERABLES FOR ARENA.AI & Z.AI:
1. **Universe Forensic Review**: Individually interrogate the eligible candidates across Crypto, Metals, Indices, and Forex using the data above and full dossiers on GitHub (`docs/dossiers/<ASSET>_MASTER_DOSSIER.md`).
2. **Resting Tickets Disposition**: Evaluate the 3 remaining resting orders (XAUUSD #19489158, NAS100 #19489159, DJ30 #19489160). Confirm whether to RETAIN or CANCEL under TIER_0_DEFENSIVE.
3. **Capital Stance**: Confirm 100% fail-closed capital defense (0.00 USD new risk) until account recovers above 4,775.00 USD hard floor.
"""
    return prompt

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_030 UNIVERSE FORENSIC PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)
    
    prompt = build_cycle_030_prompt()
    print(f"Built Cycle_030 prompt: {len(prompt)} characters.")
    
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    
    results = {}
    
    # 1. Arena.ai
    if arena_tab:
        print(f"\n[1/2] Dispatching to Arena.ai ({arena_tab['url']})...")
        res_arena = await post_prompt_to_arena_single(arena_tab["webSocketDebuggerUrl"], prompt, "Arena.ai")
        results["arena"] = res_arena
        print(f"Arena.ai dispatch result: {'SUCCESS' if res_arena else 'FAILED'}")
    else:
        results["arena"] = False
        
    # 2. Z.ai
    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai ({zai_tab['url']})...")
        res_zai = await post_prompt_to_zai(prompt)
        results["zai"] = res_zai
        print(f"Z.ai dispatch result: {'SUCCESS' if res_zai else 'FAILED'}")
    else:
        results["zai"] = False

    print("\n" + "=" * 80)
    print("CYCLE_030 DISPATCH SUMMARY:", results)
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(main())
