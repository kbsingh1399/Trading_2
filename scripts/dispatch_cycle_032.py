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

with open(ROOT / 'docs' / 'trade_plans' / 'CYCLE_032_DOSSIER_FORENSICS_ALL_92.json', 'r', encoding='utf-8') as f:
    forensics = json.load(f)

by_sector = {}
for item in forensics:
    sec = item.get('sector', 'Other')
    if sec not in by_sector:
        by_sector[sec] = []
    by_sector[sec].append(item)

def format_sector_table(items):
    lines = [
        "| Symbol | Bid / Ask | Spread (bps) | VAH | VAL | POC | Antigravity Sovereign Stance |",
        "|---|---|---|---|---|---|---|"
    ]
    for i in items:
        sym = i['symbol']
        quote = f"{i['bid']} / {i['ask']}"
        spread = f"{i['spread_bps']:.2f}"
        vah = f"{i['vah']:.4f}" if isinstance(i.get('vah'), (int, float)) else str(i.get('vah', 'N/A'))
        val = f"{i['val']:.4f}" if isinstance(i.get('val'), (int, float)) else str(i.get('val', 'N/A'))
        poc = f"{i['poc']:.4f}" if isinstance(i.get('poc'), (int, float)) else str(i.get('poc', 'N/A'))
        lines.append(f"| `{sym}` | {quote} | {spread} | {vah} | {val} | {poc} | **`STAND_ASIDE_MONITOR`** |")
    return "\n".join(lines)

def build_cycle_032_prompt():
    crypto_tbl = format_sector_table(by_sector.get('Crypto Perpetuals & CFDs', []))
    metals_tbl = format_sector_table(by_sector.get('Precious & Industrial Metals', []))
    indices_tbl = format_sector_table(by_sector.get('Equity Indices', []))
    energy_tbl = format_sector_table(by_sector.get('Energy & Commodities', []))
    fx_items = sorted(by_sector.get('Forex Majors & Crosses', []), key=lambda x: x['spread_bps'])[:25]
    fx_tbl = format_sector_table(fx_items)

    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & UNIVERSE REVIEW: Cycle_032
**Seat #1: Antigravity Autonomous Lead | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (UTC)**: 2026-10-30 10:35:00 UTC (16:05:00 IST) | **Cycle ID**: `Cycle_032`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`
**Canonical Checklist**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Hard Solvency Floor**: **4,775.00 USD** (Deficit: **-11.77 USD**)
- **Operating Buffer**: **4,795.00 USD** (Deficit: **-31.77 USD**)
- **Capital Regime**: **`TIER_0_DEFENSIVE` (FAIL-CLOSED)**
- **New Market Risk Capacity**: **0.00 USD** (Zero new market orders admitted)
- **Dynamic Portfolio Capacity**: $N_{{open}} + N_{{pending}} \\le 3$
- **Current Position State**: **0 ACTIVE POSITIONS** (100% Flat Cash Defense)
- **Current Order State**: **0 ACTIVE PENDING ORDERS** (All resting maker limit orders cancelled on MT5 in Cycle_030)
- **Total Contingent Downside Risk**: **0.00 USD**
- **Capital Solvency Assessment**: Capital floor is strictly protected in cash. No filled risk. No pending order drawdown risk.

---

## 🔬 2. STEP 1 & STEP 2 COMPREHENSIVE DOSSIER FORENSICS (92+ ELIGIBLE ASSETS)
All eligible spread-cleared assets have been physically read and forensically examined across all 4 macro classes from their 360° master dossiers (`docs/dossiers/<ASSET>_MASTER_DOSSIER.md`).

### 🪙 Crypto Perpetuals & CFDs:
{crypto_tbl}

### 🥇 Precious & Industrial Metals:
{metals_tbl}

### 📈 Global Equity Indices:
{indices_tbl}

### 🛢️ Energy & Commodities:
{energy_tbl}

### 💱 Forex Majors & Crosses (Top 25 of 60 Assets):
{fx_tbl}

---

## 📋 MANDATORY INSTRUCTIONS & DELIVERABLES FOR ARENA.AI & Z.AI:
1. **Independent Asset Analysis**: Perform independent quantitative and risk analysis across the eligible universe using the data above and full-length dossiers on GitHub (`docs/dossiers/<ASSET>_MASTER_DOSSIER.md`).
2. **Solvency Kernel Ruling**: Under `TIER_0_DEFENSIVE` (Equity $4,763.23 < $4,775.00 Hard Floor), confirm whether the desk must remain in **100% Cash Defense** (`STAND_ASIDE_MONITOR`, 0.00 USD new risk) or if any ultra-high confluence passive maker limit order meeting $\\ge 2.5R$ and backed by verified institutional whale walls ($> 100k USD, > 180s$) should be staged.
3. **Rollover Embargo Assessment**: Evaluate the approaching Friday rollover spread expansion window (21:15–22:30 UTC) and provide execution recommendations.
4. **Structured Output**: Provide your executive summary, candidate rankings, and definitive directional verdict.
"""
    return prompt

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_032 UNIVERSE FORENSIC PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)

    prompt = build_cycle_032_prompt()
    prompt_path = ROOT / "docs" / "trade_plans" / "CYCLE_032_DISPATCH_PROMPT.txt"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")
    print(f"Saved Cycle_032 prompt ({len(prompt)} chars) to {prompt_path}")

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
        print("Warning: Arena.ai tab not found on port 9222.")
        results["arena"] = False

    # 2. Z.ai
    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai ({zai_tab['url']})...")
        res_zai = await post_prompt_to_zai(prompt)
        results["zai"] = res_zai
        print(f"Z.ai dispatch result: {'SUCCESS' if res_zai else 'FAILED'}")
    else:
        print("Warning: Z.ai tab not found on port 9222.")
        results["zai"] = False

    print("\n" + "=" * 80)
    print("CYCLE_032 DISPATCH SUMMARY:", results)
    print("=" * 80)

    if not (results.get("arena") and results.get("zai")):
        print("Dispatch incomplete. Check connection or generation state.")
        sys.exit(1)
    else:
        print("All prompts dispatched successfully!")

if __name__ == "__main__":
    asyncio.run(main())
