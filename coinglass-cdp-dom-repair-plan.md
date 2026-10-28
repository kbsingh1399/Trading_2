# CoinGlass CDP Scraping & DOM Analysis Repair Plan

**Task Slug**: `coinglass-cdp-dom-repair-plan`  
**Target Domain**: Data Pipeline & Browser CDP Collectors (`Collectors/Browser/`, `Collectors/Core/`, `Terminal/Data_Factory/`)  
**Created At**: 2026-10-28 21:25:00 IST (15:55:00 UTC)  
**Status**: `PENDING USER APPROVAL` (Phase 1 Planning Complete)

---

## 1. Executive Summary & Problem Diagnosis

The user identified two critical operational failure modes in the browser CDP data collection pipeline:
1. **CoinGlass UI Redesign on Liquidation Max Pain (`https://www.coinglass.com/liquidation-maxpain`)**:
   - *Forensic Finding*: Live CDP DOM probe confirmed that CoinGlass removed `.ant-table` CSS class (`hasAntTable: false`). The shared extractor engine [`Collectors/Core/liquidation_maxpain_core.py`](file:///c:/Users/SIGMA/Documents/Trading_2/Collectors/Core/liquidation_maxpain_core.py#L210-L245) hardcodes `document.querySelector('.ant-table')` and React fiber key matching on `__reactFiber$`.
   - *Impact*: Affects 4 high-value feeds: `9_Liquidation_Max_Pain_24H.parquet`, `9_Liquidation_Max_Pain_48H.parquet`, `9_Liquidation_Max_Pain_3D.parquet`, and `9_Liquidation_Max_Pain_7D.parquet`.
   - *Solution*: Modernize DOM selectors to query generic semantic `table`, traverse React 18 fiber root (`__next` / `#root`), and implement dual-fallback network response interception (`/api/futures/liquidation/max-pain`).

2. **The "No Data" / Empty State / Intermittent Page Load Failure (Screenshot Analysis)**:
   - *Screenshot Evidence (`media_1793202378170_6c9dc098.png`)*: On `https://www.coinglass.com/pro/futures/LiquidationMap`, the top chart (Binance BTC/USDT) renders, but the bottom chart ("SUI Exchange Liquidation Map") displays a prominent "no data" icon.
   - *Root Causes*:
     1. Asynchronous WebSocket/REST latency: Chart DOM is inspected before the client WebSocket payload hydrates the canvas/SVG.
     2. Illiquid / New Pairs: Certain altcoins or 7-day windows have zero recorded liquidation volume on specific exchanges.
     3. Premature Scraping / Timeout: The collector attempts to read canvas/table before the spinner disappears.
   - *Defensive Parquet Dumping Architecture*:
     * **Empty-State Sentinel**: Explicitly inspect DOM for `.ant-empty`, SVG sad-face icons, or `"no data"` text.
     * **Snapshot Retention Invariant**: If a live page returns "no data" or fails hydration after 3 adaptive retries, **NEVER overwrite healthy parquet data with empty records**. Preserve the last verified snapshot and record an explicit telemetry warning.
     * **Tab Recycling & Exponential Backoff**: Implement automatic tab reload and 3-stage exponential backoff (2s, 5s, 10s) before flagging a feed as stale.

---

## 2. Multi-Agent Orchestration Roster (Phase 2 Execution)

Under the `/orchestrate` protocol, Phase 2 execution will deploy 3 specialized subagents in parallel groups:

| Agent # | Role & Specialist | Domain Scope | Concrete Action & Deliverables |
| :--- | :--- | :--- | :--- |
| **Agent 1** | **`code-explorer`** | **DOM & Selector Discovery** | Probe all 20 browser collector pages on active Chrome CDP port 9222. Map updated CSS classes, container elements, and React fiber nodes for each page. |
| **Agent 2** | **`code-architect`** | **Extractor Refactoring & Defensive Dumping** | Update `liquidation_maxpain_core.py` and `Collectors/Browser/` modules with adaptive dual-fallback selectors (semantic `table` + React Fiber + network interception) and the Snapshot Retention Guard. |
| **Agent 3** | **`test-engineer`** | **Test Harvest, Parquet Verification & Daemon Restart** | Run individual standalone test harvests for the repaired feeds, verify row counts and non-null constraints, and restart `Terminal/run_pipeline_continuous_daemon.py`. |

---

## 3. Detailed Work Breakdown & Implementation Blueprint

### Packet 1: `liquidation_maxpain_core.py` DOM Modernization
* **File**: [`Collectors/Core/liquidation_maxpain_core.py`](file:///c:/Users/SIGMA/Documents/Trading_2/Collectors/Core/liquidation_maxpain_core.py)
* **Edits**:
  - Replace `.ant-table` selector with `table, [class*="table"], .ant-table`.
  - Update React Fiber detection to inspect `document.querySelector('table')` and traverse both child and parent fiber branches.
  - Add text-based row parsing fallback (`tbody tr`) as a secondary extractor if fiber inspection is blocked by minification.
  - Implement direct CDP Network request interception for `/api/futures/liquidation/max-pain` to extract raw JSON directly from network responses if DOM structure changes again.

### Packet 2: Defensive Data Dumping & Empty-State Handling
* **File**: [`Terminal/Data_Factory/parquet_feed_writer.py`](file:///c:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/parquet_feed_writer.py) & Individual Collectors
* **Edits**:
  - Add `validate_feed_payload(records, min_rows=1, allow_empty=False)` gate.
  - If a scraper extracts 0 rows or detects "no data" UI:
    1. Log warning: `[EMPTY_STATE_DETECTED] Feed {sheet_name} returned no data`.
    2. Read existing parquet file if present; if existing file has > 0 rows and age < 60m, preserve existing records and update only `banner_ist` with `STATUS: PRESERVED_PREVIOUS_SNAPSHOT`.
    3. Never write a 0-row parquet file that wipes out analytical models.

### Packet 3: Full 20-Feed Browser CDP Audit
* **Audit Target**: All scripts in `Collectors/Browser/`:
  - `1_Crypto_ETF_Flows.py` (`https://www.coinglass.com/etf`)
  - `2_Spot_Netflow_S.py` (`https://www.coinglass.com/spot-inflow-outflow`)
  - `3_Exchanges_LS_Ratio_*.py` (`https://www.coinglass.com/LongShortRatio`)
  - `4_Hyperliquid_Analysis.py` (`https://www.coinglass.com/hl`)
  - `5_OI.py`, `5_Funding_Rate.py`, `6_Funding_Fee_Settlement.py`
  - `7_Liq_Heapmap.py`, `7_Live_Liq.py`
  - `8_Exchange_Liquidation_Map_1D.py` & `7D.py` (`https://www.coinglass.com/pro/futures/LiquidationMap`)
  - `10_Whale_Orders.py` (`https://www.coinglass.com/large-orderbook-statistics`)
  - `19_News.py`, `19_Calendar.py`
  - `25_CoinGlass_Footprint_Signals.py`, `26_Aggregated_Footprint_Bar_Metrics.py`

### Packet 4: Single-Run Validation & Daemon Re-Launch
* Execute test run on:
  - `python Collectors/Browser/9_Liquidation_Max_Pain_24H.py`
  - `python Collectors/Browser/8_Exchange_Liquidation_Map_1D.py`
* Verify resulting `.parquet` files in `Data/feeds/`: row count > 0, monotonic timestamps, 0 nulls in key columns.
* Re-launch `python Terminal/run_pipeline_continuous_daemon.py --gap 120` as `IsDaemon=true`.

---

## 4. Verification & Exit Gates
1. ✅ `coinglass-cdp-dom-repair-plan.md` created and approved by user.
2. ✅ Live CDP inspection passes for all 20 CoinGlass endpoints without `no table` or `timeout` errors.
3. ✅ Max Pain feeds (`9_Liquidation_Max_Pain_*.parquet`) successfully extract ~750 rows per timeframe.
4. ✅ Pipeline continuous daemon safely restarted and verified running.
