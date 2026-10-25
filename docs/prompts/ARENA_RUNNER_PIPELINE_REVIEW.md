# 🏛️ INSTITUTIONAL CODE AUDIT & PIPELINE REVIEW: CONTINUOUS EXCEL RUNNER & HARVESTER SUITE

**Target Models:** Arena.ai (Claude 3.7 Sonnet / Opus 5.5 / DeepSeek R1 / GPT-4o) & Z.ai (GLM-5.3-Flash)  
**Repository:** `https://github.com/kbsingh1399/Trading_2` (Branch: `main`, Latest Commit: `d57ef48d8`)  
**Mission:** Pass Blueberry Markets Phase 1 5,000 USD Evaluation (Account #5064568) with 100% automated floor defense (< 4,600.00 USD Hard Floor) powered by a real-time 32-sheet quant workbook (`DataBase_Trading.xlsx`).

---

## 1. EXECUTIVE CONTEXT & ARCHITECTURAL OVERVIEW

We operate an institutional high-frequency quantitative crypto futures desk trading 18 Binance USDT-Margined perpetual contracts (`BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB`). 

The desk's tactical decision engine relies on a unified 5.85 MB Excel workbook (`Data/DataBase_Trading.xlsx`) comprising 32 specialized telemetry worksheets, ranging from MT5 account telemetry and CVD aggregations to CoinGlass liquidation maps and orderbook microstructure depth. 

To maintain sub-5-minute freshness across all 32 sheets without human intervention, we engineered an autonomous multi-process harvesting pipeline executed via `Data/Excel_Modules/runner.py`.

### Core Pipeline Topology
1. **Runner Orchestrator (`Data/Excel_Modules/runner.py`)**:
   - Executes continuous cycles (`--continuous --stale --interval 120`).
   - Categorizes 32 modules into two execution pools:
     * **API Pool** (15 modules): MT5, Binance REST/WebSocket, Hyperdash GraphQL, Tradfye, Technicals.
     * **Browser/CDP Pool** (17 modules): CoinGlass scrapers operating over Chrome DevTools Protocol (CDP port 9222).
   - Manages subprocess timeouts (120s–180s) and cleans orphaned Edge tabs via `reap_scraping_tabs()`.

2. **Reentrant Lock Hook (`Data/Excel_Modules/excel_lock_hook.py` & `sitecustomize.py`)**:
   - Solves Windows NTFS multi-process file contention (`PermissionError: [WinError 32]`).
   - Implements `ReentrantFileLock` with thread-local depth tracking (`_tls.depth`) to eliminate self-deadlocks.
   - Intercepts `openpyxl.load_workbook` to read binary data into memory (`io.BytesIO`) under a transient ~5ms lock, immediately releasing the Windows file handle.
   - Directs all workbook saves to unique temporary files (`DataBase_Trading_<pid>_<ts>.tmp.xlsx`), followed by an atomic rename (`Path.replace`) under a ~50ms lock.
   - Automatically loaded into every spawned Python process via `sitecustomize.py`.

3. **CoinGlass Scrapers (`Data/Excel_Modules/3_Exchanges_LS_Ratio_15M.py`, `1H.py`, `4H.py`)**:
   - Extracts live exchange-by-exchange Long/Short ratios and taker volume across all 18 universe assets.
   - Uses Edge CDP over `websockets` to open a dedicated ephemeral tab.
   - Interacts with Material UI (MUI) components: scopes timeframe dropdown selection via `aria-controls` listbox matching (`"15 minute"`, `"1 hour"`, `"4 hour"`).
   - Employs 40-step progressive DOM readiness polling with automatic single-reload fallback to eliminate Next.js hydration stalls.

---

## 2. CANONICAL CODE REPOSITORY ARTIFACTS (MAIN BRANCH)

Please inspect the following production files directly from GitHub:
- **Runner Daemon**: [Data/Excel_Modules/runner.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/runner.py)
- **Lock Hook**: [Data/Excel_Modules/excel_lock_hook.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/excel_lock_hook.py)
- **Sitecustomize Auto-Hook**: [Data/Excel_Modules/sitecustomize.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/sitecustomize.py)
- **15M LS Ratio Module**: [Data/Excel_Modules/3_Exchanges_LS_Ratio_15M.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/3_Exchanges_LS_Ratio_15M.py)
- **1H LS Ratio Module**: [Data/Excel_Modules/3_Exchanges_LS_Ratio_1H.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/3_Exchanges_LS_Ratio_1H.py)
- **4H LS Ratio Module**: [Data/Excel_Modules/3_Exchanges_LS_Ratio_4H.py](https://github.com/kbsingh1399/Trading_2/blob/main/Data/Excel_Modules/3_Exchanges_LS_Ratio_4H.py)
- **Checklist Auditor**: [Terminal/Data_Factory/excel_sheet_checklist_auditor.py](https://github.com/kbsingh1399/Trading_2/blob/main/Terminal/Data_Factory/excel_sheet_checklist_auditor.py)

---

## 3. CORE AUDIT QUESTIONS & QUANT/SYSTEMS CHALLENGES

Please conduct an exhaustive, peer-level review across the following 5 dimensions:

### A. Concurrency & Lost Update Prevention under Monolithic Openpyxl
In openpyxl, `load_workbook` loads the entire 32-sheet workbook into memory. When Process A modifies Sheet 1 and Process B modifies Sheet 2 concurrently:
- If Process A and Process B both load `DataBase_Trading.xlsx` at T=0:
  - Process A writes Sheet 1 and atomically replaces the file at T=10s.
  - Process B writes Sheet 2 and atomically replaces the file at T=15s.
  - **Does Process B overwrite and wipe out Process A's Sheet 1 update because Process B's in-memory workbook reflects the T=0 snapshot?**
- What is the most elegant, robust architectural pattern to eliminate this "lost update" race condition without degrading throughput? Should the critical section encompass `load -> mutate -> save`, or should writers be strictly serialized through a single writer daemon / queue?

### B. Windows NTFS Locking & Atomic File Replacement
- Windows handles file locking aggressively. While `excel_lock_hook.py` uses `ReentrantFileLock` around `Path.replace(target)`, what happens if an external reader (e.g. an analyst viewing Excel or a background auditor) opens the workbook with shared read permissions (`FILE_SHARE_READ`)?
- Under Windows NTFS, does `os.replace` fail with `PermissionError: [WinError 32]` if a read handle is active? How can we harden `locked_path_replace` against persistent reader collisions?

### C. Chrome/Edge CDP Automation Resilience & Anti-Stall
- In `3_Exchanges_LS_Ratio_*.py`, each script navigates across 18 assets sequentially in an ephemeral tab.
- Could rapid `Page.navigate` calls trigger rate limiting, WebSocket disconnects, or memory leaks in the browser process?
- Between ephemeral tabs (`/json/new` and `/json/close`) vs reusing a single long-lived background tab with client-side history navigation, which yields superior stability and speed under continuous 24/7 operation?
- Are there any edge cases where CoinGlass DOM updates (such as dynamic class obfuscation or virtualized DOM tables) could cause row extraction to return incomplete data?

### D. Memory & CPU Scalability
- Loading and saving a 5.85 MB openpyxl workbook consumes ~250MB–400MB RAM and 1.5s–3.0s CPU time per run.
- With 32 modules running every few minutes, memory pressure can spike significantly.
- Would you recommend decoupling data collection into fast per-sheet Parquet/SQLite storage, paired with an incremental Excel sync engine, or optimizing openpyxl via `read_only=True` / `write_only=True`?

### E. Scheduler Optimization & Freshness SLA (< 5.0m Target)
- Currently, `runner.py` uses a simple batch execution loop with `max_workers=2` and a 120s sleep interval.
- Sheets have wildly different velocity requirements:
  * High Velocity (< 1m): MT5 Account Telemetry, Live Liquidations, CVD, Forced Liq.
  * Medium Velocity (< 5m): Long/Short Ratio, Funding Rates, Open Interest, Heatmaps.
  * Low Velocity (< 30m): Macro Calendar, News, ETF Flows.
- Design an optimal scheduling architecture (e.g., priority heap, token bucket, or asyncio task worker pool) that mathematically guarantees sub-5m freshness across all 32 sheets with minimal CPU overhead.

---

## 4. DELIVERABLE REQUIREMENTS

1. **Executive Verdict**: Summary of architectural strengths and critical vulnerabilities.
2. **Specific Bug Findings & Flaw Analysis**: Detailed breakdown of any race conditions, memory leaks, or selector fragility.
3. **Concrete Code Recommendations**: Production-ready code snippets or refactored functions for `runner.py`, `excel_lock_hook.py`, and the harvester modules.
4. **Targeted Freshness Architecture**: Concrete blueprint to maintain 100% PASS (< 5.0m) across all 32 sheets indefinitely.
