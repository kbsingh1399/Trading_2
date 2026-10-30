# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:05:59 IST` (`2026-10-30 09:35:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.68` | **Live Ask Quote**: `6.70` | **Mid Price**: `6.69`
- **Spread Points**: `25.00` | **Spread BPS**: `37.37 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.59` | VWAP Z-Score: `+0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0662` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `48.82` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.02` | Lower -3.00σ Band: `6.16`
  * Upper +2.51σ Band: `6.95` | Lower -2.51σ Band: `6.23`
  * Upper +2.01σ Band: `6.88` | Lower -2.01σ Band: `6.30`
  * Upper +2.00σ Band: `6.88` | Lower -2.00σ Band: `6.31`
  * Upper +1.28σ Band: `6.78` | Lower -1.28σ Band: `6.41`
  * Upper +1.00σ Band: `6.74` | Lower -1.00σ Band: `6.45`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.69` | EMA-20=`6.70` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.73` (Slope: `+0.0000`) | EMA-100=`6.82`
  * Institutional Anchors: EMA-144=`6.88` | EMA-200=`6.92` (Slope: `-0.4113`) | EMA-233=`6.94`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.66` (Distance: `+0.36%`)
  * Point of Control (POC) = `6.46` (Distance: `+3.50%`)
  * Value Area Low (VAL) = `6.25` (Distance: `+7.05%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.26` | Weekly POC=`7.05` | Weekly VAL=`6.87`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.85` | Low=`6.64`
  * New York Session (13:00-21:00 UTC): High=`6.73` | Low=`6.65`
  * Initial Balance (First Hour): IB High=`6.85` | IB Low=`6.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.66` - `6.72`
  * Optimal Trade Entry (OTE 0.705): `6.70`
  * Structural Invalidation Anchor (0.786): `6.74`

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
| --- | **`6.69`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `334` | `0x5396...8b79` | `LONG` | 6,709,988.66 USD | `999,999.80` | `6.88` | `6.70` | `5.66` | -170,709.67 USD | `-2.54%` | `5X Cross` |
| `756` | `0x9df2...c665` | `SHORT` | 3,017,520.00 USD | `450,000.00` | `4.49` | `6.70` | `74.50` | -996,519.87 USD | `-33.02%` | `10X Cross` |
| `809` | `0xecb6...2b00` | `SHORT` | 2,815,915.10 USD | `419,740.80` | `6.64` | `6.70` | `78.58` | -30,684.89 USD | `-1.09%` | `10X Cross` |
| `822` | `0xbf6d...ecc0` | `LONG` | 2,758,970.68 USD | `411,412.10` | `7.41` | `6.70` | `5.18` | -290,452.32 USD | `-10.53%` | `10X Cross` |
| `861` | `0xcd21...9826` | `LONG` | 2,618,450.59 USD | `390,271.80` | `7.51` | `6.70` | `5.38` | -311,228.84 USD | `-11.89%` | `10X Cross` |
| `997` | `0xdd53...2b13` | `SHORT` | 2,219,473.07 USD | `331,155.90` | `7.28` | `6.70` | `187.89` | 191,133.23 USD | `+8.61%` | `3X Cross` |
| `1089` | `0xb46b...538e` | `SHORT` | 2,010,660.00 USD | `300,000.00` | `8.20` | `6.70` | `20.83` | 449,124.42 USD | `+22.34%` | `10X Cross` |
| `1172` | `0x60a8...85f6` | `SHORT` | 1,891,148.42 USD | `282,067.30` | `6.48` | `6.70` | `65.96` | -62,728.63 USD | `-3.32%` | `10X Cross` |
| `1243` | `0xf21d...3b2d` | `LONG` | 1,781,178.25 USD | `265,479.00` | `4.32` | `6.70` | `4.10` | 634,919.23 USD | `+35.65%` | `10X Isolated` |
| `1334` | `0xf472...5d8b` | `LONG` | 1,617,882.32 USD | `241,374.10` | `4.44` | `6.70` | `0.000000` | 545,239.04 USD | `+33.70%` | `5X Cross` |
| `1470` | `0xb5b3...7a08` | `LONG` | 1,473,758.00 USD | `220,000.00` | `7.36` | `6.70` | `1.82` | -146,452.15 USD | `-9.94%` | `10X Cross` |
| `1522` | `0x265e...7f70` | `LONG` | 1,412,322.58 USD | `210,665.50` | `7.39` | `6.70` | `0.000000` | -145,010.61 USD | `-10.27%` | `3X Cross` |
| `1588` | `0xcac1...26b3` | `SHORT` | 1,343,999.49 USD | `200,336.80` | `7.76` | `6.70` | `49.48` | 209,848.48 USD | `+15.61%` | `10X Cross` |
| `1731` | `0x12d2...f97f` | `LONG` | 1,211,178.53 USD | `180,697.40` | `8.85` | `6.70` | `0.000000` | -388,741.36 USD | `-32.10%` | `10X Cross` |
| `1762` | `0x7cee...fc93` | `SHORT` | 1,176,626.77 USD | `175,532.10` | `6.84` | `6.70` | `21.78` | 23,862.66 USD | `+2.03%` | `5X Cross` |
| `1811` | `0x645b...87b8` | `SHORT` | 1,146,779.81 USD | `170,939.20` | `8.57` | `6.70` | `132.45` | 318,615.64 USD | `+27.78%` | `10X Cross` |
| `1824` | `0x51f6...2b39` | `SHORT` | 1,137,025.36 USD | `169,485.20` | `7.30` | `6.70` | `14.01` | 99,641.85 USD | `+8.76%` | `10X Cross` |
| `1830` | `0xb83d...6e36` | `SHORT` | 1,133,339.19 USD | `168,971.00` | `7.45` | `6.70` | `675.63` | 124,763.04 USD | `+11.01%` | `3X Cross` |
| `1935` | `0xdf95...7d72` | `SHORT` | 1,036,888.62 USD | `154,558.80` | `6.56` | `6.70` | `250.65` | -22,311.26 USD | `-2.15%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `7.16` | 960.02 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.96K USD at 7.1643 USD [API] | `2026-10-26 15:10:36` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 3,706.21 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.71K USD at 6.8532 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 3,708.27 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 3.71K USD at 6.8532 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.32 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8533 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.33 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8534 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.33 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8534 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.34 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8535 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.36 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8536 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.37 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8537 USD [API] | `2026-10-23 22:51:50` |
| `ANNOUNCEMENT` | `INFO` | `6.85` | 966.39 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.97K USD at 6.8538 USD [API] | `2026-10-23 22:51:50` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+13.35%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--5.40%`)
  * 48H Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+6.18%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--5.40%`)
  * 3D Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+6.18%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--5.40%`)
  * 7D Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+6.18%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--5.40%`)
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
  * Current Rate: `24.96K` | Last 24h: `48.59K` | Last 3d: `131.97K` | Last 7d: `247.30K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0071%` | **USDT KuCoin** | `0.0093%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0095%` | **USDT Bitget** | `0.0015%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

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
| `0:00 UTC` | `6.81` | `6.79` | `6.81` | `6.83` | `6.75` | 2,972,960.85 USD | 1,512,195.93 USD | 1,460,764.92 USD | 51,431.01 USD | `+1.73%` | `9B / 20S` |
| `5:00 UTC` | `6.76` | `6.75` | `6.76` | `6.77` | `6.74` | 1,239,699.80 USD | 499,379.40 USD | 740,320.40 USD | -240,941.00 USD | `-19.44%` | `1B / 7S` |
| `0:00 UTC` | `6.73` | `6.71` | `6.73` | `6.77` | `6.66` | 3,255,523.56 USD | 1,227,814.01 USD | 2,027,709.55 USD | -799,895.54 USD | `-24.57%` | `8B / 47S` |
| `5:00 UTC` | `6.69` | `6.70` | `6.69` | `6.73` | `6.67` | 3,274,506.44 USD | 1,781,957.77 USD | 1,492,548.68 USD | 289,409.09 USD | `+8.84%` | `9B / 6S` |
| `0:00 UTC` | `6.68` | `6.69` | `6.68` | `6.71` | `6.66` | 2,334,317.24 USD | 1,277,056.29 USD | 1,057,260.95 USD | 219,795.35 USD | `+9.42%` | `7B / 4S` |
| `5:00 UTC` | `6.71` | `6.72` | `6.71` | `6.74` | `6.70` | 1,972,150.91 USD | 1,143,502.79 USD | 828,648.12 USD | 314,854.67 USD | `+15.97%` | `7B / 1S` |
| `0:00 UTC` | `6.70` | `6.70` | `6.70` | `6.72` | `6.68` | 1,603,540.26 USD | 838,217.11 USD | 765,323.15 USD | 72,893.96 USD | `+4.55%` | `6B / 4S` |
| `5:00 UTC` | `6.70` | `6.72` | `6.70` | `6.75` | `6.69` | 1,521,221.36 USD | 767,404.45 USD | 753,816.91 USD | 13,587.54 USD | `+0.89%` | `14B / 4S` |
| `0:00 UTC` | `6.73` | `6.73` | `6.73` | `6.76` | `6.69` | 1,774,118.48 USD | 1,147,816.84 USD | 626,301.63 USD | 521,515.21 USD | `+29.40%` | `14B / 3S` |
| `5:00 UTC` | `6.69` | `6.69` | `6.69` | `6.72` | `6.67` | 1,553,279.73 USD | 866,978.57 USD | 686,301.16 USD | 180,677.42 USD | `+11.63%` | `5B / 5S` |

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
| `5m` | -66,320.00 USD | -24,300.00 USD | **`DISTRIBUTION`** |
| `15m` | -329,590.00 USD | -160,790.00 USD | **`DISTRIBUTION`** |
| `30m` | -78,750.00 USD | 287,820.00 USD | **`ACCUMULATION`** |
| `1h` | 126,440.00 USD | 1,450,000.00 USD | **`ACCUMULATION`** |
| `2h` | 291,750.00 USD | 1,190,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,020,000.00 USD | 731,990.00 USD | **`ACCUMULATION`** |
| `6h` | 1,600,000.00 USD | 1,950,000.00 USD | **`ACCUMULATION`** |
| `8h` | -919,310.00 USD | -1,790,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,310,000.00 USD | -29,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,630,000.00 USD | -41,650,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -18,410,000.00 USD | -78,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,120,000.00 USD | -500,180,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-66.32K` | 15m=`-329.59K` | 1h=`+126.44K` | 24h=`-11.63M`
* Futures Capital Netflows: 5m=`-24.30K` | 15m=`-160.79K` | 1h=`+1.45M` | 24h=`-41.65M`
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
  * `2026-10-30 14:41:20 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:20 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.13` (Risk Distance: `0.1169` pts)
  * +2.5R Take Profit: `6.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.66` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.78` (Risk Distance: `0.1169` pts)
  * +2.5R Take Profit: `6.37`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.74`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
