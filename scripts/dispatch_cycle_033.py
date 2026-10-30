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

with open(ROOT / 'docs' / 'trade_plans' / 'CYCLE_033_DOSSIER_FORENSICS_ALL_94.json', 'r', encoding='utf-8') as f:
    forensics = json.load(f)

items = list(forensics.values())

def build_cycle_033_prompt():
    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & UNIVERSE REVIEW: Cycle_033
**Seat #1: Antigravity Autonomous Lead | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (UTC)**: 2026-10-30 11:10:00 UTC (16:40:00 IST) | **Cycle ID**: `Cycle_033`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`
**Canonical Checklist**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Hard Solvency Floor**: **4,775.00 USD** (Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Deficit: **-31.77 USD**)
- **Capital Posture**: `TIER_0_DEFENSIVE` (Operator Override Active for High-Confluence Maker Limits $\\ge 2.5R$, Risk $\\le 10.00$ USD, Capacity $N \\le 3$)
- **Active Open Positions**: **0** (100% Cash Defense)
- **Active Resting Maker Limit Orders**: **3** (Current Capacity: **3/3 Slots Utilized**)
  1. **Ticket #19520222**: `BTCUSD.pi` SELL_LIMIT 0.02 lot @ **78,962.00** | SL **79,318.00** | TP **78,072.00** | Risk **$7.12 USD** | **2.500R**
     - Live Ask: `77,597.00` | Sits 1,365 pts above market, resting above daily VAH `78,646.96` and protected by $25.38M ask wall at 78,677.00.
  2. **Ticket #19520223**: `XAUUSD.pi` SELL_LIMIT 0.01 lot @ **4,007.50** | SL **4,017.00** | TP **3,983.70** | Risk **$9.50 USD** | **2.505R**
     - Live Ask: `3,980.30` | Sits 27.20 pts above market, defending daily VAH `4,006.65` and Model 1 Short Candidate Entry.
  3. **Ticket #19520224**: `AUDUSD.pi` BUY_LIMIT 0.15 lot @ **0.70240** | SL **0.70180** | TP **0.70390** | Risk **$9.00 USD** | **2.500R**
     - Live Bid: `0.70394` | Sits 15.4 pips below market, waiting at daily VAL `0.70240` sweep.
- **Total Combined Downside Risk**: **$25.62 USD** (All tickets strictly $\\le 10.00$ USD risk).

---

## 🔍 2. UNIVERSE DOSSIER FORENSICS (ALL 94 SPREAD-PASSING ASSETS AUDITED)
- In Cycle_033 Step 2, Antigravity physically opened and scanned **100% of all 94 eligible dossiers to EOF** (48,251 lines, 4,347,004 bytes / 4.15 MB, zero byte skipping, zero line caps).
- Macro Distribution:
  * Crypto Perpetuals & CFDs: 9 pairs (BTC, ETH, BCH, AVE, XLM, YFI, XMR, ZEC, DSH)
  * Precious & Base Metals: 8 pairs (XAUUSD, XAUEUR, XAUGBP, XAUAUD, XAUCNH, XAUSGD, XAGAUD, XAGSGD)
  * Global Equity Indices: 13 indices (DJ30, NAS100, SP500, GER40, UK100, JP225, etc.)
  * Forex Majors & Liquid Crosses: 64 pairs
- All 94 assets currently stand aside for new market orders as portfolio capacity is fully staged ($3/3$ slots).

---

## 🎯 3. MANDATORY TRI-COUNCIL AUDIT DELIVERABLES
Arena.ai and Z.ai are instructed to independently deliver:
1. **Resting Limit Orders Audit**:
   - Evaluate Ticket #19520222 (BTCUSD.pi 78,962.00 SELL_LIMIT). Confirm if VAH level, +2.51σ VWAP band, and ask wall defense remain valid. Recommendation: `MAINTAIN` or `CANCEL`.
   - Evaluate Ticket #19520223 (XAUUSD.pi 4,007.50 SELL_LIMIT). Confirm if VAH resistance at 4,006.65 remains valid. Recommendation: `MAINTAIN` or `CANCEL`.
   - Evaluate Ticket #19520224 (AUDUSD.pi 0.70240 BUY_LIMIT). Confirm if VAL sweep at 0.70240 remains valid. Recommendation: `MAINTAIN` or `CANCEL`.
2. **Friday Rollover & Weekend Blackout Guidance**:
   - Assess rollover window (21:15–22:30 UTC) and weekend gap risk for resting orders.
3. **Definitive Solvency Verdict**:
   - Ratify whether current $N=3$ resting limit stance ($25.62 USD risk) preserves the $4,775.00 USD solvency floor while effectively positioning for high-probability mean-reversion fills.
"""
    return prompt

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_033 UNIVERSE FORENSIC PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)

    prompt = build_cycle_033_prompt()
    prompt_path = ROOT / "docs" / "trade_plans" / "CYCLE_033_DISPATCH_PROMPT.txt"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")
    print(f"Saved Cycle_033 prompt ({len(prompt)} chars) to {prompt_path}")

    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)

    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)

    results = {}

    if arena_tab:
        print(f"\n[1/2] Dispatching to Arena.ai ({arena_tab['url']})...")
        res_arena = await post_prompt_to_arena_single(arena_tab["webSocketDebuggerUrl"], prompt, "Arena.ai")
        results["arena"] = res_arena
        print(f"Arena.ai dispatch result: {'SUCCESS' if res_arena else 'FAILED'}")
    else:
        print("Warning: Arena.ai tab not found on port 9222.")
        results["arena"] = False

    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai ({zai_tab['url']})...")
        res_zai = await post_prompt_to_zai(prompt)
        results["zai"] = res_zai
        print(f"Z.ai dispatch result: {'SUCCESS' if res_zai else 'FAILED'}")
    else:
        print("Warning: Z.ai tab not found on port 9222.")
        results["zai"] = False

    print("\n" + "=" * 80)
    print("CYCLE_033 DISPATCH SUMMARY:", results)
    print("=" * 80)

if __name__ == '__main__':
    asyncio.run(main())
