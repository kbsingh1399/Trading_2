# 📋 PROJECT PLAN: Standardized IST Completion Timestamp Across All 33 Excel Sheets

> **Task Slug**: `excel-ist-timestamp-banner.md`  
> **Target Workbook**: `Data/DataBase_Trading.xlsx` (33 Sheets)  
> **Governing Standards**: `xlsx-official`, `coordinator-mode`, `clean-code`, `systematic-debugging`  
> **Core Requirement**: Stamp Tier-1 Banner Timestamp in Indian Standard Time (IST = UTC + 5:30) **ONLY ONCE** row data is successfully filled (`row_count > 0`).

---

## 🎯 Objective & Success Criteria

1. **Human At-a-Glance Clarity**: Every sheet in `DataBase_Trading.xlsx` prominently displays in Cell `A1` (or banner header) the exact IST time of completion:
   `LAST UPDATED: 2026-10-23 16:45:10 IST (11:15:10 UTC) | ROWS: 172 | STATUS: LIVE`
2. **Strict Invariant**: The timestamp is stamped **ONLY AFTER** all data rows are populated. If `row_count == 0` or an error occurs, the timestamp remains unchanged.
3. **Automated Audit Parity**: `Terminal/Data_Factory/excel_data_quality_checker.py` is updated to parse this standardized IST header directly, removing all `UNKNOWN` or `DERIVED/LIVE` ambiguities.
4. **Zero Regression**: 0 formula errors, 100% header integrity, and zero write collisions across all 33 sheets.

---

## 🏗️ Phase Breakdown & Architecture

```
Phase 1: Research & Module Classification (Read-Only)
   ├── Subtask 1.1: Census of all 33 modules in Data/Excel_Modules/
   └── Subtask 1.2: Map existing banner/header insertion mechanisms

Phase 2: Core Infrastructure Implementation
   ├── Subtask 2.1: Add `stamp_sheet_completion_ist()` to `Data/Excel_Modules/logger_config.py`
   └── Subtask 2.2: Add unit validation for empty row protection

Phase 3: Harvester Implementation (Batch Rollout)
   ├── Batch A: Core Real-Time Feeds (00_MT5, 11_Technical, 17_Orderbook, 18_CVD, 20_AMS)
   ├── Batch B: Macro & Intel Feeds (10_Whale, 19_News, 19_Calendar, 12_Hyperdash, 14_Liq_Map)
   ├── Batch C: Periodic API & Hyperliquid (1_ETF, 4_HL, 5_OI, 5_FR, 6_Fee, 13_HL, 15_Stops, 16_Intel)
   └── Batch D: CoinGlass Queue Modules (2_Spot, 3_LS_15M/1H/4H, 7_Heapmap/Live, 8_Map_1D/7D, 9_MaxPain)

Phase 4: Quality Checker & Autonomous Verification
   ├── Subtask 4.1: Update `excel_data_quality_checker.py` to parse IST banner
   ├── Subtask 4.2: Execute full 33-sheet quality audit
   └── Subtask 4.3: Restart continuous pipeline daemon `task-116833`
```

---

## 👥 Multi-Agent Assignments

| Role / Persona | Phase | Specific Mandate |
|---|---|---|
| **Data Architect (Coordinator)** | Phase 1 & 2 | Design the centralized `stamp_sheet_completion_ist()` API and enforce `row_count > 0` guard. |
| **Excel Engineering Specialist** | Phase 3 | Implement banner formatting in `Data/Excel_Modules/*.py` with openpyxl styling (soft green fill, dark green text). |
| **QA / Verification Auditor** | Phase 4 | Run `excel_data_quality_checker.py`, verify IST timestamp accuracy against system clock, confirm 0 errors. |

---

## 🔍 Verification Checklist

- [ ] `stamp_sheet_completion_ist()` rejects `row_count <= 0` (zero stamp on empty harvest).
- [ ] Cell `A1` on all 33 sheets displays `LAST UPDATED: YYYY-MM-DD HH:MM:SS IST`.
- [ ] `excel_data_quality_checker.py` reports 33/33 sheets with verified ages.
- [ ] No Excel write collisions or `.lock` file leaks.
- [ ] Continuous pipeline daemon relaunched cleanly in memory.
- [ ] Working tree clean and synced with `origin/main`.
