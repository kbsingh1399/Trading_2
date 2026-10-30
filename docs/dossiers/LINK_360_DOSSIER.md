# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 14:38:47 IST` (`2026-10-30 09:08:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.94` | **Live Ask Quote**: `11.03` | **Mid Price**: `10.99`
- **Spread Points**: `85.00` | **Spread BPS**: `77.37 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `10.74` | VWAP Z-Score: `+0.77` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0878` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.55` | Lower -3.00σ Band: `9.93`
  * Upper +2.51σ Band: `11.42` | Lower -2.51σ Band: `10.06`
  * Upper +2.01σ Band: `11.28` | Lower -2.01σ Band: `10.20`
  * Upper +2.00σ Band: `11.28` | Lower -2.00σ Band: `10.20`
  * Upper +1.28σ Band: `11.09` | Lower -1.28σ Band: `10.39`
  * Upper +1.00σ Band: `11.01` | Lower -1.00σ Band: `10.47`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.98` | EMA-20=`10.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.98` (Slope: `+0.0000`) | EMA-100=`11.12`
  * Institutional Anchors: EMA-144=`11.20` | EMA-200=`11.27` (Slope: `-0.2923`) | EMA-233=`11.29`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-1.10%`)
  * Point of Control (POC) = `11.04` (Distance: `-0.42%`)
  * Value Area Low (VAL) = `10.54` (Distance: `+4.36%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.77` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.93`
  * New York Session (13:00-21:00 UTC): High=`11.05` | Low=`10.92`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.94` - `11.03`
  * Optimal Trade Entry (OTE 0.705): `11.01`
  * Structural Invalidation Anchor (0.786): `11.07`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.01` | `11.05` | `11.00` | `11.05` | `34,158` | 376,540.64 USD | 40,781.58 USD | `+10.83%` | -11,927,983.60 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.05` | `11.05` | `11.00` | `11.01` | `24,676` | 271,875.75 USD | -43,099.55 USD | `-15.85%` | -11,971,083.15 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.01` | `11.02` | `11.00` | `11.01` | `12,280` | 135,164.50 USD | -29,546.51 USD | `-21.86%` | -12,000,629.66 USD | `+0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.05` | `11.07` | `11.00` | `11.00` | `133,941` | 1,477,587.17 USD | 1,384.99 USD | `+0.09%` | -12,166,940.36 USD | `-0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.00` | `11.05` | `10.99` | `11.01` | `102,496` | 1,128,540.66 USD | -101,977.17 USD | `-9.04%` | -12,268,917.53 USD | `-0.54` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.01` | `11.02` | `11.00` | `11.00` | `12,168` | 133,935.91 USD | -30,372.28 USD | `-22.68%` | -12,299,289.80 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `11.13` | `11.15` | `11.00` | `11.04` | `706,212` | 7,823,977.42 USD | -443,394.34 USD | `-5.67%` | -11,819,138.86 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.04` | `11.11` | `10.99` | `11.01` | `546,831` | 6,037,228.26 USD | -347,696.97 USD | `-5.76%` | -12,166,835.83 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.01` | `11.02` | `11.00` | `11.00` | `12,168` | 133,935.91 USD | -30,372.28 USD | `-22.68%` | -12,197,208.11 USD | `+0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.99` | `11.01` | `559,110` | 6,172,392.76 USD | -377,243.48 USD | `-6.11%` | -12,252,348.76 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.99` | `11.01` | `559,110` | 6,172,392.76 USD | -377,243.48 USD | `-6.11%` | -12,252,348.76 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |

- **Deribit Institutional Options Max Pain & Volatility Surface (21_Tradfye_Orderflow.parquet)**:
  * Options Max Pain Price: `0.000000`
  * Call Wall Strike: `0.000000` | Put Wall Strike: `0.000000`

---

