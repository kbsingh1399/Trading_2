# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:30:40 IST` (`2026-10-29 21:00:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.66` | **Live Ask Quote**: `6.68` | **Mid Price**: `6.67`
- **Spread Points**: `25.00` | **Spread BPS**: `37.49 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `7.13` | VWAP Z-Score: `-3.30` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0907` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `15.08` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.59` | Lower -3.00σ Band: `6.67`
  * Upper +2.51σ Band: `7.51` | Lower -2.51σ Band: `6.75`
  * Upper +2.01σ Band: `7.44` | Lower -2.01σ Band: `6.83`
  * Upper +2.00σ Band: `7.44` | Lower -2.00σ Band: `6.83`
  * Upper +1.28σ Band: `7.33` | Lower -1.28σ Band: `6.94`
  * Upper +1.00σ Band: `7.28` | Lower -1.00σ Band: `6.98`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7.03` | EMA-20=`7.13` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7.16` (Slope: `+0.0000`) | EMA-100=`7.14`
  * Institutional Anchors: EMA-144=`7.13` | EMA-200=`7.12` (Slope: `-0.0230`) | EMA-233=`7.11`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.60` | Weekly High=`7.50` | Weekly Low=`6.60`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7.32` (Distance: `-8.86%`)
  * Point of Control (POC) = `7.16` (Distance: `-6.88%`)
  * Value Area Low (VAL) = `6.99` (Distance: `-4.62%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.18` | POC=`7.05` | VAL=`7.03`
  * Prior Day Extremes: PDH=`7.32` | PDL=`6.95` | PDC=`7.22`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.18` | Weekly POC=`7.05` | Weekly VAL=`6.94`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`7.33` | Low=`6.89`
  * London Session (08:00-16:00 UTC): High=`7.22` | Low=`6.95`
  * New York Session (13:00-21:00 UTC): High=`7.50` | Low=`7.00`
  * Initial Balance (First Hour): IB High=`7.12` | IB Low=`7.02`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.64` - `6.70`
  * Optimal Trade Entry (OTE 0.705): `6.68`
  * Structural Invalidation Anchor (0.786): `6.72`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `347` | `0x5396...8b79` | `LONG` | 6,663,498.67 USD | `999,999.80` | `6.88` | `6.63` | `5.66` | -217,199.66 USD | `-3.26%` | `5X Cross` |
| `759` | `0x9df2...c665` | `SHORT` | 2,984,535.00 USD | `450,000.00` | `4.49` | `6.63` | `74.19` | -963,534.87 USD | `-32.28%` | `10X Cross` |
| `935` | `0xdd53...2b13` | `SHORT` | 2,382,151.05 USD | `358,110.50` | `7.28` | `6.63` | `173.01` | 225,480.21 USD | `+9.47%` | `3X Cross` |
| `1008` | `0xbf6d...ecc0` | `LONG` | 2,209,735.90 USD | `331,662.70` | `7.64` | `6.63` | `4.88` | -324,277.98 USD | `-14.67%` | `10X Cross` |
| `1075` | `0xcd21...9826` | `LONG` | 2,049,599.16 USD | `290,326.30` | `7.85` | `6.63` | `5.04` | -230,083.14 USD | `-11.23%` | `10X Cross` |
| `1125` | `0xb46b...538e` | `SHORT` | 1,987,740.00 USD | `300,000.00` | `8.20` | `6.63` | `21.31` | 472,044.42 USD | `+23.75%` | `10X Cross` |
| `1211` | `0xf21d...3b2d` | `LONG` | 1,853,429.51 USD | `262,384.20` | `4.28` | `6.63` | `4.06` | 730,611.67 USD | `+39.42%` | `10X Isolated` |
| `1267` | `0x9aa5...58af` | `SHORT` | 1,782,166.34 USD | `252,320.70` | `7.34` | `6.63` | `37.94` | 69,999.72 USD | `+3.93%` | `10X Cross` |
| `1332` | `0xf472...5d8b` | `LONG` | 1,659,760.72 USD | `241,374.10` | `4.44` | `6.63` | `0.000000` | 587,117.45 USD | `+35.37%` | `5X Cross` |
| `1451` | `0xb5b3...7a08` | `LONG` | 1,541,606.00 USD | `220,000.00` | `7.36` | `6.63` | `1.49` | -78,604.15 USD | `-5.10%` | `10X Cross` |
| `1484` | `0xecb6...2b00` | `SHORT` | 1,499,595.56 USD | `226,422.40` | `7.21` | `6.63` | `120.82` | 132,526.24 USD | `+8.84%` | `10X Cross` |
| `1620` | `0xcac1...26b3` | `SHORT` | 1,334,483.49 USD | `200,336.80` | `7.76` | `6.63` | `48.03` | 219,364.48 USD | `+16.44%` | `10X Cross` |
| `1626` | `0x645b...87b8` | `SHORT` | 1,325,802.25 USD | `199,545.80` | `8.57` | `6.63` | `107.21` | 384,826.49 USD | `+29.03%` | `10X Cross` |
| `1682` | `0x265e...7f70` | `LONG` | 1,266,085.76 USD | `180,665.50` | `7.54` | `6.63` | `0.000000` | -96,568.99 USD | `-7.63%` | `3X Cross` |
| `1742` | `0x12d2...f97f` | `LONG` | 1,203,715.73 USD | `180,697.40` | `8.85` | `6.63` | `0.000000` | -396,204.17 USD | `-32.92%` | `10X Cross` |
| `1757` | `0x51f6...2b39` | `SHORT` | 1,191,629.98 USD | `179,670.70` | `7.35` | `6.63` | `15.62` | 129,219.64 USD | `+10.84%` | `10X Cross` |
| `1787` | `0xb83d...6e36` | `SHORT` | 1,161,253.20 USD | `168,971.00` | `7.45` | `6.63` | `817.24` | 96,849.03 USD | `+8.34%` | `3X Cross` |
| `1933` | `0xdf95...7d72` | `SHORT` | 1,035,489.49 USD | `156,347.50` | `6.56` | `6.63` | `254.39` | -9,168.99 USD | `-0.89%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `6.67` | 3,243.01 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.24K USD at 6.6660 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 6,007.09 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 6.01K USD at 6.6664 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 1,000.76 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 1.00K USD at 6.6673 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 114.68 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.11K USD at 6.6676 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 500.11 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.50K USD at 6.6681 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 7,506.28 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 7.51K USD at 6.6681 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 585.47 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.59K USD at 6.6682 USD [API] | `2026-10-24 14:17:02` |
| `ANNOUNCEMENT` | `INFO` | `7.55` | 2,640.23 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 2.64K USD at 7.5500 USD [API] | `2026-10-08 12:46:59` |
| `ANNOUNCEMENT` | `INFO` | `7.55` | 135.91 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.14K USD at 7.5503 USD [API] | `2026-10-08 12:46:59` |
| `ANNOUNCEMENT` | `INFO` | `9.08` | 69.91 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.07K USD at 9.0788 USD [API] | `2026-09-29 08:17:06` |
| `ANNOUNCEMENT` | `INFO` | `9.30` | 134.85 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.13K USD at 9.3000 USD [API] | `2026-09-24 14:25:55` |
| `ANNOUNCEMENT` | `INFO` | `8.68` | 638.05 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.64K USD at 8.6810 USD [API] | `2026-09-21 18:31:52` |
| `ANNOUNCEMENT` | `INFO` | `9.04` | 1,469.75 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.47K USD at 9.0446 USD [API] | `2026-09-21 09:17:14` |
| `ANNOUNCEMENT` | `INFO` | `8.32` | 9,400.22 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 9.40K USD at 8.3151 USD [API] | `2026-10-07 01:35:44` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+7.21%`) | Long MP=`6.89` (Vol: 228,900.00 USD, Dist: `--2.50%`)
  * 48H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+7.21%`) | Long MP=`6.91` (Vol: 378,300.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+7.21%`) | Long MP=`6.91` (Vol: 537,300.00 USD, Dist: `--2.29%`)
  * 7D Horizon: Short MP=`7.61` (Vol: 392,700.00 USD, Dist: `+7.62%`) | Long MP=`6.90` (Vol: 565,900.00 USD, Dist: `--2.46%`)
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
  * Current Rate: `-3.48K` | Last 24h: `66.11K` | Last 3d: `148.58K` | Last 7d: `245.37K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `0.0040%` |
| **USDT Bybit** | `-0.0155%` | **USDT KuCoin** | `-0.0083%` |
| **USDT MEXC** | `0.0019%` | **USDT BingX** | `0.0045%` |
| **USDT Gate** | `-0.0075%` | **USDT Bitget** | `0.0006%` |
| **CoinM Binance** | `-0.0052%` | **CoinM OKX** | `0.0100%` |

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
| `0:00 UTC` | `7.17` | `7.18` | `7.17` | `7.22` | `7.16` | 3,597,323.95 USD | 1,700,383.25 USD | 1,896,940.71 USD | -196,557.46 USD | `-5.46%` | `4B / 12S` |
| `5:00 UTC` | `7.16` | `7.18` | `7.16` | `7.21` | `7.15` | 2,196,425.29 USD | 1,064,538.01 USD | 1,131,887.28 USD | -67,349.27 USD | `-3.07%` | `19B / 4S` |
| `0:00 UTC` | `7.17` | `7.17` | `7.17` | `7.19` | `7.15` | 1,134,824.79 USD | 719,458.28 USD | 415,366.51 USD | 304,091.78 USD | `+26.80%` | `8B / 1S` |
| `5:00 UTC` | `7.17` | `7.16` | `7.17` | `7.18` | `7.15` | 1,021,800.59 USD | 474,808.50 USD | 546,992.09 USD | -72,183.59 USD | `-7.06%` | `10B / 9S` |
| `0:00 UTC` | `7.19` | `7.18` | `7.19` | `7.20` | `7.16` | 1,186,980.52 USD | 673,356.83 USD | 513,623.68 USD | 159,733.15 USD | `+13.46%` | `7B / 4S` |
| `5:00 UTC` | `7.17` | `7.17` | `7.17` | `7.19` | `7.16` | 858,297.55 USD | 532,157.34 USD | 326,140.21 USD | 206,017.13 USD | `+24.00%` | `12B / 2S` |
| `0:00 UTC` | `7.04` | `7.07` | `7.04` | `7.18` | `7.00` | 7,778,114.56 USD | 3,383,167.15 USD | 4,394,947.42 USD | -1,011,780.27 USD | `-13.01%` | `9B / 40S` |
| `5:00 UTC` | `7.07` | `7.07` | `7.07` | `7.09` | `7.05` | 2,718,151.99 USD | 1,546,820.47 USD | 1,171,331.52 USD | 375,488.95 USD | `+13.81%` | `12B / 0S` |
| `0:00 UTC` | `6.85` | `6.82` | `6.85` | `7.08` | `6.60` | 29,256,795.21 USD | 12,783,224.59 USD | 16,473,570.62 USD | -3,690,346.03 USD | `-12.61%` | `1B / 25S` |
| `5:00 UTC` | `6.60` | `6.60` | `6.60` | `6.72` | `6.48` | 13,748,084.37 USD | 6,704,596.75 USD | 7,043,487.61 USD | -338,890.86 USD | `-2.47%` | `2B / 9S` |

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
| `5m` | -149,660.00 USD | 1,380,000.00 USD | **`ACCUMULATION`** |
| `15m` | -216,440.00 USD | -2,990,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,760,000.00 USD | -7,080,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,280,000.00 USD | -8,300,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,150,000.00 USD | -6,880,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,640,000.00 USD | -9,730,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,140,000.00 USD | -8,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,220,000.00 USD | -11,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,050,000.00 USD | -12,380,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,580,000.00 USD | -22,720,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,150,000.00 USD | -56,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -45,310,000.00 USD | -486,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-149.66K` | 15m=`-216.44K` | 1h=`-2.28M` | 24h=`-1.58M`
* Futures Capital Netflows: 5m=`+1.38M` | 15m=`-2.99M` | 1h=`-8.30M` | 24h=`-22.72M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.85` (Risk Distance: `0.1463` pts)
  * +2.5R Take Profit: `7.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.47` (Risk Distance: `0.1463` pts)
  * +2.5R Take Profit: `6.95`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.72`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
