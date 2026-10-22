# Project Plan: Liquidation Map & Max Pain Data Harvesting Pipeline

## Executive Overview
Automate high-fidelity extraction of CoinGlass Liquidation data into `Data/DataBase_Trading.xlsx`:
1. **Source 1: Exchange Liquidation Map** (`https://www.coinglass.com/pro/futures/LiquidationMap`):
   - Sheets to create: `Exchange_Liquidation_Map_1D` and `Exchange_Liquidation_Map_7D`.
   - Harvests multi-exchange liquidation leverage across Binance, OKX, Bybit, plus Cumulative Long & Cumulative Short curves.
   - Core Assets to harvest: Canonical perpetuals (`BTC`, `ETH`, `SOL`, `XRP`, `DOGE`, `BNB`, `HYPE`, etc.).
2. **Source 2: Liquidation Max Pain** (`https://www.coinglass.com/liquidation-maxpain`):
   - Sheets to create: `liquidation_maxpain_1D` (24h tab) and `liquidation_maxpain_2D` (48h tab).
   - Complete candidate extraction across all 15 pagination pages (~745 crypto assets) using React Fiber `onChange(page)` so zero candidates are missed.
   - Exact columnar schema matching user screenshots (Ranking, Symbol, Price, Short Max Pain, Short Distance, Long Max Pain, Long Distance).

---

## Phase 1: Technical Architecture & Reverse Engineering (Verified via CDP)

### 1.1 Exchange Liquidation Map DOM & ECharts Specs
- **Target Chart**: Second ECharts instance on `/pro/futures/LiquidationMap` ("Exchange Liquidation Map").
- **Series Names**:
  - `Binance` (Bar - Orange)
  - `OKX` (Bar - Yellow)
  - `Bybit` (Bar - Blue)
  - `Cumulative Short Liquidation Leverage` (Line - Teal/Green)
  - `Cumulative Long Liquidation Leverage` (Line - Crimson/Red)
- **Current Price**: Extracted from `opt.series[].markLine.data[0].xAxis` (e.g. `2413.9` for ETH).
- **Asset Switching**: MUI Autocomplete (`.MuiAutocomplete-root`), triggering `cur.memoizedProps.onChange(null, assetSymbol, 'selectOption')`.
- **Timeframe Switching**: Target listbox scoped by `aria-controls` (`1 day` vs `7 day`).

### 1.2 Liquidation Max Pain DOM & Pagination Specs
- **Target Page**: `https://www.coinglass.com/liquidation-maxpain`.
- **Tabs**: Joy UI Tab buttons (`24 hour` for 1D, `48 hour` for 2D).
- **Pagination**: Ant Design Pagination (`.ant-pagination`), total 745 items across 15 pages (50 items/page).
- **Deterministic Multi-Page Harvesting Loop**: Call `cur.memoizedProps.onChange(pageNum)` for `pageNum` in `1..15`, wait 800ms for DOM re-render, and accumulate rows until all ~745 candidates are collected.
- **Columns to Extract & Format**:
  1. `Ranking` (Integer)
  2. `Symbol` (e.g. `BTC`, `ETH`, `SOL`)
  3. `Market Price` (Currency string, e.g. `$81,980.00`)
  4. `Short Max Pain Price` (e.g. `$82,427.50`)
  5. `Short Max Pain Vol` (e.g. `$79.54M`)
  6. `Short Distance (USD)` (e.g. `+$447.50`)
  7. `Short Distance (%)` (e.g. `+0.55%`, font green)
  8. `Long Max Pain Price` (e.g. `$80,100.00`)
  9. `Long Max Pain Vol` (e.g. `$66.33M`)
  10. `Long Distance (USD)` (e.g. `-$1,880.00`)
  11. `Long Distance (%)` (e.g. `-2.29%`, font red)

---

## Phase 2: Sheet Specifications & Columnar Layout

### Sheet 1 & 2: `Exchange_Liquidation_Map_1D` & `Exchange_Liquidation_Map_7D`
- **Banner**: Row 1 Section Banner: `COINGLASS DERIVATIVES ANALYTICS - EXCHANGE LIQUIDATION MAP ({TIMEFRAME}) - STACKED ASSET-WISE`
- **Headers**:
  `Sr.No | Asset | Timeframe | Current Price (USD) | Price Level (USD) | Binance Leverage (USD) | OKX Leverage (USD) | Bybit Leverage (USD) | Total Exchange Leverage (USD) | Cumulative Long Leverage (USD) | Cumulative Short Leverage (USD)`
- **Data Stacking**: Assets stacked one below another with distinct section divider headers.

### Sheet 3 & 4: `liquidation_maxpain_1D` & `liquidation_maxpain_2D`
- **Banner**: Row 1 Section Banner: `COINGLASS CRYPTOCURRENCY LIQUIDATION MAX PAIN ({TIMEFRAME}) - ALL CANDIDATES ({COUNT} ASSETS)`
- **Headers**:
  `Ranking | Symbol | Market Price | Short Max Pain Price | Short Max Pain Vol | Short Distance ($) | Short Distance (%) | Long Max Pain Price | Long Max Pain Vol | Long Distance ($) | Long Distance (%)`
- **Formatting**:
  - Frozen panes at `C3` (Ranking & Symbol fixed).
  - Conditional font colors: Green for positive distances, Red for negative distances.
  - Alternating light gray zebra rows (`#F9FAFB`).

---

## Phase 3: Step-by-Step Implementation Roadmap

1. **Task 1: Build Liquidation Map Multi-Asset Harvester (`scratch/harvest_liq_map.py`)**:
   - Navigate to `/pro/futures/LiquidationMap`.
   - Iterate across target assets (`BTC`, `ETH`, `SOL`, `XRP`, `DOGE`, `BNB`, `HYPE`).
   - For each asset, extract `1 day` (1D) and `7 day` (7D) ECharts series and current price.
2. **Task 2: Build Liquidation Max Pain Multi-Page Harvester (`scratch/harvest_maxpain.py`)**:
   - Navigate to `/liquidation-maxpain`.
   - Select `24 hour` tab, iterate through pages 1..15, extract all ~745 candidates.
   - Select `48 hour` tab, iterate through pages 1..15, extract all ~745 candidates.
3. **Task 3: Excel Workbook Assembly (`scratch/build_liquidation_and_maxpain_sheets.py`)**:
   - Write `Exchange_Liquidation_Map_1D` and `Exchange_Liquidation_Map_7D`.
   - Write `liquidation_maxpain_1D` and `liquidation_maxpain_2D`.
   - Apply professional financial typography, borders, zebra striping, and auto-fit column widths.
4. **Task 4: Cross-Verification & Validation**:
   - Compare extracted values against user screenshots:
     - `ETH 1D`: Current price ~`$2,413.1`, bar at `2451.4` (Binance `$21.58M`, OKX `$17.45M`, Bybit `$5.31M`, Cum Short `$368.67M`).
     - `XRP 7D`: Current price ~`$1.296`, bar at `1.323` (Binance `$3.50M`, OKX `$3.21M`, Bybit `$8.37M`, Cum Short `$63.27M`).
     - `Max Pain 24h & 48h`: BTC ranking 1, ETH ranking 2, SOL ranking 3 with exact pain prices and distances.
   - Run Microsoft Excel COM verification (`win32com.client.Dispatch('Excel.Application')`) for 0 errors/warnings.
5. **Task 5: Cleanup & History Commit**:
   - Prune all scratch scripts per Part 4 Rule 4.
   - Append execution logs to `session_chat_history.md`.
