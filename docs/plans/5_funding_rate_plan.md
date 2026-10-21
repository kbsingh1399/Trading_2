# Implementation Plan: Module 5 Funding Rate (`5_Funding_Rate.py`)

## 1. Overview & Objective
Build and deploy dedicated Excel Module 5: `5_Funding_Rate.py` and worksheet `5_Funding_Rate` in `Data/DataBase_Trading.xlsx` to extract real-time Perpetual & Futures Funding Rates across all exchanges from CoinGlass (`https://www.coinglass.com/FundingRate`).

Per operator specifications:
- **Exact Tabular Layout**: Dump the complete funding rate comparison table as it is in the exact same tabular format across all exchanges, structured under dual super-headers: `USDT or USD Margined` and `Token Margined`.
- **All-Page Pagination Traversal**: Hit all pages till the end (30 pages x 20 assets = up to 600 crypto pairs) to scrape the entire dataset and append all rows sequentially without omitting any assets.
- **Visual & Color Parity**: Emerald Green (`#00A86B`) for positive funding rates (longs pay shorts), Crimson Red (`#E53935`) for negative funding rates (shorts pay longs), dark institutional headers (`#161B22` and `#21262D`), and thin border gridlines.
- **Tab Hygiene & Network Shield**: Executes in an isolated ephemeral CDP tab on port 9222, unconditionally closes tab in a `finally:` block, preserves `arena.ai` untouched, and routes through Cloudflare Anycast.
- **Master Pipeline Integration**: Registered into `Data/Excel_Modules/Run_Pipeline.py`.

---

## 2. Requirements & Acceptance Criteria
1. **Target URL**: `https://www.coinglass.com/FundingRate`
2. **Target File**: `Data/Excel_Modules/5_Funding_Rate.py`
3. **Target Worksheet**: `5_Funding_Rate` in `Data/DataBase_Trading.xlsx` (positioned sequentially after `5_OI` at Index 7).
4. **Complete Exchange Coverage (15 Exchanges)**:
   - **USDT or USD Margined (12 Exchanges)**: `Binance`, `OKX`, `Bybit`, `KuCoin`, `MEXC`, `BingX`, `Gate`, `Bitunix`, `Bitget`, `WhiteBIT`, `LBank`, `tradeXYZ`.
   - **Token Margined / Coin-M (3 Exchanges)**: `Binance`, `OKX`, `Bybit`.
5. **30-Page Exhaustive Traversal**:
   - Page size is 20 rows per page across 30 pagination pages (`< 1 2 3 ... 30 >`).
   - The engine iterates sequentially across all 30 pages, waiting for DOM readiness on each page transition, collecting 600+ unique asset rows.
6. **Detailed Table Schema**:
   - Header Row 1: Merged section banners (`USDT or USD Margined` across cols B-M, `Token Margined` across cols N-P).
   - Header Row 2:
     1. `Symbol`: Base token symbol (e.g. `BTC`, `ETH`, `SOL`, `XRP`, `HYPE`, `DOGE`...)
     2. `USDT Binance`
     3. `USDT OKX`
     4. `USDT Bybit`
     5. `USDT KuCoin`
     6. `USDT MEXC`
     7. `USDT BingX`
     8. `USDT Gate`
     9. `USDT Bitunix`
     10. `USDT Bitget`
     11. `USDT WhiteBIT`
     12. `USDT LBank`
     13. `USDT tradeXYZ`
     14. `Coin Binance`
     15. `Coin OKX`
     16. `Coin Bybit`
     17. `Timestamp (UTC)`: Harvest timestamp.
7. **Cell Formatting & Dynamic Color Coding**:
   - Positive funding rates: Emerald Green bold font (`#00A86B`).
   - Negative funding rates: Crimson Red bold font (`#E53935`).
   - Inactive / dash (`-`): Subdued gray (`#888888`).
   - Symbol column: Centered, bold.
   - All rates: Right-aligned.
   - Column auto-widths with Excel gridlines enabled.
8. **Pipeline Registration**:
   - Registered as Module 8 in `Data/Excel_Modules/Run_Pipeline.py`.

---

## 3. Multi-Agent Orchestration Structure
In accordance with `/orchestrate` protocol and canonical agent directives, this task coordinates 3 distinct personas:

| # | Agent Persona | Domain / Focus Area | Mandate & Status |
|---|---|---|---|
| 1 | **Lead Architect / Project Planner** | Planning & Schema Design | Analyzed user requirements, mapped 15-exchange dual-tier schema, designed 30-page traversal engine, authored implementation plan. |
| 2 | **Data Reverse-Engineer** | DOM Extraction & Traversal Engine | Targeted `.ant-table-body table` via CDP on port 9222, constructed pagination click loop across all 30 pages, writes `5_Funding_Rate.py`. |
| 3 | **QA & Verification Engineer** | Workbook Audit & Pipeline Integration | Audits worksheet placement (Index 7), verifies 600+ row count, validates tab hygiene (`arena.ai` preserved), and registers module in `Run_Pipeline.py`. |

---

## 4. Execution Roadmap
- **Step 1: DOM & Selector Verification**:
  - Connect to `https://www.coinglass.com/FundingRate`.
  - Target `.ant-table-body table`.
  - Filter out spacer rows and parse `Symbol` + 12 USDT-M exchanges + 3 Coin-M exchanges.
- **Step 2: Script Construction (`5_Funding_Rate.py`)**:
  - Implement async CDP communication via websockets.
  - Implement pagination loop: extract 20 rows per page, click `li.ant-pagination-next:not(.ant-pagination-disabled)`, wait for active page update, iterate through all 30 pages (up to 600 pairs).
  - Implement openpyxl formatting engine with dual-tier header and conditional green/red styling writing to `Data/DataBase_Trading.xlsx`.
- **Step 3: Verification & Workbook Audit**:
  - Run `5_Funding_Rate.py` standalone.
  - Audit `Data/DataBase_Trading.xlsx` to confirm sheet `5_Funding_Rate` is created at Index 7 with ~600 rows.
- **Step 4: Master Pipeline Integration**:
  - Register Module in `Data/Excel_Modules/Run_Pipeline.py`.
  - Test via `Run_Pipeline.py --only 8`.
