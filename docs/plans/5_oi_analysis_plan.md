# Implementation Plan: Module 5 Open Interest (`5_OI.py`)

## 1. Overview & Objective
Build and deploy dedicated Excel Module 5: `5_OI.py` and worksheet `5_OI` in `Data/DataBase_Trading.xlsx` to extract real-time Futures Open Interest (OI) from CoinGlass (`https://www.coinglass.com/open-interest/<ASSET>`) across all 18 institutional universe assets (`BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB`).

Per operator specifications:
- **Exchanges in Columns & Assets in Rows**: Provide a clean cross-exchange Open Interest matrix table with Assets as rows and Exchanges (Total/All, Binance, Bybit, OKX, CME, KuCoin, Gate, Bitget, BingX, MEXC, Bitunix, Hyperliquid, Others) as columns.
- **Stacked Assets Data**: Provide the full granular breakdown with all assets stacked vertically, detailing every exchange's token OI, USD OI, market share (%), 1h/4h/24h OI percentage changes, and OI/24h Volume ratio.
- **Visual & Color Parity**: Emerald Green (`#00A86B`) for positive OI growth, Crimson Red (`#E53935`) for OI declines, dark institutional headers (`#161B22`), and thin borders.
- **Tab Hygiene & Shield**: Runs via ephemeral CDP tab on port 9222, unconditionally closes tab in `finally:` block, preserves `arena.ai` untouched, and routes via Cloudflare WARP Anycast.
- **Master Pipeline Integration**: Registered into `Data/Excel_Modules/Run_Pipeline.py`.

---

## 2. Requirements & Acceptance Criteria
1. **Target URL Pattern**: `https://www.coinglass.com/open-interest/{asset}`
2. **Target File**: `Data/Excel_Modules/5_OI.py`
3. **Target Worksheet**: `5_OI` in `Data/DataBase_Trading.xlsx` (positioned at Index 6, sequentially after `4_Hyperliquid_Analysis`).
4. **Institutional Universe (18 Assets)**:
   `BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB`.
5. **Dual Institutional Layouts in Sheet `5_OI`**:
   - **Section 1: Open Interest Exchange Matrix (Assets in Rows, Exchanges in Columns)**:
     - Columns: `Asset`, `Total OI (USD)`, `Binance`, `Bybit`, `OKX`, `CME`, `KuCoin`, `Gate`, `Bitget`, `BingX`, `MEXC`, `Bitunix`, `Hyperliquid`, `Others`, `24h Total Change (%)`, `Timestamp (UTC)`.
     - Rows: All 18 institutional assets.
   - **Section 2: Comprehensive Stacked Granular Dataset**:
     - Columns: `Asset`, `Rank`, `Exchange`, `OI (Tokens)`, `OI (USD)`, `Market Share (%)`, `OI Change (1h)`, `OI Change (4h)`, `OI Change (24h)`, `OI / 24h Vol`, `Timestamp (UTC)`.
     - Rows: All exchanges for each asset stacked sequentially (~20-25 rows per asset = ~350-400 total rows).
6. **Data Extraction & DOM Targeting**:
   - Fixed header is `.ant-table-header table`.
   - Data rows are in `.ant-table-body table`.
   - Skip row 0 (Ant Design measurement spacer row).
   - Row 1 is the aggregated "All" row; Rows 2+ are individual exchange rows.
   - Extract raw numeric and formatted string values for accurate sorting and matrix aggregation.
7. **Pipeline Registration**:
   - Registered as Module 7 in `Data/Excel_Modules/Run_Pipeline.py`.

---

## 3. Multi-Agent Orchestration Structure
In accordance with `/orchestrate` protocol and canonical agent directives, this task coordinates 3 distinct personas:

| # | Agent Persona | Domain / Focus Area | Mandate & Status |
|---|---|---|---|
| 1 | **Lead Architect / Project Planner** | Planning & Schema Design | Analyzed user requirements, formulated dual matrix and stacked layout architecture, authored implementation plan. |
| 2 | **Data Reverse-Engineer** | DOM Extraction & Matrix Engine | Inspects `.ant-table-body table`, builds rapid 18-asset traversal loop via CDP, implements pivot matrix aggregation, writes `5_OI.py`. |
| 3 | **QA & Verification Engineer** | Workbook Audit & Pipeline Integration | Audits worksheet placement (Index 6), verifies row and column counts, validates tab hygiene (`arena.ai` preserved), and registers module in `Run_Pipeline.py`. |

---

## 4. Execution Roadmap
- **Step 1: DOM & Selector Verification**:
  - Connect to `https://www.coinglass.com/open-interest/XRP`.
  - Confirm table body selector `.ant-table-body table` and field extraction offsets (`Ranking`, `Exchanges`, `OI Tokens`, `OI USD`, `Rate`, `1h`, `4h`, `24h`, `OI/Vol`).
- **Step 2: Script Construction (`5_OI.py`)**:
  - Implement async CDP communication via websockets.
  - Implement sequential loop across all 18 institutional assets with dynamic DOM readiness verification.
  - Pivot exchange values into the Matrix table and compile the Stacked dataset.
  - Apply openpyxl institutional styling (dark header, green/red conditional colors, gridlines, auto column widths).
- **Step 3: Verification & Workbook Audit**:
  - Run `5_OI.py` standalone.
  - Audit `Data/DataBase_Trading.xlsx` to confirm sheet `5_OI` is created at Index 6 with both Matrix and Stacked sections populated.
- **Step 4: Master Pipeline Integration**:
  - Register Module in `Data/Excel_Modules/Run_Pipeline.py`.
  - Test via `Run_Pipeline.py --only 7`.
