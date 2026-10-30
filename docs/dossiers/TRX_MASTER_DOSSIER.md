# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:18:38 IST` (`2026-10-30 02:48:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3542` | **Live Ask Quote**: `0.3576` | **Mid Price**: `0.3559`
- **Spread Points**: `34.00` | **Spread BPS**: `95.53 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3542` | VWAP Z-Score: `+1.48` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0054` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `63.06` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3593` | Lower -3.00σ Band: `0.3491`
  * Upper +2.51σ Band: `0.3585` | Lower -2.51σ Band: `0.3499`
  * Upper +2.01σ Band: `0.3576` | Lower -2.01σ Band: `0.3508`
  * Upper +2.00σ Band: `0.3576` | Lower -2.00σ Band: `0.3508`
  * Upper +1.28σ Band: `0.3564` | Lower -1.28σ Band: `0.3520`
  * Upper +1.00σ Band: `0.3559` | Lower -1.00σ Band: `0.3525`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3541` | EMA-20=`0.3502` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3428` (Slope: `+0.0000`) | EMA-100=`0.3377`
  * Institutional Anchors: EMA-144=`0.3356` | EMA-200=`0.3341` (Slope: `+0.7539`) | EMA-233=`0.3334`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3572` (Distance: `-0.42%`)
  * Point of Control (POC) = `0.3544` (Distance: `+0.36%`)
  * Value Area Low (VAL) = `0.3451` (Distance: `+3.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3470` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3573` | Low=`0.3545`
  * New York Session (13:00-21:00 UTC): High=`0.3580` | Low=`0.3538`
  * Initial Balance (First Hour): IB High=`0.3570` | IB Low=`0.3548`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3545` - `0.3573`
  * Optimal Trade Entry (OTE 0.705): `0.3566`
  * Structural Invalidation Anchor (0.786): `0.3587`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3583` | `0.3584` | `0.3565` | `0.3568` | `2,655,648` | 949,154.93 USD | -140,689.80 USD | `-14.82%` | 6,497,275.12 USD | `-1.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3568` | `0.3587` | `0.3566` | `0.3572` | `3,052,939` | 1,092,220.44 USD | 138,616.41 USD | `+12.69%` | 6,635,891.53 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.3573` | `0.3574` | `0.3553` | `0.3558` | `1,432,879` | 510,738.53 USD | -55,050.13 USD | `-10.78%` | 6,580,841.40 USD | `-0.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3565` | `0.3589` | `0.3549` | `0.3564` | `8,125,133` | 2,900,250.45 USD | 45,893.52 USD | `+1.58%` | 6,574,669.93 USD | `-0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3565` | `0.3599` | `0.3549` | `0.3583` | `8,792,965` | 3,146,983.44 USD | 63,295.00 USD | `+2.01%` | 6,637,964.92 USD | `-0.21` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3583` | `0.3587` | `0.3553` | `0.3558` | `7,157,845` | 2,557,940.51 USD | -62,198.04 USD | `-2.43%` | 6,575,766.89 USD | `-0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3533` | `0.3604` | `0.3498` | `0.3579` | `113,009,587` | 40,089,855.22 USD | 1,802,077.87 USD | `+4.50%` | 5,383,639.13 USD | `+1.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3579` | `0.3608` | `0.3516` | `0.3565` | `62,320,691` | 22,267,555.61 USD | 1,112,045.02 USD | `+4.99%` | 6,495,684.14 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3565` | `0.3599` | `0.3549` | `0.3558` | `24,059,564` | 8,599,347.78 USD | 52,065.00 USD | `+0.61%` | 6,547,749.14 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3498` | `0.3558` | `199,389,842` | 70,956,758.61 USD | 2,966,187.88 USD | `+4.18%` | 6,361,374.46 USD | `+1.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 662,939.61 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,032,247.78 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3498` | `0.3558` | `199,389,842` | 70,956,758.61 USD | 2,966,187.88 USD | `+4.18%` | 6,361,374.46 USD | `+1.73` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3559`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `769` | `0xecb6...2b00` | `LONG` | 2,977,247.31 USD | `8,356,599.00` | `0.3340` | `0.3561` | `0.000000` | 186,235.49 USD | `+6.26%` | `10X Cross` |
| `1511` | `0xeadc...9d55` | `LONG` | 1,424,600.00 USD | `4,000,000.00` | `0.3421` | `0.3561` | `0.000000` | 56,121.91 USD | `+3.94%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3296` | 8,035.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.04K USD at 0.3296 USD [API] | `2026-10-28 21:03:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3591` (Vol: 1,400,000.00 USD, Dist: `+1.28%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--8.39%`)
  * 48H Horizon: Short MP=`0.3591` (Vol: 1,400,000.00 USD, Dist: `+1.28%`) | Long MP=`0.3249` (Vol: 801,900.00 USD, Dist: `--8.39%`)
  * 3D Horizon: Short MP=`0.3588` (Vol: 1,300,000.00 USD, Dist: `+1.18%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--8.39%`)
  * 7D Horizon: Short MP=`0.3588` (Vol: 1,300,000.00 USD, Dist: `+1.18%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--8.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0715` | 117.40 USD | 569,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 105.70 USD | 569,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 188.15 USD | 569,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 7,790.00 USD | 569,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 114.87 USD | 561,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 268.18 USD | 561,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 124.32 USD | 561,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 209.53 USD | 560,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 152.86 USD | 560,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 560,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 3,250.00 USD | 560,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 239.53 USD | 556,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 20,240.00 USD | 556,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 1,140.00 USD | 536,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 652.74 USD | 535,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 10,500.00 USD | 534,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,370.00 USD | 524,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,170.00 USD | 522,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 256.98 USD | 518,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 175.37 USD | 518,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 208.67 USD | 518,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 7,380.00 USD | 517,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,860.00 USD | 510,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 533.44 USD | 508,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 36,500.00 USD | 508,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 635.20 USD | 471,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 598.50 USD | 471,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 45,170.00 USD | 470,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 425,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 423,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 101,430.00 USD | 423,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 321,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,080.00 USD | 317,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 411.84 USD | 315,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 5,220.00 USD | 314,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 415.30 USD | 309,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 5,730.00 USD | 309,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 3,150.00 USD | 303,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 937.65 USD | 300,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 712.16 USD | 299,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 159.45 USD | 298,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 139.92 USD | 298,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 298,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 297,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 2,800.00 USD | 296,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 294,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 263.07 USD | 282,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 230.97 USD | 281,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 281,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 13,200.00 USD | 280,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 752.06 USD | 267,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 26,590.00 USD | 266,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 2,660.00 USD | 239,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 506.08 USD | 237,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 236,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 3,170.00 USD | 236,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 411.32 USD | 233,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 3,950.00 USD | 232,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 80,810.00 USD | 228,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 182.04 USD | 148,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,060.00 USD | 147,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 134,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 19,010.00 USD | 128,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 3,700.00 USD | 109,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 359.16 USD | 105,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 298.92 USD | 105,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 291.50 USD | 105,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 24,310,000.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 104,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 3,540.00 USD | 103,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 213.81 USD | 100,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 24,230,000.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 24,170,000.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 100,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 24,090,000.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,950,000.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 305.39 USD | 100,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 23,720,000.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 23,460,000.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 23,350,000.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 23,130,000.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,980,000.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 3,440.00 USD | 99,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3001` | 21,260,000.00 USD | 21,260,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 198.03 USD | 96,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 21,260,000.00 USD | 21,260,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,970,000.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,650.00 USD | 96,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 103.15 USD | 85,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 21,200,000.00 USD | 21,200,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 2,520.00 USD | 85,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 267.35 USD | 82,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 21,160,000.00 USD | 21,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 22,930,000.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 21,080,000.00 USD | 21,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 22,880,000.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 138.70 USD | 82,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 21,010,000.00 USD | 21,010,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 22,880,000.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 82,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 20,950,000.00 USD | 20,950,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 22,810,000.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 20,870,000.00 USD | 20,870,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 22,800,000.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 5,920.00 USD | 67,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3079` | 20,840,000.00 USD | 20,840,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 22,790,000.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 20,840,000.00 USD | 20,840,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 22,690,000.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 724.98 USD | 61,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3091` | 20,820,000.00 USD | 20,820,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 22,690,000.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 292.48 USD | 61,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 20,820,000.00 USD | 20,820,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 22,680,000.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 20,820,000.00 USD | 20,820,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 22,660,000.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 530.02 USD | 60,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 22,530,000.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 22,520,000.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,500.00 USD | 60,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3121` | 22,520,000.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 246.56 USD | 46,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 20,710,000.00 USD | 20,710,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 22,360,000.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 20,680,000.00 USD | 20,680,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 22,340,000.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 21,230.00 USD | 46,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 20,630,000.00 USD | 20,630,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 22,340,000.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 20,630,000.00 USD | 20,630,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 22,330,000.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 141.84 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3151` | 20,630,000.00 USD | 20,630,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 22,020,000.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,490.00 USD | 25,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 21,760,000.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 20,590,000.00 USD | 20,590,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 21,220,000.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 23,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 20,440,000.00 USD | 20,440,000.00 USD | 84,050.00 USD | 16,200.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 20,330,000.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 20,300,000.00 USD | 20,300,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 19,470,000.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,500.00 USD | 22,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3181` | 20,220,000.00 USD | 20,220,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 19,140,000.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 109.25 USD | 20,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3187` | 19,670,000.00 USD | 19,670,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 18,190,000.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 17,720,000.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 19,400,000.00 USD | 19,400,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 19,350,000.00 USD | 19,350,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 17,420,000.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 19,050,000.00 USD | 19,050,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 17,320,000.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 18,890,000.00 USD | 18,890,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 16,460,000.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 18,800,000.00 USD | 18,800,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 16,010,000.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 18,510,000.00 USD | 18,510,000.00 USD | 140,560.00 USD | 81,070.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 15,080,000.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 18,080,000.00 USD | 18,080,000.00 USD | 129,720.00 USD | 77,760.00 USD | 168,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 13,630,000.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 17,710,000.00 USD | 17,710,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 11,910,000.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 17,510,000.00 USD | 17,510,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 11,100,000.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 16,520,000.00 USD | 16,520,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 9,770,000.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 2,280.00 USD | 20,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 15,150,000.00 USD | 15,150,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 8,440,000.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 8,050,000.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3271` | 14,630,000.00 USD | 14,630,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 7,860,000.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 2,970.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 14,170,000.00 USD | 14,170,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 7,660,000.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 163.92 USD | 14,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 13,700,000.00 USD | 13,700,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 13,500,000.00 USD | 13,500,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 7,270,000.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 7,240,000.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3305` | 3,300.00 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3307` | 13,420,000.00 USD | 13,420,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 7,170,000.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 13,210,000.00 USD | 13,210,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 6,830,000.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 12,500,000.00 USD | 12,500,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 11,990,000.00 USD | 11,990,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 6,580,000.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3325` | 160.93 USD | 11,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3331` | 11,660,000.00 USD | 11,660,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 6,450,000.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3335` | 474.57 USD | 11,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3337` | 11,660,000.00 USD | 11,660,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 10,770,000.00 USD | 10,770,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 1,010.00 USD | 10,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3349` | 10,600,000.00 USD | 10,600,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 5,610,000.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3355` | 10,260,000.00 USD | 10,260,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 5,380,000.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3355` | 7,800.00 USD | 9,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3361` | 10,170,000.00 USD | 10,170,000.00 USD | 177,350.00 USD | 81,810.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 5,120,000.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 9,840,000.00 USD | 9,840,000.00 USD | 237,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3373` | 9,600,000.00 USD | 9,600,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 4,880,000.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3379` | 9,470,000.00 USD | 9,470,000.00 USD | 514,160.00 USD | 67,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 4,290,000.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 8,890,000.00 USD | 8,890,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 3,620,000.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3385` | 116.78 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3391` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3395` | 841.96 USD | 1,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3397` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,340,000.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 2,910,000.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3405` | 343.22 USD | 998.90 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3409` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 8,210,000.00 USD | 8,210,000.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3415` | 655.68 USD | 655.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3421` | 7,400,000.00 USD | 7,400,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3427` | 6,890,000.00 USD | 6,890,000.00 USD | 262,640.00 USD | 93,060.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3433` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 162,950.00 USD | 176,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3439` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 34,460.00 USD | 392,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3445` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 217,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3445` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3451` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 46,510.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3457` | 5,090,000.00 USD | 5,090,000.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3469` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3469` | 699,440.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3475` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3481` | 191,880.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3487` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3499` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3505` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3517` | 2,440,000.00 USD | 2,440,000.00 USD | 221,620.00 USD | 0.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3523` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3529` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3541` | 704,710.00 USD | 704,710.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3547` | 534,120.00 USD | 534,120.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 653,810.00 USD | 653,810.00 USD | 0.00 USD | 119,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3559` | 1,490,000.00 USD | 1,490,000.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 2,230,000.00 USD | 2,230,000.00 USD | 3,220.00 USD | 163,630.00 USD | 578,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 2,620,000.00 USD | 2,620,000.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 3,100,000.00 USD | 3,100,000.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 3,720,000.00 USD | 3,720,000.00 USD | 1,810.00 USD | 212,630.00 USD | 400,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3595` | 4,080,000.00 USD | 4,080,000.00 USD | 199,420.00 USD | 163,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 91,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 4,430,000.00 USD | 4,430,000.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 5,400,000.00 USD | 5,400,000.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 5,520,000.00 USD | 5,520,000.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 5,640,000.00 USD | 5,640,000.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 43,900.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 5,860,000.00 USD | 5,860,000.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 6,150,000.00 USD | 6,150,000.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 6,430,000.00 USD | 6,430,000.00 USD | 259,500.00 USD | 23,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3667` | 6,840,000.00 USD | 6,840,000.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 6,920,000.00 USD | 6,920,000.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,360.00 USD | 46,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3679` | 7,670,000.00 USD | 7,670,000.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 8,210,000.00 USD | 8,210,000.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 2,050.00 USD | 48,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3691` | 8,540,000.00 USD | 8,540,000.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3695` | 221.33 USD | 48,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3697` | 8,720,000.00 USD | 8,720,000.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 9,470,000.00 USD | 9,470,000.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 10,000,000.00 USD | 10,000,000.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 11,500,000.00 USD | 11,500,000.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 2,690.00 USD | 51,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3721` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 179.92 USD | 51,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3727` | 12,860,000.00 USD | 12,860,000.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 13,730,000.00 USD | 13,730,000.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 3,240.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3739` | 14,220,000.00 USD | 14,220,000.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 14,600,000.00 USD | 14,600,000.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 23,830.00 USD | 78,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 15,440,000.00 USD | 15,440,000.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 38,070.00 USD | 116,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 15,710,000.00 USD | 15,710,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 16,960,000.00 USD | 16,960,000.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3765` | 172.06 USD | 116,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3769` | 17,010,000.00 USD | 17,010,000.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3775` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3781` | 17,320,000.00 USD | 17,320,000.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 104.47 USD | 116,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 17,830,000.00 USD | 17,830,000.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 18,030,000.00 USD | 18,030,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 558,060.00 USD | 674,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3799` | 18,030,000.00 USD | 18,030,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 18,360,000.00 USD | 18,360,000.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3823` | 18,630,000.00 USD | 18,630,000.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3829` | 18,660,000.00 USD | 18,660,000.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 99,860.00 USD | 774,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3841` | 18,870,000.00 USD | 18,870,000.00 USD | 850.22 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3847` | 18,870,000.00 USD | 18,870,000.00 USD | 899.18 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3853` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3865` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3871` | 18,970,000.00 USD | 18,970,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3877` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3883` | 19,000,000.00 USD | 19,000,000.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3885` | 695.80 USD | 775,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3895` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 780,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 19,080,000.00 USD | 19,080,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3913` | 19,250,000.00 USD | 19,250,000.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 780,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 19,320,000.00 USD | 19,320,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 19,390,000.00 USD | 19,390,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3931` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 2,250.00 USD | 782,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3937` | 19,560,000.00 USD | 19,560,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 19,770,000.00 USD | 19,770,000.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 901,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 19,900,000.00 USD | 19,900,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 20,100,000.00 USD | 20,100,000.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 123.40 USD | 901,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3961` | 20,200,000.00 USD | 20,200,000.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 1,580.00 USD | 902,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3967` | 20,290,000.00 USD | 20,290,000.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 20,460,000.00 USD | 20,460,000.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3979` | 20,860,000.00 USD | 20,860,000.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 20,870,000.00 USD | 20,870,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3991` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3997` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 21,080,000.00 USD | 21,080,000.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4005` | 45,000.00 USD | 947,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.4009` | 21,240,000.00 USD | 21,240,000.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4027` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4035` | 190.45 USD | 947,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.4045` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,040.00 USD | 950,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 410.73 USD | 950,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4175` | 599.53 USD | 951,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 4,720.00 USD | 955,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 11,900.00 USD | 967,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4285` | 81,730.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4295` | 10,210.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4325` | 70,400.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 378.34 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 307.39 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 1,130.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,060.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4485` | 65,760.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 7,130.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4535` | 1,140.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4555` | 1,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4595` | 19,280.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4645` | 603,850.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4675` | 280,590.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4735` | 8,060.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4795` | 3,330.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 16,810.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 2,740.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 235.71 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5055` | 292.18 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5105` | 790,090.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5495` | 2,280.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5535` | 40,960.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5595` | 8,260.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5745` | 55,060.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5795` | 441,200.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5855` | 759,540.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5965` | 1,060.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 28,550.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6265` | 32,930.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 1,140.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 48,630.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6445` | 1,060.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6555` | 27,910.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6595` | 399.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 81,930.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6625` | 2,060.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 2,530.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 1,210.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6705` | 824.72 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6735` | 83,060.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6745` | 978.70 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6805` | 16,850.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6875` | 262.62 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6925` | 414.12 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7005` | 28,020.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7015` | 794,240.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7095` | 4,190.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0715` | 569,590.00 USD | 0.00 USD | 117.40 USD | `-79.93%` | `1,642.00` |
| `Live` | `Long` | `0.0865` | 569,470.00 USD | 0.00 USD | 105.70 USD | `-75.72%` | `1,222.00` |
| `Live` | `Long` | `0.0905` | 569,370.00 USD | 0.00 USD | 188.15 USD | `-74.60%` | `2,079.00` |
| `Live` | `Long` | `0.1015` | 569,180.00 USD | 0.00 USD | 7,790.00 USD | `-71.52%` | `76,797.00` |
| `Live` | `Long` | `0.1095` | 561,380.00 USD | 0.00 USD | 114.87 USD | `-69.27%` | `1,049.00` |
| `Live` | `Long` | `0.1165` | 561,270.00 USD | 0.00 USD | 268.18 USD | `-67.31%` | `2,302.00` |
| `Live` | `Long` | `0.1175` | 561,000.00 USD | 0.00 USD | 124.32 USD | `-67.02%` | `1,058.00` |
| `Live` | `Long` | `0.1485` | 560,880.00 USD | 0.00 USD | 209.53 USD | `-58.33%` | `1,411.00` |
| `Live` | `Long` | `0.1515` | 560,670.00 USD | 0.00 USD | 152.86 USD | `-57.48%` | `1,009.00` |
| `Live` | `Long` | `0.1595` | 560,510.00 USD | 0.00 USD | 390.46 USD | `-55.24%` | `2,448.00` |
| `Live` | `Long` | `0.1625` | 560,120.00 USD | 0.00 USD | 3,250.00 USD | `-54.40%` | `20,000.00` |
| `Live` | `Long` | `0.1675` | 556,870.00 USD | 0.00 USD | 239.53 USD | `-52.99%` | `1,430.00` |
| `Live` | `Long` | `0.1695` | 556,630.00 USD | 0.00 USD | 20,240.00 USD | `-52.43%` | `119,400.00` |
| `Live` | `Long` | `0.1715` | 536,400.00 USD | 0.00 USD | 1,140.00 USD | `-51.87%` | `6,621.00` |
| `Live` | `Long` | `0.1725` | 535,260.00 USD | 0.00 USD | 652.74 USD | `-51.59%` | `3,784.00` |
| `Live` | `Long` | `0.1735` | 534,610.00 USD | 0.00 USD | 10,500.00 USD | `-51.31%` | `60,538.00` |
| `Live` | `Long` | `0.1745` | 524,100.00 USD | 0.00 USD | 1,370.00 USD | `-51.03%` | `7,823.00` |
| `Live` | `Long` | `0.1755` | 522,740.00 USD | 0.00 USD | 4,170.00 USD | `-50.75%` | `23,777.00` |
| `Live` | `Long` | `0.1765` | 518,570.00 USD | 0.00 USD | 256.98 USD | `-50.47%` | `1,456.00` |
| `Live` | `Long` | `0.1775` | 518,310.00 USD | 0.00 USD | 175.37 USD | `-50.19%` | `988.00` |
| `Live` | `Long` | `0.1785` | 518,130.00 USD | 0.00 USD | 208.67 USD | `-49.91%` | `1,169.00` |
| `Live` | `Long` | `0.1795` | 517,920.00 USD | 0.00 USD | 7,380.00 USD | `-49.63%` | `41,100.00` |
| `Live` | `Long` | `0.1845` | 510,550.00 USD | 0.00 USD | 1,860.00 USD | `-48.22%` | `10,084.00` |
| `Live` | `Long` | `0.1875` | 508,690.00 USD | 0.00 USD | 533.44 USD | `-47.38%` | `2,845.00` |
| `Live` | `Long` | `0.1885` | 508,150.00 USD | 0.00 USD | 36,500.00 USD | `-47.10%` | `193,636.00` |
| `Live` | `Long` | `0.1985` | 471,650.00 USD | 0.00 USD | 635.20 USD | `-44.29%` | `3,200.00` |
| `Live` | `Long` | `0.1995` | 471,020.00 USD | 0.00 USD | 598.50 USD | `-44.01%` | `3,000.00` |
| `Live` | `Long` | `0.2065` | 470,420.00 USD | 0.00 USD | 45,170.00 USD | `-42.05%` | `218,745.00` |
| `Live` | `Long` | `0.2175` | 425,250.00 USD | 0.00 USD | 1,520.00 USD | `-38.96%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 423,730.00 USD | 0.00 USD | 515.17 USD | `-38.40%` | `2,347.00` |
| `Live` | `Long` | `0.2225` | 423,210.00 USD | 0.00 USD | 101,430.00 USD | `-37.56%` | `455,855.00` |
| `Live` | `Long` | `0.2255` | 321,780.00 USD | 0.00 USD | 4,590.00 USD | `-36.72%` | `20,360.00` |
| `Live` | `Long` | `0.2305` | 317,190.00 USD | 0.00 USD | 2,080.00 USD | `-35.31%` | `9,004.00` |
| `Live` | `Long` | `0.2315` | 315,120.00 USD | 0.00 USD | 411.84 USD | `-35.03%` | `1,779.00` |
| `Live` | `Long` | `0.2335` | 314,700.00 USD | 0.00 USD | 5,220.00 USD | `-34.47%` | `22,339.00` |
| `Live` | `Long` | `0.2345` | 309,490.00 USD | 0.00 USD | 415.30 USD | `-34.19%` | `1,771.00` |
| `Live` | `Long` | `0.2355` | 309,070.00 USD | 0.00 USD | 5,730.00 USD | `-33.91%` | `24,311.00` |
| `Live` | `Long` | `0.2365` | 303,350.00 USD | 0.00 USD | 3,150.00 USD | `-33.63%` | `13,311.00` |
| `Live` | `Long` | `0.2375` | 300,200.00 USD | 0.00 USD | 937.65 USD | `-33.35%` | `3,948.00` |
| `Live` | `Long` | `0.2385` | 299,260.00 USD | 0.00 USD | 712.16 USD | `-33.07%` | `2,986.00` |
| `Live` | `Long` | `0.2405` | 298,550.00 USD | 0.00 USD | 159.45 USD | `-32.51%` | `663.00` |
| `Live` | `Long` | `0.2425` | 298,390.00 USD | 0.00 USD | 139.92 USD | `-31.95%` | `577.00` |
| `Live` | `Long` | `0.2445` | 298,250.00 USD | 0.00 USD | 889.49 USD | `-31.38%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 297,360.00 USD | 0.00 USD | 466.70 USD | `-31.10%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 296,890.00 USD | 0.00 USD | 2,800.00 USD | `-30.82%` | `11,365.00` |
| `Live` | `Long` | `0.2485` | 294,090.00 USD | 0.00 USD | 11,890.00 USD | `-30.26%` | `47,833.00` |
| `Live` | `Long` | `0.2515` | 282,210.00 USD | 0.00 USD | 263.07 USD | `-29.42%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 281,940.00 USD | 0.00 USD | 230.97 USD | `-28.30%` | `904.00` |
| `Live` | `Long` | `0.2565` | 281,710.00 USD | 0.00 USD | 1,230.00 USD | `-28.02%` | `4,794.00` |
| `Live` | `Long` | `0.2595` | 280,480.00 USD | 0.00 USD | 13,200.00 USD | `-27.17%` | `50,854.00` |
| `Live` | `Long` | `0.2605` | 267,290.00 USD | 0.00 USD | 752.06 USD | `-26.89%` | `2,887.00` |
| `Live` | `Long` | `0.2625` | 266,530.00 USD | 0.00 USD | 26,590.00 USD | `-26.33%` | `101,292.00` |
| `Live` | `Long` | `0.2655` | 239,940.00 USD | 0.00 USD | 2,660.00 USD | `-25.49%` | `10,032.00` |
| `Live` | `Long` | `0.2665` | 237,280.00 USD | 0.00 USD | 506.08 USD | `-25.21%` | `1,899.00` |
| `Live` | `Long` | `0.2685` | 236,770.00 USD | 0.00 USD | 322.74 USD | `-24.65%` | `1,202.00` |
| `Live` | `Long` | `0.2695` | 236,450.00 USD | 0.00 USD | 3,170.00 USD | `-24.37%` | `11,746.00` |
| `Live` | `Long` | `0.2715` | 233,290.00 USD | 0.00 USD | 411.32 USD | `-23.81%` | `1,515.00` |
| `Live` | `Long` | `0.2745` | 232,880.00 USD | 0.00 USD | 3,950.00 USD | `-22.96%` | `14,395.00` |
| `Live` | `Long` | `0.2755` | 228,920.00 USD | 0.00 USD | 80,810.00 USD | `-22.68%` | `293,333.00` |
| `Live` | `Long` | `0.2775` | 148,110.00 USD | 0.00 USD | 182.04 USD | `-22.12%` | `656.00` |
| `Live` | `Long` | `0.2795` | 147,930.00 USD | 0.00 USD | 13,060.00 USD | `-21.56%` | `46,725.00` |
| `Live` | `Long` | `0.2805` | 134,870.00 USD | 0.00 USD | 6,280.00 USD | `-21.28%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 128,590.00 USD | 0.00 USD | 19,010.00 USD | `-21.00%` | `67,528.00` |
| `Live` | `Long` | `0.2825` | 109,580.00 USD | 0.00 USD | 3,700.00 USD | `-20.72%` | `13,109.00` |
| `Live` | `Long` | `0.2855` | 105,880.00 USD | 0.00 USD | 359.16 USD | `-19.88%` | `1,258.00` |
| `Live` | `Long` | `0.2905` | 105,520.00 USD | 0.00 USD | 298.92 USD | `-18.47%` | `1,029.00` |
| `Live` | `Long` | `0.2915` | 105,220.00 USD | 0.00 USD | 291.50 USD | `-18.19%` | `1,000.00` |
| `Live` | `Long` | `0.2925` | 104,930.00 USD | 0.00 USD | 957.64 USD | `-17.91%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 103,970.00 USD | 0.00 USD | 3,540.00 USD | `-17.63%` | `12,054.00` |
| `Live` | `Long` | `0.2945` | 100,430.00 USD | 0.00 USD | 213.81 USD | `-17.35%` | `726.00` |
| `Live` | `Long` | `0.2955` | 100,220.00 USD | 0.00 USD | 125.29 USD | `-17.07%` | `424.00` |
| `Live` | `Long` | `0.2965` | 100,090.00 USD | 0.00 USD | 305.39 USD | `-16.79%` | `1,030.00` |
| `Live` | `Long` | `0.2995` | 99,790.00 USD | 0.00 USD | 3,440.00 USD | `-15.95%` | `11,488.00` |
| `Live` | `Long` | `0.3005` | 96,350.00 USD | 0.00 USD | 198.03 USD | `-15.67%` | `659.00` |
| `Live` | `Long` | `0.3015` | 96,150.00 USD | 0.00 USD | 10,650.00 USD | `-15.39%` | `35,336.00` |
| `Live` | `Long` | `0.3025` | 85,500.00 USD | 0.00 USD | 103.15 USD | `-15.11%` | `341.00` |
| `Live` | `Long` | `0.3035` | 85,390.00 USD | 0.00 USD | 2,520.00 USD | `-14.83%` | `8,314.00` |
| `Live` | `Long` | `0.3045` | 82,870.00 USD | 0.00 USD | 267.35 USD | `-14.55%` | `878.00` |
| `Live` | `Long` | `0.3055` | 82,600.00 USD | 0.00 USD | 138.70 USD | `-14.26%` | `454.00` |
| `Live` | `Long` | `0.3065` | 82,460.00 USD | 0.00 USD | 14,720.00 USD | `-13.98%` | `48,026.00` |
| `Live` | `Long` | `0.3075` | 67,740.00 USD | 0.00 USD | 5,920.00 USD | `-13.70%` | `19,262.00` |
| `Live` | `Long` | `0.3085` | 61,820.00 USD | 0.00 USD | 724.98 USD | `-13.42%` | `2,350.00` |
| `Live` | `Long` | `0.3095` | 61,100.00 USD | 0.00 USD | 292.48 USD | `-13.14%` | `945.00` |
| `Live` | `Long` | `0.3105` | 60,800.00 USD | 0.00 USD | 530.02 USD | `-12.86%` | `1,707.00` |
| `Live` | `Long` | `0.3115` | 60,270.00 USD | 0.00 USD | 13,500.00 USD | `-12.58%` | `43,326.00` |
| `Live` | `Long` | `0.3125` | 46,780.00 USD | 0.00 USD | 246.56 USD | `-12.30%` | `789.00` |
| `Live` | `Long` | `0.3135` | 46,530.00 USD | 0.00 USD | 21,230.00 USD | `-12.02%` | `67,725.00` |
| `Live` | `Long` | `0.3145` | 25,300.00 USD | 0.00 USD | 141.84 USD | `-11.74%` | `451.00` |
| `Live` | `Long` | `0.3155` | 25,160.00 USD | 0.00 USD | 1,490.00 USD | `-11.46%` | `4,723.00` |
| `Live` | `Long` | `0.3165` | 23,670.00 USD | 0.00 USD | 935.89 USD | `-11.18%` | `2,957.00` |
| `Live` | `Long` | `0.3175` | 22,730.00 USD | 0.00 USD | 2,500.00 USD | `-10.90%` | `7,883.00` |
| `Live` | `Long` | `0.3185` | 20,230.00 USD | 0.00 USD | 109.25 USD | `-10.62%` | `343.00` |
| `Live` | `Long` | `0.3255` | 20,120.00 USD | 0.00 USD | 2,280.00 USD | `-8.65%` | `6,996.00` |
| `Live` | `Long` | `0.3275` | 17,840.00 USD | 0.00 USD | 2,970.00 USD | `-8.09%` | `9,073.00` |
| `Live` | `Long` | `0.3285` | 14,870.00 USD | 0.00 USD | 163.92 USD | `-7.81%` | `499.00` |
| `Live` | `Long` | `0.3305` | 14,710.00 USD | 0.00 USD | 3,300.00 USD | `-7.25%` | `9,995.00` |
| `Live` | `Long` | `0.3325` | 11,400.00 USD | 0.00 USD | 160.93 USD | `-6.69%` | `484.00` |
| `Live` | `Long` | `0.3335` | 11,240.00 USD | 0.00 USD | 474.57 USD | `-6.41%` | `1,423.00` |
| `Live` | `Long` | `0.3345` | 10,770.00 USD | 0.00 USD | 1,010.00 USD | `-6.13%` | `3,030.00` |
| `Live` | `Long` | `0.3355` | 9,750.00 USD | 0.00 USD | 7,800.00 USD | `-5.85%` | `23,240.00` |
| `Live` | `Long` | `0.3385` | 1,960.00 USD | 0.00 USD | 116.78 USD | `-5.00%` | `345.00` |
| `Live` | `Long` | `0.3395` | 1,840.00 USD | 0.00 USD | 841.96 USD | `-4.72%` | `2,480.00` |
| `Live` | `Long` | `0.3405` | 998.90 USD | 0.00 USD | 343.22 USD | `-4.44%` | `1,008.00` |
| `Live` | `Long` | `0.3415` | 655.68 USD | 0.00 USD | 655.68 USD | `-4.16%` | `1,920.00` |
| `Live` | `Short` | `0.3645` | 43,900.00 USD | 43,900.00 USD | 0.00 USD | `+2.29%` | `120,426.00` |
| `Live` | `Short` | `0.3675` | 46,250.00 USD | 2,360.00 USD | 0.00 USD | `+3.13%` | `6,413.00` |
| `Live` | `Short` | `0.3685` | 48,300.00 USD | 2,050.00 USD | 0.00 USD | `+3.42%` | `5,557.00` |
| `Live` | `Short` | `0.3695` | 48,520.00 USD | 221.33 USD | 0.00 USD | `+3.70%` | `599.00` |
| `Live` | `Short` | `0.3715` | 51,210.00 USD | 2,690.00 USD | 0.00 USD | `+4.26%` | `7,251.00` |
| `Live` | `Short` | `0.3725` | 51,390.00 USD | 179.92 USD | 0.00 USD | `+4.54%` | `483.00` |
| `Live` | `Short` | `0.3735` | 54,630.00 USD | 3,240.00 USD | 0.00 USD | `+4.82%` | `8,671.00` |
| `Live` | `Short` | `0.3745` | 78,460.00 USD | 23,830.00 USD | 0.00 USD | `+5.10%` | `63,619.00` |
| `Live` | `Short` | `0.3755` | 116,530.00 USD | 38,070.00 USD | 0.00 USD | `+5.38%` | `101,398.00` |
| `Live` | `Short` | `0.3765` | 116,710.00 USD | 172.06 USD | 0.00 USD | `+5.66%` | `457.00` |
| `Live` | `Short` | `0.3785` | 116,810.00 USD | 104.47 USD | 0.00 USD | `+6.22%` | `276.00` |
| `Live` | `Short` | `0.3795` | 674,870.00 USD | 558,060.00 USD | 0.00 USD | `+6.50%` | `1,470,526.00` |
| `Live` | `Short` | `0.3835` | 774,740.00 USD | 99,860.00 USD | 0.00 USD | `+7.62%` | `260,396.00` |
| `Live` | `Short` | `0.3885` | 775,430.00 USD | 695.80 USD | 0.00 USD | `+9.03%` | `1,791.00` |
| `Live` | `Short` | `0.3905` | 780,200.00 USD | 4,770.00 USD | 0.00 USD | `+9.59%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 780,690.00 USD | 487.42 USD | 0.00 USD | `+9.87%` | `1,245.00` |
| `Live` | `Short` | `0.3935` | 782,940.00 USD | 2,250.00 USD | 0.00 USD | `+10.43%` | `5,719.00` |
| `Live` | `Short` | `0.3945` | 901,070.00 USD | 118,130.00 USD | 0.00 USD | `+10.71%` | `299,436.00` |
| `Live` | `Short` | `0.3955` | 901,190.00 USD | 123.40 USD | 0.00 USD | `+10.99%` | `312.00` |
| `Live` | `Short` | `0.3965` | 902,770.00 USD | 1,580.00 USD | 0.00 USD | `+11.27%` | `3,992.00` |
| `Live` | `Short` | `0.4005` | 947,780.00 USD | 45,000.00 USD | 0.00 USD | `+12.40%` | `112,367.00` |
| `Live` | `Short` | `0.4035` | 947,970.00 USD | 190.45 USD | 0.00 USD | `+13.24%` | `472.00` |
| `Live` | `Short` | `0.4085` | 950,010.00 USD | 2,040.00 USD | 0.00 USD | `+14.64%` | `4,999.00` |
| `Live` | `Short` | `0.4095` | 950,420.00 USD | 410.73 USD | 0.00 USD | `+14.92%` | `1,003.00` |
| `Live` | `Short` | `0.4175` | 951,020.00 USD | 599.53 USD | 0.00 USD | `+17.17%` | `1,436.00` |
| `Live` | `Short` | `0.4195` | 955,740.00 USD | 4,720.00 USD | 0.00 USD | `+17.73%` | `11,258.00` |
| `Live` | `Short` | `0.4235` | 967,640.00 USD | 11,900.00 USD | 0.00 USD | `+18.85%` | `28,092.00` |
| `Live` | `Short` | `0.4285` | 1,050,000.00 USD | 81,730.00 USD | 0.00 USD | `+20.25%` | `190,735.00` |
| `Live` | `Short` | `0.4295` | 1,060,000.00 USD | 10,210.00 USD | 0.00 USD | `+20.53%` | `23,779.00` |
| `Live` | `Short` | `0.4325` | 1,130,000.00 USD | 70,400.00 USD | 0.00 USD | `+21.38%` | `162,775.00` |
| `Live` | `Short` | `0.4425` | 1,130,000.00 USD | 378.34 USD | 0.00 USD | `+24.18%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,130,000.00 USD | 307.39 USD | 0.00 USD | `+25.02%` | `690.00` |
| `Live` | `Short` | `0.4465` | 1,130,000.00 USD | 1,130.00 USD | 0.00 USD | `+25.31%` | `2,539.00` |
| `Live` | `Short` | `0.4475` | 1,130,000.00 USD | 1,060.00 USD | 0.00 USD | `+25.59%` | `2,371.00` |
| `Live` | `Short` | `0.4485` | 1,200,000.00 USD | 65,760.00 USD | 0.00 USD | `+25.87%` | `146,614.00` |
| `Live` | `Short` | `0.4525` | 1,210,000.00 USD | 7,130.00 USD | 0.00 USD | `+26.99%` | `15,751.00` |
| `Live` | `Short` | `0.4535` | 1,210,000.00 USD | 1,140.00 USD | 0.00 USD | `+27.27%` | `2,519.00` |
| `Live` | `Short` | `0.4555` | 1,210,000.00 USD | 1,800.00 USD | 0.00 USD | `+27.83%` | `3,962.00` |
| `Live` | `Short` | `0.4595` | 1,230,000.00 USD | 19,280.00 USD | 0.00 USD | `+28.95%` | `41,969.00` |
| `Live` | `Short` | `0.4645` | 1,830,000.00 USD | 603,850.00 USD | 0.00 USD | `+30.36%` | `1,300,000.00` |
| `Live` | `Short` | `0.4675` | 2,110,000.00 USD | 280,590.00 USD | 0.00 USD | `+31.20%` | `600,198.00` |
| `Live` | `Short` | `0.4735` | 2,120,000.00 USD | 8,060.00 USD | 0.00 USD | `+32.88%` | `17,027.00` |
| `Live` | `Short` | `0.4795` | 2,120,000.00 USD | 3,330.00 USD | 0.00 USD | `+34.57%` | `6,944.00` |
| `Live` | `Short` | `0.4905` | 2,120,000.00 USD | 841.21 USD | 0.00 USD | `+37.65%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 2,130,000.00 USD | 5,130.00 USD | 0.00 USD | `+37.93%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,150,000.00 USD | 16,810.00 USD | 0.00 USD | `+40.18%` | `33,650.00` |
| `Live` | `Short` | `0.5005` | 2,150,000.00 USD | 2,740.00 USD | 0.00 USD | `+40.46%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 2,150,000.00 USD | 235.71 USD | 0.00 USD | `+40.74%` | `470.00` |
| `Live` | `Short` | `0.5055` | 2,150,000.00 USD | 292.18 USD | 0.00 USD | `+41.86%` | `578.00` |
| `Live` | `Short` | `0.5105` | 2,940,000.00 USD | 790,090.00 USD | 0.00 USD | `+43.27%` | `1,547,681.00` |
| `Live` | `Short` | `0.5335` | 2,940,000.00 USD | 668.48 USD | 0.00 USD | `+49.72%` | `1,253.00` |
| `Live` | `Short` | `0.5495` | 2,940,000.00 USD | 2,280.00 USD | 0.00 USD | `+54.21%` | `4,154.00` |
| `Live` | `Short` | `0.5535` | 2,980,000.00 USD | 40,960.00 USD | 0.00 USD | `+55.33%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,980,000.00 USD | 740.92 USD | 0.00 USD | `+56.46%` | `1,329.00` |
| `Live` | `Short` | `0.5595` | 2,990,000.00 USD | 8,260.00 USD | 0.00 USD | `+57.02%` | `14,763.00` |
| `Live` | `Short` | `0.5615` | 2,990,000.00 USD | 140.38 USD | 0.00 USD | `+57.58%` | `250.00` |
| `Live` | `Short` | `0.5745` | 3,050,000.00 USD | 55,060.00 USD | 0.00 USD | `+61.23%` | `95,846.00` |
| `Live` | `Short` | `0.5795` | 3,490,000.00 USD | 441,200.00 USD | 0.00 USD | `+62.63%` | `761,341.00` |
| `Live` | `Short` | `0.5855` | 4,250,000.00 USD | 759,540.00 USD | 0.00 USD | `+64.31%` | `1,297,248.00` |
| `Live` | `Short` | `0.5965` | 4,250,000.00 USD | 1,060.00 USD | 0.00 USD | `+67.40%` | `1,776.00` |
| `Live` | `Short` | `0.6155` | 4,280,000.00 USD | 28,550.00 USD | 0.00 USD | `+72.73%` | `46,380.00` |
| `Live` | `Short` | `0.6265` | 4,310,000.00 USD | 32,930.00 USD | 0.00 USD | `+75.82%` | `52,566.00` |
| `Live` | `Short` | `0.6285` | 4,310,000.00 USD | 1,140.00 USD | 0.00 USD | `+76.38%` | `1,808.00` |
| `Live` | `Short` | `0.6345` | 4,360,000.00 USD | 48,630.00 USD | 0.00 USD | `+78.07%` | `76,641.00` |
| `Live` | `Short` | `0.6445` | 4,360,000.00 USD | 1,060.00 USD | 0.00 USD | `+80.87%` | `1,642.00` |
| `Live` | `Short` | `0.6515` | 4,360,000.00 USD | 951.19 USD | 0.00 USD | `+82.84%` | `1,460.00` |
| `Live` | `Short` | `0.6555` | 4,390,000.00 USD | 27,910.00 USD | 0.00 USD | `+83.96%` | `42,576.00` |
| `Live` | `Short` | `0.6595` | 4,390,000.00 USD | 399.00 USD | 0.00 USD | `+85.08%` | `605.00` |
| `Live` | `Short` | `0.6615` | 4,470,000.00 USD | 81,930.00 USD | 0.00 USD | `+85.64%` | `123,851.00` |
| `Live` | `Short` | `0.6625` | 4,480,000.00 USD | 2,060.00 USD | 0.00 USD | `+85.92%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 4,480,000.00 USD | 2,530.00 USD | 0.00 USD | `+86.20%` | `3,811.00` |
| `Live` | `Short` | `0.6645` | 4,480,000.00 USD | 1,210.00 USD | 0.00 USD | `+86.48%` | `1,821.00` |
| `Live` | `Short` | `0.6705` | 4,480,000.00 USD | 824.72 USD | 0.00 USD | `+88.17%` | `1,230.00` |
| `Live` | `Short` | `0.6735` | 4,560,000.00 USD | 83,060.00 USD | 0.00 USD | `+89.01%` | `123,332.00` |
| `Live` | `Short` | `0.6745` | 4,560,000.00 USD | 978.70 USD | 0.00 USD | `+89.29%` | `1,451.00` |
| `Live` | `Short` | `0.6805` | 4,580,000.00 USD | 16,850.00 USD | 0.00 USD | `+90.97%` | `24,756.00` |
| `Live` | `Short` | `0.6875` | 4,580,000.00 USD | 262.62 USD | 0.00 USD | `+92.94%` | `382.00` |
| `Live` | `Short` | `0.6925` | 4,580,000.00 USD | 414.12 USD | 0.00 USD | `+94.34%` | `598.00` |
| `Live` | `Short` | `0.7005` | 4,610,000.00 USD | 28,020.00 USD | 0.00 USD | `+96.59%` | `40,000.00` |
| `Live` | `Short` | `0.7015` | 5,400,000.00 USD | 794,240.00 USD | 0.00 USD | `+96.87%` | `1,132,197.00` |
| `Live` | `Short` | `0.7095` | 5,410,000.00 USD | 4,190.00 USD | 0.00 USD | `+99.11%` | `5,899.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 1,180,000.00 USD | 0.00 USD | 198.45 USD | `-73.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 1,180,000.00 USD | 0.00 USD | 330.26 USD | `-60.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 1,180,000.00 USD | 0.00 USD | 6,100.00 USD | `-49.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,170,000.00 USD | 0.00 USD | 1,750.00 USD | `-42.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,170,000.00 USD | 0.00 USD | 2,220.00 USD | `-40.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,170,000.00 USD | 0.00 USD | 121.70 USD | `-35.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,170,000.00 USD | 0.00 USD | 705.61 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 1,170,000.00 USD | 0.00 USD | 159.20 USD | `-33.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,170,000.00 USD | 0.00 USD | 1,200.00 USD | `-32.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,170,000.00 USD | 0.00 USD | 127.51 USD | `-32.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,170,000.00 USD | 0.00 USD | 1,850.00 USD | `-29.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 1,170,000.00 USD | 0.00 USD | 41,500.00 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 1,120,000.00 USD | 0.00 USD | 1,920.00 USD | `-28.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 1,120,000.00 USD | 0.00 USD | 664.01 USD | `-26.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 1,120,000.00 USD | 0.00 USD | 954.98 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 1,120,000.00 USD | 0.00 USD | 103.56 USD | `-26.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 1,120,000.00 USD | 0.00 USD | 695.50 USD | `-24.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 1,120,000.00 USD | 0.00 USD | 1,630.00 USD | `-24.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 1,120,000.00 USD | 0.00 USD | 1,470.00 USD | `-24.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 1,120,000.00 USD | 0.00 USD | 101.94 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 1,120,000.00 USD | 0.00 USD | 3,260.00 USD | `-22.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 1,110,000.00 USD | 0.00 USD | 2,550.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 1,110,000.00 USD | 0.00 USD | 229.92 USD | `-20.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 1,110,000.00 USD | 0.00 USD | 8,010.00 USD | `-19.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 1,100,000.00 USD | 0.00 USD | 11,610.00 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 1,090,000.00 USD | 0.00 USD | 111.19 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 1,090,000.00 USD | 0.00 USD | 326.86 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 1,090,000.00 USD | 0.00 USD | 2,710.00 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 1,090,000.00 USD | 0.00 USD | 335.56 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 1,090,000.00 USD | 0.00 USD | 919.50 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 1,090,000.00 USD | 0.00 USD | 193.11 USD | `-13.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 1,090,000.00 USD | 0.00 USD | 15,150.00 USD | `-13.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 1,070,000.00 USD | 0.00 USD | 147.32 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 1,070,000.00 USD | 0.00 USD | 12,200.00 USD | `-12.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 1,060,000.00 USD | 0.00 USD | 6,530.00 USD | `-12.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 1,050,000.00 USD | 0.00 USD | 524,570.00 USD | `-12.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 528,430.00 USD | 0.00 USD | 1,270.00 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 527,160.00 USD | 0.00 USD | 53,690.00 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 473,480.00 USD | 0.00 USD | 1,540.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 471,940.00 USD | 0.00 USD | 6,100.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 465,840.00 USD | 0.00 USD | 850.90 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 464,990.00 USD | 0.00 USD | 1,040.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 463,950.00 USD | 0.00 USD | 6,220.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 457,730.00 USD | 0.00 USD | 10,000.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 447,730.00 USD | 0.00 USD | 43,570.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 404,160.00 USD | 0.00 USD | 131.90 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 404,030.00 USD | 0.00 USD | 4,710.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 399,320.00 USD | 0.00 USD | 3,220.00 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 396,100.00 USD | 0.00 USD | 63,670.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 332,430.00 USD | 0.00 USD | 6,130.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 326,300.00 USD | 0.00 USD | 6,770.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 319,530.00 USD | 0.00 USD | 996.01 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 318,530.00 USD | 0.00 USD | 2,570.00 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 315,960.00 USD | 0.00 USD | 949.53 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 315,010.00 USD | 0.00 USD | 100.11 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 314,910.00 USD | 0.00 USD | 135.99 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 314,770.00 USD | 0.00 USD | 1,010.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 313,760.00 USD | 0.00 USD | 5,640.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 308,130.00 USD | 0.00 USD | 174,860.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 133,270.00 USD | 0.00 USD | 34,710.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 98,550.00 USD | 0.00 USD | 32,490.00 USD | `-5.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 66,070.00 USD | 0.00 USD | 157.74 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 65,910.00 USD | 0.00 USD | 3,380.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 62,530.00 USD | 0.00 USD | 3,870.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 58,660.00 USD | 0.00 USD | 13,710.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 44,950.00 USD | 0.00 USD | 359.28 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 44,590.00 USD | 0.00 USD | 828.18 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 43,760.00 USD | 0.00 USD | 1,950.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 41,810.00 USD | 0.00 USD | 3,980.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 37,840.00 USD | 0.00 USD | 555.44 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 37,280.00 USD | 0.00 USD | 1,020.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3485` | 36,260.00 USD | 0.00 USD | 305.29 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3495` | 35,950.00 USD | 0.00 USD | 8,090.00 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 27,860.00 USD | 0.00 USD | 2,430.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3515` | 25,430.00 USD | 0.00 USD | 3,810.00 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3525` | 21,620.00 USD | 0.00 USD | 19,380.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3535` | 2,230.00 USD | 0.00 USD | 494.90 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3545` | 1,740.00 USD | 0.00 USD | 769.97 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3555` | 969.45 USD | 0.00 USD | 969.45 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 39,430.00 USD | 39,430.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 79,820.00 USD | 40,390.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 83,130.00 USD | 3,310.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 84,160.00 USD | 1,030.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 87,100.00 USD | 2,940.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 88,210.00 USD | 1,110.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 88,430.00 USD | 216.65 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 91,810.00 USD | 3,380.00 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 102,940.00 USD | 11,140.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 114,120.00 USD | 11,170.00 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 123,390.00 USD | 9,270.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 123,710.00 USD | 321.70 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 138,040.00 USD | 14,330.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 143,110.00 USD | 5,070.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 143,280.00 USD | 174.60 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 143,390.00 USD | 107.28 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 143,830.00 USD | 439.61 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 144,270.00 USD | 437.79 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 145,440.00 USD | 1,170.00 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 145,620.00 USD | 182.60 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 152,070.00 USD | 6,450.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 152,350.00 USD | 275.17 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 152,920.00 USD | 569.25 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 158,890.00 USD | 5,980.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 159,150.00 USD | 257.89 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 160,120.00 USD | 963.52 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 161,090.00 USD | 972.17 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 162,880.00 USD | 1,790.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 163,580.00 USD | 702.27 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 164,690.00 USD | 1,110.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 164,870.00 USD | 181.04 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 165,230.00 USD | 352.11 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 165,380.00 USD | 155.03 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 165,660.00 USD | 276.40 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 165,780.00 USD | 126.24 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 168,190.00 USD | 2,400.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 169,200.00 USD | 1,010.00 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 171,210.00 USD | 2,010.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 224,090.00 USD | 52,880.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 224,950.00 USD | 864.28 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 228,870.00 USD | 3,920.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 308,200.00 USD | 79,330.00 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 309,400.00 USD | 1,200.00 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 310,600.00 USD | 1,200.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 310,740.00 USD | 138.07 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 312,010.00 USD | 1,270.00 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 312,340.00 USD | 331.63 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 312,650.00 USD | 313.54 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 312,840.00 USD | 186.70 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 313,160.00 USD | 325.75 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 313,460.00 USD | 299.19 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 352,040.00 USD | 38,580.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 352,210.00 USD | 170.69 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 352,340.00 USD | 135.59 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 353,730.00 USD | 1,390.00 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 359,070.00 USD | 5,340.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 439,840.00 USD | 80,770.00 USD | 0.00 USD | `+37.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 440,010.00 USD | 169.22 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 440,730.00 USD | 724.89 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 451,890.00 USD | 11,150.00 USD | 0.00 USD | `+40.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 453,810.00 USD | 1,930.00 USD | 0.00 USD | `+41.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 453,950.00 USD | 135.02 USD | 0.00 USD | `+48.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 454,190.00 USD | 240.85 USD | 0.00 USD | `+76.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 455,290.00 USD | 1,100.00 USD | 0.00 USD | `+77.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 468,900.00 USD | 13,610.00 USD | 0.00 USD | `+89.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 470,740.00 USD | 1,840.00 USD | 0.00 USD | `+90.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 471,730.00 USD | 991.76 USD | 0.00 USD | `+91.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 472,850.00 USD | 1,130.00 USD | 0.00 USD | `+92.38%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2923` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD |
| `7D` | `0.2947` | 24,230,000.00 USD | 0.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD |
| `7D` | `0.2953` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD |
| `7D` | `0.2959` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 23,950,000.00 USD | 0.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD |
| `7D` | `0.2971` | 23,720,000.00 USD | 0.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD |
| `7D` | `0.2977` | 23,460,000.00 USD | 0.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD |
| `7D` | `0.2983` | 23,350,000.00 USD | 0.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `7D` | `0.2989` | 23,130,000.00 USD | 0.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD |
| `7D` | `0.2995` | 22,980,000.00 USD | 0.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD |
| `1D` | `0.3001` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3007` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD |
| `7D` | `0.3007` | 22,970,000.00 USD | 0.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3019` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3031` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD |
| `1D` | `0.3049` | 21,160,000.00 USD | 0.00 USD | 21,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3049` | 22,930,000.00 USD | 0.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3055` | 21,080,000.00 USD | 0.00 USD | 21,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 21,010,000.00 USD | 0.00 USD | 21,010,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3067` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 22,810,000.00 USD | 0.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3073` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3073` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 22,790,000.00 USD | 0.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3085` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3085` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3103` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 22,660,000.00 USD | 0.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `7D` | `0.3109` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3121` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 20,710,000.00 USD | 0.00 USD | 20,710,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD |
| `7D` | `0.3127` | 22,360,000.00 USD | 0.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3133` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD |
| `7D` | `0.3139` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3145` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3145` | 22,330,000.00 USD | 0.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3151` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 22,020,000.00 USD | 0.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3157` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD |
| `7D` | `0.3157` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3163` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD |
| `7D` | `0.3163` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD |
| `1D` | `0.3169` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 84,050.00 USD | 16,200.00 USD | 38,410.00 USD |
| `7D` | `0.3169` | 20,330,000.00 USD | 0.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD |
| `1D` | `0.3175` | 20,300,000.00 USD | 0.00 USD | 20,300,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD |
| `7D` | `0.3175` | 19,470,000.00 USD | 0.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD |
| `1D` | `0.3181` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD |
| `7D` | `0.3181` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD |
| `1D` | `0.3187` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD |
| `7D` | `0.3187` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3193` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `7D` | `0.3193` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3199` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 17,520,000.00 USD | 0.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3205` | 19,350,000.00 USD | 0.00 USD | 19,350,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD |
| `7D` | `0.3205` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3211` | 19,050,000.00 USD | 0.00 USD | 19,050,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD |
| `7D` | `0.3211` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3217` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3217` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3223` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD |
| `7D` | `0.3223` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3229` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 140,560.00 USD | 81,070.00 USD | 205,050.00 USD |
| `7D` | `0.3229` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD |
| `1D` | `0.3235` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 129,720.00 USD | 77,760.00 USD | 168,760.00 USD |
| `7D` | `0.3235` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD |
| `1D` | `0.3241` | 17,710,000.00 USD | 0.00 USD | 17,710,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD |
| `7D` | `0.3241` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD |
| `1D` | `0.3247` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD |
| `7D` | `0.3247` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3253` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD |
| `7D` | `0.3253` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3259` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3265` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD |
| `7D` | `0.3265` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3271` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD |
| `7D` | `0.3271` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3277` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3283` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD |
| `7D` | `0.3283` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3289` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3295` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `7D` | `0.3301` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3307` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD |
| `7D` | `0.3307` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3313` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD |
| `7D` | `0.3313` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3319` | 12,500,000.00 USD | 0.00 USD | 12,500,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD |
| `7D` | `0.3319` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3325` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD |
| `7D` | `0.3325` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD |
| `1D` | `0.3331` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3331` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD |
| `1D` | `0.3337` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD |
| `7D` | `0.3337` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD |
| `1D` | `0.3343` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3343` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `1D` | `0.3349` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD |
| `7D` | `0.3349` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3355` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD |
| `1D` | `0.3361` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 177,350.00 USD | 81,810.00 USD | 65,250.00 USD |
| `7D` | `0.3361` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3367` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 237,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3367` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3373` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD |
| `7D` | `0.3373` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3379` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 514,160.00 USD | 67,660.00 USD | 0.00 USD |
| `7D` | `0.3379` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3385` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD |
| `7D` | `0.3385` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3391` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD |
| `1D` | `0.3397` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD |
| `7D` | `0.3397` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD |
| `1D` | `0.3403` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD |
| `7D` | `0.3403` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3409` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD |
| `7D` | `0.3409` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD |
| `1D` | `0.3415` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD |
| `1D` | `0.3421` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD |
| `1D` | `0.3427` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 262,640.00 USD | 93,060.00 USD | 187,820.00 USD |
| `7D` | `0.3427` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3433` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 0.00 USD | 162,950.00 USD | 176,350.00 USD |
| `1D` | `0.3439` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 0.00 USD | 34,460.00 USD | 392,630.00 USD |
| `1D` | `0.3445` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 217,030.00 USD |
| `7D` | `0.3445` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3451` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 0.00 USD | 46,510.00 USD | 229,860.00 USD |
| `7D` | `0.3451` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3457` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD |
| `1D` | `0.3469` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD |
| `7D` | `0.3469` | 699,440.00 USD | 0.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD |
| `1D` | `0.3475` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD |
| `7D` | `0.3481` | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `7D` | `0.3485` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3487` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD |
| `1D` | `0.3499` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD |
| `1D` | `0.3505` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD |
| `1D` | `0.3511` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD |
| `1D` | `0.3517` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 221,620.00 USD | 0.00 USD | 434,060.00 USD |
| `1D` | `0.3523` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 459,710.00 USD |
| `7D` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD |
| `1D` | `0.3541` | 704,710.00 USD | 0.00 USD | 704,710.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD |
| `7D` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 0.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3544` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3547` | 534,120.00 USD | 534,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD |
| `1D` | `0.3553` | 653,810.00 USD | 653,810.00 USD | 0.00 USD | 0.00 USD | 119,690.00 USD | 0.00 USD |
| `1D` | `0.3559` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD |
| `1D` | `0.3571` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 3,220.00 USD | 163,630.00 USD | 578,320.00 USD |
| `1D` | `0.3577` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3583` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD |
| `7D` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3589` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 1,810.00 USD | 212,630.00 USD | 400,320.00 USD |
| `7D` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD |
| `1D` | `0.3595` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 199,420.00 USD | 163,620.00 USD | 0.00 USD |
| `7D` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3601` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD |
| `7D` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD |
| `7D` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3613` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD |
| `7D` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD |
| `1D` | `0.3619` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `1D` | `0.3625` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3631` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3637` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD |
| `1D` | `0.3643` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD |
| `7D` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3649` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD |
| `7D` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3655` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD |
| `7D` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3661` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 259,500.00 USD | 23,260.00 USD | 0.00 USD |
| `7D` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3667` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD |
| `7D` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3673` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD |
| `7D` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3679` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD |
| `7D` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3685` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD |
| `7D` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD |
| `1D` | `0.3691` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD |
| `7D` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD |
| `1D` | `0.3697` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD |
| `7D` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD |
| `1D` | `0.3703` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD |
| `1D` | `0.3709` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD |
| `7D` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3715` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD |
| `7D` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3721` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD |
| `7D` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3727` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD |
| `7D` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3733` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3739` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD |
| `7D` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3745` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD |
| `7D` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3751` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD |
| `1D` | `0.3757` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD |
| `7D` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3763` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3769` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD |
| `7D` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3775` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3781` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD |
| `7D` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3787` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD |
| `7D` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3793` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD |
| `7D` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3799` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3805` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD |
| `7D` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3823` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD |
| `7D` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3829` | 18,660,000.00 USD | 18,660,000.00 USD | 0.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD |
| `1D` | `0.3835` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 850.22 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3847` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 899.18 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3853` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3865` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD |
| `7D` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `1D` | `0.3871` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3877` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD |
| `7D` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3883` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3895` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD |
| `7D` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3907` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `1D` | `0.3913` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3919` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3925` | 19,390,000.00 USD | 19,390,000.00 USD | 0.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD |
| `7D` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `1D` | `0.3931` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `1D` | `0.3937` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD |
| `7D` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `1D` | `0.3943` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD |
| `7D` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `1D` | `0.3949` | 19,900,000.00 USD | 19,900,000.00 USD | 0.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD |
| `7D` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD |
| `1D` | `0.3955` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD |
| `7D` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD |
| `1D` | `0.3961` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD |
| `7D` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD |
| `1D` | `0.3967` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD |
| `7D` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD |
| `1D` | `0.3973` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD |
| `7D` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `1D` | `0.3979` | 20,860,000.00 USD | 20,860,000.00 USD | 0.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD |
| `7D` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD |
| `1D` | `0.3985` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD |
| `7D` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `1D` | `0.3991` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `7D` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD |
| `1D` | `0.3997` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD |
| `1D` | `0.4003` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD |
| `7D` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `1D` | `0.4009` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD |
| `7D` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD |
| `1D` | `0.4027` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.4045` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `411.29M` | Total OI Tokens: `1,156,551,051.4 TRX`
  * 1h OI Change: `+0.35%` | 4h OI Change: `+2.44%` | 24h OI Change: `+41.89%`
  * Exchange Breakdown: Binance=`115.86M` | Bybit=`85.62M` | OKX=`25.40M` | Hyperliquid=`19.98M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-782.99K` | Last 24h: `-591.71K` | Last 3d: `-625.30K` | Last 7d: `-857.35K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.3669%` | **USDT OKX** | `-0.8025%` |