## 5. Institutional Whale Armor, Hyperdash Intel & L2 Depth Ladders
*(Sources: 10_Whale_Orders.parquet, 17_Orderbook.parquet, 12_Hyperdash.parquet, 13_Hyperliquid.parquet, 4_Hyperliquid_Analysis.parquet, 16_Hyperdash_telegram_Intel.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Top Defending Bid Wall: `None` (Unarmored)
  * Top Defending Ask Wall: `None` (Unarmored)
| Side | Wall Price (USD) | Size (Coins) | Depth (USD) | Distance (%) | Persistence | Traded % | Venue | Order ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| --- | **`10.99`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `424` | `0xecb6...2b00` | `SHORT` | 5,220,301.17 USD | `473,969,600.00` | `10.66` | `11.01` | `76.96` | -168,423.99 USD | `-3.23%` | `10X Cross` |
| `509` | `0x73ce...8ce9` | `LONG` | 4,406,927.80 USD | `400,011,600.00` | `12.05` | `11.01` | `7.82` | -412,825.91 USD | `-9.37%` | `5X Cross` |
| `858` | `0xb83d...6e36` | `SHORT` | 2,665,531.18 USD | `242,013,000.00` | `12.93` | `11.01` | `522.02` | 464,363.01 USD | `+17.42%` | `3X Cross` |
| `900` | `0x458d...ab3b` | `LONG` | 2,500,540.95 USD | `227,156,700.00` | `13.13` | `11.01` | `9.34` | -481,689.44 USD | `-19.26%` | `3X Isolated` |
| `985` | `0xdd53...2b13` | `SHORT` | 2,276,183.71 USD | `206,475,300.00` | `11.92` | `11.01` | `297.42` | 185,039.22 USD | `+8.13%` | `3X Cross` |
| `1016` | `0x3dc9...54b0` | `SHORT` | 2,202,800.00 USD | `200,000,000.00` | `7.56` | `11.01` | `94.47` | -691,641.58 USD | `-31.40%` | `10X Cross` |
| `1031` | `0x45d2...4029` | `SHORT` | 2,154,996.50 USD | `195,500,000.00` | `11.54` | `11.01` | `219.52` | 101,486.93 USD | `+4.71%` | `10X Cross` |
| `1199` | `0x6540...f7b7` | `LONG` | 1,845,836.51 USD | `167,438,000.00` | `12.40` | `11.01` | `6.70` | -230,388.72 USD | `-12.48%` | `5X Isolated` |
| `1277` | `0xeadc...9d55` | `LONG` | 1,736,815.28 USD | `157,691,600.00` | `9.43` | `11.01` | `0.000000` | 250,160.38 USD | `+14.40%` | `10X Cross` |
| `1493` | `0x5b5d...c060` | `SHORT` | 1,451,375.36 USD | `131,775,500.00` | `13.61` | `11.01` | `1156.34` | 341,882.61 USD | `+23.56%` | `3X Cross` |
| `1674` | `0xf6f3...47f8` | `SHORT` | 1,268,091.00 USD | `115,024,600.00` | `11.42` | `11.01` | `18.33` | 45,239.18 USD | `+3.57%` | `5X Cross` |
| `1849` | `0xfe7e...11b4` | `LONG` | 1,115,090.55 USD | `101,142,000.00` | `14.47` | `11.01` | `5.33` | -348,022.60 USD | `-31.21%` | `5X Isolated` |
| `1886` | `0x8af7...fa05` | `SHORT` | 1,087,645.02 USD | `98,661,200.00` | `14.08` | `11.01` | `203.30` | 301,537.52 USD | `+27.72%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.46` | 6,666.32 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.4640 USD [API] | `2026-10-29 09:31:24` |
| `ANNOUNCEMENT` | `INFO` | `11.48` | 5,889.12 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.89K USD at 11.4820 USD [API] | `2026-10-29 09:50:11` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 8,316.00 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 8.32K USD at 11.5500 USD [API] | `2026-10-29 10:34:53` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 169.54 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.17K USD at 11.5330 USD [API] | `2026-10-24 09:35:07` |
| `ANNOUNCEMENT` | `INFO` | `11.59` | 7,508.89 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.51K USD at 11.5860 USD [API] | `2026-10-29 11:05:03` |
| `ANNOUNCEMENT` | `INFO` | `11.63` | 5,465.85 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.6270 USD [API] | `2026-10-29 11:53:04` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.6000 USD [API] | `2026-10-29 12:19:39` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,643.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.64K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.72 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.68` | 6,290.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.29K USD at 11.6780 USD [API] | `2026-10-29 13:02:36` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,599.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:46` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,597.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:45` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.27` | 23.67 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.02K USD at 11.2730 USD [API] | `2026-09-13 09:25:11` |
| `ANNOUNCEMENT` | `INFO` | `11.63` | 227.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.23K USD at 11.6300 USD [API] | `2026-09-09 22:09:04` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 63.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 12.02 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.01K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `11.83` | 5,469.27 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8280 USD [API] | `2026-10-29 17:21:54` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+2.09%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.28%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+2.08%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.29%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+2.08%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.29%`)
  * 7D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.99%`) | Long MP=`10.30` (Vol: 866,700.00 USD, Dist: `--6.33%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 168.08 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 1,170.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 3,590.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 154.78 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,830.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 1,300.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,060.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 14,090.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 616.50 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 14,270.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 393.01 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 11,200.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 47,860.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 7,040.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 2,440.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 239,570.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 425.83 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 85,490.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,840.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 3,940.00 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 26,320.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,770.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 2,940.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 2,230.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 9,920.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 13,590.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 29,010.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 83,010.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,700.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,870.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,160,000.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 20,240.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 44,610.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 696,600.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 44,910.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 17,730.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 9,730.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 37,190.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 173,010.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 2,020.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 17,510.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,190,000.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,610.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 66,130.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 50,510.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 196,200.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 351,270.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,960.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 19,940.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 27,170.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 75,200.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 453,270.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 86,680.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.15` | 13,070,000.00 USD | 13,070,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,970.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.17` | 13,000,000.00 USD | 13,000,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.19` | 12,950,000.00 USD | 12,950,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.21` | 12,890,000.00 USD | 12,890,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.23` | 12,880,000.00 USD | 12,880,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.25` | 12,850,000.00 USD | 12,850,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,830.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.27` | 12,810,000.00 USD | 12,810,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.29` | 12,790,000.00 USD | 12,790,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.31` | 12,750,000.00 USD | 12,750,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.33` | 12,690,000.00 USD | 12,690,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.35` | 12,690,000.00 USD | 12,690,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.37` | 12,640,000.00 USD | 12,640,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.39` | 12,630,000.00 USD | 12,630,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.41` | 12,580,000.00 USD | 12,580,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.43` | 12,570,000.00 USD | 12,570,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.45` | 12,520,000.00 USD | 12,520,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 46,490.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.47` | 12,370,000.00 USD | 12,370,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.49` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.51` | 12,370,000.00 USD | 12,370,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 12,300,000.00 USD | 12,300,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 102,190.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.57` | 12,260,000.00 USD | 12,260,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 12,170,000.00 USD | 12,170,000.00 USD | 62,800.00 USD | 1,250.00 USD | 105,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 11,960,000.00 USD | 11,960,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 11,950,000.00 USD | 11,950,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 202,750.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.69` | 11,940,000.00 USD | 11,940,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 11,870,000.00 USD | 11,870,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 63,190.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 11,790,000.00 USD | 11,790,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 11,740,000.00 USD | 11,740,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 11,640,000.00 USD | 11,640,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 11,580,000.00 USD | 11,580,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 30,620.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.87` | 11,520,000.00 USD | 11,520,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.89` | 8,250,000.00 USD | 8,250,000.00 USD | 13,350.00 USD | 9,160.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 11,510,000.00 USD | 11,510,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 8,210,000.00 USD | 8,210,000.00 USD | 30,130.00 USD | 36,120.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 8,150,000.00 USD | 8,150,000.00 USD | 13,840.00 USD | 14,790.00 USD | 219.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 8,120,000.00 USD | 8,120,000.00 USD | 14,390.00 USD | 7,200.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 11,380,000.00 USD | 11,380,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 421,600.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 8,090,000.00 USD | 8,090,000.00 USD | 77,130.00 USD | 7,890.00 USD | 60,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 11,330,000.00 USD | 11,330,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 7,940,000.00 USD | 7,940,000.00 USD | 8,980.00 USD | 7,950.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 11,320,000.00 USD | 11,320,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 7,850,000.00 USD | 7,850,000.00 USD | 14,600.00 USD | 6,210.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 7,810,000.00 USD | 7,810,000.00 USD | 6,170.00 USD | 15,550.00 USD | 264.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.03` | 11,240,000.00 USD | 11,240,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 7,780,000.00 USD | 7,780,000.00 USD | 38,520.00 USD | 555.00 USD | 18,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 781,760.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.07` | 7,730,000.00 USD | 7,730,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 7,560,000.00 USD | 7,560,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 11,030,000.00 USD | 11,030,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 7,440,000.00 USD | 7,440,000.00 USD | 7,530.00 USD | 41,480.00 USD | 123.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 10,810,000.00 USD | 10,810,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 7,390,000.00 USD | 7,390,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 10,740,000.00 USD | 10,740,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 7,320,000.00 USD | 7,320,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 10,630,000.00 USD | 10,630,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 66,890.00 USD | 261,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.17` | 7,250,000.00 USD | 7,250,000.00 USD | 127,800.00 USD | 25,060.00 USD | 640.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 10,380,000.00 USD | 10,380,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 7,100,000.00 USD | 7,100,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 10,280,000.00 USD | 10,280,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 6,780,000.00 USD | 6,780,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 10,020,000.00 USD | 10,020,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 6,330,000.00 USD | 6,330,000.00 USD | 100,980.00 USD | 58,340.00 USD | 282,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 9,670,000.00 USD | 9,670,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 5,890,000.00 USD | 5,890,000.00 USD | 9,720.00 USD | 25,460.00 USD | 34,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 8,940,000.00 USD | 8,940,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 32,460.00 USD | 194,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.27` | 5,820,000.00 USD | 5,820,000.00 USD | 64,690.00 USD | 18,820.00 USD | 130,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 8,680,000.00 USD | 8,680,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 5,610,000.00 USD | 5,610,000.00 USD | 328,720.00 USD | 1,910.00 USD | 151,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 8,260,000.00 USD | 8,260,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 5,130,000.00 USD | 5,130,000.00 USD | 11,920.00 USD | 19,120.00 USD | 48,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 7,560,000.00 USD | 7,560,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 5,050,000.00 USD | 5,050,000.00 USD | 14,820.00 USD | 3,820.00 USD | 50,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 7,520,000.00 USD | 7,520,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 4,980,000.00 USD | 4,980,000.00 USD | 61,320.00 USD | 6,620.00 USD | 72,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 7,360,000.00 USD | 7,360,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,720.00 USD | 162,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.37` | 4,840,000.00 USD | 4,840,000.00 USD | 12,790.00 USD | 13,750.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 6,950,000.00 USD | 6,950,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 4,800,000.00 USD | 4,800,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 6,950,000.00 USD | 6,950,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 4,640,000.00 USD | 4,640,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 6,940,000.00 USD | 6,940,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 4,460,000.00 USD | 4,460,000.00 USD | 311,620.00 USD | 0.00 USD | 88,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 6,490,000.00 USD | 6,490,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 4,060,000.00 USD | 4,060,000.00 USD | 329,820.00 USD | 44,950.00 USD | 216,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 6,250,000.00 USD | 6,250,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 5,590.00 USD | 21,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.47` | 3,470,000.00 USD | 3,470,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 5,370,000.00 USD | 5,370,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 3,370,000.00 USD | 3,370,000.00 USD | 41,670.00 USD | 38,130.00 USD | 25,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 4,980,000.00 USD | 4,980,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 3,270,000.00 USD | 3,270,000.00 USD | 11,220.00 USD | 10,370.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 4,840,000.00 USD | 4,840,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 3,230,000.00 USD | 3,230,000.00 USD | 1,160.00 USD | 18,090.00 USD | 117,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 4,780,000.00 USD | 4,780,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 3,090,000.00 USD | 3,090,000.00 USD | 65,860.00 USD | 48,520.00 USD | 52,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 4,740,000.00 USD | 4,740,000.00 USD | 121,680.00 USD | 114,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 15,850.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.57` | 2,930,000.00 USD | 2,930,000.00 USD | 40,970.00 USD | 30,280.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 2,840,000.00 USD | 2,840,000.00 USD | 18,130.00 USD | 27,220.00 USD | 15,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 2,780,000.00 USD | 2,780,000.00 USD | 9,410.00 USD | 9,370.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 4,510,000.00 USD | 4,510,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 2,750,000.00 USD | 2,750,000.00 USD | 42,360.00 USD | 2,580.00 USD | 128,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 4,500,000.00 USD | 4,500,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 2,570,000.00 USD | 2,570,000.00 USD | 77,540.00 USD | 6,020.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 4,440,000.00 USD | 4,440,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.67` | 2,440,000.00 USD | 2,440,000.00 USD | 67,580.00 USD | 15,280.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 2,330,000.00 USD | 2,330,000.00 USD | 36,050.00 USD | 30,270.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 4,400,000.00 USD | 4,400,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 2,080,000.00 USD | 2,080,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 2,000,000.00 USD | 2,000,000.00 USD | 89,590.00 USD | 8,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 3,880,000.00 USD | 3,880,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.77` | 1,900,000.00 USD | 1,900,000.00 USD | 22,390.00 USD | 62,430.00 USD | 51,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 3,750,000.00 USD | 3,750,000.00 USD | 537,300.00 USD | 111,300.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 1,760,000.00 USD | 1,760,000.00 USD | 167,780.00 USD | 134,790.00 USD | 26,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 2,990,000.00 USD | 2,990,000.00 USD | 32,480.00 USD | 64,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 1,430,000.00 USD | 1,430,000.00 USD | 13,650.00 USD | 23,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.83` | 1,400,000.00 USD | 1,400,000.00 USD | 334,330.00 USD | 15,810.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.85` | 1,040,000.00 USD | 1,040,000.00 USD | 148,850.00 USD | 17,390.00 USD | 199,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 2,350,000.00 USD | 2,350,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.87` | 674,250.00 USD | 674,250.00 USD | 155,080.00 USD | 10,430.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 2,050,000.00 USD | 2,050,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.89` | 463,570.00 USD | 463,570.00 USD | 76,840.00 USD | 14,710.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 1,180,000.00 USD | 1,180,000.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.91` | 308,410.00 USD | 308,410.00 USD | 164,650.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 770,060.00 USD | 770,060.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.93` | 110,220.00 USD | 110,220.00 USD | 3,920.00 USD | 15,020.00 USD | 86.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 511,590.00 USD | 511,590.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.95` | 91,190.00 USD | 91,190.00 USD | 1,550.00 USD | 1,320.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 294,960.00 USD | 294,960.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 966.88 USD | 966.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.97` | 237,220.00 USD | 237,220.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.99` | 570.72 USD | 570.72 USD | 0.00 USD | 467.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 224,900.00 USD | 224,900.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.01` | 103.72 USD | 103.72 USD | 0.00 USD | 0.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 11,680.00 USD | 11,680.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.03` | 305,660.00 USD | 305,660.00 USD | 0.00 USD | 718.45 USD | 304,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 279,660.00 USD | 279,660.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.05` | 307,240.00 USD | 307,240.00 USD | 0.00 USD | 1,480.00 USD | 99.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 556,870.00 USD | 556,870.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.07` | 334,220.00 USD | 334,220.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 559,180.00 USD | 559,180.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 640,870.00 USD | 640,870.00 USD | 4,520.00 USD | 0.00 USD | 302,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 815,200.00 USD | 815,200.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 652,680.00 USD | 652,680.00 USD | 9,550.00 USD | 2,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,320,000.00 USD | 1,320,000.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 857,100.00 USD | 857,100.00 USD | 0.00 USD | 0.00 USD | 204,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,810,000.00 USD | 1,810,000.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 1,020,000.00 USD | 1,020,000.00 USD | 109,480.00 USD | 506.95 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,100,000.00 USD | 2,100,000.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 1,100,000.00 USD | 1,100,000.00 USD | 22,450.00 USD | 2,450.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,190,000.00 USD | 2,190,000.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 1,240,000.00 USD | 1,240,000.00 USD | 72,050.00 USD | 22,010.00 USD | 40,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 1,530,000.00 USD | 1,530,000.00 USD | 122,450.00 USD | 59,670.00 USD | 113,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,930,000.00 USD | 2,930,000.00 USD | 554,520.00 USD | 106,700.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 1,960,000.00 USD | 1,960,000.00 USD | 250,870.00 USD | 54,330.00 USD | 120,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 3,310,000.00 USD | 3,310,000.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 2,260,000.00 USD | 2,260,000.00 USD | 108,110.00 USD | 57,600.00 USD | 138,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,780,000.00 USD | 3,780,000.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.27` | 2,790,000.00 USD | 2,790,000.00 USD | 329,340.00 USD | 15,580.00 USD | 178,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,430,000.00 USD | 4,430,000.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 3,420,000.00 USD | 3,420,000.00 USD | 237,630.00 USD | 122,270.00 USD | 276,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,750,000.00 USD | 4,750,000.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 3,820,000.00 USD | 3,820,000.00 USD | 218,320.00 USD | 72,220.00 USD | 111,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 5,060,000.00 USD | 5,060,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 4,180,000.00 USD | 4,180,000.00 USD | 219,020.00 USD | 45,400.00 USD | 95,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 5,450,000.00 USD | 5,450,000.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 4,750,000.00 USD | 4,750,000.00 USD | 343,170.00 USD | 135,950.00 USD | 84,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,740,000.00 USD | 5,740,000.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.37` | 5,050,000.00 USD | 5,050,000.00 USD | 152,070.00 USD | 105,530.00 USD | 47,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 6,080,000.00 USD | 6,080,000.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 5,120,000.00 USD | 5,120,000.00 USD | 14,820.00 USD | 47,470.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 5,400,000.00 USD | 5,400,000.00 USD | 96,590.00 USD | 35,740.00 USD | 140,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 5,650,000.00 USD | 5,650,000.00 USD | 64,580.00 USD | 56,680.00 USD | 132,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 6,670,000.00 USD | 6,670,000.00 USD | 265,450.00 USD | 105,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 5,850,000.00 USD | 5,850,000.00 USD | 77,400.00 USD | 91,580.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 6,980,000.00 USD | 6,980,000.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 1,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.47` | 5,960,000.00 USD | 5,960,000.00 USD | 56,320.00 USD | 28,930.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 7,070,000.00 USD | 7,070,000.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 6,070,000.00 USD | 6,070,000.00 USD | 42,800.00 USD | 33,150.00 USD | 37,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 7,210,000.00 USD | 7,210,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 6,230,000.00 USD | 6,230,000.00 USD | 71,900.00 USD | 30,900.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 7,330,000.00 USD | 7,330,000.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 6,430,000.00 USD | 6,430,000.00 USD | 111,420.00 USD | 18,960.00 USD | 63,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 7,450,000.00 USD | 7,450,000.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 6,620,000.00 USD | 6,620,000.00 USD | 112,550.00 USD | 7,230.00 USD | 70,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 7,640,000.00 USD | 7,640,000.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 2,600.00 USD | 3,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.57` | 6,760,000.00 USD | 6,760,000.00 USD | 102,740.00 USD | 17,450.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 6,850,000.00 USD | 6,850,000.00 USD | 28,580.00 USD | 17,270.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 7,020,000.00 USD | 7,020,000.00 USD | 86,530.00 USD | 512.95 USD | 85,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 7,750,000.00 USD | 7,750,000.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 7,060,000.00 USD | 7,060,000.00 USD | 3,670.00 USD | 6,700.00 USD | 31,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 7,860,000.00 USD | 7,860,000.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 7,070,000.00 USD | 7,070,000.00 USD | 2,630.00 USD | 7,840.00 USD | 63.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 6,130.00 USD | 9,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.67` | 7,160,000.00 USD | 7,160,000.00 USD | 19,420.00 USD | 11,530.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 7,300,000.00 USD | 7,300,000.00 USD | 106,690.00 USD | 34,170.00 USD | 352.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 8,090,000.00 USD | 8,090,000.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 7,400,000.00 USD | 7,400,000.00 USD | 65,810.00 USD | 13,000.00 USD | 15,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 8,290,000.00 USD | 8,290,000.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 7,670,000.00 USD | 7,670,000.00 USD | 139,850.00 USD | 11,770.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 8,470,000.00 USD | 8,470,000.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 7,790,000.00 USD | 7,790,000.00 USD | 21,990.00 USD | 38,420.00 USD | 61,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 8,530,000.00 USD | 8,530,000.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 7,870,000.00 USD | 7,870,000.00 USD | 41,580.00 USD | 20,480.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 8,680,000.00 USD | 8,680,000.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 7,920,000.00 USD | 7,920,000.00 USD | 12,300.00 USD | 339.50 USD | 40,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 8,750,000.00 USD | 8,750,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 7,950,000.00 USD | 7,950,000.00 USD | 281.26 USD | 17,880.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 8,920,000.00 USD | 8,920,000.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 8,010,000.00 USD | 8,010,000.00 USD | 11,600.00 USD | 11,560.00 USD | 29,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 9,040,000.00 USD | 9,040,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 8,140,000.00 USD | 8,140,000.00 USD | 54,810.00 USD | 8,620.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 9,290,000.00 USD | 9,290,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 8,240,000.00 USD | 8,240,000.00 USD | 20,840.00 USD | 20,660.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 9,320,000.00 USD | 9,320,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 8,340,000.00 USD | 8,340,000.00 USD | 43,100.00 USD | 13,000.00 USD | 43,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 9,410,000.00 USD | 9,410,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 8,490,000.00 USD | 8,490,000.00 USD | 102,960.00 USD | 18,190.00 USD | 31,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 9,570,000.00 USD | 9,570,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 8,680,000.00 USD | 8,680,000.00 USD | 135,130.00 USD | 28,180.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 9,640,000.00 USD | 9,640,000.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 8,830,000.00 USD | 8,830,000.00 USD | 84,630.00 USD | 20,620.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 9,880,000.00 USD | 9,880,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 685.93 USD | 10,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.97` | 9,020,000.00 USD | 9,020,000.00 USD | 71,610.00 USD | 36,230.00 USD | 87,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 10,520,000.00 USD | 10,520,000.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 9,200,000.00 USD | 9,200,000.00 USD | 107,470.00 USD | 27,660.00 USD | 36,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 10,990,000.00 USD | 10,990,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 9,300,000.00 USD | 9,300,000.00 USD | 47,340.00 USD | 9,290.00 USD | 50,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 11,450,000.00 USD | 11,450,000.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 9,410,000.00 USD | 9,410,000.00 USD | 46,830.00 USD | 34,660.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 12,160,000.00 USD | 12,160,000.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 9,620,000.00 USD | 9,620,000.00 USD | 108,910.00 USD | 43,590.00 USD | 59,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 12,810,000.00 USD | 12,810,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 9,760,000.00 USD | 9,760,000.00 USD | 34,850.00 USD | 33,440.00 USD | 67,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 13,380,000.00 USD | 13,380,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 9,830,000.00 USD | 9,830,000.00 USD | 21,290.00 USD | 24,790.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 13,740,000.00 USD | 13,740,000.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 10,030,000.00 USD | 10,030,000.00 USD | 101,880.00 USD | 41,480.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 14,020,000.00 USD | 14,020,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 10,200,000.00 USD | 10,200,000.00 USD | 93,220.00 USD | 36,620.00 USD | 39,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 14,290,000.00 USD | 14,290,000.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 10,420,000.00 USD | 10,420,000.00 USD | 113,490.00 USD | 42,340.00 USD | 65,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 14,810,000.00 USD | 14,810,000.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 10,670,000.00 USD | 10,670,000.00 USD | 123,050.00 USD | 60,070.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 14,960,000.00 USD | 14,960,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 10,790,000.00 USD | 10,790,000.00 USD | 67,790.00 USD | 24,020.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 15,280,000.00 USD | 15,280,000.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 10,910,000.00 USD | 10,910,000.00 USD | 37,080.00 USD | 30,260.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 15,650,000.00 USD | 15,650,000.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 10,960,000.00 USD | 10,960,000.00 USD | 15,850.00 USD | 23,710.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 15,870,000.00 USD | 15,870,000.00 USD | 140,270.00 USD | 27,350.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 10,970,000.00 USD | 10,970,000.00 USD | 2,260.00 USD | 6,420.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 16,070,000.00 USD | 16,070,000.00 USD | 101,460.00 USD | 47,320.00 USD | 46,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,690.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.27` | 11,040,000.00 USD | 11,040,000.00 USD | 38,860.00 USD | 8,240.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 16,240,000.00 USD | 16,240,000.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 11,080,000.00 USD | 11,080,000.00 USD | 23,030.00 USD | 9,300.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 16,550,000.00 USD | 16,550,000.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 11,090,000.00 USD | 11,090,000.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 16,680,000.00 USD | 16,680,000.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,730,000.00 USD | 16,730,000.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,780,000.00 USD | 16,780,000.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 13,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,850,000.00 USD | 16,850,000.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 17,010,000.00 USD | 17,010,000.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 17,030,000.00 USD | 17,030,000.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 15,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,070.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 779.24 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.75` | 531.68 USD | 17,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 22,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 115,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 116,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 7,740.00 USD | 123,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 868.18 USD | 124,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 150,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 150,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 150,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 151,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 151,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 325.00 USD | 151,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 152,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 17,400.00 USD | 170,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,430.00 USD | 184,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 286,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 366,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 367,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,800.00 USD | 394,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,450.00 USD | 400,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 649,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 470.29 USD | 650,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 652,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 27,640.00 USD | 679,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 62,390.00 USD | 742,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 745,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 746,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 746,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 73,030.00 USD | 819,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 2,450.00 USD | 821,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 756.29 USD | 822,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.15` | 722,150.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 2,230,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.65` | 220.83 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,270,000.00 USD | 0.00 USD | 46,320.00 USD | `-79.55%` | `20,585,500.00` |
| `Live` | `Long` | `2.35` | 12,220,000.00 USD | 0.00 USD | 222.31 USD | `-78.64%` | `94,600.00` |
| `Live` | `Long` | `2.55` | 12,220,000.00 USD | 0.00 USD | 29,610.00 USD | `-76.82%` | `11,610,100.00` |
| `Live` | `Long` | `2.65` | 12,190,000.00 USD | 0.00 USD | 3,480.00 USD | `-75.91%` | `1,314,000.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 7,300.00 USD | `-72.27%` | `2,394,200.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 1,430.00 USD | `-71.36%` | `454,900.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 2,420.00 USD | `-69.55%` | `723,600.00` |
| `Live` | `Long` | `3.45` | 12,180,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.64%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 126.73 USD | `-67.73%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.82%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,170,000.00 USD | 0.00 USD | 250.25 USD | `-65.00%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,170,000.00 USD | 0.00 USD | 4,810.00 USD | `-64.09%` | `1,217,900.00` |
| `Live` | `Long` | `4.05` | 12,160,000.00 USD | 0.00 USD | 15,960.00 USD | `-63.18%` | `3,941,700.00` |
| `Live` | `Long` | `4.25` | 12,150,000.00 USD | 0.00 USD | 24,410.00 USD | `-61.36%` | `5,744,100.00` |
| `Live` | `Long` | `4.35` | 12,120,000.00 USD | 0.00 USD | 411.94 USD | `-60.45%` | `94,700.00` |
| `Live` | `Long` | `4.45` | 12,120,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.55%` | `235,700.00` |
| `Live` | `Long` | `4.55` | 12,120,000.00 USD | 0.00 USD | 57,150.00 USD | `-58.64%` | `12,560,000.00` |
| `Live` | `Long` | `4.65` | 12,060,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.73%` | `515,900.00` |
| `Live` | `Long` | `4.75` | 12,060,000.00 USD | 0.00 USD | 235,200.00 USD | `-56.82%` | `49,515,000.00` |
| `Live` | `Long` | `4.85` | 11,820,000.00 USD | 0.00 USD | 83,570.00 USD | `-55.91%` | `17,230,400.00` |
| `Live` | `Long` | `4.95` | 11,740,000.00 USD | 0.00 USD | 5,440.00 USD | `-55.00%` | `1,098,200.00` |
| `Live` | `Long` | `5.05` | 11,740,000.00 USD | 0.00 USD | 217.66 USD | `-54.09%` | `43,100.00` |
| `Live` | `Long` | `5.25` | 11,740,000.00 USD | 0.00 USD | 6,620.00 USD | `-52.27%` | `1,261,800.00` |
| `Live` | `Long` | `5.35` | 11,730,000.00 USD | 0.00 USD | 543,120.00 USD | `-51.36%` | `101,517,700.00` |
| `Live` | `Long` | `5.45` | 11,190,000.00 USD | 0.00 USD | 1,780.00 USD | `-50.45%` | `327,300.00` |
| `Live` | `Long` | `5.55` | 11,180,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.55%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 52,720.00 USD | `-48.64%` | `9,330,200.00` |
| `Live` | `Long` | `5.75` | 11,120,000.00 USD | 0.00 USD | 276.57 USD | `-47.73%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 11,120,000.00 USD | 0.00 USD | 6,010.00 USD | `-46.82%` | `1,026,700.00` |
| `Live` | `Long` | `5.95` | 11,120,000.00 USD | 0.00 USD | 10,260.00 USD | `-45.91%` | `1,724,100.00` |
| `Live` | `Long` | `6.05` | 11,110,000.00 USD | 0.00 USD | 13,590.00 USD | `-45.00%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 11,090,000.00 USD | 0.00 USD | 489.54 USD | `-44.09%` | `79,600.00` |
| `Live` | `Long` | `6.25` | 11,090,000.00 USD | 0.00 USD | 69,580.00 USD | `-43.18%` | `11,133,300.00` |
| `Live` | `Long` | `6.35` | 11,020,000.00 USD | 0.00 USD | 15,990.00 USD | `-42.27%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 11,010,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.36%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 11,000,000.00 USD | 0.00 USD | 3,270.00 USD | `-40.45%` | `499,500.00` |
| `Live` | `Long` | `6.65` | 10,990,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.55%` | `169,517,500.00` |
| `Live` | `Long` | `6.75` | 9,870,000.00 USD | 0.00 USD | 20,540.00 USD | `-38.64%` | `3,042,300.00` |
| `Live` | `Long` | `6.85` | 9,850,000.00 USD | 0.00 USD | 5,060.00 USD | `-37.73%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,840,000.00 USD | 0.00 USD | 79,550.00 USD | `-36.82%` | `11,445,400.00` |
| `Live` | `Long` | `7.05` | 9,760,000.00 USD | 0.00 USD | 710,860.00 USD | `-35.91%` | `100,830,900.00` |
| `Live` | `Long` | `7.15` | 9,050,000.00 USD | 0.00 USD | 10,740.00 USD | `-35.00%` | `1,501,900.00` |
| `Live` | `Long` | `7.25` | 9,040,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.09%` | `986,900.00` |
| `Live` | `Long` | `7.35` | 9,030,000.00 USD | 0.00 USD | 55,430.00 USD | `-33.18%` | `7,541,100.00` |
| `Live` | `Long` | `7.45` | 8,980,000.00 USD | 0.00 USD | 5,120.00 USD | `-32.27%` | `686,600.00` |
| `Live` | `Long` | `7.55` | 8,970,000.00 USD | 0.00 USD | 173,010.00 USD | `-31.36%` | `22,914,800.00` |
| `Live` | `Long` | `7.65` | 8,800,000.00 USD | 0.00 USD | 38,790.00 USD | `-30.45%` | `5,070,100.00` |
| `Live` | `Long` | `7.75` | 8,760,000.00 USD | 0.00 USD | 15,080.00 USD | `-29.55%` | `1,945,700.00` |
| `Live` | `Long` | `7.85` | 8,740,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.64%` | `401,116,200.00` |
| `Live` | `Long` | `7.95` | 5,600,000.00 USD | 0.00 USD | 15,610.00 USD | `-27.73%` | `1,963,900.00` |
| `Live` | `Long` | `8.05` | 5,580,000.00 USD | 0.00 USD | 66,130.00 USD | `-26.82%` | `8,214,600.00` |
| `Live` | `Long` | `8.15` | 5,510,000.00 USD | 0.00 USD | 90,360.00 USD | `-25.91%` | `11,087,300.00` |
| `Live` | `Long` | `8.25` | 5,420,000.00 USD | 0.00 USD | 32,110.00 USD | `-25.00%` | `3,892,000.00` |
| `Live` | `Long` | `8.35` | 5,390,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.09%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,390,000.00 USD | 0.00 USD | 520,270.00 USD | `-23.18%` | `61,570,800.00` |
| `Live` | `Long` | `8.55` | 4,860,000.00 USD | 0.00 USD | 15,960.00 USD | `-22.27%` | `1,866,700.00` |
| `Live` | `Long` | `8.65` | 4,850,000.00 USD | 0.00 USD | 14,810.00 USD | `-21.36%` | `1,712,600.00` |
| `Live` | `Long` | `8.75` | 4,830,000.00 USD | 0.00 USD | 23,240.00 USD | `-20.45%` | `2,655,700.00` |
| `Live` | `Long` | `8.85` | 4,810,000.00 USD | 0.00 USD | 57,860.00 USD | `-19.55%` | `6,537,900.00` |
| `Live` | `Long` | `8.95` | 4,750,000.00 USD | 0.00 USD | 473,800.00 USD | `-18.64%` | `52,938,100.00` |
| `Live` | `Long` | `9.05` | 4,280,000.00 USD | 0.00 USD | 87,420.00 USD | `-17.73%` | `9,660,200.00` |
| `Live` | `Long` | `9.15` | 4,190,000.00 USD | 0.00 USD | 76,340.00 USD | `-16.82%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,120,000.00 USD | 0.00 USD | 19,930.00 USD | `-15.91%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,100,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.00%` | `229,774,900.00` |
| `Live` | `Long` | `9.45` | 1,950,000.00 USD | 0.00 USD | 55,970.00 USD | `-14.09%` | `5,922,500.00` |
| `Live` | `Long` | `9.55` | 1,890,000.00 USD | 0.00 USD | 102,020.00 USD | `-13.18%` | `10,682,700.00` |
| `Live` | `Long` | `9.65` | 1,790,000.00 USD | 0.00 USD | 204,090.00 USD | `-12.27%` | `21,148,900.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 63,190.00 USD | `-11.36%` | `6,481,300.00` |
| `Live` | `Long` | `9.85` | 1,520,000.00 USD | 0.00 USD | 30,620.00 USD | `-10.45%` | `3,108,900.00` |
| `Live` | `Long` | `9.95` | 1,490,000.00 USD | 0.00 USD | 421,600.00 USD | `-9.55%` | `42,372,100.00` |
| `Live` | `Long` | `10.05` | 1,070,000.00 USD | 0.00 USD | 781,760.00 USD | `-8.64%` | `77,786,700.00` |
| `Live` | `Long` | `10.15` | 287,760.00 USD | 0.00 USD | 79,580.00 USD | `-7.73%` | `7,840,300.00` |
| `Live` | `Long` | `10.25` | 208,180.00 USD | 0.00 USD | 32,460.00 USD | `-6.82%` | `3,166,900.00` |
| `Live` | `Long` | `10.35` | 175,720.00 USD | 0.00 USD | 140,720.00 USD | `-5.91%` | `13,596,500.00` |
| `Live` | `Long` | `10.45` | 34,990.00 USD | 0.00 USD | 26,900.00 USD | `-5.00%` | `2,574,100.00` |
| `Live` | `Long` | `10.55` | 8,100.00 USD | 0.00 USD | 8,100.00 USD | `-4.09%` | `767,300.00` |
| `Live` | `Short` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | `+4.09%` | `21,800.00` |
| `Live` | `Short` | `11.85` | 1,670.00 USD | 1,420.00 USD | 0.00 USD | `+7.73%` | `119,600.00` |
| `Live` | `Short` | `11.95` | 7,310.00 USD | 5,650.00 USD | 0.00 USD | `+8.64%` | `472,500.00` |
| `Live` | `Short` | `12.25` | 8,740.00 USD | 1,430.00 USD | 0.00 USD | `+11.36%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 10,680.00 USD | 1,940.00 USD | 0.00 USD | `+12.27%` | `157,000.00` |
| `Live` | `Short` | `12.45` | 12,660.00 USD | 1,980.00 USD | 0.00 USD | `+13.18%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 13,730.00 USD | 1,070.00 USD | 0.00 USD | `+14.09%` | `85,200.00` |
| `Live` | `Short` | `12.65` | 14,510.00 USD | 779.24 USD | 0.00 USD | `+15.00%` | `61,600.00` |
| `Live` | `Short` | `12.85` | 15,040.00 USD | 535.85 USD | 0.00 USD | `+16.82%` | `41,700.00` |
| `Live` | `Short` | `13.25` | 16,100.00 USD | 1,060.00 USD | 0.00 USD | `+20.45%` | `79,900.00` |
| `Live` | `Short` | `13.45` | 21,530.00 USD | 5,430.00 USD | 0.00 USD | `+22.27%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 114,430.00 USD | 92,890.00 USD | 0.00 USD | `+23.18%` | `6,855,700.00` |
| `Live` | `Short` | `14.05` | 115,290.00 USD | 866.89 USD | 0.00 USD | `+27.73%` | `61,700.00` |
| `Live` | `Short` | `14.25` | 115,840.00 USD | 544.35 USD | 0.00 USD | `+29.55%` | `38,200.00` |
| `Live` | `Short` | `14.35` | 119,700.00 USD | 3,860.00 USD | 0.00 USD | `+30.45%` | `269,100.00` |
| `Live` | `Short` | `14.45` | 123,980.00 USD | 4,280.00 USD | 0.00 USD | `+31.36%` | `296,400.00` |
| `Live` | `Short` | `14.95` | 149,320.00 USD | 25,330.00 USD | 0.00 USD | `+35.91%` | `1,694,600.00` |
| `Live` | `Short` | `15.25` | 149,470.00 USD | 155.55 USD | 0.00 USD | `+38.64%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 150,050.00 USD | 578.46 USD | 0.00 USD | `+41.36%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 150,320.00 USD | 271.04 USD | 0.00 USD | `+44.09%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 150,460.00 USD | 138.76 USD | 0.00 USD | `+45.00%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 150,780.00 USD | 323.00 USD | 0.00 USD | `+46.82%` | `20,000.00` |
| `Live` | `Short` | `16.35` | 152,180.00 USD | 1,390.00 USD | 0.00 USD | `+48.64%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 152,410.00 USD | 230.30 USD | 0.00 USD | `+49.55%` | `14,000.00` |
| `Live` | `Short` | `16.55` | 184,110.00 USD | 31,700.00 USD | 0.00 USD | `+50.45%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 286,020.00 USD | 101,910.00 USD | 0.00 USD | `+52.27%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 365,790.00 USD | 79,770.00 USD | 0.00 USD | `+54.09%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 367,160.00 USD | 1,370.00 USD | 0.00 USD | `+55.91%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 393,860.00 USD | 26,700.00 USD | 0.00 USD | `+57.73%` | `1,539,000.00` |
| `Live` | `Short` | `17.55` | 393,960.00 USD | 101.79 USD | 0.00 USD | `+59.55%` | `5,800.00` |
| `Live` | `Short` | `17.65` | 399,420.00 USD | 5,450.00 USD | 0.00 USD | `+60.45%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 649,000.00 USD | 249,580.00 USD | 0.00 USD | `+62.27%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 649,350.00 USD | 351.82 USD | 0.00 USD | `+63.18%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 651,320.00 USD | 1,970.00 USD | 0.00 USD | `+64.09%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 679,240.00 USD | 27,920.00 USD | 0.00 USD | `+65.91%` | `1,529,600.00` |
| `Live` | `Short` | `18.45` | 2,810,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+67.73%` | `115,235,400.00` |
| `Live` | `Short` | `18.55` | 2,810,000.00 USD | 185.50 USD | 0.00 USD | `+68.64%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,870,000.00 USD | 63,600.00 USD | 0.00 USD | `+69.55%` | `3,410,000.00` |
| `Live` | `Short` | `18.75` | 3,580,000.00 USD | 707,060.00 USD | 0.00 USD | `+70.45%` | `37,710,000.00` |
| `Live` | `Short` | `18.85` | 3,650,000.00 USD | 75,870.00 USD | 0.00 USD | `+71.36%` | `4,024,800.00` |
| `Live` | `Short` | `18.95` | 3,650,000.00 USD | 619.67 USD | 0.00 USD | `+72.27%` | `32,700.00` |
| `Live` | `Short` | `19.55` | 3,650,000.00 USD | 316.71 USD | 0.00 USD | `+77.73%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,690,000.00 USD | 39,570.00 USD | 0.00 USD | `+78.64%` | `2,013,700.00` |
| `Live` | `Short` | `19.75` | 3,690,000.00 USD | 359.45 USD | 0.00 USD | `+79.55%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,690,000.00 USD | 291.27 USD | 0.00 USD | `+81.36%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,690,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.18%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,700,000.00 USD | 1,770.00 USD | 0.00 USD | `+85.91%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,700,000.00 USD | 7,250.00 USD | 0.00 USD | `+86.82%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,700,000.00 USD | 114.68 USD | 0.00 USD | `+89.55%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,700,000.00 USD | 202.08 USD | 0.00 USD | `+91.36%` | `9,600.00` |
| `Live` | `Short` | `21.75` | 3,770,000.00 USD | 65,060.00 USD | 0.00 USD | `+97.73%` | `2,991,400.00` |
| `Live` | `Short` | `21.85` | 3,770,000.00 USD | 222.87 USD | 0.00 USD | `+98.64%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 413,080.00 USD | 0.00 USD | 182.03 USD | `-77.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 412,900.00 USD | 0.00 USD | 221.45 USD | `-74.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 412,670.00 USD | 0.00 USD | 234.23 USD | `-73.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 412,440.00 USD | 0.00 USD | 209.48 USD | `-71.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 412,230.00 USD | 0.00 USD | 236.33 USD | `-68.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 411,990.00 USD | 0.00 USD | 431.68 USD | `-67.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 411,560.00 USD | 0.00 USD | 290.29 USD | `-58.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 411,270.00 USD | 0.00 USD | 120.22 USD | `-52.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 411,150.00 USD | 0.00 USD | 3,790.00 USD | `-48.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 407,360.00 USD | 0.00 USD | 251.68 USD | `-45.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 407,110.00 USD | 0.00 USD | 749.94 USD | `-42.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 406,360.00 USD | 0.00 USD | 772.71 USD | `-41.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 405,580.00 USD | 0.00 USD | 3,760.00 USD | `-40.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 401,820.00 USD | 0.00 USD | 133.00 USD | `-39.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 401,690.00 USD | 0.00 USD | 1,320.00 USD | `-36.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 400,370.00 USD | 0.00 USD | 3,770.00 USD | `-35.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 396,600.00 USD | 0.00 USD | 2,070.00 USD | `-34.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 394,530.00 USD | 0.00 USD | 3,740.00 USD | `-32.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 390,790.00 USD | 0.00 USD | 1,050.00 USD | `-31.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 389,740.00 USD | 0.00 USD | 120.90 USD | `-29.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 389,610.00 USD | 0.00 USD | 146.80 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 389,470.00 USD | 0.00 USD | 124.02 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 389,340.00 USD | 0.00 USD | 5,000.00 USD | `-26.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 384,340.00 USD | 0.00 USD | 393.64 USD | `-25.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 383,950.00 USD | 0.00 USD | 10,560.00 USD | `-25.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 373,380.00 USD | 0.00 USD | 57,340.00 USD | `-24.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 316,040.00 USD | 0.00 USD | 1,480.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 314,560.00 USD | 0.00 USD | 52,990.00 USD | `-22.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 261,580.00 USD | 0.00 USD | 186.84 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 261,390.00 USD | 0.00 USD | 742.88 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 260,650.00 USD | 0.00 USD | 902.70 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 259,740.00 USD | 0.00 USD | 1,570.00 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 258,180.00 USD | 0.00 USD | 3,440.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 254,730.00 USD | 0.00 USD | 194.90 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 254,540.00 USD | 0.00 USD | 232.18 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 254,300.00 USD | 0.00 USD | 9,010.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 245,300.00 USD | 0.00 USD | 518.80 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 244,780.00 USD | 0.00 USD | 19,590.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 225,190.00 USD | 0.00 USD | 686.12 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 224,500.00 USD | 0.00 USD | 3,030.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 221,470.00 USD | 0.00 USD | 24,350.00 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 197,110.00 USD | 0.00 USD | 3,450.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 193,670.00 USD | 0.00 USD | 44,450.00 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 149,220.00 USD | 0.00 USD | 5,650.00 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 143,570.00 USD | 0.00 USD | 48,680.00 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 94,890.00 USD | 0.00 USD | 3,540.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 91,350.00 USD | 0.00 USD | 20,560.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 70,790.00 USD | 0.00 USD | 18,080.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 52,710.00 USD | 0.00 USD | 6,120.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 46,590.00 USD | 0.00 USD | 34,900.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 11,690.00 USD | 0.00 USD | 3,710.00 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 7,980.00 USD | 0.00 USD | 7,980.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 7,550.00 USD | 7,550.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 32,980.00 USD | 25,430.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 45,610.00 USD | 12,640.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 62,280.00 USD | 16,660.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 66,160.00 USD | 3,880.00 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 92,030.00 USD | 25,870.00 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 94,970.00 USD | 2,940.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 95,970.00 USD | 992.88 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 103,090.00 USD | 7,130.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 106,950.00 USD | 3,850.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 134,660.00 USD | 27,710.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 136,590.00 USD | 1,930.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 229,870.00 USD | 93,280.00 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 230,470.00 USD | 597.74 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 235,130.00 USD | 4,650.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 237,620.00 USD | 2,500.00 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 243,800.00 USD | 6,180.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 244,480.00 USD | 679.57 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 264,850.00 USD | 20,360.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 265,300.00 USD | 451.95 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 281,930.00 USD | 16,630.00 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 282,850.00 USD | 919.19 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 284,160.00 USD | 1,320.00 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 291,950.00 USD | 7,790.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 294,490.00 USD | 2,540.00 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 295,950.00 USD | 1,470.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 296,910.00 USD | 954.14 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 316,460.00 USD | 19,550.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 321,340.00 USD | 4,880.00 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 321,610.00 USD | 266.44 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 337,870.00 USD | 16,260.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 338,020.00 USD | 152.82 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 342,300.00 USD | 4,280.00 USD | 0.00 USD | `+29.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 345,710.00 USD | 3,410.00 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 364,430.00 USD | 18,720.00 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 364,650.00 USD | 218.25 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 366,500.00 USD | 1,850.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 373,770.00 USD | 7,270.00 USD | 0.00 USD | `+34.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 374,720.00 USD | 950.82 USD | 0.00 USD | `+35.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 400,410.00 USD | 25,700.00 USD | 0.00 USD | `+36.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 402,860.00 USD | 2,450.00 USD | 0.00 USD | `+37.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 635,900.00 USD | 233,040.00 USD | 0.00 USD | `+38.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 636,830.00 USD | 924.07 USD | 0.00 USD | `+39.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 637,720.00 USD | 893.01 USD | 0.00 USD | `+40.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 662,460.00 USD | 24,740.00 USD | 0.00 USD | `+41.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 662,700.00 USD | 237.88 USD | 0.00 USD | `+42.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 665,990.00 USD | 3,290.00 USD | 0.00 USD | `+43.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 669,160.00 USD | 3,170.00 USD | 0.00 USD | `+44.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 674,300.00 USD | 5,130.00 USD | 0.00 USD | `+45.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 689,730.00 USD | 15,440.00 USD | 0.00 USD | `+45.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 696,540.00 USD | 6,800.00 USD | 0.00 USD | `+46.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 703,040.00 USD | 6,500.00 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 709,580.00 USD | 6,540.00 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 716,160.00 USD | 6,580.00 USD | 0.00 USD | `+49.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 726,090.00 USD | 9,930.00 USD | 0.00 USD | `+50.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 830,070.00 USD | 103,980.00 USD | 0.00 USD | `+51.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 844,310.00 USD | 14,240.00 USD | 0.00 USD | `+52.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 928,660.00 USD | 84,360.00 USD | 0.00 USD | `+53.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 930,360.00 USD | 1,700.00 USD | 0.00 USD | `+54.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 937,720.00 USD | 7,370.00 USD | 0.00 USD | `+55.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 939,440.00 USD | 1,710.00 USD | 0.00 USD | `+55.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 941,740.00 USD | 2,300.00 USD | 0.00 USD | `+56.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 943,480.00 USD | 1,740.00 USD | 0.00 USD | `+57.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 966,040.00 USD | 22,560.00 USD | 0.00 USD | `+58.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 970,430.00 USD | 4,390.00 USD | 0.00 USD | `+59.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 974,840.00 USD | 4,410.00 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 979,280.00 USD | 4,440.00 USD | 0.00 USD | `+61.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 983,740.00 USD | 4,460.00 USD | 0.00 USD | `+62.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 984,190.00 USD | 448.75 USD | 0.00 USD | `+63.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,020,000.00 USD | 30,960.00 USD | 0.00 USD | `+64.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,020,000.00 USD | 453.75 USD | 0.00 USD | `+65.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,020,000.00 USD | 456.25 USD | 0.00 USD | `+65.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,020,000.00 USD | 458.75 USD | 0.00 USD | `+66.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,020,000.00 USD | 461.25 USD | 0.00 USD | `+67.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,020,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,020,000.00 USD | 466.25 USD | 0.00 USD | `+69.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,020,000.00 USD | 468.75 USD | 0.00 USD | `+70.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,020,000.00 USD | 471.25 USD | 0.00 USD | `+71.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,020,000.00 USD | 473.75 USD | 0.00 USD | `+72.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,090,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,090,000.00 USD | 574.50 USD | 0.00 USD | `+74.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,090,000.00 USD | 577.50 USD | 0.00 USD | `+75.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,090,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,100,000.00 USD | 972.50 USD | 0.00 USD | `+76.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,100,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,100,000.00 USD | 786.00 USD | 0.00 USD | `+78.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,100,000.00 USD | 790.00 USD | 0.00 USD | `+79.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,110,000.00 USD | 992.50 USD | 0.00 USD | `+80.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,110,000.00 USD | 997.50 USD | 0.00 USD | `+81.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,710,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+82.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,720,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,720,000.00 USD | 1,040.00 USD | 0.00 USD | `+88.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,720,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,720,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,720,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,730,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,770,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+94.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,770,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,780,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,780,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,780,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.55%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.15` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD |
| `7D` | `9.17` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD |
| `7D` | `9.19` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD |
| `7D` | `9.21` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD |
| `7D` | `9.23` | 12,720,000.00 USD | 0.00 USD | 12,720,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD |
| `7D` | `9.25` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD |
| `7D` | `9.27` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD |
| `7D` | `9.29` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD |
| `7D` | `9.31` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD |
| `7D` | `9.33` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD |
| `7D` | `9.35` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD |
| `7D` | `9.37` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD |
| `7D` | `9.39` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD |
| `7D` | `9.41` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD |
| `7D` | `9.43` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD |
| `7D` | `9.45` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD |
| `7D` | `9.47` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.49` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD |
| `7D` | `9.51` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `9.53` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD |
| `7D` | `9.55` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD |
| `7D` | `9.57` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,150.00 USD |
| `7D` | `9.59` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,540.00 USD |
| `7D` | `9.61` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD |
| `7D` | `9.63` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD |
| `7D` | `9.65` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD |
| `7D` | `9.69` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.73` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.75` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD |
| `7D` | `9.77` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD |
| `7D` | `9.79` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.81` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD |
| `7D` | `9.83` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD |
| `7D` | `9.85` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD |
| `7D` | `9.87` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD |
| `1D` | `9.89` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 11,010.00 USD | 9,160.00 USD | 11,570.00 USD |
| `7D` | `9.89` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD |
| `1D` | `9.91` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 35,210.00 USD | 36,170.00 USD | 2,290.00 USD |
| `7D` | `9.91` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.93` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 17,260.00 USD | 14,790.00 USD | 219.74 USD |
| `7D` | `9.93` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD |
| `1D` | `9.95` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 14,390.00 USD | 7,200.00 USD | 8,900.00 USD |
| `7D` | `9.95` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD |
| `1D` | `9.97` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 77,130.00 USD | 7,890.00 USD | 60,310.00 USD |
| `7D` | `9.97` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD |
| `1D` | `9.99` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 8,980.00 USD | 7,950.00 USD | 73,220.00 USD |
| `7D` | `9.99` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD |
| `1D` | `10.01` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 14,600.00 USD | 6,210.00 USD | 24,690.00 USD |
| `7D` | `10.01` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD |
| `1D` | `10.03` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 6,170.00 USD | 15,550.00 USD | 264.22 USD |
| `7D` | `10.03` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.05` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 38,520.00 USD | 555.00 USD | 18,800.00 USD |
| `7D` | `10.05` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD |
| `1D` | `10.07` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,450.00 USD |
| `7D` | `10.07` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.09` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,120.00 USD |
| `7D` | `10.09` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 7,530.00 USD | 41,480.00 USD | 123.54 USD |
| `7D` | `10.11` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD |
| `1D` | `10.13` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD |
| `7D` | `10.13` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD |
| `1D` | `10.15` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,470.00 USD |
| `7D` | `10.15` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD |
| `1D` | `10.17` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 127,800.00 USD | 25,060.00 USD | 640.95 USD |
| `7D` | `10.17` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD |
| `1D` | `10.19` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,270.00 USD |
| `7D` | `10.19` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD |
| `1D` | `10.21` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,560.00 USD |
| `7D` | `10.21` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD |
| `1D` | `10.23` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 100,980.00 USD | 58,340.00 USD | 282,510.00 USD |
| `7D` | `10.23` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD |
| `1D` | `10.25` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 9,900.00 USD | 25,460.00 USD | 34,360.00 USD |
| `7D` | `10.25` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD |
| `1D` | `10.27` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 64,690.00 USD | 18,820.00 USD | 130,260.00 USD |
| `7D` | `10.27` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD |
| `1D` | `10.29` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 328,720.00 USD | 1,910.00 USD | 151,660.00 USD |
| `7D` | `10.29` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD |
| `1D` | `10.31` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 11,920.00 USD | 19,120.00 USD | 44,080.00 USD |
| `7D` | `10.31` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.33` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 11,690.00 USD | 3,820.00 USD | 45,040.00 USD |
| `7D` | `10.33` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.35` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 61,320.00 USD | 6,620.00 USD | 72,840.00 USD |
| `7D` | `10.35` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.37` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 12,790.00 USD | 13,750.00 USD | 7,590.00 USD |
| `7D` | `10.37` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.39` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD |
| `7D` | `10.39` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.41` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,810.00 USD |
| `7D` | `10.41` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD |
| `1D` | `10.43` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 311,620.00 USD | 0.00 USD | 88,870.00 USD |
| `7D` | `10.43` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD |
| `1D` | `10.45` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 330,070.00 USD | 44,950.00 USD | 216,610.00 USD |
| `7D` | `10.45` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD |
| `1D` | `10.47` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,200.00 USD |
| `7D` | `10.47` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD |
| `1D` | `10.49` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 41,670.00 USD | 38,130.00 USD | 25,100.00 USD |
| `7D` | `10.49` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD |
| `1D` | `10.51` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 11,220.00 USD | 10,370.00 USD | 13,010.00 USD |
| `7D` | `10.51` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD |
| `1D` | `10.53` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 1,160.00 USD | 18,090.00 USD | 117,670.00 USD |
| `7D` | `10.53` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD |
| `1D` | `10.55` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 65,860.00 USD | 48,520.00 USD | 52,320.00 USD |
| `7D` | `10.55` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 121,680.00 USD | 114,000.00 USD | 0.00 USD |
| `1D` | `10.57` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 58,630.00 USD | 33,630.00 USD | 15,210.00 USD |
| `7D` | `10.57` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.59` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 26,670.00 USD | 27,220.00 USD | 15,230.00 USD |
| `7D` | `10.59` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD |
| `1D` | `10.61` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 9,410.00 USD | 9,370.00 USD | 18,130.00 USD |
| `7D` | `10.61` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD |
| `1D` | `10.63` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 42,360.00 USD | 2,580.00 USD | 128,370.00 USD |
| `7D` | `10.63` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD |
| `1D` | `10.65` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 77,540.00 USD | 6,020.00 USD | 46,280.00 USD |
| `7D` | `10.65` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD |
| `1D` | `10.67` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 67,580.00 USD | 15,280.00 USD | 31,800.00 USD |
| `7D` | `10.67` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD |
| `1D` | `10.69` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 36,050.00 USD | 30,270.00 USD | 36,190.00 USD |
| `7D` | `10.69` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD |
| `1D` | `10.71` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD |
| `7D` | `10.71` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `10.73` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD |
| `7D` | `10.73` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.75` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 89,590.00 USD | 8,370.00 USD | 0.00 USD |
| `7D` | `10.75` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD |
| `1D` | `10.77` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 22,390.00 USD | 62,430.00 USD | 51,590.00 USD |
| `7D` | `10.77` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 537,300.00 USD | 111,300.00 USD | 103,760.00 USD |
| `1D` | `10.79` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 203,110.00 USD | 141,500.00 USD | 30,420.00 USD |
| `7D` | `10.79` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 79,540.00 USD | 64,510.00 USD | 0.00 USD |
| `1D` | `10.81` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 30,730.00 USD | 23,590.00 USD | 0.00 USD |
| `7D` | `10.81` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD |
| `1D` | `10.83` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 334,330.00 USD | 15,810.00 USD | 5,210.00 USD |
| `7D` | `10.83` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD |
| `1D` | `10.85` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 148,850.00 USD | 17,390.00 USD | 199,760.00 USD |
| `7D` | `10.85` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD |
| `1D` | `10.87` | 674,150.00 USD | 0.00 USD | 674,150.00 USD | 155,080.00 USD | 10,430.00 USD | 45,180.00 USD |
| `7D` | `10.87` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD |
| `1D` | `10.89` | 463,460.00 USD | 0.00 USD | 463,460.00 USD | 76,840.00 USD | 14,710.00 USD | 63,610.00 USD |
| `7D` | `10.89` | 959,600.00 USD | 0.00 USD | 959,600.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD |
| `1D` | `10.91` | 308,310.00 USD | 0.00 USD | 308,310.00 USD | 164,650.00 USD | 33,540.00 USD | 0.00 USD |
| `7D` | `10.91` | 545,160.00 USD | 0.00 USD | 545,160.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD |
| `1D` | `10.93` | 110,120.00 USD | 0.00 USD | 110,120.00 USD | 3,920.00 USD | 15,020.00 USD | 86.22 USD |
| `7D` | `10.93` | 286,690.00 USD | 0.00 USD | 286,690.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.95` | 91,090.00 USD | 0.00 USD | 91,090.00 USD | 1,550.00 USD | 1,320.00 USD | 87,750.00 USD |
| `7D` | `10.95` | 70,060.00 USD | 0.00 USD | 70,060.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD |
| `7D` | `10.97` | 12,320.00 USD | 0.00 USD | 12,320.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 467.00 USD | 0.00 USD | 467.00 USD | 0.00 USD | 467.00 USD | 0.00 USD |
| `7D` | `10.99` | 224,900.00 USD | 224,900.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD |
| `7D` | `10.99` | 449,800.00 USD | 449,800.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.01` | 103.72 USD | 103.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | 103.72 USD |
| `7D` | `11.01` | 461,480.00 USD | 461,480.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD |
| `1D` | `11.03` | 305,760.00 USD | 305,760.00 USD | 0.00 USD | 0.00 USD | 718.45 USD | 304,940.00 USD |
| `7D` | `11.03` | 729,460.00 USD | 729,460.00 USD | 0.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD |
| `1D` | `11.05` | 307,340.00 USD | 307,340.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD | 99.36 USD |
| `7D` | `11.05` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD |
| `1D` | `11.07` | 334,320.00 USD | 334,320.00 USD | 0.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD |
| `7D` | `11.07` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.09` | 640,970.00 USD | 640,970.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | 302,140.00 USD |
| `7D` | `11.09` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD |
| `1D` | `11.11` | 652,780.00 USD | 652,780.00 USD | 0.00 USD | 9,550.00 USD | 2,260.00 USD | 0.00 USD |
| `7D` | `11.11` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD |
| `1D` | `11.13` | 857,200.00 USD | 857,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 204,420.00 USD |
| `7D` | `11.13` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD |
| `1D` | `11.15` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 109,480.00 USD | 506.95 USD | 50,270.00 USD |
| `7D` | `11.15` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD |
| `1D` | `11.17` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 22,450.00 USD | 2,450.00 USD | 59,080.00 USD |
| `7D` | `11.17` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD |
| `1D` | `11.19` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 72,050.00 USD | 22,010.00 USD | 40,560.00 USD |
| `7D` | `11.19` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD |
| `1D` | `11.21` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 122,450.00 USD | 59,670.00 USD | 113,960.00 USD |
| `7D` | `11.21` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 554,520.00 USD | 106,700.00 USD | 1,090.00 USD |
| `1D` | `11.23` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 286,200.00 USD | 61,040.00 USD | 101,640.00 USD |
| `7D` | `11.23` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 288,220.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 125,190.00 USD | 57,600.00 USD | 109,560.00 USD |
| `7D` | `11.25` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD |
| `1D` | `11.27` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 329,340.00 USD | 15,580.00 USD | 178,310.00 USD |
| `7D` | `11.27` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.29` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 237,630.00 USD | 122,270.00 USD | 276,930.00 USD |
| `7D` | `11.29` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD |
| `1D` | `11.31` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 218,320.00 USD | 72,220.00 USD | 111,700.00 USD |
| `7D` | `11.31` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 219,020.00 USD | 45,400.00 USD | 95,220.00 USD |
| `7D` | `11.33` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD |
| `1D` | `11.35` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 343,170.00 USD | 135,950.00 USD | 84,490.00 USD |
| `7D` | `11.35` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD |
| `1D` | `11.37` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 152,070.00 USD | 105,530.00 USD | 47,530.00 USD |
| `7D` | `11.37` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD |
| `1D` | `11.39` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 14,820.00 USD | 47,470.00 USD | 7,570.00 USD |
| `7D` | `11.39` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 96,590.00 USD | 35,740.00 USD | 140,680.00 USD |
| `7D` | `11.41` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD |
| `1D` | `11.43` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 64,580.00 USD | 56,680.00 USD | 132,800.00 USD |
| `7D` | `11.43` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 265,450.00 USD | 105,330.00 USD | 92,240.00 USD |
| `1D` | `11.45` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 95,070.00 USD | 94,930.00 USD | 35,780.00 USD |
| `7D` | `11.45` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 227,420.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.47` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 64,860.00 USD | 28,930.00 USD | 23,420.00 USD |
| `7D` | `11.47` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 42,800.00 USD | 33,150.00 USD | 37,280.00 USD |
| `7D` | `11.49` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 71,900.00 USD | 30,900.00 USD | 56,650.00 USD |
| `7D` | `11.51` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD |
| `1D` | `11.53` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 111,420.00 USD | 18,960.00 USD | 63,640.00 USD |
| `7D` | `11.53` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD |
| `1D` | `11.55` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 112,800.00 USD | 7,230.00 USD | 70,140.00 USD |
| `7D` | `11.55` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD |
| `1D` | `11.57` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 102,740.00 USD | 17,450.00 USD | 23,920.00 USD |
| `7D` | `11.57` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.59` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 28,580.00 USD | 17,270.00 USD | 39,570.00 USD |
| `7D` | `11.59` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD |
| `1D` | `11.61` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 86,530.00 USD | 512.95 USD | 85,200.00 USD |
| `7D` | `11.61` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.63` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 3,670.00 USD | 6,700.00 USD | 31,290.00 USD |
| `7D` | `11.63` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.65` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 2,630.00 USD | 7,840.00 USD | 63.02 USD |
| `7D` | `11.65` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD |
| `1D` | `11.67` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 19,420.00 USD | 11,530.00 USD | 57,510.00 USD |
| `7D` | `11.67` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD |
| `1D` | `11.69` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 106,690.00 USD | 34,170.00 USD | 352.04 USD |
| `7D` | `11.69` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD |
| `1D` | `11.71` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 55,880.00 USD | 13,000.00 USD | 15,390.00 USD |
| `7D` | `11.71` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD |
| `1D` | `11.73` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 140,030.00 USD | 11,770.00 USD | 120,130.00 USD |
| `7D` | `11.73` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD |
| `1D` | `11.75` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 21,990.00 USD | 38,420.00 USD | 61,390.00 USD |
| `7D` | `11.75` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD |
| `1D` | `11.77` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 41,580.00 USD | 20,480.00 USD | 14,560.00 USD |
| `7D` | `11.77` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 12,300.00 USD | 339.50 USD | 40,240.00 USD |
| `7D` | `11.79` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.81` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 281.26 USD | 17,880.00 USD | 17,880.00 USD |
| `7D` | `11.81` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 11,600.00 USD | 11,560.00 USD | 29,420.00 USD |
| `7D` | `11.83` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.85` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 54,810.00 USD | 8,620.00 USD | 69,830.00 USD |
| `7D` | `11.85` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.87` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 20,840.00 USD | 20,660.00 USD | 53,710.00 USD |
| `7D` | `11.87` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.89` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 43,100.00 USD | 13,000.00 USD | 43,750.00 USD |
| `7D` | `11.89` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.91` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 102,960.00 USD | 18,190.00 USD | 31,690.00 USD |
| `7D` | `11.91` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.93` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 135,130.00 USD | 28,180.00 USD | 28,570.00 USD |
| `7D` | `11.93` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 84,630.00 USD | 20,620.00 USD | 43,540.00 USD |
| `7D` | `11.95` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.97` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 71,610.00 USD | 36,230.00 USD | 87,420.00 USD |
| `7D` | `11.97` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.99` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 107,470.00 USD | 27,660.00 USD | 36,360.00 USD |
| `7D` | `11.99` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.01` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 47,340.00 USD | 9,290.00 USD | 50,020.00 USD |
| `7D` | `12.01` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD |
| `1D` | `12.03` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 46,830.00 USD | 34,660.00 USD | 24,300.00 USD |
| `7D` | `12.03` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD |
| `1D` | `12.05` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 108,860.00 USD | 43,590.00 USD | 59,560.00 USD |
| `7D` | `12.05` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.07` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 34,850.00 USD | 33,440.00 USD | 67,900.00 USD |
| `7D` | `12.07` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD |
| `1D` | `12.09` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 21,370.00 USD | 24,790.00 USD | 27,880.00 USD |
| `7D` | `12.09` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD |
| `1D` | `12.11` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 106,960.00 USD | 41,520.00 USD | 57,600.00 USD |
| `7D` | `12.11` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.13` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 96,640.00 USD | 36,620.00 USD | 39,690.00 USD |
| `7D` | `12.13` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD |
| `1D` | `12.15` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 113,490.00 USD | 42,340.00 USD | 65,330.00 USD |
| `7D` | `12.15` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD |
| `1D` | `12.17` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 123,050.00 USD | 60,070.00 USD | 69,710.00 USD |
| `7D` | `12.17` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.19` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 67,790.00 USD | 24,020.00 USD | 18,670.00 USD |
| `7D` | `12.19` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD |
| `1D` | `12.21` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 37,080.00 USD | 30,260.00 USD | 55,540.00 USD |
| `7D` | `12.21` | 16,170,000.00 USD | 16,170,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD |
| `1D` | `12.23` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 15,850.00 USD | 23,710.00 USD | 10,870.00 USD |
| `7D` | `12.23` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 140,270.00 USD | 27,350.00 USD | 9,170.00 USD |
| `1D` | `12.25` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 2,230.00 USD | 6,420.00 USD | 7,630.00 USD |
| `7D` | `12.25` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 101,460.00 USD | 47,320.00 USD | 46,950.00 USD |
| `1D` | `12.27` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 37,130.00 USD | 8,240.00 USD | 20,000.00 USD |
| `7D` | `12.27` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD |
| `1D` | `12.28` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 22,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `12.29` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD |
| `7D` | `12.31` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD |
| `7D` | `12.33` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD |
| `7D` | `12.35` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD |
| `7D` | `12.37` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD |
| `7D` | `12.39` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD |
| `7D` | `12.40` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `513.49M` | Total OI Tokens: `46,625,683.2 LINK`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-1.16%` | 24h OI Change: `-6.90%`
  * Exchange Breakdown: Binance=`100.11M` | Bybit=`68.50M` | OKX=`26.59M` | Hyperliquid=`55.46M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.87K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0040%` |
| **USDT Bybit** | `-0.0033%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0085%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `53.89%` | `46.11%` | `1.17` | 8,920,000.00 USD |
| `15M` | `Binance` | `57.2%` | `42.8%` | `1.34` | 3,430,000.00 USD |
| `15M` | `OKX` | `54.85%` | `45.15%` | `1.21` | 1,470,000.00 USD |
| `15M` | `Bybit` | `57.52%` | `42.48%` | `1.35` | 861,120.00 USD |
| `15M` | `KuCoin` | `43.63%` | `56.37%` | `0.77` | 64,090.00 USD |
| `15M` | `Gate` | `49.22%` | `50.78%` | `0.97` | 1,520,000.00 USD |
| `15M` | `Bitget` | `50.78%` | `49.22%` | `1.03` | 123,270.00 USD |
| `15M` | `BingX` | `47.75%` | `52.25%` | `0.91` | 234,390.00 USD |
| `15M` | `MEXC` | `56.7%` | `43.3%` | `1.31` | 393,110.00 USD |
| `15M` | `Bitunix` | `51.05%` | `48.95%` | `1.04` | 178,440.00 USD |
| `15M` | `Hyperliquid` | `52.63%` | `47.37%` | `1.11` | 34,660.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `40.64%` | `59.36%` | `0.68` | 57,780.00 USD |
| `15M` | `Crypto.com` | `35.21%` | `64.79%` | `0.54` | 18,010.00 USD |
| `15M` | `WhiteBIT` | `42.21%` | `57.79%` | `0.73` | 372,660.00 USD |
| `15M` | `HTX` | `38.88%` | `61.12%` | `0.64` | 42,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.62%` | `52.38%` | `0.91` | 75,140.00 USD |
| `15M` | `Aster` | `43.75%` | `56.25%` | `0.78` | 36,140.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `76.78%` | `23.22%` | `3.31` | 446.23 USD |
| `15M` | `Whale Positions` | `57.2%` | `42.8%` | `1.34` | 3,430,000.00 USD |
| `15M` | `Global Accounts` | `53.89%` | `46.11%` | `1.17` | 8,920,000.00 USD |
| `1H` | `LINK` | `47.33%` | `52.67%` | `0.90` | 226,850,000.00 USD |
| `1H` | `Binance` | `46.63%` | `53.37%` | `0.87` | 64,290,000.00 USD |
| `1H` | `OKX` | `48.09%` | `51.91%` | `0.93` | 45,250,000.00 USD |
| `1H` | `Bybit` | `50.67%` | `49.33%` | `1.03` | 16,140,000.00 USD |
| `1H` | `KuCoin` | `48.44%` | `51.56%` | `0.94` | 903,970.00 USD |
| `1H` | `Gate` | `50.73%` | `49.27%` | `1.03` | 17,270,000.00 USD |
| `1H` | `Bitget` | `41.12%` | `58.88%` | `0.70` | 12,320,000.00 USD |
| `1H` | `BingX` | `46.61%` | `53.39%` | `0.87` | 9,310,000.00 USD |
| `1H` | `MEXC` | `44.81%` | `55.19%` | `0.81` | 29,920,000.00 USD |
| `1H` | `Bitunix` | `49.41%` | `50.59%` | `0.98` | 9,690,000.00 USD |
| `1H` | `Hyperliquid` | `51.36%` | `48.64%` | `1.06` | 8,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.32%` | `48.68%` | `1.05` | 6,960,000.00 USD |
| `1H` | `Crypto.com` | `44.24%` | `55.76%` | `0.79` | 585,360.00 USD |
| `1H` | `WhiteBIT` | `43.91%` | `56.09%` | `0.78` | 1,730,000.00 USD |
| `1H` | `HTX` | `45.29%` | `54.71%` | `0.83` | 275,780.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `30.06%` | `69.94%` | `0.43` | 1,300,000.00 USD |
| `1H` | `Aster` | `47.71%` | `52.29%` | `0.91` | 1,100,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.49%` | `49.51%` | `1.02` | 1,670,000.00 USD |
| `1H` | `Whale Positions` | `46.63%` | `53.37%` | `0.87` | 64,290,000.00 USD |
| `1H` | `Global Accounts` | `47.33%` | `52.67%` | `0.90` | 226,850,000.00 USD |
| `4H` | `LINK` | `45.48%` | `54.52%` | `0.83` | 162,430,000.00 USD |
| `4H` | `Binance` | `45.29%` | `54.71%` | `0.83` | 61,090,000.00 USD |
| `4H` | `OKX` | `46.3%` | `53.7%` | `0.86` | 32,950,000.00 USD |
| `4H` | `Bybit` | `43.61%` | `56.39%` | `0.77` | 10,680,000.00 USD |
| `4H` | `KuCoin` | `44.21%` | `55.79%` | `0.79` | 1,060,000.00 USD |
| `4H` | `Gate` | `46.72%` | `53.28%` | `0.88` | 27,140,000.00 USD |
| `4H` | `Bitget` | `40.12%` | `59.88%` | `0.67` | 3,240,000.00 USD |
| `4H` | `BingX` | `36.82%` | `63.18%` | `0.58` | 2,910,000.00 USD |
| `4H` | `MEXC` | `47.81%` | `52.19%` | `0.92` | 11,650,000.00 USD |
| `4H` | `Bitunix` | `49.94%` | `50.06%` | `1.00` | 4,270,000.00 USD |
| `4H` | `Hyperliquid` | `57.12%` | `42.88%` | `1.33` | 1,180,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.37%` | `48.63%` | `1.06` | 1,140,000.00 USD |
| `4H` | `Crypto.com` | `34.66%` | `65.34%` | `0.53` | 195,730.00 USD |
| `4H` | `WhiteBIT` | `26.13%` | `73.87%` | `0.35` | 2,770,000.00 USD |
| `4H` | `HTX` | `53.64%` | `46.36%` | `1.16` | 1,010,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.3%` | `57.7%` | `0.73` | 269,060.00 USD |
| `4H` | `Aster` | `41.53%` | `58.47%` | `0.71` | 822,330.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.62%` | `43.38%` | `1.31` | 21,880.00 USD |
| `4H` | `Whale Positions` | `45.29%` | `54.71%` | `0.83` | 61,090,000.00 USD |
| `4H` | `Global Accounts` | `45.48%` | `54.52%` | `0.83` | 162,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.13` | `11.13` | `11.13` | `11.18` | `11.10` | 1,213,870.73 USD | 582,767.27 USD | 631,103.46 USD | -48,336.19 USD | `-3.98%` | `13B / 23S` |
| `5:00 UTC` | `11.16` | `11.13` | `11.16` | `11.17` | `11.07` | 2,366,030.30 USD | 1,531,021.43 USD | 835,008.87 USD | 696,012.56 USD | `+29.42%` | `24B / 20S` |
| `0:00 UTC` | `11.13` | `11.11` | `11.13` | `11.15` | `11.07` | 1,690,695.18 USD | 790,625.60 USD | 900,069.57 USD | -109,443.97 USD | `-6.47%` | `4B / 10S` |
| `5:00 UTC` | `11.11` | `11.11` | `11.11` | `11.13` | `11.07` | 1,646,720.35 USD | 860,860.38 USD | 785,859.96 USD | 75,000.42 USD | `+4.55%` | `16B / 7S` |
| `0:00 UTC` | `11.14` | `11.07` | `11.14` | `11.15` | `11.01` | 2,445,438.23 USD | 1,141,920.05 USD | 1,303,518.19 USD | -161,598.14 USD | `-6.61%` | `15B / 43S` |
| `5:00 UTC` | `11.07` | `11.04` | `11.07` | `11.07` | `11.00` | 2,041,123.66 USD | 896,885.50 USD | 1,144,238.16 USD | -247,352.65 USD | `-12.12%` | `4B / 9S` |
| `0:00 UTC` | `11.04` | `11.03` | `11.04` | `11.08` | `10.99` | 1,789,361.54 USD | 895,862.51 USD | 893,499.03 USD | 2,363.48 USD | `+0.13%` | `15B / 15S` |
| `5:00 UTC` | `11.07` | `11.08` | `11.07` | `11.11` | `11.04` | 1,641,738.88 USD | 696,135.31 USD | 945,603.58 USD | -249,468.27 USD | `-15.20%` | `10B / 19S` |
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.07` | `11.00` | 1,477,587.17 USD | 739,486.08 USD | 738,101.09 USD | 1,384.99 USD | `+0.09%` | `8B / 13S` |
| `5:00 UTC` | `11.00` | `11.01` | `11.00` | `11.05` | `10.99` | 1,025,540.05 USD | 485,679.57 USD | 539,860.49 USD | -54,180.92 USD | `-5.28%` | `15B / 17S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 29,570.00 USD | -121,760.00 USD | **`DISTRIBUTION`** |
| `15m` | 267,590.00 USD | 78,230.00 USD | **`ACCUMULATION`** |
| `30m` | 197,540.00 USD | -49,830.00 USD | **`ACCUMULATION`** |
| `1h` | 253,370.00 USD | -259,180.00 USD | **`DISTRIBUTION`** |
| `2h` | -167,330.00 USD | -888,880.00 USD | **`DISTRIBUTION`** |
| `4h` | -103,060.00 USD | -627,380.00 USD | **`DISTRIBUTION`** |
| `6h` | -588,400.00 USD | -410,090.00 USD | **`DISTRIBUTION`** |
| `8h` | -745,630.00 USD | 916,250.00 USD | **`ACCUMULATION`** |
| `12h` | -7,620,000.00 USD | -13,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,940,000.00 USD | -22,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,370,000.00 USD | -42,080,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,450,000.00 USD | -192,620,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+29.57K` | 15m=`+267.59K` | 1h=`+253.37K` | 24h=`-10.94M`
* Futures Capital Netflows: 5m=`-121.76K` | 15m=`+78.23K` | 1h=`-259.18K` | 24h=`-22.00M`
- **Institutional Crypto ETF Capital Flows (1_Crypto_ETF_Flows.parquet)**:
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)

