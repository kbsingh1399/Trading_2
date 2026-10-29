# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:42:57 IST` (`2026-10-29 17:12:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `7.34` | **Live Ask Quote**: `7.36` | **Mid Price**: `7.35`
- **Spread Points**: `26.00` | **Spread BPS**: `35.37 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `7.14` | VWAP Z-Score: `+1.49` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0664` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.55` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.57` | Lower -3.00σ Band: `6.71`
  * Upper +2.51σ Band: `7.50` | Lower -2.51σ Band: `6.78`
  * Upper +2.01σ Band: `7.43` | Lower -2.01σ Band: `6.85`
  * Upper +2.00σ Band: `7.43` | Lower -2.00σ Band: `6.86`
  * Upper +1.28σ Band: `7.32` | Lower -1.28σ Band: `6.96`
  * Upper +1.00σ Band: `7.28` | Lower -1.00σ Band: `7.00`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7.35` | EMA-20=`7.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7.19` (Slope: `+0.0000`) | EMA-100=`7.15`
  * Institutional Anchors: EMA-144=`7.13` | EMA-200=`7.12` (Slope: `+0.3899`) | EMA-233=`7.10`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.89` | Weekly High=`7.50` | Weekly Low=`6.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7.24` (Distance: `+1.49%`)
  * Point of Control (POC) = `7.01` (Distance: `+4.71%`)
  * Value Area Low (VAL) = `6.92` (Distance: `+6.05%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.18` | POC=`7.05` | VAL=`7.03`
  * Prior Day Extremes: PDH=`7.32` | PDL=`6.95` | PDC=`7.22`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.18` | Weekly POC=`7.04` | Weekly VAL=`6.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`7.33` | Low=`6.89`
  * London Session (08:00-16:00 UTC): High=`7.22` | Low=`6.95`
  * New York Session (13:00-21:00 UTC): High=`7.50` | Low=`7.00`
  * Initial Balance (First Hour): IB High=`7.12` | IB Low=`7.02`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `7.32` - `7.38`
  * Optimal Trade Entry (OTE 0.705): `7.36`
  * Structural Invalidation Anchor (0.786): `7.41`

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
| --- | **`7.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `333` | `0x5396...8b79` | `LONG` | 7,342,298.53 USD | `999,999.80` | `6.88` | `7.34` | `5.66` | 461,600.21 USD | `+6.29%` | `5X Cross` |
| `721` | `0x9df2...c665` | `SHORT` | 3,305,520.00 USD | `450,000.00` | `4.49` | `7.34` | `68.33` | -1,284,519.87 USD | `-38.86%` | `10X Cross` |
| `887` | `0xdd53...2b13` | `SHORT` | 2,639,251.53 USD | `359,478.00` | `7.29` | `7.34` | `151.43` | -19,747.05 USD | `-0.75%` | `3X Cross` |
| `1045` | `0xb46b...538e` | `SHORT` | 2,202,600.00 USD | `300,000.00` | `8.20` | `7.34` | `18.78` | 257,184.42 USD | `+11.68%` | `10X Cross` |
| `1052` | `0xbf6d...ecc0` | `LONG` | 2,170,768.52 USD | `295,575.90` | `7.78` | `7.34` | `4.77` | -128,657.59 USD | `-5.93%` | `10X Cross` |
| `1069` | `0xcd21...9826` | `LONG` | 2,133,317.65 USD | `290,326.30` | `7.85` | `7.34` | `5.09` | -146,364.65 USD | `-6.86%` | `10X Cross` |
| `1201` | `0xf21d...3b2d` | `LONG` | 1,927,999.10 USD | `262,384.20` | `4.28` | `7.34` | `4.06` | 805,181.26 USD | `+41.76%` | `10X Isolated` |
| `1260` | `0x9aa5...58af` | `SHORT` | 1,855,869.21 USD | `252,320.70` | `7.34` | `7.34` | `35.09` | -3,703.15 USD | `-0.20%` | `10X Cross` |
| `1293` | `0xecb6...2b00` | `SHORT` | 1,804,971.55 USD | `245,768.30` | `7.23` | `7.34` | `135.35` | -28,611.45 USD | `-1.59%` | `10X Cross` |
| `1312` | `0xf472...5d8b` | `LONG` | 1,772,313.47 USD | `241,374.10` | `4.44` | `7.34` | `0.000000` | 699,670.19 USD | `+39.48%` | `5X Cross` |
| `1440` | `0xb5b3...7a08` | `LONG` | 1,616,560.00 USD | `220,000.00` | `7.36` | `7.34` | `0.000000` | -3,650.15 USD | `-0.23%` | `10X Cross` |
| `1531` | `0x645b...87b8` | `SHORT` | 1,489,739.96 USD | `202,567.20` | `8.57` | `7.34` | `95.95` | 246,790.07 USD | `+16.57%` | `10X Cross` |
| `1548` | `0xcac1...26b3` | `SHORT` | 1,471,313.53 USD | `200,336.80` | `7.76` | `7.34` | `44.45` | 82,534.45 USD | `+5.61%` | `10X Cross` |
| `1674` | `0x265e...7f70` | `LONG` | 1,329,318.68 USD | `180,665.50` | `7.54` | `7.34` | `0.000000` | -33,336.07 USD | `-2.51%` | `3X Cross` |
| `1676` | `0x12d2...f97f` | `LONG` | 1,327,077.85 USD | `180,697.40` | `8.85` | `7.34` | `0.000000` | -272,842.05 USD | `-20.56%` | `10X Cross` |
| `1682` | `0x51f6...2b39` | `SHORT` | 1,322,658.76 USD | `180,147.20` | `7.35` | `7.34` | `16.04` | 1,693.85 USD | `+0.13%` | `10X Cross` |
| `1757` | `0xb83d...6e36` | `SHORT` | 1,241,193.38 USD | `168,971.00` | `7.45` | `7.34` | `721.61` | 16,908.85 USD | `+1.36%` | `3X Cross` |
| `1872` | `0xdf95...7d72` | `SHORT` | 1,148,217.93 USD | `156,343.50` | `6.56` | `7.34` | `227.11` | -121,924.87 USD | `-10.62%` | `10X Cross` |
| `1913` | `0xcb84...52cd` | `SHORT` | 1,106,364.22 USD | `150,519.60` | `7.14` | `7.34` | `19.87` | -31,056.62 USD | `-2.81%` | `10X Cross` |
| `1940` | `0xa23d...bf71` | `LONG` | 1,084,140.36 USD | `147,660.80` | `7.66` | `7.34` | `5.62` | -46,534.99 USD | `-4.29%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `7.25` | 8,082.97 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 8.08K USD at 7.2493 USD [API] | `2026-10-08 15:23:23` |
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
  * 24H Horizon: Short MP=`7.43` (Vol: 470,100.00 USD, Dist: `+2.56%`) | Long MP=`6.91` (Vol: 353,400.00 USD, Dist: `--4.62%`)
  * 48H Horizon: Short MP=`7.43` (Vol: 404,800.00 USD, Dist: `+2.56%`) | Long MP=`6.91` (Vol: 378,300.00 USD, Dist: `--4.62%`)
  * 3D Horizon: Short MP=`7.35` (Vol: 437,300.00 USD, Dist: `+1.48%`) | Long MP=`6.91` (Vol: 643,300.00 USD, Dist: `--4.62%`)
  * 7D Horizon: Short MP=`7.43` (Vol: 619,800.00 USD, Dist: `+2.58%`) | Long MP=`6.91` (Vol: 661,400.00 USD, Dist: `--4.58%`)
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
  * Current Rate: `28.68K` | Last 24h: `66.11K` | Last 3d: `148.54K` | Last 7d: `245.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0056%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0084%` |
| **CoinM Binance** | `0.0006%` | **CoinM OKX** | `0.0100%` |

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
| `5:00 UTC` | `7.28` | `7.30` | `7.28` | `7.33` | `7.26` | 2,958,524.45 USD | 1,500,754.88 USD | 1,457,769.57 USD | 42,985.31 USD | `+1.45%` | `10B / 5S` |
| `0:00 UTC` | `7.36` | `7.33` | `7.36` | `7.39` | `7.26` | 3,643,534.57 USD | 1,978,385.00 USD | 1,665,149.56 USD | 313,235.44 USD | `+8.60%` | `35B / 16S` |
| `5:00 UTC` | `7.37` | `7.36` | `7.37` | `7.39` | `7.34` | 3,735,951.80 USD | 1,862,529.96 USD | 1,873,421.84 USD | -10,891.88 USD | `-0.29%` | `4B / 5S` |
| `0:00 UTC` | `7.39` | `7.39` | `7.39` | `7.42` | `7.35` | 4,002,802.67 USD | 1,789,628.72 USD | 2,213,173.96 USD | -423,545.24 USD | `-10.58%` | `6B / 7S` |
| `5:00 UTC` | `7.40` | `7.40` | `7.40` | `7.42` | `7.37` | 2,730,635.21 USD | 1,260,988.93 USD | 1,469,646.29 USD | -208,657.36 USD | `-7.64%` | `5B / 6S` |
| `0:00 UTC` | `7.50` | `7.47` | `7.50` | `7.52` | `7.37` | 7,276,216.74 USD | 4,552,149.99 USD | 2,724,066.75 USD | 1,828,083.24 USD | `+25.12%` | `47B / 11S` |
| `5:00 UTC` | `7.45` | `7.44` | `7.45` | `7.48` | `7.41` | 4,064,958.66 USD | 1,436,607.98 USD | 2,628,350.68 USD | -1,191,742.70 USD | `-29.32%` | `7B / 15S` |
| `0:00 UTC` | `7.42` | `7.39` | `7.42` | `7.43` | `7.35` | 3,574,044.16 USD | 1,480,242.42 USD | 2,093,801.73 USD | -613,559.31 USD | `-17.17%` | `4B / 16S` |
| `5:00 UTC` | `7.38` | `7.38` | `7.38` | `7.39` | `7.35` | 1,324,026.23 USD | 564,857.55 USD | 759,168.68 USD | -194,311.13 USD | `-14.68%` | `2B / 13S` |
| `0:00 UTC` | `7.34` | `7.35` | `7.34` | `7.38` | `7.34` | 1,488,934.04 USD | 555,349.97 USD | 933,584.07 USD | -378,234.10 USD | `-25.40%` | `1B / 9S` |

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
| `5m` | -3,330.00 USD | -334,190.00 USD | **`DISTRIBUTION`** |
| `15m` | -58,430.00 USD | -566,080.00 USD | **`DISTRIBUTION`** |
| `30m` | 412,070.00 USD | -1,200,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,190,000.00 USD | -1,090,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,420,000.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,470,000.00 USD | -1,990,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,650,000.00 USD | -2,530,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 1,670,000.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 1,500,000.00 USD | -4,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 3,370,000.00 USD | -10,410,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,770,000.00 USD | -46,180,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -40,550,000.00 USD | -473,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.33K` | 15m=`-58.43K` | 1h=`+1.19M` | 24h=`+3.37M`
* Futures Capital Netflows: 5m=`-334.19K` | 15m=`-566.08K` | 1h=`-1.09M` | 24h=`-10.41M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.81` (Risk Distance: `0.1187` pts)
  * +2.5R Take Profit: `7.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7.24` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.35` (Risk Distance: `0.1187` pts)
  * +2.5R Take Profit: `6.94`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`7.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
