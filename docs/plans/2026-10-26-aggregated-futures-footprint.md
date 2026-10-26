# Aggregated Futures Footprint & Bar Metrics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Overview
This plan establishes a continuous, multi-venue orderflow intelligence engine extracting:
1. **Perp Aggregated Futures Signals**: 100% of signals under the "Signals" tab across all timeframes (15m, Volume, Range bars) for all universe assets without missing any coin.
2. **Granular Footprint Bar Metrics (Bottom Pane Time-Series)**: Continuous bar-by-bar orderflow stats table (Volume, Buy/Sell Volume, Delta, Delta %, Max/Min Delta, Cumulative Delta, Trades, Avg Size, Open Interest, OI Change, VAH, VAL, POC, VWAP).
3. **Unified Schema Parity**: Direct capture for crypto perpetuals via CoinGlass CDP / internal API, bridged with MT5 CVD and tick orderflow for macro CFDs (NAS100, SP500, USWTI, EURUSD, GBPUSD).

---

## Architecture & Data Flow

```
                      +------------------------------------------+
                      |   CoinGlass Aggregated Futures Footprint |
                      |   (Binance + OKX + Bybit + Hyperliquid)  |
                      +------------------------------------------+
                                           |
                    +----------------------+----------------------+
                    |                                             |
                    v                                             v
       [Signals Tab Intelligence]                    [Bottom Bar Metrics Pane]
     - Absorption (Limit Walls)                    - Bar Volume & Buy/Sell Split
     - Trapped Longs / Shorts                      - Bar Delta & Delta %
     - Exhaustion (Buyer/Seller)                   - Max / Min Delta Excursions
     - Delta Divergences (CVD vs P)                - Cumulative Delta
     - Bull / Bear Div swings                      - Trades Count & Avg Size
                    |                              - Open Interest & OI Change
                    v                              - VAH, VAL, POC, Session VWAP
     +------------------------------+                             |
     | 25_CoinGlass_Footprint_      |                             v
     | Signals.parquet              |              +------------------------------+
     +------------------------------+              | 26_Aggregated_Footprint_     |
                                                   | Bar_Metrics.parquet          |
                                                   +------------------------------+
```

---

## Task Breakdown

### Phase 1: Aggregated Futures Universe Census & Signal Expansion
- [ ] **Task 1.1**: Update `Collectors/Browser/25_CoinGlass_Footprint_Signals.py` to target `Perp Aggregated futures` explicitly.
  - Verify that every navigation defaults to or selects `Aggregated futures` across all exchanges.
  - Expand universe asset list:
    `["BTC", "ETH", "SOL", "XRP", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "XAU", "SPX", "AAVE", "UNI", "ZEC", "TAO", "WLD", "ENA"]`.
- [ ] **Task 1.2**: Capture 100% of signals across all 3 bar types under the Signals tab:
  - Extract `All` signals (not just 15m; include Volume bars and Range bars).
  - Extract exact metadata: Timestamp, Bar Type, Signal Type, Bias, Headline, Detailed Description, Price Level, Absorbed Volume ($).
  - Validate with test run and verify zero missing assets.

### Phase 2: Continuous Bar-by-Bar Orderflow Metrics Engine (Feed 26)
- [ ] **Task 2.1**: Build `Collectors/Browser/26_Aggregated_Footprint_Bar_Metrics.py`:
  - Harvest the complete time-series of the bottom orderflow pane for each bar:
    - `timestamp_ist`, `symbol`, `interval`
    - `volume_usd`, `buy_volume_usd`, `sell_volume_usd`
    - `delta_usd`, `delta_pct`, `max_delta_usd`, `min_delta_usd`
    - `cumulative_delta_usd`, `trades_count`, `avg_trade_size`
    - `open_interest_usd`, `oi_change_usd`
    - `vah_price`, `val_price`, `poc_price`, `vwap_price`
  - Ingest directly from CoinGlass aggregated endpoints:
    `https://capi.coinglass.com/api/orderFlow` and `https://capi.coinglass.com/api/v2/kline?symbol=...#oi_kline` within the authenticated CDP session.
- [ ] **Task 2.2**: Integrate MT5 Macro CFD footprint bridging:
  - For traditional assets (`NAS100.p`, `SP500.p`, `USWTI.p`, `EURUSD.pi`, `GBPUSD.pi`), calculate and append identical orderflow bar metrics from `18_CVD.parquet`, `20_Auction_Market_Structure.parquet`, and `21_Tradfye_Orderflow.parquet`.
  - Output to `Data/feeds/26_Aggregated_Footprint_Bar_Metrics.parquet`.

### Phase 3: Pipeline Integration & Scorecard Telemetry
- [ ] **Task 3.1**: Register Feed 26 in `Data/metadata/parquet_all_feeds_checklist.json` and `Terminal/parquet_checklist_auditor.py`.
- [ ] **Task 3.2**: Add `26_Aggregated_Footprint_Bar_Metrics.py` to `Terminal/run_master_pipeline.py`.
- [ ] **Task 3.3**: Execute verification suite and confirm that all 34 feeds audit 100% green with 0 errors.

### Phase 4: Strategy Confluence Integration (Model 1 & Model 2)
- [ ] **Task 4.1**: Connect `Absorption` and `Exhaustion` signals to Model 1 Mean Reversion gates (|Z| >= 2.0 SD) in `Engine/s1_liquidation_cascade.py`.
- [ ] **Task 4.2**: Connect `Trapped longs` / `Trapped shorts` and `OI change` expansion to Model 2 Trend Following pullback gates (|Z| < 2.0 SD).
- [ ] **Task 4.3**: Sync dual-repo parity via `python .agents/scripts/verify_and_sync_agents.py`.

---

## Verification Checklist
1. `25_CoinGlass_Footprint_Signals.parquet` has all 26+ universe assets with `Aggregated futures` attribution.
2. `26_Aggregated_Footprint_Bar_Metrics.parquet` populated with granular bar time-series (Volume, Delta, Max/Min Delta, OI change).
3. Scorecard auditor validates freshness < 5.0m across all feeds.
4. Parity script confirms 21,133+ files matched with 0 byte mismatches.
