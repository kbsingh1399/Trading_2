import re

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace header for Cycle_025
old_c25_header = "### ⏳ Cycle_025 Scorecard: PRE-INITIALIZED & ARMED\n**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"
new_c25_header = """### ⏳ Cycle_025 Scorecard: IN PROGRESS
**Timestamp**: 2026-10-30 10:07:00 IST (2026-10-30 04:37:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

text = text.replace(old_c25_header, new_c25_header)

# Check off Step 0
text = text.replace("- [ ] **Step 0: Mandatory 4-Document Governance", "- [x] **Step 0: Mandatory 4-Document Governance")
text = text.replace("- [ ] Full-length read & study: `STANDARDIZED_TRADING_DECISION_CHAIN.md`", "- [x] Full-length read & study: `STANDARDIZED_TRADING_DECISION_CHAIN.md`")
text = text.replace("- [ ] Full-length read & study: `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`", "- [x] Full-length read & study: `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`")
text = text.replace("- [ ] Full-length read & study: `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`", "- [x] Full-length read & study: `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`")
text = text.replace("- [ ] Full-length read & study: `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`", "- [x] Full-length read & study: `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`")

# Check off Step 1
text = text.replace("- [ ] **Step 1: Identify Eligible Assets", "- [x] **Step 1: Identify Eligible Assets")
text = text.replace("- [ ] Interrogate live MT5 account telemetry", "- [x] Interrogate live MT5 account telemetry")
text = text.replace("- [ ] Filter all tradeable assets against broker spread thresholds", "- [x] Filter all tradeable assets against broker spread thresholds")
text = text.replace("- [ ] Catalog complete list of eligible candidates", "- [x] Catalog complete list of eligible candidates")

# Check off Step 2
text = text.replace("- [ ] **Step 2: Conduct Comprehensive Asset-Level Forensics", "- [x] **Step 2: Conduct Comprehensive Asset-Level Forensics")
text = text.replace("- [ ] **Phase 2A: Comprehensive Sector-Wide Forensic Screening", "- [x] **Phase 2A: Comprehensive Sector-Wide Forensic Screening")
text = text.replace("- [ ] **Phase 2B: Running Trade & Resting Order Microstructure Inspection", "- [x] **Phase 2B: Running Trade & Resting Order Microstructure Inspection")
text = text.replace("- [ ] **Phase 2C: Active Order Microstructure Optimization", "- [x] **Phase 2C: Active Order Microstructure Optimization")

# Check off Step 3
text = text.replace("- [ ] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry", "- [x] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry")
text = text.replace("- [ ] Regenerate `cycle_envelope.json`", "- [x] Regenerate `cycle_envelope.json`")
text = text.replace("- [ ] Reconcile `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`", "- [x] Reconcile `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`")
text = text.replace("- [ ] Guarantee byte-for-byte consistency", "- [x] Guarantee byte-for-byte consistency")

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cycle_025 in ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
