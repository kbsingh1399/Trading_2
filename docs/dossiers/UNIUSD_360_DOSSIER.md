# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 07:36:17 IST` (`2026-10-30 02:06:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.48` | **Live Ask Quote**: `6.51` | **Mid Price**: `6.50`
- **Spread Points**: `26.00` | **Spread BPS**: `40.03 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.96` | VWAP Z-Score: `-1.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1313` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `31.82` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.91` | Lower -3.00σ Band: `6.02`
  * Upper +2.51σ Band: `7.76` | Lower -2.51σ Band: `6.17`
  * Upper +2.01σ Band: `7.60` | Lower -2.01σ Band: `6.33`
  * Upper +2.00σ Band: `7.60` | Lower -2.00σ Band: `6.33`
  * Upper +1.28σ Band: `7.37` | Lower -1.28σ Band: `6.56`
  * Upper +1.00σ Band: `7.28` | Lower -1.00σ Band: `6.65`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.50` | EMA-20=`6.69` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.92` (Slope: `+0.0000`) | EMA-100=`7.01`
  * Institutional Anchors: EMA-144=`7.04` | EMA-200=`7.05` (Slope: `-0.9730`) | EMA-233=`7.06`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.53` (Distance: `-0.53%`)
  * Point of Control (POC) = `6.46` (Distance: `+0.62%`)
  * Value Area Low (VAL) = `6.35` (Distance: `+2.34%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.22` | Weekly POC=`7.05` | Weekly VAL=`6.91`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.52` | Low=`6.47`
  * New York Session (13:00-21:00 UTC): High=`6.53` | Low=`6.46`
  * Initial Balance (First Hour): IB High=`6.51` | IB Low=`6.48`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.47` - `6.52`
  * Optimal Trade Entry (OTE 0.705): `6.51`
  * Structural Invalidation Anchor (0.786): `6.55`

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
| --- | **`6.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `344` | `0x5396...8b79` | `LONG` | 6,507,898.70 USD | `999,999.80` | `6.88` | `6.56` | `5.66` | -372,799.62 USD | `-5.73%` | `5X Cross` |
| `761` | `0x9df2...c665` | `SHORT` | 2,945,655.00 USD | `450,000.00` | `4.49` | `6.56` | `77.95` | -924,654.87 USD | `-31.39%` | `10X Cross` |
| `821` | `0xecb6...2b00` | `SHORT` | 2,695,382.33 USD | `411,766.50` | `6.63` | `6.56` | `76.90` | 34,897.89 USD | `+1.29%` | `10X Cross` |
| `844` | `0xbf6d...ecc0` | `LONG` | 2,632,655.33 USD | `404,134.80` | `7.42` | `6.56` | `5.10` | -366,768.26 USD | `-13.93%` | `10X Cross` |
| `882` | `0xcd21...9826` | `LONG` | 2,506,674.13 USD | `382,990.70` | `7.52` | `6.56` | `5.31` | -373,005.99 USD | `-14.88%` | `10X Cross` |
| `964` | `0x60a8...85f6` | `SHORT` | 2,279,531.12 USD | `348,238.00` | `6.48` | `6.56` | `55.33` | -22,178.88 USD | `-0.97%` | `10X Cross` |
| `995` | `0xdd53...2b13` | `SHORT` | 2,168,806.22 USD | `331,155.90` | `7.28` | `6.56` | `202.39` | 241,800.08 USD | `+11.15%` | `3X Cross` |
| `1096` | `0xb46b...538e` | `SHORT` | 1,958,160.00 USD | `300,000.00` | `8.20` | `6.56` | `22.54` | 501,624.42 USD | `+25.62%` | `10X Cross` |
| `1246` | `0xf21d...3b2d` | `LONG` | 1,737,586.60 USD | `265,479.00` | `4.32` | `6.56` | `4.10` | 591,327.58 USD | `+34.03%` | `10X Isolated` |
| `1338` | `0xf472...5d8b` | `LONG` | 1,578,586.61 USD | `241,374.10` | `4.44` | `6.56` | `0.000000` | 505,943.34 USD | `+32.05%` | `5X Cross` |
| `1468` | `0xb5b3...7a08` | `LONG` | 1,440,113.40 USD | `220,000.00` | `7.36` | `6.56` | `1.95` | -180,096.75 USD | `-12.51%` | `10X Cross` |
| `1537` | `0x265e...7f70` | `LONG` | 1,379,016.36 USD | `210,665.50` | `7.39` | `6.56` | `0.000000` | -178,316.83 USD | `-12.93%` | `3X Cross` |
| `1588` | `0xcac1...26b3` | `SHORT` | 1,308,479.78 USD | `200,336.80` | `7.76` | `6.56` | `51.55` | 245,368.20 USD | `+18.75%` | `10X Cross` |
| `1591` | `0x9aa5...58af` | `SHORT` | 1,305,910.40 USD | `199,518.80` | `7.34` | `6.56` | `54.40` | 158,662.06 USD | `+12.15%` | `10X Cross` |
| `1719` | `0x12d2...f97f` | `LONG` | 1,181,182.76 USD | `180,697.40` | `8.85` | `6.56` | `0.000000` | -418,737.13 USD | `-35.45%` | `10X Cross` |
| `1770` | `0x645b...87b8` | `SHORT` | 1,136,724.87 USD | `173,670.40` | `8.57` | `6.56` | `136.53` | 352,084.10 USD | `+30.97%` | `10X Cross` |
| `1800` | `0x51f6...2b39` | `SHORT` | 1,110,173.51 USD | `169,598.30` | `7.30` | `6.56` | `14.40` | 127,318.94 USD | `+11.47%` | `10X Cross` |
| `1805` | `0xb83d...6e36` | `SHORT` | 1,104,985.85 USD | `168,971.00` | `7.45` | `6.56` | `846.58` | 153,116.37 USD | `+13.86%` | `3X Cross` |
| `1899` | `0x7cee...fc93` | `SHORT` | 1,024,714.82 USD | `156,543.00` | `6.88` | `6.56` | `24.89` | 52,474.95 USD | `+5.12%` | `5X Cross` |
| `1921` | `0xdf95...7d72` | `SHORT` | 1,013,378.01 USD | `154,714.20` | `6.56` | `6.56` | `260.67` | 2,219.45 USD | `+0.22%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 48H Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 3D Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 7D Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
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
  * Current Rate: `27.79K` | Last 24h: `53.94K` | Last 3d: `142.67K` | Last 7d: `259.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `6.49` | `6.48` | `6.49` | `6.52` | `6.45` | 5,870,358.50 USD | 2,583,580.54 USD | 3,286,777.96 USD | -703,197.42 USD | `-11.98%` | `1B / 8S` |
| `5:00 UTC` | `6.47` | `6.48` | `6.47` | `6.51` | `6.43` | 6,029,172.30 USD | 2,718,609.12 USD | 3,310,563.18 USD | -591,954.05 USD | `-9.82%` | `2B / 9S` |
| `0:00 UTC` | `6.46` | `6.46` | `6.46` | `6.50` | `6.43` | 7,714,315.60 USD | 3,882,377.81 USD | 3,831,937.79 USD | 50,440.02 USD | `+0.65%` | `1B / 1S` |
| `5:00 UTC` | `6.33` | `6.37` | `6.33` | `6.51` | `6.25` | 21,731,536.36 USD | 9,271,035.82 USD | 12,460,500.54 USD | -3,189,464.71 USD | `-14.68%` | `3B / 10S` |
| `0:00 UTC` | `6.42` | `6.36` | `6.42` | `6.44` | `6.26` | 10,203,831.59 USD | 4,743,342.97 USD | 5,460,488.62 USD | -717,145.66 USD | `-7.03%` | `6B / 14S` |
| `5:00 UTC` | `6.49` | `6.47` | `6.49` | `6.52` | `6.39` | 10,332,566.01 USD | 6,083,569.00 USD | 4,248,997.01 USD | 1,834,571.99 USD | `+17.76%` | `31B / 4S` |
| `0:00 UTC` | `6.52` | `6.48` | `6.52` | `6.55` | `6.41` | 7,350,422.21 USD | 3,756,137.60 USD | 3,594,284.62 USD | 161,852.98 USD | `+2.20%` | `10B / 21S` |
| `5:00 UTC` | `6.50` | `6.52` | `6.50` | `6.56` | `6.48` | 5,770,145.58 USD | 2,140,624.21 USD | 3,629,521.37 USD | -1,488,897.17 USD | `-25.80%` | `4B / 15S` |
| `0:00 UTC` | `6.55` | `6.52` | `6.55` | `6.58` | `6.44` | 5,592,794.96 USD | 2,688,660.61 USD | 2,904,134.35 USD | -215,473.74 USD | `-3.85%` | `7B / 23S` |
| `5:00 UTC` | `6.48` | `6.49` | `6.48` | `6.56` | `6.45` | 3,285,328.36 USD | 1,268,218.37 USD | 2,017,109.99 USD | -748,891.62 USD | `-22.80%` | `4B / 23S` |

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
| `5m` | 1,190,000.00 USD | 921,140.00 USD | **`ACCUMULATION`** |
| `15m` | 404,250.00 USD | 79,540.00 USD | **`ACCUMULATION`** |
| `30m` | 119,500.00 USD | 96,120.00 USD | **`ACCUMULATION`** |
| `1h` | -462,380.00 USD | -106,500.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,580,000.00 USD | -2,790,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -6,050,000.00 USD | -21,550,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -10,750,000.00 USD | -38,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,970,000.00 USD | -40,480,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,490,000.00 USD | -37,220,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,150,000.00 USD | -46,530,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,710,000.00 USD | -86,850,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,390,000.00 USD | -507,880,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.19M` | 15m=`+404.25K` | 1h=`-462.38K` | 24h=`-11.15M`
* Futures Capital Netflows: 5m=`+921.14K` | 15m=`+79.54K` | 1h=`-106.50K` | 24h=`-46.53M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.15` (Risk Distance: `0.1966` pts)
  * +2.5R Take Profit: `6.84`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.73` (Risk Distance: `0.1966` pts)
  * +2.5R Take Profit: `6.04`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
