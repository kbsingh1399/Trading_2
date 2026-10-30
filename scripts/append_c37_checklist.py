import datetime
import pathlib

p = pathlib.Path("Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
text = p.read_text(encoding="utf-8")

now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
now_ist = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")

c37_block = f"""
---

## 🏛️ CYCLE EXECUTION SCORECARD: Cycle_037
- **Timestamp**: {now_ist} ({now_utc}) | **Cycle ID**: `Cycle_037`
- **Capital Posture**: `ACTIVE_HIGH_CONFLUENCE_OPERATION` (Operator Floor Override: Active trading authorized)
- **Account Balance & Equity**: **$4,755.23 USD** | **Free Margin**: **$4,755.23 USD** | **Margin Used**: **$0.00 USD**
- **Active Running Positions**: **0 ACTIVE** (100% Cash Defense Preserved)
- **Active Resting Pending Orders**: **2 ACTIVE** (2/3 capacity deployed):
  1. Ticket #19532055: `BTCUSD.pi` BUY_LIMIT 0.01 lot @ `76,350.00` | SL `75,850.00` | TP `77,600.00` | Risk: **$5.00 USD**
  2. Ticket #19532058: `AVEUSD.p` BUY_LIMIT 0.07 lot @ `122.50` | SL `121.20` | TP `125.75` | Risk: **$9.10 USD**
- **Total Contingent Downside Risk**: **$14.10 USD** (0.29% of account equity)
- **Execution Capacity Remaining**: **1 Available Slot** (Dedicated for new high-confluence candidate)

### 📋 Canonical 8-Step Verification Loop (Cycle_037):
- [x] **Step 0: Mandatory 4-Document Governance & Pitfall Avoidance Read Gate**
  - Cross-referenced `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`, `CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md`, `STANDARDIZED_TRADING_DECISION_CHAIN.md`, and `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`.
  - Account verified in flat cash defense with 2 maker limit orders resting.
- [x] **Step 1: Identify eligible assets (spread screening)**
  - Audited `00_MT5_Account_Telemetry.parquet` and broker quotes.
  - 92 assets passed broker spread thresholds (TradFi <= 5.0 bps, Crypto <= 25.0 bps).
  - Generated eligible asset list with exact Raw GitHub URLs for 100% of candidate assets.
- [x] **Step 2: Conduct comprehensive asset-level forensics & mandatory 10-section audit**
  - Executed `scripts/mechanical_asset_forensics_examiner.py Cycle_037`: 92/92 assets audited, 5,479,852 bytes verified (`docs/trade_plans/CYCLE_037_PHYSICAL_EXAMINATION_CERTIFICATE.json`).
  - Executed `scripts/mechanical_multi_feed_forensics_examiner.py Cycle_037`: Interrogated all 15 quantitative features from individual JSON dossiers.
  - Multi-Feed Certificate: `docs/trade_plans/CYCLE_037_MULTI_FEED_EXAMINATION_CERTIFICATE.json` (SHA256: `5d059d3eafd8a3f88a3f13f4db9f01cc8f16a76518167b8b9115be77ed153eba`).
- [x] **Step 3: Synchronise intelligence ledger and portfolio registry**
  - Updated `Data/cycle_envelope.json` and `Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`.
  - Reconciled balance: $4,755.23 USD, 0 positions, 2 resting orders.
- [x] **Step 4: Dispatch independent analysis to Arena.ai and Z.ai**
  - Dispatched enhanced prompt (`scripts/dispatch_council_cycle.py --cycle Cycle_037`) with exact Raw GitHub URLs for all 92 assets.
  - Emphasized explicit intent to actively discover and formulate NEW high-confluence trades for the open slot.
- [ ] **Step 5: Activate AutoWake daemon and await completion of both systems** (IN PROGRESS)
- [ ] **Step 6: Tri-Council Triangulation & Broker Desk Execution**
- [ ] **Step 7: Update records and restart 20-minute AutoWake cycle**
"""

p.write_text(text + c37_block, encoding="utf-8")
print("Appended Cycle_037 scorecard to ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md!")
