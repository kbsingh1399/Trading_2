# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9090` | **Live Ask Quote**: `0.9300` | **Mid Price**: `0.9195`
- **Spread Points**: `21.00` | **Spread BPS**: `228.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9643` | VWAP Z-Score: `-1.86` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0132` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `28.37` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.05` | Lower -3.00σ Band: `0.8800`
  * Upper +2.51σ Band: `1.03` | Lower -2.51σ Band: `0.8938`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.9078`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.9081`
  * Upper +1.28σ Band: `1.00` | Lower -1.28σ Band: `0.9283`
  * Upper +1.00σ Band: `0.9925` | Lower -1.00σ Band: `0.9362`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9278` | EMA-20=`0.9475` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9651` (Slope: `+0.0000`) | EMA-100=`0.9735`
  * Institutional Anchors: EMA-144=`0.9769` | EMA-200=`0.9789` (Slope: `-0.5171`) | EMA-233=`0.9804`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8800` | Weekly High=`1.03` | Weekly Low=`0.8800`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9236` (Distance: `-0.45%`)
  * Point of Control (POC) = `0.9150` (Distance: `+0.49%`)
  * Value Area Low (VAL) = `0.9111` (Distance: `+0.93%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9932` | Weekly VAL=`0.9751`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.9050`
  * London Session (08:00-16:00 UTC): High=`0.9232` | Low=`0.9158`
  * New York Session (13:00-21:00 UTC): High=`0.9250` | Low=`0.9140`
  * Initial Balance (First Hour): IB High=`0.9223` | IB Low=`0.9167`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9158` - `0.9232`
  * Optimal Trade Entry (OTE 0.705): `0.9213`
  * Structural Invalidation Anchor (0.786): `0.9269`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9266` | `0.9291` | `0.9218` | `0.9232` | `315,680` | 292,054.46 USD | 74,571.57 USD | `+25.53%` | -4,635,625.96 USD | `+0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9232` | `0.9278` | `0.9155` | `0.9203` | `1,267,156` | 1,167,731.61 USD | -39,093.78 USD | `-3.35%` | -4,674,719.73 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9202` | `0.9205` | `0.9192` | `0.9198` | `33,269` | 30,598.85 USD | -13,600.30 USD | `-44.45%` | -4,688,320.04 USD | `+0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9317` | `0.9380` | `0.9248` | `0.9249` | `1,998,582` | 1,862,169.82 USD | -746,008.82 USD | `-40.06%` | -4,339,951.84 USD | `-1.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9250` | `0.9293` | `0.9218` | `0.9232` | `1,451,516` | 1,343,196.16 USD | -289,517.21 USD | `-21.55%` | -4,629,469.06 USD | `-0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9232` | `0.9278` | `0.9155` | `0.9198` | `1,300,425` | 1,198,330.46 USD | -52,694.08 USD | `-4.40%` | -4,682,163.14 USD | `+0.33` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.8892` | `0.9107` | `25,741,782` | 23,981,753.25 USD | -3,181,821.86 USD | `-13.27%` | -3,433,243.38 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9106` | `0.9391` | `0.9075` | `0.9232` | `9,308,289` | 8,622,274.03 USD | -1,228,979.98 USD | `-14.25%` | -4,662,223.36 USD | `-1.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9232` | `0.9278` | `0.9155` | `0.9202` | `1,304,785` | 1,202,342.00 USD | -49,034.95 USD | `-4.08%` | -4,711,258.30 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9198` | `36,350,496` | 33,802,357.73 USD | -4,463,495.92 USD | `-13.20%` | -4,744,055.24 USD | `-2.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9198` | `36,350,496` | 33,802,357.73 USD | -4,463,495.92 USD | `-13.20%` | -4,744,055.24 USD | `-2.17` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9195`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

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
  * 24H Horizon: Short MP=`0.9823` (Vol: 101,100.00 USD, Dist: `+5.74%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.9828` (Vol: 101,100.00 USD, Dist: `+5.79%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.9828` (Vol: 101,100.00 USD, Dist: `+5.79%`) | Long MP=`0.8959` (Vol: 126,000.00 USD, Dist: `--3.57%`)
  * 7D Horizon: Short MP=`1.06` (Vol: 231,300.00 USD, Dist: `+13.83%`) | Long MP=`0.8963` (Vol: 126,000.00 USD, Dist: `--3.52%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2215` | 110.75 USD | 342,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3525` | 142.30 USD | 341,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3595` | 794.14 USD | 341,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4145` | 31,090.00 USD | 341,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 309,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 2,500.00 USD | 307,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 304,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 302,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 301,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 212.33 USD | 297,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 35,030.00 USD | 297,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 2,240.00 USD | 262,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 259,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 259,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 259,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 255,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 253,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 251,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 251,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 251,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 250,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 250,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 250,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 247,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 104.60 USD | 227,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 253.09 USD | 227,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 227,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 461.93 USD | 223,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 222,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6605` | 210.90 USD | 222,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6635` | 1,200.00 USD | 222,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 221,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 157,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 156,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 156,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 176.38 USD | 155,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 155,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 139,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 138,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 137,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 136,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 136,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 134,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 736.50 USD | 133,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 132,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 8,590.00 USD | 131,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 123,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 123,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 121,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 119,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 172.80 USD | 118,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 1,710.00 USD | 118,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 55,630.00 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 1,280.00 USD | 60,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 59,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,130,000.00 USD | 2,130,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 59,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,120,000.00 USD | 2,120,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7930` | 1,390,000.00 USD | 1,390,000.00 USD | 5,980.00 USD | 1,060.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,100,000.00 USD | 2,100,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7950` | 1,370,000.00 USD | 1,370,000.00 USD | 1,120.00 USD | 958.57 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,070,000.00 USD | 2,070,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 1,370,000.00 USD | 1,370,000.00 USD | 222.45 USD | 1,550.00 USD | 41.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,050,000.00 USD | 2,050,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7990` | 1,370,000.00 USD | 1,370,000.00 USD | 1,140.00 USD | 5.58 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 2,030,000.00 USD | 2,030,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8010` | 1,360,000.00 USD | 1,360,000.00 USD | 7.83 USD | 5.00 USD | 947.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,990,000.00 USD | 1,990,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 38,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8030` | 1,360,000.00 USD | 1,360,000.00 USD | 2,310.00 USD | 2,600.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,980,000.00 USD | 1,980,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8050` | 1,360,000.00 USD | 1,360,000.00 USD | 1,010.00 USD | 821.12 USD | 55.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,960,000.00 USD | 1,960,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 13,340.00 USD | 38,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 1,350,000.00 USD | 1,350,000.00 USD | 444.13 USD | 359.76 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,940,000.00 USD | 1,940,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8090` | 1,350,000.00 USD | 1,350,000.00 USD | 4,740.00 USD | 322.74 USD | 2,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,920,000.00 USD | 1,920,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8110` | 1,350,000.00 USD | 1,350,000.00 USD | 2,000.00 USD | 252.43 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,910,000.00 USD | 1,910,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8130` | 1,340,000.00 USD | 1,340,000.00 USD | 1,040.00 USD | 35.58 USD | 796.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,900,000.00 USD | 1,900,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 25,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 1,340,000.00 USD | 1,340,000.00 USD | 2,620.00 USD | 191.37 USD | 26.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,880,000.00 USD | 1,880,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8170` | 1,340,000.00 USD | 1,340,000.00 USD | 9,220.00 USD | 6.18 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,860,000.00 USD | 1,860,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,840,000.00 USD | 1,840,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 200.69 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,820,000.00 USD | 1,820,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 24,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 1,490.00 USD | 880.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,800,000.00 USD | 1,800,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8250` | 1,320,000.00 USD | 1,320,000.00 USD | 8,060.00 USD | 5,240.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 1,770,000.00 USD | 1,770,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 4,100.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8270` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 1,750,000.00 USD | 1,750,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 1,740,000.00 USD | 1,740,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 1,300,000.00 USD | 1,300,000.00 USD | 25,230.00 USD | 1,090.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 1,730,000.00 USD | 1,730,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8350` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 3,440.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 1,700,000.00 USD | 1,700,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 18,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 1,260,000.00 USD | 1,260,000.00 USD | 9,580.00 USD | 0.00 USD | 9,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,680,000.00 USD | 1,680,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 1,240,000.00 USD | 1,240,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,660,000.00 USD | 1,660,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 18,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,650,000.00 USD | 1,650,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 1,240,000.00 USD | 1,240,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,640,000.00 USD | 1,640,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,630,000.00 USD | 1,630,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 16,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 1,240,000.00 USD | 1,240,000.00 USD | 421.90 USD | 2,000.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,630,000.00 USD | 1,630,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,620,000.00 USD | 1,620,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 1,230,000.00 USD | 1,230,000.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,610,000.00 USD | 1,610,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 1,110.00 USD | 15,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8570` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 1,530.00 USD | 14,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 1,230,000.00 USD | 1,230,000.00 USD | 3,490.00 USD | 1,030.00 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 1,220,000.00 USD | 1,220,000.00 USD | 6,980.00 USD | 24.95 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,600,000.00 USD | 1,600,000.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 12,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8630` | 1,220,000.00 USD | 1,220,000.00 USD | 3,170.00 USD | 111.70 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,590,000.00 USD | 1,590,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 12,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 12,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 1,210,000.00 USD | 1,210,000.00 USD | 5,670.00 USD | 1,930.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,590,000.00 USD | 1,590,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 11,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,200,000.00 USD | 1,200,000.00 USD | 2,670.00 USD | 1,590.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,580,000.00 USD | 1,580,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,190,000.00 USD | 1,190,000.00 USD | 14,770.00 USD | 3,720.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,560,000.00 USD | 1,560,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 10,740.00 USD | 11,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,170,000.00 USD | 1,170,000.00 USD | 12,380.00 USD | 1,850.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,520,000.00 USD | 1,520,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,150,000.00 USD | 1,150,000.00 USD | 29,740.00 USD | 3,080.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,110,000.00 USD | 1,110,000.00 USD | 6,210.00 USD | 2,690.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 1,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,100,000.00 USD | 1,100,000.00 USD | 32,550.00 USD | 6,610.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,490,000.00 USD | 1,490,000.00 USD | 52,140.00 USD | 16,130.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,050,000.00 USD | 1,050,000.00 USD | 34,680.00 USD | 11,940.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,420,000.00 USD | 1,420,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 948.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8810` | 981,570.00 USD | 981,570.00 USD | 17,010.00 USD | 18,200.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,410,000.00 USD | 1,410,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 940,790.00 USD | 940,790.00 USD | 6,640.00 USD | 4,200.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,410,000.00 USD | 1,410,000.00 USD | 8,430.00 USD | 5,730.00 USD | 469.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 929,920.00 USD | 929,920.00 USD | 8,900.00 USD | 2,370.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,400,000.00 USD | 1,400,000.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 912,200.00 USD | 912,200.00 USD | 19,160.00 USD | 7,070.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,380,000.00 USD | 1,380,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 876,240.00 USD | 876,240.00 USD | 67,190.00 USD | 6,440.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,350,000.00 USD | 1,350,000.00 USD | 54,380.00 USD | 24,510.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 786,500.00 USD | 786,500.00 USD | 47,930.00 USD | 11,990.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,260,000.00 USD | 1,260,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 696,520.00 USD | 696,520.00 USD | 31,260.00 USD | 4,990.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,140,000.00 USD | 1,140,000.00 USD | 62,870.00 USD | 5,820.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 635,520.00 USD | 635,520.00 USD | 21,170.00 USD | 2,440.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,060,000.00 USD | 1,060,000.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 607,450.00 USD | 607,450.00 USD | 25,280.00 USD | 23,820.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 966,460.00 USD | 966,460.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 513,810.00 USD | 513,810.00 USD | 76,980.00 USD | 16,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 824,760.00 USD | 824,760.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 419,430.00 USD | 419,430.00 USD | 254.26 USD | 14,150.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 729,480.00 USD | 729,480.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 403,230.00 USD | 403,230.00 USD | 5,770.00 USD | 3,600.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 694,380.00 USD | 694,380.00 USD | 13,100.00 USD | 8,710.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 389,640.00 USD | 389,640.00 USD | 0.00 USD | 3,570.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 646,090.00 USD | 646,090.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 382,540.00 USD | 382,540.00 USD | 126,150.00 USD | 10,840.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 585,610.00 USD | 585,610.00 USD | 114,070.00 USD | 38,860.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 226,720.00 USD | 226,720.00 USD | 0.00 USD | 21,600.00 USD | 55,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 417,180.00 USD | 417,180.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 149,540.00 USD | 149,540.00 USD | 50,190.00 USD | 5,680.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 298,970.00 USD | 298,970.00 USD | 76,180.00 USD | 441.10 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 47,950.00 USD | 47,950.00 USD | 0.00 USD | 210.91 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 205,900.00 USD | 205,900.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 47,740.00 USD | 47,740.00 USD | 0.00 USD | 228.28 USD | 19,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 147,390.00 USD | 147,390.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 28,480.00 USD | 28,480.00 USD | 0.00 USD | 132.18 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 113,650.00 USD | 113,650.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 28,350.00 USD | 28,350.00 USD | 0.00 USD | 170.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 98,400.00 USD | 98,400.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 28,180.00 USD | 28,180.00 USD | 0.00 USD | 118.70 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 19,190.00 USD | 19,190.00 USD | 14,160.00 USD | 556.44 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 64,140.00 USD | 64,140.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 898.10 USD | 898.10 USD | 0.00 USD | 898.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 1,800.00 USD | 1,800.00 USD | 0.00 USD | 898.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 778.79 USD | 259.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 3,470.00 USD | 3,470.00 USD | 0.00 USD | 275.97 USD | 356.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 6,390.00 USD | 6,390.00 USD | 0.00 USD | 76.32 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 68,600.00 USD | 68,600.00 USD | 38,560.00 USD | 18,340.00 USD | 5,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 217,900.00 USD | 217,900.00 USD | 123,740.00 USD | 15,750.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 768.64 USD | 768.64 USD | 0.00 USD | 0.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 290,120.00 USD | 290,120.00 USD | 45,940.00 USD | 14,450.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 18,870.00 USD | 18,870.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 346,560.00 USD | 346,560.00 USD | 53,820.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 66,790.00 USD | 66,790.00 USD | 39,250.00 USD | 0.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 419,270.00 USD | 419,270.00 USD | 72,250.00 USD | 0.00 USD | 465.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 101,870.00 USD | 101,870.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 444,520.00 USD | 444,520.00 USD | 20,020.00 USD | 5,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 159,880.00 USD | 159,880.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 659,100.00 USD | 659,100.00 USD | 190,140.00 USD | 5,610.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 530,900.00 USD | 530,900.00 USD | 261,930.00 USD | 38,000.00 USD | 71,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 856,530.00 USD | 856,530.00 USD | 120,750.00 USD | 21,110.00 USD | 55,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 808,010.00 USD | 808,010.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 1,050,000.00 USD | 1,050,000.00 USD | 147,280.00 USD | 5,080.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,180,000.00 USD | 1,180,000.00 USD | 193,040.00 USD | 0.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 1,130,000.00 USD | 1,130,000.00 USD | 71,040.00 USD | 3,830.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,570,000.00 USD | 1,570,000.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 1,220,000.00 USD | 1,220,000.00 USD | 25,510.00 USD | 9,830.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 1,270,000.00 USD | 1,270,000.00 USD | 11,050.00 USD | 14,910.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 1,270,000.00 USD | 1,270,000.00 USD | 865.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,730,000.00 USD | 1,730,000.00 USD | 1,910.00 USD | 0.00 USD | 469.21 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 313.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,730,000.00 USD | 1,730,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9605` | 210.64 USD | 210.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9610` | 1,270,000.00 USD | 1,270,000.00 USD | 2,830.00 USD | 2,760.00 USD | 232.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,760,000.00 USD | 1,760,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 1,350,000.00 USD | 1,350,000.00 USD | 65,790.00 USD | 2,800.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,830,000.00 USD | 1,830,000.00 USD | 53,510.00 USD | 19,000.00 USD | 481.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 1,410,000.00 USD | 1,410,000.00 USD | 497.80 USD | 20,140.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,890,000.00 USD | 1,890,000.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 1,460,000.00 USD | 1,460,000.00 USD | 25,900.00 USD | 2,540.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,930,000.00 USD | 1,930,000.00 USD | 38,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 2,060.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9685` | 211.13 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9690` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 82.70 USD | 326.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 20,260.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 2,090.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,560,000.00 USD | 1,560,000.00 USD | 39,840.00 USD | 5,170.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,010,000.00 USD | 2,010,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,610,000.00 USD | 1,610,000.00 USD | 25,480.00 USD | 11,090.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,700,000.00 USD | 1,700,000.00 USD | 76,840.00 USD | 5,820.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,130,000.00 USD | 2,130,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,770,000.00 USD | 1,770,000.00 USD | 29,240.00 USD | 9,580.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 376.40 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,330,000.00 USD | 2,330,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,840,000.00 USD | 1,840,000.00 USD | 15,980.00 USD | 20,640.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,500,000.00 USD | 2,500,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,910,000.00 USD | 1,910,000.00 USD | 38,470.00 USD | 4,330.00 USD | 19,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,940,000.00 USD | 1,940,000.00 USD | 12,080.00 USD | 3,550.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,620,000.00 USD | 2,620,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 432.33 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,980,000.00 USD | 1,980,000.00 USD | 23,610.00 USD | 0.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,640,000.00 USD | 2,640,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 2,050,000.00 USD | 2,050,000.00 USD | 51,270.00 USD | 1,520.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 2,080,000.00 USD | 2,080,000.00 USD | 15,020.00 USD | 15,830.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 2,100,000.00 USD | 2,100,000.00 USD | 16,320.00 USD | 1,630.00 USD | 329.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,750,000.00 USD | 2,750,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 2,150,000.00 USD | 2,150,000.00 USD | 33,860.00 USD | 2,480.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,820,000.00 USD | 2,820,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9975` | 218.35 USD | 3,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 2,190,000.00 USD | 2,190,000.00 USD | 33,110.00 USD | 8,690.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 156.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,260,000.00 USD | 2,260,000.00 USD | 41,520.00 USD | 24,950.00 USD | 348.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,870,000.00 USD | 2,870,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,280,000.00 USD | 2,280,000.00 USD | 10,110.00 USD | 7,370.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,020,000.00 USD | 3,020,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,350,000.00 USD | 2,350,000.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,060,000.00 USD | 3,060,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,460,000.00 USD | 2,460,000.00 USD | 47,140.00 USD | 11,580.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,120,000.00 USD | 3,120,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,500,000.00 USD | 2,500,000.00 USD | 25,730.00 USD | 13,790.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,140,000.00 USD | 3,140,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,540,000.00 USD | 2,540,000.00 USD | 7,380.00 USD | 26,630.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,180,000.00 USD | 3,180,000.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,550,000.00 USD | 2,550,000.00 USD | 10,040.00 USD | 4,070.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,230,000.00 USD | 3,230,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,620,000.00 USD | 2,620,000.00 USD | 26,070.00 USD | 4,370.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,660,000.00 USD | 2,660,000.00 USD | 1,810.00 USD | 8,510.00 USD | 24,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,310,000.00 USD | 3,310,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,740,000.00 USD | 2,740,000.00 USD | 64,600.00 USD | 3,790.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,420,000.00 USD | 3,420,000.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,800,000.00 USD | 2,800,000.00 USD | 27,370.00 USD | 5,700.00 USD | 26,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,590,000.00 USD | 3,590,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,920,000.00 USD | 2,920,000.00 USD | 63,820.00 USD | 5,700.00 USD | 49,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,900,000.00 USD | 3,900,000.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,060,000.00 USD | 3,060,000.00 USD | 68,350.00 USD | 32,010.00 USD | 37,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,020,000.00 USD | 4,020,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,110,000.00 USD | 3,110,000.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,330,000.00 USD | 4,330,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,200,000.00 USD | 3,200,000.00 USD | 30,250.00 USD | 24,670.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,540,000.00 USD | 4,540,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,390,000.00 USD | 3,390,000.00 USD | 133,770.00 USD | 17,580.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,450,000.00 USD | 3,450,000.00 USD | 38,620.00 USD | 156.67 USD | 23,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,870,000.00 USD | 4,870,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,510,000.00 USD | 3,510,000.00 USD | 27,320.00 USD | 18,490.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,180,000.00 USD | 5,180,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,580,000.00 USD | 3,580,000.00 USD | 58,810.00 USD | 7,400.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,480,000.00 USD | 5,480,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,600,000.00 USD | 3,600,000.00 USD | 10,930.00 USD | 4,240.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,850,000.00 USD | 5,850,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,620,000.00 USD | 3,620,000.00 USD | 4,130.00 USD | 3,730.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,290,000.00 USD | 6,290,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,660,000.00 USD | 3,660,000.00 USD | 14,730.00 USD | 11,600.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,480,000.00 USD | 6,480,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,680,000.00 USD | 3,680,000.00 USD | 5,920.00 USD | 6,310.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,750,000.00 USD | 6,750,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,700,000.00 USD | 3,700,000.00 USD | 10,810.00 USD | 5,210.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,270,000.00 USD | 7,270,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 3,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,720,000.00 USD | 3,720,000.00 USD | 5,810.00 USD | 6,880.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,470,000.00 USD | 7,470,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,800,000.00 USD | 3,800,000.00 USD | 58,390.00 USD | 4,140.00 USD | 17,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,780,000.00 USD | 7,780,000.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,820,000.00 USD | 3,820,000.00 USD | 10,080.00 USD | 523.25 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,980,000.00 USD | 7,980,000.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,840,000.00 USD | 3,840,000.00 USD | 17,580.00 USD | 1,000.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,210,000.00 USD | 8,210,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,860,000.00 USD | 3,860,000.00 USD | 11,390.00 USD | 4,410.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,610,000.00 USD | 8,610,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,890,000.00 USD | 3,890,000.00 USD | 22,480.00 USD | 3,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,070,000.00 USD | 9,070,000.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,900,000.00 USD | 3,900,000.00 USD | 1,670.00 USD | 3,600.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,340,000.00 USD | 9,340,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,920,000.00 USD | 3,920,000.00 USD | 12,300.00 USD | 2,270.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,630,000.00 USD | 9,630,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,930,000.00 USD | 3,930,000.00 USD | 9,600.00 USD | 1,900.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,840,000.00 USD | 9,840,000.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,950,000.00 USD | 3,950,000.00 USD | 7,240.00 USD | 3,310.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,060,000.00 USD | 10,060,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,960,000.00 USD | 3,960,000.00 USD | 6,210.00 USD | 2,970.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,350,000.00 USD | 10,350,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,980,000.00 USD | 3,980,000.00 USD | 14,210.00 USD | 3,170.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,580,000.00 USD | 10,580,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 4,000,000.00 USD | 4,000,000.00 USD | 5,480.00 USD | 1,390.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,820,000.00 USD | 10,820,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 4,010,000.00 USD | 4,010,000.00 USD | 4,340.00 USD | 5,200.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,010,000.00 USD | 11,010,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 4,020,000.00 USD | 4,020,000.00 USD | 7,570.00 USD | 3,480.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,160,000.00 USD | 11,160,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 4,040,000.00 USD | 4,040,000.00 USD | 7,630.00 USD | 4,280.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,400,000.00 USD | 11,400,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 4,050,000.00 USD | 4,050,000.00 USD | 7,980.00 USD | 2,510.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,620,000.00 USD | 11,620,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 4,050,000.00 USD | 4,050,000.00 USD | 2,060.00 USD | 690.13 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,830,000.00 USD | 11,830,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 4,080,000.00 USD | 4,080,000.00 USD | 17,750.00 USD | 3,900.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,980,000.00 USD | 11,980,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 4,100,000.00 USD | 4,100,000.00 USD | 3,730.00 USD | 3,730.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,210,000.00 USD | 12,210,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 4,100,000.00 USD | 4,100,000.00 USD | 1,820.00 USD | 1,630.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,390,000.00 USD | 12,390,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 4,120,000.00 USD | 4,120,000.00 USD | 11,930.00 USD | 2,470.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,520,000.00 USD | 12,520,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 4,120,000.00 USD | 4,120,000.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,680,000.00 USD | 12,680,000.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,850,000.00 USD | 12,850,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,000,000.00 USD | 13,000,000.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,320,000.00 USD | 13,320,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,500,000.00 USD | 13,500,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,730,000.00 USD | 13,730,000.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,790,000.00 USD | 13,790,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 13,900,000.00 USD | 13,900,000.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,080,000.00 USD | 14,080,000.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,240,000.00 USD | 14,240,000.00 USD | 77,150.00 USD | 18,350.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,340,000.00 USD | 14,340,000.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,390,000.00 USD | 14,390,000.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,540,000.00 USD | 14,540,000.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,600,000.00 USD | 14,600,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.12` | 78,920.00 USD | 82,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,710,000.00 USD | 14,710,000.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,800,000.00 USD | 14,800,000.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,860,000.00 USD | 14,860,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 14,880,000.00 USD | 14,880,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,010,000.00 USD | 15,010,000.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,220,000.00 USD | 15,220,000.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,320,000.00 USD | 15,320,000.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.13` | 1,480.00 USD | 84,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,410,000.00 USD | 15,410,000.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,430,000.00 USD | 15,430,000.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,470,000.00 USD | 15,470,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,520,000.00 USD | 15,520,000.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,590,000.00 USD | 15,590,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 86,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 109,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 120,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 634,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 3,420.00 USD | 637,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 638,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 639,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 779.81 USD | 640,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 292.58 USD | 640,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 649,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 649,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 247.76 USD | 649,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 333.04 USD | 650,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `0.7890` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `1D` | `0.7930` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 5,980.00 USD | 1,060.00 USD | 5,540.00 USD |
| `7D` | `0.7930` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD |
| `1D` | `0.7950` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,120.00 USD | 958.57 USD | 1,510.00 USD |
| `7D` | `0.7950` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD |
| `1D` | `0.7970` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 222.45 USD | 1,550.00 USD | 41.12 USD |
| `7D` | `0.7970` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `1D` | `0.7990` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,140.00 USD | 5.58 USD | 1,110.00 USD |
| `7D` | `0.7990` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `1D` | `0.8010` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 7.83 USD | 5.00 USD | 947.35 USD |
| `7D` | `0.8010` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `1D` | `0.8030` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 2,310.00 USD | 2,600.00 USD | 2,640.00 USD |
| `7D` | `0.8030` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `1D` | `0.8050` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,010.00 USD | 821.12 USD | 55.50 USD |
| `7D` | `0.8050` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `1D` | `0.8070` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 444.13 USD | 359.76 USD | 1,130.00 USD |
| `7D` | `0.8070` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD |
| `1D` | `0.8090` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 4,740.00 USD | 322.74 USD | 2,410.00 USD |
| `7D` | `0.8090` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `1D` | `0.8110` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,000.00 USD | 252.43 USD | 1,840.00 USD |
| `7D` | `0.8110` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `1D` | `0.8130` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,040.00 USD | 35.58 USD | 796.05 USD |
| `7D` | `0.8130` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD |
| `1D` | `0.8150` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 2,620.00 USD | 191.37 USD | 26.89 USD |
| `7D` | `0.8150` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD |
| `1D` | `0.8170` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 9,220.00 USD | 6.18 USD | 0.00 USD |
| `7D` | `0.8170` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD |
| `1D` | `0.8230` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 1,490.00 USD | 880.65 USD |
| `7D` | `0.8230` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD |
| `1D` | `0.8250` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 8,060.00 USD | 5,240.00 USD | 6,380.00 USD |
| `7D` | `0.8250` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `1D` | `0.8270` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD |
| `7D` | `0.8270` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD |
| `7D` | `0.8290` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD |
| `1D` | `0.8330` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 25,230.00 USD | 1,090.00 USD | 3,530.00 USD |
| `7D` | `0.8330` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD |
| `1D` | `0.8350` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 3,440.00 USD | 11,120.00 USD |
| `7D` | `0.8350` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8370` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 9,580.00 USD | 0.00 USD | 9,140.00 USD |
| `7D` | `0.8370` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD |
| `1D` | `0.8390` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8390` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8410` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8410` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `7D` | `0.8430` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8450` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD |
| `7D` | `0.8470` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD |
| `7D` | `0.8490` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD |
| `1D` | `0.8510` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 421.90 USD | 2,000.00 USD | 2,680.00 USD |
| `7D` | `0.8510` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD |
| `7D` | `0.8530` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8550` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8550` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8570` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8590` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 3,490.00 USD | 1,030.00 USD | 182.69 USD |
| `7D` | `0.8590` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `0.8610` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,980.00 USD | 24.95 USD | 251.39 USD |
| `7D` | `0.8610` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD |
| `1D` | `0.8630` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 3,170.00 USD | 111.70 USD | 2,010.00 USD |
| `7D` | `0.8630` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8650` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 5,670.00 USD | 1,930.00 USD | 1,790.00 USD |
| `7D` | `0.8650` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8670` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,670.00 USD | 1,590.00 USD | 1,990.00 USD |
| `7D` | `0.8670` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8690` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 14,770.00 USD | 3,720.00 USD | 8,610.00 USD |
| `7D` | `0.8690` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD |
| `1D` | `0.8710` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 12,380.00 USD | 1,850.00 USD | 2,990.00 USD |
| `7D` | `0.8710` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8730` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 29,740.00 USD | 3,080.00 USD | 8,610.00 USD |
| `7D` | `0.8730` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD |
| `1D` | `0.8750` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 6,210.00 USD | 2,690.00 USD | 2,930.00 USD |
| `7D` | `0.8750` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.8770` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 32,550.00 USD | 6,610.00 USD | 6,200.00 USD |
| `7D` | `0.8770` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 52,140.00 USD | 16,130.00 USD | 2,760.00 USD |
| `1D` | `0.8790` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 34,680.00 USD | 11,940.00 USD | 22,970.00 USD |
| `7D` | `0.8790` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8810` | 981,570.00 USD | 0.00 USD | 981,570.00 USD | 17,010.00 USD | 18,200.00 USD | 5,560.00 USD |
| `7D` | `0.8810` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8830` | 940,790.00 USD | 0.00 USD | 940,790.00 USD | 6,640.00 USD | 4,200.00 USD | 36.19 USD |
| `7D` | `0.8830` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 8,430.00 USD | 5,730.00 USD | 469.21 USD |
| `1D` | `0.8850` | 929,920.00 USD | 0.00 USD | 929,920.00 USD | 8,900.00 USD | 2,370.00 USD | 6,450.00 USD |
| `7D` | `0.8850` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD |
| `1D` | `0.8870` | 912,200.00 USD | 0.00 USD | 912,200.00 USD | 19,160.00 USD | 7,070.00 USD | 9,730.00 USD |
| `7D` | `0.8870` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8890` | 876,240.00 USD | 0.00 USD | 876,240.00 USD | 67,190.00 USD | 6,440.00 USD | 16,110.00 USD |
| `7D` | `0.8890` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 54,380.00 USD | 24,510.00 USD | 14,360.00 USD |
| `1D` | `0.8910` | 786,500.00 USD | 0.00 USD | 786,500.00 USD | 47,930.00 USD | 11,990.00 USD | 30,060.00 USD |
| `7D` | `0.8910` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD |
| `1D` | `0.8930` | 696,520.00 USD | 0.00 USD | 696,520.00 USD | 31,260.00 USD | 4,990.00 USD | 24,750.00 USD |
| `7D` | `0.8930` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 62,870.00 USD | 5,820.00 USD | 10,100.00 USD |
| `1D` | `0.8950` | 635,520.00 USD | 0.00 USD | 635,520.00 USD | 21,170.00 USD | 2,440.00 USD | 4,460.00 USD |
| `7D` | `0.8950` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD |
| `1D` | `0.8970` | 607,450.00 USD | 0.00 USD | 607,450.00 USD | 25,280.00 USD | 23,820.00 USD | 44,540.00 USD |
| `7D` | `0.8970` | 966,460.00 USD | 0.00 USD | 966,460.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD |
| `1D` | `0.8990` | 513,810.00 USD | 0.00 USD | 513,810.00 USD | 76,980.00 USD | 16,160.00 USD | 1,240.00 USD |
| `7D` | `0.8990` | 824,760.00 USD | 0.00 USD | 824,760.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD |
| `1D` | `0.9010` | 419,430.00 USD | 0.00 USD | 419,430.00 USD | 254.26 USD | 14,150.00 USD | 1,800.00 USD |
| `7D` | `0.9010` | 729,480.00 USD | 0.00 USD | 729,480.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD |
| `1D` | `0.9030` | 403,230.00 USD | 0.00 USD | 403,230.00 USD | 5,770.00 USD | 3,600.00 USD | 4,220.00 USD |
| `7D` | `0.9030` | 694,380.00 USD | 0.00 USD | 694,380.00 USD | 13,100.00 USD | 8,710.00 USD | 26,480.00 USD |
| `1D` | `0.9050` | 389,640.00 USD | 0.00 USD | 389,640.00 USD | 0.00 USD | 3,570.00 USD | 3,530.00 USD |
| `7D` | `0.9050` | 646,090.00 USD | 0.00 USD | 646,090.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD |
| `1D` | `0.9070` | 382,540.00 USD | 0.00 USD | 382,540.00 USD | 126,150.00 USD | 10,840.00 USD | 18,830.00 USD |
| `7D` | `0.9070` | 585,610.00 USD | 0.00 USD | 585,610.00 USD | 114,070.00 USD | 38,860.00 USD | 15,500.00 USD |
| `1D` | `0.9090` | 226,720.00 USD | 0.00 USD | 226,720.00 USD | 0.00 USD | 21,600.00 USD | 55,580.00 USD |
| `7D` | `0.9090` | 417,180.00 USD | 0.00 USD | 417,180.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD |
| `1D` | `0.9110` | 149,540.00 USD | 0.00 USD | 149,540.00 USD | 50,190.00 USD | 5,680.00 USD | 45,720.00 USD |
| `7D` | `0.9110` | 298,970.00 USD | 0.00 USD | 298,970.00 USD | 76,180.00 USD | 441.10 USD | 16,450.00 USD |
| `1D` | `0.9130` | 47,950.00 USD | 0.00 USD | 47,950.00 USD | 0.00 USD | 210.91 USD | 0.00 USD |
| `7D` | `0.9130` | 205,900.00 USD | 0.00 USD | 205,900.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD |
| `1D` | `0.9150` | 47,740.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD | 228.28 USD | 19,030.00 USD |
| `7D` | `0.9150` | 147,390.00 USD | 0.00 USD | 147,390.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD |
| `1D` | `0.9170` | 28,480.00 USD | 0.00 USD | 28,480.00 USD | 0.00 USD | 132.18 USD | 0.00 USD |
| `7D` | `0.9170` | 113,650.00 USD | 0.00 USD | 113,650.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9190` | 28,350.00 USD | 0.00 USD | 28,350.00 USD | 0.00 USD | 170.58 USD | 0.00 USD |
| `7D` | `0.9190` | 98,400.00 USD | 0.00 USD | 98,400.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `1D` | `0.9210` | 28,180.00 USD | 0.00 USD | 28,180.00 USD | 0.00 USD | 118.70 USD | 8,870.00 USD |
| `7D` | `0.9210` | 79,930.00 USD | 0.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `1D` | `0.9230` | 19,190.00 USD | 0.00 USD | 19,190.00 USD | 14,160.00 USD | 556.44 USD | 4,470.00 USD |
| `7D` | `0.9230` | 64,140.00 USD | 0.00 USD | 64,140.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD |
| `1D` | `0.9250` | 898.10 USD | 898.10 USD | 0.00 USD | 0.00 USD | 898.10 USD | 0.00 USD |
| `1D` | `0.9250` | 1,800.00 USD | 1,800.00 USD | 0.00 USD | 0.00 USD | 898.10 USD | 0.00 USD |
| `7D` | `0.9250` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9270` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 778.79 USD | 259.15 USD |
| `1D` | `0.9290` | 3,470.00 USD | 3,470.00 USD | 0.00 USD | 0.00 USD | 275.97 USD | 356.59 USD |
| `1D` | `0.9310` | 6,390.00 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 76.32 USD | 2,850.00 USD |
| `1D` | `0.9330` | 68,600.00 USD | 68,600.00 USD | 0.00 USD | 38,560.00 USD | 18,340.00 USD | 5,310.00 USD |
| `1D` | `0.9350` | 217,900.00 USD | 217,900.00 USD | 0.00 USD | 123,740.00 USD | 15,750.00 USD | 9,810.00 USD |
| `7D` | `0.9350` | 768.64 USD | 768.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | 768.64 USD |
| `1D` | `0.9370` | 290,120.00 USD | 290,120.00 USD | 0.00 USD | 45,940.00 USD | 14,450.00 USD | 11,830.00 USD |
| `7D` | `0.9370` | 18,870.00 USD | 18,870.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9390` | 346,560.00 USD | 346,560.00 USD | 0.00 USD | 53,820.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `0.9390` | 66,790.00 USD | 66,790.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 8,670.00 USD |
| `1D` | `0.9410` | 419,270.00 USD | 419,270.00 USD | 0.00 USD | 72,250.00 USD | 0.00 USD | 465.13 USD |
| `7D` | `0.9410` | 101,870.00 USD | 101,870.00 USD | 0.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.9430` | 444,520.00 USD | 444,520.00 USD | 0.00 USD | 20,020.00 USD | 5,230.00 USD | 0.00 USD |
| `7D` | `0.9430` | 159,880.00 USD | 159,880.00 USD | 0.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD |
| `1D` | `0.9450` | 659,100.00 USD | 659,100.00 USD | 0.00 USD | 190,140.00 USD | 5,610.00 USD | 18,830.00 USD |
| `7D` | `0.9450` | 530,900.00 USD | 530,900.00 USD | 0.00 USD | 261,930.00 USD | 38,000.00 USD | 71,090.00 USD |
| `1D` | `0.9470` | 856,530.00 USD | 856,530.00 USD | 0.00 USD | 120,750.00 USD | 21,110.00 USD | 55,580.00 USD |
| `7D` | `0.9470` | 808,010.00 USD | 808,010.00 USD | 0.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD |
| `1D` | `0.9490` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 147,280.00 USD | 5,080.00 USD | 45,720.00 USD |
| `7D` | `0.9490` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 193,040.00 USD | 0.00 USD | 178,870.00 USD |
| `1D` | `0.9510` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 71,040.00 USD | 3,830.00 USD | 3,250.00 USD |
| `7D` | `0.9510` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD |
| `1D` | `0.9530` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 25,510.00 USD | 9,830.00 USD | 56,200.00 USD |
| `7D` | `0.9530` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD |
| `1D` | `0.9550` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 11,050.00 USD | 14,910.00 USD | 16,230.00 USD |
| `7D` | `0.9550` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD |
| `1D` | `0.9570` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 865.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9570` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 469.21 USD |
| `1D` | `0.9590` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.25 USD |
| `7D` | `0.9590` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9610` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,830.00 USD | 2,760.00 USD | 232.57 USD |
| `7D` | `0.9610` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9630` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 65,790.00 USD | 2,800.00 USD | 10,450.00 USD |
| `7D` | `0.9630` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 53,510.00 USD | 19,000.00 USD | 481.70 USD |
| `1D` | `0.9650` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 497.80 USD | 20,140.00 USD | 40,150.00 USD |
| `7D` | `0.9650` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9670` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 25,900.00 USD | 2,540.00 USD | 22,860.00 USD |
| `7D` | `0.9670` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 38,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9690` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 82.70 USD | 326.35 USD |
| `7D` | `0.9690` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | 20,150.00 USD |
| `1D` | `0.9710` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 30,810.00 USD |
| `7D` | `0.9710` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.9730` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 39,840.00 USD | 5,170.00 USD | 14,000.00 USD |
| `7D` | `0.9730` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9750` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 25,480.00 USD | 11,090.00 USD | 17,210.00 USD |
| `7D` | `0.9750` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9770` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 76,840.00 USD | 5,820.00 USD | 9,980.00 USD |
| `7D` | `0.9770` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 26,770.00 USD |
| `7D` | `0.9790` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9810` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 376.40 USD | 8,420.00 USD |
| `7D` | `0.9810` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9830` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 15,980.00 USD | 20,640.00 USD | 28,830.00 USD |
| `7D` | `0.9830` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9850` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 38,470.00 USD | 4,330.00 USD | 19,350.00 USD |
| `7D` | `0.9850` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD |
| `1D` | `0.9870` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 12,080.00 USD | 3,550.00 USD | 15,120.00 USD |
| `7D` | `0.9870` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9890` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 23,610.00 USD | 0.00 USD | 20,110.00 USD |
| `7D` | `0.9890` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 51,270.00 USD | 1,520.00 USD | 20,230.00 USD |
| `7D` | `0.9910` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9930` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 15,020.00 USD | 15,830.00 USD | 1,290.00 USD |
| `7D` | `0.9930` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9950` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 16,320.00 USD | 1,630.00 USD | 329.08 USD |
| `7D` | `0.9950` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 33,860.00 USD | 2,480.00 USD | 5,580.00 USD |
| `7D` | `0.9970` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9990` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 33,110.00 USD | 8,690.00 USD | 6,480.00 USD |
| `7D` | `0.9990` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 156.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 41,520.00 USD | 24,950.00 USD | 348.39 USD |
| `7D` | `1.00` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 10,110.00 USD | 7,370.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD |
| `7D` | `1.00` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 47,140.00 USD | 11,580.00 USD | 50,050.00 USD |
| `7D` | `1.01` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 25,730.00 USD | 13,790.00 USD | 6,630.00 USD |
| `7D` | `1.01` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 7,380.00 USD | 26,630.00 USD | 155.80 USD |
| `7D` | `1.01` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 10,040.00 USD | 4,070.00 USD | 352.75 USD |
| `7D` | `1.01` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 26,070.00 USD | 4,370.00 USD | 40,290.00 USD |
| `7D` | `1.01` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 1,810.00 USD | 8,510.00 USD | 24,720.00 USD |
| `7D` | `1.02` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 64,600.00 USD | 3,790.00 USD | 13,570.00 USD |
| `7D` | `1.02` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 27,370.00 USD | 5,700.00 USD | 26,050.00 USD |
| `7D` | `1.02` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 63,820.00 USD | 5,700.00 USD | 49,890.00 USD |
| `7D` | `1.02` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 68,350.00 USD | 32,010.00 USD | 37,870.00 USD |
| `7D` | `1.02` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD |
| `7D` | `1.03` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 30,250.00 USD | 24,670.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 133,770.00 USD | 17,580.00 USD | 40,480.00 USD |
| `7D` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 38,620.00 USD | 156.67 USD | 23,160.00 USD |
| `7D` | `1.03` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 27,320.00 USD | 18,490.00 USD | 11,550.00 USD |
| `7D` | `1.03` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 58,810.00 USD | 7,400.00 USD | 6,600.00 USD |
| `7D` | `1.04` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 10,930.00 USD | 4,240.00 USD | 6,400.00 USD |
| `7D` | `1.04` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 4,130.00 USD | 3,730.00 USD | 8,370.00 USD |
| `7D` | `1.04` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 14,730.00 USD | 11,600.00 USD | 12,970.00 USD |
| `7D` | `1.04` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 5,920.00 USD | 6,310.00 USD | 8,710.00 USD |
| `7D` | `1.04` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 10,810.00 USD | 5,210.00 USD | 1,570.00 USD |
| `7D` | `1.05` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 5,810.00 USD | 6,880.00 USD | 11,530.00 USD |
| `7D` | `1.05` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 58,390.00 USD | 4,140.00 USD | 17,510.00 USD |
| `7D` | `1.05` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD |
| `1D` | `1.05` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 10,080.00 USD | 523.25 USD | 3,560.00 USD |
| `7D` | `1.05` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 17,580.00 USD | 1,000.00 USD | 8,480.00 USD |
| `7D` | `1.05` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 11,390.00 USD | 4,410.00 USD | 3,290.00 USD |
| `7D` | `1.06` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD |
| `1D` | `1.06` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 22,480.00 USD | 3,010.00 USD | 0.00 USD |
| `7D` | `1.06` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD |
| `1D` | `1.06` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 1,670.00 USD | 3,600.00 USD | 7,860.00 USD |
| `7D` | `1.06` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 12,300.00 USD | 2,270.00 USD | 1,880.00 USD |
| `7D` | `1.06` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `1D` | `1.06` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 9,600.00 USD | 1,900.00 USD | 2,990.00 USD |
| `7D` | `1.06` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `1D` | `1.07` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 7,240.00 USD | 3,310.00 USD | 8,610.00 USD |
| `7D` | `1.07` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 6,210.00 USD | 2,970.00 USD | 2,930.00 USD |
| `7D` | `1.07` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 14,210.00 USD | 3,170.00 USD | 4,000.00 USD |
| `7D` | `1.07` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 5,480.00 USD | 1,390.00 USD | 4,210.00 USD |
| `7D` | `1.07` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 4,340.00 USD | 5,200.00 USD | 2,800.00 USD |
| `7D` | `1.07` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 7,570.00 USD | 3,480.00 USD | 5,560.00 USD |
| `7D` | `1.08` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 7,630.00 USD | 4,280.00 USD | 36.19 USD |
| `7D` | `1.08` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 7,980.00 USD | 2,510.00 USD | 2,160.00 USD |
| `7D` | `1.08` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `1D` | `1.08` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 2,060.00 USD | 690.13 USD | 2,730.00 USD |
| `7D` | `1.08` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `1D` | `1.08` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 17,750.00 USD | 3,900.00 USD | 7,170.00 USD |
| `7D` | `1.08` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 3,730.00 USD | 3,730.00 USD | 6,690.00 USD |
| `7D` | `1.09` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD |
| `1D` | `1.09` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 1,820.00 USD | 1,630.00 USD | 2,270.00 USD |
| `7D` | `1.09` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `1D` | `1.09` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 11,930.00 USD | 2,470.00 USD | 1,890.00 USD |
| `7D` | `1.09` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD |
| `7D` | `1.09` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `7D` | `1.09` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD |
| `7D` | `1.10` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 77,150.00 USD | 18,350.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,320,000.00 USD | 15,320,000.00 USD | 0.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,410,000.00 USD | 15,410,000.00 USD | 0.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `197.63M` | Total OI Tokens: `212,997,327.4 DOT`
  * 1h OI Change: `+3.05%` | 4h OI Change: `-5.60%` | 24h OI Change: `-10.88%`
  * Exchange Breakdown: Binance=`34.87M` | Bybit=`22.45M` | OKX=`9.86M` | Hyperliquid=`5.43M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.64K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0054%` | **USDT OKX** | `-0.0058%` |
| **USDT Bybit** | `0.0029%` | **USDT KuCoin** | `-0.0002%` |
| **USDT MEXC** | `-0.0053%` | **USDT BingX** | `0.0031%` |
| **USDT Gate** | `-0.0064%` | **USDT Bitget** | `-0.0119%` |
| **CoinM Binance** | `-0.0011%` | **CoinM OKX** | `0.0093%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `47.31%` | `52.69%` | `0.90` | 44,760,000.00 USD |
| `15M` | `Binance` | `50.5%` | `49.5%` | `1.02` | 17,410,000.00 USD |
| `15M` | `OKX` | `42.92%` | `57.08%` | `0.75` | 4,030,000.00 USD |
| `15M` | `Bybit` | `44.09%` | `55.91%` | `0.79` | 8,580,000.00 USD |
| `15M` | `KuCoin` | `42.53%` | `57.47%` | `0.74` | 238,580.00 USD |
| `15M` | `Gate` | `49.1%` | `50.9%` | `0.96` | 408,630.00 USD |
| `15M` | `Bitget` | `46.73%` | `53.27%` | `0.88` | 1,880,000.00 USD |
| `15M` | `BingX` | `40.82%` | `59.18%` | `0.69` | 1,120,000.00 USD |
| `15M` | `MEXC` | `54.38%` | `45.62%` | `1.19` | 2,690,000.00 USD |
| `15M` | `Bitunix` | `51.05%` | `48.95%` | `1.04` | 826,550.00 USD |
| `15M` | `Hyperliquid` | `35.43%` | `64.57%` | `0.55` | 5,370,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.63%` | `41.37%` | `1.42` | 296,960.00 USD |
| `15M` | `Crypto.com` | `59.64%` | `40.36%` | `1.48` | 1,960.00 USD |
| `15M` | `WhiteBIT` | `79.69%` | `20.31%` | `3.92` | 1,060,000.00 USD |
| `15M` | `HTX` | `41.51%` | `58.49%` | `0.71` | 39,890.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `52.65%` | `47.35%` | `1.11` | 497,080.00 USD |
| `15M` | `Aster` | `40.61%` | `59.39%` | `0.68` | 173,340.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.37%` | `43.63%` | `1.29` | 132,120.00 USD |
| `15M` | `Whale Positions` | `50.5%` | `49.5%` | `1.02` | 17,410,000.00 USD |
| `15M` | `Global Accounts` | `47.31%` | `52.69%` | `0.90` | 44,760,000.00 USD |
| `1H` | `DOT` | `46.85%` | `53.15%` | `0.88` | 66,900,000.00 USD |
| `1H` | `Binance` | `43.32%` | `56.68%` | `0.76` | 23,770,000.00 USD |
| `1H` | `OKX` | `48.98%` | `51.02%` | `0.96` | 6,550,000.00 USD |
| `1H` | `Bybit` | `40.71%` | `59.29%` | `0.69` | 6,310,000.00 USD |
| `1H` | `KuCoin` | `48.48%` | `51.52%` | `0.94` | 493,080.00 USD |
| `1H` | `Gate` | `50.75%` | `49.25%` | `1.03` | 850,720.00 USD |
| `1H` | `Bitget` | `42.86%` | `57.14%` | `0.75` | 1,940,000.00 USD |
| `1H` | `BingX` | `42.64%` | `57.36%` | `0.74` | 1,450,000.00 USD |
| `1H` | `MEXC` | `49.09%` | `50.91%` | `0.96` | 14,140,000.00 USD |
| `1H` | `Bitunix` | `44.77%` | `55.23%` | `0.81` | 2,710,000.00 USD |
| `1H` | `Hyperliquid` | `50.36%` | `49.64%` | `1.01` | 4,780,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.97%` | `49.03%` | `1.04` | 1,580,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.83%` | `1.17%` | `84.47` | 1,440,000.00 USD |
| `1H` | `HTX` | `51.76%` | `48.24%` | `1.07` | 15,900.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.97%` | `64.03%` | `0.56` | 439,720.00 USD |
| `1H` | `Aster` | `67.49%` | `32.51%` | `2.08` | 157,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.03%` | `68.97%` | `0.45` | 275,270.00 USD |
| `1H` | `Whale Positions` | `43.32%` | `56.68%` | `0.76` | 23,770,000.00 USD |
| `1H` | `Global Accounts` | `46.85%` | `53.15%` | `0.88` | 66,900,000.00 USD |
| `4H` | `DOT` | `46.80%` | `53.20%` | `0.88` | 107,470,000.00 USD |
| `4H` | `Binance` | `44.18%` | `55.82%` | `0.79` | 40,050,000.00 USD |
| `4H` | `OKX` | `50.13%` | `49.87%` | `1.01` | 11,890,000.00 USD |
| `4H` | `Bybit` | `44.14%` | `55.86%` | `0.79` | 12,170,000.00 USD |
| `4H` | `KuCoin` | `48.17%` | `51.83%` | `0.93` | 2,700,000.00 USD |
| `4H` | `Gate` | `53.51%` | `46.49%` | `1.15` | 9,980,000.00 USD |
| `4H` | `Bitget` | `48.15%` | `51.85%` | `0.93` | 5,110,000.00 USD |
| `4H` | `BingX` | `43.8%` | `56.2%` | `0.78` | 3,170,000.00 USD |
| `4H` | `MEXC` | `45.01%` | `54.99%` | `0.82` | 6,490,000.00 USD |
| `4H` | `Bitunix` | `47.27%` | `52.73%` | `0.90` | 2,790,000.00 USD |
| `4H` | `Hyperliquid` | `50.72%` | `49.28%` | `1.03` | 1,910,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.6%` | `50.4%` | `0.98` | 8,630,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `50.44%` | `49.56%` | `1.02` | 1,820,000.00 USD |
| `4H` | `HTX` | `53.26%` | `46.74%` | `1.14` | 130,010.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.03%` | `49.97%` | `1.00` | 515,780.00 USD |
| `4H` | `Aster` | `43.72%` | `56.28%` | `0.78` | 106,710.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `44.18%` | `55.82%` | `0.79` | 40,050,000.00 USD |
| `4H` | `Global Accounts` | `46.80%` | `53.20%` | `0.88` | 107,470,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9858` | `0.9859` | `0.9858` | `0.9880` | `0.9839` | 388,071.33 USD | 177,551.18 USD | 210,520.15 USD | -32,968.97 USD | `-8.50%` | `3B / 8S` |
| `0:00 UTC` | `0.9681` | `0.9669` | `0.9681` | `0.9851` | `0.9557` | 3,728,299.49 USD | 1,667,776.70 USD | 2,060,522.79 USD | -392,746.09 USD | `-10.53%` | `7B / 26S` |
| `5:00 UTC` | `0.9681` | `0.9687` | `0.9681` | `0.9718` | `0.9650` | 792,721.03 USD | 373,256.63 USD | 419,464.39 USD | -46,207.76 USD | `-5.83%` | `5B / 11S` |
| `0:00 UTC` | `0.9271` | `0.9372` | `0.9271` | `0.9707` | `0.9107` | 10,294,158.77 USD | 4,127,124.83 USD | 6,167,033.94 USD | -2,039,909.11 USD | `-19.82%` | `5B / 37S` |
| `5:00 UTC` | `0.9157` | `0.9093` | `0.9157` | `0.9241` | `0.8893` | 9,166,573.96 USD | 4,231,807.53 USD | 4,934,766.43 USD | -702,958.89 USD | `-7.67%` | `6B / 13S` |
| `0:00 UTC` | `0.9138` | `0.9204` | `0.9138` | `0.9302` | `0.9076` | 3,388,598.53 USD | 1,615,651.50 USD | 1,772,947.04 USD | -157,295.54 USD | `-4.64%` | `11B / 8S` |
| `5:00 UTC` | `0.9302` | `0.9320` | `0.9302` | `0.9392` | `0.9254` | 2,028,309.51 USD | 996,075.55 USD | 1,032,233.96 USD | -36,158.40 USD | `-1.78%` | `11B / 12S` |
| `0:00 UTC` | `0.9301` | `0.9318` | `0.9301` | `0.9381` | `0.9248` | 1,862,169.82 USD | 558,080.50 USD | 1,304,089.32 USD | -746,008.82 USD | `-40.06%` | `17B / 36S` |
| `5:00 UTC` | `0.9251` | `0.9254` | `0.9251` | `0.9294` | `0.9219` | 1,343,196.16 USD | 526,839.48 USD | 816,356.69 USD | -289,517.21 USD | `-21.55%` | `18B / 7S` |
| `0:00 UTC` | `0.9254` | `0.9243` | `0.9254` | `0.9278` | `0.9211` | 370,152.94 USD | 232,125.90 USD | 138,027.04 USD | 94,098.86 USD | `+25.42%` | `19B / 3S` |

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
| `5m` | 13,310.00 USD | 197,730.00 USD | **`ACCUMULATION`** |
| `15m` | 1,040.00 USD | 146,060.00 USD | **`ACCUMULATION`** |
| `30m` | -41,640.00 USD | -778,120.00 USD | **`DISTRIBUTION`** |
| `1h` | 77,480.00 USD | -263,150.00 USD | **`DISTRIBUTION`** |
| `2h` | -828,290.00 USD | -5,830,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -936,200.00 USD | -5,920,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,010,000.00 USD | -7,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -985,170.00 USD | -7,770,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,140,000.00 USD | -8,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,160,000.00 USD | -7,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,250,000.00 USD | -25,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,560,000.00 USD | -78,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+13.31K` | 15m=`+1.04K` | 1h=`+77.48K` | 24h=`-1.16M`
* Futures Capital Netflows: 5m=`+197.73K` | 15m=`+146.06K` | 1h=`-263.15K` | 24h=`-7.52M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9111` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8638` (Risk Distance: `0.0473` pts)
  * +2.5R Take Profit: `1.03`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9236` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9709` (Risk Distance: `0.0473` pts)
  * +2.5R Take Profit: `0.8053`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9269`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
