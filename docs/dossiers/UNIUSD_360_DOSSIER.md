# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `7.20` | **Live Ask Quote**: `7.23` | **Mid Price**: `7.21`
- **Spread Points**: `23.00` | **Spread BPS**: `31.88 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `7.08` | VWAP Z-Score: `+0.91` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0546` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `57.04` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.37` | Lower -3.00σ Band: `6.78`
  * Upper +2.51σ Band: `7.32` | Lower -2.51σ Band: `6.83`
  * Upper +2.01σ Band: `7.28` | Lower -2.01σ Band: `6.88`
  * Upper +2.00σ Band: `7.27` | Lower -2.00σ Band: `6.88`
  * Upper +1.28σ Band: `7.20` | Lower -1.28σ Band: `6.95`
  * Upper +1.00σ Band: `7.18` | Lower -1.00σ Band: `6.98`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7.16` | EMA-20=`7.13` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7.10` (Slope: `+0.0000`) | EMA-100=`7.09`
  * Institutional Anchors: EMA-144=`7.09` | EMA-200=`7.08` (Slope: `+0.1500`) | EMA-233=`7.08`
- **Range Boundaries**: 24H High=`7.33` | 24H Low=`6.89` | Weekly High=`7.33` | Weekly Low=`6.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7.19` (Distance: `+0.32%`)
  * Point of Control (POC) = `7.01` (Distance: `+2.95%`)
  * Value Area Low (VAL) = `6.92` (Distance: `+4.16%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.18` | POC=`7.05` | VAL=`7.03`
  * Prior Day Extremes: PDH=`7.32` | PDL=`6.95` | PDC=`7.22`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.17` | Weekly POC=`7.04` | Weekly VAL=`6.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`7.33` | Low=`6.89`
  * London Session (08:00-16:00 UTC): High=`7.22` | Low=`6.95`
  * New York Session (13:00-21:00 UTC): High=`7.25` | Low=`7.00`
  * Initial Balance (First Hour): IB High=`7.12` | IB Low=`7.02`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `7.19` - `7.24`
  * Optimal Trade Entry (OTE 0.705): `7.23`
  * Structural Invalidation Anchor (0.786): `7.27`

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
| --- | **`7.21`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `340` | `0x5396...8b79` | `LONG` | 7,217,298.56 USD | `999,999.80` | `6.88` | `7.21` | `5.66` | 336,600.23 USD | `+4.66%` | `5X Cross` |
| `710` | `0x9df2...c665` | `SHORT` | 3,248,325.00 USD | `450,000.00` | `4.49` | `7.21` | `70.97` | -1,227,324.87 USD | `-37.78%` | `10X Cross` |
| `885` | `0xdd53...2b13` | `SHORT` | 2,595,395.21 USD | `359,478.00` | `7.29` | `7.21` | `159.90` | 24,109.27 USD | `+0.93%` | `3X Cross` |
| `982` | `0xbf6d...ecc0` | `LONG` | 2,334,826.07 USD | `323,266.70` | `7.78` | `7.21` | `5.00` | -180,020.01 USD | `-7.71%` | `10X Cross` |
| `1001` | `0xcd21...9826` | `LONG` | 2,293,412.62 USD | `317,576.80` | `7.85` | `7.21` | `5.29` | -200,244.38 USD | `-8.73%` | `10X Cross` |
| `1046` | `0xb46b...538e` | `SHORT` | 2,166,540.00 USD | `300,000.00` | `8.20` | `7.21` | `19.69` | 293,244.42 USD | `+13.54%` | `10X Cross` |
| `1220` | `0xf21d...3b2d` | `LONG` | 1,894,833.74 USD | `262,384.20` | `4.28` | `7.21` | `4.06` | 772,015.90 USD | `+40.74%` | `10X Isolated` |
| `1265` | `0x9aa5...58af` | `SHORT` | 1,820,064.91 USD | `252,320.70` | `7.34` | `7.21` | `37.51` | 32,101.16 USD | `+1.76%` | `10X Cross` |
| `1315` | `0xecb6...2b00` | `SHORT` | 1,744,691.96 USD | `241,697.30` | `7.22` | `7.21` | `110.90` | 789.61 USD | `+0.05%` | `10X Cross` |
| `1316` | `0xf472...5d8b` | `LONG` | 1,742,093.43 USD | `241,374.10` | `4.44` | `7.21` | `0.000000` | 669,450.15 USD | `+38.43%` | `5X Cross` |
| `1440` | `0xb5b3...7a08` | `LONG` | 1,586,926.00 USD | `220,000.00` | `7.36` | `7.21` | `0.000000` | -33,284.15 USD | `-2.10%` | `10X Cross` |
| `1532` | `0x645b...87b8` | `SHORT` | 1,468,046.18 USD | `203,257.30` | `8.57` | `7.21` | `101.18` | 274,590.32 USD | `+18.70%` | `10X Cross` |
| `1553` | `0xcac1...26b3` | `SHORT` | 1,446,952.57 USD | `200,336.80` | `7.76` | `7.21` | `46.09` | 106,895.40 USD | `+7.39%` | `10X Cross` |
| `1676` | `0x12d2...f97f` | `LONG` | 1,304,617.16 USD | `180,697.40` | `8.85` | `7.21` | `0.000000` | -295,302.74 USD | `-22.64%` | `10X Cross` |
| `1677` | `0x265e...7f70` | `LONG` | 1,304,115.85 USD | `180,665.50` | `7.54` | `7.21` | `0.000000` | -58,538.91 USD | `-4.49%` | `3X Cross` |
| `1683` | `0x51f6...2b39` | `SHORT` | 1,301,336.58 USD | `180,195.60` | `7.35` | `7.21` | `16.80` | 23,408.34 USD | `+1.80%` | `10X Cross` |
| `1759` | `0xb83d...6e36` | `SHORT` | 1,219,717.16 USD | `168,971.00` | `7.45` | `7.21` | `666.37` | 38,385.06 USD | `+3.15%` | `3X Cross` |
| `1869` | `0xdf95...7d72` | `SHORT` | 1,128,570.00 USD | `156,313.80` | `6.56` | `7.21` | `227.66` | -102,528.98 USD | `-9.08%` | `10X Cross` |
| `1925` | `0xcb84...52cd` | `SHORT` | 1,086,510.68 USD | `150,519.60` | `7.14` | `7.21` | `20.64` | -11,203.09 USD | `-1.03%` | `10X Cross` |
| `1952` | `0xa23d...bf71` | `LONG` | 1,065,933.78 USD | `147,660.80` | `7.66` | `7.21` | `5.62` | -64,741.56 USD | `-6.07%` | `10X Cross` |
| `1961` | `0x7cee...fc93` | `SHORT` | 1,057,670.99 USD | `146,496.90` | `6.99` | `7.21` | `36.33` | -34,086.42 USD | `-3.22%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `7.25` | 8,082.97 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 8.08K USD at 7.2493 USD [API] | `2026-10-08 15:23:23` |


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
  * Current Rate: `21.71K` | Last 24h: `60.93K` | Last 3d: `140.85K` | Last 7d: `214.96K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0001%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0037%` | **USDT Bitget** | `0.0026%` |
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
| `5:00 UTC` | `7.20` | `7.21` | `7.20` | `7.24` | `7.18` | 3,784,986.44 USD | 1,909,635.61 USD | 1,875,350.83 USD | 34,284.78 USD | `+0.91%` | `10B / 8S` |
| `0:00 UTC` | `7.16` | `7.16` | `7.16` | `7.19` | `7.15` | 1,612,972.79 USD | 653,864.07 USD | 959,108.72 USD | -305,244.66 USD | `-18.92%` | `4B / 8S` |
| `5:00 UTC` | `7.20` | `7.19` | `7.20` | `7.21` | `7.16` | 1,458,372.64 USD | 783,946.92 USD | 674,425.72 USD | 109,521.21 USD | `+7.51%` | `8B / 2S` |
| `0:00 UTC` | `7.22` | `7.21` | `7.22` | `7.24` | `7.18` | 2,478,774.40 USD | 1,346,387.62 USD | 1,132,386.79 USD | 214,000.83 USD | `+8.63%` | `6B / 6S` |
| `5:00 UTC` | `7.20` | `7.20` | `7.20` | `7.23` | `7.18` | 1,892,867.27 USD | 816,322.58 USD | 1,076,544.69 USD | -260,222.11 USD | `-13.75%` | `4B / 9S` |
| `0:00 UTC` | `7.24` | `7.24` | `7.24` | `7.26` | `7.21` | 2,167,822.07 USD | 1,054,110.53 USD | 1,113,711.53 USD | -59,601.00 USD | `-2.75%` | `4B / 10S` |
| `5:00 UTC` | `7.23` | `7.23` | `7.23` | `7.27` | `7.21` | 3,028,324.39 USD | 1,455,722.40 USD | 1,572,601.99 USD | -116,879.59 USD | `-3.86%` | `8B / 12S` |
| `0:00 UTC` | `7.16` | `7.17` | `7.16` | `7.23` | `7.11` | 9,805,300.63 USD | 3,190,839.84 USD | 6,614,460.79 USD | -3,423,620.95 USD | `-34.92%` | `4B / 41S` |
| `5:00 UTC` | `7.18` | `7.17` | `7.18` | `7.21` | `7.14` | 2,879,839.60 USD | 1,707,408.53 USD | 1,172,431.08 USD | 534,977.45 USD | `+18.58%` | `20B / 3S` |
| `0:00 UTC` | `7.20` | `7.20` | `7.20` | `7.22` | `7.18` | 1,351,066.39 USD | 695,594.09 USD | 655,472.30 USD | 40,121.79 USD | `+2.97%` | `2B / 3S` |

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
| `5m` | 135,740.00 USD | -68,610.00 USD | **`ACCUMULATION`** |
| `15m` | 93,010.00 USD | 126,900.00 USD | **`ACCUMULATION`** |
| `30m` | 369,850.00 USD | 1,390,000.00 USD | **`ACCUMULATION`** |
| `1h` | -42,660.00 USD | -3,990,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -95,770.00 USD | -3,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 464,760.00 USD | -4,520,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 23,380.00 USD | -4,360,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 85,720.00 USD | -6,140,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -163,100.00 USD | -7,690,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 2,280,000.00 USD | -12,600,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,430,000.00 USD | -56,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -44,670,000.00 USD | -484,600,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+135.74K` | 15m=`+93.01K` | 1h=`-42.66K` | 24h=`+2.28M`
* Futures Capital Netflows: 5m=`-68.61K` | 15m=`+126.90K` | 1h=`-3.99M` | 24h=`-12.60M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `6.82` (Risk Distance: `0.1001` pts)
  * +2.5R Take Profit: `7.18`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7.19` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.29` (Risk Distance: `0.1001` pts)
  * +2.5R Take Profit: `6.94`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`7.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
