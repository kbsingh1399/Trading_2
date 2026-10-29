# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:14:11 IST` (`2026-10-29 18:44:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `7.16` | **Live Ask Quote**: `7.18` | **Mid Price**: `7.17`
- **Spread Points**: `23.00` | **Spread BPS**: `32.08 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `7.15` | VWAP Z-Score: `+0.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0632` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.58` | Lower -3.00σ Band: `6.73`
  * Upper +2.51σ Band: `7.51` | Lower -2.51σ Band: `6.80`
  * Upper +2.01σ Band: `7.44` | Lower -2.01σ Band: `6.87`
  * Upper +2.00σ Band: `7.43` | Lower -2.00σ Band: `6.87`
  * Upper +1.28σ Band: `7.33` | Lower -1.28σ Band: `6.97`
  * Upper +1.00σ Band: `7.29` | Lower -1.00σ Band: `7.01`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7.27` | EMA-20=`7.27` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7.20` (Slope: `+0.0000`) | EMA-100=`7.16`
  * Institutional Anchors: EMA-144=`7.14` | EMA-200=`7.12` (Slope: `+0.3500`) | EMA-233=`7.11`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.89` | Weekly High=`7.50` | Weekly Low=`6.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7.41` (Distance: `-3.23%`)
  * Point of Control (POC) = `7.20` (Distance: `-0.35%`)
  * Value Area Low (VAL) = `7.04` (Distance: `+1.88%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `7.14` - `7.20`
  * Optimal Trade Entry (OTE 0.705): `7.18`
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:05:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `331` | `0x5396...8b79` | `LONG` | 7,188,198.56 USD | `999,999.80` | `6.88` | `7.19` | `5.66` | 307,500.24 USD | `+4.28%` | `5X Cross` |
| `718` | `0x9df2...c665` | `SHORT` | 3,227,625.00 USD | `450,000.00` | `4.49` | `7.19` | `69.94` | -1,206,624.87 USD | `-37.38%` | `10X Cross` |
| `884` | `0xdd53...2b13` | `SHORT` | 2,583,820.02 USD | `359,478.00` | `7.29` | `7.19` | `157.92` | 35,684.46 USD | `+1.38%` | `3X Cross` |
| `1042` | `0xb46b...538e` | `SHORT` | 2,156,316.00 USD | `300,000.00` | `8.20` | `7.19` | `19.66` | 303,468.42 USD | `+14.07%` | `10X Cross` |
| `1048` | `0xbf6d...ecc0` | `LONG` | 2,126,047.89 USD | `295,575.90` | `7.78` | `7.19` | `4.74` | -173,378.23 USD | `-8.15%` | `10X Cross` |
| `1076` | `0xcd21...9826` | `LONG` | 2,082,017.00 USD | `290,326.30` | `7.85` | `7.19` | `5.07` | -197,665.31 USD | `-9.49%` | `10X Cross` |
| `1219` | `0xf21d...3b2d` | `LONG` | 1,881,347.19 USD | `262,384.20` | `4.28` | `7.19` | `4.06` | 758,529.35 USD | `+40.32%` | `10X Isolated` |
| `1261` | `0x9aa5...58af` | `SHORT` | 1,809,290.81 USD | `252,320.70` | `7.34` | `7.19` | `36.96` | 42,875.25 USD | `+2.37%` | `10X Cross` |
| `1288` | `0xecb6...2b00` | `SHORT` | 1,761,069.75 USD | `245,010.90` | `7.23` | `7.19` | `114.24` | 9,826.92 USD | `+0.56%` | `10X Cross` |
| `1311` | `0xf472...5d8b` | `LONG` | 1,731,014.36 USD | `241,374.10` | `4.44` | `7.19` | `0.000000` | 658,371.08 USD | `+38.03%` | `5X Cross` |
| `1434` | `0xb5b3...7a08` | `LONG` | 1,577,510.00 USD | `220,000.00` | `7.36` | `7.19` | `0.000000` | -42,700.15 USD | `-2.71%` | `10X Cross` |
| `1530` | `0x645b...87b8` | `SHORT` | 1,452,791.70 USD | `202,567.20` | `8.57` | `7.19` | `100.71` | 283,738.33 USD | `+19.53%` | `10X Cross` |
| `1544` | `0xcac1...26b3` | `SHORT` | 1,441,002.57 USD | `200,336.80` | `7.76` | `7.19` | `45.60` | 112,845.41 USD | `+7.83%` | `10X Cross` |
| `1683` | `0x12d2...f97f` | `LONG` | 1,296,124.38 USD | `180,697.40` | `8.85` | `7.19` | `0.000000` | -303,795.52 USD | `-23.44%` | `10X Cross` |
| `1684` | `0x265e...7f70` | `LONG` | 1,295,714.90 USD | `180,665.50` | `7.54` | `7.19` | `0.000000` | -66,939.85 USD | `-5.17%` | `3X Cross` |
| `1687` | `0x51f6...2b39` | `SHORT` | 1,293,364.81 USD | `179,940.90` | `7.35` | `7.19` | `16.23` | 29,471.19 USD | `+2.28%` | `10X Cross` |
| `1756` | `0xb83d...6e36` | `SHORT` | 1,211,944.50 USD | `168,971.00` | `7.45` | `7.19` | `760.52` | 46,157.73 USD | `+3.81%` | `3X Cross` |
| `1860` | `0xdf95...7d72` | `SHORT` | 1,120,951.63 USD | `156,343.50` | `6.56` | `7.19` | `234.33` | -94,658.57 USD | `-8.44%` | `10X Cross` |
| `1906` | `0xcb84...52cd` | `SHORT` | 1,079,556.68 USD | `150,519.60` | `7.14` | `7.19` | `20.61` | -4,249.08 USD | `-0.39%` | `10X Cross` |
| `1930` | `0xa23d...bf71` | `LONG` | 1,061,503.96 USD | `147,660.80` | `7.66` | `7.19` | `5.62` | -69,171.39 USD | `-6.52%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.02%`) | Long MP=`7.04` (Vol: 235,800.00 USD, Dist: `--2.46%`)
  * 48H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.02%`) | Long MP=`6.91` (Vol: 378,300.00 USD, Dist: `--4.28%`)
  * 3D Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+5.02%`) | Long MP=`6.91` (Vol: 537,300.00 USD, Dist: `--4.28%`)
  * 7D Horizon: Short MP=`7.61` (Vol: 392,700.00 USD, Dist: `+5.43%`) | Long MP=`6.90` (Vol: 565,900.00 USD, Dist: `--4.45%`)
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
  * Current Rate: `20.36K` | Last 24h: `66.11K` | Last 3d: `148.54K` | Last 7d: `245.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0034%` | **USDT KuCoin** | `-0.0009%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0062%` | **USDT Bitget** | `0.0060%` |
