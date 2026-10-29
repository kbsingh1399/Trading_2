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

async def main():
    print("=" * 80)
    print("🚀 DISPATCHING SOVEREIGN DOSSIER REVIEW PROMPT TO ARENA.AI & Z.AI")
    print("=" * 80)

    # 1. Read sample dossiers
    btc_path = ROOT / "docs" / "dossiers" / "BTC_MASTER_DOSSIER.md"
    nzd_path = ROOT / "docs" / "dossiers" / "NZDUSD_MASTER_DOSSIER.md"

    btc_content = btc_path.read_text(encoding="utf-8") if btc_path.exists() else "BTC dossier missing"
    nzd_content = nzd_path.read_text(encoding="utf-8") if nzd_path.exists() else "NZDUSD dossier missing"

    # Truncate slightly to stay within prompt length bounds if needed, or include the core sections
    prompt = f"""# 🏛️ INSTITUTIONAL QUANT REVIEW REQUEST: SOVEREIGN DOSSIER ENGINE v3.1 & 400 MASTER DOSSIERS

You are acting as Senior Lead Quantitative Architect and Chief Risk Officer reviewing our production **Sovereign Dossier Architecture**.

### 🎯 GOAL & PRIMARY QUESTION
We have built and deployed the **Sovereign Dossier Engine v3.1** (spec: `sovereign-dossier-engine.md`), which pre-compiles 760 quantitative parameters from all 43 Parquet data lake feeds across all 162 assets in our multi-asset universe (Crypto, Precious Metals, FX Majors, Equity Indices, Energy) into unified 10-section dossiers in `docs/dossiers/`.

**OUR CORE TEST IS**:
*If you (Arena / Z.ai) or the Antigravity autonomous desk read this document alone, can you formulate a rigorous, high-confluence institutional trade setup (Direction, Exact Entry, Spread-Padded Stop Loss, +2.5R Take Profit, Lot Sizing, and Invalidation triggers) WITHOUT needing to query any external API or raw Parquet data?*

---

### 🔬 DOSSIER ARCHITECTURE (10 SECTIONS / 760 PARAMETERS)
1. **MT5 Live Broker Telemetry**: Bid, Ask, Spread (bps), Tick Value, Contract Size, Lot Min/Step, Margin Free, Equity, Solvency Cushion (4,775 USD Hard Floor, 4,795 USD Operating Buffer).
2. **Technical Profile & Dispersion**: 14-band VWAP grid (±1σ, ±1.28σ, ±2σ, ±2.01σ, ±2.51σ, ±3σ), 11-period EMA ribbon (5, 9, 13, 20, 34, 50, 89, 100, 144, 200, 233), ATR-14, RSI-14, MACD, Bollinger Bands.
3. **Auction Market Structure (61 params)**: Daily/Previous Day/Weekly VAH/VAL/POC, Monday High/Low/Mid, Weekly/Monthly ranges, Asian/London/NY session extremes, Initial Balance, Fib Golden Pocket/OTE/Invalidation.
4. **CVD & Options Flow**: Multi-timeframe CVD delta (5m, 15m, 1h, 4h, ALL), delta percentage, Deribit Max Pain, Call/Put Walls.
5. **Institutional Whale Armor**: Defending resting limit walls (>100K USD, >180s persistence, coins, order IDs), L3 book skew, Hyperliquid top trader positioning.
6. **Liquidation Max Pain & Retail Stops Map**: 24H/48H/3D/7D short/long strikes & volume, 1D/7D cumulative pools, real-time forced liquidations, Hyperdash retail stop-loss clusters (Pitfall 2 & 4 defense).
7. **Derivatives Sentiment & 12-Venue Rates**: Aggregated Open Interest across 12 venues, Funding Rates across 12 exchanges, 15m/1h/4h Long/Short ratios, Settlement fee payouts.
8. **Microstructure Footprint & Macro Netflows**: Bar VWAP, Bar POC, Bar VAH/VAL, taker buy/sell volume, bar delta, >300% tape imbalances, Footprint absorption signals, Spot/Futures capital netflows (12 horizons), Crypto ETF daily inflows & AUM, Economic Calendar & News.
9. **TradFi & Interbank Mechanics**: Central Bank monetary policy, Tokyo/London/NY fixings, 21:15-22:30 UTC rollover spread halt.
10. **Algorithmic Trade Formulation**: Full 12-step SOP scorecard, dynamic lot sizing, and execution decision.

---

### 📄 LIVE EXAMPLE 1: CRYPTO (BTC_MASTER_DOSSIER.md)
```markdown
{btc_content[:3500]}
... [truncated for prompt length] ...
```

---

### 📄 LIVE EXAMPLE 2: FOREX MAJOR (NZDUSD_MASTER_DOSSIER.md)
```markdown
{nzd_content[:2500]}
... [truncated for prompt length] ...
```

---

### 📋 SPECIFIC REVIEW PROMPTS / QUESTIONS FOR YOU
1. **Trade Formulatability**: Can you immediately derive an executable limit order with exact mathematical price levels from this dossier alone? What calculation or parameter is missing, if any?
2. **Pitfall Elimination**: Does the dossier provide sufficient clarity on retail stop cascades (`15_Hyperdash_Stops_Map`) and defending whale walls (`10_Whale_Orders`) to completely prevent front-running traps (Pitfall 1) and sub-ATR stops (Pitfall 4)?
3. **TradFi / FX Specifics**: For FX and Indices, what additional macro or fixing metrics would make Section 9 and Section 10 even more authoritative?
4. **Structural Recommendations**: What specific format refinements, table layouts, or additional synthesis metrics would you suggest we implement in Sovereign Dossier Engine v3.2?
"""

    print(f"Prompt length: {len(prompt)} characters.")

    # 2. Get tabs
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode("utf-8"))
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)

    results = {}

    # 3. Post to Arena.ai
    if arena_tab:
        print(f"\n[1/2] Dispatching to Arena.ai tab: {arena_tab['url']}...")
        success_arena = await post_prompt_to_arena_single(arena_tab["webSocketDebuggerUrl"], prompt, "Arena.ai")
        results["arena"] = success_arena
        print(f"Arena.ai dispatch result: {'SUCCESS' if success_arena else 'FAILED'}")
    else:
        print("\n[1/2] No Arena.ai tab found on CDP port 9222.")
        results["arena"] = False

    # 4. Post to Z.ai
    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai tab: {zai_tab['url']}...")
        success_zai = await post_prompt_to_zai(prompt)
        results["zai"] = success_zai
        print(f"Z.ai dispatch result: {'SUCCESS' if success_zai else 'FAILED'}")
    else:
        print("\n[2/2] No Z.ai tab found on CDP port 9222.")
        results["zai"] = False

    print("\n" + "=" * 80)
    print(f"DISPATCH COMPLETED: Arena: {results.get('arena')}, Z.ai: {results.get('zai')}")
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(main())
