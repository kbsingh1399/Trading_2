# Implementation Plan: Perpetual Futures Funding Fee Settlement Data Scraper & Excel Dumper

## Executive Summary
This plan details the design, engineering, and verification of a dedicated high-fidelity scraping module `Data/Excel_Modules/6_Funding_Fee_Settlement.py` and its corresponding target worksheet `6_Funding_Fee_Settlement` inside `Data/DataBase_Trading.xlsx`. The module harvests the complete **Funding Fee Settlement Overview** table across all 19 pages (~950+ cryptocurrency pairs) from [CoinGlass Funding Fees](https://www.coinglass.com/funding-fees) using Chrome DevTools Protocol (CDP) on port 9222 under Cloudflare WARP Anycast protection, with strict browser tab hygiene preserving `arena.ai`.

---

## 1. Architectural Specifications & Data Schema

### 1.1 Source & Page Attributes
- **Target URL**: `https://www.coinglass.com/funding-fees`
- **Component**: `.ant-table-wrapper` containing `.ant-table-header` and `.ant-table-body`
- **Total Depth**: 19 pages (~50 assets per page, ~950+ total crypto assets)
- **Pagination**: `.ant-pagination` with active items, Next button `li.ant-pagination-next:not(.ant-pagination-disabled)`

### 1.2 Extracted Column Schema
| Column Index | Field Name | Description | Example | Alignment |
|---|---|---|---|---|
| A | `#` (Rank) | Integer ranking | 1 | Right |
| B | `Symbol` | Cryptocurrency asset ticker | BTC | Left |
| C | `Price` | Live reference market price | $82,562.10 | Right |
| D | `Price (24h%)` | 24-hour price change percentage | +0.79% | Right |
| E | `Open Interest` | Current aggregate futures open interest | $16.84B | Right |
| F | `Current` | Current funding fee settlement amount | $1.33M | Right |
| G | `Last 24h` | Cumulative funding fee paid/received (24h) | $2.97M | Right |
| H | `Last 3 Days` | Cumulative funding fee paid/received (3d) | $8.48M | Right |
| I | `Last 7 Days` | Cumulative funding fee paid/received (7d) | $16.02M | Right |
| J | `Timestamp (UTC)` | Extraction timestamp in ISO UTC | 2026-10-19 19:35:00 UTC | Center |

---

## 2. Scraping & Automation Strategy

1. **CDP Ephemeral Tab Lifecycle**:
   - Query `http://127.0.0.1:9222/json/new?https://www.coinglass.com/funding-fees` (method: `PUT`).
   - Connect via `websockets.connect` with 25MB max frame size.
   - Wait for `.ant-table-tbody tr:not(.ant-table-measure-row)` to render 50 rows.
   - For page 1 to `max_pages` (19):
     * Extract all 50 row cells in a single JavaScript `Runtime.evaluate` pass (<0.02s per page).
     * Check for next page button `li.ant-pagination-next:not(.ant-pagination-disabled)`.
     * Dispatch `.click()` event on next button, wait for row transition via hash/content check.
   - Close ephemeral tab in `finally:` block via `http://127.0.0.1:9222/json/close/{tab_id}`.
   - Strictly guarantee that `arena.ai` (`https://arena.ai/agent`) is preserved untouched.

2. **Parsing & Clean Tokenization**:
   - Clean currency symbols (`$`, `K`, `M`, `B`) while retaining readable string representation and raw values where applicable.
   - Parse percentage signs and signs (`+`, `-`) for color highlighting.
   - Deduplicate rows while preserving exact ranking order.

---

## 3. Excel Worksheet Layout & Typography

1. **Worksheet Placement**:
   - Workbook: `Data/DataBase_Trading.xlsx`
   - Sheet Name: `6_Funding_Fee_Settlement`
   - Position: Index 8 (immediately following `5_Funding_Rate` at Index 7).
   - Downstream sheets (`Top_Institutions`, `ETF_Market_Overview`, etc.) fully preserved.

2. **Styling Rules**:
   - Header Row (Row 1): Deep Midnight Slate `#0F172A`, bold white text (`#FFFFFF`), 11pt Calibri, centered/aligned.
   - Row Height: Header 28pt, Data Rows 20pt.
   - Borders: Thin light-slate gridlines (`#E2E8F0`).
   - Conditional Color Formatting:
     * Positive Price Change & Positive Funding: Soft Emerald Green `#059669`.
     * Negative Price Change & Negative Funding: Soft Crimson Red `#DC2626`.
     * Rank & Symbol: Deep Charcoal `#1E293B`, bold for symbols.
   - View Configuration: Freeze top row (`freeze_panes = 'A2'`), enable auto-fit column widths + padding.

---

## 4. Pipeline Integration & Verification

1. **Register Module in `Data/Excel_Modules/Run_Pipeline.py`**:
   - Register as Module 9:
     ```python
     {
         "id": 9,
         "name": "Perpetual Futures Funding Fee Settlement",
         "script": MODULES_DIR / "6_Funding_Fee_Settlement.py",
         "sheet": "6_Funding_Fee_Settlement",
         "expected_min_rows": 900,
         "args": ["--pages", "19"],
     }
     ```
   - Update `argparse` choices to `choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
2. **Dual-Gate Verification**:
   - Standalone run: `python Data/Excel_Modules/6_Funding_Fee_Settlement.py --pages 19`
   - Orchestrated pipeline run: `python Data/Excel_Modules/Run_Pipeline.py --only 9`
   - Excel workbook structure and row audit across all 51 sheets.
   - Browser tab audit: Edge port 9222 has 0 lingering scraper tabs and `arena.ai` is untouched.