- **High-Impact Macro Economic Events (19_Calendar.parquet)**:
  * `Sun Oct 25` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Mon Oct 26` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
  * `Tue Oct 27` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
  * `Tue Oct 27` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
  * `Tue Oct 27` [EUR - Low Impact]: M3 Money Supply y/y (Forecast: 3.5%, Previous: 3.5%)
  * `Tue Oct 27` [EUR - Low Impact]: Private Loans y/y (Forecast: 3.1%, Previous: 3.1%)
  * `Tue Oct 27` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)

- **Breaking Institutional News & Market Intelligence (19_News.parquet)**:
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Interbank Foreign Exchange Mechanics**:
  * London/NY Overlap Window (13:00 - 16:00 UTC): Prime Institutional Liquidity.
  * Rollover Spread Expansion Gate: Execution strictly prohibited between 21:15 UTC and 22:30 UTC.
- **Global Commodity & Index Pricing Drivers**:
  * Precious Metals (XAU/XAG): Real Yield Sensitivity & Geopolitical Safe-Haven Premium.
  * Equity Indices (US30, SP500, NAS100): E-mini Auction VWAP Dispersion & Institutional Gamma Profiles.

---

## 10. Quantitative Trade Formulation & Autonomous Broker Execution Card
*(Sources: Canonical Quant Rules, STANDARDIZED_TRADING_DECISION_CHAIN.md, 10 lethal traps)*
- **Candidate Long Setup (Model 1 / Model 2 VAL Sweep Fade)**:
  * Order Type: `BUY_LIMIT`
  * Execution Entry: `10.54` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.31` (Risk Distance: `0.2328` pts)
  * +2.5R Take Profit: `11.12`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.35` (Risk Distance: `0.2328` pts)
  * +2.5R Take Profit: `10.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.07`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
