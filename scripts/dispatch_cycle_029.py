import asyncio
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single, post_prompt_to_zai, get_zai_tab_ws_url

def build_cycle_029_prompt():
    prompt = """# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & TRADE PLAN REVIEW: Cycle_029
**Seat #1: Antigravity Autonomous Lead | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (IST)**: 2026-10-30 14:10:00 IST | **Cycle ID**: `Cycle_029`
**Authoritative Single Source of Truth**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & CAPITAL STATE
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Statutory Hard Floor**: **4,775.00 USD** (Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Deficit: **-31.77 USD**)
- **Capital Regime**: **`TIER_0_DEFENSIVE` (FAIL-CLOSED)**
- **New Market Risk Capacity**: **0.00 USD** (Zero new market risk admitted until equity >= 4,795.00 USD)
- **Dynamic Portfolio Capacity**: $N_{open} + N_{pending} \le 3$
- **Active Open Positions**: **0 Active** (AUDUSD.pi Long #19490051 closed in profit at 0.70282 via ratchet, +0.40 USD net banked)
- **Active Resting Pending Orders**: **5 Live MT5 Pending Tickets** (Contingent Risk = 33.27 USD):
  1. `#19489155`: `BTCUSD.pi` SELL_LIMIT @ 81,084.00 (SL: 81,680.00 | TP: 80,180.00 | Risk: 5.96 USD | R:R = 1.517)
  2. `#19489157`: `BNBUSD.p` SELL_LIMIT @ 753.30 (SL: 761.50 | TP: 743.50 | Risk: 0.41 USD | R:R = 1.195)
  3. `#19489158`: `XAUUSD.pi` SELL_LIMIT @ 4,040.50 (SL: 4,049.50 | TP: 4,018.00 | Risk: 9.00 USD | R:R = 2.500)
  4. `#19489159`: `NAS100.p` SELL_LIMIT @ 29,535.00 (SL: 29,620.00 | TP: 29,320.00 | Risk: 8.50 USD | R:R = 2.529)
  5. `#19489160`: `DJ30.p` SELL_LIMIT @ 52,638.00 (SL: 52,732.00 | TP: 52,402.00 | Risk: 9.40 USD | R:R = 2.511)

---

## 🔬 2. STEP 1 & STEP 2 DOSSIER FORENSICS (ALL 96 ELIGIBLE ASSETS EXAMINED)
Antigravity completed full-length inspection of all 96 eligible asset master dossiers (3.78 MB, 44,727 lines).
- **76 Assets**: Classified as `STAND_ASIDE` due to lack of structural edge or adverse MTF delta.
- **20 Assets**: Candidate passive maker limit setups identified:
  * **Metals**: XAUUSD (Sell Limit @ 4013.29, SL: 4023.27, TP: 3988.34), XAUEUR, XAUAUD, XAUSGD, XAUGBP, XAGSGD
  * **Crypto**: BTCUSD (Sell Limit @ 79210.96, SL: 79652.55, TP: 78106.99), ETHUSD, SOLUSD, BCHUSD, AVEUSD, XRPUSD
  * **Indices**: NAS100 (Sell Limit @ 28858.74, SL: 28921.67, TP: 28701.42), SP500, US2000
  * **Forex**: EURUSD, AUDUSD, GBPUSD, USDJPY (Sell Limit @ 157.61, SL: 157.78, TP: 157.19)
  * **Energy**: USWTI (Sell Limit @ 104.31, SL: 104.71, TP: 103.29)

---

## 📋 MANDATORY TRI-COUNCIL QUESTIONS FOR ARENA.AI & Z.AI:
1. **Resting Orders Disposition**:
   - Ticket #19489155 (BTC) has R:R = 1.517R and Ticket #19489157 (BNB) has R:R = 1.195R — both violate the statutory 2.5R minimum mandate. Do you mandate CANCELing these 2 tickets immediately to comply with the 2.5R rule and bring pending orders closer to capacity $N \le 3$?
   - Should XAUUSD (#19489158), NAS100 (#19489159), and DJ30 (#19489160) remain armed as resting defensive maker limits?
2. **New Candidate Admission**:
   - Under TIER_0_DEFENSIVE (equity 4,763.23 USD < 4,775.00 USD), do you admit ANY new order execution, or mandate 100% fail-closed capital defense?
3. **Cycle_029 Ruling**:
   - Deliver your independent, evidence-grounded recommendation for Cycle_029 including exact action on all 5 resting tickets and capital stance.
"""
    return prompt

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_029 PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)
    
    prompt = build_cycle_029_prompt()
    print(f"Built prompt: {len(prompt)} characters.")
    
    # Get tabs from CDP
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    
    results = {}
    
    # 1. Dispatch Arena.ai
    if arena_tab:
        print(f"\n[1/2] Dispatching to Arena.ai ({arena_tab['url']})...")
        res_arena = await post_prompt_to_arena_single(arena_tab["webSocketDebuggerUrl"], prompt, "Arena.ai")
        results["arena"] = res_arena
        print(f"Arena.ai dispatch result: {'SUCCESS' if res_arena else 'FAILED'}")
    else:
        print("\n[1/2] Arena.ai tab not found on CDP!")
        results["arena"] = False
        
    # 2. Dispatch Z.ai
    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai ({zai_tab['url']})...")
        res_zai = await post_prompt_to_zai(prompt)
        results["zai"] = res_zai
        print(f"Z.ai dispatch result: {'SUCCESS' if res_zai else 'FAILED'}")
    else:
        print("\n[2/2] Z.ai tab not found on CDP!")
        results["zai"] = False

    print("\n" + "=" * 80)
    print("DISPATCH SUMMARY:", results)
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(main())
