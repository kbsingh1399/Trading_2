# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 15:42:18 IST` (`2026-10-30 10:12:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.96` | **Live Ask Quote**: `11.05` | **Mid Price**: `11.01`
- **Spread Points**: `89.00` | **Spread BPS**: `80.87 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.76` | VWAP Z-Score: `+0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0803` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.92` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.55` | Lower -3.00σ Band: `9.96`
  * Upper +2.51σ Band: `11.42` | Lower -2.51σ Band: `10.09`
  * Upper +2.01σ Band: `11.29` | Lower -2.01σ Band: `10.22`
  * Upper +2.00σ Band: `11.29` | Lower -2.00σ Band: `10.22`
  * Upper +1.28σ Band: `11.10` | Lower -1.28σ Band: `10.42`
  * Upper +1.00σ Band: `11.02` | Lower -1.00σ Band: `10.49`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.97` | EMA-20=`10.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.98` (Slope: `+0.0000`) | EMA-100=`11.11`
  * Institutional Anchors: EMA-144=`11.19` | EMA-200=`11.26` (Slope: `-0.3224`) | EMA-233=`11.28`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-1.02%`)
  * Point of Control (POC) = `10.96` (Distance: `+0.42%`)
  * Value Area Low (VAL) = `10.55` (Distance: `+4.32%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.78` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.89`
  * New York Session (13:00-21:00 UTC): High=`10.99` | Low=`10.95`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.96` - `11.05`
  * Optimal Trade Entry (OTE 0.705): `11.03`
  * Structural Invalidation Anchor (0.786): `11.09`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.02` | `11.03` | `10.99` | `11.02` | `27,430` | 301,897.80 USD | -35,490.92 USD | `-11.76%` | -12,655,039.40 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.02` | `11.04` | `11.01` | `11.03` | `32,418` | 357,499.40 USD | 35,013.47 USD | `+9.79%` | -12,620,025.93 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.03` | `11.05` | `11.02` | `11.04` | `38,219` | 421,630.80 USD | -110,042.82 USD | `-26.10%` | -12,730,068.75 USD | `-0.88` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.00` | `11.03` | `10.95` | `11.02` | `111,633` | 1,226,717.62 USD | -73,723.30 USD | `-6.01%` | -12,474,533.43 USD | `-0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.02` | `11.05` | `10.99` | `11.04` | `98,545` | 1,086,301.02 USD | -114,119.49 USD | `-10.51%` | -12,588,652.92 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.04` | `11.04` | `11.00` | `11.02` | `68,017` | 749,538.78 USD | 26,750.20 USD | `+3.57%` | -12,561,902.72 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.04` | `11.11` | `10.99` | `11.01` | `546,831` | 6,037,228.26 USD | -347,696.97 USD | `-5.76%` | -12,182,060.85 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.01` | `11.05` | `10.95` | `11.04` | `483,549` | 5,317,760.14 USD | -566,832.14 USD | `-10.66%` | -12,748,892.99 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.04` | `11.00` | `11.02` | `68,017` | 749,538.78 USD | 26,750.20 USD | `+3.57%` | -12,722,142.79 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.04` | `1,029,925` | 11,349,962.59 USD | -910,682.68 USD | `-8.02%` | -12,785,787.97 USD | `+0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.02` | `1,098,397` | 12,104,527.18 USD | -887,778.91 USD | `-7.33%` | -12,762,884.19 USD | `+0.22` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.01`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `421` | `0xecb6...2b00` | `SHORT` | 5,226,041.55 USD | `473,931,400.00` | `10.66` | `11.02` | `74.02` | -174,571.53 USD | `-3.34%` | `10X Cross` |
| `503` | `0x73ce...8ce9` | `LONG` | 4,412,527.96 USD | `400,011,600.00` | `12.05` | `11.02` | `7.82` | -407,225.74 USD | `-9.23%` | `5X Cross` |
| `842` | `0xb83d...6e36` | `SHORT` | 2,668,677.35 USD | `242,013,000.00` | `12.93` | `11.02` | `474.82` | 461,216.84 USD | `+17.28%` | `3X Cross` |
| `886` | `0x458d...ab3b` | `LONG` | 2,504,856.93 USD | `227,156,700.00` | `13.13` | `11.02` | `9.34` | -477,373.47 USD | `-19.06%` | `3X Isolated` |
| `971` | `0xdd53...2b13` | `SHORT` | 2,276,305.53 USD | `206,475,300.00` | `11.92` | `11.02` | `297.54` | 184,917.40 USD | `+8.12%` | `3X Cross` |
| `995` | `0x3dc9...54b0` | `SHORT` | 2,206,400.00 USD | `200,000,000.00` | `7.56` | `11.02` | `96.00` | -695,241.58 USD | `-31.51%` | `10X Cross` |
| `1011` | `0x45d2...4029` | `SHORT` | 2,155,387.50 USD | `195,500,000.00` | `11.54` | `11.02` | `222.44` | 101,095.93 USD | `+4.69%` | `10X Cross` |
| `1184` | `0x6540...f7b7` | `LONG` | 1,845,562.67 USD | `167,404,200.00` | `12.40` | `11.02` | `6.70` | -230,243.44 USD | `-12.48%` | `5X Isolated` |
| `1259` | `0xeadc...9d55` | `LONG` | 1,741,230.65 USD | `157,691,600.00` | `9.43` | `11.02` | `0.000000` | 254,575.75 USD | `+14.62%` | `10X Cross` |
| `1476` | `0x5b5d...c060` | `SHORT` | 1,455,065.07 USD | `131,775,500.00` | `13.61` | `11.02` | `1106.25` | 338,192.90 USD | `+23.24%` | `3X Cross` |
| `1658` | `0xf6f3...47f8` | `SHORT` | 1,268,615.52 USD | `115,024,600.00` | `11.42` | `11.02` | `18.32` | 44,714.67 USD | `+3.52%` | `5X Cross` |
| `1840` | `0xfe7e...11b4` | `LONG` | 1,115,393.98 USD | `101,142,000.00` | `14.47` | `11.02` | `5.33` | -347,719.17 USD | `-31.17%` | `5X Isolated` |
| `1880` | `0x8af7...fa05` | `SHORT` | 1,087,542.41 USD | `98,661,200.00` | `14.08` | `11.02` | `202.28` | 301,640.13 USD | `+27.74%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `11.71` | 6,883.73 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.88K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 8,500.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.50K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+1.95%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.41%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.94%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.41%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.94%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.41%`)
  * 7D Horizon: Short MP=`11.21` (Vol: 486,800.00 USD, Dist: `+1.84%`) | Long MP=`10.29` (Vol: 866,700.00 USD, Dist: `--6.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 46,320.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 222.31 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 29,610.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 3,480.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,300.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,430.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,420.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 250.25 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,810.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 15,960.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 24,410.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 411.94 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 1,050.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 57,150.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 2,400.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 235,200.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 83,570.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 5,440.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 6,620.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 543,120.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 1,780.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 9,670.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 52,720.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 276.57 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 6,010.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,260.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 13,590.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 69,580.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 15,990.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 3,270.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 20,540.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 79,550.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 710,860.00 USD | 9,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 10,740.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 7,160.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 55,430.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 5,120.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 173,010.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 38,790.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 15,080.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,610.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 66,130.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 90,360.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 32,110.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 520,270.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,960.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 14,810.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 23,240.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 57,860.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 473,800.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 87,420.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.15` | 13,180,000.00 USD | 13,180,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.17` | 13,110,000.00 USD | 13,110,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.19` | 13,060,000.00 USD | 13,060,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.21` | 13,000,000.00 USD | 13,000,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.23` | 13,000,000.00 USD | 13,000,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.25` | 12,960,000.00 USD | 12,960,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 19,930.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.27` | 12,930,000.00 USD | 12,930,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.29` | 12,900,000.00 USD | 12,900,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.31` | 12,860,000.00 USD | 12,860,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.33` | 12,810,000.00 USD | 12,810,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.35` | 12,800,000.00 USD | 12,800,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.37` | 12,750,000.00 USD | 12,750,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.39` | 12,740,000.00 USD | 12,740,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.41` | 12,700,000.00 USD | 12,700,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.43` | 12,680,000.00 USD | 12,680,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.45` | 12,640,000.00 USD | 12,640,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 55,970.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.47` | 12,490,000.00 USD | 12,490,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.49` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.51` | 12,480,000.00 USD | 12,480,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 12,420,000.00 USD | 12,420,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 102,020.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.57` | 12,370,000.00 USD | 12,370,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 12,280,000.00 USD | 12,280,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 12,080,000.00 USD | 12,080,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 12,070,000.00 USD | 12,070,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 204,090.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.69` | 12,050,000.00 USD | 12,050,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 11,990,000.00 USD | 11,990,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 63,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 11,910,000.00 USD | 11,910,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 11,860,000.00 USD | 11,860,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 11,760,000.00 USD | 11,760,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 11,700,000.00 USD | 11,700,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 30,620.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 8,600,000.00 USD | 8,600,000.00 USD | 29,590.00 USD | 11,010.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.87` | 11,640,000.00 USD | 11,640,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 8,550,000.00 USD | 8,550,000.00 USD | 6,450.00 USD | 14,150.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 11,630,000.00 USD | 11,630,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 8,520,000.00 USD | 8,520,000.00 USD | 37,810.00 USD | 29,660.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 8,450,000.00 USD | 8,450,000.00 USD | 23,540.00 USD | 19,950.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 8,400,000.00 USD | 8,400,000.00 USD | 1,820.00 USD | 3,260.00 USD | 101.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 11,500,000.00 USD | 11,500,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 421,600.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 8,400,000.00 USD | 8,400,000.00 USD | 67,680.00 USD | 14,110.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 11,440,000.00 USD | 11,440,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 8,290,000.00 USD | 8,290,000.00 USD | 31,010.00 USD | 6,830.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 11,440,000.00 USD | 11,440,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,190,000.00 USD | 8,190,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,120,000.00 USD | 8,120,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.03` | 11,360,000.00 USD | 11,360,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,070,000.00 USD | 8,070,000.00 USD | 18,000.00 USD | 1,900.00 USD | 264.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 781,760.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,050,000.00 USD | 8,050,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 7,980,000.00 USD | 7,980,000.00 USD | 167,250.00 USD | 701.42 USD | 76,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 11,140,000.00 USD | 11,140,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 7,730,000.00 USD | 7,730,000.00 USD | 7,570.00 USD | 42,810.00 USD | 288.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 10,920,000.00 USD | 10,920,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 7,680,000.00 USD | 7,680,000.00 USD | 1,150.00 USD | 20,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 10,860,000.00 USD | 10,860,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 7,660,000.00 USD | 7,660,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 10,740,000.00 USD | 10,740,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 79,580.00 USD | 287,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 7,600,000.00 USD | 7,600,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 10,500,000.00 USD | 10,500,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 7,480,000.00 USD | 7,480,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 10,390,000.00 USD | 10,390,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,200,000.00 USD | 7,200,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 10,140,000.00 USD | 10,140,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 6,720,000.00 USD | 6,720,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 9,790,000.00 USD | 9,790,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 6,320,000.00 USD | 6,320,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 9,060,000.00 USD | 9,060,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 32,460.00 USD | 208,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,130,000.00 USD | 6,130,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 8,800,000.00 USD | 8,800,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 5,960,000.00 USD | 5,960,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 8,380,000.00 USD | 8,380,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 5,620,000.00 USD | 5,620,000.00 USD | 166,230.00 USD | 20,900.00 USD | 39,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 7,680,000.00 USD | 7,680,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 5,390,000.00 USD | 5,390,000.00 USD | 11,920.00 USD | 1,310.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 7,640,000.00 USD | 7,640,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 5,300,000.00 USD | 5,300,000.00 USD | 68,350.00 USD | 9,100.00 USD | 86,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 7,480,000.00 USD | 7,480,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,720.00 USD | 175,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,140,000.00 USD | 5,140,000.00 USD | 5,630.00 USD | 3,580.00 USD | 39.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 7,070,000.00 USD | 7,070,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,130,000.00 USD | 5,130,000.00 USD | 41,250.00 USD | 45,790.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 7,060,000.00 USD | 7,060,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,040,000.00 USD | 5,040,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 7,060,000.00 USD | 7,060,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 4,850,000.00 USD | 4,850,000.00 USD | 247,240.00 USD | 0.00 USD | 98.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 6,610,000.00 USD | 6,610,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 4,600,000.00 USD | 4,600,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 6,370,000.00 USD | 6,370,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 26,900.00 USD | 34,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,070,000.00 USD | 4,070,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 5,490,000.00 USD | 5,490,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 3,740,000.00 USD | 3,740,000.00 USD | 50,950.00 USD | 2,200.00 USD | 55,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 5,090,000.00 USD | 5,090,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 3,630,000.00 USD | 3,630,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 4,950,000.00 USD | 4,950,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 3,560,000.00 USD | 3,560,000.00 USD | 446.87 USD | 12,710.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 4,900,000.00 USD | 4,900,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 3,510,000.00 USD | 3,510,000.00 USD | 15,130.00 USD | 72,580.00 USD | 153,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 4,860,000.00 USD | 4,860,000.00 USD | 121,680.00 USD | 125,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 8,100.00 USD | 8,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,260,000.00 USD | 3,260,000.00 USD | 100,350.00 USD | 31,770.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 4,610,000.00 USD | 4,610,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,110,000.00 USD | 3,110,000.00 USD | 54,810.00 USD | 29,840.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,000,000.00 USD | 3,000,000.00 USD | 9,410.00 USD | 20,470.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 4,590,000.00 USD | 4,590,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 2,970,000.00 USD | 2,970,000.00 USD | 21,530.00 USD | 4,920.00 USD | 126,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 4,580,000.00 USD | 4,580,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 2,820,000.00 USD | 2,820,000.00 USD | 85,770.00 USD | 3,750.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 4,520,000.00 USD | 4,520,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 2,680,000.00 USD | 2,680,000.00 USD | 53,760.00 USD | 7,540.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,590,000.00 USD | 2,590,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,450,000.00 USD | 2,450,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 4,480,000.00 USD | 4,480,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,430,000.00 USD | 2,430,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,210,000.00 USD | 2,210,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 3,960,000.00 USD | 3,960,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,100,000.00 USD | 2,100,000.00 USD | 35,390.00 USD | 78,300.00 USD | 68,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 3,830,000.00 USD | 3,830,000.00 USD | 537,300.00 USD | 134,970.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 1,920,000.00 USD | 1,920,000.00 USD | 198,180.00 USD | 150,540.00 USD | 50,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 3,050,000.00 USD | 3,050,000.00 USD | 79,540.00 USD | 64,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,520,000.00 USD | 1,520,000.00 USD | 66,060.00 USD | 23,280.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,420,000.00 USD | 1,420,000.00 USD | 106,890.00 USD | 34,220.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,270,000.00 USD | 1,270,000.00 USD | 351,160.00 USD | 5,480.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 2,360,000.00 USD | 2,360,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.86` | 901,130.00 USD | 901,130.00 USD | 155,010.00 USD | 23,860.00 USD | 189,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 2,060,000.00 USD | 2,060,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 532,870.00 USD | 532,870.00 USD | 49,200.00 USD | 9,550.00 USD | 59,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 1,200,000.00 USD | 1,200,000.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 414,670.00 USD | 414,670.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 781,740.00 USD | 781,740.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 216,370.00 USD | 216,370.00 USD | 103,270.00 USD | 19,240.00 USD | 86.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 523,260.00 USD | 523,260.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 93,780.00 USD | 93,780.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 306,640.00 USD | 306,640.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.96` | 87,860.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 248,900.00 USD | 248,900.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 236,580.00 USD | 236,580.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 103.72 USD | 103.72 USD | 0.00 USD | 0.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 11,680.00 USD | 11,680.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 267,980.00 USD | 267,980.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.04` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 2,200.00 USD | 402.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 545,190.00 USD | 545,190.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.06` | 29,580.00 USD | 29,580.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 547,510.00 USD | 547,510.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.08` | 331,720.00 USD | 331,720.00 USD | 0.00 USD | 0.00 USD | 302,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 803,520.00 USD | 803,520.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 339,460.00 USD | 339,460.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,310,000.00 USD | 1,310,000.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 484,320.00 USD | 484,320.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,800,000.00 USD | 1,800,000.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 557,370.00 USD | 557,370.00 USD | 4,910.00 USD | 0.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,090,000.00 USD | 2,090,000.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 736,750.00 USD | 736,750.00 USD | 127,020.00 USD | 2,100.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 909,130.00 USD | 909,130.00 USD | 71,610.00 USD | 14,380.00 USD | 86,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 1,160,000.00 USD | 1,160,000.00 USD | 76,580.00 USD | 85,530.00 USD | 91,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,940,000.00 USD | 2,940,000.00 USD | 554,520.00 USD | 130,380.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,670,000.00 USD | 1,670,000.00 USD | 328,370.00 USD | 63,100.00 USD | 117,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 3,360,000.00 USD | 3,360,000.00 USD | 288,220.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 2,040,000.00 USD | 2,040,000.00 USD | 163,340.00 USD | 54,170.00 USD | 155,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,840,000.00 USD | 3,840,000.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 2,310,000.00 USD | 2,310,000.00 USD | 149,280.00 USD | 44,890.00 USD | 71,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,490,000.00 USD | 4,490,000.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 2,950,000.00 USD | 2,950,000.00 USD | 336,790.00 USD | 59,260.00 USD | 243,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,810,000.00 USD | 4,810,000.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,370,000.00 USD | 3,370,000.00 USD | 213,610.00 USD | 75,000.00 USD | 129,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 5,120,000.00 USD | 5,120,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 3,750,000.00 USD | 3,750,000.00 USD | 168,840.00 USD | 74,250.00 USD | 142,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 5,510,000.00 USD | 5,510,000.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,370,000.00 USD | 4,370,000.00 USD | 390,100.00 USD | 118,470.00 USD | 107,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,800,000.00 USD | 5,800,000.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,660,000.00 USD | 4,660,000.00 USD | 138,710.00 USD | 95,240.00 USD | 56,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 6,140,000.00 USD | 6,140,000.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 4,890,000.00 USD | 4,890,000.00 USD | 118,230.00 USD | 85,980.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 5,070,000.00 USD | 5,070,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,390,000.00 USD | 5,390,000.00 USD | 126,960.00 USD | 83,600.00 USD | 113,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 6,740,000.00 USD | 6,740,000.00 USD | 265,450.00 USD | 117,170.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,620,000.00 USD | 5,620,000.00 USD | 88,630.00 USD | 48,240.00 USD | 96,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 7,070,000.00 USD | 7,070,000.00 USD | 227,420.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 5,840,000.00 USD | 5,840,000.00 USD | 86,190.00 USD | 75,110.00 USD | 50,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 7,160,000.00 USD | 7,160,000.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 5,890,000.00 USD | 5,890,000.00 USD | 24,020.00 USD | 31,070.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 7,310,000.00 USD | 7,310,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,040,000.00 USD | 6,040,000.00 USD | 52,620.00 USD | 34,750.00 USD | 53,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 7,430,000.00 USD | 7,430,000.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,200,000.00 USD | 6,200,000.00 USD | 103,860.00 USD | 16,980.00 USD | 40,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 7,550,000.00 USD | 7,550,000.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,400,000.00 USD | 6,400,000.00 USD | 86,680.00 USD | 20,290.00 USD | 101,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 7,730,000.00 USD | 7,730,000.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,600,000.00 USD | 6,600,000.00 USD | 128,820.00 USD | 20,640.00 USD | 47,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,680,000.00 USD | 6,680,000.00 USD | 58,760.00 USD | 2,950.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 6,820,000.00 USD | 6,820,000.00 USD | 59,560.00 USD | 14,330.00 USD | 67,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 7,850,000.00 USD | 7,850,000.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 6,920,000.00 USD | 6,920,000.00 USD | 44,510.00 USD | 512.95 USD | 48,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 7,950,000.00 USD | 7,950,000.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 6,960,000.00 USD | 6,960,000.00 USD | 5,220.00 USD | 7,410.00 USD | 31,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,000,000.00 USD | 7,000,000.00 USD | 228.94 USD | 12,290.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,190,000.00 USD | 7,190,000.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 8,190,000.00 USD | 8,190,000.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,210,000.00 USD | 7,210,000.00 USD | 239.66 USD | 4,760.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 8,380,000.00 USD | 8,380,000.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,440,000.00 USD | 7,440,000.00 USD | 112,130.00 USD | 18,090.00 USD | 98,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 8,570,000.00 USD | 8,570,000.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,620,000.00 USD | 7,620,000.00 USD | 76,690.00 USD | 30,300.00 USD | 73,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 8,620,000.00 USD | 8,620,000.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,690,000.00 USD | 7,690,000.00 USD | 26,330.00 USD | 14,880.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 8,770,000.00 USD | 8,770,000.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 7,780,000.00 USD | 7,780,000.00 USD | 27,690.00 USD | 20,510.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 8,850,000.00 USD | 8,850,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 7,790,000.00 USD | 7,790,000.00 USD | 1,190.00 USD | 18,000.00 USD | 531.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 9,010,000.00 USD | 9,010,000.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 7,840,000.00 USD | 7,840,000.00 USD | 11,880.00 USD | 53.10 USD | 36,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 9,140,000.00 USD | 9,140,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 7,940,000.00 USD | 7,940,000.00 USD | 43,880.00 USD | 11,870.00 USD | 45,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 9,390,000.00 USD | 9,390,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 1,420.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,020,000.00 USD | 8,020,000.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 9,420,000.00 USD | 9,420,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,130,000.00 USD | 8,130,000.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 9,500,000.00 USD | 9,500,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,210,000.00 USD | 8,210,000.00 USD | 43,700.00 USD | 8,690.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 9,660,000.00 USD | 9,660,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,490,000.00 USD | 8,490,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 9,730,000.00 USD | 9,730,000.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,590,000.00 USD | 8,590,000.00 USD | 48,030.00 USD | 15,260.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 9,980,000.00 USD | 9,980,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 5,650.00 USD | 7,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,740,000.00 USD | 8,740,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 10,620,000.00 USD | 10,620,000.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 8,900,000.00 USD | 8,900,000.00 USD | 59,940.00 USD | 29,060.00 USD | 68,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 11,090,000.00 USD | 11,090,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,090,000.00 USD | 9,090,000.00 USD | 119,890.00 USD | 23,880.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 11,550,000.00 USD | 11,550,000.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,150,000.00 USD | 9,150,000.00 USD | 13,680.00 USD | 11,370.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 12,260,000.00 USD | 12,260,000.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,330,000.00 USD | 9,330,000.00 USD | 90,410.00 USD | 39,490.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 12,900,000.00 USD | 12,900,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,520,000.00 USD | 9,520,000.00 USD | 76,750.00 USD | 43,270.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 13,480,000.00 USD | 13,480,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,660,000.00 USD | 9,660,000.00 USD | 43,090.00 USD | 40,740.00 USD | 52,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 13,830,000.00 USD | 13,830,000.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 9,760,000.00 USD | 9,760,000.00 USD | 49,200.00 USD | 22,590.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 14,120,000.00 USD | 14,120,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 9,980,000.00 USD | 9,980,000.00 USD | 116,870.00 USD | 54,460.00 USD | 50,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 14,390,000.00 USD | 14,390,000.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,150,000.00 USD | 10,150,000.00 USD | 75,780.00 USD | 35,660.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 14,900,000.00 USD | 14,900,000.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,380,000.00 USD | 10,380,000.00 USD | 124,550.00 USD | 34,710.00 USD | 67,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 15,060,000.00 USD | 15,060,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,580,000.00 USD | 10,580,000.00 USD | 112,670.00 USD | 46,930.00 USD | 47,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 15,380,000.00 USD | 15,380,000.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,740,000.00 USD | 10,740,000.00 USD | 71,000.00 USD | 43,870.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 15,740,000.00 USD | 15,740,000.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 10,800,000.00 USD | 10,800,000.00 USD | 10,400.00 USD | 18,360.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 15,920,000.00 USD | 15,920,000.00 USD | 140,270.00 USD | 27,350.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 10,820,000.00 USD | 10,820,000.00 USD | 4,800.00 USD | 15,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 16,060,000.00 USD | 16,060,000.00 USD | 47,780.00 USD | 46,250.00 USD | 46,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.27` | 16,230,000.00 USD | 16,230,000.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 16,540,000.00 USD | 16,540,000.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 16,680,000.00 USD | 16,680,000.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,720,000.00 USD | 16,720,000.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,770,000.00 USD | 16,770,000.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 1,940.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,840,000.00 USD | 16,840,000.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 17,000,000.00 USD | 17,000,000.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 17,020,000.00 USD | 17,020,000.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 12,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,070.00 USD | 13,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 779.24 USD | 14,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.85` | 535.85 USD | 15,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.25` | 1,060.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 21,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 866.89 USD | 115,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 115,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 3,860.00 USD | 119,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 4,280.00 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 149,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 149,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 150,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 150,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 150,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 323.00 USD | 150,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 152,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 230.30 USD | 152,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 31,700.00 USD | 184,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 286,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 365,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 367,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,700.00 USD | 393,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 101.79 USD | 393,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,450.00 USD | 399,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 649,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 649,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 651,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,920.00 USD | 679,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 2,130,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 63,600.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 707,060.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 75,870.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 619.67 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 39,570.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 202.08 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 222.87 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,270,000.00 USD | 0.00 USD | 1,720.00 USD | `-79.56%` | `766,500.00` |
| `Live` | `Long` | `2.35` | 12,270,000.00 USD | 0.00 USD | 50,730.00 USD | `-78.65%` | `21,585,500.00` |
| `Live` | `Long` | `2.55` | 12,220,000.00 USD | 0.00 USD | 1,030.00 USD | `-76.83%` | `402,300.00` |
| `Live` | `Long` | `2.65` | 12,220,000.00 USD | 0.00 USD | 6,130.00 USD | `-75.92%` | `2,314,300.00` |
| `Live` | `Long` | `2.75` | 12,210,000.00 USD | 0.00 USD | 28,270.00 USD | `-75.01%` | `10,281,800.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 7,490.00 USD | `-72.29%` | `2,454,900.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 1,430.00 USD | `-71.38%` | `454,900.00` |
| `Live` | `Long` | `3.25` | 12,180,000.00 USD | 0.00 USD | 445.25 USD | `-70.47%` | `137,000.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.56%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,170,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.65%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 126.73 USD | `-67.74%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.84%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,160,000.00 USD | 0.00 USD | 250.25 USD | `-65.02%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,160,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.11%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,160,000.00 USD | 0.00 USD | 950.54 USD | `-63.20%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,160,000.00 USD | 0.00 USD | 412.51 USD | `-62.29%` | `99,400.00` |
| `Live` | `Long` | `4.25` | 12,160,000.00 USD | 0.00 USD | 20,850.00 USD | `-61.38%` | `4,905,100.00` |
| `Live` | `Long` | `4.35` | 12,140,000.00 USD | 0.00 USD | 5,600.00 USD | `-60.48%` | `1,287,000.00` |
| `Live` | `Long` | `4.45` | 12,130,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.57%` | `235,700.00` |
| `Live` | `Long` | `4.55` | 12,130,000.00 USD | 0.00 USD | 7,280.00 USD | `-58.66%` | `1,599,800.00` |
| `Live` | `Long` | `4.65` | 12,120,000.00 USD | 0.00 USD | 17,600.00 USD | `-57.75%` | `3,784,500.00` |
| `Live` | `Long` | `4.75` | 12,110,000.00 USD | 0.00 USD | 366,620.00 USD | `-56.84%` | `77,183,100.00` |
| `Live` | `Long` | `4.85` | 11,740,000.00 USD | 0.00 USD | 2,070.00 USD | `-55.93%` | `426,800.00` |
| `Live` | `Long` | `4.95` | 11,740,000.00 USD | 0.00 USD | 6,080.00 USD | `-55.02%` | `1,228,100.00` |
| `Live` | `Long` | `5.05` | 11,730,000.00 USD | 0.00 USD | 217.66 USD | `-54.12%` | `43,100.00` |
| `Live` | `Long` | `5.15` | 11,730,000.00 USD | 0.00 USD | 262.13 USD | `-53.21%` | `50,900.00` |
| `Live` | `Long` | `5.25` | 11,730,000.00 USD | 0.00 USD | 5,020.00 USD | `-52.30%` | `956,800.00` |
| `Live` | `Long` | `5.35` | 11,720,000.00 USD | 0.00 USD | 543,950.00 USD | `-51.39%` | `101,672,700.00` |
| `Live` | `Long` | `5.45` | 11,180,000.00 USD | 0.00 USD | 2,600.00 USD | `-50.48%` | `477,300.00` |
| `Live` | `Long` | `5.55` | 11,180,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.57%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 35,770.00 USD | `-48.66%` | `6,330,200.00` |
| `Live` | `Long` | `5.75` | 11,130,000.00 USD | 0.00 USD | 18,750.00 USD | `-47.76%` | `3,260,900.00` |
| `Live` | `Long` | `5.85` | 11,110,000.00 USD | 0.00 USD | 6,010.00 USD | `-46.85%` | `1,026,700.00` |
| `Live` | `Long` | `5.95` | 11,110,000.00 USD | 0.00 USD | 10,260.00 USD | `-45.94%` | `1,724,100.00` |
| `Live` | `Long` | `6.05` | 11,100,000.00 USD | 0.00 USD | 13,590.00 USD | `-45.03%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 11,080,000.00 USD | 0.00 USD | 489.54 USD | `-44.12%` | `79,600.00` |
| `Live` | `Long` | `6.25` | 11,080,000.00 USD | 0.00 USD | 29,010.00 USD | `-43.21%` | `4,642,000.00` |
| `Live` | `Long` | `6.35` | 11,050,000.00 USD | 0.00 USD | 54,590.00 USD | `-42.30%` | `8,596,600.00` |
| `Live` | `Long` | `6.45` | 11,000,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.40%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 10,990,000.00 USD | 0.00 USD | 2,910.00 USD | `-40.49%` | `444,300.00` |
| `Live` | `Long` | `6.65` | 10,990,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.58%` | `169,295,200.00` |
| `Live` | `Long` | `6.75` | 9,860,000.00 USD | 0.00 USD | 24,870.00 USD | `-38.67%` | `3,684,700.00` |
| `Live` | `Long` | `6.85` | 9,840,000.00 USD | 0.00 USD | 5,060.00 USD | `-37.76%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,830,000.00 USD | 0.00 USD | 79,160.00 USD | `-36.85%` | `11,389,500.00` |
| `Live` | `Long` | `7.05` | 9,750,000.00 USD | 0.00 USD | 690,270.00 USD | `-35.94%` | `97,910,200.00` |
| `Live` | `Long` | `7.15` | 9,060,000.00 USD | 0.00 USD | 32,340.00 USD | `-35.04%` | `4,522,900.00` |
| `Live` | `Long` | `7.25` | 9,030,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.13%` | `986,900.00` |
| `Live` | `Long` | `7.35` | 9,020,000.00 USD | 0.00 USD | 20,090.00 USD | `-33.22%` | `2,734,000.00` |
| `Live` | `Long` | `7.45` | 9,000,000.00 USD | 0.00 USD | 40,720.00 USD | `-32.31%` | `5,465,700.00` |
| `Live` | `Long` | `7.55` | 8,960,000.00 USD | 0.00 USD | 173,010.00 USD | `-31.40%` | `22,914,800.00` |
| `Live` | `Long` | `7.65` | 8,790,000.00 USD | 0.00 USD | 1,830.00 USD | `-30.49%` | `239,400.00` |
| `Live` | `Long` | `7.75` | 8,790,000.00 USD | 0.00 USD | 19,300.00 USD | `-29.58%` | `2,490,300.00` |
| `Live` | `Long` | `7.85` | 8,770,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.68%` | `400,988,000.00` |
| `Live` | `Long` | `7.95` | 5,620,000.00 USD | 0.00 USD | 17,480.00 USD | `-27.77%` | `2,198,500.00` |
| `Live` | `Long` | `8.05` | 5,600,000.00 USD | 0.00 USD | 99,930.00 USD | `-26.86%` | `12,413,400.00` |
| `Live` | `Long` | `8.15` | 5,500,000.00 USD | 0.00 USD | 45,950.00 USD | `-25.95%` | `5,638,000.00` |
| `Live` | `Long` | `8.25` | 5,460,000.00 USD | 0.00 USD | 32,110.00 USD | `-25.04%` | `3,892,000.00` |
| `Live` | `Long` | `8.35` | 5,430,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.13%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,420,000.00 USD | 0.00 USD | 520,270.00 USD | `-23.22%` | `61,570,800.00` |
| `Live` | `Long` | `8.55` | 4,900,000.00 USD | 0.00 USD | 58,710.00 USD | `-22.32%` | `6,866,700.00` |
| `Live` | `Long` | `8.65` | 4,840,000.00 USD | 0.00 USD | 15,270.00 USD | `-21.41%` | `1,765,700.00` |
| `Live` | `Long` | `8.75` | 4,820,000.00 USD | 0.00 USD | 17,890.00 USD | `-20.50%` | `2,044,100.00` |
| `Live` | `Long` | `8.85` | 4,810,000.00 USD | 0.00 USD | 60,320.00 USD | `-19.59%` | `6,816,200.00` |
| `Live` | `Long` | `8.95` | 4,750,000.00 USD | 0.00 USD | 458,450.00 USD | `-18.68%` | `51,223,800.00` |
| `Live` | `Long` | `9.05` | 4,290,000.00 USD | 0.00 USD | 105,400.00 USD | `-17.77%` | `11,646,400.00` |
| `Live` | `Long` | `9.15` | 4,180,000.00 USD | 0.00 USD | 76,640.00 USD | `-16.86%` | `8,376,000.00` |
| `Live` | `Long` | `9.25` | 4,110,000.00 USD | 0.00 USD | 19,930.00 USD | `-15.95%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,090,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.05%` | `229,774,900.00` |
| `Live` | `Long` | `9.45` | 1,940,000.00 USD | 0.00 USD | 55,700.00 USD | `-14.14%` | `5,894,700.00` |
| `Live` | `Long` | `9.55` | 1,880,000.00 USD | 0.00 USD | 103,520.00 USD | `-13.23%` | `10,839,700.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 202,670.00 USD | `-12.32%` | `21,001,700.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 85,410.00 USD | `-11.41%` | `8,760,500.00` |
| `Live` | `Long` | `9.85` | 1,490,000.00 USD | 0.00 USD | 30,620.00 USD | `-10.50%` | `3,108,900.00` |
| `Live` | `Long` | `9.95` | 1,460,000.00 USD | 0.00 USD | 433,320.00 USD | `-9.59%` | `43,549,800.00` |
| `Live` | `Long` | `10.05` | 1,030,000.00 USD | 0.00 USD | 774,770.00 USD | `-8.69%` | `77,091,800.00` |
| `Live` | `Long` | `10.15` | 251,760.00 USD | 0.00 USD | 69,470.00 USD | `-7.78%` | `6,844,000.00` |
| `Live` | `Long` | `10.25` | 182,290.00 USD | 0.00 USD | 32,460.00 USD | `-6.87%` | `3,166,900.00` |
| `Live` | `Long` | `10.35` | 149,830.00 USD | 0.00 USD | 140,250.00 USD | `-5.96%` | `13,550,500.00` |
| `Live` | `Long` | `10.45` | 9,580.00 USD | 0.00 USD | 5,590.00 USD | `-5.05%` | `534,800.00` |
| `Live` | `Long` | `10.55` | 3,990.00 USD | 0.00 USD | 3,990.00 USD | `-4.14%` | `378,500.00` |
| `Live` | `Short` | `10.85` | 1,380.00 USD | 1,380.00 USD | 0.00 USD | `-1.42%` | `127,500.00` |
| `Live` | `Short` | `10.95` | 3,560.00 USD | 2,180.00 USD | 0.00 USD | `-0.51%` | `199,100.00` |
| `Live` | `Short` | `11.25` | 5,410.00 USD | 1,850.00 USD | 0.00 USD | `+2.22%` | `164,100.00` |
| `Live` | `Short` | `11.45` | 5,660.00 USD | 249.61 USD | 0.00 USD | `+4.03%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 9,450.00 USD | 3,800.00 USD | 0.00 USD | `+4.94%` | `328,600.00` |
| `Live` | `Short` | `11.65` | 14,680.00 USD | 5,230.00 USD | 0.00 USD | `+5.85%` | `448,800.00` |
| `Live` | `Short` | `11.85` | 14,850.00 USD | 169.46 USD | 0.00 USD | `+7.67%` | `14,300.00` |
| `Live` | `Short` | `11.95` | 15,140.00 USD | 283.21 USD | 0.00 USD | `+8.58%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 16,570.00 USD | 1,430.00 USD | 0.00 USD | `+11.30%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 17,300.00 USD | 736.06 USD | 0.00 USD | `+12.21%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 19,280.00 USD | 1,980.00 USD | 0.00 USD | `+13.12%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 26,470.00 USD | 7,190.00 USD | 0.00 USD | `+14.03%` | `572,900.00` |
| `Live` | `Short` | `12.65` | 26,900.00 USD | 435.16 USD | 0.00 USD | `+14.94%` | `34,400.00` |
| `Live` | `Short` | `12.95` | 27,440.00 USD | 540.01 USD | 0.00 USD | `+17.66%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 32,870.00 USD | 5,430.00 USD | 0.00 USD | `+22.21%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 125,770.00 USD | 92,890.00 USD | 0.00 USD | `+23.11%` | `6,855,700.00` |
| `Live` | `Short` | `13.95` | 126,530.00 USD | 758.88 USD | 0.00 USD | `+26.75%` | `54,400.00` |
| `Live` | `Short` | `14.05` | 127,130.00 USD | 601.34 USD | 0.00 USD | `+27.66%` | `42,800.00` |
| `Live` | `Short` | `14.25` | 127,670.00 USD | 544.35 USD | 0.00 USD | `+29.47%` | `38,200.00` |
| `Live` | `Short` | `14.35` | 131,540.00 USD | 3,860.00 USD | 0.00 USD | `+30.38%` | `269,100.00` |
| `Live` | `Short` | `14.65` | 135,880.00 USD | 4,340.00 USD | 0.00 USD | `+33.11%` | `296,400.00` |
| `Live` | `Short` | `14.95` | 161,210.00 USD | 25,330.00 USD | 0.00 USD | `+35.83%` | `1,694,600.00` |
| `Live` | `Short` | `15.55` | 161,790.00 USD | 578.46 USD | 0.00 USD | `+41.29%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 162,060.00 USD | 271.04 USD | 0.00 USD | `+44.01%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 162,200.00 USD | 138.76 USD | 0.00 USD | `+44.92%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 162,520.00 USD | 323.00 USD | 0.00 USD | `+46.74%` | `20,000.00` |
| `Live` | `Short` | `16.25` | 162,750.00 USD | 227.50 USD | 0.00 USD | `+47.65%` | `14,000.00` |
| `Live` | `Short` | `16.35` | 164,150.00 USD | 1,390.00 USD | 0.00 USD | `+48.56%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 195,850.00 USD | 31,700.00 USD | 0.00 USD | `+50.37%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 297,760.00 USD | 101,910.00 USD | 0.00 USD | `+52.19%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 377,530.00 USD | 79,770.00 USD | 0.00 USD | `+54.01%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 378,900.00 USD | 1,370.00 USD | 0.00 USD | `+55.82%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 405,600.00 USD | 26,700.00 USD | 0.00 USD | `+57.64%` | `1,539,000.00` |
| `Live` | `Short` | `17.65` | 411,150.00 USD | 5,560.00 USD | 0.00 USD | `+60.37%` | `314,800.00` |
| `Live` | `Short` | `17.85` | 411,400.00 USD | 249.90 USD | 0.00 USD | `+62.18%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 662,480.00 USD | 251,080.00 USD | 0.00 USD | `+63.09%` | `13,987,600.00` |
| `Live` | `Short` | `18.05` | 664,450.00 USD | 1,970.00 USD | 0.00 USD | `+64.00%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 692,250.00 USD | 27,790.00 USD | 0.00 USD | `+65.82%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 2,820,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+67.64%` | `115,242,000.00` |
| `Live` | `Short` | `18.55` | 2,820,000.00 USD | 185.50 USD | 0.00 USD | `+68.54%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,820,000.00 USD | 186.50 USD | 0.00 USD | `+69.45%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 3,670,000.00 USD | 850,790.00 USD | 0.00 USD | `+71.27%` | `45,134,800.00` |
| `Live` | `Short` | `19.55` | 3,670,000.00 USD | 1,090.00 USD | 0.00 USD | `+77.63%` | `55,900.00` |
| `Live` | `Short` | `19.65` | 3,710,000.00 USD | 38,790.00 USD | 0.00 USD | `+78.54%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,710,000.00 USD | 359.45 USD | 0.00 USD | `+79.45%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,710,000.00 USD | 291.27 USD | 0.00 USD | `+81.26%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,710,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.08%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,710,000.00 USD | 1,770.00 USD | 0.00 USD | `+85.81%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+86.72%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,720,000.00 USD | 114.68 USD | 0.00 USD | `+89.44%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,720,000.00 USD | 202.08 USD | 0.00 USD | `+91.26%` | `9,600.00` |
| `Live` | `Short` | `21.35` | 3,720,000.00 USD | 217.77 USD | 0.00 USD | `+93.99%` | `10,200.00` |
| `Live` | `Short` | `21.75` | 3,790,000.00 USD | 65,060.00 USD | 0.00 USD | `+97.62%` | `2,991,400.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 401,190.00 USD | 0.00 USD | 182.03 USD | `-77.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 401,010.00 USD | 0.00 USD | 221.45 USD | `-74.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 400,790.00 USD | 0.00 USD | 234.23 USD | `-73.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 400,560.00 USD | 0.00 USD | 209.48 USD | `-71.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 400,350.00 USD | 0.00 USD | 236.33 USD | `-68.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 400,110.00 USD | 0.00 USD | 431.68 USD | `-67.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 399,680.00 USD | 0.00 USD | 290.29 USD | `-58.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 399,390.00 USD | 0.00 USD | 120.22 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 399,270.00 USD | 0.00 USD | 3,790.00 USD | `-48.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 395,470.00 USD | 0.00 USD | 251.68 USD | `-45.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 395,220.00 USD | 0.00 USD | 749.94 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 394,470.00 USD | 0.00 USD | 772.71 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 393,700.00 USD | 0.00 USD | 3,760.00 USD | `-40.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 389,940.00 USD | 0.00 USD | 133.00 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 389,800.00 USD | 0.00 USD | 1,320.00 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 388,490.00 USD | 0.00 USD | 3,770.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 384,720.00 USD | 0.00 USD | 2,070.00 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 382,650.00 USD | 0.00 USD | 3,740.00 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 378,900.00 USD | 0.00 USD | 1,050.00 USD | `-31.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 377,850.00 USD | 0.00 USD | 120.90 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 377,730.00 USD | 0.00 USD | 146.80 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 377,580.00 USD | 0.00 USD | 124.02 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 377,460.00 USD | 0.00 USD | 5,000.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 372,460.00 USD | 0.00 USD | 393.64 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 372,060.00 USD | 0.00 USD | 10,560.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 361,500.00 USD | 0.00 USD | 57,330.00 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 304,170.00 USD | 0.00 USD | 1,480.00 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 302,690.00 USD | 0.00 USD | 52,990.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 249,700.00 USD | 0.00 USD | 186.84 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 249,520.00 USD | 0.00 USD | 742.88 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 248,780.00 USD | 0.00 USD | 902.70 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 247,870.00 USD | 0.00 USD | 1,570.00 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 246,300.00 USD | 0.00 USD | 3,440.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 242,860.00 USD | 0.00 USD | 194.90 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 242,660.00 USD | 0.00 USD | 1,360.00 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 241,310.00 USD | 0.00 USD | 9,010.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 232,300.00 USD | 0.00 USD | 518.80 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 231,780.00 USD | 0.00 USD | 19,590.00 USD | `-13.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 212,190.00 USD | 0.00 USD | 504.70 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 211,680.00 USD | 0.00 USD | 3,070.00 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 208,610.00 USD | 0.00 USD | 24,100.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 184,510.00 USD | 0.00 USD | 3,450.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 181,070.00 USD | 0.00 USD | 47,890.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 133,180.00 USD | 0.00 USD | 5,650.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 127,520.00 USD | 0.00 USD | 30,030.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 97,490.00 USD | 0.00 USD | 3,480.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 94,010.00 USD | 0.00 USD | 18,670.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 75,340.00 USD | 0.00 USD | 23,690.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 51,660.00 USD | 0.00 USD | 5,170.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 46,490.00 USD | 0.00 USD | 28,310.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 18,180.00 USD | 0.00 USD | 15,000.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 3,180.00 USD | 0.00 USD | 3,180.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 5,030.00 USD | 5,030.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 10,580.00 USD | 5,550.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 37,630.00 USD | 27,050.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 54,340.00 USD | 16,710.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 58,540.00 USD | 4,190.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 84,410.00 USD | 25,870.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 87,250.00 USD | 2,840.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 88,880.00 USD | 1,630.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 96,010.00 USD | 7,130.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 100,300.00 USD | 4,300.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 130,580.00 USD | 30,280.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 132,510.00 USD | 1,930.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 225,800.00 USD | 93,280.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 226,390.00 USD | 597.74 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 231,050.00 USD | 4,650.00 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 233,540.00 USD | 2,500.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 239,720.00 USD | 6,180.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 240,400.00 USD | 679.57 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 260,770.00 USD | 20,360.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 261,220.00 USD | 451.95 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 279,420.00 USD | 18,200.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 280,340.00 USD | 919.19 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 281,660.00 USD | 1,320.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 289,440.00 USD | 7,790.00 USD | 0.00 USD | `+21.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 291,980.00 USD | 2,540.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 293,450.00 USD | 1,470.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 294,400.00 USD | 954.14 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 313,950.00 USD | 19,550.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 319,590.00 USD | 5,640.00 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 319,860.00 USD | 266.44 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 336,120.00 USD | 16,260.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 336,280.00 USD | 152.82 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 340,550.00 USD | 4,280.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 343,960.00 USD | 3,410.00 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 357,630.00 USD | 13,670.00 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 357,840.00 USD | 218.25 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 359,700.00 USD | 1,850.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 366,960.00 USD | 7,270.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 367,910.00 USD | 950.82 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 393,610.00 USD | 25,700.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 396,060.00 USD | 2,450.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 633,370.00 USD | 237,310.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 634,290.00 USD | 924.07 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 635,190.00 USD | 893.01 USD | 0.00 USD | `+40.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 659,930.00 USD | 24,740.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 660,170.00 USD | 237.88 USD | 0.00 USD | `+42.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 663,460.00 USD | 3,290.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 666,630.00 USD | 3,170.00 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 671,760.00 USD | 5,130.00 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 687,200.00 USD | 15,440.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 694,010.00 USD | 6,800.00 USD | 0.00 USD | `+46.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 700,510.00 USD | 6,500.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 707,050.00 USD | 6,540.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 713,630.00 USD | 6,580.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 723,560.00 USD | 9,930.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 827,540.00 USD | 103,980.00 USD | 0.00 USD | `+51.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 841,770.00 USD | 14,240.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 926,130.00 USD | 84,360.00 USD | 0.00 USD | `+53.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 927,820.00 USD | 1,700.00 USD | 0.00 USD | `+54.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 935,190.00 USD | 7,370.00 USD | 0.00 USD | `+54.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 936,900.00 USD | 1,710.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 939,210.00 USD | 2,300.00 USD | 0.00 USD | `+56.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 940,940.00 USD | 1,740.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 963,510.00 USD | 22,560.00 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 967,890.00 USD | 4,390.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 972,310.00 USD | 4,410.00 USD | 0.00 USD | `+60.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 976,740.00 USD | 4,440.00 USD | 0.00 USD | `+61.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 981,210.00 USD | 4,460.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 981,650.00 USD | 448.75 USD | 0.00 USD | `+63.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,010,000.00 USD | 30,960.00 USD | 0.00 USD | `+64.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,010,000.00 USD | 453.75 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,010,000.00 USD | 456.25 USD | 0.00 USD | `+65.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,010,000.00 USD | 458.75 USD | 0.00 USD | `+66.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,010,000.00 USD | 461.25 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,020,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,020,000.00 USD | 466.25 USD | 0.00 USD | `+69.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,020,000.00 USD | 468.75 USD | 0.00 USD | `+70.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,020,000.00 USD | 471.25 USD | 0.00 USD | `+71.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,020,000.00 USD | 473.75 USD | 0.00 USD | `+72.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,090,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,090,000.00 USD | 574.50 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,090,000.00 USD | 577.50 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,090,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,090,000.00 USD | 972.50 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,100,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,100,000.00 USD | 786.00 USD | 0.00 USD | `+78.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,100,000.00 USD | 790.00 USD | 0.00 USD | `+79.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,100,000.00 USD | 992.50 USD | 0.00 USD | `+80.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,100,000.00 USD | 997.50 USD | 0.00 USD | `+81.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,710,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+82.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,710,000.00 USD | 1,040.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,720,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,720,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,720,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,770,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,770,000.00 USD | 1,070.00 USD | 0.00 USD | `+94.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,770,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,780,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+100.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.15` | 13,180,000.00 USD | 0.00 USD | 13,180,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD |
| `7D` | `9.17` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD |
| `7D` | `9.19` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD |
| `7D` | `9.21` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD |
| `7D` | `9.23` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD |
| `7D` | `9.25` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD |
| `7D` | `9.27` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD |
| `7D` | `9.29` | 12,900,000.00 USD | 0.00 USD | 12,900,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD |
| `7D` | `9.31` | 12,860,000.00 USD | 0.00 USD | 12,860,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD |
| `7D` | `9.33` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD |
| `7D` | `9.35` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD |
| `7D` | `9.37` | 12,750,000.00 USD | 0.00 USD | 12,750,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD |
| `7D` | `9.39` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD |
| `7D` | `9.41` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD |
| `7D` | `9.43` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD |
| `7D` | `9.45` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD |
| `7D` | `9.47` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.49` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD |
| `7D` | `9.51` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `9.53` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD |
| `7D` | `9.55` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD |
| `7D` | `9.57` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,150.00 USD |
| `7D` | `9.59` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,530.00 USD |
| `7D` | `9.61` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD |
| `7D` | `9.63` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD |
| `7D` | `9.65` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD |
| `7D` | `9.69` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.73` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.75` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD |
| `7D` | `9.77` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD |
| `7D` | `9.79` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.81` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD |
| `7D` | `9.83` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD |
| `7D` | `9.85` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD |
| `1D` | `9.86` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 29,590.00 USD | 11,010.00 USD | 11,090.00 USD |
| `7D` | `9.87` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD |
| `1D` | `9.88` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 6,450.00 USD | 14,150.00 USD | 9,220.00 USD |
| `7D` | `9.89` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD |
| `1D` | `9.90` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 37,810.00 USD | 29,660.00 USD | 7,670.00 USD |
| `7D` | `9.91` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.92` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 23,540.00 USD | 19,950.00 USD | 118.68 USD |
| `7D` | `9.93` | 11,550,000.00 USD | 0.00 USD | 11,550,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD |
| `1D` | `9.94` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 1,820.00 USD | 3,260.00 USD | 101.06 USD |
| `7D` | `9.95` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD |
| `1D` | `9.96` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 67,680.00 USD | 14,110.00 USD | 23,150.00 USD |
| `7D` | `9.97` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD |
| `1D` | `9.98` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 31,010.00 USD | 6,830.00 USD | 64,850.00 USD |
| `7D` | `9.99` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD |
| `1D` | `10.00` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD |
| `7D` | `10.01` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD |
| `1D` | `10.02` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,520.00 USD |
| `7D` | `10.03` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.04` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 18,000.00 USD | 1,900.00 USD | 264.22 USD |
| `7D` | `10.05` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD |
| `1D` | `10.06` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,130.00 USD |
| `7D` | `10.07` | 11,250,000.00 USD | 0.00 USD | 11,250,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.08` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 167,250.00 USD | 701.42 USD | 76,080.00 USD |
| `7D` | `10.09` | 11,140,000.00 USD | 0.00 USD | 11,140,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.10` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 7,570.00 USD | 42,810.00 USD | 288.89 USD |
| `7D` | `10.11` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD |
| `1D` | `10.12` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 1,150.00 USD | 20,910.00 USD | 0.00 USD |
| `7D` | `10.13` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD |
| `1D` | `10.14` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,520.00 USD |
| `7D` | `10.15` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD |
| `1D` | `10.16` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,610.00 USD |
| `7D` | `10.17` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD |
| `1D` | `10.18` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,200.00 USD |
| `7D` | `10.19` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD |
| `1D` | `10.20` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,090.00 USD |
| `7D` | `10.21` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD |
| `1D` | `10.22` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,790.00 USD |
| `7D` | `10.23` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD |
| `1D` | `10.24` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,560.00 USD |
| `7D` | `10.25` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD |
| `1D` | `10.26` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,930.00 USD |
| `7D` | `10.27` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD |
| `1D` | `10.28` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,690.00 USD |
| `7D` | `10.29` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD |
| `1D` | `10.30` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 166,230.00 USD | 20,900.00 USD | 39,850.00 USD |
| `7D` | `10.31` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 11,920.00 USD | 1,310.00 USD | 71,710.00 USD |
| `7D` | `10.33` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 68,350.00 USD | 9,100.00 USD | 86,060.00 USD |
| `7D` | `10.35` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.36` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 5,630.00 USD | 3,580.00 USD | 39.63 USD |
| `7D` | `10.37` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.38` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 41,250.00 USD | 45,790.00 USD | 7,590.00 USD |
| `7D` | `10.39` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,800.00 USD |
| `7D` | `10.41` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD |
| `1D` | `10.42` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 247,240.00 USD | 0.00 USD | 98.16 USD |
| `7D` | `10.43` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD |
| `1D` | `10.44` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,440.00 USD |
| `7D` | `10.45` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,120.00 USD |
| `7D` | `10.47` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD |
| `1D` | `10.48` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 50,950.00 USD | 2,200.00 USD | 55,100.00 USD |
| `7D` | `10.49` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,170.00 USD |
| `7D` | `10.51` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD |
| `1D` | `10.52` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 446.87 USD | 12,710.00 USD | 38,150.00 USD |
| `7D` | `10.53` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD |
| `1D` | `10.54` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 15,130.00 USD | 72,580.00 USD | 153,390.00 USD |
| `7D` | `10.55` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 121,680.00 USD | 125,840.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 100,350.00 USD | 31,770.00 USD | 25,430.00 USD |
| `7D` | `10.57` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 54,810.00 USD | 29,840.00 USD | 22,000.00 USD |
| `7D` | `10.59` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD |
| `1D` | `10.60` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 9,410.00 USD | 20,470.00 USD | 1,950.00 USD |
| `7D` | `10.61` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD |
| `1D` | `10.62` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 21,530.00 USD | 4,920.00 USD | 126,180.00 USD |
| `7D` | `10.63` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD |
| `1D` | `10.64` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 85,770.00 USD | 3,750.00 USD | 44,240.00 USD |
| `7D` | `10.65` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD |
| `1D` | `10.66` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 53,760.00 USD | 7,540.00 USD | 29,670.00 USD |
| `7D` | `10.67` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD |
| `1D` | `10.68` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD |
| `7D` | `10.69` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD |
| `1D` | `10.70` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD |
| `7D` | `10.71` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.73` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.75` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD |
| `1D` | `10.76` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 35,390.00 USD | 78,300.00 USD | 68,800.00 USD |
| `7D` | `10.77` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 537,300.00 USD | 134,970.00 USD | 103,760.00 USD |
| `1D` | `10.78` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 198,180.00 USD | 150,540.00 USD | 50,860.00 USD |
| `7D` | `10.79` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 79,540.00 USD | 64,510.00 USD | 0.00 USD |
| `1D` | `10.80` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 66,060.00 USD | 23,280.00 USD | 13,640.00 USD |
| `7D` | `10.81` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD |
| `1D` | `10.82` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 106,890.00 USD | 34,220.00 USD | 3,800.00 USD |
| `7D` | `10.83` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD |
| `1D` | `10.84` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 351,160.00 USD | 5,480.00 USD | 15,930.00 USD |
| `7D` | `10.85` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD |
| `1D` | `10.86` | 901,130.00 USD | 0.00 USD | 901,130.00 USD | 155,010.00 USD | 23,860.00 USD | 189,380.00 USD |
| `7D` | `10.87` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD |
| `1D` | `10.88` | 532,870.00 USD | 0.00 USD | 532,870.00 USD | 49,200.00 USD | 9,550.00 USD | 59,460.00 USD |
| `7D` | `10.89` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD |
| `1D` | `10.90` | 414,670.00 USD | 0.00 USD | 414,670.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD |
| `7D` | `10.91` | 781,740.00 USD | 0.00 USD | 781,740.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD |
| `1D` | `10.92` | 216,370.00 USD | 0.00 USD | 216,370.00 USD | 103,270.00 USD | 19,240.00 USD | 86.22 USD |
| `7D` | `10.93` | 523,260.00 USD | 0.00 USD | 523,260.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.94` | 93,780.00 USD | 0.00 USD | 93,780.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.95` | 306,640.00 USD | 0.00 USD | 306,640.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD |
| `1D` | `10.96` | 87,860.00 USD | 0.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `10.97` | 248,900.00 USD | 0.00 USD | 248,900.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 236,580.00 USD | 0.00 USD | 236,580.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 103.72 USD | 0.00 USD | 103.72 USD | 0.00 USD | 0.00 USD | 103.72 USD |
| `1D` | `11.01` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.01` | 11,680.00 USD | 0.00 USD | 11,680.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `11.02` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.03` | 267,980.00 USD | 267,980.00 USD | 0.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD |
| `1D` | `11.04` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | 2,200.00 USD | 402.88 USD |
| `7D` | `11.05` | 545,190.00 USD | 545,190.00 USD | 0.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD |
| `1D` | `11.06` | 29,580.00 USD | 29,580.00 USD | 0.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD |
| `7D` | `11.07` | 547,510.00 USD | 547,510.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.08` | 331,720.00 USD | 331,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302,140.00 USD |
| `7D` | `11.09` | 803,520.00 USD | 803,520.00 USD | 0.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD |
| `1D` | `11.10` | 339,460.00 USD | 339,460.00 USD | 0.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.11` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD |
| `1D` | `11.12` | 484,320.00 USD | 484,320.00 USD | 0.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD |
| `7D` | `11.13` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD |
| `1D` | `11.14` | 557,370.00 USD | 557,370.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD | 68,140.00 USD |
| `7D` | `11.15` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD |
| `1D` | `11.16` | 736,750.00 USD | 736,750.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,270.00 USD |
| `7D` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD |
| `1D` | `11.18` | 909,130.00 USD | 909,130.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,390.00 USD |
| `7D` | `11.19` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD |
| `1D` | `11.20` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 76,580.00 USD | 85,530.00 USD | 91,110.00 USD |
| `7D` | `11.21` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 554,520.00 USD | 130,380.00 USD | 1,090.00 USD |
| `1D` | `11.22` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 328,370.00 USD | 63,100.00 USD | 117,750.00 USD |
| `7D` | `11.23` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 288,220.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.24` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 163,340.00 USD | 54,170.00 USD | 155,350.00 USD |
| `7D` | `11.25` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD |
| `1D` | `11.26` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 149,280.00 USD | 44,890.00 USD | 71,490.00 USD |
| `7D` | `11.27` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.28` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 336,790.00 USD | 59,260.00 USD | 243,400.00 USD |
| `7D` | `11.29` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD |
| `1D` | `11.30` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 213,610.00 USD | 75,000.00 USD | 129,450.00 USD |
| `7D` | `11.31` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.32` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 168,840.00 USD | 74,250.00 USD | 142,340.00 USD |
| `7D` | `11.33` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD |
| `1D` | `11.34` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 390,100.00 USD | 118,470.00 USD | 107,170.00 USD |
| `7D` | `11.35` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD |
| `1D` | `11.36` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 138,710.00 USD | 95,240.00 USD | 56,330.00 USD |
| `7D` | `11.37` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD |
| `1D` | `11.38` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,380.00 USD |
| `7D` | `11.39` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD |
| `7D` | `11.41` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD |
| `1D` | `11.42` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 126,960.00 USD | 83,600.00 USD | 113,690.00 USD |
| `7D` | `11.43` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 265,450.00 USD | 117,170.00 USD | 92,240.00 USD |
| `1D` | `11.44` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 88,630.00 USD | 48,240.00 USD | 96,850.00 USD |
| `7D` | `11.45` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 227,420.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.46` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 86,190.00 USD | 75,110.00 USD | 50,780.00 USD |
| `7D` | `11.47` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD |
| `1D` | `11.48` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 24,020.00 USD | 31,070.00 USD | 1,910.00 USD |
| `7D` | `11.49` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.50` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 52,620.00 USD | 34,750.00 USD | 53,890.00 USD |
| `7D` | `11.51` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD |
| `1D` | `11.52` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 103,860.00 USD | 16,980.00 USD | 40,320.00 USD |
| `7D` | `11.53` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD |
| `1D` | `11.54` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 86,680.00 USD | 20,290.00 USD | 101,050.00 USD |
| `7D` | `11.55` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD |
| `1D` | `11.56` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 128,820.00 USD | 20,640.00 USD | 47,760.00 USD |
| `7D` | `11.57` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.58` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 58,760.00 USD | 2,950.00 USD | 17,790.00 USD |
| `7D` | `11.59` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD |
| `1D` | `11.60` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 59,560.00 USD | 14,330.00 USD | 67,580.00 USD |
| `7D` | `11.61` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.62` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 44,510.00 USD | 512.95 USD | 48,190.00 USD |
| `7D` | `11.63` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.64` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 5,220.00 USD | 7,410.00 USD | 31,250.00 USD |
| `7D` | `11.65` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD |
| `1D` | `11.66` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,690.00 USD |
| `7D` | `11.67` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD |
| `1D` | `11.68` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD |
| `7D` | `11.69` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD |
| `1D` | `11.70` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,760.00 USD |
| `7D` | `11.71` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD |
| `1D` | `11.72` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 112,130.00 USD | 18,090.00 USD | 98,120.00 USD |
| `7D` | `11.73` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD |
| `1D` | `11.74` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 76,690.00 USD | 30,300.00 USD | 73,130.00 USD |
| `7D` | `11.75` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD |
| `1D` | `11.76` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 26,330.00 USD | 14,880.00 USD | 24,830.00 USD |
| `7D` | `11.77` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.78` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 27,690.00 USD | 20,510.00 USD | 40,030.00 USD |
| `7D` | `11.79` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.80` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 1,190.00 USD | 18,000.00 USD | 531.07 USD |
| `7D` | `11.81` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 11,880.00 USD | 53.10 USD | 36,070.00 USD |
| `7D` | `11.83` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.84` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 43,880.00 USD | 11,870.00 USD | 45,600.00 USD |
| `7D` | `11.85` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.86` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD |
| `7D` | `11.87` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.88` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD |
| `7D` | `11.89` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.90` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 28,000.00 USD |
| `7D` | `11.91` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.92` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,120.00 USD |
| `7D` | `11.93` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD |
| `1D` | `11.94` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 48,030.00 USD | 15,260.00 USD | 40,220.00 USD |
| `7D` | `11.95` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD |
| `7D` | `11.97` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.98` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 59,940.00 USD | 29,060.00 USD | 68,170.00 USD |
| `7D` | `11.99` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.00` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 119,890.00 USD | 23,880.00 USD | 44,380.00 USD |
| `7D` | `12.01` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD |
| `1D` | `12.02` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 13,680.00 USD | 11,370.00 USD | 31,440.00 USD |
| `7D` | `12.03` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD |
| `1D` | `12.04` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 90,410.00 USD | 39,490.00 USD | 56,310.00 USD |
| `7D` | `12.05` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.06` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 76,750.00 USD | 43,270.00 USD | 69,900.00 USD |
| `7D` | `12.07` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD |
| `1D` | `12.08` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 43,090.00 USD | 40,740.00 USD | 52,270.00 USD |
| `7D` | `12.09` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD |
| `1D` | `12.10` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 49,200.00 USD | 22,590.00 USD | 29,830.00 USD |
| `7D` | `12.11` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.12` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 116,870.00 USD | 54,460.00 USD | 50,650.00 USD |
| `7D` | `12.13` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD |
| `1D` | `12.14` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 75,780.00 USD | 35,660.00 USD | 55,700.00 USD |
| `7D` | `12.15` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD |
| `1D` | `12.16` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 124,550.00 USD | 34,710.00 USD | 67,620.00 USD |
| `7D` | `12.17` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.18` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 112,670.00 USD | 46,930.00 USD | 47,750.00 USD |
| `7D` | `12.19` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD |
| `1D` | `12.20` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 71,000.00 USD | 43,870.00 USD | 38,370.00 USD |
| `7D` | `12.21` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD |
| `1D` | `12.22` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 10,400.00 USD | 18,360.00 USD | 32,260.00 USD |
| `7D` | `12.23` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 140,270.00 USD | 27,350.00 USD | 9,170.00 USD |
| `1D` | `12.24` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 4,800.00 USD | 15,280.00 USD | 0.00 USD |
| `7D` | `12.25` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 47,780.00 USD | 46,250.00 USD | 46,950.00 USD |
| `7D` | `12.27` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD |
| `7D` | `12.29` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD |
| `7D` | `12.31` | 16,680,000.00 USD | 16,680,000.00 USD | 0.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD |
| `7D` | `12.33` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD |
| `7D` | `12.35` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD |
| `7D` | `12.37` | 16,840,000.00 USD | 16,840,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD |
| `7D` | `12.39` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD |
| `7D` | `12.40` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `509.04M` | Total OI Tokens: `46,182,722.7 LINK`
  * 1h OI Change: `-0.72%` | 4h OI Change: `-1.50%` | 24h OI Change: `-7.11%`
  * Exchange Breakdown: Binance=`99.95M` | Bybit=`68.59M` | OKX=`26.66M` | Hyperliquid=`55.61M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.70K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0016%` |
| **USDT Bybit** | `0.0000%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0062%` | **USDT Bitget** | `0.0083%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `50.26%` | `49.74%` | `1.01` | 4,250,000.00 USD |
| `15M` | `Binance` | `46.37%` | `53.63%` | `0.86` | 1,210,000.00 USD |
| `15M` | `OKX` | `66.34%` | `33.66%` | `1.97` | 652,490.00 USD |
| `15M` | `Bybit` | `47.73%` | `52.27%` | `0.91` | 685,000.00 USD |
| `15M` | `KuCoin` | `52.62%` | `47.38%` | `1.11` | 26,350.00 USD |
| `15M` | `Gate` | `77.08%` | `22.92%` | `3.36` | 85,860.00 USD |
| `15M` | `Bitget` | `31.31%` | `68.69%` | `0.46` | 242,440.00 USD |
| `15M` | `BingX` | `44.21%` | `55.79%` | `0.79` | 107,900.00 USD |
| `15M` | `MEXC` | `72.72%` | `27.28%` | `2.67` | 323,860.00 USD |
| `15M` | `Bitunix` | `75.55%` | `24.45%` | `3.09` | 76,550.00 USD |
| `15M` | `Hyperliquid` | `41.99%` | `58.01%` | `0.72` | 6,430.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.06%` | `47.94%` | `1.09` | 563,620.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 232,190.00 USD |
| `15M` | `HTX` | `69.54%` | `30.46%` | `2.28` | 7,940.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `56.62%` | `43.38%` | `1.31` | 31,740.00 USD |
| `15M` | `Aster` | `18.17%` | `81.83%` | `0.22` | 1,080.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `91.81%` | `8.19%` | `11.21` | 113.42 USD |
| `15M` | `Whale Positions` | `46.37%` | `53.63%` | `0.86` | 1,210,000.00 USD |
| `15M` | `Global Accounts` | `50.26%` | `49.74%` | `1.01` | 4,250,000.00 USD |
| `1H` | `LINK` | `42.60%` | `57.40%` | `0.74` | 57,710,000.00 USD |
| `1H` | `Binance` | `43.91%` | `56.09%` | `0.78` | 34,140,000.00 USD |
| `1H` | `OKX` | `47.47%` | `52.53%` | `0.90` | 4,570,000.00 USD |
| `1H` | `Bybit` | `29.29%` | `70.71%` | `0.41` | 6,420,000.00 USD |
| `1H` | `KuCoin` | `51.16%` | `48.84%` | `1.05` | 778,150.00 USD |
| `1H` | `Gate` | `45.91%` | `54.09%` | `0.85` | 2,920,000.00 USD |
| `1H` | `Bitget` | `38.35%` | `61.65%` | `0.62` | 1,320,000.00 USD |
| `1H` | `BingX` | `45.5%` | `54.5%` | `0.83` | 995,420.00 USD |
| `1H` | `MEXC` | `42.46%` | `57.54%` | `0.74` | 678,290.00 USD |
| `1H` | `Bitunix` | `47.38%` | `52.62%` | `0.90` | 1,390,000.00 USD |
| `1H` | `Hyperliquid` | `56.22%` | `43.78%` | `1.28` | 1,340,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.66%` | `51.34%` | `0.95` | 430,690.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `4.07%` | `95.93%` | `0.04` | 1,000,000.00 USD |
| `1H` | `HTX` | `57.92%` | `42.08%` | `1.38` | 326,360.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.07%` | `52.93%` | `0.89` | 301,560.00 USD |
| `1H` | `Aster` | `45.81%` | `54.19%` | `0.85` | 788,950.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `65.24%` | `34.76%` | `1.88` | 319,720.00 USD |
| `1H` | `Whale Positions` | `43.91%` | `56.09%` | `0.78` | 34,140,000.00 USD |
| `1H` | `Global Accounts` | `42.60%` | `57.40%` | `0.74` | 57,710,000.00 USD |
| `4H` | `LINK` | `50.23%` | `49.77%` | `1.01` | 158,390,000.00 USD |
| `4H` | `Binance` | `48.84%` | `51.16%` | `0.95` | 57,600,000.00 USD |
| `4H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 32,830,000.00 USD |
| `4H` | `Bybit` | `55.59%` | `44.41%` | `1.25` | 10,440,000.00 USD |
| `4H` | `KuCoin` | `50.63%` | `49.37%` | `1.03` | 1,130,000.00 USD |
| `4H` | `Gate` | `43.2%` | `56.8%` | `0.76` | 27,110,000.00 USD |
| `4H` | `Bitget` | `54.65%` | `45.35%` | `1.21` | 2,580,000.00 USD |
| `4H` | `BingX` | `25.5%` | `74.5%` | `0.34` | 3,430,000.00 USD |
| `4H` | `MEXC` | `49.19%` | `50.81%` | `0.97` | 9,180,000.00 USD |
| `4H` | `Bitunix` | `51.37%` | `48.63%` | `1.06` | 3,870,000.00 USD |
| `4H` | `Hyperliquid` | `56.01%` | `43.99%` | `1.27` | 1,430,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.3%` | `49.7%` | `1.01` | 1,130,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 195,840.00 USD |
| `4H` | `WhiteBIT` | `54.99%` | `45.01%` | `1.22` | 5,140,000.00 USD |
| `4H` | `HTX` | `52.89%` | `47.11%` | `1.12` | 789,490.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.84%` | `24.16%` | `3.14` | 607,140.00 USD |
| `4H` | `Aster` | `40.2%` | `59.8%` | `0.67` | 851,290.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.6%` | `46.4%` | `1.16` | 85,260.00 USD |
| `4H` | `Whale Positions` | `48.84%` | `51.16%` | `0.95` | 57,600,000.00 USD |
| `4H` | `Global Accounts` | `50.23%` | `49.77%` | `1.01` | 158,390,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.07` | `11.04` | `11.07` | `11.07` | `11.00` | 2,041,123.66 USD | 896,885.50 USD | 1,144,238.16 USD | -247,352.65 USD | `-12.12%` | `4B / 9S` |
| `0:00 UTC` | `11.04` | `11.03` | `11.04` | `11.08` | `10.99` | 1,789,361.54 USD | 895,862.51 USD | 893,499.03 USD | 2,363.48 USD | `+0.13%` | `15B / 15S` |
| `5:00 UTC` | `11.07` | `11.08` | `11.07` | `11.11` | `11.04` | 1,641,738.88 USD | 696,135.31 USD | 945,603.58 USD | -249,468.27 USD | `-15.20%` | `10B / 19S` |
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.07` | `11.00` | 1,477,587.17 USD | 739,486.08 USD | 738,101.09 USD | 1,384.99 USD | `+0.09%` | `8B / 13S` |
| `5:00 UTC` | `11.00` | `11.01` | `11.00` | `11.05` | `10.99` | 1,128,540.66 USD | 513,281.75 USD | 615,258.92 USD | -101,977.17 USD | `-9.04%` | `14B / 18S` |
| `0:00 UTC` | `11.01` | `11.00` | `11.01` | `11.03` | `10.97` | 1,915,299.28 USD | 805,989.55 USD | 1,109,309.72 USD | -303,320.17 USD | `-15.84%` | `3B / 10S` |
| `5:00 UTC` | `10.97` | `10.99` | `10.97` | `11.01` | `10.96` | 1,089,442.23 USD | 506,886.53 USD | 582,555.71 USD | -75,669.18 USD | `-6.95%` | `5B / 8S` |
| `0:00 UTC` | `10.98` | `10.99` | `10.98` | `11.03` | `10.95` | 1,226,717.62 USD | 576,497.16 USD | 650,220.46 USD | -73,723.30 USD | `-6.01%` | `21B / 13S` |
| `5:00 UTC` | `11.03` | `11.02` | `11.03` | `11.05` | `10.99` | 1,086,301.02 USD | 486,090.76 USD | 600,210.26 USD | -114,119.49 USD | `-10.51%` | `11B / 6S` |
| `0:00 UTC` | `11.03` | `11.02` | `11.03` | `11.04` | `11.00` | 630,880.66 USD | 340,254.18 USD | 290,626.48 USD | 49,627.70 USD | `+7.87%` | `7B / 5S` |

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
| `5m` | -12,270.00 USD | -89,360.00 USD | **`DISTRIBUTION`** |
| `15m` | 31,140.00 USD | -55,540.00 USD | **`DISTRIBUTION`** |
| `30m` | 230,050.00 USD | -36,310.00 USD | **`ACCUMULATION`** |
| `1h` | 154,400.00 USD | -212,740.00 USD | **`DISTRIBUTION`** |
| `2h` | -134,390.00 USD | -732,800.00 USD | **`DISTRIBUTION`** |
| `4h` | -204,510.00 USD | -628,080.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,100,000.00 USD | -1,780,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -966,680.00 USD | 950,800.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,690,000.00 USD | -9,850,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,210,000.00 USD | -22,910,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,580,000.00 USD | -42,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,900,000.00 USD | -194,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.27K` | 15m=`+31.14K` | 1h=`+154.40K` | 24h=`-11.21M`
* Futures Capital Netflows: 5m=`-89.36K` | 15m=`-55.54K` | 1h=`-212.74K` | 24h=`-22.91M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.32` (Risk Distance: `0.2298` pts)
  * +2.5R Take Profit: `11.13`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.35` (Risk Distance: `0.2298` pts)
  * +2.5R Take Profit: `10.55`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.09`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
