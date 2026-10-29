# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:14:46 IST` (`2026-10-29 19:44:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `7.16` | **Live Ask Quote**: `7.19` | **Mid Price**: `7.18`
- **Spread Points**: `24.00` | **Spread BPS**: `33.44 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `7.15` | VWAP Z-Score: `-0.08` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0587` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.18` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.57` | Lower -3.00σ Band: `6.74`
  * Upper +2.51σ Band: `7.50` | Lower -2.51σ Band: `6.81`
  * Upper +2.01σ Band: `7.43` | Lower -2.01σ Band: `6.88`
  * Upper +2.00σ Band: `7.43` | Lower -2.00σ Band: `6.88`
  * Upper +1.28σ Band: `7.33` | Lower -1.28σ Band: `6.98`
  * Upper +1.00σ Band: `7.29` | Lower -1.00σ Band: `7.01`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7.20` | EMA-20=`7.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7.19` (Slope: `+0.0000`) | EMA-100=`7.16`
  * Institutional Anchors: EMA-144=`7.14` | EMA-200=`7.13` (Slope: `+0.1969`) | EMA-233=`7.11`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.89` | Weekly High=`7.50` | Weekly Low=`6.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7.41` (Distance: `-3.13%`)
  * Point of Control (POC) = `7.20` (Distance: `-0.24%`)
  * Value Area Low (VAL) = `7.04` (Distance: `+1.93%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.18` | POC=`7.05` | VAL=`7.03`
  * Prior Day Extremes: PDH=`7.32` | PDL=`6.95` | PDC=`7.22`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.18` | Weekly POC=`7.04` | Weekly VAL=`6.94`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`7.33` | Low=`6.89`
  * London Session (08:00-16:00 UTC): High=`7.22` | Low=`6.95`
  * New York Session (13:00-21:00 UTC): High=`7.50` | Low=`7.00`
  * Initial Balance (First Hour): IB High=`7.12` | IB Low=`7.02`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `7.15` - `7.20`
  * Optimal Trade Entry (OTE 0.705): `7.19`
  * Structural Invalidation Anchor (0.786): `7.23`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `331` | `0x5396...8b79` | `LONG` | 7,188,798.56 USD | `999,999.80` | `6.88` | `7.19` | `5.66` | 308,100.24 USD | `+4.29%` | `5X Cross` |
| `721` | `0x9df2...c665` | `SHORT` | 3,234,870.00 USD | `450,000.00` | `4.49` | `7.19` | `70.24` | -1,213,869.87 USD | `-37.52%` | `10X Cross` |
| `887` | `0xdd53...2b13` | `SHORT` | 2,583,640.28 USD | `359,478.00` | `7.29` | `7.19` | `158.15` | 35,864.20 USD | `+1.39%` | `3X Cross` |
| `1047` | `0xb46b...538e` | `SHORT` | 2,156,370.00 USD | `300,000.00` | `8.20` | `7.19` | `19.74` | 303,414.42 USD | `+14.07%` | `10X Cross` |
| `1057` | `0xbf6d...ecc0` | `LONG` | 2,124,954.26 USD | `295,575.90` | `7.78` | `7.19` | `4.76` | -174,471.86 USD | `-8.21%` | `10X Cross` |
| `1081` | `0xcd21...9826` | `LONG` | 2,086,488.02 USD | `290,326.30` | `7.85` | `7.19` | `5.08` | -193,194.28 USD | `-9.26%` | `10X Cross` |
| `1217` | `0xf21d...3b2d` | `LONG` | 1,886,201.30 USD | `262,384.20` | `4.28` | `7.19` | `4.06` | 763,383.46 USD | `+40.47%` | `10X Isolated` |
| `1274` | `0x9aa5...58af` | `SHORT` | 1,813,353.17 USD | `252,320.70` | `7.34` | `7.19` | `36.67` | 38,812.89 USD | `+2.14%` | `10X Cross` |
| `1291` | `0xecb6...2b00` | `SHORT` | 1,763,534.04 USD | `245,371.50` | `7.23` | `7.19` | `114.49` | 9,945.67 USD | `+0.56%` | `10X Cross` |
| `1318` | `0xf472...5d8b` | `LONG` | 1,734,958.41 USD | `241,374.10` | `4.44` | `7.19` | `0.000000` | 662,315.13 USD | `+38.17%` | `5X Cross` |
| `1445` | `0xb5b3...7a08` | `LONG` | 1,581,074.00 USD | `220,000.00` | `7.36` | `7.19` | `0.000000` | -39,136.15 USD | `-2.48%` | `10X Cross` |
| `1538` | `0x645b...87b8` | `SHORT` | 1,455,789.70 USD | `202,567.20` | `8.57` | `7.19` | `101.43` | 280,740.33 USD | `+19.28%` | `10X Cross` |
| `1552` | `0xcac1...26b3` | `SHORT` | 1,440,261.32 USD | `200,336.80` | `7.76` | `7.19` | `45.83` | 113,586.65 USD | `+7.89%` | `10X Cross` |
| `1687` | `0x12d2...f97f` | `LONG` | 1,299,069.75 USD | `180,697.40` | `8.85` | `7.19` | `0.000000` | -300,850.15 USD | `-23.16%` | `10X Cross` |
| `1688` | `0x265e...7f70` | `LONG` | 1,298,388.75 USD | `180,665.50` | `7.54` | `7.19` | `0.000000` | -64,266.00 USD | `-4.95%` | `3X Cross` |
| `1700` | `0x51f6...2b39` | `SHORT` | 1,292,073.18 USD | `179,756.70` | `7.35` | `7.19` | `16.03` | 29,408.67 USD | `+2.28%` | `10X Cross` |
| `1760` | `0xb83d...6e36` | `SHORT` | 1,214,664.93 USD | `168,971.00` | `7.45` | `7.19` | `752.74` | 43,437.30 USD | `+3.58%` | `3X Cross` |
| `1867` | `0xdf95...7d72` | `SHORT` | 1,123,672.00 USD | `156,343.50` | `6.56` | `7.19` | `232.53` | -97,378.95 USD | `-8.67%` | `10X Cross` |
| `1909` | `0xcb84...52cd` | `SHORT` | 1,081,803.93 USD | `150,519.60` | `7.14` | `7.19` | `20.63` | -6,496.34 USD | `-0.60%` | `10X Cross` |
| `1934` | `0xa23d...bf71` | `LONG` | 1,061,681.15 USD | `147,660.80` | `7.66` | `7.19` | `5.62` | -68,994.19 USD | `-6.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `9.56` | 27,873.78 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 27.87K USD at 9.5576 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 49.70 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.05K USD at 9.5578 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 2,206.92 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 2.21K USD at 9.5579 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 105.14 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 9.5582 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 105.14 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 9.5583 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 105.15 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 9.5589 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 3,989.97 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.99K USD at 9.5591 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 3,059.93 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.06K USD at 9.5593 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 35.37 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.04K USD at 9.5596 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 105.16 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 9.5600 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 36.33 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.04K USD at 9.5600 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 105.16 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 9.5601 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 575.52 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.58K USD at 9.5602 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 10,000.49 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 10.00K USD at 9.5607 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 3,924.75 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.92K USD at 9.5609 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 208.44 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.21K USD at 9.5615 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 74.58 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.07K USD at 9.5621 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.56` | 14,994.96 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 14.99K USD at 9.5625 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.57` | 44.00 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.04K USD at 9.5652 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.57` | 100.45 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.10K USD at 9.5671 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.57` | 4,390.48 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 4.39K USD at 9.5674 USD [API] | `2026-09-23 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `9.57` | 16,638.58 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 16.64K USD at 9.5679 USD [API] | `2026-09-23 10:24:35` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.59%`) | Long MP=`7.04` (Vol: 235,800.00 USD, Dist: `--1.93%`)
  * 48H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.59%`) | Long MP=`6.91` (Vol: 378,300.00 USD, Dist: `--3.76%`)
  * 3D Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.59%`) | Long MP=`6.91` (Vol: 537,300.00 USD, Dist: `--3.76%`)
  * 7D Horizon: Short MP=`7.61` (Vol: 392,700.00 USD, Dist: `+6.00%`) | Long MP=`6.90` (Vol: 565,900.00 USD, Dist: `--3.93%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.46K` | Last 24h: `66.11K` | Last 3d: `148.54K` | Last 7d: `245.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0093%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0123%` | **USDT KuCoin** | `-0.0024%` |
| **USDT MEXC** | `0.0093%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0066%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-0.0113%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `7.31` | `7.31` | `7.31` | `7.33` | `7.30` | 1,640,944.05 USD | 699,024.71 USD | 941,919.34 USD | -242,894.62 USD | `-14.80%` | `4B / 5S` |
| `0:00 UTC` | `7.32` | `7.30` | `7.32` | `7.35` | `7.25` | 2,769,110.24 USD | 1,235,974.80 USD | 1,533,135.44 USD | -297,160.64 USD | `-10.73%` | `10B / 30S` |
| `5:00 UTC` | `7.23` | `7.24` | `7.23` | `7.26` | `7.21` | 2,241,943.13 USD | 1,083,432.08 USD | 1,158,511.05 USD | -75,078.97 USD | `-3.35%` | `2B / 7S` |
| `0:00 UTC` | `7.24` | `7.25` | `7.24` | `7.28` | `7.22` | 1,784,775.42 USD | 846,471.36 USD | 938,304.06 USD | -91,832.70 USD | `-5.15%` | `4B / 12S` |
| `5:00 UTC` | `7.24` | `7.23` | `7.24` | `7.26` | `7.21` | 1,061,041.90 USD | 589,058.95 USD | 471,982.95 USD | 117,075.99 USD | `+11.03%` | `17B / 5S` |
| `0:00 UTC` | `7.17` | `7.18` | `7.17` | `7.22` | `7.16` | 3,597,323.95 USD | 1,700,383.25 USD | 1,896,940.71 USD | -196,557.46 USD | `-5.46%` | `4B / 12S` |
| `5:00 UTC` | `7.16` | `7.18` | `7.16` | `7.21` | `7.15` | 2,196,425.29 USD | 1,064,538.01 USD | 1,131,887.28 USD | -67,349.27 USD | `-3.07%` | `19B / 4S` |
| `0:00 UTC` | `7.17` | `7.17` | `7.17` | `7.19` | `7.15` | 1,134,824.79 USD | 719,458.28 USD | 415,366.51 USD | 304,091.78 USD | `+26.80%` | `8B / 1S` |
| `5:00 UTC` | `7.17` | `7.16` | `7.17` | `7.18` | `7.15` | 1,021,800.59 USD | 474,808.50 USD | 546,992.09 USD | -72,183.59 USD | `-7.06%` | `10B / 9S` |
| `0:00 UTC` | `7.19` | `7.18` | `7.19` | `7.20` | `7.16` | 909,975.41 USD | 542,682.64 USD | 367,292.77 USD | 175,389.87 USD | `+19.27%` | `14B / 3S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:55` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.08` | 0.00 USD | 0.00 USD |
| `10-28 20:19` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.05` | 0.00 USD | 0.00 USD |
| `10-28 19:51` | `Range 0.02` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `6.97` | 22,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Range 0.02` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `6.98` | 41,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.01` | 0.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `6.98` | 0.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.02` | 0.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `6.99` | 0.00 USD | 0.00 USD |
| `10-28 19:08` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.04` | 16,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.03` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.00` | 0.00 USD | 0.00 USD |
| `10-28 17:56` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.09` | 36,000.00 USD | 0.00 USD |
| `10-28 17:26` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.12` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.18` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.15` | 21,000.00 USD | 0.00 USD |
| `10-28 14:32` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.15` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.20` | 0.00 USD | 0.00 USD |
| `10-28 11:45` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `7.18` | 0.00 USD | 0.00 USD |
| `10-28 10:40` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `7.17` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.10` | 0.00 USD | 0.00 USD |
| `10-28 09:19` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.15` | 20,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.16` | 14,000.00 USD | 0.00 USD |
| `10-28 08:57` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.15` | 0.00 USD | 0.00 USD |
| `10-28 06:23` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.10` | 48,000.00 USD | 0.00 USD |
| `10-28 06:23` | `Range 0.02` | `Trapped longs` | **`BEARISH`** | Failed breakout | `7.10` | 48,000.00 USD | 0.00 USD |
| `10-28 06:03` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.06` | 21,000.00 USD | 0.00 USD |
| `10-28 05:38` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.04` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 263,230.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 287,900.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 569,440.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 1,330,000.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | -341,470.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -1,750,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | 1,370,000.00 USD | **`ACCUMULATION`** |
| `8h` | 0.00 USD | -3,920,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -2,910,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -12,670,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -48,310,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -478,870,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+263.23K` | 15m=`+287.90K` | 1h=`+1.33M` | 24h=`-12.67M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `7.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.93` (Risk Distance: `0.1064` pts)
  * +2.5R Take Profit: `7.31`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7.41` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.52` (Risk Distance: `0.1064` pts)
  * +2.5R Take Profit: `7.14`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`7.23`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
