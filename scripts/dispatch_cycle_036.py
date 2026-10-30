#!/usr/bin/env python3
"""
scripts/dispatch_cycle_036.py
=============================
Dispatches the Cycle_036 Autonomous Tri-Council Audit prompt to Arena.ai and Z.ai via Chrome CDP (port 9222).
"""

import asyncio
import datetime
import json
import os
import pathlib
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single, post_prompt_to_zai

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def build_cycle_036_prompt() -> str:
    # Read eligible symbols
    eligible_file = ROOT / "scripts" / "cycle_036_eligible_dossiers.txt"
    if not eligible_file.exists():
        eligible_file = ROOT / "scripts" / "cycle_035_eligible_dossiers.txt"
    
    symbols = [s.strip() for s in eligible_file.read_text(encoding="utf-8").splitlines() if s.strip() and s.strip() != "NONE_ACTIVE"]
    symbols_formatted = ", ".join(symbols)

    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    now_ist = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")

    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & TRADE COLLABORATION: Cycle_036
**Seat #1: Antigravity Autonomous Lead & Broker Desk | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp**: {now_ist} ({now_utc}) | **Cycle ID**: `Cycle_036`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`
**Canonical Checklist**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`

> ⚠️ **CRITICAL OPERATOR MANDATE & OUTPUT CONSTRAINTS**:
> 1. **NO ARTIFICIAL HARD FLOOR RESTRICTION**: Per operator directive ("no hard floor... keep punching and trading"), active high-confluence maker limit trading is authorized (Capacity N <= 3, Risk <= $10.00 USD, R:R >= 2.50R).
> 2. **PRINT INLINE ALL-IN-ONE**: PRINT YOUR COMPLETE EVALUATION, AUDIT FINDINGS, CANDIDATE SETUPS, AND VERDICTS DIRECTLY INLINE. DO NOT REFERENCE EXTERNAL ATTACHMENTS OR SIDECARS.
> 3. **GRAVITAS SCIENTIFIC RIGOR**: Zero hallucinations, zero ungrounded assertions. Every statement must be physically rooted in the master dossier JSONs or Parquet feeds.

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Margin Used**: **0.00 USD** | **Free Margin**: **4,763.23 USD**
- **Capital Posture**: `ACTIVE_HIGH_CONFLUENCE_OPERATION` (Operator Mandate: Active trading authorized)
- **Active Open Positions**: **0** (100% Cash Defense Preserved)
- **Active Resting Pending Orders**: **3 ACTIVE** (Full capacity 3/3 deployed on broker):
  1. **Ticket #19532055**: `BTCUSD.pi` BUY_LIMIT 0.01 lot @ `76,350.00` | SL `75,850.00` | TP `77,600.00` | **2.500R** | Risk: **$5.00 USD**
  2. **Ticket #19532057**: `XMRUSD.p` BUY_LIMIT 0.01 lot @ `585.50` | SL `577.50` | TP `605.50` | **2.500R** | Risk: **$8.00 USD**
  3. **Ticket #19532058**: `AVEUSD.p` BUY_LIMIT 0.07 lot @ `122.50` | SL `121.20` | TP `125.75` | **2.500R** | Risk: **$9.10 USD**
- **Total Contingent Downside Risk**: **22.10 USD** (0.46% of account equity)

---

## 🔍 2. UNIVERSE FORENSICS & SPREAD-CLEARED ASSET POOL ({len(symbols)} ASSETS)
The following {len(symbols)} assets have cleared broker spread thresholds (TradFi <= 5.0 bps, Crypto <= 25.0 bps):
`{symbols_formatted}`

All individual JSON master dossiers are hosted at:
`https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/dossiers/<SYMBOL>_MASTER_DOSSIER.json`
*(Note: Core crypto files use base tickers, e.g., `BTC_MASTER_DOSSIER.json`, `ETH_MASTER_DOSSIER.json`, `SOL_MASTER_DOSSIER.json`, while alts and forex use full pairs, e.g., `AVEUSD_MASTER_DOSSIER.json`, `XMRUSD_MASTER_DOSSIER.json`).*

### 15-Pillar Mechanical Dossier Forensics Certificate:
- **Certificate**: `docs/trade_plans/CYCLE_036_MULTI_FEED_EXAMINATION_CERTIFICATE.json`
- **Certificate SHA256**: `a1ebac008d05949153227db476b937847a7bad07e0cd94a54b6aae398ce66291` | **Verdict**: `APPROVED_FOR_BROKER_EXECUTION`
- All 15 quantitative features were read directly from individual Dossier JSONs with grounded metrics:
  * ETF Netflows (BTC ETFs: $66.17B IBIT, $14.92B FBTC)
  * Spot & Future Capital Netflows (XMR 24h Spot: +$871.89K, Fut: +$3.92M)
  * Multi-Exchange Long/Short Ratios (Binance, OKX, Bybit ladders)
  * 12-Venue Funding Rates (BTC Binance: 0.0100%, XMR: 0.0255%, AAVE: -0.0064%)
  * Multi-Venue Open Interest (BTC Total OI: $53.43B, ETH: $28.32B, SOL: $5.53B)
  * Liquidation Max Pain (BTC Short Pain: 79,868.95, Long Pain: 76,195.42)
  * Whale Orders > $100K (BTC: 325 whales, ETH: 220, SOL: 103)
  * Technical Profile & VWAP (BTC VWAP: 77,558.63, RSI: 37.61)
  * Hyperdash Stops & Intel (BTC: 926 stop clusters, ETH: 329, SOL: 728)
  * L2 Orderbook Depth & Bid/Ask ladders
  * Multi-Timeframe CVD (5m, 15m, 1h, 4h CVD deltas and absorption regimes)
  * Auction Market Structure (BTC POC: 77,180.56, XMR POC: 590.48, AAVE POC: 124.84)
  * Tradfye / Hyperliquid Orderflow
  * CoinGlass Footprint Signals
  * MT5 Broker Telemetry & true contract specs (Contract sizes: BTC 1.0, XMR 100.0, AAVE 100.0)

---

## 🎯 3. ACTIVE RESTING LIMIT ORDERS & CURRENT CANDIDATES REVIEW

1. **`BTCUSD.pi` BUY_LIMIT @ `76,350.00` (Ticket #19532055)**
   - Entry: `76,350.00` | SL: `75,850.00` (500 pts) | TP: `77,600.00` (1,250 pts) | **2.50R** | Risk: **$5.00 USD**
   - Pitfall 24 Immunity: Long Max Pain is `76,195.42`. Entry is above Long Pain, SL is below `76,195.42`. Short Max Pain magnet sits at `79,868.95` (+4.6%).
   - Status: Resting on broker.

2. **`XMRUSD.p` BUY_LIMIT @ `585.50` (Ticket #19532057)**
   - Entry: `585.50` | SL: `577.50` (8.00 pts) | TP: `605.50` (20.00 pts) | **2.50R** | Risk: **$8.00 USD** (0.01 lot, contract size 100)
   - Liquidation: Long Max Pain `579.76` | Short Max Pain `654.54`. Entry sits right at developing VAL (`586.56`).
   - Status: Resting on broker.

3. **`AVEUSD.p` BUY_LIMIT @ `122.50` (Ticket #19532058)**
   - Entry: `122.50` | SL: `121.20` (1.30 pts) | TP: `125.75` (3.25 pts) | **2.50R** | Risk: **$9.10 USD** (0.07 lot, contract size 100)
   - Liquidation: Long Max Pain `116.52` | Short Max Pain `128.80`.
   - Status: Resting on broker.

4. **Watchlist / Standby Candidates**:
   - `ETHUSD.pi`: Developing POC `2,224.76`, Long Max Pain `2,174.37`. Potential BUY_LIMIT @ `2,170.00` if capacity frees.
   - `SOLUSD.p`: Developing POC `96.55`, Long Max Pain `92.18`.

---

## ⚖️ 4. MANDATORY TRI-COUNCIL DELIVERABLES
Arena.ai (Seat #2) and Z.ai (Seat #3) are commanded to deliver:
1. **Audit of 3 Active Resting Limit Orders**: Validate tickets #19532055 (BTC), #19532057 (XMR), #19532058 (AVE). Should these remain resting as placed, or are there adverse orderflow/liquidation shifts warranting immediate cancellation or modification?
2. **Full Universe Forensic Screening**: Inspect individual JSON dossiers across all {len(symbols)} spread-cleared assets and nominate any alternative or replacement high-confluence setups ($R:R \ge 2.50R$, nominal risk $\le \$10.00$ USD).
3. **Execution Ruling**: Deliver your clear verdict on whether to HOLD active limit orders, ratchet any fills, or cancel/substitute.

> ⚠️ **REMINDER**: PRINT YOUR COMPLETE VERDICT, ANALYSIS, AND CANDIDATE SETUPS INLINE HERE ALL-IN-ONE.
"""
    return prompt

async def dispatch_cycle_036():
    print("=" * 80)
    print("🚀 DISPATCHING CYCLE_036 TRI-COUNCIL PROMPT")
    print("=" * 80)

    prompt = build_cycle_036_prompt()
    prompt_path = ROOT / "docs" / "trade_plans" / "CYCLE_036_DISPATCH_PROMPT.txt"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")
    print(f"✅ Saved Cycle_036 prompt ({len(prompt):,} chars) to {prompt_path.name}")

    try:
        raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
    except Exception as e:
        print(f"❌ Error connecting to Chrome CDP on port 9222: {e}")
        return False

    arena_tab = next((t for t in tabs if t.get("type") == "page" and "arena.ai" in t.get("url", "") and "preview-" not in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai_tab = next((t for t in tabs if t.get("type") == "page" and ("chat.z.ai" in t.get("url", "") or "z.ai" in t.get("url", "")) and "preview-" not in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)

    results = {}

    if arena_tab:
        print(f"\n[1/2] Dispatching to Arena.ai ({arena_tab['url']})...")
        res_arena = await post_prompt_to_arena_single(arena_tab["webSocketDebuggerUrl"], prompt, "Arena.ai")
        results["arena"] = res_arena
        print(f"   Arena.ai dispatch result: {'SUCCESS' if res_arena else 'FAILED'}")
    else:
        print("❌ Warning: Arena.ai tab not found on port 9222.")
        results["arena"] = False

    if zai_tab:
        print(f"\n[2/2] Dispatching to Z.ai ({zai_tab['url']})...")
        res_zai = await post_prompt_to_zai(prompt)
        results["zai"] = res_zai
        print(f"   Z.ai dispatch result: {'SUCCESS' if res_zai else 'FAILED'}")
    else:
        print("❌ Warning: Z.ai tab not found on port 9222.")
        results["zai"] = False

    print("\n" + "=" * 80)
    print(f"Dispatch Summary: Arena: {results.get('arena')}, Z.ai: {results.get('zai')}")
    print("=" * 80)
    return results

if __name__ == "__main__":
    asyncio.run(dispatch_cycle_036())
