# 360° Data Lake Dossier: SOL
**Generated**: 2026-10-27 23:36:18 IST (2026-10-27 18:06:18 UTC)
**Aliases Scanned**: `SOLUSD.P, SOLUSD.PI, SOLUSD, SOL, SOLUSDT`
**Coverage**: 35 feeds with direct asset data | 4 global macro feeds | 42 total feeds scanned

---

## 1. Executive Pillar Coverage Ledger
| Strategic Pillar | Active Feeds | Coverage Status | Feeds Included |
|---|---|---|---|
| **Pillar 1: Broker Telemetry & Solvency** | 2/2 | `FULL / PASS` | 00_MT5_Account_Telemetry, 23_Master_Pipeline_Telemetry |
| **Pillar 5: Microstructure, Whales & Footprints** | 10/11 | `FULL / PASS` | 10_Whale_Orders, 17_Orderbook, 18_CVD_30D_15m, 18_CVD_30D_1h (+6 more) |
| **Pillar 6: Technical & Auction Profile** | 7/7 | `FULL / PASS` | 11_Technical, 11_Technical_BTC_Ribbon, 12_Hyperdash, 13_Hyperliquid (+3 more) |
| **Pillar 4: Liquidation & Stops Geometry** | 10/12 | `FULL / PASS` | 14_Hyperdash_Liq_Map, 14_Liquidation_Matrix, 15_Hyperdash_Stops_Map, 7_Liq_Heapmap (+6 more) |
| **Pillar 2: Macro & ETF Netflows** | 4/4 | `FULL / PASS` | 19_Calendar, 19_News, 1_Crypto_ETF_Flows, 2_Spot_Netflow_S |
| **Pillar 3: Sentiment & Leverage Crowding** | 6/6 | `FULL / PASS` | 3_Exchanges_LS_Ratio_15M, 3_Exchanges_LS_Ratio_1H, 3_Exchanges_LS_Ratio_4H, 5_Funding_Rate (+2 more) |

---

## 2. Granular Per-Feed Data Extraction Inventory
| Feed Name | Rows Found | Pillar | Status | Key Specific Insights Extracted |
|---|---|---|---|---|
| `00_MT5_Account_Telemetry` | 1 | Pillar 1 | `DATA_EXTRACTED [PASS]` | Live Account Equity: N/A | Free Margin: N/A |
| `10_Whale_Orders` | 204 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Whale order: Sell Orders 1002.31 at 100.87 |
| `11_Technical` | 1 | Pillar 6 | `DATA_EXTRACTED [PASS]` | VWAP Z: 1.731890787184893 | RSI: 60.601422832870576 | EMA 89/233 alignment |
| `11_Technical_BTC_Ribbon` | 100 | Pillar 6 | `MACRO_GLOBAL_CONTEXT` | VWAP Z: 2.2780050437745074 | RSI: 65.77405822941165 | EMA 89/233 alignment |
| `12_Hyperdash` | 1 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 1 rows. Latest keys: ['Section', 'Asset', 'Type_or_Side', 'Price'] |
| `13_Hyperliquid` | 2 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 2 rows. Latest keys: ['Section', 'Asset', 'Price', 'Change_24h'] |
| `14_Hyperdash_Liq_Map` | 202 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `14_Liquidation_Matrix` | 380 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: 202.5 |
| `15_Hyperdash_Stops_Map` | 157 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Extracted 157 rows. Latest keys: ['sr_no', 'asset', 'time_window', 'timestamp_ist'] |
| `16_Hyperdash_telegram_Intel` | 77 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 77 rows. Latest keys: ['category', 'event_type', 'asset', 'side'] |
| `17_Orderbook` | 391 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Orderbook depth: Bid/Ask ratio N/A | Spread: N/A |
| `18_CVD` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `18_CVD_30D_15m` | 96 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 258775.7479 | Cumulative delta trend |
| `18_CVD_30D_1h` | 24 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 17034988.1249 | Cumulative delta trend |
| `18_CVD_30D_4h` | 6 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 35835378.4666 | Cumulative delta trend |
| `18_CVD_30D_5m` | 288 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 258208.0155 | Cumulative delta trend |
| `18_CVD_30D_ALL` | 414 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 35835378.4666 | Cumulative delta trend |
| `19_Calendar` | 44 | Pillar 2 | `MACRO_GLOBAL_CONTEXT` | Extracted 44 rows. Latest keys: ['date', 'time', 'currency', 'impact'] |
| `19_News` | 35 | Pillar 2 | `MACRO_GLOBAL_CONTEXT` | Extracted 35 rows. Latest keys: ['title', 'url', 'source', 'time_ago'] |
| `1_Crypto_ETF_Flows` | 5 | Pillar 2 | `DATA_EXTRACTED [PASS]` | Extracted 5 rows. Latest keys: ['#', 'Ticker', 'ETF_Name', 'Price'] |
| `20_Auction_Market_Structure` | 1 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 1 rows. Latest keys: ['timestamp', 'sr_no', 'asset', 'symbol'] |
| `21_Tradfye_Orderflow` | 384 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Extracted 384 rows. Latest keys: ['timestamp_ist', 'timestamp_utc', 'asset', 'market_pair'] |
| `22_Forced_Liquidations_MTF` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `23_Master_Pipeline_Telemetry` | 33 | Pillar 1 | `MACRO_GLOBAL_CONTEXT` | Live Account Equity: N/A | Free Margin: N/A |
| `25_CoinGlass_Footprint_Signals` | 1 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Signal: — (—) at 0.0 | Live Footprint Stream |
| `26_Aggregated_Footprint_Bar_Metrics` | 10 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Signal: None (None) at None | None |
| `2_Spot_Netflow_S` | 1 | Pillar 2 | `DATA_EXTRACTED [PASS]` | Extracted 1 rows. Latest keys: ['Symbol', '5_minute', '15_minute', '30_minute'] |
| `3_Exchanges_LS_Ratio_15M` | 25 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Long/Short ratio: N/A (N/A% Longs) |
| `3_Exchanges_LS_Ratio_1H` | 25 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Long/Short ratio: N/A (N/A% Longs) |
| `3_Exchanges_LS_Ratio_4H` | 25 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Long/Short ratio: N/A (N/A% Longs) |
| `4_Hyperliquid_Analysis` | 70 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 70 rows. Latest keys: ['rank', 'user_display', 'wallet_address', 'asset'] |
| `5_Funding_Rate` | 4 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Funding rate: N/A |
| `5_OI` | 1 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Extracted 1 rows. Latest keys: ['Asset', 'Total_OI_USD', 'Binance', 'Bybit'] |
| `6_Funding_Fee_Settlement` | 5 | Pillar 3 | `DATA_EXTRACTED [PASS]` | Funding rate: N/A |
| `7_Liq_Heapmap` | 1 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `7_Live_Liq` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `8_Exchange_Liquidation_Map_1D` | 69 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `8_Exchange_Liquidation_Map_7D` | 111 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `9_Liquidation_Max_Pain_24H` | 4 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `9_Liquidation_Max_Pain_3D` | 4 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `9_Liquidation_Max_Pain_48H` | 4 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |
| `9_Liquidation_Max_Pain_7D` | 4 | Pillar 4 | `DATA_EXTRACTED [PASS]` | Liq band / pain price: N/A |