# 🏛️ SOVEREIGN CANDIDATE DOSSIER: FILUSD
**Canonical Key**: `FILUSD` | **Broker Instrument**: `FILUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.8920` | **Live Ask Quote**: `0.9320` | **Mid Price**: `0.9120`
- **Spread Points**: `40.00` | **Spread BPS**: `438.60 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.8706` | VWAP Z-Score: `+1.26` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0058` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `64.72` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9170` | Lower -3.00σ Band: `0.8241`
  * Upper +2.51σ Band: `0.9094` | Lower -2.51σ Band: `0.8317`
  * Upper +2.01σ Band: `0.9017` | Lower -2.01σ Band: `0.8394`
  * Upper +2.00σ Band: `0.9015` | Lower -2.00σ Band: `0.8396`
  * Upper +1.28σ Band: `0.8904` | Lower -1.28σ Band: `0.8507`
  * Upper +1.00σ Band: `0.8860` | Lower -1.00σ Band: `0.8551`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.8885` | EMA-20=`0.8827` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.8766` (Slope: `+0.0000`) | EMA-100=`0.8769`
  * Institutional Anchors: EMA-144=`0.8782` | EMA-200=`0.8788` (Slope: `+0.1366`) | EMA-233=`0.8797`
- **Range Boundaries**: 24H High=`0.9140` | 24H Low=`0.8450` | Weekly High=`0.9140` | Weekly Low=`0.8450`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9020` (Distance: `+1.06%`)
  * Point of Control (POC) = `0.8930` (Distance: `+2.14%`)
  * Value Area Low (VAL) = `0.8600` (Distance: `+6.11%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9010` | POC=`0.8920` | VAL=`0.8740`
  * Prior Day Extremes: PDH=`0.9140` | PDL=`0.8570` | PDC=`0.9010`
  * Monday Range Blueprint: High=`0.9120` | Mid=`0.8950` | Low=`0.8780`
  * Developing Weekly Value Area: Weekly VAH=`0.9000` | Weekly POC=`0.8940` | Weekly VAL=`0.8730`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9100` | Low=`0.8470`
  * London Session (08:00-16:00 UTC): High=`0.8950` | Low=`0.8450`
  * New York Session (13:00-21:00 UTC): High=`0.8950` | Low=`0.8690`
  * Initial Balance (First Hour): IB High=`0.8720` | IB Low=`0.8550`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9084` - `0.9156`
  * Optimal Trade Entry (OTE 0.705): `0.9138`
  * Structural Invalidation Anchor (0.786): `0.9193`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1264` | `0xeadc...9d55` | `LONG` | 1,821,040.00 USD | `2,000,000.00` | `0.9824` | `0.9105` | `0.000000` | -143,726.39 USD | `-7.89%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9199` (Vol: 164,827.92 USD, Dist: `+2.24%`) | Long MP=`0.8731` (Vol: 103,312.89 USD, Dist: `--2.97%`)
  * 48H Horizon: Short MP=`0.9355` (Vol: 183,913.24 USD, Dist: `+3.97%`) | Long MP=`0.8732` (Vol: 123,658.99 USD, Dist: `--2.96%`)
  * 3D Horizon: Short MP=`0.9341` (Vol: 290,792.11 USD, Dist: `+3.81%`) | Long MP=`0.8782` (Vol: 163,059.73 USD, Dist: `--2.40%`)
  * 7D Horizon: Short MP=`1.02` (Vol: 374,142.31 USD, Dist: `+14.12%`) | Long MP=`0.8793` (Vol: 266,420.52 USD, Dist: `--1.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2075` | 635,930.00 USD | 0.00 USD | 499.35 USD | `-77.21%` | `2,406.50` |
| `Live` | `Long` | `0.3235` | 635,430.00 USD | 0.00 USD | 1,200.00 USD | `-64.46%` | `3,722.90` |
| `Live` | `Long` | `0.3945` | 634,230.00 USD | 0.00 USD | 198.79 USD | `-56.67%` | `503.90` |
| `Live` | `Long` | `0.4335` | 634,030.00 USD | 0.00 USD | 679.64 USD | `-52.38%` | `1,567.80` |
| `Live` | `Long` | `0.4505` | 633,350.00 USD | 0.00 USD | 183.49 USD | `-50.51%` | `407.30` |
| `Live` | `Long` | `0.4815` | 633,170.00 USD | 0.00 USD | 22,220.00 USD | `-47.11%` | `46,144.20` |
| `Live` | `Long` | `0.4855` | 610,950.00 USD | 0.00 USD | 6,570.00 USD | `-46.67%` | `13,538.60` |
| `Live` | `Long` | `0.5035` | 604,380.00 USD | 0.00 USD | 298.32 USD | `-44.69%` | `592.50` |
| `Live` | `Long` | `0.5075` | 604,080.00 USD | 0.00 USD | 113.58 USD | `-44.25%` | `223.80` |
| `Live` | `Long` | `0.5185` | 603,970.00 USD | 0.00 USD | 19,360.00 USD | `-43.04%` | `37,340.70` |
| `Live` | `Long` | `0.5275` | 584,600.00 USD | 0.00 USD | 192.01 USD | `-42.06%` | `364.00` |
| `Live` | `Long` | `0.5315` | 584,410.00 USD | 0.00 USD | 72,770.00 USD | `-41.62%` | `136,914.00` |
| `Live` | `Long` | `0.5325` | 511,640.00 USD | 0.00 USD | 1,550.00 USD | `-41.51%` | `2,908.40` |
| `Live` | `Long` | `0.5705` | 510,090.00 USD | 0.00 USD | 1,800.00 USD | `-37.33%` | `3,156.20` |
| `Live` | `Long` | `0.5745` | 508,290.00 USD | 0.00 USD | 104.56 USD | `-36.89%` | `182.00` |
| `Live` | `Long` | `0.5755` | 508,190.00 USD | 0.00 USD | 393.47 USD | `-36.78%` | `683.70` |
| `Live` | `Long` | `0.5915` | 507,790.00 USD | 0.00 USD | 101.56 USD | `-35.02%` | `171.70` |
| `Live` | `Long` | `0.5995` | 507,690.00 USD | 0.00 USD | 4,800.00 USD | `-34.15%` | `8,001.00` |
| `Live` | `Long` | `0.6145` | 502,900.00 USD | 0.00 USD | 1,230.00 USD | `-32.50%` | `2,000.00` |
| `Live` | `Long` | `0.6165` | 501,670.00 USD | 0.00 USD | 1,400.00 USD | `-32.28%` | `2,267.00` |
| `Live` | `Long` | `0.6225` | 500,270.00 USD | 0.00 USD | 5,600.00 USD | `-31.62%` | `9,000.50` |
| `Live` | `Long` | `0.6235` | 494,670.00 USD | 0.00 USD | 2,660.00 USD | `-31.51%` | `4,259.90` |
| `Live` | `Long` | `0.6295` | 492,010.00 USD | 0.00 USD | 1,960.00 USD | `-30.85%` | `3,114.10` |
| `Live` | `Long` | `0.6315` | 490,050.00 USD | 0.00 USD | 8,920.00 USD | `-30.63%` | `14,131.00` |
| `Live` | `Long` | `0.6335` | 481,130.00 USD | 0.00 USD | 393.15 USD | `-30.41%` | `620.60` |
| `Live` | `Long` | `0.6345` | 480,730.00 USD | 0.00 USD | 1,220.00 USD | `-30.30%` | `1,930.50` |
| `Live` | `Long` | `0.6355` | 479,510.00 USD | 0.00 USD | 118.33 USD | `-30.19%` | `186.20` |
| `Live` | `Long` | `0.6405` | 479,390.00 USD | 0.00 USD | 194.26 USD | `-29.64%` | `303.30` |
| `Live` | `Long` | `0.6435` | 479,200.00 USD | 0.00 USD | 3,240.00 USD | `-29.31%` | `5,033.00` |
| `Live` | `Long` | `0.6445` | 475,960.00 USD | 0.00 USD | 286.22 USD | `-29.20%` | `444.10` |
| `Live` | `Long` | `0.6515` | 475,670.00 USD | 0.00 USD | 651.50 USD | `-28.43%` | `1,000.00` |
| `Live` | `Long` | `0.6595` | 475,020.00 USD | 0.00 USD | 5,940.00 USD | `-27.56%` | `9,000.00` |
| `Live` | `Long` | `0.6745` | 469,080.00 USD | 0.00 USD | 112.17 USD | `-25.91%` | `166.30` |
| `Live` | `Long` | `0.6765` | 468,970.00 USD | 0.00 USD | 853.27 USD | `-25.69%` | `1,261.30` |
| `Live` | `Long` | `0.6805` | 468,120.00 USD | 0.00 USD | 204,150.00 USD | `-25.25%` | `300,000.00` |
| `Live` | `Long` | `0.6855` | 263,970.00 USD | 0.00 USD | 11,100.00 USD | `-24.70%` | `16,194.90` |
| `Live` | `Long` | `0.6865` | 252,870.00 USD | 0.00 USD | 3,820.00 USD | `-24.59%` | `5,566.40` |
| `Live` | `Long` | `0.6885` | 249,050.00 USD | 0.00 USD | 303.08 USD | `-24.37%` | `440.20` |
| `Live` | `Long` | `0.6935` | 248,740.00 USD | 0.00 USD | 927.42 USD | `-23.82%` | `1,337.30` |
| `Live` | `Long` | `0.6945` | 247,820.00 USD | 0.00 USD | 4,620.00 USD | `-23.71%` | `6,652.80` |
| `Live` | `Long` | `0.7005` | 243,200.00 USD | 0.00 USD | 779.94 USD | `-23.05%` | `1,113.40` |
| `Live` | `Long` | `0.7015` | 242,420.00 USD | 0.00 USD | 445.45 USD | `-22.94%` | `635.00` |
| `Live` | `Long` | `0.7085` | 241,970.00 USD | 0.00 USD | 816.62 USD | `-22.17%` | `1,152.60` |
| `Live` | `Long` | `0.7245` | 241,150.00 USD | 0.00 USD | 1,450.00 USD | `-20.42%` | `1,994.50` |
| `Live` | `Long` | `0.7285` | 239,710.00 USD | 0.00 USD | 1,730.00 USD | `-19.98%` | `2,375.60` |
| `Live` | `Long` | `0.7385` | 237,980.00 USD | 0.00 USD | 480.47 USD | `-18.88%` | `650.60` |
| `Live` | `Long` | `0.7445` | 237,500.00 USD | 0.00 USD | 6,040.00 USD | `-18.22%` | `8,114.70` |
| `Live` | `Long` | `0.7465` | 231,460.00 USD | 0.00 USD | 1,050.00 USD | `-18.00%` | `1,403.50` |
| `Live` | `Long` | `0.7545` | 230,410.00 USD | 0.00 USD | 21,150.00 USD | `-17.12%` | `28,037.30` |
| `Live` | `Long` | `0.7555` | 209,250.00 USD | 0.00 USD | 1,410.00 USD | `-17.01%` | `1,872.90` |
| `Live` | `Long` | `0.7625` | 207,840.00 USD | 0.00 USD | 5,620.00 USD | `-16.24%` | `7,376.40` |
| `Live` | `Long` | `0.7655` | 202,210.00 USD | 0.00 USD | 2,860.00 USD | `-15.91%` | `3,730.40` |
| `Live` | `Long` | `0.7665` | 199,360.00 USD | 0.00 USD | 616.19 USD | `-15.80%` | `803.90` |
| `Live` | `Long` | `0.7675` | 198,740.00 USD | 0.00 USD | 11,430.00 USD | `-15.69%` | `14,886.60` |
| `Live` | `Long` | `0.7775` | 187,320.00 USD | 0.00 USD | 753.24 USD | `-14.59%` | `968.80` |
| `Live` | `Long` | `0.7795` | 186,560.00 USD | 0.00 USD | 7,460.00 USD | `-14.37%` | `9,569.30` |
| `Live` | `Long` | `0.7835` | 179,100.00 USD | 0.00 USD | 5,320.00 USD | `-13.93%` | `6,795.00` |
| `Live` | `Long` | `0.7915` | 173,780.00 USD | 0.00 USD | 135.98 USD | `-13.06%` | `171.80` |
| `Live` | `Long` | `0.7945` | 173,640.00 USD | 0.00 USD | 7,540.00 USD | `-12.73%` | `9,489.00` |
| `Live` | `Long` | `0.7955` | 166,110.00 USD | 0.00 USD | 8,040.00 USD | `-12.62%` | `10,103.00` |
| `Live` | `Long` | `0.7975` | 158,070.00 USD | 0.00 USD | 116,200.00 USD | `-12.40%` | `145,704.90` |
| `Live` | `Long` | `0.7985` | 41,870.00 USD | 0.00 USD | 1,650.00 USD | `-12.29%` | `2,063.00` |
| `Live` | `Long` | `0.8045` | 40,220.00 USD | 0.00 USD | 20,830.00 USD | `-11.63%` | `25,889.90` |
| `Live` | `Long` | `0.8095` | 19,390.00 USD | 0.00 USD | 161.09 USD | `-11.08%` | `199.00` |
| `Live` | `Long` | `0.8115` | 19,230.00 USD | 0.00 USD | 194.92 USD | `-10.86%` | `240.20` |
| `Live` | `Long` | `0.8135` | 19,040.00 USD | 0.00 USD | 512.26 USD | `-10.64%` | `629.70` |
| `Live` | `Long` | `0.8145` | 18,530.00 USD | 0.00 USD | 1,140.00 USD | `-10.53%` | `1,398.50` |
| `Live` | `Long` | `0.8155` | 17,390.00 USD | 0.00 USD | 9,730.00 USD | `-10.42%` | `11,933.80` |
| `Live` | `Long` | `0.8185` | 7,650.00 USD | 0.00 USD | 5,810.00 USD | `-10.09%` | `7,104.30` |
| `Live` | `Long` | `0.8215` | 1,840.00 USD | 0.00 USD | 498.08 USD | `-9.76%` | `606.30` |
| `Live` | `Long` | `0.8395` | 1,340.00 USD | 0.00 USD | 210.46 USD | `-7.78%` | `250.70` |
| `Live` | `Long` | `0.8445` | 1,130.00 USD | 0.00 USD | 742.65 USD | `-7.23%` | `879.40` |
| `Live` | `Long` | `0.8525` | 388.13 USD | 0.00 USD | 226.00 USD | `-6.35%` | `265.10` |
| `Live` | `Long` | `0.8615` | 162.13 USD | 0.00 USD | 162.13 USD | `-5.37%` | `188.20` |
| `Live` | `Short` | `0.9875` | 536.41 USD | 536.41 USD | 0.00 USD | `+8.47%` | `543.20` |
| `Live` | `Short` | `0.9945` | 3,800.00 USD | 3,260.00 USD | 0.00 USD | `+9.24%` | `3,280.60` |
| `Live` | `Short` | `1.00` | 3,920.00 USD | 122.05 USD | 0.00 USD | `+10.34%` | `121.50` |
| `Live` | `Short` | `1.01` | 11,640.00 USD | 7,720.00 USD | 0.00 USD | `+10.67%` | `7,663.40` |
| `Live` | `Short` | `1.22` | 14,670.00 USD | 3,030.00 USD | 0.00 USD | `+33.85%` | `2,483.50` |
| `Live` | `Short` | `1.27` | 14,810.00 USD | 138.38 USD | 0.00 USD | `+39.45%` | `109.00` |
| `Live` | `Short` | `1.41` | 14,950.00 USD | 140.55 USD | 0.00 USD | `+54.39%` | `100.00` |
| `Live` | `Short` | `1.65` | 15,140.00 USD | 192.90 USD | 0.00 USD | `+81.41%` | `116.80` |
| `Live` | `Short` | `1.77` | 17,820.00 USD | 2,680.00 USD | 0.00 USD | `+94.82%` | `1,508.40` |
| `Live` | `Short` | `1.80` | 18,480.00 USD | 661.47 USD | 0.00 USD | `+97.34%` | `368.20` |

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
  * Current Rate: `7.66K` | Last 24h: `-5.96K` | Last 3d: `13.02K` | Last 7d: `-32.57K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0095%` | **USDT OKX** | `0.0018%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0037%` | **USDT Bitget** | `0.0100%` |
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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 10,000.00 USD | -103,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -14,520.00 USD | -68,270.00 USD | **`DISTRIBUTION`** |
| `30m` | -8,540.00 USD | -760,210.00 USD | **`DISTRIBUTION`** |
| `1h` | -42,270.00 USD | -812,180.00 USD | **`DISTRIBUTION`** |
| `2h` | 13,030.00 USD | -96,050.00 USD | **`DISTRIBUTION`** |
| `4h` | -186,860.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 33,790.00 USD | 850,290.00 USD | **`ACCUMULATION`** |
| `8h` | -418,950.00 USD | -200,200.00 USD | **`DISTRIBUTION`** |
| `12h` | -763,630.00 USD | -756,460.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,280,000.00 USD | -2,810,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -11,200,000.00 USD | -45,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -51,420,000.00 USD | -299,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.00K` | 15m=`-14.52K` | 1h=`-42.27K` | 24h=`-1.28M`
* Futures Capital Netflows: 5m=`-103.87K` | 15m=`-68.27K` | 1h=`-812.18K` | 24h=`-2.81M`
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
  * Execution Entry: `0.8600` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.7930` (Risk Distance: `0.0800` pts)
  * +2.5R Take Profit: `1.06`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9020` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9690` (Risk Distance: `0.0800` pts)
  * +2.5R Take Profit: `0.7020`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9193`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
