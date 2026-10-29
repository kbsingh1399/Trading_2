# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:55:35 IST` (`2026-10-29 22:25:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.41` | **Live Ask Quote**: `6.43` | **Mid Price**: `6.42`
- **Spread Points**: `23.00` | **Spread BPS**: `35.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.42` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `6.46` | Lower -3.00σ Band: `6.37`
  * Upper +2.51σ Band: `6.45` | Lower -2.51σ Band: `6.38`
  * Upper +2.01σ Band: `6.44` | Lower -2.01σ Band: `6.39`
  * Upper +2.00σ Band: `6.44` | Lower -2.00σ Band: `6.39`
  * Upper +1.28σ Band: `6.43` | Lower -1.28σ Band: `6.40`
  * Upper +1.00σ Band: `6.43` | Lower -1.00σ Band: `6.40`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.42` | EMA-20=`6.42` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.42` (Slope: `+0.0000`) | EMA-100=`6.42`
  * Institutional Anchors: EMA-144=`6.42` | EMA-200=`6.42` (Slope: `+0.0000`) | EMA-233=`6.42`
- **Range Boundaries**: 24H High=`6.48` | 24H Low=`6.35` | Weekly High=`6.54` | Weekly Low=`6.29`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.65` (Distance: `-3.11%`)
  * Point of Control (POC) = `6.34` (Distance: `+1.58%`)
  * Value Area Low (VAL) = `6.24` (Distance: `+3.29%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.18` | Weekly POC=`7.05` | Weekly VAL=`6.93`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.44` | Low=`6.39`
  * New York Session (13:00-21:00 UTC): High=`6.45` | Low=`6.38`
  * Initial Balance (First Hour): IB High=`6.44` | IB Low=`6.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.39` - `6.44`
  * Optimal Trade Entry (OTE 0.705): `6.43`
  * Structural Invalidation Anchor (0.786): `6.47`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `365` | `0x5396...8b79` | `LONG` | 6,422,708.72 USD | `999,999.80` | `6.88` | `6.38` | `5.66` | -457,989.61 USD | `-7.13%` | `5X Cross` |
