# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:31:46 IST` (`2026-10-30 05:01:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3455` | **Live Ask Quote**: `0.3488` | **Mid Price**: `0.3471`
- **Spread Points**: `33.00` | **Spread BPS**: `95.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3524` | VWAP Z-Score: `-2.19` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0043` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `45.11` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3623` | Lower -3.00σ Band: `0.3424`
  * Upper +2.51σ Band: `0.3607` | Lower -2.51σ Band: `0.3441`
  * Upper +2.01σ Band: `0.3590` | Lower -2.01σ Band: `0.3457`
  * Upper +2.00σ Band: `0.3590` | Lower -2.00σ Band: `0.3457`
  * Upper +1.28σ Band: `0.3566` | Lower -1.28σ Band: `0.3481`
  * Upper +1.00σ Band: `0.3557` | Lower -1.00σ Band: `0.3491`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3478` | EMA-20=`0.3487` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3444` (Slope: `+0.0000`) | EMA-100=`0.3395`
  * Institutional Anchors: EMA-144=`0.3371` | EMA-200=`0.3353` (Slope: `+0.5626`) | EMA-233=`0.3345`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3570` (Distance: `-2.72%`)
  * Point of Control (POC) = `0.3512` (Distance: `-1.13%`)
  * Value Area Low (VAL) = `0.3455` (Distance: `+0.51%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3482` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3485` | Low=`0.3458`
  * New York Session (13:00-21:00 UTC): High=`0.3492` | Low=`0.3451`
  * Initial Balance (First Hour): IB High=`0.3482` | IB Low=`0.3461`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3458` - `0.3485`
  * Optimal Trade Entry (OTE 0.705): `0.3478`
  * Structural Invalidation Anchor (0.786): `0.3499`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3449` | `0.3470` | `0.3449` | `0.3464` | `3,497,207` | 1,210,402.01 USD | 101,488.64 USD | `+8.38%` | 4,623,006.88 USD | `+0.81` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.3464` | `0.3482` | `0.3463` | `0.3465` | `2,667,532` | 925,587.96 USD | 215,403.14 USD | `+23.27%` | 4,838,410.02 USD | `+1.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3465` | `0.3475` | `0.3461` | `0.3474` | `1,775,835` | 615,687.78 USD | 138,167.07 USD | `+22.44%` | 4,976,577.09 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3455` | `0.3460` | `0.3444` | `0.3449` | `7,925,852` | 2,735,847.92 USD | 3,189.66 USD | `+0.12%` | 4,571,484.24 USD | `-0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3449` | `0.3482` | `0.3449` | `0.3472` | `8,355,971` | 2,895,955.74 USD | 462,205.98 USD | `+15.96%` | 5,033,690.22 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3472` | `0.3480` | `0.3467` | `0.3473` | `4,023,397` | 1,397,830.26 USD | 129,704.29 USD | `+9.28%` | 5,163,394.50 USD | `+0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3565` | `0.3599` | `0.3515` | `0.3526` | `36,953,084` | 13,170,319.10 USD | -246,981.15 USD | `-1.88%` | 5,793,207.80 USD | `-0.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3526` | `0.3549` | `0.3475` | `0.3495` | `45,168,744` | 15,880,052.12 USD | -558,956.14 USD | `-3.52%` | 5,234,251.67 USD | `-0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3495` | `0.3497` | `0.3444` | `0.3473` | `41,602,669` | 14,422,626.36 USD | -79,384.03 USD | `-0.55%` | 5,154,867.64 USD | `-0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3444` | `0.3474` | `37,197,230` | 12,892,104.49 USD | -204,713.67 USD | `-1.59%` | 4,651,973.08 USD | `-1.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 385,562.36 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 597,653.23 USD | `+0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3444` | `0.3473` | `41,602,669` | 14,422,626.36 USD | -79,384.03 USD | `-0.55%` | 4,777,302.72 USD | `-0.92` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3471`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `897` | `0xecb6...2b00` | `LONG` | 2,522,178.03 USD | `7,254,100.00` | `0.3343` | `0.3477` | `0.000000` | 97,015.34 USD | `+3.85%` | `10X Cross` |
| `1550` | `0xeadc...9d55` | `LONG` | 1,390,760.00 USD | `4,000,000.00` | `0.3421` | `0.3477` | `0.000000` | 22,281.91 USD | `+1.60%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `0.0705` | 115.76 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 6,840.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 789.12 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 179.83 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 114.87 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 391.44 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 9,410.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 198.06 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 208.12 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 6,950.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 496.50 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 3,350.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 1,130.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 57,320.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 11,100.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 210.28 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,150.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,170.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 256.98 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 175.37 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 208.67 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 106.68 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,860.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 622.98 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2035` | 88,390.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 418.06 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 227.46 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 286.67 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,360.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 122.23 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 310.39 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,120.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 6,120.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 2,790.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 3,160.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,260.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 152.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 139.92 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,350.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 386.51 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 263.07 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 299.45 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 312.44 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 438.42 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 2,210.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,210.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 449.23 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 27,080.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 983,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,150.00 USD | 982,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 3,950.00 USD | 979,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 80,810.00 USD | 975,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 189.66 USD | 894,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 12,870.00 USD | 894,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 881,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 15,620.00 USD | 875,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 1,420.00 USD | 859,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 5,720.00 USD | 858,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 359.16 USD | 852,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 589.42 USD | 852,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 25,780,000.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 851,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 850,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 850,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 25,710,000.00 USD | 25,710,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 25,650,000.00 USD | 25,650,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 468.37 USD | 850,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 25,560,000.00 USD | 25,560,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 25,420,000.00 USD | 25,420,000.00 USD | 122,540.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 157.14 USD | 850,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 25,200,000.00 USD | 25,200,000.00 USD | 137,530.00 USD | 37,780.00 USD | 57,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 24,970,000.00 USD | 24,970,000.00 USD | 69,090.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 24,860,000.00 USD | 24,860,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 127.46 USD | 849,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2989` | 24,640,000.00 USD | 24,640,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 24,480,000.00 USD | 24,480,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 4,440.00 USD | 849,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 24,470,000.00 USD | 24,470,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,650.00 USD | 845,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,130.00 USD | 834,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 485.90 USD | 832,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 267.35 USD | 832,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3049` | 24,440,000.00 USD | 24,440,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 24,390,000.00 USD | 24,390,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,810.00 USD | 831,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 24,390,000.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 24,310,000.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 24,310,000.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 5,920.00 USD | 817,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3079` | 24,300,000.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 24,200,000.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 1,020.00 USD | 811,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3091` | 24,200,000.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3094` | 20,580,000.00 USD | 20,580,000.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 24,190,000.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3099` | 20,580,000.00 USD | 20,580,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 24,170,000.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3104` | 20,580,000.00 USD | 20,580,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 193.13 USD | 810,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 24,030,000.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3114` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 24,030,000.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,740.00 USD | 809,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3119` | 20,450,000.00 USD | 20,450,000.00 USD | 23,970.00 USD | 10,650.00 USD | 35,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 23,990,000.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3124` | 20,380,000.00 USD | 20,380,000.00 USD | 12,740.00 USD | 3,560.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 3,130.00 USD | 796,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 23,810,000.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3129` | 20,350,000.00 USD | 20,350,000.00 USD | 126.90 USD | 38,440.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 23,690,000.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3134` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 15,080.00 USD | 793,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 20,250,000.00 USD | 20,250,000.00 USD | 952.52 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 23,680,000.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3144` | 20,240,000.00 USD | 20,240,000.00 USD | 911.00 USD | 5,900.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 23,680,000.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 141.84 USD | 777,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3149` | 20,220,000.00 USD | 20,220,000.00 USD | 297.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 23,360,000.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3154` | 20,220,000.00 USD | 20,220,000.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 3,250.00 USD | 777,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3157` | 23,110,000.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3159` | 20,180,000.00 USD | 20,180,000.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 22,560,000.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3164` | 20,150,000.00 USD | 20,150,000.00 USD | 43,210.00 USD | 33,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 774,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 20,070,000.00 USD | 20,070,000.00 USD | 1,090.00 USD | 10,820.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 21,710,000.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3174` | 20,030,000.00 USD | 20,030,000.00 USD | 22,580.00 USD | 37,950.00 USD | 36,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 20,910,000.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3179` | 19,940,000.00 USD | 19,940,000.00 USD | 67,160.00 USD | 27,250.00 USD | 48,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 20,590,000.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3184` | 19,790,000.00 USD | 19,790,000.00 USD | 467,780.00 USD | 71,300.00 USD | 101,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 19,600,000.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3189` | 19,150,000.00 USD | 19,150,000.00 USD | 27,640.00 USD | 30,250.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 19,130,000.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3194` | 19,050,000.00 USD | 19,050,000.00 USD | 74,930.00 USD | 3,120.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 18,950,000.00 USD | 18,950,000.00 USD | 54,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3204` | 18,900,000.00 USD | 18,900,000.00 USD | 236,500.00 USD | 30,500.00 USD | 34,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 18,830,000.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3209` | 18,600,000.00 USD | 18,600,000.00 USD | 103,890.00 USD | 11,980.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 18,730,000.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3214` | 18,420,000.00 USD | 18,420,000.00 USD | 914.92 USD | 34,400.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 17,860,000.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3219` | 18,290,000.00 USD | 18,290,000.00 USD | 5,550.00 USD | 3,820.00 USD | 143,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 17,410,000.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3224` | 18,140,000.00 USD | 18,140,000.00 USD | 132,310.00 USD | 13,780.00 USD | 182,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3225` | 442.15 USD | 773,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3229` | 17,810,000.00 USD | 17,810,000.00 USD | 7,860.00 USD | 46,020.00 USD | 106,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 16,490,000.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3234` | 17,650,000.00 USD | 17,650,000.00 USD | 62,890.00 USD | 42,740.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 15,100,000.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 460.66 USD | 773,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 45,410.00 USD | 157,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 13,520,000.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3244` | 17,290,000.00 USD | 17,290,000.00 USD | 160,140.00 USD | 51,630.00 USD | 193,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3245` | 128.83 USD | 772,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3247` | 12,730,000.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 16,890,000.00 USD | 16,890,000.00 USD | 1,070,000.00 USD | 137,210.00 USD | 226,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 11,400,000.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3254` | 15,460,000.00 USD | 15,460,000.00 USD | 296,640.00 USD | 75,320.00 USD | 424,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3259` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 42,480.00 USD | 94,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 10,060,000.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3264` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 9,680,000.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3269` | 14,490,000.00 USD | 14,490,000.00 USD | 124,870.00 USD | 64,710.00 USD | 369,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 9,490,000.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3274` | 13,930,000.00 USD | 13,930,000.00 USD | 194,040.00 USD | 26,070.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 6,260.00 USD | 772,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3279` | 13,630,000.00 USD | 13,630,000.00 USD | 57,970.00 USD | 39,150.00 USD | 115,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 9,290,000.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 766,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 13,420,000.00 USD | 13,420,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3294` | 13,220,000.00 USD | 13,220,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 8,900,000.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 1,650.00 USD | 21,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3301` | 8,870,000.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3304` | 13,140,000.00 USD | 13,140,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 8,800,000.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3309` | 13,140,000.00 USD | 13,140,000.00 USD | 306,740.00 USD | 39,540.00 USD | 338,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 8,460,000.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3314` | 12,450,000.00 USD | 12,450,000.00 USD | 39,300.00 USD | 117,000.00 USD | 77,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3315` | 4,780.00 USD | 19,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3319` | 12,220,000.00 USD | 12,220,000.00 USD | 159,340.00 USD | 54,860.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3324` | 11,710,000.00 USD | 11,710,000.00 USD | 137,370.00 USD | 95,620.00 USD | 232,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 8,150,000.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3325` | 634.08 USD | 14,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3329` | 11,240,000.00 USD | 11,240,000.00 USD | 30,990.00 USD | 11,620.00 USD | 97,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 7,890,000.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3334` | 11,100,000.00 USD | 11,100,000.00 USD | 38,930.00 USD | 41,320.00 USD | 359,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3335` | 10,660.00 USD | 13,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3337` | 7,230,000.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3339` | 10,660,000.00 USD | 10,660,000.00 USD | 223,020.00 USD | 219,400.00 USD | 232,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3344` | 9,990,000.00 USD | 9,990,000.00 USD | 11,850.00 USD | 75,820.00 USD | 23,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 1,010.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3349` | 9,880,000.00 USD | 9,880,000.00 USD | 266,880.00 USD | 37,190.00 USD | 83,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 6,610,000.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3354` | 9,490,000.00 USD | 9,490,000.00 USD | 1,300.00 USD | 14,760.00 USD | 13,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 6,380,000.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3359` | 9,460,000.00 USD | 9,460,000.00 USD | 268,370.00 USD | 25,890.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 6,110,000.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3364` | 9,100,000.00 USD | 9,100,000.00 USD | 148,220.00 USD | 64,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 6,110,000.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3369` | 8,890,000.00 USD | 8,890,000.00 USD | 110,520.00 USD | 29,430.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 5,860,000.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3374` | 8,710,000.00 USD | 8,710,000.00 USD | 330,500.00 USD | 107,280.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3375` | 116.44 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3379` | 8,250,000.00 USD | 8,250,000.00 USD | 268,220.00 USD | 75,530.00 USD | 16,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 5,270,000.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3384` | 7,890,000.00 USD | 7,890,000.00 USD | 249,030.00 USD | 70,580.00 USD | 49,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 4,610,000.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3385` | 2,200.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3389` | 7,520,000.00 USD | 7,520,000.00 USD | 41,890.00 USD | 100,380.00 USD | 59,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3391` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3394` | 7,320,000.00 USD | 7,320,000.00 USD | 102,390.00 USD | 93,730.00 USD | 198,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,970,000.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3399` | 6,930,000.00 USD | 6,930,000.00 USD | 81,980.00 USD | 130,600.00 USD | 320,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 3,280,000.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3404` | 6,390,000.00 USD | 6,390,000.00 USD | 187,960.00 USD | 65,630.00 USD | 223,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 5,920,000.00 USD | 5,920,000.00 USD | 79,910.00 USD | 243,360.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3414` | 5,570,000.00 USD | 5,570,000.00 USD | 415,020.00 USD | 175,790.00 USD | 110,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3415` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3419` | 4,870,000.00 USD | 4,870,000.00 USD | 808,300.00 USD | 66,220.00 USD | 252,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3424` | 3,740,000.00 USD | 3,740,000.00 USD | 109,050.00 USD | 68,870.00 USD | 101,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3429` | 3,460,000.00 USD | 3,460,000.00 USD | 255,980.00 USD | 167,970.00 USD | 381,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3434` | 2,650,000.00 USD | 2,650,000.00 USD | 119,040.00 USD | 149,150.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3439` | 2,310,000.00 USD | 2,310,000.00 USD | 113,850.00 USD | 49,600.00 USD | 556,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3439` | 733,270.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3444` | 1,590,000.00 USD | 1,590,000.00 USD | 15,020.00 USD | 39,960.00 USD | 286,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3449` | 1,250,000.00 USD | 1,250,000.00 USD | 197,010.00 USD | 81,000.00 USD | 34,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 538,440.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3454` | 934,550.00 USD | 934,550.00 USD | 78,780.00 USD | 5,390.00 USD | 535,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3459` | 314,490.00 USD | 314,490.00 USD | 0.00 USD | 0.00 USD | 314,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3479` | 47,530.00 USD | 47,530.00 USD | 0.00 USD | 0.00 USD | 47,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3499` | 423,180.00 USD | 423,180.00 USD | 0.00 USD | 0.00 USD | 375,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3504` | 458,460.00 USD | 458,460.00 USD | 0.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 529,330.00 USD | 529,330.00 USD | 25,310.00 USD | 45,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3534` | 877,740.00 USD | 877,740.00 USD | 119,840.00 USD | 53,270.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3539` | 1,060,000.00 USD | 1,060,000.00 USD | 53,400.00 USD | 17,980.00 USD | 108,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3544` | 1,200,000.00 USD | 1,200,000.00 USD | 21,880.00 USD | 83,750.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3549` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 50,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3554` | 1,360,000.00 USD | 1,360,000.00 USD | 20,180.00 USD | 40,120.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3559` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 21,340.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3564` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 29,510.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3569` | 1,490,000.00 USD | 1,490,000.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3574` | 1,600,000.00 USD | 1,600,000.00 USD | 95,510.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3579` | 1,670,000.00 USD | 1,670,000.00 USD | 29,500.00 USD | 9,130.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3584` | 1,680,000.00 USD | 1,680,000.00 USD | 1,810.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3594` | 1,940,000.00 USD | 1,940,000.00 USD | 109,010.00 USD | 0.00 USD | 133,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3599` | 2,120,000.00 USD | 2,120,000.00 USD | 45,090.00 USD | 22,780.00 USD | 108,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3604` | 2,370,000.00 USD | 2,370,000.00 USD | 59,920.00 USD | 59,060.00 USD | 136,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3609` | 2,620,000.00 USD | 2,620,000.00 USD | 75,090.00 USD | 25,740.00 USD | 146,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3614` | 2,890,000.00 USD | 2,890,000.00 USD | 10,940.00 USD | 59,640.00 USD | 203,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 3,480,000.00 USD | 3,480,000.00 USD | 368,360.00 USD | 116,660.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3624` | 3,700,000.00 USD | 3,700,000.00 USD | 98,860.00 USD | 52,010.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 4,950,000.00 USD | 4,950,000.00 USD | 1,120,000.00 USD | 42,520.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3634` | 5,360,000.00 USD | 5,360,000.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,410.00 USD | 31,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 5,820,000.00 USD | 5,820,000.00 USD | 183,690.00 USD | 195,330.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3644` | 6,240,000.00 USD | 6,240,000.00 USD | 294,060.00 USD | 93,250.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 43,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 6,630,000.00 USD | 6,630,000.00 USD | 133,400.00 USD | 59,680.00 USD | 195,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3654` | 7,200,000.00 USD | 7,200,000.00 USD | 355,110.00 USD | 47,350.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3659` | 7,730,000.00 USD | 7,730,000.00 USD | 220,710.00 USD | 153,150.00 USD | 156,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3664` | 8,420,000.00 USD | 8,420,000.00 USD | 556,330.00 USD | 70,580.00 USD | 66,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,060.00 USD | 44,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3669` | 8,890,000.00 USD | 8,890,000.00 USD | 153,920.00 USD | 51,490.00 USD | 266,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3674` | 9,220,000.00 USD | 9,220,000.00 USD | 41,260.00 USD | 118,940.00 USD | 166,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 312.74 USD | 45,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3679` | 10,180,000.00 USD | 10,180,000.00 USD | 765,190.00 USD | 29,030.00 USD | 164,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3684` | 10,440,000.00 USD | 10,440,000.00 USD | 1,290.00 USD | 84,510.00 USD | 177,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 2,270.00 USD | 47,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3689` | 11,400,000.00 USD | 11,400,000.00 USD | 715,890.00 USD | 191,500.00 USD | 52,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3694` | 11,720,000.00 USD | 11,720,000.00 USD | 225,120.00 USD | 65,630.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3695` | 151.50 USD | 47,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3699` | 12,250,000.00 USD | 12,250,000.00 USD | 472,310.00 USD | 31,900.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3704` | 13,270,000.00 USD | 13,270,000.00 USD | 285,800.00 USD | 180,250.00 USD | 554,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 13,400,000.00 USD | 13,400,000.00 USD | 110,350.00 USD | 21,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3714` | 14,850,000.00 USD | 14,850,000.00 USD | 489,730.00 USD | 134,200.00 USD | 821,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 982.62 USD | 48,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3719` | 15,330,000.00 USD | 15,330,000.00 USD | 35,660.00 USD | 200,240.00 USD | 245,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3724` | 16,250,000.00 USD | 16,250,000.00 USD | 471,540.00 USD | 46,950.00 USD | 398,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 11,540.00 USD | 60,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3729` | 16,940,000.00 USD | 16,940,000.00 USD | 67,760.00 USD | 135,260.00 USD | 492,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3734` | 17,690,000.00 USD | 17,690,000.00 USD | 76,800.00 USD | 21,010.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 44,750.00 USD | 104,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3739` | 18,280,000.00 USD | 18,280,000.00 USD | 154,860.00 USD | 163,770.00 USD | 266,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3744` | 18,620,000.00 USD | 18,620,000.00 USD | 63,330.00 USD | 33,910.00 USD | 239,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3749` | 19,580,000.00 USD | 19,580,000.00 USD | 229,090.00 USD | 12,530.00 USD | 724,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3754` | 19,730,000.00 USD | 19,730,000.00 USD | 134,010.00 USD | 0.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 6,120.00 USD | 110,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3759` | 20,930,000.00 USD | 20,930,000.00 USD | 188,010.00 USD | 70,910.00 USD | 934,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3764` | 21,250,000.00 USD | 21,250,000.00 USD | 140,690.00 USD | 24,840.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3769` | 21,310,000.00 USD | 21,310,000.00 USD | 19,360.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3774` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 32,300.00 USD | 143,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3779` | 21,610,000.00 USD | 21,610,000.00 USD | 1,210.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3784` | 21,840,000.00 USD | 21,840,000.00 USD | 222,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,700.00 USD | 699,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3789` | 22,210,000.00 USD | 22,210,000.00 USD | 644.45 USD | 80,630.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3794` | 22,320,000.00 USD | 22,320,000.00 USD | 54,830.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3799` | 22,320,000.00 USD | 22,320,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3804` | 22,660,000.00 USD | 22,660,000.00 USD | 0.00 USD | 4,980.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3809` | 22,710,000.00 USD | 22,710,000.00 USD | 13,270.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3814` | 22,750,000.00 USD | 22,750,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3819` | 22,780,000.00 USD | 22,780,000.00 USD | 11,830.00 USD | 13,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3824` | 23,050,000.00 USD | 23,050,000.00 USD | 1,760.00 USD | 25,950.00 USD | 246,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3825` | 4,850.00 USD | 704,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3829` | 23,090,000.00 USD | 23,090,000.00 USD | 896.63 USD | 26,460.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3834` | 23,310,000.00 USD | 23,310,000.00 USD | 0.00 USD | 10,610.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 34,170.00 USD | 739,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3839` | 23,320,000.00 USD | 23,320,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3844` | 23,330,000.00 USD | 23,330,000.00 USD | 1,750.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3854` | 23,370,000.00 USD | 23,370,000.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 120.28 USD | 739,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3859` | 23,400,000.00 USD | 23,400,000.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3864` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3869` | 23,470,000.00 USD | 23,470,000.00 USD | 43,210.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3874` | 23,520,000.00 USD | 23,520,000.00 USD | 5,630.00 USD | 31,380.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3875` | 5,470.00 USD | 744,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3879` | 23,550,000.00 USD | 23,550,000.00 USD | 15,630.00 USD | 0.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3884` | 23,580,000.00 USD | 23,580,000.00 USD | 1,290.00 USD | 0.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3889` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 11,790.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3894` | 23,670,000.00 USD | 23,670,000.00 USD | 9,680.00 USD | 33,600.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 3,660.00 USD | 748,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3899` | 23,690,000.00 USD | 23,690,000.00 USD | 0.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3904` | 23,770,000.00 USD | 23,770,000.00 USD | 74,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 1,800.00 USD | 750,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3909` | 23,820,000.00 USD | 23,820,000.00 USD | 54,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3914` | 24,020,000.00 USD | 24,020,000.00 USD | 182,380.00 USD | 6,370.00 USD | 11,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3915` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 11,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 750,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3919` | 14,140,000.00 USD | 14,140,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 14,300,000.00 USD | 14,300,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3925` | 67,230.00 USD | 817,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3931` | 14,330,000.00 USD | 14,330,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 819,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 14,360,000.00 USD | 14,360,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 14,390,000.00 USD | 14,390,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 166,720.00 USD | 985,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 14,520,000.00 USD | 14,520,000.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 14,750,000.00 USD | 14,750,000.00 USD | 107,420.00 USD | 10,160.00 USD | 112,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 14,960,000.00 USD | 14,960,000.00 USD | 143,850.00 USD | 54,030.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 1,580.00 USD | 987,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3967` | 14,980,000.00 USD | 14,980,000.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 15,120,000.00 USD | 15,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 15,230,000.00 USD | 15,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 15,270,000.00 USD | 15,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 15,290,000.00 USD | 15,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4015` | 290.69 USD | 987,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,210.00 USD | 990,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 990,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 730.12 USD | 991,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 1,000.00 USD | 992,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 11,900.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4275` | 201.78 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4285` | 10,190.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4335` | 1,500.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 71,050.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 378.34 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 421.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 23,340.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4485` | 65,760.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4505` | 585,650.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 318.76 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 5,560.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4535` | 1,140.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,550.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 282,390.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4735` | 8,060.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4845` | 20,330.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4925` | 284.67 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4985` | 771,520.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 23,600.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 945.72 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5545` | 41,030.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5595` | 15,070.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5635` | 54,010.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5705` | 740,080.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5935` | 8,020.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 28,550.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6245` | 32,830.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6265` | 379.03 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 1,140.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 48,630.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 705.13 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6555` | 1,080.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6625` | 2,060.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 2,530.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 1,210.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6665` | 16,500.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6695` | 85,440.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6735` | 83,060.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6865` | 769,680.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6875` | 262.62 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6885` | 846.86 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6925` | 414.12 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0705` | 1,290,000.00 USD | 0.00 USD | 115.76 USD | `-79.78%` | `1,642.00` |
| `Live` | `Long` | `0.0775` | 1,290,000.00 USD | 0.00 USD | 6,840.00 USD | `-77.78%` | `88,233.00` |
| `Live` | `Long` | `0.0795` | 1,280,000.00 USD | 0.00 USD | 789.12 USD | `-77.20%` | `9,926.00` |
| `Live` | `Long` | `0.0865` | 1,280,000.00 USD | 0.00 USD | 179.83 USD | `-75.19%` | `2,079.00` |
| `Live` | `Long` | `0.1095` | 1,280,000.00 USD | 0.00 USD | 114.87 USD | `-68.60%` | `1,049.00` |
| `Live` | `Long` | `0.1165` | 1,280,000.00 USD | 0.00 USD | 391.44 USD | `-66.59%` | `3,360.00` |
| `Live` | `Long` | `0.1225` | 1,280,000.00 USD | 0.00 USD | 9,410.00 USD | `-64.87%` | `76,797.00` |
| `Live` | `Long` | `0.1385` | 1,270,000.00 USD | 0.00 USD | 198.06 USD | `-60.28%` | `1,430.00` |
| `Live` | `Long` | `0.1475` | 1,270,000.00 USD | 0.00 USD | 208.12 USD | `-57.70%` | `1,411.00` |
| `Live` | `Long` | `0.1595` | 1,270,000.00 USD | 0.00 USD | 6,950.00 USD | `-54.26%` | `43,548.00` |
| `Live` | `Long` | `0.1655` | 1,260,000.00 USD | 0.00 USD | 496.50 USD | `-52.54%` | `3,000.00` |
| `Live` | `Long` | `0.1675` | 1,260,000.00 USD | 0.00 USD | 3,350.00 USD | `-51.97%` | `20,000.00` |
| `Live` | `Long` | `0.1685` | 1,260,000.00 USD | 0.00 USD | 1,130.00 USD | `-51.68%` | `6,706.00` |
| `Live` | `Long` | `0.1695` | 1,260,000.00 USD | 0.00 USD | 57,320.00 USD | `-51.39%` | `338,145.00` |
| `Live` | `Long` | `0.1725` | 1,200,000.00 USD | 0.00 USD | 11,100.00 USD | `-50.53%` | `64,322.00` |
| `Live` | `Long` | `0.1735` | 1,190,000.00 USD | 0.00 USD | 210.28 USD | `-50.25%` | `1,212.00` |
| `Live` | `Long` | `0.1745` | 1,190,000.00 USD | 0.00 USD | 1,150.00 USD | `-49.96%` | `6,611.00` |
| `Live` | `Long` | `0.1755` | 1,190,000.00 USD | 0.00 USD | 4,170.00 USD | `-49.67%` | `23,777.00` |
| `Live` | `Long` | `0.1765` | 1,190,000.00 USD | 0.00 USD | 256.98 USD | `-49.39%` | `1,456.00` |
| `Live` | `Long` | `0.1775` | 1,190,000.00 USD | 0.00 USD | 175.37 USD | `-49.10%` | `988.00` |
| `Live` | `Long` | `0.1785` | 1,180,000.00 USD | 0.00 USD | 208.67 USD | `-48.81%` | `1,169.00` |
| `Live` | `Long` | `0.1805` | 1,180,000.00 USD | 0.00 USD | 106.68 USD | `-48.24%` | `591.00` |
| `Live` | `Long` | `0.1845` | 1,180,000.00 USD | 0.00 USD | 1,860.00 USD | `-47.09%` | `10,084.00` |
| `Live` | `Long` | `0.1875` | 1,180,000.00 USD | 0.00 USD | 36,310.00 USD | `-46.23%` | `193,636.00` |
| `Live` | `Long` | `0.1945` | 1,150,000.00 USD | 0.00 USD | 622.98 USD | `-44.22%` | `3,203.00` |
| `Live` | `Long` | `0.1975` | 1,150,000.00 USD | 0.00 USD | 632.00 USD | `-43.36%` | `3,200.00` |
| `Live` | `Long` | `0.2035` | 1,150,000.00 USD | 0.00 USD | 88,390.00 USD | `-41.64%` | `434,330.00` |
| `Live` | `Long` | `0.2145` | 1,060,000.00 USD | 0.00 USD | 418.06 USD | `-38.49%` | `1,949.00` |
| `Live` | `Long` | `0.2175` | 1,060,000.00 USD | 0.00 USD | 1,520.00 USD | `-37.63%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,050,000.00 USD | 0.00 USD | 227.46 USD | `-37.34%` | `1,041.00` |
| `Live` | `Long` | `0.2195` | 1,050,000.00 USD | 0.00 USD | 286.67 USD | `-37.06%` | `1,306.00` |
| `Live` | `Long` | `0.2245` | 1,050,000.00 USD | 0.00 USD | 4,570.00 USD | `-35.62%` | `20,360.00` |
| `Live` | `Long` | `0.2305` | 1,050,000.00 USD | 0.00 USD | 2,360.00 USD | `-33.90%` | `10,255.00` |
| `Live` | `Long` | `0.2315` | 1,050,000.00 USD | 0.00 USD | 122.23 USD | `-33.61%` | `528.00` |
| `Live` | `Long` | `0.2325` | 1,050,000.00 USD | 0.00 USD | 310.39 USD | `-33.33%` | `1,335.00` |
| `Live` | `Long` | `0.2335` | 1,050,000.00 USD | 0.00 USD | 2,120.00 USD | `-33.04%` | `9,077.00` |
| `Live` | `Long` | `0.2345` | 1,040,000.00 USD | 0.00 USD | 6,120.00 USD | `-32.75%` | `26,082.00` |
| `Live` | `Long` | `0.2355` | 1,040,000.00 USD | 0.00 USD | 2,790.00 USD | `-32.47%` | `11,856.00` |
| `Live` | `Long` | `0.2365` | 1,040,000.00 USD | 0.00 USD | 3,160.00 USD | `-32.18%` | `13,382.00` |
| `Live` | `Long` | `0.2375` | 1,030,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.89%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 1,030,000.00 USD | 0.00 USD | 152.00 USD | `-31.03%` | `632.00` |
| `Live` | `Long` | `0.2425` | 1,030,000.00 USD | 0.00 USD | 139.92 USD | `-30.46%` | `577.00` |
| `Live` | `Long` | `0.2445` | 1,030,000.00 USD | 0.00 USD | 1,350.00 USD | `-29.89%` | `5,539.00` |
| `Live` | `Long` | `0.2465` | 1,030,000.00 USD | 0.00 USD | 386.51 USD | `-29.31%` | `1,568.00` |
| `Live` | `Long` | `0.2485` | 1,030,000.00 USD | 0.00 USD | 11,890.00 USD | `-28.74%` | `47,833.00` |
| `Live` | `Long` | `0.2515` | 1,020,000.00 USD | 0.00 USD | 263.07 USD | `-27.88%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 1,020,000.00 USD | 0.00 USD | 299.45 USD | `-26.73%` | `1,172.00` |
| `Live` | `Long` | `0.2565` | 1,020,000.00 USD | 0.00 USD | 1,230.00 USD | `-26.45%` | `4,794.00` |
| `Live` | `Long` | `0.2595` | 1,020,000.00 USD | 0.00 USD | 312.44 USD | `-25.58%` | `1,204.00` |
| `Live` | `Long` | `0.2605` | 1,020,000.00 USD | 0.00 USD | 438.42 USD | `-25.30%` | `1,683.00` |
| `Live` | `Long` | `0.2625` | 1,020,000.00 USD | 0.00 USD | 2,210.00 USD | `-24.72%` | `8,427.00` |
| `Live` | `Long` | `0.2645` | 1,010,000.00 USD | 0.00 USD | 2,210.00 USD | `-24.15%` | `8,340.00` |
| `Live` | `Long` | `0.2655` | 1,010,000.00 USD | 0.00 USD | 449.23 USD | `-23.86%` | `1,692.00` |
| `Live` | `Long` | `0.2665` | 1,010,000.00 USD | 0.00 USD | 27,080.00 USD | `-23.58%` | `101,607.00` |
| `Live` | `Long` | `0.2675` | 983,150.00 USD | 0.00 USD | 321.54 USD | `-23.29%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 982,830.00 USD | 0.00 USD | 3,150.00 USD | `-23.00%` | `11,746.00` |
| `Live` | `Long` | `0.2745` | 979,680.00 USD | 0.00 USD | 3,950.00 USD | `-21.28%` | `14,395.00` |
| `Live` | `Long` | `0.2755` | 975,730.00 USD | 0.00 USD | 80,810.00 USD | `-21.00%` | `293,333.00` |
| `Live` | `Long` | `0.2785` | 894,910.00 USD | 0.00 USD | 189.66 USD | `-20.14%` | `681.00` |
| `Live` | `Long` | `0.2795` | 894,720.00 USD | 0.00 USD | 12,870.00 USD | `-19.85%` | `46,044.00` |
| `Live` | `Long` | `0.2805` | 881,850.00 USD | 0.00 USD | 6,280.00 USD | `-19.56%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 875,580.00 USD | 0.00 USD | 15,620.00 USD | `-19.28%` | `55,479.00` |
| `Live` | `Long` | `0.2825` | 859,960.00 USD | 0.00 USD | 1,420.00 USD | `-18.99%` | `5,038.00` |
| `Live` | `Long` | `0.2845` | 858,540.00 USD | 0.00 USD | 5,720.00 USD | `-18.42%` | `20,120.00` |
| `Live` | `Long` | `0.2855` | 852,810.00 USD | 0.00 USD | 359.16 USD | `-18.13%` | `1,258.00` |
| `Live` | `Long` | `0.2905` | 852,450.00 USD | 0.00 USD | 589.42 USD | `-16.70%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 851,860.00 USD | 0.00 USD | 957.64 USD | `-16.12%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 850,910.00 USD | 0.00 USD | 213.08 USD | `-15.84%` | `726.00` |
| `Live` | `Long` | `0.2945` | 850,690.00 USD | 0.00 USD | 124.87 USD | `-15.55%` | `424.00` |
| `Live` | `Long` | `0.2955` | 850,570.00 USD | 0.00 USD | 468.37 USD | `-15.26%` | `1,585.00` |
| `Live` | `Long` | `0.2965` | 850,100.00 USD | 0.00 USD | 157.14 USD | `-14.97%` | `530.00` |
| `Live` | `Long` | `0.2985` | 849,940.00 USD | 0.00 USD | 127.46 USD | `-14.40%` | `427.00` |
| `Live` | `Long` | `0.2995` | 849,820.00 USD | 0.00 USD | 4,440.00 USD | `-14.11%` | `14,821.00` |
| `Live` | `Long` | `0.3015` | 845,380.00 USD | 0.00 USD | 10,650.00 USD | `-13.54%` | `35,336.00` |
| `Live` | `Long` | `0.3025` | 834,720.00 USD | 0.00 USD | 2,130.00 USD | `-13.25%` | `7,054.00` |
| `Live` | `Long` | `0.3035` | 832,590.00 USD | 0.00 USD | 485.90 USD | `-12.97%` | `1,601.00` |
| `Live` | `Long` | `0.3045` | 832,100.00 USD | 0.00 USD | 267.35 USD | `-12.68%` | `878.00` |
| `Live` | `Long` | `0.3055` | 831,840.00 USD | 0.00 USD | 14,810.00 USD | `-12.39%` | `48,480.00` |
| `Live` | `Long` | `0.3075` | 817,020.00 USD | 0.00 USD | 5,920.00 USD | `-11.82%` | `19,262.00` |
| `Live` | `Long` | `0.3085` | 811,100.00 USD | 0.00 USD | 1,020.00 USD | `-11.53%` | `3,295.00` |
| `Live` | `Long` | `0.3105` | 810,090.00 USD | 0.00 USD | 193.13 USD | `-10.96%` | `622.00` |
| `Live` | `Long` | `0.3115` | 809,890.00 USD | 0.00 USD | 13,740.00 USD | `-10.67%` | `44,115.00` |
| `Live` | `Long` | `0.3125` | 796,150.00 USD | 0.00 USD | 3,130.00 USD | `-10.39%` | `10,032.00` |
| `Live` | `Long` | `0.3135` | 793,020.00 USD | 0.00 USD | 15,080.00 USD | `-10.10%` | `48,117.00` |
| `Live` | `Long` | `0.3145` | 777,930.00 USD | 0.00 USD | 141.84 USD | `-9.81%` | `451.00` |
| `Live` | `Long` | `0.3155` | 777,790.00 USD | 0.00 USD | 3,250.00 USD | `-9.53%` | `10,295.00` |
| `Live` | `Long` | `0.3165` | 774,540.00 USD | 0.00 USD | 935.89 USD | `-9.24%` | `2,957.00` |
| `Live` | `Long` | `0.3225` | 773,600.00 USD | 0.00 USD | 442.15 USD | `-7.52%` | `1,371.00` |
| `Live` | `Long` | `0.3235` | 773,160.00 USD | 0.00 USD | 460.66 USD | `-7.23%` | `1,424.00` |
| `Live` | `Long` | `0.3245` | 772,700.00 USD | 0.00 USD | 128.83 USD | `-6.95%` | `397.00` |
| `Live` | `Long` | `0.3275` | 772,570.00 USD | 0.00 USD | 6,260.00 USD | `-6.09%` | `19,105.00` |
| `Live` | `Long` | `0.3285` | 766,320.00 USD | 0.00 USD | 745,260.00 USD | `-5.80%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 21,050.00 USD | 0.00 USD | 1,650.00 USD | `-5.51%` | `4,998.00` |
| `Live` | `Long` | `0.3315` | 19,410.00 USD | 0.00 USD | 4,780.00 USD | `-4.94%` | `14,420.00` |
| `Live` | `Long` | `0.3325` | 14,630.00 USD | 0.00 USD | 634.08 USD | `-4.65%` | `1,907.00` |
| `Live` | `Long` | `0.3335` | 13,990.00 USD | 0.00 USD | 10,660.00 USD | `-4.36%` | `31,962.00` |
| `Live` | `Long` | `0.3345` | 3,330.00 USD | 0.00 USD | 1,010.00 USD | `-4.08%` | `3,030.00` |
| `Live` | `Long` | `0.3375` | 2,320.00 USD | 0.00 USD | 116.44 USD | `-3.22%` | `345.00` |
| `Live` | `Long` | `0.3385` | 2,200.00 USD | 0.00 USD | 2,200.00 USD | `-2.93%` | `6,507.00` |
| `Live` | `Short` | `0.3635` | 31,410.00 USD | 31,410.00 USD | 0.00 USD | `+4.24%` | `86,423.00` |
| `Live` | `Short` | `0.3645` | 43,810.00 USD | 12,390.00 USD | 0.00 USD | `+4.53%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 44,870.00 USD | 1,060.00 USD | 0.00 USD | `+5.10%` | `2,882.00` |
| `Live` | `Short` | `0.3675` | 45,180.00 USD | 312.74 USD | 0.00 USD | `+5.39%` | `851.00` |
| `Live` | `Short` | `0.3685` | 47,450.00 USD | 2,270.00 USD | 0.00 USD | `+5.67%` | `6,156.00` |
| `Live` | `Short` | `0.3695` | 47,600.00 USD | 151.50 USD | 0.00 USD | `+5.96%` | `410.00` |
| `Live` | `Short` | `0.3715` | 48,580.00 USD | 982.62 USD | 0.00 USD | `+6.53%` | `2,645.00` |
| `Live` | `Short` | `0.3725` | 60,120.00 USD | 11,540.00 USD | 0.00 USD | `+6.82%` | `30,983.00` |
| `Live` | `Short` | `0.3735` | 104,870.00 USD | 44,750.00 USD | 0.00 USD | `+7.11%` | `119,811.00` |
| `Live` | `Short` | `0.3755` | 110,990.00 USD | 6,120.00 USD | 0.00 USD | `+7.68%` | `16,287.00` |
| `Live` | `Short` | `0.3775` | 143,290.00 USD | 32,300.00 USD | 0.00 USD | `+8.25%` | `85,568.00` |
| `Live` | `Short` | `0.3785` | 699,990.00 USD | 556,700.00 USD | 0.00 USD | `+8.54%` | `1,470,802.00` |
| `Live` | `Short` | `0.3825` | 704,840.00 USD | 4,850.00 USD | 0.00 USD | `+9.69%` | `12,674.00` |
| `Live` | `Short` | `0.3835` | 739,010.00 USD | 34,170.00 USD | 0.00 USD | `+9.97%` | `89,108.00` |
| `Live` | `Short` | `0.3855` | 739,130.00 USD | 120.28 USD | 0.00 USD | `+10.55%` | `312.00` |
| `Live` | `Short` | `0.3875` | 744,600.00 USD | 5,470.00 USD | 0.00 USD | `+11.12%` | `14,129.00` |
| `Live` | `Short` | `0.3895` | 748,260.00 USD | 3,660.00 USD | 0.00 USD | `+11.69%` | `9,400.00` |
| `Live` | `Short` | `0.3905` | 750,060.00 USD | 1,800.00 USD | 0.00 USD | `+11.98%` | `4,601.00` |
| `Live` | `Short` | `0.3915` | 750,550.00 USD | 487.42 USD | 0.00 USD | `+12.27%` | `1,245.00` |
| `Live` | `Short` | `0.3925` | 817,780.00 USD | 67,230.00 USD | 0.00 USD | `+12.55%` | `171,288.00` |
| `Live` | `Short` | `0.3935` | 819,260.00 USD | 1,480.00 USD | 0.00 USD | `+12.84%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 985,980.00 USD | 166,720.00 USD | 0.00 USD | `+13.13%` | `422,615.00` |
| `Live` | `Short` | `0.3965` | 987,570.00 USD | 1,580.00 USD | 0.00 USD | `+13.70%` | `3,992.00` |
| `Live` | `Short` | `0.4015` | 987,860.00 USD | 290.69 USD | 0.00 USD | `+15.14%` | `724.00` |
| `Live` | `Short` | `0.4085` | 990,070.00 USD | 2,210.00 USD | 0.00 USD | `+17.14%` | `5,417.00` |
| `Live` | `Short` | `0.4095` | 990,310.00 USD | 239.56 USD | 0.00 USD | `+17.43%` | `585.00` |
| `Live` | `Short` | `0.4165` | 991,040.00 USD | 730.12 USD | 0.00 USD | `+19.44%` | `1,753.00` |
| `Live` | `Short` | `0.4195` | 992,040.00 USD | 1,000.00 USD | 0.00 USD | `+20.30%` | `2,387.00` |
| `Live` | `Short` | `0.4235` | 1,000,000.00 USD | 11,900.00 USD | 0.00 USD | `+21.44%` | `28,092.00` |
| `Live` | `Short` | `0.4275` | 1,000,000.00 USD | 201.78 USD | 0.00 USD | `+22.59%` | `472.00` |
| `Live` | `Short` | `0.4285` | 1,010,000.00 USD | 10,190.00 USD | 0.00 USD | `+22.88%` | `23,779.00` |
| `Live` | `Short` | `0.4335` | 1,020,000.00 USD | 1,500.00 USD | 0.00 USD | `+24.31%` | `3,464.00` |
| `Live` | `Short` | `0.4365` | 1,090,000.00 USD | 71,050.00 USD | 0.00 USD | `+25.17%` | `162,775.00` |
| `Live` | `Short` | `0.4425` | 1,090,000.00 USD | 378.34 USD | 0.00 USD | `+26.89%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,090,000.00 USD | 421.00 USD | 0.00 USD | `+27.75%` | `945.00` |
| `Live` | `Short` | `0.4465` | 1,110,000.00 USD | 23,340.00 USD | 0.00 USD | `+28.04%` | `52,284.00` |
| `Live` | `Short` | `0.4485` | 1,180,000.00 USD | 65,760.00 USD | 0.00 USD | `+28.61%` | `146,614.00` |
| `Live` | `Short` | `0.4505` | 1,760,000.00 USD | 585,650.00 USD | 0.00 USD | `+29.19%` | `1,300,000.00` |
| `Live` | `Short` | `0.4515` | 1,760,000.00 USD | 318.76 USD | 0.00 USD | `+29.47%` | `706.00` |
| `Live` | `Short` | `0.4525` | 1,770,000.00 USD | 5,560.00 USD | 0.00 USD | `+29.76%` | `12,284.00` |
| `Live` | `Short` | `0.4535` | 1,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+30.05%` | `2,519.00` |
| `Live` | `Short` | `0.4545` | 1,770,000.00 USD | 1,550.00 USD | 0.00 USD | `+30.33%` | `3,416.00` |
| `Live` | `Short` | `0.4705` | 2,050,000.00 USD | 282,390.00 USD | 0.00 USD | `+34.92%` | `600,198.00` |
| `Live` | `Short` | `0.4735` | 2,060,000.00 USD | 8,060.00 USD | 0.00 USD | `+35.78%` | `17,027.00` |
| `Live` | `Short` | `0.4845` | 2,080,000.00 USD | 20,330.00 USD | 0.00 USD | `+38.94%` | `41,969.00` |
| `Live` | `Short` | `0.4895` | 2,080,000.00 USD | 839.49 USD | 0.00 USD | `+40.37%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,090,000.00 USD | 5,120.00 USD | 0.00 USD | `+40.66%` | `10,430.00` |
| `Live` | `Short` | `0.4925` | 2,090,000.00 USD | 284.67 USD | 0.00 USD | `+41.23%` | `578.00` |
| `Live` | `Short` | `0.4985` | 2,860,000.00 USD | 771,520.00 USD | 0.00 USD | `+42.95%` | `1,547,681.00` |
| `Live` | `Short` | `0.4995` | 2,860,000.00 USD | 2,730.00 USD | 0.00 USD | `+43.24%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 2,890,000.00 USD | 23,600.00 USD | 0.00 USD | `+43.81%` | `47,061.00` |
| `Live` | `Short` | `0.5325` | 2,890,000.00 USD | 945.72 USD | 0.00 USD | `+52.70%` | `1,776.00` |
| `Live` | `Short` | `0.5335` | 2,890,000.00 USD | 668.48 USD | 0.00 USD | `+52.99%` | `1,253.00` |
| `Live` | `Short` | `0.5545` | 2,930,000.00 USD | 41,030.00 USD | 0.00 USD | `+59.01%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,930,000.00 USD | 740.92 USD | 0.00 USD | `+59.87%` | `1,329.00` |
| `Live` | `Short` | `0.5595` | 2,940,000.00 USD | 15,070.00 USD | 0.00 USD | `+60.44%` | `26,926.00` |
| `Live` | `Short` | `0.5615` | 2,940,000.00 USD | 140.38 USD | 0.00 USD | `+61.02%` | `250.00` |
| `Live` | `Short` | `0.5635` | 3,000,000.00 USD | 54,010.00 USD | 0.00 USD | `+61.59%` | `95,846.00` |
| `Live` | `Short` | `0.5705` | 3,740,000.00 USD | 740,080.00 USD | 0.00 USD | `+63.60%` | `1,297,248.00` |
| `Live` | `Short` | `0.5935` | 3,750,000.00 USD | 8,020.00 USD | 0.00 USD | `+70.19%` | `13,510.00` |
| `Live` | `Short` | `0.6155` | 3,780,000.00 USD | 28,550.00 USD | 0.00 USD | `+76.50%` | `46,380.00` |
| `Live` | `Short` | `0.6245` | 3,810,000.00 USD | 32,830.00 USD | 0.00 USD | `+79.08%` | `52,566.00` |
| `Live` | `Short` | `0.6265` | 3,810,000.00 USD | 379.03 USD | 0.00 USD | `+79.66%` | `605.00` |
| `Live` | `Short` | `0.6285` | 3,810,000.00 USD | 1,140.00 USD | 0.00 USD | `+80.23%` | `1,808.00` |
| `Live` | `Short` | `0.6345` | 3,860,000.00 USD | 48,630.00 USD | 0.00 USD | `+81.95%` | `76,641.00` |
| `Live` | `Short` | `0.6515` | 3,860,000.00 USD | 951.19 USD | 0.00 USD | `+86.83%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 3,860,000.00 USD | 705.13 USD | 0.00 USD | `+87.40%` | `1,079.00` |
| `Live` | `Short` | `0.6555` | 3,860,000.00 USD | 1,080.00 USD | 0.00 USD | `+87.97%` | `1,642.00` |
| `Live` | `Short` | `0.6625` | 3,860,000.00 USD | 2,060.00 USD | 0.00 USD | `+89.98%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,870,000.00 USD | 2,530.00 USD | 0.00 USD | `+90.27%` | `3,811.00` |
| `Live` | `Short` | `0.6645` | 3,870,000.00 USD | 1,210.00 USD | 0.00 USD | `+90.55%` | `1,821.00` |
| `Live` | `Short` | `0.6665` | 3,880,000.00 USD | 16,500.00 USD | 0.00 USD | `+91.13%` | `24,756.00` |
| `Live` | `Short` | `0.6695` | 3,970,000.00 USD | 85,440.00 USD | 0.00 USD | `+91.99%` | `127,625.00` |
| `Live` | `Short` | `0.6735` | 4,050,000.00 USD | 83,060.00 USD | 0.00 USD | `+93.13%` | `123,332.00` |
| `Live` | `Short` | `0.6865` | 4,820,000.00 USD | 769,680.00 USD | 0.00 USD | `+96.86%` | `1,121,171.00` |
| `Live` | `Short` | `0.6875` | 4,820,000.00 USD | 262.62 USD | 0.00 USD | `+97.15%` | `382.00` |
| `Live` | `Short` | `0.6885` | 4,820,000.00 USD | 846.86 USD | 0.00 USD | `+97.44%` | `1,230.00` |
| `Live` | `Short` | `0.6925` | 4,820,000.00 USD | 414.12 USD | 0.00 USD | `+98.58%` | `598.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 957,650.00 USD | 0.00 USD | 198.45 USD | `-72.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 957,450.00 USD | 0.00 USD | 330.26 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 957,120.00 USD | 0.00 USD | 6,100.00 USD | `-48.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 951,020.00 USD | 0.00 USD | 1,750.00 USD | `-41.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 949,270.00 USD | 0.00 USD | 2,220.00 USD | `-39.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 947,050.00 USD | 0.00 USD | 121.70 USD | `-33.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 946,930.00 USD | 0.00 USD | 705.61 USD | `-32.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 946,230.00 USD | 0.00 USD | 159.20 USD | `-32.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 946,070.00 USD | 0.00 USD | 1,200.00 USD | `-31.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 944,870.00 USD | 0.00 USD | 127.51 USD | `-30.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 944,740.00 USD | 0.00 USD | 1,850.00 USD | `-28.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 942,880.00 USD | 0.00 USD | 41,500.00 USD | `-27.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 901,390.00 USD | 0.00 USD | 1,920.00 USD | `-26.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 899,460.00 USD | 0.00 USD | 664.01 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 898,800.00 USD | 0.00 USD | 954.98 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 897,840.00 USD | 0.00 USD | 103.56 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 897,740.00 USD | 0.00 USD | 695.50 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 897,040.00 USD | 0.00 USD | 1,630.00 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 895,420.00 USD | 0.00 USD | 1,470.00 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 893,940.00 USD | 0.00 USD | 101.94 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 893,840.00 USD | 0.00 USD | 3,260.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 890,580.00 USD | 0.00 USD | 2,550.00 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 888,030.00 USD | 0.00 USD | 229.92 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 887,800.00 USD | 0.00 USD | 8,010.00 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 879,790.00 USD | 0.00 USD | 11,610.00 USD | `-15.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 868,180.00 USD | 0.00 USD | 111.19 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 868,070.00 USD | 0.00 USD | 326.86 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 867,750.00 USD | 0.00 USD | 2,710.00 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 865,040.00 USD | 0.00 USD | 335.56 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 864,700.00 USD | 0.00 USD | 919.50 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 863,780.00 USD | 0.00 USD | 193.11 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 863,590.00 USD | 0.00 USD | 15,150.00 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 848,440.00 USD | 0.00 USD | 147.32 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 848,290.00 USD | 0.00 USD | 12,200.00 USD | `-10.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 836,090.00 USD | 0.00 USD | 6,530.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 829,560.00 USD | 0.00 USD | 524,570.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 304,990.00 USD | 0.00 USD | 1,270.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 303,720.00 USD | 0.00 USD | 53,690.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 250,030.00 USD | 0.00 USD | 1,920.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 248,120.00 USD | 0.00 USD | 6,100.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 242,020.00 USD | 0.00 USD | 850.90 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 241,170.00 USD | 0.00 USD | 1,040.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 240,130.00 USD | 0.00 USD | 6,220.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 233,900.00 USD | 0.00 USD | 10,000.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 223,910.00 USD | 0.00 USD | 43,570.00 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 180,340.00 USD | 0.00 USD | 131.90 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 180,210.00 USD | 0.00 USD | 4,710.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 175,490.00 USD | 0.00 USD | 3,220.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 172,280.00 USD | 0.00 USD | 64,780.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 107,500.00 USD | 0.00 USD | 6,130.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 101,360.00 USD | 0.00 USD | 6,770.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 94,600.00 USD | 0.00 USD | 996.01 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 93,600.00 USD | 0.00 USD | 2,100.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 91,500.00 USD | 0.00 USD | 949.53 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 90,550.00 USD | 0.00 USD | 100.11 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 90,450.00 USD | 0.00 USD | 135.99 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 90,310.00 USD | 0.00 USD | 1,010.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 89,300.00 USD | 0.00 USD | 5,640.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 83,670.00 USD | 0.00 USD | 936.05 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 82,730.00 USD | 0.00 USD | 34,710.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 48,020.00 USD | 0.00 USD | 32,490.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 15,530.00 USD | 0.00 USD | 157.74 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 15,370.00 USD | 0.00 USD | 3,380.00 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 12,000.00 USD | 0.00 USD | 1,400.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 10,590.00 USD | 0.00 USD | 486.30 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 10,110.00 USD | 0.00 USD | 359.28 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 9,750.00 USD | 0.00 USD | 828.18 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 8,920.00 USD | 0.00 USD | 1,950.00 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 6,970.00 USD | 0.00 USD | 3,980.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 3,000.00 USD | 0.00 USD | 555.44 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 2,440.00 USD | 0.00 USD | 1,280.00 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3485` | 1,160.00 USD | 0.00 USD | 1,160.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 1,570.00 USD | 1,570.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 4,000.00 USD | 2,430.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 4,920.00 USD | 919.52 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 5,240.00 USD | 311.26 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 5,550.00 USD | 312.14 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 5,700.00 USD | 157.04 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 8,280.00 USD | 2,580.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 47,710.00 USD | 39,430.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 88,100.00 USD | 40,390.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 91,410.00 USD | 3,310.00 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 92,440.00 USD | 1,030.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 95,380.00 USD | 2,940.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 95,610.00 USD | 224.49 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 95,710.00 USD | 103.23 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 99,030.00 USD | 3,320.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 141,600.00 USD | 42,570.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 152,770.00 USD | 11,170.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 162,040.00 USD | 9,270.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 162,260.00 USD | 218.89 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 176,590.00 USD | 14,330.00 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 181,660.00 USD | 5,070.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 181,830.00 USD | 174.60 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 181,940.00 USD | 107.28 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 182,380.00 USD | 439.61 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 182,820.00 USD | 437.79 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 184,440.00 USD | 1,620.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 184,620.00 USD | 182.60 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 191,070.00 USD | 6,450.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 191,350.00 USD | 275.17 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 191,920.00 USD | 569.25 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 197,890.00 USD | 5,980.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 198,150.00 USD | 257.89 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 199,110.00 USD | 963.52 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 199,340.00 USD | 224.73 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 201,130.00 USD | 1,790.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 201,830.00 USD | 702.27 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 202,940.00 USD | 1,110.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 203,120.00 USD | 181.04 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 203,480.00 USD | 352.11 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 203,630.00 USD | 155.03 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 203,910.00 USD | 276.40 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 204,030.00 USD | 126.24 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 206,440.00 USD | 2,400.00 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 207,450.00 USD | 1,010.00 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 209,460.00 USD | 2,010.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 280,950.00 USD | 71,490.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 281,810.00 USD | 864.28 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 285,730.00 USD | 3,920.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 365,060.00 USD | 79,330.00 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 366,260.00 USD | 1,200.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 367,460.00 USD | 1,200.00 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 367,600.00 USD | 138.07 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 368,870.00 USD | 1,270.00 USD | 0.00 USD | `+17.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 369,200.00 USD | 331.63 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 369,520.00 USD | 313.54 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 369,700.00 USD | 186.70 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 370,030.00 USD | 325.75 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 370,210.00 USD | 183.82 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 370,510.00 USD | 299.19 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 409,090.00 USD | 38,580.00 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 409,260.00 USD | 170.69 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 409,390.00 USD | 135.59 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 410,780.00 USD | 1,390.00 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 416,120.00 USD | 5,340.00 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 417,600.00 USD | 1,470.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 498,360.00 USD | 80,770.00 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 498,530.00 USD | 169.22 USD | 0.00 USD | `+40.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 498,690.00 USD | 153.79 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 499,410.00 USD | 724.89 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 510,560.00 USD | 11,150.00 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 512,490.00 USD | 1,930.00 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 512,630.00 USD | 135.02 USD | 0.00 USD | `+51.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 512,870.00 USD | 240.85 USD | 0.00 USD | `+80.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 513,960.00 USD | 1,100.00 USD | 0.00 USD | `+81.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 527,570.00 USD | 13,610.00 USD | 0.00 USD | `+94.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 529,410.00 USD | 1,840.00 USD | 0.00 USD | `+94.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 530,410.00 USD | 991.76 USD | 0.00 USD | `+96.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 531,530.00 USD | 1,130.00 USD | 0.00 USD | `+96.58%` | `TACTICAL (Retail Cluster)` |

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
| `7D` | `0.3061` | 24,390,000.00 USD | 0.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `7D` | `0.3067` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3073` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 24,300,000.00 USD | 0.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `7D` | `0.3085` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3094` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 24,190,000.00 USD | 0.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3099` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3103` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3104` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3109` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3114` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD |
| `7D` | `0.3115` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3119` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 23,970.00 USD | 10,650.00 USD | 35,060.00 USD |
| `7D` | `0.3121` | 23,990,000.00 USD | 0.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3124` | 20,380,000.00 USD | 0.00 USD | 20,380,000.00 USD | 12,740.00 USD | 3,560.00 USD | 16,390.00 USD |
| `7D` | `0.3127` | 23,810,000.00 USD | 0.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3129` | 20,350,000.00 USD | 0.00 USD | 20,350,000.00 USD | 126.90 USD | 38,440.00 USD | 29,100.00 USD |
| `7D` | `0.3133` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3134` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 0.00 USD | 23,940.00 USD | 9,590.00 USD |
| `1D` | `0.3139` | 20,250,000.00 USD | 0.00 USD | 20,250,000.00 USD | 952.52 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3144` | 20,240,000.00 USD | 0.00 USD | 20,240,000.00 USD | 911.00 USD | 5,900.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3149` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 297.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 23,360,000.00 USD | 0.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3154` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD |
| `7D` | `0.3157` | 23,110,000.00 USD | 0.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3159` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3163` | 22,560,000.00 USD | 0.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3164` | 20,150,000.00 USD | 0.00 USD | 20,150,000.00 USD | 43,210.00 USD | 33,960.00 USD | 0.00 USD |
| `1D` | `0.3169` | 20,070,000.00 USD | 0.00 USD | 20,070,000.00 USD | 1,090.00 USD | 10,820.00 USD | 29,770.00 USD |
| `7D` | `0.3169` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD |
| `1D` | `0.3174` | 20,030,000.00 USD | 0.00 USD | 20,030,000.00 USD | 22,580.00 USD | 37,950.00 USD | 36,960.00 USD |
| `7D` | `0.3175` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD |
| `1D` | `0.3179` | 19,940,000.00 USD | 0.00 USD | 19,940,000.00 USD | 67,160.00 USD | 27,250.00 USD | 48,510.00 USD |
| `7D` | `0.3181` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3184` | 19,790,000.00 USD | 0.00 USD | 19,790,000.00 USD | 467,780.00 USD | 71,300.00 USD | 101,250.00 USD |
| `7D` | `0.3187` | 19,600,000.00 USD | 0.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3189` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 27,640.00 USD | 30,250.00 USD | 43,240.00 USD |
| `7D` | `0.3193` | 19,130,000.00 USD | 0.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3194` | 19,050,000.00 USD | 0.00 USD | 19,050,000.00 USD | 74,930.00 USD | 3,120.00 USD | 20,860.00 USD |
| `1D` | `0.3199` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 54,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3204` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 236,500.00 USD | 30,500.00 USD | 34,330.00 USD |
| `7D` | `0.3205` | 18,830,000.00 USD | 0.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3209` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 103,890.00 USD | 11,980.00 USD | 63,020.00 USD |
| `7D` | `0.3211` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3214` | 18,420,000.00 USD | 0.00 USD | 18,420,000.00 USD | 914.92 USD | 34,400.00 USD | 90,380.00 USD |
| `7D` | `0.3217` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3219` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 5,550.00 USD | 3,820.00 USD | 143,060.00 USD |
| `7D` | `0.3223` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3224` | 18,140,000.00 USD | 0.00 USD | 18,140,000.00 USD | 132,310.00 USD | 13,780.00 USD | 182,490.00 USD |
| `1D` | `0.3229` | 17,810,000.00 USD | 0.00 USD | 17,810,000.00 USD | 7,860.00 USD | 46,020.00 USD | 106,810.00 USD |
| `7D` | `0.3229` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD |
| `1D` | `0.3234` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 62,890.00 USD | 42,740.00 USD | 46,110.00 USD |
| `7D` | `0.3235` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD |
| `1D` | `0.3239` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 0.00 USD | 45,410.00 USD | 157,160.00 USD |
| `7D` | `0.3241` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD |
| `1D` | `0.3244` | 17,290,000.00 USD | 0.00 USD | 17,290,000.00 USD | 160,140.00 USD | 51,630.00 USD | 193,690.00 USD |
| `7D` | `0.3247` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3249` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 1,070,000.00 USD | 137,210.00 USD | 226,730.00 USD |
| `7D` | `0.3253` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3254` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 296,640.00 USD | 75,320.00 USD | 424,410.00 USD |
| `1D` | `0.3259` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 0.00 USD | 42,480.00 USD | 94,360.00 USD |
| `7D` | `0.3259` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3264` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `7D` | `0.3265` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3269` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 124,870.00 USD | 64,710.00 USD | 369,110.00 USD |
| `7D` | `0.3271` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3274` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 194,040.00 USD | 26,070.00 USD | 80,450.00 USD |
| `1D` | `0.3279` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 57,970.00 USD | 39,150.00 USD | 115,660.00 USD |
| `7D` | `0.3283` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3289` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3294` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `7D` | `0.3301` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3304` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3307` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3309` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 306,740.00 USD | 39,540.00 USD | 338,680.00 USD |
| `7D` | `0.3313` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3314` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 39,300.00 USD | 117,000.00 USD | 77,680.00 USD |
| `1D` | `0.3319` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 159,340.00 USD | 54,860.00 USD | 295,390.00 USD |
| `7D` | `0.3319` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3324` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 137,370.00 USD | 95,620.00 USD | 232,770.00 USD |
| `7D` | `0.3325` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD |
| `1D` | `0.3329` | 11,240,000.00 USD | 0.00 USD | 11,240,000.00 USD | 30,990.00 USD | 11,620.00 USD | 97,640.00 USD |
| `7D` | `0.3331` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD |
| `1D` | `0.3334` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 38,930.00 USD | 41,320.00 USD | 359,940.00 USD |
| `7D` | `0.3337` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD |
| `1D` | `0.3339` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 223,020.00 USD | 219,400.00 USD | 232,260.00 USD |
| `7D` | `0.3343` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD |
| `1D` | `0.3344` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 11,850.00 USD | 75,820.00 USD | 23,980.00 USD |
| `1D` | `0.3349` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 266,880.00 USD | 37,190.00 USD | 83,680.00 USD |
| `7D` | `0.3349` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3354` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 1,300.00 USD | 14,760.00 USD | 13,900.00 USD |
| `7D` | `0.3355` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD |
| `1D` | `0.3359` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 268,370.00 USD | 25,890.00 USD | 65,250.00 USD |
| `7D` | `0.3361` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3364` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 148,220.00 USD | 64,000.00 USD | 0.00 USD |
| `7D` | `0.3367` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3369` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 110,520.00 USD | 29,430.00 USD | 40,590.00 USD |
| `7D` | `0.3373` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3374` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 330,500.00 USD | 107,280.00 USD | 17,230.00 USD |
| `1D` | `0.3379` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 268,220.00 USD | 75,530.00 USD | 16,800.00 USD |
| `7D` | `0.3379` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3384` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 249,030.00 USD | 70,580.00 USD | 49,800.00 USD |
| `7D` | `0.3385` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD |
| `1D` | `0.3389` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 41,890.00 USD | 100,380.00 USD | 59,530.00 USD |
| `7D` | `0.3391` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3394` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 102,390.00 USD | 93,730.00 USD | 198,790.00 USD |
| `7D` | `0.3397` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD |
| `1D` | `0.3399` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 81,980.00 USD | 130,600.00 USD | 320,620.00 USD |
| `7D` | `0.3403` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD |
| `1D` | `0.3404` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 187,960.00 USD | 65,630.00 USD | 223,250.00 USD |
| `1D` | `0.3409` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 79,910.00 USD | 243,360.00 USD | 23,760.00 USD |
| `7D` | `0.3409` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD |
| `1D` | `0.3414` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 415,020.00 USD | 175,790.00 USD | 110,640.00 USD |
| `7D` | `0.3415` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD |
| `1D` | `0.3419` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 808,300.00 USD | 66,220.00 USD | 252,220.00 USD |
| `1D` | `0.3424` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 109,050.00 USD | 68,870.00 USD | 101,870.00 USD |
| `7D` | `0.3427` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD |
| `1D` | `0.3429` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 255,980.00 USD | 167,970.00 USD | 381,820.00 USD |
| `1D` | `0.3434` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 119,040.00 USD | 149,150.00 USD | 77,610.00 USD |
| `1D` | `0.3439` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 113,850.00 USD | 49,600.00 USD | 556,470.00 USD |
| `7D` | `0.3439` | 733,270.00 USD | 0.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3444` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 15,020.00 USD | 39,960.00 USD | 286,890.00 USD |
| `1D` | `0.3449` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 197,010.00 USD | 81,000.00 USD | 34,470.00 USD |
| `7D` | `0.3451` | 538,440.00 USD | 0.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3454` | 934,550.00 USD | 0.00 USD | 934,550.00 USD | 78,780.00 USD | 5,390.00 USD | 535,880.00 USD |
| `1D` | `0.3459` | 314,490.00 USD | 0.00 USD | 314,490.00 USD | 0.00 USD | 0.00 USD | 314,490.00 USD |
| `7D` | `0.3472` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 47,530.00 USD | 47,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47,530.00 USD |
| `1D` | `0.3499` | 423,180.00 USD | 423,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 375,650.00 USD |
| `1D` | `0.3504` | 458,460.00 USD | 458,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,280.00 USD |
| `7D` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 529,330.00 USD | 529,330.00 USD | 0.00 USD | 25,310.00 USD | 45,560.00 USD | 0.00 USD |
| `1D` | `0.3534` | 877,740.00 USD | 877,740.00 USD | 0.00 USD | 119,840.00 USD | 53,270.00 USD | 175,310.00 USD |
| `7D` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3539` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 53,400.00 USD | 17,980.00 USD | 108,070.00 USD |
| `7D` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD |
| `1D` | `0.3544` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 21,880.00 USD | 83,750.00 USD | 37,920.00 USD |
| `7D` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3549` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 50,840.00 USD | 0.00 USD |
| `7D` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD |
| `1D` | `0.3554` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 20,180.00 USD | 40,120.00 USD | 47,950.00 USD |
| `1D` | `0.3559` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 21,340.00 USD | 47,720.00 USD |
| `1D` | `0.3564` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 29,510.00 USD | 27,800.00 USD |
| `7D` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3569` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD |
| `1D` | `0.3574` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 95,510.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `0.3579` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 29,500.00 USD | 9,130.00 USD | 27,240.00 USD |
| `1D` | `0.3584` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 1,810.00 USD | 14,930.00 USD | 0.00 USD |
| `1D` | `0.3589` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3594` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 109,010.00 USD | 0.00 USD | 133,180.00 USD |
| `7D` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3599` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 45,090.00 USD | 22,780.00 USD | 108,510.00 USD |
| `7D` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3604` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 59,920.00 USD | 59,060.00 USD | 136,200.00 USD |
| `7D` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3609` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 75,090.00 USD | 25,740.00 USD | 146,820.00 USD |
| `7D` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3614` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 10,940.00 USD | 59,640.00 USD | 203,600.00 USD |
| `1D` | `0.3619` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 368,360.00 USD | 116,660.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD |
| `1D` | `0.3624` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 98,860.00 USD | 52,010.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3629` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 1,120,000.00 USD | 42,520.00 USD | 79,610.00 USD |
| `7D` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3634` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD |
| `7D` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3639` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 183,690.00 USD | 195,330.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3644` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 294,060.00 USD | 93,250.00 USD | 35,280.00 USD |
| `1D` | `0.3649` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 133,400.00 USD | 59,680.00 USD | 195,820.00 USD |
| `7D` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3654` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 355,110.00 USD | 47,350.00 USD | 165,330.00 USD |
| `7D` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3659` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 220,710.00 USD | 153,150.00 USD | 156,950.00 USD |
| `7D` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3664` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 556,330.00 USD | 70,580.00 USD | 66,590.00 USD |
| `7D` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD |
| `1D` | `0.3669` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 153,920.00 USD | 51,490.00 USD | 266,750.00 USD |
| `7D` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3674` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 41,260.00 USD | 118,940.00 USD | 166,940.00 USD |
| `1D` | `0.3679` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 765,190.00 USD | 29,030.00 USD | 164,260.00 USD |
| `7D` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3684` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 1,290.00 USD | 84,510.00 USD | 177,710.00 USD |
| `7D` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3689` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 715,890.00 USD | 191,500.00 USD | 52,150.00 USD |
| `7D` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD |
| `1D` | `0.3694` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 225,120.00 USD | 65,630.00 USD | 23,760.00 USD |
| `7D` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD |
| `1D` | `0.3699` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 472,310.00 USD | 31,900.00 USD | 27,870.00 USD |
| `1D` | `0.3704` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 285,800.00 USD | 180,250.00 USD | 554,730.00 USD |
| `1D` | `0.3709` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 110,350.00 USD | 21,340.00 USD | 0.00 USD |
| `7D` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3714` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 489,730.00 USD | 134,200.00 USD | 821,910.00 USD |
| `7D` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3719` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 35,660.00 USD | 200,240.00 USD | 245,400.00 USD |
| `7D` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3724` | 16,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 471,540.00 USD | 46,950.00 USD | 398,860.00 USD |
| `7D` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3729` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 67,760.00 USD | 135,260.00 USD | 492,340.00 USD |
| `7D` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3734` | 17,690,000.00 USD | 17,690,000.00 USD | 0.00 USD | 76,800.00 USD | 21,010.00 USD | 655,100.00 USD |
| `1D` | `0.3739` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 154,860.00 USD | 163,770.00 USD | 266,490.00 USD |
| `7D` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3744` | 18,620,000.00 USD | 18,620,000.00 USD | 0.00 USD | 63,330.00 USD | 33,910.00 USD | 239,560.00 USD |
| `7D` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3749` | 19,580,000.00 USD | 19,580,000.00 USD | 0.00 USD | 229,090.00 USD | 12,530.00 USD | 724,070.00 USD |
| `1D` | `0.3754` | 19,730,000.00 USD | 19,730,000.00 USD | 0.00 USD | 134,010.00 USD | 0.00 USD | 18,250.00 USD |
| `7D` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3759` | 20,930,000.00 USD | 20,930,000.00 USD | 0.00 USD | 188,010.00 USD | 70,910.00 USD | 934,830.00 USD |
| `7D` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3764` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 140,690.00 USD | 24,840.00 USD | 159,850.00 USD |
| `1D` | `0.3769` | 21,310,000.00 USD | 21,310,000.00 USD | 0.00 USD | 19,360.00 USD | 32,810.00 USD | 0.00 USD |
| `7D` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3774` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3779` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 230,890.00 USD |
| `7D` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3784` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 222,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3789` | 22,210,000.00 USD | 22,210,000.00 USD | 0.00 USD | 644.45 USD | 80,630.00 USD | 289,160.00 USD |
| `7D` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3794` | 22,320,000.00 USD | 22,320,000.00 USD | 0.00 USD | 54,830.00 USD | 15,820.00 USD | 46,470.00 USD |
| `1D` | `0.3799` | 22,320,000.00 USD | 22,320,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3804` | 22,660,000.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 4,980.00 USD | 334,230.00 USD |
| `7D` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3809` | 22,710,000.00 USD | 22,710,000.00 USD | 0.00 USD | 13,270.00 USD | 12,220.00 USD | 17,620.00 USD |
| `7D` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3814` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3819` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 11,830.00 USD | 13,530.00 USD | 0.00 USD |
| `7D` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3824` | 23,050,000.00 USD | 23,050,000.00 USD | 0.00 USD | 1,760.00 USD | 25,950.00 USD | 246,850.00 USD |
| `1D` | `0.3829` | 23,090,000.00 USD | 23,090,000.00 USD | 0.00 USD | 896.63 USD | 26,460.00 USD | 9,590.00 USD |
| `1D` | `0.3834` | 23,310,000.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 10,610.00 USD | 210,280.00 USD |
| `1D` | `0.3839` | 23,320,000.00 USD | 23,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3844` | 23,330,000.00 USD | 23,330,000.00 USD | 0.00 USD | 1,750.00 USD | 5,900.00 USD | 0.00 USD |
| `1D` | `0.3854` | 23,370,000.00 USD | 23,370,000.00 USD | 0.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.3859` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3864` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD |
| `7D` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `1D` | `0.3869` | 23,470,000.00 USD | 23,470,000.00 USD | 0.00 USD | 43,210.00 USD | 28,780.00 USD | 0.00 USD |
| `1D` | `0.3874` | 23,520,000.00 USD | 23,520,000.00 USD | 0.00 USD | 5,630.00 USD | 31,380.00 USD | 6,720.00 USD |
| `7D` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3879` | 23,550,000.00 USD | 23,550,000.00 USD | 0.00 USD | 15,630.00 USD | 0.00 USD | 16,660.00 USD |
| `7D` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `1D` | `0.3884` | 23,580,000.00 USD | 23,580,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 27,850.00 USD |
| `1D` | `0.3889` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 11,790.00 USD | 11,950.00 USD |
| `7D` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3894` | 23,670,000.00 USD | 23,670,000.00 USD | 0.00 USD | 9,680.00 USD | 33,600.00 USD | 27,870.00 USD |
| `7D` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `1D` | `0.3899` | 23,690,000.00 USD | 23,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,860.00 USD |
| `7D` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3904` | 23,770,000.00 USD | 23,770,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `1D` | `0.3909` | 23,820,000.00 USD | 23,820,000.00 USD | 0.00 USD | 54,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3914` | 24,020,000.00 USD | 24,020,000.00 USD | 0.00 USD | 182,380.00 USD | 6,370.00 USD | 11,150.00 USD |
| `1D` | `0.3915` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 0.00 USD | 11,580.00 USD | 0.00 USD |
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
  * Total Open Interest: `425.95M` | Total OI Tokens: `1,224,831,794.4 TRX`
  * 1h OI Change: `+1.26%` | 4h OI Change: `+4.96%` | 24h OI Change: `+48.27%`
  * Exchange Breakdown: Binance=`113.45M` | Bybit=`85.80M` | OKX=`25.97M` | Hyperliquid=`18.86M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-384.00K` | Last 24h: `-591.57K` | Last 3d: `-625.17K` | Last 7d: `-857.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.1937%` | **USDT OKX** | `-0.5005%` |
| **USDT Bybit** | `-0.0513%` | **USDT KuCoin** | `-0.0205%` |
| **USDT MEXC** | `-0.1959%` | **USDT BingX** | `-0.4902%` |
| **USDT Gate** | `-0.1188%` | **USDT Bitget** | `-0.2829%` |
| **CoinM Binance** | `-0.3620%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `52.90%` | `47.10%` | `1.12` | 4,960,000.00 USD |
| `15M` | `Binance` | `55.89%` | `44.11%` | `1.27` | 2,310,000.00 USD |
| `15M` | `OKX` | `40.14%` | `59.86%` | `0.67` | 823,660.00 USD |
| `15M` | `Bybit` | `56.57%` | `43.43%` | `1.30` | 848,370.00 USD |
| `15M` | `KuCoin` | `48.4%` | `51.6%` | `0.94` | 188,630.00 USD |
| `15M` | `Gate` | `66.46%` | `33.54%` | `1.98` | 134,490.00 USD |
| `15M` | `Bitget` | `70.85%` | `29.15%` | `2.43` | 235,220.00 USD |
| `15M` | `BingX` | `43.66%` | `56.34%` | `0.77` | 38,300.00 USD |
| `15M` | `MEXC` | `32.46%` | `67.54%` | `0.48` | 30,930.00 USD |
| `15M` | `Bitunix` | `50.78%` | `49.22%` | `1.03` | 71,910.00 USD |
| `15M` | `Hyperliquid` | `40.78%` | `59.22%` | `0.69` | 110,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.8%` | `50.2%` | `0.99` | 116,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 2,060.00 USD |
| `15M` | `HTX` | `43.52%` | `56.48%` | `0.77` | 18,380.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `6.78%` | `93.22%` | `0.07` | 1,720.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `7.52%` | `92.48%` | `0.08` | 37,510.00 USD |
| `15M` | `Whale Positions` | `55.89%` | `44.11%` | `1.27` | 2,310,000.00 USD |
| `15M` | `Global Accounts` | `52.90%` | `47.10%` | `1.12` | 4,960,000.00 USD |
| `1H` | `TRX` | `49.39%` | `50.61%` | `0.98` | 18,040,000.00 USD |
| `1H` | `Binance` | `50.6%` | `49.4%` | `1.02` | 6,360,000.00 USD |
| `1H` | `OKX` | `43.96%` | `56.04%` | `0.78` | 1,740,000.00 USD |
| `1H` | `Bybit` | `54.47%` | `45.53%` | `1.20` | 2,350,000.00 USD |
| `1H` | `KuCoin` | `39.03%` | `60.97%` | `0.64` | 113,250.00 USD |
| `1H` | `Gate` | `54.65%` | `45.35%` | `1.21` | 625,490.00 USD |
| `1H` | `Bitget` | `39.87%` | `60.13%` | `0.66` | 1,160,000.00 USD |
| `1H` | `BingX` | `49.11%` | `50.89%` | `0.97` | 983,080.00 USD |
| `1H` | `MEXC` | `47.68%` | `52.32%` | `0.91` | 893,650.00 USD |
| `1H` | `Bitunix` | `45.84%` | `54.16%` | `0.85` | 306,660.00 USD |
| `1H` | `Hyperliquid` | `77.93%` | `22.07%` | `3.53` | 91,490.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.04%` | `47.96%` | `1.09` | 3,050,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `3.18%` | `96.82%` | `0.03` | 163,270.00 USD |
| `1H` | `HTX` | `49.3%` | `50.7%` | `0.97` | 78,700.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `33.92%` | `66.08%` | `0.51` | 31,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.51%` | `62.49%` | `0.60` | 85,480.00 USD |
| `1H` | `Whale Positions` | `50.6%` | `49.4%` | `1.02` | 6,360,000.00 USD |
| `1H` | `Global Accounts` | `49.39%` | `50.61%` | `0.98` | 18,040,000.00 USD |
| `4H` | `TRX` | `51.43%` | `48.57%` | `1.06` | 103,590,000.00 USD |
| `4H` | `Binance` | `53.12%` | `46.88%` | `1.13` | 37,670,000.00 USD |
| `4H` | `OKX` | `51.3%` | `48.7%` | `1.05` | 10,030,000.00 USD |
| `4H` | `Bybit` | `51.36%` | `48.64%` | `1.06` | 12,890,000.00 USD |
| `4H` | `KuCoin` | `53.01%` | `46.99%` | `1.13` | 859,150.00 USD |
| `4H` | `Gate` | `58.23%` | `41.77%` | `1.39` | 3,310,000.00 USD |
| `4H` | `Bitget` | `47.21%` | `52.79%` | `0.89` | 3,220,000.00 USD |
| `4H` | `BingX` | `47.28%` | `52.72%` | `0.90` | 5,860,000.00 USD |
| `4H` | `MEXC` | `49.09%` | `50.91%` | `0.96` | 5,840,000.00 USD |
| `4H` | `Bitunix` | `43.78%` | `56.22%` | `0.78` | 2,680,000.00 USD |
| `4H` | `Hyperliquid` | `58.66%` | `41.34%` | `1.42` | 702,630.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.72%` | `47.28%` | `1.12` | 18,320,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.19%` | `88.81%` | `0.13` | 746,750.00 USD |
| `4H` | `HTX` | `48.73%` | `51.27%` | `0.95` | 671,260.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.27%` | `36.73%` | `1.72` | 358,220.00 USD |
| `4H` | `Aster` | `15.36%` | `84.64%` | `0.18` | 269,570.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.56%` | `75.44%` | `0.33` | 162,290.00 USD |
| `4H` | `Whale Positions` | `53.12%` | `46.88%` | `1.13` | 37,670,000.00 USD |
| `4H` | `Global Accounts` | `51.43%` | `48.57%` | `1.06` | 103,590,000.00 USD |


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
| `0:00 UTC` | `0.3436` | `0.3444` | `0.3436` | `0.3460` | `0.3435` | 652,037.62 USD | 167,951.36 USD | 484,086.25 USD | -316,134.89 USD | `-48.48%` | `16B / 33S` |

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
| `5m` | -536,610.00 USD | 110,350.00 USD | **`DISTRIBUTION`** |
| `15m` | -753,110.00 USD | 387,810.00 USD | **`DISTRIBUTION`** |
| `30m` | -42,620.00 USD | 572,190.00 USD | **`ACCUMULATION`** |
| `1h` | 1,270,000.00 USD | -1,000,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,110,000.00 USD | -1,210,000.00 USD | **`ACCUMULATION`** |
| `4h` | 11,110,000.00 USD | 562,160.00 USD | **`ACCUMULATION`** |
| `6h` | 9,610,000.00 USD | 9,060,000.00 USD | **`ACCUMULATION`** |
| `8h` | 14,110,000.00 USD | 11,200,000.00 USD | **`ACCUMULATION`** |
| `12h` | 12,100,000.00 USD | 11,640,000.00 USD | **`ACCUMULATION`** |
| `24h` | 13,050,000.00 USD | 12,630,000.00 USD | **`ACCUMULATION`** |
| `1w` | 6,470,000.00 USD | 10,770,000.00 USD | **`ACCUMULATION`** |
| `30d` | -13,320,000.00 USD | 13,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-536.61K` | 15m=`-753.11K` | 1h=`+1.27M` | 24h=`+13.05M`
* Futures Capital Netflows: 5m=`+110.35K` | 15m=`+387.81K` | 1h=`-1.00M` | 24h=`+12.63M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3455` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3354` (Risk Distance: `0.0101` pts)
  * +2.5R Take Profit: `0.3708`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3570` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3671` (Risk Distance: `0.0101` pts)
  * +2.5R Take Profit: `0.3317`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3499`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
