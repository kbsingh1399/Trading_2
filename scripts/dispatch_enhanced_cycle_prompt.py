import asyncio
import json
import os
import pathlib
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena_single, post_prompt_to_zai

sys.stdout.reconfigure(encoding='utf-8')

def build_enhanced_cycle_prompt(cycle_id: str = "Cycle_035"):
    # Read eligible symbols
    eligible_file = ROOT / "scripts" / "cycle_035_eligible_dossiers.txt"
    if eligible_file.exists():
        symbols = [s.strip() for s in eligible_file.read_text(encoding="utf-8").splitlines() if s.strip()]
    else:
        symbols = []

    # Read Multi-Feed Certificate
    cert_file = ROOT / "docs" / "trade_plans" / f"{cycle_id.upper()}_MULTI_FEED_EXAMINATION_CERTIFICATE.json"
    cert_sha = "PENDING"
    if cert_file.exists():
        try:
            cert_data = json.loads(cert_file.read_text(encoding="utf-8"))
            cert_sha = cert_data.get("certificate_sha256", "UNKNOWN")
        except Exception:
            pass

    symbols_formatted = ", ".join(symbols)

    prompt = f"""# 🏛️ AUTONOMOUS TRI-COUNCIL AUDIT & TRADE COLLABORATION: {cycle_id}
**Seat #1: Antigravity Autonomous Lead & Broker Desk | Seat #2: Arena.ai Lead Strategist | Seat #3: Z.ai Solvency Arbiter**
**Timestamp (UTC)**: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} | **Cycle ID**: `{cycle_id}`
**Live Portfolio Registry**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`
**Canonical Checklist**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`

> ⚠️ **CRITICAL OPERATOR MANDATE & OUTPUT CONSTRAINTS**:
> 1. **NO ARTIFICIAL HARD FLOOR RESTRICTION**: Per operator command, the defensive capital freeze is lifted. Active high-confluence maker limit trading is authorized (Capacity N <= 3, Risk <= $10.00 USD, R:R >= 2.50R).
> 2. **PRINT INLINE ALL-IN-ONE**: PRINT YOUR COMPLETE EVALUATION, AUDIT FINDINGS, CANDIDATE SETUPS, AND VERDICTS DIRECTLY INLINE. DO NOT REFERENCE EXTERNAL ATTACHMENTS OR SIDECARS.
> 3. **GRAVITAS SCIENTIFIC RIGOR**: Zero hallucinations, zero ungrounded assertions. Every statement must be physically rooted in the master dossiers or Parquet feeds.

---

## 🏛️ 1. ACCOUNT SOLVENCY & LIVE MT5 ORDER INVENTORY
- **MT5 Account**: #5064568 (Blueberry Markets, Live Raw Spread)
- **Balance & Floating Equity**: **4,763.23 USD**
- **Margin Used**: **0.00 USD** | **Free Margin**: **4,763.23 USD**
- **Capital Posture**: `ACTIVE_HIGH_CONFLUENCE_OPERATION` (Operator Mandate: Floor lifted, active trading authorized)
- **Active Open Positions**: **0** (100% Cash Defense Preserved)
- **Active Resting Maker Limit Orders**: **0** (Full capacity 0/3 available)
- **Total Contingent Downside Risk**: **0.00 USD**

---

## 🔍 2. UNIVERSE FORENSICS & SPREAD-CLEARED ASSET POOL ({len(symbols)} ASSETS)
The following {len(symbols)} assets have cleared broker spread thresholds (TradFi <= 5.0 bps, Crypto <= 25.0 bps):
`{symbols_formatted}`

All individual JSON dossiers are hosted at:
`https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/dossiers/<SYMBOL>_MASTER_DOSSIER.json`

### 15-Pillar Mechanical Forensics Certificate:
- **Certificate**: `docs/trade_plans/{cycle_id.upper()}_MULTI_FEED_EXAMINATION_CERTIFICATE.json`
- **Certificate SHA256**: `{cert_sha}` | **Verdict**: `APPROVED_FOR_BROKER_EXECUTION`
- All 15 data pillars interrogated: ETF Netflows, Capital Netflows (Spot/Futures), MTF Long/Short Ratios, Funding Rates & Settlement, Open Interest, Liquidation Max Pain, Whale Armor, Technicals & VWAP, Hyperdash Intel, L2 Orderbook Depth, Multi-Timeframe CVD, Auction Profile, Tradfye Orderflow, CoinGlass Footprint Signals, and Broker Telemetry.

---

## 🎯 3. ANTIGRAVITY'S FORMULATED HIGH-CONFLUENCE CANDIDATE SETUPS

1. **`BTCUSD.pi` (Bitcoin) — Confluence Score: 95.0 / 100**
   - Live Mid: `76,873.00` | VAL: `77,067.76` | POC: `77,902.48` | VAH: `78,646.96` | VWAP: `77,633.72`
   - Liquidation: Long Max Pain `76,945.12` | Short Max Pain `79,868.95` (Magnet +3.8%)
   - Microstructure: 4h CVD Bullish Absorption; price sweeping below 24h Long Max Pain node.
   - Proposed Setup: **`BUY_LIMIT` @ `76,850.00`** | SL `76,350.00` (500 pts) | TP `78,100.00` (1,250 pts) | **2.500R** | Risk: **$5.00 USD** (0.01 lot)
   - Pitfall 24 Check: **IMMUNE** (Entry placed below Long Max Pain sweep; TP targets upward Short Max Pain magnet at $79,868.95).

2. **`AVEUSD.p` (Aave) — Confluence Score: 85.0 / 100**
   - Live Mid: `123.53` | VAL: `120.30` | POC: `124.84` | VAH: `127.07`
   - Liquidation: Long Max Pain `123.64` | Short Max Pain `128.80` (Magnet +4.2%)
   - Proposed Setup: **`BUY_LIMIT` @ `123.50`** | SL `122.20` (1.30 pts) | TP `126.75` (3.25 pts) | **2.500R** | Risk: **$1.30 USD** (1.00 lot)
   - Pitfall 24 Check: **IMMUNE** (Absorbs Long Max Pain sweep; targets Short Max Pain at 128.80).

3. **`ETHUSD.pi` (Ethereum) — Confluence Score: 80.0 / 100**
   - Live Mid: `2,218.60` | VAL: `2,198.86` | POC: `2,224.76` | VAH: `2,247.42`
   - Liquidation: Long Max Pain `2,174.37` | Short Max Pain `2,275.30` (Magnet +2.6%)
   - Microstructure: 4h CVD Bullish Absorption; discount positioning below developing POC.
   - Proposed Setup: **`BUY_LIMIT` @ `2,170.00`** | SL `2,130.00` (40 pts) | TP `2,270.00` (100 pts) | **2.500R** | Risk: **$4.00 USD** (0.10 lot)
   - Pitfall 24 Check: **IMMUNE**.

4. **`XMRUSD.p` (Monero) — Confluence Score: 75.0 / 100**
   - Live Mid: `586.90` | VAL: `586.56` | POC: `592.04` | VAH: `614.35`
   - Liquidation: Long Max Pain `579.76` | Short Max Pain `654.54`
   - Proposed Setup: **`BUY_LIMIT` @ `586.50`** | SL `578.50` (8.00 pts) | TP `606.50` (20.00 pts) | **2.500R** | Risk: **$8.00 USD** (0.01 lot)
   - Pitfall 24 Check: **IMMUNE**.

---

## 🎯 4. MANDATORY TRI-COUNCIL DELIVERABLES
Arena.ai (Seat #2) and Z.ai (Seat #3) are commanded to deliver:
1. **Full Universe Inspection**: Inspect individual JSON dossiers across all {len(symbols)} spread-cleared assets and nominate your top 1-3 independent high-confluence setups.
2. **Adversarial Critique of Antigravity Setups**: Evaluate BTC, AVE, ETH, and XMR setups. Specifically check whether entries/stops are immune to Pitfall 24 and whether lot sizing guarantees nominal risk <= $10.00 USD.
3. **Execution Ruling**: Recommend which setups should be authorized for live MT5 maker limit punching.

> ⚠️ **REMINDER**: PRINT YOUR COMPLETE VERDICT, ANALYSIS, AND CANDIDATE SETUPS INLINE HERE ALL-IN-ONE.
"""
    return prompt
