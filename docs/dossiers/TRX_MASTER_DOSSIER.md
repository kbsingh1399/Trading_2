# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:49:57 IST` (`2026-10-30 05:19:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3412` | **Live Ask Quote**: `0.3438` | **Mid Price**: `0.3425`
- **Spread Points**: `26.00` | **Spread BPS**: `75.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3521` | VWAP Z-Score: `-2.20` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0041` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.04` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3627` | Lower -3.00σ Band: `0.3416`
  * Upper +2.51σ Band: `0.3609` | Lower -2.51σ Band: `0.3433`
  * Upper +2.01σ Band: `0.3592` | Lower -2.01σ Band: `0.3451`
  * Upper +2.00σ Band: `0.3592` | Lower -2.00σ Band: `0.3451`
  * Upper +1.28σ Band: `0.3566` | Lower -1.28σ Band: `0.3476`
  * Upper +1.00σ Band: `0.3556` | Lower -1.00σ Band: `0.3486`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3471` | EMA-20=`0.3483` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3444` (Slope: `+0.0000`) | EMA-100=`0.3395`
  * Institutional Anchors: EMA-144=`0.3372` | EMA-200=`0.3354` (Slope: `+0.5263`) | EMA-233=`0.3346`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3570` (Distance: `-4.09%`)
  * Point of Control (POC) = `0.3512` (Distance: `-2.53%`)
  * Value Area Low (VAL) = `0.3453` (Distance: `-0.85%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3479` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3410`
  * New York Session (13:00-21:00 UTC): High=`0.3446` | Low=`0.3404`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3410`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3411` - `0.3439`
  * Optimal Trade Entry (OTE 0.705): `0.3432`
  * Structural Invalidation Anchor (0.786): `0.3452`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3458` | `0.3460` | `0.3417` | `0.3422` | `9,921,092` | 3,405,492.73 USD | -1,387,277.34 USD | `-40.74%` | 3,161,077.15 USD | `-3.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3422` | `0.3426` | `0.3414` | `0.3422` | `3,363,151` | 1,149,721.47 USD | -158,617.17 USD | `-13.80%` | 3,002,459.98 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3422` | `0.3432` | `0.3419` | `0.3422` | `1,047,829` | 358,786.14 USD | 22,563.59 USD | `+6.29%` | 3,025,023.57 USD | `+0.33` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3449` | `0.3482` | `0.3449` | `0.3472` | `8,355,971` | 2,895,955.74 USD | 462,205.98 USD | `+15.96%` | 4,361,600.88 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3472` | `0.3487` | `0.3457` | `0.3458` | `7,743,490` | 2,690,622.76 USD | 186,753.61 USD | `+6.94%` | 4,548,354.49 USD | `+0.17` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3458` | `0.3460` | `0.3414` | `0.3422` | `14,326,425` | 4,912,068.08 USD | -1,524,912.12 USD | `-31.04%` | 3,023,442.37 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3526` | `0.3549` | `0.3475` | `0.3495` | `45,168,744` | 15,880,052.12 USD | -558,956.14 USD | `-3.52%` | 4,684,564.92 USD | `-0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3495` | `0.3497` | `0.3444` | `0.3458` | `45,347,497` | 15,724,010.32 USD | -13,807.83 USD | `-0.09%` | 4,670,757.09 USD | `-0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3458` | `0.3460` | `0.3414` | `0.3422` | `14,326,425` | 4,912,068.08 USD | -1,524,912.12 USD | `-31.04%` | 3,145,844.96 USD | `-1.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3414` | `0.3422` | `59,679,569` | 20,638,010.65 USD | -1,537,138.75 USD | `-7.45%` | 3,319,547.99 USD | `-1.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 385,562.36 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 597,653.23 USD | `+0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3414` | `0.3422` | `59,679,569` | 20,638,010.65 USD | -1,537,138.75 USD | `-7.45%` | 3,319,547.99 USD | `-1.64` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.3425`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `924` | `0xecb6...2b00` | `LONG` | 2,450,921.30 USD | `7,171,679.00` | `0.3343` | `0.3419` | `0.000000` | 53,313.27 USD | `+2.18%` | `10X Cross` |
| `1577` | `0xeadc...9d55` | `LONG` | 1,367,000.00 USD | `4,000,000.00` | `0.3421` | `0.3419` | `0.000000` | -1,478.09 USD | `-0.11%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3293` | 6,377.20 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.38K USD at 0.3293 USD [API] | `2026-10-29 02:14:21` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+5.95%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--6.35%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+5.95%`) | Long MP=`0.3249` (Vol: 801,900.00 USD, Dist: `--6.35%`)
  * 3D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+5.55%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--6.36%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+5.55%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--6.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0705` | 216.44 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 7,540.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 179.83 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 908.23 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 113.82 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 391.44 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 9,790.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 208.12 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 6,430.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 493.50 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 36,200.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 3,370.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 20,240.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 12,250.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,020.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,170.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 431.37 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 208.67 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 87,060.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 189.39 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2155` | 1,430.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 227.46 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 286.67 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 1,700.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 726.42 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 6,120.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 2,790.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,260.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 3,010.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 139.92 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 464.79 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 109.49 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 377.64 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,530.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 312.44 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 438.42 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 2,100.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 108.15 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,210.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 449.23 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 193.75 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 27,310.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,150.00 USD | 978,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 9,770.00 USD | 974,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 80,970.00 USD | 965,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 13,010.00 USD | 884,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 871,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 419.35 USD | 864,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 15,200.00 USD | 864,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 1,420.00 USD | 849,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 307.60 USD | 847,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 911.60 USD | 847,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 5,780.00 USD | 846,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 589.42 USD | 840,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 840,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 25,780,000.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 126.07 USD | 839,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 839,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 839,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 25,710,000.00 USD | 25,710,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 25,650,000.00 USD | 25,650,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 147.75 USD | 838,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 25,560,000.00 USD | 25,560,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 25,420,000.00 USD | 25,420,000.00 USD | 122,540.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 157.14 USD | 838,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 25,200,000.00 USD | 25,200,000.00 USD | 137,530.00 USD | 37,780.00 USD | 57,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2975` | 2,330.00 USD | 838,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2977` | 24,970,000.00 USD | 24,970,000.00 USD | 69,090.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 24,860,000.00 USD | 24,860,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 127.46 USD | 836,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2989` | 24,640,000.00 USD | 24,640,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 24,480,000.00 USD | 24,480,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 3,510.00 USD | 836,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,290.00 USD | 832,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 24,470,000.00 USD | 24,470,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 328.03 USD | 822,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,620.00 USD | 821,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 405.59 USD | 819,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3049` | 24,440,000.00 USD | 24,440,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 24,390,000.00 USD | 24,390,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 818,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 24,390,000.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3067` | 16,510,000.00 USD | 16,510,000.00 USD | 32,000.00 USD | 0.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 24,310,000.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3072` | 16,440,000.00 USD | 16,440,000.00 USD | 95.13 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 24,310,000.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 6,650.00 USD | 804,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3077` | 16,440,000.00 USD | 16,440,000.00 USD | 23,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 24,300,000.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3082` | 16,420,000.00 USD | 16,420,000.00 USD | 18,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 24,200,000.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 797,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 16,400,000.00 USD | 16,400,000.00 USD | 673.47 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 24,200,000.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3092` | 16,380,000.00 USD | 16,380,000.00 USD | 14,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 797,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 16,370,000.00 USD | 16,370,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 24,190,000.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3102` | 16,370,000.00 USD | 16,370,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 24,170,000.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 24,030,000.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3112` | 16,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 24,030,000.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,740.00 USD | 797,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3117` | 16,240,000.00 USD | 16,240,000.00 USD | 12,410.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 23,990,000.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3122` | 16,200,000.00 USD | 16,200,000.00 USD | 13,610.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 5,330.00 USD | 783,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 16,150,000.00 USD | 16,150,000.00 USD | 10,770.00 USD | 39,470.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 23,810,000.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3132` | 16,090,000.00 USD | 16,090,000.00 USD | 37.20 USD | 26,460.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 23,690,000.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 14,630.00 USD | 778,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 16,050,000.00 USD | 16,050,000.00 USD | 638.92 USD | 10,610.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 23,680,000.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3142` | 16,020,000.00 USD | 16,020,000.00 USD | 453.70 USD | 3,580.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 23,680,000.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 141.84 USD | 763,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 16,010,000.00 USD | 16,010,000.00 USD | 839.70 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 23,360,000.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3152` | 16,010,000.00 USD | 16,010,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,490.00 USD | 763,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 15,980,000.00 USD | 15,980,000.00 USD | 24,650.00 USD | 3,680.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 23,110,000.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3162` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 5,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 22,560,000.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 761,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 15,930,000.00 USD | 15,930,000.00 USD | 43,210.00 USD | 35,060.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 21,710,000.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3172` | 15,840,000.00 USD | 15,840,000.00 USD | 17,180.00 USD | 38,410.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 20,910,000.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3177` | 15,740,000.00 USD | 15,740,000.00 USD | 53,160.00 USD | 8,980.00 USD | 32,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 20,590,000.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3182` | 15,650,000.00 USD | 15,650,000.00 USD | 419,060.00 USD | 72,550.00 USD | 116,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 15,040,000.00 USD | 15,040,000.00 USD | 76,610.00 USD | 48,980.00 USD | 52,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 19,600,000.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3192` | 14,860,000.00 USD | 14,860,000.00 USD | 45,500.00 USD | 3,120.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 19,130,000.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3197` | 14,790,000.00 USD | 14,790,000.00 USD | 84,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3202` | 14,710,000.00 USD | 14,710,000.00 USD | 207,310.00 USD | 14,420.00 USD | 34,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 18,830,000.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3207` | 14,450,000.00 USD | 14,450,000.00 USD | 132,700.00 USD | 24,620.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 18,730,000.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3212` | 14,230,000.00 USD | 14,230,000.00 USD | 1,300.00 USD | 20,180.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 14,120,000.00 USD | 14,120,000.00 USD | 5,550.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 17,860,000.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3222` | 14,030,000.00 USD | 14,030,000.00 USD | 118,640.00 USD | 17,600.00 USD | 86,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 17,410,000.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 13,800,000.00 USD | 13,800,000.00 USD | 21,530.00 USD | 37,430.00 USD | 188,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 16,490,000.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3232` | 13,560,000.00 USD | 13,560,000.00 USD | 56,470.00 USD | 14,830.00 USD | 121,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 15,100,000.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 589.09 USD | 760,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 13,360,000.00 USD | 13,360,000.00 USD | 6,420.00 USD | 66,660.00 USD | 139,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 13,520,000.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3242` | 13,150,000.00 USD | 13,150,000.00 USD | 97,850.00 USD | 28,130.00 USD | 188,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 12,840,000.00 USD | 12,840,000.00 USD | 436,670.00 USD | 124,590.00 USD | 199,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 12,730,000.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3252` | 12,080,000.00 USD | 12,080,000.00 USD | 849,380.00 USD | 121,930.00 USD | 268,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 11,400,000.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3257` | 10,840,000.00 USD | 10,840,000.00 USD | 101,780.00 USD | 36,240.00 USD | 309,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 10,060,000.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3262` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 9,680,000.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3267` | 10,380,000.00 USD | 10,380,000.00 USD | 933.66 USD | 60,860.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 9,490,000.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3272` | 10,180,000.00 USD | 10,180,000.00 USD | 162,490.00 USD | 43,110.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 6,260.00 USD | 760,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 9,750,000.00 USD | 9,750,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3282` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 9,290,000.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 754,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3287` | 9,280,000.00 USD | 9,280,000.00 USD | 45,960.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3292` | 9,120,000.00 USD | 9,120,000.00 USD | 38,710.00 USD | 0.00 USD | 119,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 8,900,000.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 839.90 USD | 8,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3297` | 8,960,000.00 USD | 8,960,000.00 USD | 977.29 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 8,870,000.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3302` | 8,960,000.00 USD | 8,960,000.00 USD | 37,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3307` | 8,920,000.00 USD | 8,920,000.00 USD | 121,770.00 USD | 13,130.00 USD | 98,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 8,800,000.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3312` | 8,690,000.00 USD | 8,690,000.00 USD | 235,230.00 USD | 100,700.00 USD | 251,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 8,460,000.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3315` | 4,780.00 USD | 7,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3317` | 8,100,000.00 USD | 8,100,000.00 USD | 159,340.00 USD | 97,570.00 USD | 373,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3322` | 7,470,000.00 USD | 7,470,000.00 USD | 106,340.00 USD | 22,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 8,150,000.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3325` | 1,560.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3327` | 7,340,000.00 USD | 7,340,000.00 USD | 62,020.00 USD | 79,240.00 USD | 289,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 7,890,000.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3332` | 6,910,000.00 USD | 6,910,000.00 USD | 27,990.00 USD | 21,620.00 USD | 99,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3335` | 496.25 USD | 1,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3337` | 6,760,000.00 USD | 6,760,000.00 USD | 158,800.00 USD | 200,290.00 USD | 533,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 7,230,000.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3342` | 5,870,000.00 USD | 5,870,000.00 USD | 76,100.00 USD | 110,060.00 USD | 23,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 115.40 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3347` | 5,660,000.00 USD | 5,660,000.00 USD | 168,490.00 USD | 43,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 6,610,000.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3352` | 5,450,000.00 USD | 5,450,000.00 USD | 109,310.00 USD | 12,500.00 USD | 97,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 6,380,000.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3357` | 5,230,000.00 USD | 5,230,000.00 USD | 268,830.00 USD | 28,250.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 6,110,000.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3362` | 4,790,000.00 USD | 4,790,000.00 USD | 3,370.00 USD | 62,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 4,720,000.00 USD | 4,720,000.00 USD | 329,140.00 USD | 9,190.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 6,110,000.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3372` | 4,350,000.00 USD | 4,350,000.00 USD | 859.70 USD | 60,180.00 USD | 37,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 5,860,000.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3377` | 4,260,000.00 USD | 4,260,000.00 USD | 619,770.00 USD | 103,090.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 5,270,000.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3382` | 3,520,000.00 USD | 3,520,000.00 USD | 209,960.00 USD | 114,980.00 USD | 66,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 4,610,000.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3385` | 984.02 USD | 984.02 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3387` | 3,120,000.00 USD | 3,120,000.00 USD | 55,650.00 USD | 44,920.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3391` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3392` | 2,990,000.00 USD | 2,990,000.00 USD | 65,650.00 USD | 108,700.00 USD | 161,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3397` | 2,660,000.00 USD | 2,660,000.00 USD | 144,030.00 USD | 157,840.00 USD | 245,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,970,000.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3402` | 2,110,000.00 USD | 2,110,000.00 USD | 53,400.00 USD | 48,800.00 USD | 325,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 3,280,000.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3407` | 1,680,000.00 USD | 1,680,000.00 USD | 206,060.00 USD | 185,590.00 USD | 61,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3412` | 1,230,000.00 USD | 1,230,000.00 USD | 161,360.00 USD | 243,090.00 USD | 110,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3415` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3417` | 713,080.00 USD | 713,080.00 USD | 605,570.00 USD | 79,640.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3422` | 334,450.00 USD | 334,450.00 USD | 0.00 USD | 46,340.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3427` | 480,940.00 USD | 480,940.00 USD | 0.00 USD | 146,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3432` | 662,420.00 USD | 662,420.00 USD | 0.00 USD | 181,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3437` | 730,820.00 USD | 730,820.00 USD | 0.00 USD | 68,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3439` | 733,270.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3442` | 757,190.00 USD | 757,190.00 USD | 0.00 USD | 26,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3447` | 817,290.00 USD | 817,290.00 USD | 0.00 USD | 60,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 538,440.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3452` | 857,170.00 USD | 857,170.00 USD | 0.00 USD | 39,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3457` | 1,230,000.00 USD | 1,230,000.00 USD | 1,150.00 USD | 0.00 USD | 370,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3482` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 47,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3497` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 454,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3502` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3507` | 1,840,000.00 USD | 1,840,000.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3512` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 1,880,000.00 USD | 1,880,000.00 USD | 21,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3527` | 1,930,000.00 USD | 1,930,000.00 USD | 25,310.00 USD | 24,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3532` | 2,150,000.00 USD | 2,150,000.00 USD | 62,050.00 USD | 61,120.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3537` | 2,420,000.00 USD | 2,420,000.00 USD | 57,790.00 USD | 23,240.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3542` | 2,600,000.00 USD | 2,600,000.00 USD | 75,280.00 USD | 62,870.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3547` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 54,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3552` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 44,640.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3557` | 2,800,000.00 USD | 2,800,000.00 USD | 20,180.00 USD | 34,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3562` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 25,000.00 USD | 115,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3567` | 2,950,000.00 USD | 2,950,000.00 USD | 1,450.00 USD | 11,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3572` | 2,960,000.00 USD | 2,960,000.00 USD | 1,770.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 3,140,000.00 USD | 3,140,000.00 USD | 159,700.00 USD | 18,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3582` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 14,930.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3587` | 3,210,000.00 USD | 3,210,000.00 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3592` | 3,300,000.00 USD | 3,300,000.00 USD | 46,870.00 USD | 15,750.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3597` | 3,520,000.00 USD | 3,520,000.00 USD | 107,230.00 USD | 12,460.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3602` | 3,800,000.00 USD | 3,800,000.00 USD | 31,030.00 USD | 42,800.00 USD | 201,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3607` | 4,010,000.00 USD | 4,010,000.00 USD | 28,890.00 USD | 31,810.00 USD | 157,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3612` | 4,400,000.00 USD | 4,400,000.00 USD | 86,030.00 USD | 60,420.00 USD | 236,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3617` | 4,800,000.00 USD | 4,800,000.00 USD | 225,350.00 USD | 70,370.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3622` | 5,120,000.00 USD | 5,120,000.00 USD | 169,910.00 USD | 75,820.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3625` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3627` | 5,560,000.00 USD | 5,560,000.00 USD | 393,900.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3632` | 6,810,000.00 USD | 6,810,000.00 USD | 941,740.00 USD | 102,260.00 USD | 207,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,520.00 USD | 33,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 7,140,000.00 USD | 7,140,000.00 USD | 183,690.00 USD | 70,930.00 USD | 71,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3642` | 7,560,000.00 USD | 7,560,000.00 USD | 103,140.00 USD | 206,820.00 USD | 111,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 45,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3647` | 8,030,000.00 USD | 8,030,000.00 USD | 324,310.00 USD | 32,390.00 USD | 110,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3652` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 63,450.00 USD | 191,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3657` | 9,110,000.00 USD | 9,110,000.00 USD | 463,120.00 USD | 145,960.00 USD | 215,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3662` | 9,430,000.00 USD | 9,430,000.00 USD | 273,550.00 USD | 35,050.00 USD | 16,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,160.00 USD | 46,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 10,140,000.00 USD | 10,140,000.00 USD | 466,660.00 USD | 118,850.00 USD | 123,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3672` | 10,640,000.00 USD | 10,640,000.00 USD | 83,650.00 USD | 82,030.00 USD | 333,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,960.00 USD | 48,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3677` | 11,400,000.00 USD | 11,400,000.00 USD | 513,320.00 USD | 60,780.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3682` | 11,930,000.00 USD | 11,930,000.00 USD | 293,500.00 USD | 87,330.00 USD | 148,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 220.73 USD | 48,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3687` | 12,600,000.00 USD | 12,600,000.00 USD | 439,120.00 USD | 147,370.00 USD | 81,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3692` | 13,020,000.00 USD | 13,020,000.00 USD | 348,280.00 USD | 49,680.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 13,270,000.00 USD | 13,270,000.00 USD | 161,360.00 USD | 81,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3702` | 14,070,000.00 USD | 14,070,000.00 USD | 576,250.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 49,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3707` | 14,820,000.00 USD | 14,820,000.00 USD | 175,430.00 USD | 21,340.00 USD | 554,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3712` | 15,680,000.00 USD | 15,680,000.00 USD | 547,890.00 USD | 90,010.00 USD | 225,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3717` | 16,790,000.00 USD | 16,790,000.00 USD | 86,560.00 USD | 220,760.00 USD | 799,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3722` | 17,130,000.00 USD | 17,130,000.00 USD | 185,610.00 USD | 64,150.00 USD | 96,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 366.17 USD | 49,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3727` | 18,320,000.00 USD | 18,320,000.00 USD | 320,090.00 USD | 32,200.00 USD | 836,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3732` | 19,140,000.00 USD | 19,140,000.00 USD | 33,590.00 USD | 130,550.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 44,750.00 USD | 94,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3737` | 19,470,000.00 USD | 19,470,000.00 USD | 231,660.00 USD | 94,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3742` | 20,050,000.00 USD | 20,050,000.00 USD | 32,620.00 USD | 90,740.00 USD | 459,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3747` | 20,850,000.00 USD | 20,850,000.00 USD | 30,710.00 USD | 24,770.00 USD | 739,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3752` | 21,260,000.00 USD | 21,260,000.00 USD | 363,100.00 USD | 0.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 6,120.00 USD | 100,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 21,530,000.00 USD | 21,530,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3762` | 22,780,000.00 USD | 22,780,000.00 USD | 303,200.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3767` | 22,830,000.00 USD | 22,830,000.00 USD | 21,660.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3772` | 22,920,000.00 USD | 22,920,000.00 USD | 0.00 USD | 75,650.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 32,300.00 USD | 132,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3777` | 23,150,000.00 USD | 23,150,000.00 USD | 1,210.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3782` | 23,170,000.00 USD | 23,170,000.00 USD | 16,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,700.00 USD | 689,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 23,680,000.00 USD | 23,680,000.00 USD | 220,670.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3792` | 23,880,000.00 USD | 23,880,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3797` | 23,880,000.00 USD | 23,880,000.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3802` | 24,010,000.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 134,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3807` | 24,240,000.00 USD | 24,240,000.00 USD | 855.55 USD | 9,110.00 USD | 217,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3812` | 24,290,000.00 USD | 24,290,000.00 USD | 23,970.00 USD | 10,650.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3815` | 9,250.00 USD | 698,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3817` | 24,320,000.00 USD | 24,320,000.00 USD | 10,680.00 USD | 0.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3822` | 24,590,000.00 USD | 24,590,000.00 USD | 2,080.00 USD | 39,470.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3827` | 24,610,000.00 USD | 24,610,000.00 USD | 1,720.00 USD | 2,520.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3832` | 24,870,000.00 USD | 24,870,000.00 USD | 0.00 USD | 34,540.00 USD | 219,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 34,170.00 USD | 732,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3842` | 24,880,000.00 USD | 24,880,000.00 USD | 1,750.00 USD | 5,900.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3852` | 24,910,000.00 USD | 24,910,000.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3857` | 24,950,000.00 USD | 24,950,000.00 USD | 24,650.00 USD | 3,680.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3862` | 24,950,000.00 USD | 24,950,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3867` | 25,030,000.00 USD | 25,030,000.00 USD | 43,210.00 USD | 31,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3872` | 25,040,000.00 USD | 25,040,000.00 USD | 0.00 USD | 3,150.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3877` | 25,100,000.00 USD | 25,100,000.00 USD | 14,770.00 USD | 28,230.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3882` | 25,130,000.00 USD | 25,130,000.00 USD | 7,780.00 USD | 0.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3885` | 5,490.00 USD | 738,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3887` | 25,140,000.00 USD | 25,140,000.00 USD | 0.00 USD | 11,790.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3892` | 25,180,000.00 USD | 25,180,000.00 USD | 9,680.00 USD | 3,350.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 3,800.00 USD | 742,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3897` | 25,230,000.00 USD | 25,230,000.00 USD | 0.00 USD | 30,250.00 USD | 21,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3902` | 25,290,000.00 USD | 25,290,000.00 USD | 45,500.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 2,140.00 USD | 744,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 25,380,000.00 USD | 25,380,000.00 USD | 83,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3912` | 25,440,000.00 USD | 25,440,000.00 USD | 64,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3917` | 25,710,000.00 USD | 25,710,000.00 USD | 216,680.00 USD | 17,950.00 USD | 33,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3919` | 14,140,000.00 USD | 14,140,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 14,300,000.00 USD | 14,300,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 14,330,000.00 USD | 14,330,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 745,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 14,360,000.00 USD | 14,360,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 14,390,000.00 USD | 14,390,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 234,290.00 USD | 980,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 14,520,000.00 USD | 14,520,000.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 14,750,000.00 USD | 14,750,000.00 USD | 107,420.00 USD | 10,160.00 USD | 112,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 14,960,000.00 USD | 14,960,000.00 USD | 143,850.00 USD | 54,030.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 1,580.00 USD | 981,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3967` | 14,980,000.00 USD | 14,980,000.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 15,120,000.00 USD | 15,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 15,230,000.00 USD | 15,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 15,270,000.00 USD | 15,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 15,290,000.00 USD | 15,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4015` | 290.69 USD | 981,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,210.00 USD | 984,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 984,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4155` | 131.71 USD | 984,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 598.09 USD | 985,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 1,000.00 USD | 986,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 11,900.00 USD | 998,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4285` | 10,390.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4315` | 1,490.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4375` | 71,210.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 378.34 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 22,270.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 1,020.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 5,550.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 1,140.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,550.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 282,390.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4735` | 8,060.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 25,700.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4955` | 286.40 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4975` | 1,050.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 23,600.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5525` | 4,420.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5545` | 41,030.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5595` | 10,580.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5675` | 54,390.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5685` | 737,490.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5695` | 608,040.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5995` | 8,100.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 28,550.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6205` | 375.40 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6225` | 32,720.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 1,140.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 48,630.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 705.13 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6625` | 2,060.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 2,530.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 1,210.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6655` | 86,020.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6735` | 88,180.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6765` | 83,430.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6875` | 262.62 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6895` | 848.09 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0705` | 1,290,000.00 USD | 0.00 USD | 216.44 USD | `-79.62%` | `3,070.00` |
| `Live` | `Long` | `0.0735` | 1,290,000.00 USD | 0.00 USD | 3,000.00 USD | `-78.75%` | `40,871.00` |
| `Live` | `Long` | `0.0855` | 1,280,000.00 USD | 0.00 USD | 7,540.00 USD | `-75.29%` | `88,233.00` |
| `Live` | `Long` | `0.0865` | 1,270,000.00 USD | 0.00 USD | 179.83 USD | `-75.00%` | `2,079.00` |
| `Live` | `Long` | `0.0915` | 1,270,000.00 USD | 0.00 USD | 908.23 USD | `-73.55%` | `9,926.00` |
| `Live` | `Long` | `0.1085` | 1,270,000.00 USD | 0.00 USD | 113.82 USD | `-68.64%` | `1,049.00` |
| `Live` | `Long` | `0.1165` | 1,270,000.00 USD | 0.00 USD | 391.44 USD | `-66.32%` | `3,360.00` |
| `Live` | `Long` | `0.1275` | 1,270,000.00 USD | 0.00 USD | 9,790.00 USD | `-63.14%` | `76,797.00` |
| `Live` | `Long` | `0.1475` | 1,260,000.00 USD | 0.00 USD | 208.12 USD | `-57.36%` | `1,411.00` |
| `Live` | `Long` | `0.1565` | 1,260,000.00 USD | 0.00 USD | 6,430.00 USD | `-54.76%` | `41,100.00` |
| `Live` | `Long` | `0.1595` | 1,260,000.00 USD | 0.00 USD | 390.46 USD | `-53.90%` | `2,448.00` |
| `Live` | `Long` | `0.1645` | 1,260,000.00 USD | 0.00 USD | 493.50 USD | `-52.45%` | `3,000.00` |
| `Live` | `Long` | `0.1655` | 1,260,000.00 USD | 0.00 USD | 36,200.00 USD | `-52.16%` | `218,745.00` |
| `Live` | `Long` | `0.1685` | 1,220,000.00 USD | 0.00 USD | 3,370.00 USD | `-51.29%` | `20,000.00` |
| `Live` | `Long` | `0.1695` | 1,220,000.00 USD | 0.00 USD | 20,240.00 USD | `-51.00%` | `119,400.00` |
| `Live` | `Long` | `0.1725` | 1,200,000.00 USD | 0.00 USD | 12,250.00 USD | `-50.14%` | `71,028.00` |
| `Live` | `Long` | `0.1735` | 1,180,000.00 USD | 0.00 USD | 339.71 USD | `-49.85%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,180,000.00 USD | 0.00 USD | 1,020.00 USD | `-49.56%` | `5,865.00` |
| `Live` | `Long` | `0.1755` | 1,180,000.00 USD | 0.00 USD | 4,170.00 USD | `-49.27%` | `23,777.00` |
| `Live` | `Long` | `0.1765` | 1,180,000.00 USD | 0.00 USD | 431.37 USD | `-48.98%` | `2,444.00` |
| `Live` | `Long` | `0.1785` | 1,180,000.00 USD | 0.00 USD | 208.67 USD | `-48.40%` | `1,169.00` |
| `Live` | `Long` | `0.1875` | 1,180,000.00 USD | 0.00 USD | 36,310.00 USD | `-45.80%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,140,000.00 USD | 0.00 USD | 632.00 USD | `-42.91%` | `3,200.00` |
| `Live` | `Long` | `0.2015` | 1,140,000.00 USD | 0.00 USD | 87,060.00 USD | `-41.75%` | `432,044.00` |
| `Live` | `Long` | `0.2095` | 1,050,000.00 USD | 0.00 USD | 189.39 USD | `-39.44%` | `904.00` |
| `Live` | `Long` | `0.2155` | 1,050,000.00 USD | 0.00 USD | 1,430.00 USD | `-37.71%` | `6,651.00` |
| `Live` | `Long` | `0.2175` | 1,050,000.00 USD | 0.00 USD | 1,520.00 USD | `-37.13%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,050,000.00 USD | 0.00 USD | 227.46 USD | `-36.84%` | `1,041.00` |
| `Live` | `Long` | `0.2195` | 1,050,000.00 USD | 0.00 USD | 286.67 USD | `-36.55%` | `1,306.00` |
| `Live` | `Long` | `0.2245` | 1,050,000.00 USD | 0.00 USD | 4,570.00 USD | `-35.11%` | `20,360.00` |
| `Live` | `Long` | `0.2295` | 1,050,000.00 USD | 0.00 USD | 2,070.00 USD | `-33.66%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,040,000.00 USD | 0.00 USD | 410.06 USD | `-33.37%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,040,000.00 USD | 0.00 USD | 1,700.00 USD | `-32.79%` | `7,301.00` |
| `Live` | `Long` | `0.2335` | 1,040,000.00 USD | 0.00 USD | 726.42 USD | `-32.50%` | `3,111.00` |
| `Live` | `Long` | `0.2345` | 1,040,000.00 USD | 0.00 USD | 6,120.00 USD | `-32.22%` | `26,082.00` |
| `Live` | `Long` | `0.2355` | 1,030,000.00 USD | 0.00 USD | 2,790.00 USD | `-31.93%` | `11,856.00` |
| `Live` | `Long` | `0.2365` | 1,030,000.00 USD | 0.00 USD | 344.11 USD | `-31.64%` | `1,455.00` |
| `Live` | `Long` | `0.2375` | 1,030,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.35%` | `5,298.00` |
| `Live` | `Long` | `0.2395` | 1,030,000.00 USD | 0.00 USD | 3,010.00 USD | `-30.77%` | `12,559.00` |
| `Live` | `Long` | `0.2425` | 1,030,000.00 USD | 0.00 USD | 139.92 USD | `-29.90%` | `577.00` |
| `Live` | `Long` | `0.2435` | 1,030,000.00 USD | 0.00 USD | 885.85 USD | `-29.61%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 1,030,000.00 USD | 0.00 USD | 464.79 USD | `-29.33%` | `1,901.00` |
| `Live` | `Long` | `0.2455` | 1,030,000.00 USD | 0.00 USD | 109.49 USD | `-29.04%` | `446.00` |
| `Live` | `Long` | `0.2465` | 1,030,000.00 USD | 0.00 USD | 377.64 USD | `-28.75%` | `1,532.00` |
| `Live` | `Long` | `0.2485` | 1,020,000.00 USD | 0.00 USD | 11,890.00 USD | `-28.17%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 1,010,000.00 USD | 0.00 USD | 262.02 USD | `-27.59%` | `1,046.00` |
| `Live` | `Long` | `0.2565` | 1,010,000.00 USD | 0.00 USD | 1,530.00 USD | `-25.86%` | `5,966.00` |
| `Live` | `Long` | `0.2595` | 1,010,000.00 USD | 0.00 USD | 312.44 USD | `-24.99%` | `1,204.00` |
| `Live` | `Long` | `0.2605` | 1,010,000.00 USD | 0.00 USD | 438.42 USD | `-24.70%` | `1,683.00` |
| `Live` | `Long` | `0.2615` | 1,010,000.00 USD | 0.00 USD | 2,100.00 USD | `-24.41%` | `8,015.00` |
| `Live` | `Long` | `0.2625` | 1,010,000.00 USD | 0.00 USD | 108.15 USD | `-24.12%` | `412.00` |
| `Live` | `Long` | `0.2645` | 1,010,000.00 USD | 0.00 USD | 2,210.00 USD | `-23.54%` | `8,340.00` |
| `Live` | `Long` | `0.2655` | 1,010,000.00 USD | 0.00 USD | 449.23 USD | `-23.25%` | `1,692.00` |
| `Live` | `Long` | `0.2665` | 1,010,000.00 USD | 0.00 USD | 193.75 USD | `-22.97%` | `727.00` |
| `Live` | `Long` | `0.2675` | 1,010,000.00 USD | 0.00 USD | 27,310.00 USD | `-22.68%` | `102,082.00` |
| `Live` | `Long` | `0.2685` | 978,090.00 USD | 0.00 USD | 3,150.00 USD | `-22.39%` | `11,746.00` |
| `Live` | `Long` | `0.2745` | 974,930.00 USD | 0.00 USD | 9,770.00 USD | `-20.65%` | `35,594.00` |
| `Live` | `Long` | `0.2755` | 965,160.00 USD | 0.00 USD | 80,970.00 USD | `-20.36%` | `293,891.00` |
| `Live` | `Long` | `0.2785` | 884,190.00 USD | 0.00 USD | 13,010.00 USD | `-19.50%` | `46,725.00` |
| `Live` | `Long` | `0.2795` | 871,180.00 USD | 0.00 USD | 6,260.00 USD | `-19.21%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 864,930.00 USD | 0.00 USD | 419.35 USD | `-18.92%` | `1,495.00` |
| `Live` | `Long` | `0.2815` | 864,510.00 USD | 0.00 USD | 15,200.00 USD | `-18.63%` | `53,984.00` |
| `Live` | `Long` | `0.2825` | 849,310.00 USD | 0.00 USD | 1,420.00 USD | `-18.34%` | `5,038.00` |
| `Live` | `Long` | `0.2835` | 847,890.00 USD | 0.00 USD | 307.60 USD | `-18.05%` | `1,085.00` |
| `Live` | `Long` | `0.2855` | 847,580.00 USD | 0.00 USD | 911.60 USD | `-17.47%` | `3,193.00` |
| `Live` | `Long` | `0.2875` | 846,670.00 USD | 0.00 USD | 5,780.00 USD | `-16.90%` | `20,120.00` |
| `Live` | `Long` | `0.2905` | 840,880.00 USD | 0.00 USD | 589.42 USD | `-16.03%` | `2,029.00` |
| `Live` | `Long` | `0.2915` | 840,290.00 USD | 0.00 USD | 954.37 USD | `-15.74%` | `3,274.00` |
| `Live` | `Long` | `0.2925` | 839,340.00 USD | 0.00 USD | 126.07 USD | `-15.45%` | `431.00` |
| `Live` | `Long` | `0.2935` | 839,210.00 USD | 0.00 USD | 213.08 USD | `-15.16%` | `726.00` |
| `Live` | `Long` | `0.2945` | 839,000.00 USD | 0.00 USD | 124.87 USD | `-14.87%` | `424.00` |
| `Live` | `Long` | `0.2955` | 838,880.00 USD | 0.00 USD | 147.75 USD | `-14.58%` | `500.00` |
| `Live` | `Long` | `0.2965` | 838,730.00 USD | 0.00 USD | 157.14 USD | `-14.29%` | `530.00` |
| `Live` | `Long` | `0.2975` | 838,570.00 USD | 0.00 USD | 2,330.00 USD | `-14.00%` | `7,844.00` |
| `Live` | `Long` | `0.2985` | 836,240.00 USD | 0.00 USD | 127.46 USD | `-13.72%` | `427.00` |
| `Live` | `Long` | `0.2995` | 836,110.00 USD | 0.00 USD | 3,510.00 USD | `-13.43%` | `11,720.00` |
| `Live` | `Long` | `0.3005` | 832,600.00 USD | 0.00 USD | 10,290.00 USD | `-13.14%` | `34,248.00` |
| `Live` | `Long` | `0.3015` | 822,310.00 USD | 0.00 USD | 328.03 USD | `-12.85%` | `1,088.00` |
| `Live` | `Long` | `0.3025` | 821,980.00 USD | 0.00 USD | 2,620.00 USD | `-12.56%` | `8,655.00` |
| `Live` | `Long` | `0.3045` | 819,360.00 USD | 0.00 USD | 405.59 USD | `-11.98%` | `1,332.00` |
| `Live` | `Long` | `0.3055` | 818,960.00 USD | 0.00 USD | 14,670.00 USD | `-11.69%` | `48,026.00` |
| `Live` | `Long` | `0.3075` | 804,280.00 USD | 0.00 USD | 6,650.00 USD | `-11.11%` | `21,612.00` |
| `Live` | `Long` | `0.3085` | 797,640.00 USD | 0.00 USD | 291.53 USD | `-10.83%` | `945.00` |
| `Live` | `Long` | `0.3095` | 797,350.00 USD | 0.00 USD | 192.51 USD | `-10.54%` | `622.00` |
| `Live` | `Long` | `0.3115` | 797,150.00 USD | 0.00 USD | 13,740.00 USD | `-9.96%` | `44,115.00` |
| `Live` | `Long` | `0.3125` | 783,410.00 USD | 0.00 USD | 5,330.00 USD | `-9.67%` | `17,060.00` |
| `Live` | `Long` | `0.3135` | 778,080.00 USD | 0.00 USD | 14,630.00 USD | `-9.38%` | `46,661.00` |
| `Live` | `Long` | `0.3145` | 763,450.00 USD | 0.00 USD | 141.84 USD | `-9.09%` | `451.00` |
| `Live` | `Long` | `0.3155` | 763,310.00 USD | 0.00 USD | 1,490.00 USD | `-8.80%` | `4,723.00` |
| `Live` | `Long` | `0.3165` | 761,820.00 USD | 0.00 USD | 935.89 USD | `-8.51%` | `2,957.00` |
| `Live` | `Long` | `0.3235` | 760,880.00 USD | 0.00 USD | 589.09 USD | `-6.49%` | `1,821.00` |
| `Live` | `Long` | `0.3275` | 760,300.00 USD | 0.00 USD | 6,260.00 USD | `-5.33%` | `19,105.00` |
| `Live` | `Long` | `0.3285` | 754,040.00 USD | 0.00 USD | 745,260.00 USD | `-5.04%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 8,780.00 USD | 0.00 USD | 839.90 USD | `-4.76%` | `2,549.00` |
| `Live` | `Long` | `0.3315` | 7,940.00 USD | 0.00 USD | 4,780.00 USD | `-4.18%` | `14,420.00` |
| `Live` | `Long` | `0.3325` | 3,160.00 USD | 0.00 USD | 1,560.00 USD | `-3.89%` | `4,691.00` |
| `Live` | `Long` | `0.3335` | 1,600.00 USD | 0.00 USD | 496.25 USD | `-3.60%` | `1,488.00` |
| `Live` | `Long` | `0.3345` | 1,100.00 USD | 0.00 USD | 115.40 USD | `-3.31%` | `345.00` |
| `Live` | `Long` | `0.3385` | 984.02 USD | 0.00 USD | 984.02 USD | `-2.15%` | `2,907.00` |
| `Live` | `Short` | `0.3625` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | `+4.78%` | `4,554.00` |
| `Live` | `Short` | `0.3635` | 33,170.00 USD | 31,520.00 USD | 0.00 USD | `+5.07%` | `86,708.00` |
| `Live` | `Short` | `0.3645` | 45,560.00 USD | 12,390.00 USD | 0.00 USD | `+5.36%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 46,720.00 USD | 1,160.00 USD | 0.00 USD | `+5.94%` | `3,165.00` |
| `Live` | `Short` | `0.3675` | 48,680.00 USD | 1,960.00 USD | 0.00 USD | `+6.23%` | `5,333.00` |
| `Live` | `Short` | `0.3685` | 48,900.00 USD | 220.73 USD | 0.00 USD | `+6.52%` | `599.00` |
| `Live` | `Short` | `0.3705` | 49,180.00 USD | 278.99 USD | 0.00 USD | `+7.10%` | `753.00` |
| `Live` | `Short` | `0.3725` | 49,550.00 USD | 366.17 USD | 0.00 USD | `+7.67%` | `983.00` |
| `Live` | `Short` | `0.3735` | 94,300.00 USD | 44,750.00 USD | 0.00 USD | `+7.96%` | `119,811.00` |
| `Live` | `Short` | `0.3755` | 100,410.00 USD | 6,120.00 USD | 0.00 USD | `+8.54%` | `16,287.00` |
| `Live` | `Short` | `0.3775` | 132,720.00 USD | 32,300.00 USD | 0.00 USD | `+9.12%` | `85,568.00` |
| `Live` | `Short` | `0.3785` | 689,410.00 USD | 556,700.00 USD | 0.00 USD | `+9.41%` | `1,470,802.00` |
| `Live` | `Short` | `0.3815` | 698,670.00 USD | 9,250.00 USD | 0.00 USD | `+10.28%` | `24,250.00` |
| `Live` | `Short` | `0.3835` | 732,840.00 USD | 34,170.00 USD | 0.00 USD | `+10.85%` | `89,108.00` |
| `Live` | `Short` | `0.3885` | 738,330.00 USD | 5,490.00 USD | 0.00 USD | `+12.30%` | `14,129.00` |
| `Live` | `Short` | `0.3895` | 742,130.00 USD | 3,800.00 USD | 0.00 USD | `+12.59%` | `9,767.00` |
| `Live` | `Short` | `0.3905` | 744,270.00 USD | 2,140.00 USD | 0.00 USD | `+12.88%` | `5,479.00` |
| `Live` | `Short` | `0.3935` | 745,760.00 USD | 1,480.00 USD | 0.00 USD | `+13.74%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 980,050.00 USD | 234,290.00 USD | 0.00 USD | `+14.03%` | `593,903.00` |
| `Live` | `Short` | `0.3965` | 981,630.00 USD | 1,580.00 USD | 0.00 USD | `+14.61%` | `3,992.00` |
| `Live` | `Short` | `0.4015` | 981,920.00 USD | 290.69 USD | 0.00 USD | `+16.06%` | `724.00` |
| `Live` | `Short` | `0.4085` | 984,140.00 USD | 2,210.00 USD | 0.00 USD | `+18.08%` | `5,417.00` |
| `Live` | `Short` | `0.4095` | 984,380.00 USD | 239.56 USD | 0.00 USD | `+18.37%` | `585.00` |
| `Live` | `Short` | `0.4155` | 984,510.00 USD | 131.71 USD | 0.00 USD | `+20.10%` | `317.00` |
| `Live` | `Short` | `0.4165` | 985,110.00 USD | 598.09 USD | 0.00 USD | `+20.39%` | `1,436.00` |
| `Live` | `Short` | `0.4195` | 986,110.00 USD | 1,000.00 USD | 0.00 USD | `+21.26%` | `2,387.00` |
| `Live` | `Short` | `0.4235` | 998,000.00 USD | 11,900.00 USD | 0.00 USD | `+22.42%` | `28,092.00` |
| `Live` | `Short` | `0.4285` | 1,010,000.00 USD | 10,390.00 USD | 0.00 USD | `+23.86%` | `24,251.00` |
| `Live` | `Short` | `0.4315` | 1,010,000.00 USD | 1,490.00 USD | 0.00 USD | `+24.73%` | `3,464.00` |
| `Live` | `Short` | `0.4375` | 1,080,000.00 USD | 71,210.00 USD | 0.00 USD | `+26.46%` | `162,775.00` |
| `Live` | `Short` | `0.4425` | 1,080,000.00 USD | 378.34 USD | 0.00 USD | `+27.91%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,100,000.00 USD | 22,270.00 USD | 0.00 USD | `+28.78%` | `50,000.00` |
| `Live` | `Short` | `0.4465` | 1,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+29.06%` | `2,284.00` |
| `Live` | `Short` | `0.4475` | 1,170,000.00 USD | 65,610.00 USD | 0.00 USD | `+29.35%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 1,180,000.00 USD | 5,550.00 USD | 0.00 USD | `+30.51%` | `12,301.00` |
| `Live` | `Short` | `0.4525` | 1,180,000.00 USD | 1,140.00 USD | 0.00 USD | `+30.80%` | `2,519.00` |
| `Live` | `Short` | `0.4545` | 1,180,000.00 USD | 1,550.00 USD | 0.00 USD | `+31.38%` | `3,416.00` |
| `Live` | `Short` | `0.4705` | 1,460,000.00 USD | 282,390.00 USD | 0.00 USD | `+36.00%` | `600,198.00` |
| `Live` | `Short` | `0.4735` | 1,470,000.00 USD | 8,060.00 USD | 0.00 USD | `+36.87%` | `17,027.00` |
| `Live` | `Short` | `0.4895` | 1,470,000.00 USD | 839.49 USD | 0.00 USD | `+41.49%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 1,500,000.00 USD | 25,700.00 USD | 0.00 USD | `+41.78%` | `52,399.00` |
| `Live` | `Short` | `0.4955` | 1,500,000.00 USD | 286.40 USD | 0.00 USD | `+43.23%` | `578.00` |
| `Live` | `Short` | `0.4975` | 1,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+43.81%` | `2,120.00` |
| `Live` | `Short` | `0.4995` | 1,500,000.00 USD | 2,730.00 USD | 0.00 USD | `+44.39%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 1,520,000.00 USD | 23,600.00 USD | 0.00 USD | `+44.96%` | `47,061.00` |
| `Live` | `Short` | `0.5335` | 1,520,000.00 USD | 668.48 USD | 0.00 USD | `+54.21%` | `1,253.00` |
| `Live` | `Short` | `0.5525` | 1,530,000.00 USD | 4,420.00 USD | 0.00 USD | `+59.71%` | `8,009.00` |
| `Live` | `Short` | `0.5545` | 1,570,000.00 USD | 41,030.00 USD | 0.00 USD | `+60.28%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 1,570,000.00 USD | 740.92 USD | 0.00 USD | `+61.15%` | `1,329.00` |
| `Live` | `Short` | `0.5595` | 1,580,000.00 USD | 10,580.00 USD | 0.00 USD | `+61.73%` | `18,917.00` |
| `Live` | `Short` | `0.5615` | 1,580,000.00 USD | 140.38 USD | 0.00 USD | `+62.31%` | `250.00` |
| `Live` | `Short` | `0.5675` | 1,640,000.00 USD | 54,390.00 USD | 0.00 USD | `+64.04%` | `95,846.00` |
| `Live` | `Short` | `0.5685` | 2,370,000.00 USD | 737,490.00 USD | 0.00 USD | `+64.33%` | `1,297,248.00` |
| `Live` | `Short` | `0.5695` | 2,980,000.00 USD | 608,040.00 USD | 0.00 USD | `+64.62%` | `1,067,681.00` |
| `Live` | `Short` | `0.5995` | 2,990,000.00 USD | 8,100.00 USD | 0.00 USD | `+73.29%` | `13,510.00` |
| `Live` | `Short` | `0.6155` | 3,020,000.00 USD | 28,550.00 USD | 0.00 USD | `+77.92%` | `46,380.00` |
| `Live` | `Short` | `0.6205` | 3,020,000.00 USD | 375.40 USD | 0.00 USD | `+79.36%` | `605.00` |
| `Live` | `Short` | `0.6225` | 3,050,000.00 USD | 32,720.00 USD | 0.00 USD | `+79.94%` | `52,566.00` |
| `Live` | `Short` | `0.6285` | 3,050,000.00 USD | 1,140.00 USD | 0.00 USD | `+81.67%` | `1,808.00` |
| `Live` | `Short` | `0.6345` | 3,100,000.00 USD | 48,630.00 USD | 0.00 USD | `+83.41%` | `76,641.00` |
| `Live` | `Short` | `0.6515` | 3,100,000.00 USD | 951.19 USD | 0.00 USD | `+88.32%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 3,100,000.00 USD | 705.13 USD | 0.00 USD | `+88.90%` | `1,079.00` |
| `Live` | `Short` | `0.6625` | 3,100,000.00 USD | 2,060.00 USD | 0.00 USD | `+91.50%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,110,000.00 USD | 2,530.00 USD | 0.00 USD | `+91.79%` | `3,811.00` |
| `Live` | `Short` | `0.6645` | 3,110,000.00 USD | 1,210.00 USD | 0.00 USD | `+92.08%` | `1,821.00` |
| `Live` | `Short` | `0.6655` | 3,190,000.00 USD | 86,020.00 USD | 0.00 USD | `+92.37%` | `129,256.00` |
| `Live` | `Short` | `0.6735` | 3,280,000.00 USD | 88,180.00 USD | 0.00 USD | `+94.68%` | `130,928.00` |
| `Live` | `Short` | `0.6765` | 3,370,000.00 USD | 83,430.00 USD | 0.00 USD | `+95.55%` | `123,332.00` |
| `Live` | `Short` | `0.6875` | 3,370,000.00 USD | 262.62 USD | 0.00 USD | `+98.73%` | `382.00` |
| `Live` | `Short` | `0.6895` | 3,370,000.00 USD | 848.09 USD | 0.00 USD | `+99.31%` | `1,230.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 954,660.00 USD | 0.00 USD | 198.45 USD | `-72.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 954,460.00 USD | 0.00 USD | 330.26 USD | `-59.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 954,130.00 USD | 0.00 USD | 6,100.00 USD | `-47.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 948,030.00 USD | 0.00 USD | 1,750.00 USD | `-41.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 946,270.00 USD | 0.00 USD | 2,220.00 USD | `-39.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 944,060.00 USD | 0.00 USD | 121.70 USD | `-33.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 943,940.00 USD | 0.00 USD | 705.61 USD | `-32.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 943,230.00 USD | 0.00 USD | 159.20 USD | `-31.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 943,070.00 USD | 0.00 USD | 1,200.00 USD | `-30.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 941,870.00 USD | 0.00 USD | 127.51 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 941,740.00 USD | 0.00 USD | 1,850.00 USD | `-27.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 939,890.00 USD | 0.00 USD | 41,500.00 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 898,390.00 USD | 0.00 USD | 1,920.00 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 896,470.00 USD | 0.00 USD | 664.01 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 895,800.00 USD | 0.00 USD | 954.98 USD | `-24.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 894,850.00 USD | 0.00 USD | 103.56 USD | `-23.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 894,750.00 USD | 0.00 USD | 695.50 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 894,050.00 USD | 0.00 USD | 1,630.00 USD | `-22.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 892,420.00 USD | 0.00 USD | 1,470.00 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 890,950.00 USD | 0.00 USD | 101.94 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 890,850.00 USD | 0.00 USD | 3,260.00 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 887,590.00 USD | 0.00 USD | 2,550.00 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 885,040.00 USD | 0.00 USD | 229.92 USD | `-18.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 884,810.00 USD | 0.00 USD | 8,010.00 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 876,800.00 USD | 0.00 USD | 11,610.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 865,190.00 USD | 0.00 USD | 111.19 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 865,080.00 USD | 0.00 USD | 326.86 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 864,750.00 USD | 0.00 USD | 2,710.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 862,040.00 USD | 0.00 USD | 335.56 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 861,710.00 USD | 0.00 USD | 919.50 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 860,790.00 USD | 0.00 USD | 193.11 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 860,600.00 USD | 0.00 USD | 15,150.00 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 845,440.00 USD | 0.00 USD | 147.32 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 845,300.00 USD | 0.00 USD | 12,200.00 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 833,090.00 USD | 0.00 USD | 6,530.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 826,560.00 USD | 0.00 USD | 524,570.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 301,990.00 USD | 0.00 USD | 1,270.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 300,720.00 USD | 0.00 USD | 53,690.00 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 247,040.00 USD | 0.00 USD | 1,920.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 245,120.00 USD | 0.00 USD | 6,100.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 239,030.00 USD | 0.00 USD | 850.90 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 238,170.00 USD | 0.00 USD | 1,040.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 237,130.00 USD | 0.00 USD | 6,220.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 230,910.00 USD | 0.00 USD | 10,000.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 220,910.00 USD | 0.00 USD | 43,570.00 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 177,340.00 USD | 0.00 USD | 131.90 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 177,210.00 USD | 0.00 USD | 4,710.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 172,500.00 USD | 0.00 USD | 3,220.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 169,280.00 USD | 0.00 USD | 64,780.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 104,500.00 USD | 0.00 USD | 6,130.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 98,370.00 USD | 0.00 USD | 6,770.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 91,600.00 USD | 0.00 USD | 996.01 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 90,610.00 USD | 0.00 USD | 2,100.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 88,500.00 USD | 0.00 USD | 949.53 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 87,550.00 USD | 0.00 USD | 100.11 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 87,450.00 USD | 0.00 USD | 135.99 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 87,320.00 USD | 0.00 USD | 1,010.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 86,310.00 USD | 0.00 USD | 5,640.00 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 80,670.00 USD | 0.00 USD | 936.05 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 79,730.00 USD | 0.00 USD | 34,710.00 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 45,020.00 USD | 0.00 USD | 32,490.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 12,540.00 USD | 0.00 USD | 157.74 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 12,380.00 USD | 0.00 USD | 3,380.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 9,000.00 USD | 0.00 USD | 1,400.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 7,600.00 USD | 0.00 USD | 486.30 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 7,110.00 USD | 0.00 USD | 359.28 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 6,750.00 USD | 0.00 USD | 828.18 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 5,920.00 USD | 0.00 USD | 1,950.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 3,980.00 USD | 0.00 USD | 3,980.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 555.44 USD | 555.44 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 1,840.00 USD | 1,280.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 3,000.00 USD | 1,160.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 4,570.00 USD | 1,570.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 7,000.00 USD | 2,430.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 7,920.00 USD | 919.52 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 8,230.00 USD | 311.26 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 8,540.00 USD | 312.14 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 8,700.00 USD | 157.04 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 11,280.00 USD | 2,580.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 50,710.00 USD | 39,430.00 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 91,100.00 USD | 40,390.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 94,400.00 USD | 3,310.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 95,440.00 USD | 1,030.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 98,380.00 USD | 2,940.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 98,600.00 USD | 224.49 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 98,700.00 USD | 103.23 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 102,020.00 USD | 3,320.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 144,590.00 USD | 42,570.00 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 155,760.00 USD | 11,170.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 165,030.00 USD | 9,270.00 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 165,250.00 USD | 218.89 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 179,590.00 USD | 14,330.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 184,650.00 USD | 5,070.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 184,830.00 USD | 174.60 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 184,930.00 USD | 107.28 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 185,370.00 USD | 439.61 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 185,810.00 USD | 437.79 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 187,430.00 USD | 1,620.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 187,620.00 USD | 182.60 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 194,070.00 USD | 6,450.00 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 194,340.00 USD | 275.17 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 194,910.00 USD | 569.25 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 200,890.00 USD | 5,980.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 201,150.00 USD | 257.89 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 202,110.00 USD | 963.52 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 202,330.00 USD | 224.73 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 204,120.00 USD | 1,790.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 204,830.00 USD | 702.27 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 205,940.00 USD | 1,110.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 206,120.00 USD | 181.04 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 206,470.00 USD | 352.11 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 206,630.00 USD | 155.03 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 206,900.00 USD | 276.40 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 207,030.00 USD | 126.24 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 209,430.00 USD | 2,400.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 210,450.00 USD | 1,010.00 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 212,450.00 USD | 2,010.00 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 283,940.00 USD | 71,490.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 284,810.00 USD | 864.28 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 288,730.00 USD | 3,920.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 368,060.00 USD | 79,330.00 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 369,260.00 USD | 1,200.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 370,460.00 USD | 1,200.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 370,600.00 USD | 138.07 USD | 0.00 USD | `+18.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 371,860.00 USD | 1,270.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 372,200.00 USD | 331.63 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 372,510.00 USD | 313.54 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 372,700.00 USD | 186.70 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 373,020.00 USD | 325.75 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 373,210.00 USD | 183.82 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 373,510.00 USD | 299.19 USD | 0.00 USD | `+25.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 412,080.00 USD | 38,580.00 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 412,250.00 USD | 170.69 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 412,390.00 USD | 135.59 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 413,780.00 USD | 1,390.00 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 419,120.00 USD | 5,340.00 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 420,590.00 USD | 1,470.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 501,360.00 USD | 80,770.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 501,530.00 USD | 169.22 USD | 0.00 USD | `+41.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 501,680.00 USD | 153.79 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 502,410.00 USD | 724.89 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 513,560.00 USD | 11,150.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 515,490.00 USD | 1,930.00 USD | 0.00 USD | `+46.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 515,620.00 USD | 135.02 USD | 0.00 USD | `+53.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 515,860.00 USD | 240.85 USD | 0.00 USD | `+82.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 516,960.00 USD | 1,100.00 USD | 0.00 USD | `+82.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 530,570.00 USD | 13,610.00 USD | 0.00 USD | `+95.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 532,410.00 USD | 1,840.00 USD | 0.00 USD | `+96.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 533,400.00 USD | 991.76 USD | 0.00 USD | `+97.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 534,530.00 USD | 1,130.00 USD | 0.00 USD | `+98.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2923` | 25,780,000.00 USD | 0.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD |
| `7D` | `0.2947` | 25,710,000.00 USD | 0.00 USD | 25,710,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD |
| `7D` | `0.2953` | 25,650,000.00 USD | 0.00 USD | 25,650,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD |
| `7D` | `0.2959` | 25,560,000.00 USD | 0.00 USD | 25,560,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 25,420,000.00 USD | 0.00 USD | 25,420,000.00 USD | 122,540.00 USD | 38,150.00 USD | 60,970.00 USD |
| `7D` | `0.2971` | 25,200,000.00 USD | 0.00 USD | 25,200,000.00 USD | 137,530.00 USD | 37,780.00 USD | 57,710.00 USD |
| `7D` | `0.2977` | 24,970,000.00 USD | 0.00 USD | 24,970,000.00 USD | 69,090.00 USD | 18,540.00 USD | 17,670.00 USD |
| `7D` | `0.2983` | 24,860,000.00 USD | 0.00 USD | 24,860,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `7D` | `0.2989` | 24,640,000.00 USD | 0.00 USD | 24,640,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD |
| `7D` | `0.2995` | 24,480,000.00 USD | 0.00 USD | 24,480,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD |
| `7D` | `0.3007` | 24,470,000.00 USD | 0.00 USD | 24,470,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `7D` | `0.3049` | 24,440,000.00 USD | 0.00 USD | 24,440,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `7D` | `0.3055` | 24,390,000.00 USD | 0.00 USD | 24,390,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 885.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3061` | 24,390,000.00 USD | 0.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3066` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 31,110.00 USD | 0.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 67.24 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3073` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3076` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 23,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 24,300,000.00 USD | 0.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3081` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD |
| `7D` | `0.3085` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3086` | 15,590,000.00 USD | 0.00 USD | 15,590,000.00 USD | 648.20 USD | 0.00 USD | 15,810.00 USD |
| `1D` | `0.3091` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 321.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3096` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 15,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 24,190,000.00 USD | 0.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3101` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 36,900.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3106` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 17,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3116` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 0.00 USD | 17,210.00 USD | 17,620.00 USD |
| `1D` | `0.3121` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,970.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3121` | 23,990,000.00 USD | 0.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3126` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 12,830.00 USD | 13,530.00 USD | 7,580.00 USD |
| `7D` | `0.3127` | 23,810,000.00 USD | 0.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3131` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 37.20 USD | 28,470.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3136` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 20.40 USD | 34,540.00 USD | 9,590.00 USD |
| `7D` | `0.3139` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3141` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 1,010.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3146` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 899.30 USD | 5,900.00 USD | 0.00 USD |
| `1D` | `0.3151` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 23,360,000.00 USD | 0.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3156` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 24,650.00 USD | 3,680.00 USD | 10,790.00 USD |
| `7D` | `0.3157` | 23,110,000.00 USD | 0.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3161` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 0.00 USD | 2,990.00 USD | 5,450.00 USD |
| `7D` | `0.3163` | 22,560,000.00 USD | 0.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3166` | 15,130,000.00 USD | 0.00 USD | 15,130,000.00 USD | 43,210.00 USD | 37,250.00 USD | 17,210.00 USD |
| `7D` | `0.3169` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD |
| `1D` | `0.3171` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 6,720.00 USD | 35,130.00 USD | 35,030.00 USD |
| `7D` | `0.3175` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD |
| `1D` | `0.3176` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 49,880.00 USD | 9,730.00 USD | 30,850.00 USD |
| `1D` | `0.3181` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 315,930.00 USD | 66,130.00 USD | 99,380.00 USD |
| `7D` | `0.3181` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3186` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 164,170.00 USD | 54,010.00 USD | 51,430.00 USD |
| `7D` | `0.3187` | 19,600,000.00 USD | 0.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3191` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 45,860.00 USD | 0.00 USD | 42,840.00 USD |
| `7D` | `0.3193` | 19,130,000.00 USD | 0.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3196` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 29,860.00 USD | 3,120.00 USD | 0.00 USD |
| `7D` | `0.3199` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3201` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 237,870.00 USD | 6,370.00 USD | 11,150.00 USD |
| `7D` | `0.3205` | 18,830,000.00 USD | 0.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3206` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 123,240.00 USD | 24,130.00 USD | 86,190.00 USD |
| `1D` | `0.3211` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 35,150.00 USD | 25,270.00 USD | 90,380.00 USD |
| `7D` | `0.3211` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3216` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 5,550.00 USD | 21,120.00 USD | 70,540.00 USD |
| `7D` | `0.3217` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3221` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 61,560.00 USD | 17,600.00 USD | 72,520.00 USD |
| `7D` | `0.3223` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3226` | 13,100,000.00 USD | 0.00 USD | 13,100,000.00 USD | 70,750.00 USD | 0.00 USD | 202,490.00 USD |
| `7D` | `0.3229` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD |
| `1D` | `0.3231` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 9,630.00 USD | 46,020.00 USD | 104,800.00 USD |
| `7D` | `0.3235` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD |
| `1D` | `0.3236` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 61,120.00 USD | 72,910.00 USD | 143,550.00 USD |
| `1D` | `0.3241` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 966.93 USD | 23,400.00 USD | 122,990.00 USD |
| `7D` | `0.3241` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD |
| `1D` | `0.3246` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 386,130.00 USD | 100,760.00 USD | 223,450.00 USD |
| `7D` | `0.3247` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3251` | 11,530,000.00 USD | 0.00 USD | 11,530,000.00 USD | 820,760.00 USD | 114,270.00 USD | 317,710.00 USD |
| `7D` | `0.3253` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3256` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 220,770.00 USD | 64,600.00 USD | 309,080.00 USD |
| `7D` | `0.3259` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3261` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD |
| `7D` | `0.3265` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3266` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 933.66 USD | 30,260.00 USD | 141,160.00 USD |
| `1D` | `0.3271` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 162,490.00 USD | 73,710.00 USD | 227,940.00 USD |
| `7D` | `0.3271` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3276` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 155,490.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3281` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 57,970.00 USD | 32,250.00 USD | 0.00 USD |
| `7D` | `0.3283` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3286` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 45,960.00 USD | 0.00 USD | 113,560.00 USD |
| `1D` | `0.3291` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 38,710.00 USD | 0.00 USD | 152,210.00 USD |
| `7D` | `0.3295` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `0.3296` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 977.29 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3301` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 36,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3301` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3306` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 112,020.00 USD | 0.00 USD | 11,710.00 USD |
| `7D` | `0.3307` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3311` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 246,180.00 USD | 113,820.00 USD | 338,680.00 USD |
| `7D` | `0.3313` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3316` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 158,550.00 USD | 65,180.00 USD | 77,680.00 USD |
| `7D` | `0.3319` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3321` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 14,290.00 USD | 44,860.00 USD | 295,390.00 USD |
| `7D` | `0.3325` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD |
| `1D` | `0.3326` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 154,010.00 USD | 89,560.00 USD | 276,370.00 USD |
| `1D` | `0.3331` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 28,850.00 USD | 8,990.00 USD | 54,030.00 USD |
| `7D` | `0.3331` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD |
| `1D` | `0.3336` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 158,800.00 USD | 170,300.00 USD | 413,740.00 USD |
| `7D` | `0.3337` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD |
| `1D` | `0.3341` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 76,100.00 USD | 152,670.00 USD | 178,470.00 USD |
| `7D` | `0.3343` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD |
| `1D` | `0.3346` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 168,490.00 USD | 36,310.00 USD | 23,980.00 USD |
| `7D` | `0.3349` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3351` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 109,310.00 USD | 19,610.00 USD | 97,580.00 USD |
| `7D` | `0.3355` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD |
| `1D` | `0.3356` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 191,400.00 USD | 5,810.00 USD | 126,490.00 USD |
| `1D` | `0.3361` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 79,180.00 USD | 85,270.00 USD | 79,030.00 USD |
| `7D` | `0.3361` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3366` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 257,840.00 USD | 9,190.00 USD | 26,970.00 USD |
| `7D` | `0.3367` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3371` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 73,780.00 USD | 24,860.00 USD | 13,620.00 USD |
| `7D` | `0.3373` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3376` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 434,190.00 USD | 130,530.00 USD | 40,650.00 USD |
| `7D` | `0.3379` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3381` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 287,610.00 USD | 122,850.00 USD | 16,800.00 USD |
| `7D` | `0.3385` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD |
| `1D` | `0.3386` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 163,580.00 USD | 44,920.00 USD | 82,020.00 USD |
| `1D` | `0.3391` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 65,650.00 USD | 103,260.00 USD | 46,300.00 USD |
| `7D` | `0.3391` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3396` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 144,030.00 USD | 84,320.00 USD | 300,030.00 USD |
| `7D` | `0.3397` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD |
| `1D` | `0.3401` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 53,400.00 USD | 102,500.00 USD | 216,250.00 USD |
| `7D` | `0.3403` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD |
| `1D` | `0.3406` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 206,060.00 USD | 198,260.00 USD | 207,390.00 USD |
| `7D` | `0.3409` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD |
| `1D` | `0.3411` | 469,180.00 USD | 0.00 USD | 469,180.00 USD | 161,360.00 USD | 236,110.00 USD | 71,720.00 USD |
| `7D` | `0.3415` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD |
| `1D` | `0.3416` | 766,400.00 USD | 766,400.00 USD | 0.00 USD | 605,570.00 USD | 70,270.00 USD | 90,560.00 USD |
| `1D` | `0.3416` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 605,570.00 USD | 70,270.00 USD | 90,560.00 USD |
| `1D` | `0.3421` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 75,300.00 USD | 0.00 USD |
| `1D` | `0.3426` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | 0.00 USD |
| `7D` | `0.3427` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD |
| `1D` | `0.3431` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 220,760.00 USD | 0.00 USD |
| `1D` | `0.3436` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 73,980.00 USD | 0.00 USD |
| `7D` | `0.3439` | 733,270.00 USD | 0.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3441` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD |
| `1D` | `0.3446` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 75,030.00 USD | 0.00 USD |
| `1D` | `0.3451` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 39,880.00 USD | 0.00 USD |
| `7D` | `0.3451` | 538,440.00 USD | 0.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3456` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 166,920.00 USD |
| `1D` | `0.3461` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 203,150.00 USD |
| `7D` | `0.3472` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3481` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47,530.00 USD |
| `1D` | `0.3491` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61,240.00 USD |
| `1D` | `0.3496` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79,030.00 USD |
| `1D` | `0.3501` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 410,930.00 USD |
| `1D` | `0.3506` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,420.00 USD |
| `7D` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3516` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 21,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 25,310.00 USD | 86,040.00 USD | 88,110.00 USD |
| `7D` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3536` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 119,840.00 USD | 12,790.00 USD | 195,270.00 USD |
| `1D` | `0.3541` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 75,280.00 USD | 73,320.00 USD | 0.00 USD |
| `7D` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD |
| `1D` | `0.3546` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 41,600.00 USD | 37,920.00 USD |
| `7D` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3551` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 37,660.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD |
| `1D` | `0.3556` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 20,180.00 USD | 54,340.00 USD | 0.00 USD |
| `1D` | `0.3561` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 25,000.00 USD | 106,140.00 USD |
| `7D` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3566` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 11,630.00 USD | 39,520.00 USD |
| `1D` | `0.3571` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD |
| `1D` | `0.3576` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 159,700.00 USD | 18,380.00 USD | 0.00 USD |
| `1D` | `0.3581` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,950.00 USD |
| `1D` | `0.3586` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 12,770.00 USD | 14,930.00 USD | 0.00 USD |
| `7D` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3591` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 18,730.00 USD | 15,750.00 USD | 33,590.00 USD |
| `7D` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3596` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 135,370.00 USD | 12,460.00 USD | 99,590.00 USD |
| `1D` | `0.3601` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 36,520.00 USD | 163,110.00 USD |
| `7D` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3606` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 59,920.00 USD | 32,860.00 USD | 195,380.00 USD |
| `7D` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3611` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 86,030.00 USD | 60,060.00 USD | 190,770.00 USD |
| `7D` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3616` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 225,350.00 USD | 38,210.00 USD | 150,170.00 USD |
| `7D` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD |
| `1D` | `0.3621` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 143,010.00 USD | 113,560.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3626` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 99,950.00 USD | 49,330.00 USD | 0.00 USD |
| `1D` | `0.3631` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 1,260,000.00 USD | 102,260.00 USD | 93,510.00 USD |
| `7D` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3636` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 183,690.00 USD | 48,500.00 USD | 185,880.00 USD |
| `7D` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3641` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 85,150.00 USD | 229,250.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3646` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 342,300.00 USD | 21,220.00 USD | 62,250.00 USD |
| `7D` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3651` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 67,160.00 USD | 207,000.00 USD |
| `7D` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3656` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 463,120.00 USD | 130,170.00 USD | 284,120.00 USD |
| `1D` | `0.3661` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 264,180.00 USD | 58,300.00 USD | 16,800.00 USD |
| `7D` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3666` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 476,030.00 USD | 108,070.00 USD | 49,800.00 USD |
| `7D` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD |
| `1D` | `0.3671` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 83,650.00 USD | 87,880.00 USD | 387,820.00 USD |
| `7D` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3676` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 55,130.00 USD | 48,480.00 USD | 210,130.00 USD |
| `7D` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3681` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 751,690.00 USD | 104,570.00 USD | 103,470.00 USD |
| `7D` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3686` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 326,450.00 USD | 147,370.00 USD | 126,390.00 USD |
| `1D` | `0.3691` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 460,950.00 USD | 49,680.00 USD | 23,760.00 USD |
| `7D` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD |
| `1D` | `0.3696` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 161,360.00 USD | 81,600.00 USD | 0.00 USD |
| `7D` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD |
| `1D` | `0.3701` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 504,210.00 USD | 196,170.00 USD | 27,870.00 USD |
| `1D` | `0.3706` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 247,470.00 USD | 0.00 USD | 554,730.00 USD |
| `7D` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3711` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 547,890.00 USD | 102,740.00 USD | 225,950.00 USD |
| `7D` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3716` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 75,120.00 USD | 229,370.00 USD | 799,390.00 USD |
| `1D` | `0.3721` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 11,440.00 USD | 58,130.00 USD | 77,610.00 USD |
| `7D` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3726` | 19,390,000.00 USD | 19,390,000.00 USD | 0.00 USD | 505,700.00 USD | 26,770.00 USD | 567,550.00 USD |
| `7D` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3731` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 33,590.00 USD | 142,000.00 USD | 943,090.00 USD |
| `7D` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3736` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 214,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3741` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 49,810.00 USD | 163,770.00 USD | 403,580.00 USD |
| `7D` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3746` | 21,760,000.00 USD | 21,760,000.00 USD | 0.00 USD | 30,710.00 USD | 46,440.00 USD | 341,310.00 USD |
| `1D` | `0.3751` | 22,610,000.00 USD | 22,610,000.00 USD | 0.00 USD | 363,100.00 USD | 0.00 USD | 485,230.00 USD |
| `1D` | `0.3756` | 22,890,000.00 USD | 22,890,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 265,460.00 USD |
| `7D` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3761` | 24,120,000.00 USD | 24,120,000.00 USD | 0.00 USD | 303,200.00 USD | 70,910.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3766` | 24,180,000.00 USD | 24,180,000.00 USD | 0.00 USD | 21,660.00 USD | 24,840.00 USD | 12,250.00 USD |
| `7D` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3771` | 24,220,000.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 32,810.00 USD | 15,810.00 USD |
| `1D` | `0.3776` | 24,530,000.00 USD | 24,530,000.00 USD | 0.00 USD | 1,210.00 USD | 75,650.00 USD | 230,890.00 USD |
| `1D` | `0.3781` | 24,550,000.00 USD | 24,550,000.00 USD | 0.00 USD | 16,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3786` | 25,060,000.00 USD | 25,060,000.00 USD | 0.00 USD | 220,670.00 USD | 0.00 USD | 289,160.00 USD |
| `7D` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3791` | 25,240,000.00 USD | 25,240,000.00 USD | 0.00 USD | 36,900.00 USD | 96,440.00 USD | 46,470.00 USD |
| `7D` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3796` | 25,260,000.00 USD | 25,260,000.00 USD | 0.00 USD | 17,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3801` | 25,390,000.00 USD | 25,390,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 134,070.00 USD |
| `7D` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3806` | 25,600,000.00 USD | 25,600,000.00 USD | 0.00 USD | 855.55 USD | 9,110.00 USD | 200,160.00 USD |
| `1D` | `0.3811` | 25,640,000.00 USD | 25,640,000.00 USD | 0.00 USD | 12,410.00 USD | 8,100.00 USD | 17,620.00 USD |
| `7D` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3816` | 25,690,000.00 USD | 25,690,000.00 USD | 0.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3821` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 12,760.00 USD | 39,470.00 USD | 225,330.00 USD |
| `7D` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3826` | 25,990,000.00 USD | 25,990,000.00 USD | 0.00 USD | 1,720.00 USD | 2,520.00 USD | 21,520.00 USD |
| `1D` | `0.3831` | 26,020,000.00 USD | 26,020,000.00 USD | 0.00 USD | 0.00 USD | 23,940.00 USD | 9,590.00 USD |
| `1D` | `0.3836` | 26,240,000.00 USD | 26,240,000.00 USD | 0.00 USD | 0.00 USD | 10,610.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 26,260,000.00 USD | 26,260,000.00 USD | 0.00 USD | 850.22 USD | 3,580.00 USD | 9,540.00 USD |
| `7D` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3846` | 26,260,000.00 USD | 26,260,000.00 USD | 0.00 USD | 899.18 USD | 2,330.00 USD | 0.00 USD |
| `1D` | `0.3851` | 26,290,000.00 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD |
| `1D` | `0.3856` | 26,310,000.00 USD | 26,310,000.00 USD | 0.00 USD | 24,650.00 USD | 1,850.00 USD | 0.00 USD |
| `7D` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3861` | 26,330,000.00 USD | 26,330,000.00 USD | 0.00 USD | 0.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `1D` | `0.3866` | 26,360,000.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 31,770.00 USD | 0.00 USD |
| `1D` | `0.3871` | 26,410,000.00 USD | 26,410,000.00 USD | 0.00 USD | 43,210.00 USD | 3,150.00 USD | 0.00 USD |
| `1D` | `0.3876` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 14,770.00 USD | 28,230.00 USD | 23,380.00 USD |
| `7D` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3881` | 26,490,000.00 USD | 26,490,000.00 USD | 0.00 USD | 7,350.00 USD | 0.00 USD | 9,330.00 USD |
| `7D` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `1D` | `0.3886` | 26,520,000.00 USD | 26,520,000.00 USD | 0.00 USD | 434.57 USD | 11,790.00 USD | 18,520.00 USD |
| `7D` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3891` | 26,550,000.00 USD | 26,550,000.00 USD | 0.00 USD | 9,680.00 USD | 3,350.00 USD | 11,950.00 USD |
| `7D` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `1D` | `0.3896` | 26,610,000.00 USD | 26,610,000.00 USD | 0.00 USD | 0.00 USD | 30,250.00 USD | 27,870.00 USD |
| `1D` | `0.3901` | 26,670,000.00 USD | 26,670,000.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | 20,860.00 USD |
| `7D` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3906` | 26,700,000.00 USD | 26,700,000.00 USD | 0.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `1D` | `0.3911` | 26,760,000.00 USD | 26,760,000.00 USD | 0.00 USD | 54,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3916` | 27,000,000.00 USD | 27,000,000.00 USD | 0.00 USD | 211,200.00 USD | 17,950.00 USD | 11,150.00 USD |
| `1D` | `0.3919` | 27,090,000.00 USD | 27,090,000.00 USD | 0.00 USD | 69,650.00 USD | 0.00 USD | 22,790.00 USD |
| `7D` | `0.3919` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3925` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 14,330,000.00 USD | 14,330,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 107,420.00 USD | 10,160.00 USD | 112,040.00 USD |
| `7D` | `0.3961` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 143,850.00 USD | 54,030.00 USD | 8,320.00 USD |
| `7D` | `0.3967` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD |
| `7D` | `0.4003` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `7D` | `0.4009` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.4015` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `419.95M` | Total OI Tokens: `1,228,005,418.9 TRX`
  * 1h OI Change: `-0.88%` | 4h OI Change: `+2.97%` | 24h OI Change: `+45.71%`
  * Exchange Breakdown: Binance=`111.76M` | Bybit=`85.05M` | OKX=`25.54M` | Hyperliquid=`18.48M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-340.61K` | Last 24h: `-591.57K` | Last 3d: `-625.17K` | Last 7d: `-857.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.1650%` | **USDT OKX** | `-0.4460%` |
| **USDT Bybit** | `-0.0375%` | **USDT KuCoin** | `-0.0189%` |
| **USDT MEXC** | `-0.1668%` | **USDT BingX** | `-0.4310%` |
| **USDT Gate** | `-0.1050%` | **USDT Bitget** | `-0.2568%` |
| **CoinM Binance** | `-0.3221%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `46.23%` | `53.77%` | `0.86` | 6,830,000.00 USD |
| `15M` | `Binance` | `51.62%` | `48.38%` | `1.07` | 2,310,000.00 USD |
| `15M` | `OKX` | `46.61%` | `53.39%` | `0.87` | 668,360.00 USD |
| `15M` | `Bybit` | `51.11%` | `48.89%` | `1.05` | 975,010.00 USD |
| `15M` | `KuCoin` | `51.69%` | `48.31%` | `1.07` | 42,580.00 USD |
| `15M` | `Gate` | `38.46%` | `61.54%` | `0.62` | 275,990.00 USD |
| `15M` | `Bitget` | `61.31%` | `38.69%` | `1.58` | 269,580.00 USD |
| `15M` | `BingX` | `7.03%` | `92.97%` | `0.08` | 697,720.00 USD |
| `15M` | `MEXC` | `47.46%` | `52.54%` | `0.90` | 279,740.00 USD |
| `15M` | `Bitunix` | `44.49%` | `55.51%` | `0.80` | 121,190.00 USD |
| `15M` | `Hyperliquid` | `64.58%` | `35.42%` | `1.82` | 8,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.92%` | `45.08%` | `1.22` | 1,100,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `19.36%` | `80.64%` | `0.24` | 60,410.00 USD |
| `15M` | `HTX` | `20.57%` | `79.43%` | `0.26` | 16,240.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `59.01%` | `40.99%` | `1.44` | 459.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `21.77%` | `78.23%` | `0.28` | 1,780.00 USD |
| `15M` | `Whale Positions` | `51.62%` | `48.38%` | `1.07` | 2,310,000.00 USD |
| `15M` | `Global Accounts` | `46.23%` | `53.77%` | `0.86` | 6,830,000.00 USD |
| `1H` | `TRX` | `47.85%` | `52.15%` | `0.92` | 18,660,000.00 USD |
| `1H` | `Binance` | `46.9%` | `53.1%` | `0.88` | 6,870,000.00 USD |
| `1H` | `OKX` | `43.11%` | `56.89%` | `0.76` | 1,650,000.00 USD |
| `1H` | `Bybit` | `54.82%` | `45.18%` | `1.21` | 2,570,000.00 USD |
| `1H` | `KuCoin` | `49.67%` | `50.33%` | `0.99` | 128,680.00 USD |
| `1H` | `Gate` | `51.23%` | `48.77%` | `1.05` | 810,640.00 USD |
| `1H` | `Bitget` | `49.41%` | `50.59%` | `0.98` | 792,630.00 USD |
| `1H` | `BingX` | `46.41%` | `53.59%` | `0.87` | 975,580.00 USD |
| `1H` | `MEXC` | `54.01%` | `45.99%` | `1.17` | 847,630.00 USD |
| `1H` | `Bitunix` | `49.73%` | `50.27%` | `0.99` | 340,320.00 USD |
| `1H` | `Hyperliquid` | `37.06%` | `62.94%` | `0.59` | 87,730.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.82%` | `49.18%` | `1.03` | 3,300,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `47.31%` | `52.69%` | `0.90` | 176,670.00 USD |
| `1H` | `HTX` | `45.9%` | `54.1%` | `0.85` | 68,440.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `26.42%` | `73.58%` | `0.36` | 2,190.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.93%` | `39.07%` | `1.56` | 36,330.00 USD |
| `1H` | `Whale Positions` | `46.9%` | `53.1%` | `0.88` | 6,870,000.00 USD |
| `1H` | `Global Accounts` | `47.85%` | `52.15%` | `0.92` | 18,660,000.00 USD |
| `4H` | `TRX` | `49.57%` | `50.43%` | `0.98` | 94,810,000.00 USD |
| `4H` | `Binance` | `50.1%` | `49.9%` | `1.00` | 33,640,000.00 USD |
| `4H` | `OKX` | `49.26%` | `50.74%` | `0.97` | 9,120,000.00 USD |
| `4H` | `Bybit` | `52.88%` | `47.12%` | `1.12` | 12,080,000.00 USD |
| `4H` | `KuCoin` | `51.01%` | `48.99%` | `1.04` | 793,540.00 USD |
| `4H` | `Gate` | `52.04%` | `47.96%` | `1.09` | 2,990,000.00 USD |
| `4H` | `Bitget` | `47.7%` | `52.3%` | `0.91` | 3,290,000.00 USD |
| `4H` | `BingX` | `42.87%` | `57.13%` | `0.75` | 6,440,000.00 USD |
| `4H` | `MEXC` | `49.66%` | `50.34%` | `0.99` | 5,150,000.00 USD |
| `4H` | `Bitunix` | `43.06%` | `56.94%` | `0.76` | 2,530,000.00 USD |
| `4H` | `Hyperliquid` | `56.24%` | `43.76%` | `1.29` | 600,990.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.19%` | `47.81%` | `1.09` | 16,120,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.98%` | `89.02%` | `0.12` | 768,480.00 USD |
| `4H` | `HTX` | `47.81%` | `52.19%` | `0.92` | 649,290.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.74%` | `51.26%` | `0.95` | 196,450.00 USD |
| `4H` | `Aster` | `15.37%` | `84.63%` | `0.18` | 268,240.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.57%` | `75.43%` | `0.33` | 163,400.00 USD |
| `4H` | `Whale Positions` | `50.1%` | `49.9%` | `1.00` | 33,640,000.00 USD |
| `4H` | `Global Accounts` | `49.57%` | `50.43%` | `0.98` | 94,810,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3551` | `0.3543` | `0.3551` | `0.3561` | `0.3515` | 3,963,398.63 USD | 1,776,100.41 USD | 2,187,298.22 USD | -411,197.81 USD | `-10.37%` | `5B / 21S` |
| `0:00 UTC` | `0.3520` | `0.3514` | `0.3520` | `0.3534` | `0.3499` | 4,774,258.73 USD | 2,385,646.34 USD | 2,388,612.39 USD | -2,966.06 USD | `-0.06%` | `18B / 14S` |
| `5:00 UTC` | `0.3528` | `0.3532` | `0.3528` | `0.3548` | `0.3511` | 2,568,313.45 USD | 1,243,630.68 USD | 1,324,682.77 USD | -81,052.09 USD | `-3.16%` | `19B / 34S` |
| `0:00 UTC` | `0.3524` | `0.3518` | `0.3524` | `0.3549` | `0.3493` | 4,212,194.59 USD | 2,183,257.63 USD | 2,028,936.96 USD | 154,320.67 USD | `+3.66%` | `11B / 11S` |
| `5:00 UTC` | `0.3505` | `0.3505` | `0.3505` | `0.3539` | `0.3475` | 4,325,285.35 USD | 1,848,013.35 USD | 2,477,272.00 USD | -629,258.65 USD | `-14.55%` | `8B / 22S` |
| `0:00 UTC` | `0.3460` | `0.3471` | `0.3460` | `0.3497` | `0.3450` | 7,401,583.91 USD | 3,367,813.41 USD | 4,033,770.49 USD | -665,957.08 USD | `-9.00%` | `10B / 13S` |
| `5:00 UTC` | `0.3454` | `0.3452` | `0.3454` | `0.3460` | `0.3444` | 2,735,847.92 USD | 1,369,518.79 USD | 1,366,329.13 USD | 3,189.66 USD | `+0.12%` | `29B / 17S` |
| `0:00 UTC` | `0.3463` | `0.3466` | `0.3463` | `0.3482` | `0.3449` | 2,895,955.74 USD | 1,679,080.86 USD | 1,216,874.88 USD | 462,205.98 USD | `+15.96%` | `37B / 15S` |
| `5:00 UTC` | `0.3476` | `0.3475` | `0.3476` | `0.3487` | `0.3457` | 2,690,622.76 USD | 1,438,688.18 USD | 1,251,934.57 USD | 186,753.61 USD | `+6.94%` | `22B / 33S` |
| `0:00 UTC` | `0.3418` | `0.3429` | `0.3418` | `0.3460` | `0.3414` | 4,572,480.67 USD | 1,512,080.05 USD | 3,060,400.62 USD | -1,548,320.57 USD | `-33.86%` | `2B / 38S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 14:33` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3320` | 2,500,000.00 USD | 0.00 USD |
| `10-28 14:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3319` | 0.00 USD | 0.00 USD |
| `10-28 14:18` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3318` | 0.00 USD | 0.00 USD |
| `10-28 14:13` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3317` | 438,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:48` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 13:43` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3318` | 192,000.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3315` | 266,000.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3315` | 493,000.00 USD | 0.00 USD |
| `10-28 09:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3313` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3309` | 205,000.00 USD | 0.00 USD |
| `10-28 05:53` | `Volume 1.0M TRX` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:51` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:44` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3318` | 198,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 399,980.00 USD | -21,840.00 USD | **`ACCUMULATION`** |
| `15m` | -26,720.00 USD | -1,370,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,090,000.00 USD | -1,130,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -208,900.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,760,000.00 USD | -1,810,000.00 USD | **`ACCUMULATION`** |
| `4h` | 8,500,000.00 USD | -2,160,000.00 USD | **`ACCUMULATION`** |
| `6h` | 8,390,000.00 USD | 8,950,000.00 USD | **`ACCUMULATION`** |
| `8h` | 12,650,000.00 USD | 9,630,000.00 USD | **`ACCUMULATION`** |
| `12h` | 11,880,000.00 USD | 10,180,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,230,000.00 USD | 10,520,000.00 USD | **`ACCUMULATION`** |
| `1w` | 6,180,000.00 USD | 9,110,000.00 USD | **`ACCUMULATION`** |
| `30d` | -14,040,000.00 USD | 9,940,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+399.98K` | 15m=`-26.72K` | 1h=`-208.90K` | 24h=`+12.23M`
* Futures Capital Netflows: 5m=`-21.84K` | 15m=`-1.37M` | 1h=`-1.43M` | 24h=`+10.52M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3453` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3364` (Risk Distance: `0.0089` pts)
  * +2.5R Take Profit: `0.3675`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3570` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3659` (Risk Distance: `0.0089` pts)
  * +2.5R Take Profit: `0.3348`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3452`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
