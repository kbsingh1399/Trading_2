# Implementation Plan: Module 4 Hyperliquid Whale Analysis (`4_Hyperliquid_Analysis.py`)

## 1. Overview & Objective
Build and deploy dedicated Excel Module 4: `4_Hyperliquid_Analysis.py` and worksheet `4_Hyperliquid_Analysis` in `Data/DataBase_Trading.xlsx` to extract real-time Hyperliquid whale positions from CoinGlass (`https://www.coinglass.com/hyperliquid`).
The extraction must capture the entire table across all pages (40 pages x 50 rows = up to 2,000 whale positions), recover the **full 42-character unmasked hexadecimal wallet address**, preserve exact UI formatting and color schemes (green for long/profit, red for short/loss), enforce strict tab hygiene (preserving `arena.ai`), and integrate into `Data/Excel_Modules/Run_Pipeline.py`.

---

## 2. Requirements & Acceptance Criteria
1. **Target URL**: `https://www.coinglass.com/hyperliquid`
2. **Target File**: `Data/Excel_Modules/4_Hyperliquid_Analysis.py`
3. **Target Worksheet**: `4_Hyperliquid_Analysis` in `Data/DataBase_Trading.xlsx` (positioned sequentially after the 3 Exchanges Long/Short Ratio sheets).
4. **Full Wallet Address Recovery**:
   - In CoinGlass UI, the user column displays an abbreviated address like `0x5b5d..60`.
   - The DOM elements (links `<a href="...">`, copy button attributes `data-clipboard-text`, or tooltips) contain the unmasked 42-character Ethereum address (`0x[a-fA-F0-9]{40}`).
   - Both the display handle and the verified full address must be captured and populated.
5. **Multi-Page Pagination Handling**:
   - Page 1 loads rows 1 to 50.
   - The bottom pagination controls `< 1 2 3 4 5 ... 40 >` allow sequential paging up to page 40.
   - The extraction engine will iterate through all available pages (with a configurable `--pages` flag, defaulting to all pages or 40 pages) until all positions are harvested with zero missing records.
6. **Complete Table Schema**:
   Exact columns mapped directly to CoinGlass UI + quantitative context:
   - `#`: Position Rank (1, 2, 3...)
   - `User`: Display address / name (`0x5b5d..60`)
   - `Wallet_Address`: Full 42-char hexadecimal wallet address (`0x...`)
   - `Assets`: Contract symbol (`ETH`, `BTC`, `HYPE`, `SOL`, `xyz:GOLD`, `NEAR`, etc.)
   - `Side`: Direction (`Long`, `Short`)
   - `Position`: Formatted size (`$257.67M / 106.35K ETH`)
   - `Unrealised_PNL`: Formatted PnL (`-$10.66M / -4.14%`)
   - `Entry_Price`: Entry Price & Leverage (`$2322.65 / 5X Cross`)
   - `Liq_Price`: Liquidation Price (`$4,109`)
   - `Margin`: Margin allocated (`$51.53M`)
   - `Funding_Fee`: Accrued funding fee (`$3.85M`, `-$902.72K`)
   - `Price`: Current Mark Price (`$2421.6`)
   - `Entry_Time`: Timestamp of entry (`05-09 21:18`)
   - `Timestamp_UTC`: Harvest timestamp (UTC)
7. **Excel Visual & Typographic Styling**:
   - Dark theme header (`#161B22`, pure white bold text).
   - Dynamic conditional font styling:
     - `Side`: Emerald Green (`#00A86B`) for Long, Crimson Red (`#E53935`) for Short.
     - `Unrealised_PNL`: Green for positive, Red for negative.
   - Alt+Enter multi-line cell formatting with `wrap_text=True` to match CoinGlass visual layout.
   - Auto-fit column widths with thin border gridlines.
8. **Tab Hygiene & Preserving Arena.ai**:
   - Connect via Chrome/Edge remote debugging protocol (port 9222).
   - Never close, navigate, or reload the `arena.ai` tab.
   - Always open a dedicated ephemeral tab for `https://www.coinglass.com/hyperliquid` and close it in a `finally:` block.
9. **Pipeline Integration**:
   - Register Module 4 into `Data/Excel_Modules/Run_Pipeline.py` as sequential Step 6.
   - Support `--rotate-ip`, `--fail-fast`, and post-execution sheet auditing.

---

## 3. Multi-Agent Orchestration Structure
In accordance with `/orchestrate` protocol and canonical agent directives, this task coordinates 3 distinct personas:

| # | Agent Persona | Responsibility |
|---|---|---|
| 1 | **Lead Architect / Project Planner** (`project-planner`) | Requirements specification, schema design, pagination state modeling, plan formulation. |
| 2 | **Data Reverse-Engineer** (`backend-specialist`) | CDP interaction, DOM parsing for full 42-char wallet addresses, pagination click & readiness loop, script implementation. |
| 3 | **QA & Verification Engineer** (`test-engineer`) | Execution testing, Excel sheet index & row count verification, non-arena tab cleanup audit, pipeline integration. |

---

## 4. Execution Roadmap
- **Step 1: DOM & Address Inspection**:
  - Connect via CDP to `https://www.coinglass.com/hyperliquid`.
  - Inspect the table DOM structure, the exact selectors for the wallet link/copy button containing the full address, and the pagination controls (`.ant-pagination-item`, `.ant-pagination-next`, or MUI buttons).
- **Step 2: Script Construction (`4_Hyperliquid_Analysis.py`)**:
  - Implement async CDP communication via websockets.
  - Implement dynamic readiness checks (waiting for table `tbody tr` >= 20).
  - Implement pagination loop: extract 50 rows per page, click next page button, wait for DOM update, repeat until all 40 pages (or user specified limit) are collected.
  - Implement openpyxl formatting engine writing to `Data/DataBase_Trading.xlsx`.
- **Step 3: Verification & Workbook Audit**:
  - Run `4_Hyperliquid_Analysis.py` standalone.
  - Verify sheet `4_Hyperliquid_Analysis` row count matches extracted records.
  - Confirm all 42-char addresses are fully populated without masking.
- **Step 4: Master Pipeline Integration**:
  - Update `Data/Excel_Modules/Run_Pipeline.py` to include `4_Hyperliquid_Analysis.py`.
  - Validate end-to-end execution with Cloudflare WARP Anycast protection.
