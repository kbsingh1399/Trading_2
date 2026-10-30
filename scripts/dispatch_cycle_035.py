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

# Load the Cycle_035 Full-Scale Universe Database
db_path = ROOT / 'docs' / 'trade_plans' / 'CYCLE_035_FULL_SCALE_UNIVERSE_DATABASE.json'
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

top_candidates = db.get('top_actionable_candidates', [])
eligible_count = db.get('total_eligible_assets', 93)

def build_cycle_035_prompt():
    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & TRADE COLLABORATION: Cycle_035
**Seat #1: Antigravity Autonomous Lead & Broker Desk | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (UTC)**: 2026-10-30 13:22:00 UTC (18:52:00 IST) | **Cycle ID**: `Cycle_035`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`
**Canonical Checklist**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`

> ⚠️ **CRITICAL OUTPUT FORMATTING MANDATE FOR ARENA.AI & Z.AI**:
> **PRINT YOUR COMPLETE EVALUATION, AUDIT FINDINGS, CANDIDATE SETUPS, AND VERDICTS ALL-IN-ONE DIRECTLY INSIDE THIS SINGLE CHAT RESPONSE.**
> **DO NOT CREATE, REFERENCE, OR DELEGATE TO ANY EXTERNAL ATTACHMENTS, SIDECAR JSONs, SEPARATE .MD FILES, OR DOWNLOAD DIRECTORIES. EVERYTHING MUST BE EXPLICITLY AND FULLY PRINTED INLINE IN THIS SINGLE OUTPUT.**

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Margin Used**: **0.00 USD** | **Free Margin**: **4,763.23 USD**
- **Hard Solvency Floor**: **4,775.00 USD** (Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Deficit: **-31.77 USD**)
- **Capital Posture**: `TIER_0_DEFENSIVE` (Operator Override Active for High-Confluence Maker Limits >= 2.5R, Risk <= 10.00 USD, Capacity N <= 3)
- **Active Open Positions**: **0** (100% Cash Defense Preserved)
- **Active Resting Maker Limit Orders**: **0** (All prior orders cleanly cancelled with retcode=10009 in Cycle_034)
- **Total Contingent Downside Risk**: **0.00 USD** (Full capacity 0/3 available for new high-confluence staging)

---

## 🔍 2. UNIVERSE FORENSICS & SPREAD-CLEARED ASSET POOL ({eligible_count} ASSETS)
In Cycle_035, exactly {eligible_count} assets cleared broker spread gates (TradFi <= 5.0 bps, Crypto <= 25.0 bps).
All individual JSON dossiers are hosted at:
`https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/dossiers/{{SYMBOL}}_MASTER_DOSSIER.json`
Unified Cache: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/dossiers/ALL_MASTER_DOSSIERS.json`

### Antigravity's Formulated High-Confluence Setups:
1. **XAUUSD** (`XAUUSD.pi` | Precious Metal | Spread: 0.41 bps | Score: 85.0/100)
   - Live Mid: `3,965.45` | VAL: `3,979.17` | POC: `3,992.40` | VAH: `4,009.00` | VWAP: `3,993.54`
   - Liquidation: Short Max Pain `4,042.73` (+2.56%) | Long Max Pain `3,883.52` (-1.48%)
   - Setup: BUY_LIMIT @ `3,948.50` | SL `3,939.50` (9.00 pts, outside retail stop cluster) | TP `3,971.00` | **2.500R** | Risk: **$9.00 USD** (0.01 lot)
2. **BTCUSD** (`BTCUSD.pi` | Crypto Major | Spread: 2.97 bps | Score: 95.0/100)
   - Live Mid: `77,419.00` | VAL: `77,000.08` | POC: `77,902.48` | VAH: `78,646.96` | VWAP: `77,633.72`
   - Liquidation: Short Max Pain `79,868.95` (+3.16%) | Long Max Pain `76,945.12` (-0.61%)
   - Setup: BUY_LIMIT @ `76,880.00` (leans below Long Max Pain sweep 76,945.12) | SL `76,380.00` (500 pts) | TP `78,130.00` | **2.500R** | Risk: **$5.00 USD** (0.01 lot)
3. **ETHUSD** (`ETHUSD.pi` | Crypto Major | Spread: 16.10 bps | Score: 95.0/100)
   - Live Mid: `2,236.55` | VAL: `2,197.24` | POC: `2,224.76` | VAH: `2,249.04` | VWAP: `2,221.39`
   - Liquidation: Short Max Pain `2,275.30` (+1.73%) | Long Max Pain `2,174.37` (-2.78%)
   - Setup: BUY_LIMIT @ `2,170.00` (below Long Max Pain 2,174.37 sweep) | SL `2,130.00` (40 pts) | TP `2,270.00` | **2.500R** | Risk: **$4.00 USD** (0.10 lot)
4. **XMRUSD** (`XMRUSD.p` | Altcoin | Spread: 6.48 bps | Score: 90.0/100)
   - Live Mid: `589.50` | VAL: `586.96` | POC: `592.04` | VAH: `614.74`
   - Setup: BUY_LIMIT @ `586.50` | SL `578.50` (8.0 pts below Long Max Pain 579.76) | TP `606.50` | **2.500R** | Risk: **$8.00 USD** (0.01 lot)

---

## 🎯 3. MANDATORY TRI-COUNCIL DELIVERABLES & ADVERSARIAL CROSS-EXAMINATION
Arena.ai (Seat #2) and Z.ai (Seat #3) are commanded to deliver:
1. **Independent Candidate Selection**: Inspect the individual JSON dossiers across all {eligible_count} assets and select your top 1-3 trade setups (Entry, SL, TP, R:R >= 2.5R, nominal risk <= $10.00 USD).
2. **Adversarial Critique of Antigravity Setups**: Evaluate Antigravity's BTC, ETH, XAU, and XMR setups. Specifically check whether the proposed entries/stops are immune to Pitfall 24 (stop-hunt magnets) and whether lot sizing guarantees risk <= $10.00 USD.
3. **Friday Rollover (21:15-22:30 UTC) & Weekend Protocol**: Provide specific risk mitigation rules for any order staged today.
4. **Execution Ruling**: Recommend which (if any) setup should be authorized for live MT5 maker limit punching.

> ⚠️ **REMINDER**: PRINT YOUR COMPLETE VERDICT, ANALYSIS, AND CANDIDATE SETUPS INLINE HERE ALL-IN-ONE. DO NOT REFERENCE EXTERNAL FILES.

Antigravity as lead broker desk will synthesize all three findings, issue the final verdict, and punch qualified trades to MT5.
"""
    return prompt

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_035 COLLABORATIVE PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)

    prompt = build_cycle_035_prompt()
    prompt_path = ROOT / "docs" / "trade_plans" / "CYCLE_035_DISPATCH_PROMPT.txt"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")
    print(f"Saved Cycle_035 prompt ({len(prompt)} chars) to {prompt_path}")

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
    print("CYCLE_035 DISPATCH SUMMARY:", results)
    print("=" * 80)

if __name__ == '__main__':
    asyncio.run(main())
