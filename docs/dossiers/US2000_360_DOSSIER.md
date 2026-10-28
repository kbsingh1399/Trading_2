# 360° Data Lake Dossier: US2000
**Generated**: 2026-10-28 11:01:18 IST (2026-10-28 05:31:18 UTC)
**Aliases Scanned**: `US2000, US2000USD.PI, US2000USD, US2000USDT, US2000USD.P`
**Coverage**: 7 feeds with direct asset data | 4 global macro feeds | 42 total feeds scanned

---

## 1. Executive Pillar Coverage Ledger
| Strategic Pillar | Active Feeds | Coverage Status | Feeds Included |
|---|---|---|---|
| **Pillar 1: Broker Telemetry & Solvency** | 1/2 | `FULL / PASS` | 23_Master_Pipeline_Telemetry |
| **Pillar 5: Microstructure, Whales & Footprints** | 5/11 | `FULL / PASS` | 18_CVD_30D_15m, 18_CVD_30D_1h, 18_CVD_30D_4h, 18_CVD_30D_5m (+1 more) |
| **Pillar 6: Technical & Auction Profile** | 3/7 | `FULL / PASS` | 11_Technical, 11_Technical_BTC_Ribbon, 20_Auction_Market_Structure |
| **Pillar 4: Liquidation & Stops Geometry** | 0/12 | `ABSENT` |  |
| **Pillar 2: Macro & ETF Netflows** | 2/4 | `FULL / PASS` | 19_Calendar, 19_News |
| **Pillar 3: Sentiment & Leverage Crowding** | 0/6 | `ABSENT` |  |

---

## 2. Granular Per-Feed Data Extraction Inventory
| Feed Name | Rows Found | Pillar | Status | Key Specific Insights Extracted |
|---|---|---|---|---|
| `00_MT5_Account_Telemetry` | 0 | Pillar 1 | `NO_DIRECT_MATCH` | No direct records for asset |
| `10_Whale_Orders` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `11_Technical` | 1 | Pillar 6 | `DATA_EXTRACTED [PASS]` | VWAP Z: -0.11517657331693101 | RSI: 47.28515362002847 | EMA 89/233 alignment |
| `11_Technical_BTC_Ribbon` | 100 | Pillar 6 | `MACRO_GLOBAL_CONTEXT` | VWAP Z: 0.5742418494837214 | RSI: 54.12584752084207 | EMA 89/233 alignment |
| `12_Hyperdash` | 0 | Pillar 6 | `NO_DIRECT_MATCH` | No direct records for asset |
| `13_Hyperliquid` | 0 | Pillar 6 | `NO_DIRECT_MATCH` | No direct records for asset |
| `14_Hyperdash_Liq_Map` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `14_Liquidation_Matrix` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `15_Hyperdash_Stops_Map` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `16_Hyperdash_telegram_Intel` | 0 | Pillar 6 | `NO_DIRECT_MATCH` | No direct records for asset |
| `17_Orderbook` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `18_CVD` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `18_CVD_30D_15m` | 92 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 2032138.4760135752 | Cumulative delta trend |
| `18_CVD_30D_1h` | 23 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 14445232.875839125 | Cumulative delta trend |
| `18_CVD_30D_4h` | 6 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 40961677.24186308 | Cumulative delta trend |
| `18_CVD_30D_5m` | 276 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 947165.6279264946 | Cumulative delta trend |
| `18_CVD_30D_ALL` | 397 | Pillar 5 | `DATA_EXTRACTED [PASS]` | Taker delta: 947165.6279264946 | Cumulative delta trend |
| `19_Calendar` | 44 | Pillar 2 | `MACRO_GLOBAL_CONTEXT` | Extracted 44 rows. Latest keys: ['date', 'time', 'currency', 'impact'] |
| `19_News` | 33 | Pillar 2 | `MACRO_GLOBAL_CONTEXT` | Extracted 33 rows. Latest keys: ['title', 'url', 'source', 'time_ago'] |
| `1_Crypto_ETF_Flows` | 0 | Pillar 2 | `NO_DIRECT_MATCH` | No direct records for asset |
| `20_Auction_Market_Structure` | 1 | Pillar 6 | `DATA_EXTRACTED [PASS]` | Extracted 1 rows. Latest keys: ['timestamp', 'sr_no', 'asset', 'symbol'] |
| `21_Tradfye_Orderflow` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `22_Forced_Liquidations_MTF` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `23_Master_Pipeline_Telemetry` | 33 | Pillar 1 | `MACRO_GLOBAL_CONTEXT` | Live Account Equity: N/A | Free Margin: N/A |
| `25_CoinGlass_Footprint_Signals` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `26_Aggregated_Footprint_Bar_Metrics` | 0 | Pillar 5 | `NO_DIRECT_MATCH` | No direct records for asset |
| `2_Spot_Netflow_S` | 0 | Pillar 2 | `NO_DIRECT_MATCH` | No direct records for asset |
| `3_Exchanges_LS_Ratio_15M` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `3_Exchanges_LS_Ratio_1H` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `3_Exchanges_LS_Ratio_4H` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `4_Hyperliquid_Analysis` | 0 | Pillar 6 | `NO_DIRECT_MATCH` | No direct records for asset |
| `5_Funding_Rate` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `5_OI` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `6_Funding_Fee_Settlement` | 0 | Pillar 3 | `NO_DIRECT_MATCH` | No direct records for asset |
| `7_Liq_Heapmap` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `7_Live_Liq` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `8_Exchange_Liquidation_Map_1D` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `8_Exchange_Liquidation_Map_7D` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `9_Liquidation_Max_Pain_24H` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `9_Liquidation_Max_Pain_3D` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `9_Liquidation_Max_Pain_48H` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |
| `9_Liquidation_Max_Pain_7D` | 0 | Pillar 4 | `NO_DIRECT_MATCH` | No direct records for asset |