| `789` | `0x9df2...c665` | `SHORT` | 2,880,090.00 USD | `450,000.00` | `4.49` | `6.38` | `75.50` | -859,089.87 USD | `-29.83%` | `10X Cross` |
| `855` | `0x60a8...85f6` | `SHORT` | 2,625,763.00 USD | `410,000.00` | `6.48` | `6.38` | `46.89` | 31,943.57 USD | `+1.22%` | `10X Cross` |
| `871` | `0xbf6d...ecc0` | `LONG` | 2,597,536.01 USD | `404,134.80` | `7.42` | `6.38` | `5.19` | -401,887.57 USD | `-15.47%` | `10X Cross` |
| `932` | `0xcd21...9826` | `LONG` | 2,425,441.80 USD | `382,990.70` | `7.52` | `6.38` | `5.42` | -454,238.31 USD | `-18.73%` | `10X Cross` |
| `1038` | `0xdd53...2b13` | `SHORT` | 2,126,426.07 USD | `332,238.50` | `7.28` | `6.38` | `190.29` | 292,060.87 USD | `+13.73%` | `3X Cross` |
| `1164` | `0xb46b...538e` | `SHORT` | 1,920,000.00 USD | `300,000.00` | `8.20` | `6.38` | `21.73` | 539,784.42 USD | `+28.11%` | `10X Cross` |
| `1325` | `0xf21d...3b2d` | `LONG` | 1,665,402.86 USD | `265,479.00` | `4.32` | `6.38` | `4.10` | 519,143.84 USD | `+31.17%` | `10X Isolated` |
| `1352` | `0x9aa5...58af` | `SHORT` | 1,640,109.78 USD | `252,320.70` | `7.34` | `6.38` | `41.34` | 212,056.28 USD | `+12.93%` | `10X Cross` |
| `1438` | `0xf472...5d8b` | `LONG` | 1,544,070.12 USD | `241,374.10` | `4.44` | `6.38` | `0.000000` | 471,426.84 USD | `+30.53%` | `5X Cross` |
| `1578` | `0xb5b3...7a08` | `LONG` | 1,379,961.00 USD | `220,000.00` | `7.36` | `6.38` | `2.00` | -240,249.15 USD | `-17.41%` | `10X Cross` |
| `1655` | `0xcac1...26b3` | `SHORT` | 1,287,644.75 USD | `200,336.80` | `7.76` | `6.38` | `49.09` | 266,203.23 USD | `+20.67%` | `10X Cross` |
| `1684` | `0xecb6...2b00` | `SHORT` | 1,256,187.75 USD | `199,439.20` | `6.80` | `6.38` | `146.70` | 99,999.56 USD | `+7.96%` | `10X Cross` |
| `1782` | `0x12d2...f97f` | `LONG` | 1,158,722.08 USD | `180,697.40` | `8.85` | `6.38` | `0.000000` | -441,197.82 USD | `-38.08%` | `10X Cross` |
| `1811` | `0x265e...7f70` | `LONG` | 1,132,555.89 USD | `180,665.50` | `7.54` | `6.38` | `0.000000` | -230,098.87 USD | `-20.32%` | `3X Cross` |
| `1829` | `0x645b...87b8` | `SHORT` | 1,120,779.55 USD | `175,211.60` | `8.57` | `6.38` | `125.71` | 381,241.53 USD | `+34.02%` | `10X Cross` |
| `1880` | `0xb83d...6e36` | `SHORT` | 1,082,140.98 USD | `168,971.00` | `7.45` | `6.38` | `872.81` | 175,961.25 USD | `+16.26%` | `3X Cross` |
| `1939` | `0x51f6...2b39` | `SHORT` | 1,027,724.84 USD | `160,785.50` | `7.34` | `6.38` | `16.48` | 152,335.43 USD | `+14.82%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 423,200.00 USD, Dist: `+17.95%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`6.68` (Vol: 533,600.00 USD, Dist: `+4.05%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`6.68` (Vol: 577,600.00 USD, Dist: `+4.05%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`6.76` (Vol: 446,900.00 USD, Dist: `+5.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
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
  * Current Rate: `-13.02K` | Last 24h: `66.11K` | Last 3d: `148.58K` | Last 7d: `245.37K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0041%` | **USDT OKX** | `-0.0021%` |
| **USDT Bybit** | `-0.0137%` | **USDT KuCoin** | `-0.0075%` |
| **USDT MEXC** | `-0.0040%` | **USDT BingX** | `-0.0019%` |
| **USDT Gate** | `-0.0042%` | **USDT Bitget** | `-0.0069%` |
| **CoinM Binance** | `0.0067%` | **CoinM OKX** | `0.0040%` |

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
| `0:00 UTC` | `7.04` | `7.07` | `7.04` | `7.18` | `7.00` | 7,778,114.56 USD | 3,383,167.15 USD | 4,394,947.42 USD | -1,011,780.27 USD | `-13.01%` | `9B / 40S` |
| `5:00 UTC` | `7.07` | `7.07` | `7.07` | `7.09` | `7.05` | 2,718,151.99 USD | 1,546,820.47 USD | 1,171,331.52 USD | 375,488.95 USD | `+13.81%` | `12B / 0S` |
| `0:00 UTC` | `6.85` | `6.82` | `6.85` | `7.08` | `6.60` | 29,256,795.21 USD | 12,783,224.59 USD | 16,473,570.62 USD | -3,690,346.03 USD | `-12.61%` | `1B / 25S` |
| `5:00 UTC` | `6.60` | `6.61` | `6.60` | `6.72` | `6.48` | 19,730,963.97 USD | 10,096,604.97 USD | 9,634,359.00 USD | 462,245.96 USD | `+2.34%` | `1B / 9S` |
| `0:00 UTC` | `6.69` | `6.65` | `6.69` | `6.72` | `6.56` | 12,306,886.81 USD | 6,652,493.57 USD | 5,654,393.24 USD | 998,100.33 USD | `+8.11%` | `11B / 9S` |
| `5:00 UTC` | `6.79` | `6.75` | `6.79` | `6.82` | `6.68` | 8,815,257.34 USD | 4,612,494.62 USD | 4,202,762.72 USD | 409,731.90 USD | `+4.65%` | `15B / 8S` |
| `0:00 UTC` | `6.77` | `6.74` | `6.77` | `6.79` | `6.64` | 6,411,655.15 USD | 2,728,448.47 USD | 3,683,206.68 USD | -954,758.21 USD | `-14.89%` | `21B / 30S` |
| `5:00 UTC` | `6.47` | `6.50` | `6.47` | `6.67` | `6.35` | 31,415,495.29 USD | 11,741,221.34 USD | 19,674,273.95 USD | -7,933,052.62 USD | `-25.25%` | `1B / 39S` |
| `0:00 UTC` | `6.28` | `6.35` | `6.28` | `6.49` | `6.25` | 56,914,501.13 USD | 27,583,787.93 USD | 29,330,713.20 USD | -1,746,925.28 USD | `-3.07%` | `6B / 3S` |
| `5:00 UTC` | `6.42` | `6.43` | `6.42` | `6.50` | `6.36` | 13,848,839.50 USD | 6,464,776.61 USD | 7,384,062.89 USD | -919,286.28 USD | `-6.64%` | `7B / 19S` |

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
  * `2026-10-30 03:30:02 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:54:02 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:51:02 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:02 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `5.00` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `9.32`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7.88` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.56`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