| **CoinM Binance** | `-0.0093%` | **CoinM OKX** | `0.0100%` |

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
| `5:00 UTC` | `7.45` | `7.44` | `7.45` | `7.48` | `7.41` | 4,064,958.66 USD | 1,436,607.98 USD | 2,628,350.68 USD | -1,191,742.70 USD | `-29.32%` | `7B / 15S` |
| `0:00 UTC` | `7.42` | `7.39` | `7.42` | `7.43` | `7.35` | 3,574,044.16 USD | 1,480,242.42 USD | 2,093,801.73 USD | -613,559.31 USD | `-17.17%` | `4B / 16S` |
| `5:00 UTC` | `7.38` | `7.38` | `7.38` | `7.39` | `7.35` | 1,324,026.23 USD | 564,857.55 USD | 759,168.68 USD | -194,311.13 USD | `-14.68%` | `2B / 13S` |
| `0:00 UTC` | `7.32` | `7.34` | `7.32` | `7.38` | `7.31` | 2,591,397.44 USD | 868,020.88 USD | 1,723,376.56 USD | -855,355.67 USD | `-33.01%` | `1B / 26S` |
| `5:00 UTC` | `7.31` | `7.31` | `7.31` | `7.33` | `7.30` | 1,640,944.05 USD | 699,024.71 USD | 941,919.34 USD | -242,894.62 USD | `-14.80%` | `4B / 5S` |
| `0:00 UTC` | `7.32` | `7.30` | `7.32` | `7.35` | `7.25` | 2,769,110.24 USD | 1,235,974.80 USD | 1,533,135.44 USD | -297,160.64 USD | `-10.73%` | `10B / 30S` |
| `5:00 UTC` | `7.23` | `7.24` | `7.23` | `7.26` | `7.21` | 2,241,943.13 USD | 1,083,432.08 USD | 1,158,511.05 USD | -75,078.97 USD | `-3.35%` | `2B / 7S` |
| `0:00 UTC` | `7.24` | `7.25` | `7.24` | `7.28` | `7.22` | 1,784,775.42 USD | 846,471.36 USD | 938,304.06 USD | -91,832.70 USD | `-5.15%` | `4B / 12S` |
| `5:00 UTC` | `7.24` | `7.23` | `7.24` | `7.26` | `7.21` | 1,061,041.90 USD | 589,058.95 USD | 471,982.95 USD | 117,075.99 USD | `+11.03%` | `17B / 5S` |
| `0:00 UTC` | `7.17` | `7.18` | `7.17` | `7.22` | `7.16` | 3,067,139.95 USD | 1,477,617.80 USD | 1,589,522.16 USD | -111,904.36 USD | `-3.65%` | `4B / 13S` |

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
| `5m` | -466,150.00 USD | -562,430.00 USD | **`DISTRIBUTION`** |
| `15m` | -400,420.00 USD | -440,570.00 USD | **`DISTRIBUTION`** |
| `30m` | -949,140.00 USD | -782,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -897,720.00 USD | -981,440.00 USD | **`DISTRIBUTION`** |
| `2h` | -329,020.00 USD | -5,130,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,200,000.00 USD | -485,610.00 USD | **`ACCUMULATION`** |
| `6h` | 667,440.00 USD | -4,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 796,840.00 USD | -6,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 591,040.00 USD | -4,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 1,800,000.00 USD | -13,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,540,000.00 USD | -49,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -42,510,000.00 USD | -482,140,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-466.15K` | 15m=`-400.42K` | 1h=`-897.72K` | 24h=`+1.80M`
* Futures Capital Netflows: 5m=`-562.43K` | 15m=`-440.57K` | 1h=`-981.44K` | 24h=`-13.48M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `6.93` (Risk Distance: `0.1103` pts)
  * +2.5R Take Profit: `7.31`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7.41` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.52` (Risk Distance: `0.1103` pts)
  * +2.5R Take Profit: `7.13`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`7.23`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
