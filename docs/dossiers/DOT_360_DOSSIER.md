# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:28:57 IST` (`2026-10-29 22:58:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9110` | **Live Ask Quote**: `0.9320` | **Mid Price**: `0.9215`
- **Spread Points**: `21.00` | **Spread BPS**: `227.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9607` | VWAP Z-Score: `-1.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0129` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.61` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.05` | Lower -3.00σ Band: `0.8705`
  * Upper +2.51σ Band: `1.04` | Lower -2.51σ Band: `0.8852`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.9002`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.9005`
  * Upper +1.28σ Band: `0.9992` | Lower -1.28σ Band: `0.9222`
  * Upper +1.00σ Band: `0.9908` | Lower -1.00σ Band: `0.9306`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9213` | EMA-20=`0.9389` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9594` (Slope: `+0.0000`) | EMA-100=`0.9701`
  * Institutional Anchors: EMA-144=`0.9743` | EMA-200=`0.9768` (Slope: `-0.6733`) | EMA-233=`0.9788`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8800` | Weekly High=`1.03` | Weekly Low=`0.8800`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9213` (Distance: `+0.08%`)
  * Point of Control (POC) = `0.9149` (Distance: `+0.77%`)
  * Value Area Low (VAL) = `0.9108` (Distance: `+1.24%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9932` | Weekly VAL=`0.9751`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.9030`
  * London Session (08:00-16:00 UTC): High=`0.9252` | Low=`0.9178`
  * New York Session (13:00-21:00 UTC): High=`0.9270` | Low=`0.9160`
  * Initial Balance (First Hour): IB High=`0.9243` | IB Low=`0.9187`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9178` - `0.9252`
  * Optimal Trade Entry (OTE 0.705): `0.9233`
  * Structural Invalidation Anchor (0.786): `0.9289`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9282` | `0.9325` | `0.9278` | `0.9314` | `346,940` | 322,828.27 USD | 79,933.94 USD | `+24.76%` | -4,325,952.99 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9314` | `0.9327` | `0.9251` | `0.9252` | `494,774` | 460,337.56 USD | -43,006.64 USD | `-9.34%` | -4,368,959.63 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9253` | `0.9294` | `0.9237` | `0.9286` | `300,419` | 278,373.98 USD | 26,335.83 USD | `+9.46%` | -4,342,623.79 USD | `+0.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9232` | `0.9288` | `0.9142` | `0.9248` | `2,151,446` | 1,982,933.95 USD | 178,609.02 USD | `+9.01%` | -4,499,569.13 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9249` | `0.9327` | `0.9200` | `0.9252` | `1,261,322` | 1,171,136.75 USD | 91,279.80 USD | `+7.79%` | -4,408,289.34 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9253` | `0.9294` | `0.9237` | `0.9286` | `300,419` | 278,373.98 USD | 26,335.83 USD | `+9.46%` | -4,381,953.51 USD | `+0.45` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.9845` | `0.9849` | `0.8892` | `0.9107` | `25,741,782` | 23,981,753.25 USD | -3,181,821.86 USD | `-13.27%` | -3,433,243.38 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9106` | `0.9391` | `0.9075` | `0.9232` | `9,308,289` | 8,622,274.03 USD | -1,228,979.98 USD | `-14.25%` | -4,662,223.36 USD | `-1.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9232` | `0.9327` | `0.9142` | `0.9286` | `3,713,186` | 3,432,444.68 USD | 296,224.65 USD | `+8.63%` | -4,365,998.71 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9286` | `38,763,257` | 36,036,471.95 USD | -4,114,577.19 USD | `-11.42%` | -4,395,136.51 USD | `-2.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9286` | `38,763,257` | 36,036,471.95 USD | -4,114,577.19 USD | `-11.42%` | -4,395,136.51 USD | `-2.16` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9215`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9461` (Vol: 248,700.00 USD, Dist: `+2.36%`) | Long MP=`0.9083` (Vol: 248,700.00 USD, Dist: `--1.73%`)
  * 48H Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.38%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.71%`)
  * 3D Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.38%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.71%`)
  * 7D Horizon: Short MP=`0.9460` (Vol: 248,700.00 USD, Dist: `+2.35%`) | Long MP=`0.9102` (Vol: 172,900.00 USD, Dist: `--1.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2285` | 114.25 USD | 350,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3475` | 140.29 USD | 350,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3555` | 785.30 USD | 350,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 30,490.00 USD | 349,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 319,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,390.00 USD | 316,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4365` | 1,090.00 USD | 313,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 1,350.00 USD | 312,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 311,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 29,070.00 USD | 308,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 279,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 279,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 211.93 USD | 275,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 274,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 274,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 273,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 273,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 1,030.00 USD | 270,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 269,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 266,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 265,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 264,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6275` | 200.36 USD | 264,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 264,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 263,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 263,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 261,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 362.05 USD | 241,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 20,920.00 USD | 240,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 220,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 576.71 USD | 219,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 219,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 219,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 629.33 USD | 155,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 154,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 154,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 153,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 152,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 136,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 135,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 133,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 133,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 132,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 3,030.00 USD | 131,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 128,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 127,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 127,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 126,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 125,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 169.23 USD | 125,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 125,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 804.07 USD | 124,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 54,780.00 USD | 123,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 68,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 1,010.00 USD | 65,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 234.45 USD | 64,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 63,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,180,000.00 USD | 2,180,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,170,000.00 USD | 2,170,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,150,000.00 USD | 2,150,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,120,000.00 USD | 2,120,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 301.32 USD | 63,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,100,000.00 USD | 2,100,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 2,080,000.00 USD | 2,080,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 2,040,000.00 USD | 2,040,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 63,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 2,030,000.00 USD | 2,030,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 2,010,000.00 USD | 2,010,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,990,000.00 USD | 1,990,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 13,380.00 USD | 62,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,970,000.00 USD | 1,970,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,960,000.00 USD | 1,960,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8130` | 1,420,000.00 USD | 1,420,000.00 USD | 878.33 USD | 138.33 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,950,000.00 USD | 1,950,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 49,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 1,420,000.00 USD | 1,420,000.00 USD | 2,620.00 USD | 191.37 USD | 26.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,930,000.00 USD | 1,930,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8170` | 1,420,000.00 USD | 1,420,000.00 USD | 9,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,910,000.00 USD | 1,910,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,890,000.00 USD | 1,890,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,870,000.00 USD | 1,870,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 48,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,490.00 USD | 880.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,850,000.00 USD | 1,850,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 46,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 1,410,000.00 USD | 1,410,000.00 USD | 8,060.00 USD | 5,240.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 1,810,000.00 USD | 1,810,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8270` | 1,390,000.00 USD | 1,390,000.00 USD | 244.70 USD | 2,830.00 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 1,800,000.00 USD | 1,800,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8290` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 40.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 1,380,000.00 USD | 1,380,000.00 USD | 163.37 USD | 1,760.00 USD | 442.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 1,790,000.00 USD | 1,790,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 1,380,000.00 USD | 1,380,000.00 USD | 25,550.00 USD | 2,130.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 1,780,000.00 USD | 1,780,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8350` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 3,440.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 1,750,000.00 USD | 1,750,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 1,330,000.00 USD | 1,330,000.00 USD | 9,580.00 USD | 1,900.00 USD | 9,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,730,000.00 USD | 1,730,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 1,310,000.00 USD | 1,310,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,710,000.00 USD | 1,710,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 45,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,700,000.00 USD | 1,700,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 1,310,000.00 USD | 1,310,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,690,000.00 USD | 1,690,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,680,000.00 USD | 1,680,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 44,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 1,310,000.00 USD | 1,310,000.00 USD | 421.90 USD | 2,000.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,680,000.00 USD | 1,680,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,670,000.00 USD | 1,670,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 1,310,000.00 USD | 1,310,000.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,660,000.00 USD | 1,660,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 1,300,000.00 USD | 1,300,000.00 USD | 366.87 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 43,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 1,300,000.00 USD | 1,300,000.00 USD | 3,490.00 USD | 1,100.00 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 127.01 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8610` | 1,300,000.00 USD | 1,300,000.00 USD | 7,350.00 USD | 128.03 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,650,000.00 USD | 1,650,000.00 USD | 7,320.00 USD | 3,160.00 USD | 467.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8630` | 1,290,000.00 USD | 1,290,000.00 USD | 3,170.00 USD | 151.21 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,640,000.00 USD | 1,640,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 42,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 42,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 1,280,000.00 USD | 1,280,000.00 USD | 6,220.00 USD | 1,930.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,640,000.00 USD | 1,640,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,270,000.00 USD | 1,270,000.00 USD | 2,930.00 USD | 1,590.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,630,000.00 USD | 1,630,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,270,000.00 USD | 1,270,000.00 USD | 14,770.00 USD | 3,820.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,610,000.00 USD | 1,610,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 41,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,240,000.00 USD | 1,240,000.00 USD | 12,380.00 USD | 1,850.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,570,000.00 USD | 1,570,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,220,000.00 USD | 1,220,000.00 USD | 30,230.00 USD | 3,080.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,180,000.00 USD | 1,180,000.00 USD | 6,210.00 USD | 2,770.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 29,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,170,000.00 USD | 1,170,000.00 USD | 33,040.00 USD | 6,750.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,540,000.00 USD | 1,540,000.00 USD | 52,140.00 USD | 16,410.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,120,000.00 USD | 1,120,000.00 USD | 34,680.00 USD | 12,000.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,470,000.00 USD | 1,470,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 28,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,050,000.00 USD | 1,050,000.00 USD | 17,760.00 USD | 18,200.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,460,000.00 USD | 1,460,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 27,450.00 USD | 28,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,010,000.00 USD | 1,010,000.00 USD | 6,980.00 USD | 4,200.00 USD | 311.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,460,000.00 USD | 1,460,000.00 USD | 8,430.00 USD | 5,730.00 USD | 957.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 549.72 USD | 549.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,000,000.00 USD | 1,000,000.00 USD | 8,900.00 USD | 5,700.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,450,000.00 USD | 1,450,000.00 USD | 8,630.00 USD | 10,630.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 978,630.00 USD | 978,630.00 USD | 19,160.00 USD | 11,410.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,430,000.00 USD | 1,430,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 937,570.00 USD | 937,570.00 USD | 67,190.00 USD | 12,700.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,390,000.00 USD | 1,390,000.00 USD | 54,380.00 USD | 29,640.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 841,570.00 USD | 841,570.00 USD | 47,930.00 USD | 13,730.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,300,000.00 USD | 1,300,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 749,840.00 USD | 749,840.00 USD | 31,260.00 USD | 11,150.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,180,000.00 USD | 1,180,000.00 USD | 62,870.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 682,680.00 USD | 682,680.00 USD | 21,170.00 USD | 3,980.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,090,000.00 USD | 1,090,000.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 653,070.00 USD | 653,070.00 USD | 25,280.00 USD | 23,820.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 999,100.00 USD | 999,100.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 559,440.00 USD | 559,440.00 USD | 76,980.00 USD | 16,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 857,400.00 USD | 857,400.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 465,050.00 USD | 465,050.00 USD | 254.26 USD | 14,150.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 762,110.00 USD | 762,110.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 448,300.00 USD | 448,300.00 USD | 5,770.00 USD | 6,910.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 727,020.00 USD | 727,020.00 USD | 13,100.00 USD | 8,710.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 431,410.00 USD | 431,410.00 USD | 0.00 USD | 15,360.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 677,750.00 USD | 677,750.00 USD | 31,190.00 USD | 13,050.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 409,890.00 USD | 409,890.00 USD | 126,150.00 USD | 23,360.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 606,210.00 USD | 606,210.00 USD | 114,070.00 USD | 49,120.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 241,550.00 USD | 241,550.00 USD | 0.00 USD | 25,080.00 USD | 55,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 427,520.00 USD | 427,520.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 160,890.00 USD | 160,890.00 USD | 50,190.00 USD | 17,990.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 309,320.00 USD | 309,320.00 USD | 76,180.00 USD | 10,780.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 46,980.00 USD | 46,980.00 USD | 0.00 USD | 3,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 205,900.00 USD | 205,900.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 43,690.00 USD | 43,690.00 USD | 0.00 USD | 168.83 USD | 19,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 147,390.00 USD | 147,390.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 24,490.00 USD | 24,490.00 USD | 0.00 USD | 132.18 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 113,650.00 USD | 113,650.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 24,360.00 USD | 24,360.00 USD | 0.00 USD | 158.23 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 98,400.00 USD | 98,400.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 24,200.00 USD | 24,200.00 USD | 0.00 USD | 118.70 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 19,190.00 USD | 19,190.00 USD | 14,160.00 USD | 556.44 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 64,140.00 USD | 64,140.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 778.79 USD | 259.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 1,670.00 USD | 1,670.00 USD | 0.00 USD | 275.97 USD | 356.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 4,600.00 USD | 4,600.00 USD | 0.00 USD | 76.32 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 66,800.00 USD | 66,800.00 USD | 38,560.00 USD | 18,340.00 USD | 5,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 216,110.00 USD | 216,110.00 USD | 123,740.00 USD | 15,750.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 768.64 USD | 768.64 USD | 0.00 USD | 0.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 288,880.00 USD | 288,880.00 USD | 45,940.00 USD | 14,450.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 18,870.00 USD | 18,870.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 348,630.00 USD | 348,630.00 USD | 53,820.00 USD | 3,310.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 67,770.00 USD | 67,770.00 USD | 39,250.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 435,750.00 USD | 435,750.00 USD | 72,250.00 USD | 11,790.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 113,900.00 USD | 113,900.00 USD | 29,630.00 USD | 9,330.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 461,000.00 USD | 461,000.00 USD | 20,020.00 USD | 5,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 171,910.00 USD | 171,910.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 688,100.00 USD | 688,100.00 USD | 190,140.00 USD | 18,130.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 553,200.00 USD | 553,200.00 USD | 261,930.00 USD | 48,260.00 USD | 71,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 889,020.00 USD | 889,020.00 USD | 120,750.00 USD | 24,600.00 USD | 55,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 830,300.00 USD | 830,300.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 1,100,000.00 USD | 1,100,000.00 USD | 147,280.00 USD | 17,390.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,210,000.00 USD | 1,210,000.00 USD | 193,040.00 USD | 10,340.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 1,180,000.00 USD | 1,180,000.00 USD | 71,040.00 USD | 6,910.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,600,000.00 USD | 1,600,000.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 1,270,000.00 USD | 1,270,000.00 USD | 25,510.00 USD | 9,810.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 1,310,000.00 USD | 1,310,000.00 USD | 11,050.00 USD | 14,910.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 1,320,000.00 USD | 1,320,000.00 USD | 865.00 USD | 0.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,760,000.00 USD | 1,760,000.00 USD | 1,910.00 USD | 0.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 3,210.00 USD | 863.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,770,000.00 USD | 1,770,000.00 USD | 1,980.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 1,330,000.00 USD | 1,330,000.00 USD | 2,830.00 USD | 7,110.00 USD | 995.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,800,000.00 USD | 1,800,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 1,420,000.00 USD | 1,420,000.00 USD | 65,790.00 USD | 9,060.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,870,000.00 USD | 1,870,000.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 1,480,000.00 USD | 1,480,000.00 USD | 489.40 USD | 21,880.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,940,000.00 USD | 1,940,000.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 1,540,000.00 USD | 1,540,000.00 USD | 25,900.00 USD | 8,780.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,980,000.00 USD | 1,980,000.00 USD | 38,090.00 USD | 5,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9685` | 211.13 USD | 211.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9690` | 1,540,000.00 USD | 1,540,000.00 USD | 490.10 USD | 1,740.00 USD | 326.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 20,550.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 2,150.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,630,000.00 USD | 1,630,000.00 USD | 40,580.00 USD | 5,170.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,060,000.00 USD | 2,060,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,690,000.00 USD | 1,690,000.00 USD | 25,830.00 USD | 11,090.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,780,000.00 USD | 1,780,000.00 USD | 76,840.00 USD | 5,950.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,170,000.00 USD | 2,170,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,840,000.00 USD | 1,840,000.00 USD | 29,240.00 USD | 9,580.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,850,000.00 USD | 1,850,000.00 USD | 366.87 USD | 376.40 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,380,000.00 USD | 2,380,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,920,000.00 USD | 1,920,000.00 USD | 15,980.00 USD | 20,710.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,550,000.00 USD | 2,550,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,980,000.00 USD | 1,980,000.00 USD | 38,840.00 USD | 4,430.00 USD | 19,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 2,010,000.00 USD | 2,010,000.00 USD | 12,080.00 USD | 3,590.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,670,000.00 USD | 2,670,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 2,060,000.00 USD | 2,060,000.00 USD | 24,170.00 USD | 0.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,690,000.00 USD | 2,690,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 2,130,000.00 USD | 2,130,000.00 USD | 51,530.00 USD | 1,520.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 216.96 USD | 428.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 2,160,000.00 USD | 2,160,000.00 USD | 15,020.00 USD | 15,930.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 2,180,000.00 USD | 2,180,000.00 USD | 16,320.00 USD | 1,630.00 USD | 329.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,800,000.00 USD | 2,800,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 2,220,000.00 USD | 2,220,000.00 USD | 33,860.00 USD | 2,480.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,870,000.00 USD | 2,870,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 2,270,000.00 USD | 2,270,000.00 USD | 33,110.00 USD | 8,690.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 156.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,340,000.00 USD | 2,340,000.00 USD | 41,520.00 USD | 23,800.00 USD | 348.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,920,000.00 USD | 2,920,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,360,000.00 USD | 2,360,000.00 USD | 10,110.00 USD | 7,370.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,070,000.00 USD | 3,070,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,420,000.00 USD | 2,420,000.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,110,000.00 USD | 3,110,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,530,000.00 USD | 2,530,000.00 USD | 47,140.00 USD | 11,580.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,170,000.00 USD | 3,170,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 25,730.00 USD | 13,790.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,190,000.00 USD | 3,190,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,610,000.00 USD | 2,610,000.00 USD | 7,620.00 USD | 26,630.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,230,000.00 USD | 3,230,000.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,630,000.00 USD | 2,630,000.00 USD | 10,040.00 USD | 4,110.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,280,000.00 USD | 3,280,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 26,240.00 USD | 6,130.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 222.21 USD | 650.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,740,000.00 USD | 2,740,000.00 USD | 1,810.00 USD | 8,510.00 USD | 24,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,360,000.00 USD | 3,360,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,820,000.00 USD | 2,820,000.00 USD | 64,920.00 USD | 4,830.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,470,000.00 USD | 3,470,000.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,880,000.00 USD | 2,880,000.00 USD | 27,370.00 USD | 5,700.00 USD | 26,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,640,000.00 USD | 3,640,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,000,000.00 USD | 3,000,000.00 USD | 63,820.00 USD | 7,600.00 USD | 49,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,950,000.00 USD | 3,950,000.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,140,000.00 USD | 3,140,000.00 USD | 68,350.00 USD | 32,010.00 USD | 37,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,070,000.00 USD | 4,070,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,190,000.00 USD | 3,190,000.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,380,000.00 USD | 4,380,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,280,000.00 USD | 3,280,000.00 USD | 30,250.00 USD | 24,670.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,470,000.00 USD | 3,470,000.00 USD | 133,770.00 USD | 17,580.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,790,000.00 USD | 4,790,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,530,000.00 USD | 3,530,000.00 USD | 38,620.00 USD | 156.67 USD | 23,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,920,000.00 USD | 4,920,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,580,000.00 USD | 3,580,000.00 USD | 22,000.00 USD | 18,470.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,230,000.00 USD | 5,230,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,630,000.00 USD | 3,630,000.00 USD | 37,490.00 USD | 4,480.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,530,000.00 USD | 5,530,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,900,000.00 USD | 5,900,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,340,000.00 USD | 6,340,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,530,000.00 USD | 6,530,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,800,000.00 USD | 6,800,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,320,000.00 USD | 7,320,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,520,000.00 USD | 7,520,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,830,000.00 USD | 7,830,000.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,030,000.00 USD | 8,030,000.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,260,000.00 USD | 8,260,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,660,000.00 USD | 8,660,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,120,000.00 USD | 9,120,000.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,680,000.00 USD | 9,680,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,890,000.00 USD | 9,890,000.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,110,000.00 USD | 10,110,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,400,000.00 USD | 10,400,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,630,000.00 USD | 10,630,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 12,350.00 USD | 13,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,870,000.00 USD | 10,870,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,060,000.00 USD | 11,060,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,210,000.00 USD | 11,210,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,450,000.00 USD | 11,450,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,670,000.00 USD | 11,670,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,880,000.00 USD | 11,880,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,030,000.00 USD | 12,030,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,260,000.00 USD | 12,260,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,440,000.00 USD | 12,440,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,570,000.00 USD | 12,570,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,730,000.00 USD | 12,730,000.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,900,000.00 USD | 12,900,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,050,000.00 USD | 13,050,000.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,370,000.00 USD | 13,370,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,550,000.00 USD | 13,550,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,780,000.00 USD | 13,780,000.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,840,000.00 USD | 13,840,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 13,950,000.00 USD | 13,950,000.00 USD | 51,840.00 USD | 24,350.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,130,000.00 USD | 14,130,000.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 13,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,290,000.00 USD | 14,290,000.00 USD | 77,150.00 USD | 17,970.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,390,000.00 USD | 14,390,000.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,440,000.00 USD | 14,440,000.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,590,000.00 USD | 14,590,000.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,650,000.00 USD | 14,650,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,760,000.00 USD | 14,760,000.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,850,000.00 USD | 14,850,000.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,910,000.00 USD | 14,910,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 14,930,000.00 USD | 14,930,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,050,000.00 USD | 15,050,000.00 USD | 46,320.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,250,000.00 USD | 15,250,000.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,360,000.00 USD | 15,360,000.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,450,000.00 USD | 15,450,000.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,470,000.00 USD | 15,470,000.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,510,000.00 USD | 15,510,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,560,000.00 USD | 15,560,000.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,630,000.00 USD | 15,630,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.15` | 1,500.00 USD | 14,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 17,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 39,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 424.16 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 51,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 51,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 54,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 568,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 121.83 USD | 568,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 568,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 570,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 786.31 USD | 571,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 573,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 240.15 USD | 574,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 582,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 582,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 324.22 USD | 582,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 91,090.00 USD | 674,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2285` | 350,650.00 USD | 0.00 USD | 114.25 USD | `-75.28%` | `500.00` |
| `Live` | `Long` | `0.3475` | 350,540.00 USD | 0.00 USD | 140.29 USD | `-62.40%` | `403.70` |
| `Live` | `Long` | `0.3555` | 350,400.00 USD | 0.00 USD | 785.30 USD | `-61.53%` | `2,209.00` |
| `Live` | `Long` | `0.4065` | 349,610.00 USD | 0.00 USD | 30,490.00 USD | `-56.02%` | `75,000.00` |
| `Live` | `Long` | `0.4185` | 319,130.00 USD | 0.00 USD | 2,790.00 USD | `-54.72%` | `6,675.20` |
| `Live` | `Long` | `0.4195` | 316,330.00 USD | 0.00 USD | 2,390.00 USD | `-54.61%` | `5,698.80` |
| `Live` | `Long` | `0.4365` | 313,940.00 USD | 0.00 USD | 1,090.00 USD | `-52.77%` | `2,500.00` |
| `Live` | `Long` | `0.4385` | 312,850.00 USD | 0.00 USD | 1,350.00 USD | `-52.55%` | `3,069.40` |
| `Live` | `Long` | `0.4695` | 311,500.00 USD | 0.00 USD | 2,580.00 USD | `-49.20%` | `5,500.00` |
| `Live` | `Long` | `0.4845` | 308,920.00 USD | 0.00 USD | 29,070.00 USD | `-47.58%` | `60,000.00` |
| `Live` | `Long` | `0.5115` | 279,850.00 USD | 0.00 USD | 606.38 USD | `-44.65%` | `1,185.50` |
| `Live` | `Long` | `0.5125` | 279,250.00 USD | 0.00 USD | 4,130.00 USD | `-44.55%` | `8,067.10` |
| `Live` | `Long` | `0.5345` | 275,110.00 USD | 0.00 USD | 211.93 USD | `-42.17%` | `396.50` |
| `Live` | `Long` | `0.5695` | 274,900.00 USD | 0.00 USD | 577.36 USD | `-38.38%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 274,320.00 USD | 0.00 USD | 683.51 USD | `-36.76%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 273,640.00 USD | 0.00 USD | 137.53 USD | `-36.21%` | `233.30` |
| `Live` | `Long` | `0.5955` | 273,500.00 USD | 0.00 USD | 3,390.00 USD | `-35.57%` | `5,695.60` |
| `Live` | `Long` | `0.5985` | 270,110.00 USD | 0.00 USD | 1,030.00 USD | `-35.24%` | `1,715.50` |
| `Live` | `Long` | `0.6055` | 269,080.00 USD | 0.00 USD | 2,260.00 USD | `-34.48%` | `3,731.20` |
| `Live` | `Long` | `0.6065` | 266,820.00 USD | 0.00 USD | 1,800.00 USD | `-34.37%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 265,020.00 USD | 0.00 USD | 105.96 USD | `-33.73%` | `173.00` |
| `Live` | `Long` | `0.6145` | 264,920.00 USD | 0.00 USD | 147.48 USD | `-33.51%` | `240.00` |
| `Live` | `Long` | `0.6275` | 264,770.00 USD | 0.00 USD | 200.36 USD | `-32.10%` | `319.30` |
| `Live` | `Long` | `0.6315` | 264,570.00 USD | 0.00 USD | 757.80 USD | `-31.67%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 263,810.00 USD | 0.00 USD | 106.00 USD | `-31.24%` | `166.80` |
| `Live` | `Long` | `0.6405` | 263,700.00 USD | 0.00 USD | 2,090.00 USD | `-30.70%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 261,610.00 USD | 0.00 USD | 20,270.00 USD | `-30.59%` | `31,595.60` |
| `Live` | `Long` | `0.6425` | 241,350.00 USD | 0.00 USD | 362.05 USD | `-30.48%` | `563.50` |
| `Live` | `Long` | `0.6465` | 240,980.00 USD | 0.00 USD | 20,920.00 USD | `-30.05%` | `32,356.30` |
| `Live` | `Long` | `0.6475` | 220,070.00 USD | 0.00 USD | 202.47 USD | `-29.94%` | `312.70` |
| `Live` | `Long` | `0.6515` | 219,860.00 USD | 0.00 USD | 576.71 USD | `-29.51%` | `885.20` |
| `Live` | `Long` | `0.6595` | 219,290.00 USD | 0.00 USD | 149.44 USD | `-28.64%` | `226.60` |
| `Live` | `Long` | `0.6725` | 219,140.00 USD | 0.00 USD | 63,890.00 USD | `-27.23%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 155,250.00 USD | 0.00 USD | 629.33 USD | `-26.69%` | `928.90` |
| `Live` | `Long` | `0.6835` | 154,620.00 USD | 0.00 USD | 512.97 USD | `-26.04%` | `750.50` |
| `Live` | `Long` | `0.6955` | 154,110.00 USD | 0.00 USD | 322.16 USD | `-24.74%` | `463.20` |
| `Live` | `Long` | `0.7005` | 153,780.00 USD | 0.00 USD | 1,140.00 USD | `-24.20%` | `1,634.20` |
| `Live` | `Long` | `0.7075` | 152,640.00 USD | 0.00 USD | 16,520.00 USD | `-23.45%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 136,120.00 USD | 0.00 USD | 988.87 USD | `-22.69%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 135,130.00 USD | 0.00 USD | 1,580.00 USD | `-21.93%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 133,550.00 USD | 0.00 USD | 397.93 USD | `-21.72%` | `550.00` |
| `Live` | `Long` | `0.7255` | 133,160.00 USD | 0.00 USD | 1,090.00 USD | `-21.50%` | `1,500.00` |
| `Live` | `Long` | `0.7285` | 132,070.00 USD | 0.00 USD | 291.18 USD | `-21.17%` | `399.70` |
| `Live` | `Long` | `0.7305` | 131,780.00 USD | 0.00 USD | 3,030.00 USD | `-20.96%` | `4,143.00` |
| `Live` | `Long` | `0.7335` | 128,750.00 USD | 0.00 USD | 1,140.00 USD | `-20.63%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 127,610.00 USD | 0.00 USD | 283.30 USD | `-19.98%` | `383.10` |
| `Live` | `Long` | `0.7525` | 127,320.00 USD | 0.00 USD | 331.18 USD | `-18.58%` | `440.10` |
| `Live` | `Long` | `0.7535` | 126,990.00 USD | 0.00 USD | 1,400.00 USD | `-18.47%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 125,590.00 USD | 0.00 USD | 144.07 USD | `-18.25%` | `190.70` |
| `Live` | `Long` | `0.7575` | 125,450.00 USD | 0.00 USD | 169.23 USD | `-18.04%` | `223.40` |
| `Live` | `Long` | `0.7605` | 125,280.00 USD | 0.00 USD | 834.88 USD | `-17.71%` | `1,097.80` |
| `Live` | `Long` | `0.7615` | 124,440.00 USD | 0.00 USD | 804.07 USD | `-17.60%` | `1,055.90` |
| `Live` | `Long` | `0.7715` | 123,640.00 USD | 0.00 USD | 54,780.00 USD | `-16.52%` | `71,003.30` |
| `Live` | `Long` | `0.7725` | 68,860.00 USD | 0.00 USD | 3,840.00 USD | `-16.41%` | `4,968.90` |
| `Live` | `Long` | `0.7765` | 65,020.00 USD | 0.00 USD | 1,010.00 USD | `-15.98%` | `1,295.40` |
| `Live` | `Long` | `0.7815` | 64,020.00 USD | 0.00 USD | 234.45 USD | `-15.44%` | `300.00` |
| `Live` | `Long` | `0.7865` | 63,780.00 USD | 0.00 USD | 292.03 USD | `-14.90%` | `371.30` |
| `Live` | `Long` | `0.7965` | 63,490.00 USD | 0.00 USD | 301.32 USD | `-13.82%` | `378.30` |
| `Live` | `Long` | `0.8025` | 63,190.00 USD | 0.00 USD | 238.90 USD | `-13.17%` | `297.70` |
| `Live` | `Long` | `0.8085` | 62,950.00 USD | 0.00 USD | 13,380.00 USD | `-12.52%` | `16,544.60` |
| `Live` | `Long` | `0.8135` | 49,570.00 USD | 0.00 USD | 647.79 USD | `-11.98%` | `796.30` |
| `Live` | `Long` | `0.8215` | 48,930.00 USD | 0.00 USD | 1,950.00 USD | `-11.11%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 46,980.00 USD | 0.00 USD | 749.96 USD | `-10.89%` | `910.70` |
| `Live` | `Long` | `0.8365` | 46,230.00 USD | 0.00 USD | 316.70 USD | `-9.49%` | `378.60` |
| `Live` | `Long` | `0.8415` | 45,910.00 USD | 0.00 USD | 1,240.00 USD | `-8.95%` | `1,469.60` |
| `Live` | `Long` | `0.8495` | 44,670.00 USD | 0.00 USD | 1,260.00 USD | `-8.08%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 43,410.00 USD | 0.00 USD | 620.32 USD | `-7.22%` | `723.40` |
| `Live` | `Long` | `0.8605` | 42,790.00 USD | 0.00 USD | 127.01 USD | `-6.89%` | `147.60` |
| `Live` | `Long` | `0.8625` | 42,660.00 USD | 0.00 USD | 309.55 USD | `-6.68%` | `358.90` |
| `Live` | `Long` | `0.8635` | 42,350.00 USD | 0.00 USD | 208.02 USD | `-6.57%` | `240.90` |
| `Live` | `Long` | `0.8645` | 42,150.00 USD | 0.00 USD | 438.30 USD | `-6.46%` | `507.00` |
| `Live` | `Long` | `0.8695` | 41,710.00 USD | 0.00 USD | 12,590.00 USD | `-5.92%` | `14,478.80` |
| `Live` | `Long` | `0.8765` | 29,120.00 USD | 0.00 USD | 171.88 USD | `-5.16%` | `196.10` |
| `Live` | `Long` | `0.8795` | 28,950.00 USD | 0.00 USD | 948.01 USD | `-4.84%` | `1,077.90` |
| `Live` | `Long` | `0.8815` | 28,000.00 USD | 0.00 USD | 27,450.00 USD | `-4.62%` | `31,139.20` |
| `Live` | `Long` | `0.8845` | 549.72 USD | 0.00 USD | 549.72 USD | `-4.29%` | `621.50` |
| `Live` | `Short` | `0.9685` | 211.13 USD | 211.13 USD | 0.00 USD | `+4.79%` | `218.00` |
| `Live` | `Short` | `0.9925` | 428.09 USD | 216.96 USD | 0.00 USD | `+7.39%` | `218.60` |
| `Live` | `Short` | `1.02` | 650.30 USD | 222.21 USD | 0.00 USD | `+9.99%` | `218.60` |
| `Live` | `Short` | `1.07` | 13,000.00 USD | 12,350.00 USD | 0.00 USD | `+16.05%` | `11,518.80` |
| `Live` | `Short` | `1.11` | 13,170.00 USD | 169.86 USD | 0.00 USD | `+20.05%` | `153.10` |
| `Live` | `Short` | `1.15` | 14,670.00 USD | 1,500.00 USD | 0.00 USD | `+24.16%` | `1,306.30` |
| `Live` | `Short` | `1.17` | 17,130.00 USD | 2,450.00 USD | 0.00 USD | `+26.65%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 39,310.00 USD | 22,180.00 USD | 0.00 USD | `+28.60%` | `18,664.00` |
| `Live` | `Short` | `1.21` | 39,730.00 USD | 424.16 USD | 0.00 USD | `+30.98%` | `350.40` |
| `Live` | `Short` | `1.32` | 51,460.00 USD | 11,730.00 USD | 0.00 USD | `+43.21%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 51,700.00 USD | 239.77 USD | 0.00 USD | `+44.94%` | `179.00` |
| `Live` | `Short` | `1.42` | 54,900.00 USD | 3,190.00 USD | 0.00 USD | `+53.59%` | `2,249.30` |
| `Live` | `Short` | `1.49` | 568,500.00 USD | 513,610.00 USD | 0.00 USD | `+61.06%` | `345,051.20` |
| `Live` | `Short` | `1.53` | 568,630.00 USD | 121.83 USD | 0.00 USD | `+65.82%` | `79.50` |
| `Live` | `Short` | `1.54` | 568,800.00 USD | 176.31 USD | 0.00 USD | `+66.90%` | `114.30` |
| `Live` | `Short` | `1.56` | 570,610.00 USD | 1,810.00 USD | 0.00 USD | `+68.42%` | `1,161.90` |
| `Live` | `Short` | `1.57` | 571,400.00 USD | 786.31 USD | 0.00 USD | `+70.37%` | `499.40` |
| `Live` | `Short` | `1.62` | 573,830.00 USD | 2,440.00 USD | 0.00 USD | `+75.78%` | `1,500.00` |
| `Live` | `Short` | `1.64` | 574,070.00 USD | 240.15 USD | 0.00 USD | `+77.61%` | `146.30` |
| `Live` | `Short` | `1.65` | 582,310.00 USD | 8,240.00 USD | 0.00 USD | `+78.26%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 582,610.00 USD | 300.15 USD | 0.00 USD | `+80.43%` | `180.00` |
| `Live` | `Short` | `1.69` | 582,940.00 USD | 324.22 USD | 0.00 USD | `+82.81%` | `191.90` |
| `Live` | `Short` | `1.83` | 674,020.00 USD | 91,090.00 USD | 0.00 USD | `+98.07%` | `49,759.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 330,910.00 USD | 0.00 USD | 120.45 USD | `-56.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 330,790.00 USD | 0.00 USD | 150.15 USD | `-45.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 330,640.00 USD | 0.00 USD | 1,150.00 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 329,490.00 USD | 0.00 USD | 781.90 USD | `-24.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 328,710.00 USD | 0.00 USD | 477.38 USD | `-23.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 328,230.00 USD | 0.00 USD | 341.33 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 327,890.00 USD | 0.00 USD | 972.82 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 326,920.00 USD | 0.00 USD | 160.20 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 326,760.00 USD | 0.00 USD | 102.58 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 326,660.00 USD | 0.00 USD | 289.49 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 326,370.00 USD | 0.00 USD | 14,570.00 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 311,800.00 USD | 0.00 USD | 274,830.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 36,970.00 USD | 0.00 USD | 108.47 USD | `-13.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 36,860.00 USD | 0.00 USD | 405.75 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 36,450.00 USD | 0.00 USD | 772.84 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 35,680.00 USD | 0.00 USD | 3,470.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 32,210.00 USD | 0.00 USD | 9,180.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 23,030.00 USD | 0.00 USD | 341.94 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 22,690.00 USD | 0.00 USD | 1,150.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 21,540.00 USD | 0.00 USD | 2,020.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 19,520.00 USD | 0.00 USD | 429.25 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 19,090.00 USD | 0.00 USD | 1,290.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 17,800.00 USD | 0.00 USD | 518.51 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 17,280.00 USD | 0.00 USD | 224.84 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 17,060.00 USD | 0.00 USD | 193.35 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 16,870.00 USD | 0.00 USD | 223.04 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 16,640.00 USD | 0.00 USD | 10,840.00 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 5,800.00 USD | 0.00 USD | 158.51 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 5,640.00 USD | 0.00 USD | 192.07 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 5,450.00 USD | 0.00 USD | 195.32 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 5,250.00 USD | 0.00 USD | 196.96 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 5,060.00 USD | 0.00 USD | 196.10 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 4,860.00 USD | 0.00 USD | 198.61 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 4,660.00 USD | 0.00 USD | 994.35 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 3,670.00 USD | 0.00 USD | 363.40 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 3,300.00 USD | 0.00 USD | 398.72 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 2,910.00 USD | 0.00 USD | 199.80 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 2,710.00 USD | 0.00 USD | 199.49 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 2,510.00 USD | 0.00 USD | 198.06 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 2,310.00 USD | 0.00 USD | 198.64 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 2,110.00 USD | 0.00 USD | 198.52 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 1,910.00 USD | 0.00 USD | 913.41 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 997.74 USD | 0.00 USD | 795.81 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 201.94 USD | 0.00 USD | 201.94 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 2,120.00 USD | 2,120.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 2,360.00 USD | 246.05 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 2,770.00 USD | 407.49 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 2,980.00 USD | 203.97 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 3,380.00 USD | 403.40 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 3,580.00 USD | 203.41 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 3,780.00 USD | 201.97 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 13,470.00 USD | 9,680.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 14,020.00 USD | 555.18 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 14,170.00 USD | 145.43 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 15,900.00 USD | 1,730.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 16,280.00 USD | 383.87 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 17,100.00 USD | 817.40 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 17,510.00 USD | 414.68 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 17,890.00 USD | 381.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 20,120.00 USD | 2,230.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 24,020.00 USD | 3,900.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 24,250.00 USD | 236.26 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 24,420.00 USD | 166.41 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 24,800.00 USD | 376.80 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 26,700.00 USD | 1,910.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 27,270.00 USD | 568.75 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 27,430.00 USD | 163.29 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 27,990.00 USD | 554.58 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 28,370.00 USD | 385.74 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 28,530.00 USD | 153.22 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 51,330.00 USD | 22,800.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 62,560.00 USD | 11,230.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 72,930.00 USD | 10,370.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 73,310.00 USD | 387.83 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 80,950.00 USD | 7,630.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 89,690.00 USD | 8,750.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 111,660.00 USD | 21,960.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 112,050.00 USD | 396.17 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 112,730.00 USD | 676.53 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 124,130.00 USD | 11,400.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 124,250.00 USD | 123.61 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 132,600.00 USD | 8,350.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 134,660.00 USD | 2,060.00 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 135,030.00 USD | 362.49 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 150,100.00 USD | 15,070.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 182,890.00 USD | 32,800.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 217,870.00 USD | 34,970.00 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 221,390.00 USD | 3,520.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 253,140.00 USD | 31,750.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 253,540.00 USD | 403.06 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 254,330.00 USD | 782.07 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 254,730.00 USD | 403.28 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 259,870.00 USD | 5,140.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 297,180.00 USD | 37,310.00 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 298,180.00 USD | 1,000.00 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 338,780.00 USD | 40,590.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 339,010.00 USD | 235.79 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 340,350.00 USD | 1,340.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 340,580.00 USD | 230.39 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 340,800.00 USD | 218.64 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 341,210.00 USD | 409.86 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 341,320.00 USD | 110.95 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 341,940.00 USD | 615.60 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 342,500.00 USD | 561.17 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 342,600.00 USD | 103.07 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 343,010.00 USD | 401.26 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 343,810.00 USD | 804.09 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 344,010.00 USD | 201.52 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 344,220.00 USD | 207.97 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 344,420.00 USD | 201.60 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 344,520.00 USD | 101.51 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 344,730.00 USD | 208.26 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 345,250.00 USD | 516.75 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 345,450.00 USD | 204.93 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 345,800.00 USD | 348.86 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 346,210.00 USD | 413.76 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 346,570.00 USD | 354.91 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 348,470.00 USD | 1,900.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 348,680.00 USD | 207.87 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 348,890.00 USD | 207.97 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 350,180.00 USD | 1,290.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 350,390.00 USD | 206.97 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 350,500.00 USD | 107.99 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 350,750.00 USD | 247.60 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 425,580.00 USD | 74,840.00 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 426,130.00 USD | 544.88 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 426,280.00 USD | 157.10 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 428,460.00 USD | 2,170.00 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 429,990.00 USD | 1,540.00 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 439,920.00 USD | 9,930.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 440,800.00 USD | 877.63 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 440,970.00 USD | 171.50 USD | 0.00 USD | `+20.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 441,140.00 USD | 171.09 USD | 0.00 USD | `+20.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 443,910.00 USD | 2,770.00 USD | 0.00 USD | `+21.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 445,950.00 USD | 2,040.00 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 448,610.00 USD | 2,670.00 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 448,790.00 USD | 174.84 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 448,940.00 USD | 150.90 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,090.00 USD | 151.03 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,240.00 USD | 151.16 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,390.00 USD | 151.29 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,540.00 USD | 151.42 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,700.00 USD | 151.55 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 449,850.00 USD | 151.69 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 451,900.00 USD | 2,050.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 452,010.00 USD | 110.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 452,360.00 USD | 356.85 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 453,570.00 USD | 1,210.00 USD | 0.00 USD | `+29.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 496,500.00 USD | 42,930.00 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 498,500.00 USD | 2,000.00 USD | 0.00 USD | `+33.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 499,880.00 USD | 1,380.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 500,130.00 USD | 245.41 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 507,480.00 USD | 7,350.00 USD | 0.00 USD | `+39.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 507,890.00 USD | 415.25 USD | 0.00 USD | `+40.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 514,410.00 USD | 6,520.00 USD | 0.00 USD | `+41.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 971,400.00 USD | 456,990.00 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 972,050.00 USD | 655.75 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 973,870.00 USD | 1,810.00 USD | 0.00 USD | `+45.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 987,750.00 USD | 13,880.00 USD | 0.00 USD | `+45.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 989,000.00 USD | 1,250.00 USD | 0.00 USD | `+46.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 991,070.00 USD | 2,070.00 USD | 0.00 USD | `+50.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 991,210.00 USD | 140.05 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 991,370.00 USD | 160.42 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 991,970.00 USD | 598.33 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 1,030,000.00 USD | 34,170.00 USD | 0.00 USD | `+55.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 1,030,000.00 USD | 879.84 USD | 0.00 USD | `+61.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 1,030,000.00 USD | 590.88 USD | 0.00 USD | `+62.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 1,030,000.00 USD | 3,050.00 USD | 0.00 USD | `+63.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 1,030,000.00 USD | 297.27 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 1,040,000.00 USD | 8,530.00 USD | 0.00 USD | `+78.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 1,040,000.00 USD | 143.99 USD | 0.00 USD | `+80.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 1,040,000.00 USD | 177.05 USD | 0.00 USD | `+91.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 1,040,000.00 USD | 431.40 USD | 0.00 USD | `+94.82%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7890` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `7D` | `0.8050` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD |
| `7D` | `0.8090` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `1D` | `0.8130` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 878.33 USD | 138.33 USD | 2,640.00 USD |
| `7D` | `0.8130` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD |
| `1D` | `0.8150` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,620.00 USD | 191.37 USD | 26.89 USD |
| `7D` | `0.8150` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD |
| `1D` | `0.8170` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 9,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8170` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD |
| `1D` | `0.8230` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,490.00 USD | 880.65 USD |
| `7D` | `0.8230` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD |
| `1D` | `0.8250` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 8,060.00 USD | 5,240.00 USD | 6,380.00 USD |
| `7D` | `0.8250` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `1D` | `0.8270` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 244.70 USD | 2,830.00 USD | 110.11 USD |
| `7D` | `0.8270` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD |
| `1D` | `0.8290` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 40.90 USD | 0.00 USD |
| `7D` | `0.8290` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `1D` | `0.8310` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 163.37 USD | 1,760.00 USD | 442.45 USD |
| `7D` | `0.8310` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `1D` | `0.8330` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 25,550.00 USD | 2,130.00 USD | 3,530.00 USD |
| `7D` | `0.8330` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD |
| `1D` | `0.8350` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 3,440.00 USD | 11,120.00 USD |
| `7D` | `0.8350` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8370` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 9,580.00 USD | 1,900.00 USD | 9,140.00 USD |
| `7D` | `0.8370` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD |
| `1D` | `0.8390` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8390` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8410` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8410` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `7D` | `0.8430` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8450` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD |
| `7D` | `0.8470` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD |
| `7D` | `0.8490` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD |
| `1D` | `0.8510` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 421.90 USD | 2,000.00 USD | 2,680.00 USD |
| `7D` | `0.8510` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD |
| `7D` | `0.8530` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8550` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8550` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8570` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 366.87 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8590` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 3,490.00 USD | 1,100.00 USD | 182.69 USD |
| `7D` | `0.8590` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `0.8610` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 7,350.00 USD | 128.03 USD | 251.39 USD |
| `7D` | `0.8610` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 7,320.00 USD | 3,160.00 USD | 467.14 USD |
| `1D` | `0.8630` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 3,170.00 USD | 151.21 USD | 2,010.00 USD |
| `7D` | `0.8630` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8650` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 6,220.00 USD | 1,930.00 USD | 1,790.00 USD |
| `7D` | `0.8650` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8670` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 2,930.00 USD | 1,590.00 USD | 1,990.00 USD |
| `7D` | `0.8670` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8690` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 14,770.00 USD | 3,820.00 USD | 8,610.00 USD |
| `7D` | `0.8690` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD |
| `1D` | `0.8710` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 12,380.00 USD | 1,850.00 USD | 2,990.00 USD |
| `7D` | `0.8710` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8730` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 30,230.00 USD | 3,080.00 USD | 8,610.00 USD |
| `7D` | `0.8730` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD |
| `1D` | `0.8750` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 6,210.00 USD | 2,770.00 USD | 2,930.00 USD |
| `7D` | `0.8750` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.8770` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 33,040.00 USD | 6,750.00 USD | 6,200.00 USD |
| `7D` | `0.8770` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 52,140.00 USD | 16,410.00 USD | 2,760.00 USD |
| `1D` | `0.8790` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 34,680.00 USD | 12,000.00 USD | 22,970.00 USD |
| `7D` | `0.8790` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8810` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 17,760.00 USD | 18,200.00 USD | 5,560.00 USD |
| `7D` | `0.8810` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8830` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 6,980.00 USD | 4,200.00 USD | 311.46 USD |
| `7D` | `0.8830` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 8,430.00 USD | 5,730.00 USD | 957.94 USD |
| `1D` | `0.8850` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 8,900.00 USD | 5,700.00 USD | 7,000.00 USD |
| `7D` | `0.8850` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 8,630.00 USD | 10,630.00 USD | 866.69 USD |
| `1D` | `0.8870` | 978,630.00 USD | 0.00 USD | 978,630.00 USD | 19,160.00 USD | 11,410.00 USD | 10,490.00 USD |
| `7D` | `0.8870` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8890` | 937,570.00 USD | 0.00 USD | 937,570.00 USD | 67,190.00 USD | 12,700.00 USD | 16,110.00 USD |
| `7D` | `0.8890` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 54,380.00 USD | 29,640.00 USD | 14,360.00 USD |
| `1D` | `0.8910` | 841,570.00 USD | 0.00 USD | 841,570.00 USD | 47,930.00 USD | 13,730.00 USD | 30,060.00 USD |
| `7D` | `0.8910` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD |
| `1D` | `0.8930` | 749,840.00 USD | 0.00 USD | 749,840.00 USD | 31,260.00 USD | 11,150.00 USD | 24,750.00 USD |
| `7D` | `0.8930` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 62,870.00 USD | 10,990.00 USD | 10,100.00 USD |
| `1D` | `0.8950` | 682,680.00 USD | 0.00 USD | 682,680.00 USD | 21,170.00 USD | 3,980.00 USD | 4,460.00 USD |
| `7D` | `0.8950` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD |
| `1D` | `0.8970` | 653,070.00 USD | 0.00 USD | 653,070.00 USD | 25,280.00 USD | 23,820.00 USD | 44,540.00 USD |
| `7D` | `0.8970` | 999,100.00 USD | 0.00 USD | 999,100.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD |
| `1D` | `0.8990` | 559,440.00 USD | 0.00 USD | 559,440.00 USD | 76,980.00 USD | 16,160.00 USD | 1,240.00 USD |
| `7D` | `0.8990` | 857,400.00 USD | 0.00 USD | 857,400.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD |
| `1D` | `0.9010` | 465,050.00 USD | 0.00 USD | 465,050.00 USD | 254.26 USD | 14,150.00 USD | 2,350.00 USD |
| `7D` | `0.9010` | 762,110.00 USD | 0.00 USD | 762,110.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD |
| `1D` | `0.9030` | 448,300.00 USD | 0.00 USD | 448,300.00 USD | 5,770.00 USD | 6,910.00 USD | 4,220.00 USD |
| `7D` | `0.9030` | 727,020.00 USD | 0.00 USD | 727,020.00 USD | 13,100.00 USD | 8,710.00 USD | 27,460.00 USD |
| `1D` | `0.9050` | 431,410.00 USD | 0.00 USD | 431,410.00 USD | 0.00 USD | 15,360.00 USD | 6,160.00 USD |
| `7D` | `0.9050` | 677,750.00 USD | 0.00 USD | 677,750.00 USD | 31,190.00 USD | 13,050.00 USD | 27,300.00 USD |
| `1D` | `0.9070` | 409,890.00 USD | 0.00 USD | 409,890.00 USD | 126,150.00 USD | 23,360.00 USD | 18,830.00 USD |
| `7D` | `0.9070` | 606,210.00 USD | 0.00 USD | 606,210.00 USD | 114,070.00 USD | 49,120.00 USD | 15,500.00 USD |
| `1D` | `0.9090` | 241,550.00 USD | 0.00 USD | 241,550.00 USD | 0.00 USD | 25,080.00 USD | 55,580.00 USD |
| `7D` | `0.9090` | 427,520.00 USD | 0.00 USD | 427,520.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD |
| `1D` | `0.9110` | 160,890.00 USD | 0.00 USD | 160,890.00 USD | 50,190.00 USD | 17,990.00 USD | 45,720.00 USD |
| `7D` | `0.9110` | 309,320.00 USD | 0.00 USD | 309,320.00 USD | 76,180.00 USD | 10,780.00 USD | 16,450.00 USD |
| `1D` | `0.9130` | 46,980.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 3,290.00 USD | 0.00 USD |
| `7D` | `0.9130` | 205,900.00 USD | 0.00 USD | 205,900.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD |
| `1D` | `0.9150` | 43,690.00 USD | 0.00 USD | 43,690.00 USD | 0.00 USD | 168.83 USD | 19,030.00 USD |
| `7D` | `0.9150` | 147,390.00 USD | 0.00 USD | 147,390.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD |
| `1D` | `0.9170` | 24,490.00 USD | 0.00 USD | 24,490.00 USD | 0.00 USD | 132.18 USD | 0.00 USD |
| `7D` | `0.9170` | 113,650.00 USD | 0.00 USD | 113,650.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9190` | 24,360.00 USD | 0.00 USD | 24,360.00 USD | 0.00 USD | 158.23 USD | 0.00 USD |
| `7D` | `0.9190` | 98,400.00 USD | 0.00 USD | 98,400.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `1D` | `0.9210` | 24,200.00 USD | 0.00 USD | 24,200.00 USD | 0.00 USD | 118.70 USD | 4,890.00 USD |
| `7D` | `0.9210` | 79,930.00 USD | 0.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `1D` | `0.9230` | 19,190.00 USD | 0.00 USD | 19,190.00 USD | 14,160.00 USD | 556.44 USD | 4,470.00 USD |
| `7D` | `0.9230` | 64,140.00 USD | 0.00 USD | 64,140.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD |
| `7D` | `0.9240` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9250` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9270` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 778.79 USD | 259.15 USD |
| `1D` | `0.9290` | 1,670.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | 275.97 USD | 356.59 USD |
| `1D` | `0.9310` | 4,600.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | 76.32 USD | 2,850.00 USD |
| `1D` | `0.9330` | 66,800.00 USD | 66,800.00 USD | 0.00 USD | 38,560.00 USD | 18,340.00 USD | 5,310.00 USD |
| `1D` | `0.9350` | 216,110.00 USD | 216,110.00 USD | 0.00 USD | 123,740.00 USD | 15,750.00 USD | 9,810.00 USD |
| `7D` | `0.9350` | 768.64 USD | 768.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | 768.64 USD |
| `1D` | `0.9370` | 288,880.00 USD | 288,880.00 USD | 0.00 USD | 45,940.00 USD | 14,450.00 USD | 12,380.00 USD |
| `7D` | `0.9370` | 18,870.00 USD | 18,870.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9390` | 348,630.00 USD | 348,630.00 USD | 0.00 USD | 53,820.00 USD | 3,310.00 USD | 2,620.00 USD |
| `7D` | `0.9390` | 67,770.00 USD | 67,770.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 9,650.00 USD |
| `1D` | `0.9410` | 435,750.00 USD | 435,750.00 USD | 0.00 USD | 72,250.00 USD | 11,790.00 USD | 3,090.00 USD |
| `7D` | `0.9410` | 113,900.00 USD | 113,900.00 USD | 0.00 USD | 29,630.00 USD | 9,330.00 USD | 7,180.00 USD |
| `1D` | `0.9430` | 461,000.00 USD | 461,000.00 USD | 0.00 USD | 20,020.00 USD | 5,230.00 USD | 0.00 USD |
| `7D` | `0.9430` | 171,910.00 USD | 171,910.00 USD | 0.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD |
| `1D` | `0.9450` | 688,100.00 USD | 688,100.00 USD | 0.00 USD | 190,140.00 USD | 18,130.00 USD | 18,830.00 USD |
| `7D` | `0.9450` | 553,200.00 USD | 553,200.00 USD | 0.00 USD | 261,930.00 USD | 48,260.00 USD | 71,090.00 USD |
| `1D` | `0.9470` | 889,020.00 USD | 889,020.00 USD | 0.00 USD | 120,750.00 USD | 24,600.00 USD | 55,580.00 USD |
| `7D` | `0.9470` | 830,300.00 USD | 830,300.00 USD | 0.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD |
| `1D` | `0.9490` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 147,280.00 USD | 17,390.00 USD | 45,720.00 USD |
| `7D` | `0.9490` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 193,040.00 USD | 10,340.00 USD | 178,870.00 USD |
| `1D` | `0.9510` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 71,040.00 USD | 6,910.00 USD | 3,250.00 USD |
| `7D` | `0.9510` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD |
| `1D` | `0.9530` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 25,510.00 USD | 9,810.00 USD | 56,200.00 USD |
| `7D` | `0.9530` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD |
| `1D` | `0.9550` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 11,050.00 USD | 14,910.00 USD | 16,230.00 USD |
| `7D` | `0.9550` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD |
| `1D` | `0.9570` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 865.00 USD | 0.00 USD | 275.27 USD |
| `7D` | `0.9570` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 957.94 USD |
| `1D` | `0.9590` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 3,210.00 USD | 863.21 USD |
| `7D` | `0.9590` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 1,980.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9610` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 2,830.00 USD | 7,110.00 USD | 995.78 USD |
| `7D` | `0.9610` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9630` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 65,790.00 USD | 9,060.00 USD | 10,450.00 USD |
| `7D` | `0.9630` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD |
| `1D` | `0.9650` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 489.40 USD | 21,880.00 USD | 40,150.00 USD |
| `7D` | `0.9650` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9670` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 25,900.00 USD | 8,780.00 USD | 22,860.00 USD |
| `7D` | `0.9670` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 38,090.00 USD | 5,170.00 USD | 0.00 USD |
| `1D` | `0.9690` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 490.10 USD | 1,740.00 USD | 326.35 USD |
| `7D` | `0.9690` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 20,550.00 USD | 20,150.00 USD |
| `1D` | `0.9710` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 2,150.00 USD | 30,810.00 USD |
| `7D` | `0.9710` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.9730` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 40,580.00 USD | 5,170.00 USD | 14,000.00 USD |
| `7D` | `0.9730` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9750` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 25,830.00 USD | 11,090.00 USD | 17,210.00 USD |
| `7D` | `0.9750` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9770` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 76,840.00 USD | 5,950.00 USD | 9,980.00 USD |
| `7D` | `0.9770` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 26,770.00 USD |
| `7D` | `0.9790` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9810` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 366.87 USD | 376.40 USD | 8,420.00 USD |
| `7D` | `0.9810` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9830` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 15,980.00 USD | 20,710.00 USD | 28,830.00 USD |
| `7D` | `0.9830` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9850` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 38,840.00 USD | 4,430.00 USD | 19,350.00 USD |
| `7D` | `0.9850` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9870` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 12,080.00 USD | 3,590.00 USD | 15,120.00 USD |
| `7D` | `0.9870` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9890` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 24,170.00 USD | 0.00 USD | 20,110.00 USD |
| `7D` | `0.9890` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 51,530.00 USD | 1,520.00 USD | 20,230.00 USD |
| `7D` | `0.9910` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9930` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 15,020.00 USD | 15,930.00 USD | 1,290.00 USD |
| `7D` | `0.9930` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9950` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 16,320.00 USD | 1,630.00 USD | 329.08 USD |
| `7D` | `0.9950` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 33,860.00 USD | 2,480.00 USD | 5,580.00 USD |
| `7D` | `0.9970` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9990` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 33,110.00 USD | 8,690.00 USD | 6,100.00 USD |
| `7D` | `0.9990` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 156.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 41,520.00 USD | 23,800.00 USD | 348.39 USD |
| `7D` | `1.00` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 10,110.00 USD | 7,370.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD |
| `7D` | `1.00` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 47,140.00 USD | 11,580.00 USD | 50,050.00 USD |
| `7D` | `1.01` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 25,730.00 USD | 13,790.00 USD | 6,630.00 USD |
| `7D` | `1.01` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 7,620.00 USD | 26,630.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 10,040.00 USD | 4,110.00 USD | 352.75 USD |
| `7D` | `1.01` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 26,240.00 USD | 6,130.00 USD | 40,730.00 USD |
| `7D` | `1.01` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 1,810.00 USD | 8,510.00 USD | 24,720.00 USD |
| `7D` | `1.02` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 64,920.00 USD | 4,830.00 USD | 13,570.00 USD |
| `7D` | `1.02` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 27,370.00 USD | 5,700.00 USD | 26,050.00 USD |
| `7D` | `1.02` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 63,820.00 USD | 7,600.00 USD | 49,890.00 USD |
| `7D` | `1.02` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 68,350.00 USD | 32,010.00 USD | 37,870.00 USD |
| `7D` | `1.02` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD |
| `7D` | `1.03` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 30,250.00 USD | 24,670.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 133,770.00 USD | 17,580.00 USD | 40,480.00 USD |
| `7D` | `1.03` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 38,620.00 USD | 156.67 USD | 23,160.00 USD |
| `7D` | `1.03` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 22,000.00 USD | 18,470.00 USD | 9,760.00 USD |
| `7D` | `1.03` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 37,490.00 USD | 4,480.00 USD | 3,300.00 USD |
| `7D` | `1.04` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `7D` | `1.04` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `7D` | `1.04` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `7D` | `1.04` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `7D` | `1.04` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `7D` | `1.05` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `7D` | `1.05` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `7D` | `1.05` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD |
| `7D` | `1.05` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD |
| `7D` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `7D` | `1.07` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `7D` | `1.07` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `7D` | `1.07` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `7D` | `1.07` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `7D` | `1.07` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `7D` | `1.08` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `7D` | `1.08` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `7D` | `1.08` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `7D` | `1.08` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `7D` | `1.08` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `7D` | `1.09` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD |
| `7D` | `1.09` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `7D` | `1.09` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `7D` | `1.09` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `7D` | `1.09` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD |
| `7D` | `1.10` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 51,840.00 USD | 24,350.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 77,150.00 USD | 17,970.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 14,760,000.00 USD | 14,760,000.00 USD | 0.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 14,910,000.00 USD | 14,910,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 15,050,000.00 USD | 15,050,000.00 USD | 0.00 USD | 46,320.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `195.99M` | Total OI Tokens: `211,966,741.8 DOT`
  * 1h OI Change: `-0.32%` | 4h OI Change: `-5.37%` | 24h OI Change: `-10.73%`
  * Exchange Breakdown: Binance=`34.17M` | Bybit=`22.04M` | OKX=`9.92M` | Hyperliquid=`5.43M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.22K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0037%` | **USDT OKX** | `-0.0125%` |
| **USDT Bybit** | `0.0053%` | **USDT KuCoin** | `0.0022%` |
| **USDT MEXC** | `-0.0031%` | **USDT BingX** | `0.0047%` |
| **USDT Gate** | `-0.0022%` | **USDT Bitget** | `-0.0140%` |
| **CoinM Binance** | `0.0005%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `41.89%` | `58.11%` | `0.72` | 29,670,000.00 USD |
| `15M` | `Binance` | `42.94%` | `57.06%` | `0.75` | 10,390,000.00 USD |
| `15M` | `OKX` | `45.69%` | `54.31%` | `0.84` | 2,840,000.00 USD |
| `15M` | `Bybit` | `41.96%` | `58.04%` | `0.72` | 4,080,000.00 USD |
| `15M` | `KuCoin` | `33.96%` | `66.04%` | `0.51` | 120,340.00 USD |
| `15M` | `Gate` | `46.61%` | `53.39%` | `0.87` | 438,120.00 USD |
| `15M` | `Bitget` | `35.09%` | `64.91%` | `0.54` | 939,020.00 USD |
| `15M` | `BingX` | `61.07%` | `38.93%` | `1.57` | 580,050.00 USD |
| `15M` | `MEXC` | `32.6%` | `67.4%` | `0.48` | 3,410,000.00 USD |
| `15M` | `Bitunix` | `49.27%` | `50.73%` | `0.97` | 460,240.00 USD |
| `15M` | `Hyperliquid` | `35.11%` | `64.89%` | `0.54` | 4,790,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.02%` | `54.98%` | `0.82` | 177,730.00 USD |
| `15M` | `Crypto.com` | `76.89%` | `23.11%` | `3.33` | 1,200.00 USD |
| `15M` | `WhiteBIT` | `84.64%` | `15.36%` | `5.51` | 911,130.00 USD |
| `15M` | `HTX` | `23.82%` | `76.18%` | `0.31` | 5,190.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `39.52%` | `60.48%` | `0.65` | 282,370.00 USD |
| `15M` | `Aster` | `3.01%` | `96.99%` | `0.03` | 76,610.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `24.32%` | `75.68%` | `0.32` | 148,820.00 USD |
| `15M` | `Whale Positions` | `42.94%` | `57.06%` | `0.75` | 10,390,000.00 USD |
| `15M` | `Global Accounts` | `41.89%` | `58.11%` | `0.72` | 29,670,000.00 USD |
| `1H` | `DOT` | `47.40%` | `52.60%` | `0.90` | 171,060,000.00 USD |
| `1H` | `Binance` | `49.51%` | `50.49%` | `0.98` | 64,450,000.00 USD |
| `1H` | `OKX` | `46.99%` | `53.01%` | `0.89` | 17,650,000.00 USD |
| `1H` | `Bybit` | `46.34%` | `53.66%` | `0.86` | 25,460,000.00 USD |
| `1H` | `KuCoin` | `50.78%` | `49.22%` | `1.03` | 1,010,000.00 USD |
| `1H` | `Gate` | `45.45%` | `54.55%` | `0.83` | 2,090,000.00 USD |
| `1H` | `Bitget` | `46.14%` | `53.86%` | `0.86` | 6,540,000.00 USD |
| `1H` | `BingX` | `52.13%` | `47.87%` | `1.09` | 5,660,000.00 USD |
| `1H` | `MEXC` | `42.19%` | `57.81%` | `0.73` | 10,170,000.00 USD |
| `1H` | `Bitunix` | `49.3%` | `50.7%` | `0.97` | 3,100,000.00 USD |
| `1H` | `Hyperliquid` | `40.95%` | `59.05%` | `0.69` | 27,440,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.42%` | `50.58%` | `0.98` | 1,120,000.00 USD |
| `1H` | `Crypto.com` | `36.17%` | `63.83%` | `0.57` | 6,740.00 USD |
| `1H` | `WhiteBIT` | `81.07%` | `18.93%` | `4.28` | 3,690,000.00 USD |
| `1H` | `HTX` | `37.92%` | `62.08%` | `0.61` | 71,680.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.55%` | `56.45%` | `0.77` | 1,450,000.00 USD |
| `1H` | `Aster` | `20.76%` | `79.24%` | `0.26` | 290,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.93%` | `62.07%` | `0.61` | 854,400.00 USD |
| `1H` | `Whale Positions` | `49.51%` | `50.49%` | `0.98` | 64,450,000.00 USD |
| `1H` | `Global Accounts` | `47.40%` | `52.60%` | `0.90` | 171,060,000.00 USD |
| `4H` | `DOT` | `46.32%` | `53.68%` | `0.86` | 330,710,000.00 USD |
| `4H` | `Binance` | `47.49%` | `52.51%` | `0.90` | 133,100,000.00 USD |
| `4H` | `OKX` | `50.24%` | `49.76%` | `1.01` | 45,260,000.00 USD |
| `4H` | `Bybit` | `45.94%` | `54.06%` | `0.85` | 45,100,000.00 USD |
| `4H` | `KuCoin` | `43.57%` | `56.43%` | `0.77` | 3,620,000.00 USD |
| `4H` | `Gate` | `48.71%` | `51.29%` | `0.95` | 7,000,000.00 USD |
| `4H` | `Bitget` | `46.97%` | `53.03%` | `0.89` | 20,540,000.00 USD |
| `4H` | `BingX` | `41.35%` | `58.65%` | `0.71` | 9,770,000.00 USD |
| `4H` | `MEXC` | `43.07%` | `56.93%` | `0.76` | 28,230,000.00 USD |
| `4H` | `Bitunix` | `44.92%` | `55.08%` | `0.82` | 13,180,000.00 USD |
| `4H` | `Hyperliquid` | `42.47%` | `57.53%` | `0.74` | 11,650,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `42.65%` | `57.35%` | `0.74` | 2,740,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `27.32%` | `72.68%` | `0.38` | 5,540,000.00 USD |
| `4H` | `HTX` | `47.53%` | `52.47%` | `0.91` | 701,590.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.9%` | `60.1%` | `0.66` | 2,460,000.00 USD |
| `4H` | `Aster` | `43.7%` | `56.3%` | `0.78` | 1,430,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.68%` | `52.32%` | `0.91` | 423,040.00 USD |
| `4H` | `Whale Positions` | `47.49%` | `52.51%` | `0.90` | 133,100,000.00 USD |
| `4H` | `Global Accounts` | `46.32%` | `53.68%` | `0.86` | 330,710,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9271` | `0.9372` | `0.9271` | `0.9707` | `0.9107` | 10,294,158.77 USD | 4,127,124.83 USD | 6,167,033.94 USD | -2,039,909.11 USD | `-19.82%` | `5B / 37S` |
| `5:00 UTC` | `0.9157` | `0.9093` | `0.9157` | `0.9241` | `0.8893` | 9,166,573.96 USD | 4,231,807.53 USD | 4,934,766.43 USD | -702,958.89 USD | `-7.67%` | `6B / 13S` |
| `0:00 UTC` | `0.9138` | `0.9204` | `0.9138` | `0.9302` | `0.9076` | 3,388,598.53 USD | 1,615,651.50 USD | 1,772,947.04 USD | -157,295.54 USD | `-4.64%` | `11B / 8S` |
| `5:00 UTC` | `0.9302` | `0.9320` | `0.9302` | `0.9392` | `0.9254` | 2,028,309.51 USD | 996,075.55 USD | 1,032,233.96 USD | -36,158.40 USD | `-1.78%` | `11B / 12S` |
| `0:00 UTC` | `0.9301` | `0.9318` | `0.9301` | `0.9381` | `0.9248` | 1,862,169.82 USD | 558,080.50 USD | 1,304,089.32 USD | -746,008.82 USD | `-40.06%` | `17B / 36S` |
| `5:00 UTC` | `0.9251` | `0.9254` | `0.9251` | `0.9294` | `0.9219` | 1,343,196.16 USD | 526,839.48 USD | 816,356.69 USD | -289,517.21 USD | `-21.55%` | `18B / 7S` |
| `0:00 UTC` | `0.9254` | `0.9217` | `0.9254` | `0.9288` | `0.9143` | 1,982,933.95 USD | 1,080,771.49 USD | 902,162.47 USD | 178,609.02 USD | `+9.01%` | `16B / 22S` |
| `5:00 UTC` | `0.9313` | `0.9286` | `0.9313` | `0.9327` | `0.9201` | 1,171,136.75 USD | 631,208.27 USD | 539,928.48 USD | 91,279.80 USD | `+7.79%` | `19B / 8S` |
| `0:00 UTC` | `0.9294` | `0.9281` | `0.9294` | `0.9324` | `0.9237` | 735,316.47 USD | 385,478.28 USD | 349,838.19 USD | 35,640.09 USD | `+4.85%` | `10B / 6S` |
| `5:00 UTC` | `0.9244` | `0.9246` | `0.9244` | `0.9277` | `0.9221` | 310,341.49 USD | 159,274.62 USD | 151,066.87 USD | 8,207.75 USD | `+2.64%` | `8B / 12S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:39` | `Volume 1.0M DOT` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9951` | 122,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 333,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:58` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:40` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9970` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 219,000.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 221,000.00 USD | 0.00 USD |
| `10-28 18:19` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 18:16` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 229,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 260,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 11:08` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `1.01` | 363,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 36,340.00 USD | -5,790.00 USD | **`ACCUMULATION`** |
| `15m` | 10,310.00 USD | -68,890.00 USD | **`DISTRIBUTION`** |
| `30m` | 82,760.00 USD | -32,400.00 USD | **`ACCUMULATION`** |
| `1h` | 155,410.00 USD | 387,580.00 USD | **`ACCUMULATION`** |
| `2h` | 340,760.00 USD | -363,210.00 USD | **`DISTRIBUTION`** |
| `4h` | -661,200.00 USD | -6,100,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -776,170.00 USD | -6,540,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -828,700.00 USD | -7,500,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -829,250.00 USD | -8,040,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -992,980.00 USD | -7,540,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,100,000.00 USD | -24,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,300,000.00 USD | -78,910,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+36.34K` | 15m=`+10.31K` | 1h=`+155.41K` | 24h=`-992.98K`
* Futures Capital Netflows: 5m=`-5.79K` | 15m=`-68.89K` | 1h=`+387.58K` | 24h=`-7.54M`
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
  * Execution Entry: `0.9108` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8639` (Risk Distance: `0.0469` pts)
  * +2.5R Take Profit: `1.03`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9213` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9682` (Risk Distance: `0.0469` pts)
  * +2.5R Take Profit: `0.8039`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9289`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
