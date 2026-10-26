# Plan: Upgrading Standardized Trading Decision Chain to Canonical 35-Feed Parquet Lake

## Goal Description
Upgrade `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md` (and related architecture docs) from the legacy 33-sheet Excel workbook (`DataBase_Trading.xlsx`) to the production **35-Feed Canonical Parquet Data Lake**, integrating all current data structures, the live CDP orderflow footprint engines (Feeds 25 & 26), current account solvency baselines, and harmonizing related documentation.

## User Review Required
1. Complete transition from `Data/DataBase_Trading.xlsx` to `Data/feeds/*.parquet` (35 atomic Parquet feeds).
2. Addition of Feed 25 (`25_CoinGlass_Footprint_Signals.parquet`) and Feed 26 (`26_Aggregated_Footprint_Bar_Metrics.parquet`).
3. Grounding in live account telemetry: 4,846.32 USD realized balance, Tier 1 Standard regime, 4,600.00 USD hard floor, 4,650.00 USD operating buffer, 4,795.00 USD kernel admission floor (+49.32 USD net headroom).
4. Incorporation of Unified Multi-Venue Liquidation Matrix (`14_Liquidation_Matrix.parquet`, 8,858 rows).
5. Explicit inclusion of all 10 precious/industrial metals and commodities (`XAG, XAU, CL, COPPER, ALUMINIUM, LEAD, ZINC, XPT, XPD`).

## Proposed Changes
- `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`
- `docs/specs/PARQUET_PIPELINE_ARCHITECTURE_PLAN.md`
- `docs/specs/CYCLE_LIFECYCLE_CHECKLIST.md`
- `docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md`
- Dual-repo verification and sync via `python .agents/scripts/verify_and_sync_agents.py`.

## Verification Plan
1. Parquet auditor verification: `python Terminal/parquet_checklist_auditor.py`.
2. Collector verification: test Feed 25 and Feed 26 execution.
3. Dual-repo twin parity check: `python .agents/scripts/verify_and_sync_agents.py`.
