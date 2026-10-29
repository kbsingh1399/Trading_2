# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 04:28:57 IST` (`2026-10-29 22:58:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.62` | **Live Ask Quote**: `66.66` | **Mid Price**: `66.64`
- **Spread Points**: `37.00` | **Spread BPS**: `5.55 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `52.72` | VWAP Z-Score: `-1.34` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1747` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.59` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.35` | Lower -3.00σ Band: `51.10`
  * Upper +2.51σ Band: `54.08` | Lower -2.51σ Band: `51.36`
  * Upper +2.01σ Band: `53.81` | Lower -2.01σ Band: `51.64`
  * Upper +2.00σ Band: `53.80` | Lower -2.00σ Band: `51.64`
  * Upper +1.28σ Band: `53.42` | Lower -1.28σ Band: `52.03`
  * Upper +1.00σ Band: `53.26` | Lower -1.00σ Band: `52.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.12` | EMA-20=`52.18` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.40` (Slope: `+0.0000`) | EMA-100=`52.74`
  * Institutional Anchors: EMA-144=`52.95` | EMA-200=`53.13` (Slope: `-0.2364`) | EMA-233=`53.22`
- **Range Boundaries**: 24H High=`54.37` | 24H Low=`51.93` | Weekly High=`54.61` | Weekly Low=`51.93`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.13` (Distance: `-0.07%`)
  * Point of Control (POC) = `52.02` (Distance: `+0.14%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.19%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.48` | Weekly POC=`53.87` | Weekly VAL=`53.16`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.93`
  * London Session (08:00-16:00 UTC): High=`66.91` | Low=`66.38`
  * New York Session (13:00-21:00 UTC): High=`67.04` | Low=`66.24`
  * Initial Balance (First Hour): IB High=`66.84` | IB Low=`66.44`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.38` - `66.91`
  * Optimal Trade Entry (OTE 0.705): `66.78`
  * Structural Invalidation Anchor (0.786): `67.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.05` | `52.11` | `52.05` | `52.11` | `527` | 27,460.92 USD | 23,696.11 USD | `+86.29%` | -760,993.14 USD | `+0.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.11` | `52.18` | `52.11` | `52.14` | `619` | 32,274.04 USD | 5,302.16 USD | `+16.43%` | -755,690.98 USD | `+0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.14` | `52.18` | `52.08` | `52.11` | `710` | 37,000.94 USD | -10,464.91 USD | `-28.28%` | -766,155.89 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.08` | `52.10` | `51.99` | `52.00` | `2,318` | 120,533.68 USD | -96,314.30 USD | `-79.91%` | -1,964,057.16 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.00` | `52.18` | `51.98` | `52.14` | `1,888` | 98,438.43 USD | 64,520.53 USD | `+65.54%` | -1,899,536.64 USD | `+0.84` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.14` | `52.18` | `52.08` | `52.13` | `1,989` | 103,682.59 USD | -7,331.09 USD | `-7.07%` | -1,906,867.73 USD | `+0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -2,335,773.51 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.01` | `52.12` | `51.95` | `52.08` | `9,961` | 518,719.08 USD | 235,233.07 USD | `+45.35%` | -2,100,540.44 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.08` | `52.36` | `51.98` | `52.35` | `8,673` | 454,014.20 USD | 384,260.00 USD | `+84.64%` | -1,716,280.44 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,894,512.32 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -3,185,036.74 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,982,960.46 USD | `345,023.32` | `58.92` | `52.12` | `585.18` | 2,346,400.89 USD | `+13.05%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,196,662.25 USD | `310,751.18` | `53.23` | `52.12` | `251.86` | 345,830.66 USD | `+2.14%` | `5X Cross` |
| `203` | `0xacb6...efbd` | `SHORT` | 10,483,069.16 USD | `201,133.33` | `59.63` | `52.12` | `76.44` | 1,509,587.96 USD | `+14.40%` | `6X Cross` |
| `209` | `0x49e9...e1d0` | `SHORT` | 10,263,473.95 USD | `196,916.29` | `55.51` | `52.12` | `94.63` | 666,937.08 USD | `+6.50%` | `4X Cross` |
| `236` | `0xc26c...b8f4` | `LONG` | 9,458,054.39 USD | `181,463.41` | `55.43` | `52.12` | `0.000000` | -600,700.69 USD | `-6.35%` | `2X Cross` |
| `349` | `0x645b...87b8` | `LONG` | 6,592,639.35 USD | `126,487.20` | `56.63` | `52.12` | `0.000000` | -570,069.31 USD | `-8.65%` | `3X Cross` |
| `350` | `0xd8c5...99b0` | `SHORT` | 6,583,926.80 USD | `126,320.04` | `61.98` | `52.12` | `199.57` | 1,245,411.04 USD | `+18.92%` | `3X Cross` |
| `391` | `0xe9ff...5903` | `SHORT` | 5,889,468.69 USD | `112,996.08` | `60.07` | `52.12` | `200.07` | 898,482.12 USD | `+15.26%` | `5X Cross` |
| `602` | `0x9aa5...58af` | `LONG` | 3,713,136.33 USD | `71,243.43` | `61.59` | `52.12` | `0.000000` | -675,021.20 USD | `-18.18%` | `20X Cross` |
| `724` | `0x2056...8396` | `LONG` | 3,127,140.00 USD | `60,000.00` | `66.92` | `52.12` | `21.34` | -888,187.14 USD | `-28.40%` | `10X Cross` |
| `859` | `0x0242...ffa1` | `SHORT` | 2,601,706.76 USD | `49,916.67` | `56.48` | `52.12` | `350.97` | 217,425.11 USD | `+8.36%` | `10X Cross` |
| `868` | `0x960b...f0fc` | `LONG` | 2,577,798.33 USD | `49,457.96` | `55.82` | `52.12` | `0.000000` | -183,138.70 USD | `-7.10%` | `25X Cross` |
| `961` | `0x8b9d...7b28` | `LONG` | 2,336,244.08 USD | `44,823.47` | `58.35` | `52.12` | `0.000000` | -279,204.46 USD | `-11.95%` | `10X Cross` |
| `1047` | `0x5647...e7de` | `LONG` | 2,098,459.09 USD | `40,262.07` | `57.38` | `52.12` | `0.000000` | -211,778.51 USD | `-10.09%` | `20X Cross` |
| `1056` | `0xa2ce...3126` | `LONG` | 2,084,840.00 USD | `40,000.00` | `74.30` | `52.12` | `0.000000` | -887,215.49 USD | `-42.56%` | `20X Cross` |
| `1075` | `0xb078...de15` | `SHORT` | 2,032,719.52 USD | `39,000.01` | `52.58` | `52.12` | `195.20` | 17,799.43 USD | `+0.88%` | `8X Cross` |
| `1407` | `0x5a88...d997` | `LONG` | 1,563,630.00 USD | `30,000.00` | `59.50` | `52.12` | `41.13` | -221,257.59 USD | `-14.15%` | `25X Cross` |
| `1408` | `0x3678...b209` | `LONG` | 1,563,630.00 USD | `30,000.00` | `57.15` | `52.12` | `0.000000` | -150,870.00 USD | `-9.65%` | `20X Cross` |
| `1461` | `0xfc66...ca06` | `SHORT` | 1,499,062.41 USD | `28,761.75` | `54.61` | `52.12` | `538.45` | 71,505.35 USD | `+4.77%` | `7X Cross` |
| `1640` | `0x7ea9...fc7f` | `LONG` | 1,303,025.00 USD | `25,000.00` | `53.60` | `52.12` | `30.09` | -36,979.05 USD | `-2.84%` | `25X Cross` |
| `1768` | `0xf517...c032` | `LONG` | 1,179,322.67 USD | `22,627.50` | `66.29` | `52.12` | `0.000000` | -320,672.43 USD | `-27.19%` | `20X Cross` |
| `1893` | `0xcc9f...d218` | `LONG` | 1,069,533.67 USD | `20,520.60` | `52.63` | `52.12` | `26.86` | -10,374.38 USD | `-0.97%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `65.51` | 14,313.28 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 14.31K USD at 65.5130 USD [API] | `2026-09-04 12:30:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`52.72` (Vol: 3,200,000.00 USD, Dist: `+0.87%`) | Long MP=`51.68` (Vol: 3,900,000.00 USD, Dist: `--1.11%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.40%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.11%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.40%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.58%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.91%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.58%`)
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
  * Current Rate: `10.74K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.73` (Risk Distance: `0.2651` pts)
  * +2.5R Take Profit: `52.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.13` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.39` (Risk Distance: `0.2651` pts)
  * +2.5R Take Profit: `51.47`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