| **USDT Bybit** | `-0.1863%` | **USDT KuCoin** | `-0.0269%` |
| **USDT MEXC** | `-0.3691%` | **USDT BingX** | `-0.5000%` |
| **USDT Gate** | `-0.2046%` | **USDT Bitget** | `-0.3949%` |
| **CoinM Binance** | `-0.5999%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `47.57%` | `52.43%` | `0.91` | 7,680,000.00 USD |
| `15M` | `Binance` | `50.99%` | `49.01%` | `1.04` | 3,240,000.00 USD |
| `15M` | `OKX` | `43.24%` | `56.76%` | `0.76` | 1,160,000.00 USD |
| `15M` | `Bybit` | `44.1%` | `55.9%` | `0.79` | 1,090,000.00 USD |
| `15M` | `KuCoin` | `50.8%` | `49.2%` | `1.03` | 175,130.00 USD |
| `15M` | `Gate` | `30.91%` | `69.09%` | `0.45` | 196,620.00 USD |
| `15M` | `Bitget` | `34.58%` | `65.42%` | `0.53` | 100,590.00 USD |
| `15M` | `BingX` | `49.09%` | `50.91%` | `0.96` | 36,930.00 USD |
| `15M` | `MEXC` | `41.39%` | `58.61%` | `0.71` | 314,880.00 USD |
| `15M` | `Bitunix` | `52.3%` | `47.7%` | `1.10` | 91,570.00 USD |
| `15M` | `Hyperliquid` | `67.27%` | `32.73%` | `2.06` | 625,430.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.75%` | `50.25%` | `0.99` | 80,740.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `30.32%` | `69.68%` | `0.44` | 520,170.00 USD |
| `15M` | `HTX` | `25.52%` | `74.48%` | `0.34` | 31,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `54.8%` | `45.2%` | `1.21` | 1,880.00 USD |
| `15M` | `Aster` | `57.1%` | `42.9%` | `1.33` | 9,500.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `93.64%` | `6.36%` | `14.72` | 6,250.00 USD |
| `15M` | `Whale Positions` | `50.99%` | `49.01%` | `1.04` | 3,240,000.00 USD |
| `15M` | `Global Accounts` | `47.57%` | `52.43%` | `0.91` | 7,680,000.00 USD |
| `1H` | `TRX` | `49.07%` | `50.93%` | `0.96` | 72,690,000.00 USD |
| `1H` | `Binance` | `51.37%` | `48.63%` | `1.06` | 27,320,000.00 USD |
| `1H` | `OKX` | `48.36%` | `51.64%` | `0.94` | 16,140,000.00 USD |
| `1H` | `Bybit` | `42.97%` | `57.03%` | `0.75` | 6,010,000.00 USD |
| `1H` | `KuCoin` | `48.18%` | `51.82%` | `0.93` | 374,330.00 USD |
| `1H` | `Gate` | `45.1%` | `54.9%` | `0.82` | 9,010,000.00 USD |
| `1H` | `Bitget` | `41.08%` | `58.92%` | `0.70` | 1,520,000.00 USD |
| `1H` | `BingX` | `21.55%` | `78.45%` | `0.27` | 3,280,000.00 USD |
| `1H` | `MEXC` | `54.6%` | `45.4%` | `1.20` | 2,090,000.00 USD |
| `1H` | `Bitunix` | `49.14%` | `50.86%` | `0.97` | 2,760,000.00 USD |
| `1H` | `Hyperliquid` | `65.49%` | `34.51%` | `1.90` | 1,170,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.11%` | `50.89%` | `0.97` | 266,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 46,580.00 USD |
| `1H` | `WhiteBIT` | `39.76%` | `60.24%` | `0.66` | 543,430.00 USD |
| `1H` | `HTX` | `51.25%` | `48.75%` | `1.05` | 1,370,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.28%` | `54.72%` | `0.83` | 172,630.00 USD |
| `1H` | `Aster` | `47.27%` | `52.73%` | `0.90` | 558,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `77.39%` | `22.61%` | `3.42` | 33,490.00 USD |
| `1H` | `Whale Positions` | `51.37%` | `48.63%` | `1.06` | 27,320,000.00 USD |
| `1H` | `Global Accounts` | `49.07%` | `50.93%` | `0.96` | 72,690,000.00 USD |
| `4H` | `TRX` | `51.47%` | `48.53%` | `1.06` | 339,930,000.00 USD |
| `4H` | `Binance` | `52.1%` | `47.9%` | `1.09` | 142,610,000.00 USD |
| `4H` | `OKX` | `51.74%` | `48.26%` | `1.07` | 49,930,000.00 USD |
| `4H` | `Bybit` | `52.01%` | `47.99%` | `1.08` | 57,630,000.00 USD |
| `4H` | `KuCoin` | `48.02%` | `51.98%` | `0.92` | 3,790,000.00 USD |
| `4H` | `Gate` | `48.8%` | `51.2%` | `0.95` | 14,430,000.00 USD |
| `4H` | `Bitget` | `55.84%` | `44.16%` | `1.26` | 8,800,000.00 USD |
| `4H` | `BingX` | `46.04%` | `53.96%` | `0.85` | 4,040,000.00 USD |
| `4H` | `MEXC` | `49.71%` | `50.29%` | `0.99` | 5,260,000.00 USD |
| `4H` | `Bitunix` | `49.07%` | `50.93%` | `0.96` | 5,440,000.00 USD |
| `4H` | `Hyperliquid` | `54.54%` | `45.46%` | `1.20` | 14,790,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.01%` | `48.99%` | `1.04` | 5,890,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `40.6%` | `59.4%` | `0.68` | 16,550,000.00 USD |
| `4H` | `HTX` | `48.61%` | `51.39%` | `0.95` | 938,620.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `65.81%` | `34.19%` | `1.92` | 6,350,000.00 USD |
| `4H` | `Aster` | `34.09%` | `65.91%` | `0.52` | 1,250,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.55%` | `51.45%` | `0.94` | 2,230,000.00 USD |
| `4H` | `Whale Positions` | `52.1%` | `47.9%` | `1.09` | 142,610,000.00 USD |
| `4H` | `Global Accounts` | `51.47%` | `48.53%` | `1.06` | 339,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3547` | `0.3546` | `0.3547` | `0.3577` | `0.3519` | 8,993,332.14 USD | 4,558,287.41 USD | 4,435,044.74 USD | 123,242.67 USD | `+1.37%` | `6B / 24S` |
| `0:00 UTC` | `0.3500` | `0.3513` | `0.3500` | `0.3535` | `0.3498` | 9,846,103.40 USD | 5,465,919.25 USD | 4,380,184.15 USD | 1,085,735.10 USD | `+11.03%` | `32B / 21S` |
| `5:00 UTC` | `0.3527` | `0.3554` | `0.3527` | `0.3583` | `0.3516` | 6,386,124.75 USD | 3,796,524.00 USD | 2,589,600.75 USD | 1,206,923.24 USD | `+18.90%` | `28B / 5S` |
| `0:00 UTC` | `0.3580` | `0.3582` | `0.3580` | `0.3596` | `0.3560` | 6,263,390.39 USD | 3,238,511.83 USD | 3,024,878.56 USD | 213,633.28 USD | `+3.41%` | `14B / 19S` |
| `5:00 UTC` | `0.3600` | `0.3588` | `0.3600` | `0.3608` | `0.3547` | 5,984,969.75 USD | 3,428,902.99 USD | 2,556,066.76 USD | 872,836.23 USD | `+14.58%` | `13B / 17S` |
| `0:00 UTC` | `0.3569` | `0.3560` | `0.3569` | `0.3597` | `0.3516` | 6,905,900.10 USD | 3,419,045.32 USD | 3,486,854.78 USD | -67,809.47 USD | `-0.98%` | `7B / 10S` |
| `5:00 UTC` | `0.3569` | `0.3557` | `0.3569` | `0.3573` | `0.3538` | 3,113,295.36 USD | 1,603,340.17 USD | 1,509,955.19 USD | 93,384.98 USD | `+3.00%` | `23B / 15S` |
| `0:00 UTC` | `0.3561` | `0.3570` | `0.3561` | `0.3589` | `0.3549` | 2,900,250.45 USD | 1,473,071.99 USD | 1,427,178.46 USD | 45,893.52 USD | `+1.58%` | `30B / 17S` |
| `5:00 UTC` | `0.3597` | `0.3579` | `0.3597` | `0.3599` | `0.3549` | 3,146,983.44 USD | 1,605,139.22 USD | 1,541,844.22 USD | 63,295.00 USD | `+2.01%` | `14B / 4S` |
| `0:00 UTC` | `0.3573` | `0.3576` | `0.3573` | `0.3587` | `0.3565` | 2,035,970.72 USD | 1,016,958.58 USD | 1,019,012.14 USD | -2,053.56 USD | `-0.10%` | `8B / 13S` |

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
| `5m` | 308,360.00 USD | 30,090.00 USD | **`ACCUMULATION`** |
| `15m` | 449,580.00 USD | -189,960.00 USD | **`ACCUMULATION`** |
| `30m` | 799,470.00 USD | -102,450.00 USD | **`ACCUMULATION`** |
| `1h` | 1,270,000.00 USD | -608,720.00 USD | **`ACCUMULATION`** |
| `2h` | 5,850,000.00 USD | 4,100,000.00 USD | **`ACCUMULATION`** |
| `4h` | 5,810,000.00 USD | 12,190,000.00 USD | **`ACCUMULATION`** |
| `6h` | 8,670,000.00 USD | 12,940,000.00 USD | **`ACCUMULATION`** |
| `8h` | 6,970,000.00 USD | 12,960,000.00 USD | **`ACCUMULATION`** |
| `12h` | 7,390,000.00 USD | 12,750,000.00 USD | **`ACCUMULATION`** |
| `24h` | 8,650,000.00 USD | 14,580,000.00 USD | **`ACCUMULATION`** |
| `1w` | 1,670,000.00 USD | 12,180,000.00 USD | **`ACCUMULATION`** |
| `30d` | -16,490,000.00 USD | 15,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+308.36K` | 15m=`+449.58K` | 1h=`+1.27M` | 24h=`+8.65M`
* Futures Capital Netflows: 5m=`+30.09K` | 15m=`-189.96K` | 1h=`-608.72K` | 24h=`+14.58M`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3451` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3335` (Risk Distance: `0.0116` pts)
  * +2.5R Take Profit: `0.3742`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3572` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3688` (Risk Distance: `0.0116` pts)
  * +2.5R Take Profit: `0.3281`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3587`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
