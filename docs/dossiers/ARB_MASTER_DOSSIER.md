# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 14:14:31 IST` (`2026-10-30 08:44:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1700` | **Live Ask Quote**: `0.1700` | **Mid Price**: `0.1700`
- **Spread Points**: `0.000034` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
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
  * Session VWAP: `0.1700` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1712` | Lower -3.00σ Band: `0.1688`
  * Upper +2.51σ Band: `0.1710` | Lower -2.51σ Band: `0.1691`
  * Upper +2.01σ Band: `0.1707` | Lower -2.01σ Band: `0.1693`
  * Upper +2.00σ Band: `0.1707` | Lower -2.00σ Band: `0.1693`
  * Upper +1.28σ Band: `0.1705` | Lower -1.28σ Band: `0.1695`
  * Upper +1.00σ Band: `0.1704` | Lower -1.00σ Band: `0.1697`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1700` | EMA-20=`0.1700` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1700` (Slope: `+0.0000`) | EMA-100=`0.1700`
  * Institutional Anchors: EMA-144=`0.1700` | EMA-200=`0.1700` (Slope: `+0.0000`) | EMA-233=`0.1700`
- **Range Boundaries**: 24H High=`0.1717` | 24H Low=`0.1683` | Weekly High=`0.1734` | Weekly Low=`0.1666`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1705` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.1700` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.1695` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1707` | POC=`0.1700` | VAL=`0.1693`
  * Prior Day Extremes: PDH=`0.1710` | PDL=`0.1690` | PDC=`0.1700`
  * Monday Range Blueprint: High=`0.1709` | Mid=`0.1700` | Low=`0.1692`
  * Developing Weekly Value Area: Weekly VAH=`0.1714` | Weekly POC=`0.1700` | Weekly VAL=`0.1687`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1704` | Low=`0.1697`
  * London Session (08:00-16:00 UTC): High=`0.1707` | Low=`0.1693`
  * New York Session (13:00-21:00 UTC): High=`0.1710` | Low=`0.1690`
  * Initial Balance (First Hour): IB High=`0.1705` | IB Low=`0.1695`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1693` - `0.1707`
  * Optimal Trade Entry (OTE 0.705): `0.1704`
  * Structural Invalidation Anchor (0.786): `0.1714`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1637` | `0.1638` | `0.1632` | `0.1634` | `1,501,252` | 245,365.64 USD | -28,187.66 USD | `-11.49%` | -7,527,695.61 USD | `-0.61` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1634` | `0.1638` | `0.1632` | `0.1635` | `973,399` | 159,217.24 USD | 9,809.82 USD | `+6.16%` | -7,517,885.79 USD | `-0.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1635` | `0.1635` | `0.1631` | `0.1633` | `474,071` | 77,361.09 USD | -43,756.91 USD | `-56.56%` | -7,561,642.70 USD | `-0.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1650` | `0.1657` | `0.1639` | `0.1644` | `14,613,160` | 2,406,571.88 USD | -3,221.81 USD | `-0.13%` | -7,283,742.36 USD | `-0.04` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1644` | `0.1647` | `0.1634` | `0.1637` | `4,760,505` | 780,398.32 USD | -215,765.59 USD | `-27.65%` | -7,499,507.95 USD | `-0.84` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1637` | `0.1638` | `0.1631` | `0.1633` | `2,948,985` | 481,986.98 USD | -62,104.65 USD | `-12.89%` | -7,561,612.60 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1639` | `0.1665` | `0.1630` | `0.1646` | `21,337,794` | 3,509,114.39 USD | 260,486.52 USD | `+7.42%` | -7,718,945.15 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1646` | `0.1657` | `0.1633` | `0.1649` | `22,323,310` | 3,671,078.25 USD | 439,965.29 USD | `+11.98%` | -7,278,979.86 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1650` | `0.1657` | `0.1631` | `0.1633` | `22,322,386` | 3,668,914.18 USD | -281,122.14 USD | `-7.66%` | -7,560,102.00 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1631` | `0.1633` | `22,322,386` | 3,668,914.18 USD | -281,122.14 USD | `-7.66%` | -7,128,636.77 USD | `+0.75` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1631` | `0.1633` | `22,322,386` | 3,668,914.18 USD | -281,122.14 USD | `-7.66%` | -7,128,636.77 USD | `+0.75` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1700`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1633` | 5,642.04 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 5.64K USD at 0.1633 USD [API] | `2026-10-29 08:09:23` |
| `ANNOUNCEMENT` | `INFO` | `0.1625` | 8,564.49 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.56K USD at 0.1625 USD [API] | `2026-10-29 07:16:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1625` | 4,182.60 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.18K USD at 0.1625 USD [API] | `2026-10-29 07:16:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1684` | 5,823.61 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 5.82K USD at 0.1684 USD [API] | `2026-10-29 10:57:33` |
| `ANNOUNCEMENT` | `INFO` | `0.1770` | 709.13 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.71K USD at 0.1770 USD [API] | `2026-10-28 20:01:24` |
| `ANNOUNCEMENT` | `INFO` | `0.1730` | 1,220.98 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.22K USD at 0.1730 USD [API] | `2026-10-26 08:46:55` |
| `ANNOUNCEMENT` | `INFO` | `0.2105` | 227.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.23K USD at 0.2105 USD [API] | `2026-09-19 03:39:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1708` | 6,077.79 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 6.08K USD at 0.1708 USD [API] | `2026-10-29 13:59:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1629` (Vol: 153,600.00 USD, Dist: `+4.92%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--2.69%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 7D Horizon: Short MP=`0.1791` (Vol: 196,100.00 USD, Dist: `+15.75%`) | Long MP=`0.1511` (Vol: 221,900.00 USD, Dist: `--2.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0365` | 3,650.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 124.33 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 622.79 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 184,900.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,760.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 718.35 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 2,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 1,110.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 1,210.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 6,570.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 4,260.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 465.46 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,150.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 466.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 63,580.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 19,130.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,930.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 4,830.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 482.15 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 895.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,900.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,750.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 10,110.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 3,210.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 7,670.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 3,860.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 8,870.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 8,910.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,640.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 450.48 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,820.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 129,840.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 2,010.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 6,230.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 7,420.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 2,750.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,220.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,430.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 377.05 USD | 989,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 348.01 USD | 989,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 16,720.00 USD | 988,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 972,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,010.00 USD | 962,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 18,760.00 USD | 960,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 9,040,000.00 USD | 9,040,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 18,320.00 USD | 941,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 9,020,000.00 USD | 9,020,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 9,000,000.00 USD | 9,000,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,980,000.00 USD | 8,980,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 923,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,940,000.00 USD | 8,940,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,910,000.00 USD | 8,910,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,880,000.00 USD | 8,880,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 59,240.00 USD | 918,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,870,000.00 USD | 8,870,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,840,000.00 USD | 8,840,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 30,990.00 USD | 859,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,800,000.00 USD | 8,800,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,740,000.00 USD | 8,740,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,710,000.00 USD | 8,710,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,680,000.00 USD | 8,680,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 2,830.00 USD | 828,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,660,000.00 USD | 8,660,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,620,000.00 USD | 8,620,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,600,000.00 USD | 8,600,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 8,920.00 USD | 825,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 8,580,000.00 USD | 8,580,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 8,560,000.00 USD | 8,560,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 816,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 8,520,000.00 USD | 8,520,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 8,510,000.00 USD | 8,510,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 6,100.00 USD | 802,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 8,450,000.00 USD | 8,450,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 9,210.00 USD | 796,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 8,350,000.00 USD | 8,350,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 8,340,000.00 USD | 8,340,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,550.00 USD | 787,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,540.00 USD | 772,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,200.00 USD | 756,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1430` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 257,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 8,290,000.00 USD | 8,290,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 8,260,000.00 USD | 8,260,000.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 238,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1451` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 228,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,850.00 USD | 136,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 5,170,000.00 USD | 5,170,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1466` | 8,220,000.00 USD | 8,220,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1468` | 5,150,000.00 USD | 5,150,000.00 USD | 4,430.00 USD | 1,110.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 8,110,000.00 USD | 8,110,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 5,140,000.00 USD | 5,140,000.00 USD | 7,760.00 USD | 17,450.00 USD | 64,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 8,100,000.00 USD | 8,100,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 5,050,000.00 USD | 5,050,000.00 USD | 43,430.00 USD | 16,470.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 8,070,000.00 USD | 8,070,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 82,880.00 USD | 107,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 4,970,000.00 USD | 4,970,000.00 USD | 49,710.00 USD | 20,650.00 USD | 156,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1478` | 4,740,000.00 USD | 4,740,000.00 USD | 85,250.00 USD | 6,140.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 8,030,000.00 USD | 8,030,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 4,620,000.00 USD | 4,620,000.00 USD | 74,060.00 USD | 13,400.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,760,000.00 USD | 7,760,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 4,530,000.00 USD | 4,530,000.00 USD | 18,610.00 USD | 6,260.00 USD | 124,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 4,380,000.00 USD | 4,380,000.00 USD | 63,600.00 USD | 4,640.00 USD | 71,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,660,000.00 USD | 7,660,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 24,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 4,240,000.00 USD | 4,240,000.00 USD | 9,210.00 USD | 1,840.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 7,450,000.00 USD | 7,450,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1488` | 4,230,000.00 USD | 4,230,000.00 USD | 16,750.00 USD | 1,740.00 USD | 14,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 4,190,000.00 USD | 4,190,000.00 USD | 40,720.00 USD | 15,530.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 7,350,000.00 USD | 7,350,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 4,130,000.00 USD | 4,130,000.00 USD | 6,410.00 USD | 6,010.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 7,220,000.00 USD | 7,220,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 4,100,000.00 USD | 4,100,000.00 USD | 45,060.00 USD | 3,020.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 22,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1496` | 4,040,000.00 USD | 4,040,000.00 USD | 26,530.00 USD | 0.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1496` | 7,150,000.00 USD | 7,150,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1498` | 4,000,000.00 USD | 4,000,000.00 USD | 8,630.00 USD | 4,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,910,000.00 USD | 6,910,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,980,000.00 USD | 3,980,000.00 USD | 5,920.00 USD | 4,820.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1502` | 3,970,000.00 USD | 3,970,000.00 USD | 11,460.00 USD | 13,970.00 USD | 131,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,820,000.00 USD | 6,820,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 3,810,000.00 USD | 3,810,000.00 USD | 84,100.00 USD | 3,920.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,810,000.00 USD | 6,810,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1506` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 1,150.00 USD | 199,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1508` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,670,000.00 USD | 6,670,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 6,130.00 USD | 50,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 6,260,000.00 USD | 6,260,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 3,330,000.00 USD | 3,330,000.00 USD | 5,040.00 USD | 3,900.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 3,320,000.00 USD | 3,320,000.00 USD | 11,720.00 USD | 0.00 USD | 250,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 21,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 3,060,000.00 USD | 3,060,000.00 USD | 7,210.00 USD | 0.00 USD | 139,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,740,000.00 USD | 5,740,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 2,910,000.00 USD | 2,910,000.00 USD | 31,590.00 USD | 8,960.00 USD | 27,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 2,840,000.00 USD | 2,840,000.00 USD | 49,700.00 USD | 4,400.00 USD | 12,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 4,770.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,760,000.00 USD | 2,760,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1526` | 2,720,000.00 USD | 2,720,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1528` | 2,700,000.00 USD | 2,700,000.00 USD | 17,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 2,680,000.00 USD | 2,680,000.00 USD | 12,670.00 USD | 15,770.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1532` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 2,640,000.00 USD | 2,640,000.00 USD | 10,930.00 USD | 0.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 5,270,000.00 USD | 5,270,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,650.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 2,620,000.00 USD | 2,620,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1538` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1540` | 2,590,000.00 USD | 2,590,000.00 USD | 27,770.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 2,550,000.00 USD | 2,550,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1544` | 2,540,000.00 USD | 2,540,000.00 USD | 10,090.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1546` | 2,520,000.00 USD | 2,520,000.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 2,510,000.00 USD | 2,510,000.00 USD | 16,200.00 USD | 12,300.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 2,470,000.00 USD | 2,470,000.00 USD | 8,630.00 USD | 14,430.00 USD | 20,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 1,680.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 2,420,000.00 USD | 2,420,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 2,270.00 USD | 12,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1556` | 2,380,000.00 USD | 2,380,000.00 USD | 7,120.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1556` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1558` | 2,360,000.00 USD | 2,360,000.00 USD | 6,990.00 USD | 11,690.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1562` | 2,340,000.00 USD | 2,340,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1564` | 2,330,000.00 USD | 2,330,000.00 USD | 11,460.00 USD | 38,290.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,860,000.00 USD | 4,860,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,830.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 2,270,000.00 USD | 2,270,000.00 USD | 70,570.00 USD | 1,850.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1568` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,760,000.00 USD | 4,760,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1570` | 2,180,000.00 USD | 2,180,000.00 USD | 27,380.00 USD | 5,080.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 4,480,000.00 USD | 4,480,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 2,040,000.00 USD | 2,040,000.00 USD | 48,950.00 USD | 5,380.00 USD | 82,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1574` | 1,900,000.00 USD | 1,900,000.00 USD | 11,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 4,220,000.00 USD | 4,220,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1576` | 1,890,000.00 USD | 1,890,000.00 USD | 4,460.00 USD | 0.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 4,030,000.00 USD | 4,030,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 1,870,000.00 USD | 1,870,000.00 USD | 30,670.00 USD | 29,200.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1580` | 1,790,000.00 USD | 1,790,000.00 USD | 9,050.00 USD | 6,060.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,880,000.00 USD | 3,880,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1582` | 1,770,000.00 USD | 1,770,000.00 USD | 49,700.00 USD | 14,280.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,590,000.00 USD | 3,590,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 1,690,000.00 USD | 1,690,000.00 USD | 60,550.00 USD | 19,610.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1586` | 1,590,000.00 USD | 1,590,000.00 USD | 18,000.00 USD | 28,750.00 USD | 47,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 3,480,000.00 USD | 3,480,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1588` | 1,500,000.00 USD | 1,500,000.00 USD | 10,670.00 USD | 19,300.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 3,400,000.00 USD | 3,400,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 1,430,000.00 USD | 1,430,000.00 USD | 18,670.00 USD | 8,510.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1592` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 24,520.00 USD | 44,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1592` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1594` | 1,310,000.00 USD | 1,310,000.00 USD | 10,260.00 USD | 20,310.00 USD | 19,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1598` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1600` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 1,250,000.00 USD | 1,250,000.00 USD | 44,810.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1604` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 3,850.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,970,000.00 USD | 2,970,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1606` | 1,180,000.00 USD | 1,180,000.00 USD | 21,600.00 USD | 0.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,580,000.00 USD | 2,580,000.00 USD | 166,880.00 USD | 0.00 USD | 381,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 1,130,000.00 USD | 1,130,000.00 USD | 34,860.00 USD | 7,790.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1610` | 998,950.00 USD | 998,950.00 USD | 71,710.00 USD | 58,400.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 2,030,000.00 USD | 2,030,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1612` | 840,020.00 USD | 840,020.00 USD | 23,810.00 USD | 23,830.00 USD | 25,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,660,000.00 USD | 1,660,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 767,380.00 USD | 767,380.00 USD | 6,760.00 USD | 34,180.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1616` | 720,750.00 USD | 720,750.00 USD | 0.00 USD | 29,840.00 USD | 46,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 910,620.00 USD | 910,620.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1618` | 643,950.00 USD | 643,950.00 USD | 21,220.00 USD | 12,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1619` | 638,790.00 USD | 638,790.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 609,950.00 USD | 609,950.00 USD | 10,990.00 USD | 8,710.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1622` | 559,290.00 USD | 559,290.00 USD | 34,840.00 USD | 5,660.00 USD | 43,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 562,130.00 USD | 562,130.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1624` | 474,930.00 USD | 474,930.00 USD | 63,030.00 USD | 17,020.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 406,910.00 USD | 406,910.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1626` | 366,960.00 USD | 366,960.00 USD | 38,240.00 USD | 20,350.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1628` | 257,440.00 USD | 257,440.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 147,720.00 USD | 147,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1630` | 122,300.00 USD | 122,300.00 USD | 23,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1631` | 70,940.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 98,410.00 USD | 98,410.00 USD | 98,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 17,390.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1636` | 32,260.00 USD | 32,260.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 103,750.00 USD | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 61,950.00 USD | 61,950.00 USD | 0.00 USD | 8,980.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 121,760.00 USD | 121,760.00 USD | 0.00 USD | 9,280.00 USD | 50,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 265,580.00 USD | 265,580.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1666` | 159,460.00 USD | 159,460.00 USD | 0.00 USD | 5,340.00 USD | 32,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 320,830.00 USD | 320,830.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1668` | 178,780.00 USD | 178,780.00 USD | 0.00 USD | 11,890.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1670` | 200,020.00 USD | 200,020.00 USD | 4,600.00 USD | 3,850.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 657,080.00 USD | 657,080.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 284,180.00 USD | 284,180.00 USD | 56,860.00 USD | 3,960.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 770,180.00 USD | 770,180.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 346,260.00 USD | 346,260.00 USD | 20,040.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1676` | 519,380.00 USD | 519,380.00 USD | 82,670.00 USD | 60,390.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,010,000.00 USD | 1,010,000.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 575,070.00 USD | 575,070.00 USD | 26,550.00 USD | 0.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,210,000.00 USD | 1,210,000.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 677,420.00 USD | 677,420.00 USD | 70,670.00 USD | 22,970.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1682` | 818,560.00 USD | 818,560.00 USD | 43,920.00 USD | 31,520.00 USD | 65,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,460,000.00 USD | 1,460,000.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 922,730.00 USD | 922,730.00 USD | 45,340.00 USD | 40,190.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,550,000.00 USD | 1,550,000.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1686` | 1,040,000.00 USD | 1,040,000.00 USD | 19,830.00 USD | 18,520.00 USD | 75,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1688` | 1,110,000.00 USD | 1,110,000.00 USD | 10,760.00 USD | 5,660.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,640,000.00 USD | 1,640,000.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 1,240,000.00 USD | 1,240,000.00 USD | 55,800.00 USD | 29,860.00 USD | 42,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,820,000.00 USD | 1,820,000.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 1,500,000.00 USD | 1,500,000.00 USD | 66,540.00 USD | 86,510.00 USD | 111,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 1,580,000.00 USD | 1,580,000.00 USD | 41,320.00 USD | 23,520.00 USD | 16,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 1,940,000.00 USD | 1,940,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1696` | 1,620,000.00 USD | 1,620,000.00 USD | 23,530.00 USD | 4,640.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,750,000.00 USD | 1,750,000.00 USD | 26,000.00 USD | 57,580.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1700` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 1,810,000.00 USD | 1,810,000.00 USD | 9,960.00 USD | 1,920.00 USD | 40,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 2,240,000.00 USD | 2,240,000.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,850,000.00 USD | 1,850,000.00 USD | 11,790.00 USD | 14,420.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 5,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1706` | 1,920,000.00 USD | 1,920,000.00 USD | 44,560.00 USD | 9,590.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1706` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 2,020,000.00 USD | 2,020,000.00 USD | 26,090.00 USD | 63,220.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 2,110,000.00 USD | 2,110,000.00 USD | 30,670.00 USD | 29,200.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 2,160,000.00 USD | 2,160,000.00 USD | 16,380.00 USD | 21,110.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1712` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 2,180,000.00 USD | 2,180,000.00 USD | 1,800.00 USD | 16,560.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 2,190.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1716` | 2,260,000.00 USD | 2,260,000.00 USD | 19,740.00 USD | 31,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 2,320,000.00 USD | 2,320,000.00 USD | 20,700.00 USD | 20,360.00 USD | 18,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,550,000.00 USD | 2,550,000.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 2,380,000.00 USD | 2,380,000.00 USD | 34,970.00 USD | 2,830.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 2,900,000.00 USD | 2,900,000.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 2,530,000.00 USD | 2,530,000.00 USD | 72,810.00 USD | 25,370.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 2,600,000.00 USD | 2,600,000.00 USD | 8,230.00 USD | 1,570.00 USD | 52,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 3,100,000.00 USD | 3,100,000.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 1,440.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1726` | 2,640,000.00 USD | 2,640,000.00 USD | 10,260.00 USD | 12,580.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 2,660,000.00 USD | 2,660,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 3,410,000.00 USD | 3,410,000.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 2,680,000.00 USD | 2,680,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,550,000.00 USD | 3,550,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 2,680,000.00 USD | 2,680,000.00 USD | 1,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 1,190.00 USD | 9,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1736` | 2,710,000.00 USD | 2,710,000.00 USD | 16,980.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 2,730,000.00 USD | 2,730,000.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 4,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 2,460.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 2,770,000.00 USD | 2,770,000.00 USD | 3,500.00 USD | 0.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1748` | 2,870,000.00 USD | 2,870,000.00 USD | 55,280.00 USD | 2,280.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,750,000.00 USD | 3,750,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 2,900,000.00 USD | 2,900,000.00 USD | 24,790.00 USD | 0.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 2,960,000.00 USD | 2,960,000.00 USD | 30,220.00 USD | 0.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 3,000,000.00 USD | 3,000,000.00 USD | 21,260.00 USD | 8,430.00 USD | 14,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 4,190,000.00 USD | 4,190,000.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 3,060,000.00 USD | 3,060,000.00 USD | 6,850.00 USD | 3,540.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 4,360,000.00 USD | 4,360,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 3,130,000.00 USD | 3,130,000.00 USD | 37,400.00 USD | 14,260.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 3,230,000.00 USD | 3,230,000.00 USD | 20,970.00 USD | 73,590.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,620,000.00 USD | 4,620,000.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 3,350,000.00 USD | 3,350,000.00 USD | 50,470.00 USD | 2,140.00 USD | 60,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 4,960,000.00 USD | 4,960,000.00 USD | 203,430.00 USD | 119,360.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 3,420,000.00 USD | 3,420,000.00 USD | 8,260.00 USD | 25,840.00 USD | 38,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1766` | 3,460,000.00 USD | 3,460,000.00 USD | 7,570.00 USD | 3,150.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,290,000.00 USD | 5,290,000.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1768` | 3,580,000.00 USD | 3,580,000.00 USD | 19,860.00 USD | 70,050.00 USD | 25,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,490,000.00 USD | 5,490,000.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 3,640,000.00 USD | 3,640,000.00 USD | 32,300.00 USD | 12,060.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 3,670,000.00 USD | 3,670,000.00 USD | 4,900.00 USD | 9,310.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,700,000.00 USD | 5,700,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 3,700,000.00 USD | 3,700,000.00 USD | 12,400.00 USD | 14,420.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 5,900,000.00 USD | 5,900,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 3,750,000.00 USD | 3,750,000.00 USD | 22,060.00 USD | 12,480.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1778` | 3,860,000.00 USD | 3,860,000.00 USD | 26,670.00 USD | 70,980.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 6,100,000.00 USD | 6,100,000.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 1,610.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,150,000.00 USD | 6,150,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 10,130.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1784` | 3,940,000.00 USD | 3,940,000.00 USD | 40,030.00 USD | 8,820.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,380,000.00 USD | 6,380,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 921.36 USD | 10,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1786` | 3,980,000.00 USD | 3,980,000.00 USD | 4,570.00 USD | 25,290.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,550,000.00 USD | 6,550,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 4,010,000.00 USD | 4,010,000.00 USD | 9,350.00 USD | 20,220.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1790` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,670,000.00 USD | 6,670,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 3,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,800,000.00 USD | 6,800,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 4,070,000.00 USD | 4,070,000.00 USD | 13,620.00 USD | 34,190.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1796` | 4,110,000.00 USD | 4,110,000.00 USD | 18,470.00 USD | 0.00 USD | 21,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 6,870,000.00 USD | 6,870,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 12,950.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 4,160,000.00 USD | 4,160,000.00 USD | 5,820.00 USD | 2,030.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1802` | 4,200,000.00 USD | 4,200,000.00 USD | 6,120.00 USD | 28,340.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 7,070,000.00 USD | 7,070,000.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 4,220,000.00 USD | 4,220,000.00 USD | 4,010.00 USD | 2,830.00 USD | 7,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 7,120,000.00 USD | 7,120,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1806` | 4,230,000.00 USD | 4,230,000.00 USD | 4,770.00 USD | 0.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1808` | 4,270,000.00 USD | 4,270,000.00 USD | 15,180.00 USD | 22,870.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,270,000.00 USD | 7,270,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 4,290,000.00 USD | 4,290,000.00 USD | 9,360.00 USD | 3,190.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,380,000.00 USD | 7,380,000.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 4,340,000.00 USD | 4,340,000.00 USD | 11,890.00 USD | 33,700.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1814` | 4,370,000.00 USD | 4,370,000.00 USD | 3,830.00 USD | 4,640.00 USD | 14,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,500,000.00 USD | 7,500,000.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1816` | 4,370,000.00 USD | 4,370,000.00 USD | 5,320.00 USD | 1,840.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,610,000.00 USD | 7,610,000.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 8,320.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1820` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 12,390.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,750,000.00 USD | 7,750,000.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 4,430,000.00 USD | 4,430,000.00 USD | 6,150.00 USD | 7,660.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 7,940,000.00 USD | 7,940,000.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 4,440,000.00 USD | 4,440,000.00 USD | 7,970.00 USD | 0.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1826` | 4,450,000.00 USD | 4,450,000.00 USD | 5,300.00 USD | 3,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 8,030,000.00 USD | 8,030,000.00 USD | 68,170.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,130,000.00 USD | 8,130,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,260,000.00 USD | 8,260,000.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,380,000.00 USD | 8,380,000.00 USD | 74,850.00 USD | 26,020.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,560,000.00 USD | 8,560,000.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,630,000.00 USD | 8,630,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,710,000.00 USD | 8,710,000.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,630.00 USD | 13,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1847` | 8,750,000.00 USD | 8,750,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 8,930,000.00 USD | 8,930,000.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,030,000.00 USD | 9,030,000.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,040,000.00 USD | 9,040,000.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 333.88 USD | 14,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,010.00 USD | 18,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 18,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 30,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 257.20 USD | 30,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 474.40 USD | 30,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 31,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2105` | 190.73 USD | 31,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2115` | 4,260.00 USD | 35,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 51,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 92,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 92,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 180,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 180,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 338.64 USD | 181,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 181,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 188,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 204,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 204,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 48,100.00 USD | 252,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 22,840.00 USD | 275,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 275,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 275,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 279,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 26,570.00 USD | 306,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 54,960.00 USD | 361,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 361,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2635` | 182,510.00 USD | 543,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 544,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 557,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 557,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 569,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 569,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2815` | 2,140.00 USD | 571,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2865` | 12,580.00 USD | 584,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 584,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 585,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 290,580.00 USD | 876,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 1,910.00 USD | 877,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3025` | 481.13 USD | 878,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 884,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 885,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 896,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 242.44 USD | 897,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 897,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 1,790,000.00 USD | 0.00 USD | 3,650.00 USD | `-77.88%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,790,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.67%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,790,000.00 USD | 0.00 USD | 110.22 USD | `-74.85%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,790,000.00 USD | 0.00 USD | 170.00 USD | `-74.25%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,790,000.00 USD | 0.00 USD | 124.33 USD | `-70.61%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,790,000.00 USD | 0.00 USD | 109.52 USD | `-70.00%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,790,000.00 USD | 0.00 USD | 622.79 USD | `-68.79%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,790,000.00 USD | 0.00 USD | 184,900.00 USD | `-68.19%` | `3,521,922,800,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,600,000.00 USD | 0.00 USD | 2,760.00 USD | `-66.97%` | `50,592,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,600,000.00 USD | 0.00 USD | 15,650.00 USD | `-65.76%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,580,000.00 USD | 0.00 USD | 718.35 USD | `-65.16%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,580,000.00 USD | 0.00 USD | 2,000.00 USD | `-64.55%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,580,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.94%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,580,000.00 USD | 0.00 USD | 1,210.00 USD | `-63.34%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0645` | 1,580,000.00 USD | 0.00 USD | 6,570.00 USD | `-60.91%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0655` | 1,570,000.00 USD | 0.00 USD | 4,260.00 USD | `-60.31%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,570,000.00 USD | 0.00 USD | 99,790.00 USD | `-59.10%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,470,000.00 USD | 0.00 USD | 465.46 USD | `-58.49%` | `6,795,000,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,470,000.00 USD | 0.00 USD | 976.14 USD | `-57.88%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,470,000.00 USD | 0.00 USD | 2,970.00 USD | `-57.28%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,460,000.00 USD | 0.00 USD | 6,150.00 USD | `-56.67%` | `86,064,300,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,460,000.00 USD | 0.00 USD | 111.58 USD | `-56.07%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,460,000.00 USD | 0.00 USD | 2,440.00 USD | `-55.46%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,450,000.00 USD | 0.00 USD | 466.00 USD | `-54.85%` | `6,255,000,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,450,000.00 USD | 0.00 USD | 63,580.00 USD | `-54.25%` | `842,071,000,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,390,000.00 USD | 0.00 USD | 14,690.00 USD | `-53.64%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,370,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.82%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,370,000.00 USD | 0.00 USD | 19,130.00 USD | `-50.01%` | `231,907,800,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,350,000.00 USD | 0.00 USD | 1,930.00 USD | `-48.19%` | `22,623,800,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,350,000.00 USD | 0.00 USD | 19,460.00 USD | `-47.58%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,330,000.00 USD | 0.00 USD | 4,830.00 USD | `-46.98%` | `55,220,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,320,000.00 USD | 0.00 USD | 482.15 USD | `-46.37%` | `5,448,000,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,320,000.00 USD | 0.00 USD | 895.00 USD | `-45.76%` | `10,000,000,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,320,000.00 USD | 0.00 USD | 113.80 USD | `-44.55%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,320,000.00 USD | 0.00 USD | 2,040.00 USD | `-43.95%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,320,000.00 USD | 0.00 USD | 814.24 USD | `-43.34%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,320,000.00 USD | 0.00 USD | 1,900.00 USD | `-42.73%` | `20,100,000,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,320,000.00 USD | 0.00 USD | 2,750.00 USD | `-42.13%` | `28,821,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,320,000.00 USD | 0.00 USD | 1,600.00 USD | `-41.52%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,310,000.00 USD | 0.00 USD | 10,110.00 USD | `-40.92%` | `103,669,500,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,300,000.00 USD | 0.00 USD | 3,210.00 USD | `-40.31%` | `32,563,800,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,300,000.00 USD | 0.00 USD | 7,670.00 USD | `-39.70%` | `77,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,290,000.00 USD | 0.00 USD | 3,860.00 USD | `-39.10%` | `38,436,400,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,290,000.00 USD | 0.00 USD | 8,870.00 USD | `-38.49%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,280,000.00 USD | 0.00 USD | 8,910.00 USD | `-37.28%` | `86,083,300,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,270,000.00 USD | 0.00 USD | 6,640.00 USD | `-36.67%` | `63,563,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,260,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.07%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,260,000.00 USD | 0.00 USD | 450.48 USD | `-35.46%` | `4,229,900,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,260,000.00 USD | 0.00 USD | 1,820.00 USD | `-34.86%` | `16,928,700,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,250,000.00 USD | 0.00 USD | 11,210.00 USD | `-34.25%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,240,000.00 USD | 0.00 USD | 129,840.00 USD | `-33.04%` | `1,175,027,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,110,000.00 USD | 0.00 USD | 425.50 USD | `-32.43%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,110,000.00 USD | 0.00 USD | 281.48 USD | `-31.22%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,110,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.61%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,100,000.00 USD | 0.00 USD | 2,010.00 USD | `-30.01%` | `17,439,600,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,100,000.00 USD | 0.00 USD | 6,230.00 USD | `-29.40%` | `53,476,700,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,100,000.00 USD | 0.00 USD | 7,420.00 USD | `-28.80%` | `63,146,600,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,090,000.00 USD | 0.00 USD | 25,800.00 USD | `-28.19%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,060,000.00 USD | 0.00 USD | 2,750.00 USD | `-27.58%` | `23,024,600,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,060,000.00 USD | 0.00 USD | 303.75 USD | `-26.37%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,060,000.00 USD | 0.00 USD | 19,220.00 USD | `-25.77%` | `156,903,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,040,000.00 USD | 0.00 USD | 50,430.00 USD | `-25.16%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 989,440.00 USD | 0.00 USD | 377.05 USD | `-24.55%` | `3,028,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 989,070.00 USD | 0.00 USD | 348.01 USD | `-23.95%` | `2,773,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 988,720.00 USD | 0.00 USD | 16,720.00 USD | `-23.34%` | `132,151,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 972,000.00 USD | 0.00 USD | 9,780.00 USD | `-22.13%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 962,220.00 USD | 0.00 USD | 2,010.00 USD | `-21.52%` | `15,486,600,000,000.00` |
| `Live` | `Long` | `0.1305` | 960,220.00 USD | 0.00 USD | 18,760.00 USD | `-20.92%` | `143,742,300,000,000.00` |
| `Live` | `Long` | `0.1315` | 941,460.00 USD | 0.00 USD | 18,320.00 USD | `-20.31%` | `139,289,200,000,000.02` |
| `Live` | `Long` | `0.1325` | 923,140.00 USD | 0.00 USD | 4,640.00 USD | `-19.71%` | `35,013,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 918,510.00 USD | 0.00 USD | 59,240.00 USD | `-19.10%` | `443,725,300,000,000.00` |
| `Live` | `Long` | `0.1345` | 859,270.00 USD | 0.00 USD | 30,990.00 USD | `-18.49%` | `230,382,400,000,000.00` |
| `Live` | `Long` | `0.1355` | 828,280.00 USD | 0.00 USD | 2,830.00 USD | `-17.89%` | `20,869,500,000,000.00` |
| `Live` | `Long` | `0.1365` | 825,450.00 USD | 0.00 USD | 8,920.00 USD | `-17.28%` | `65,376,500,000,000.00` |
| `Live` | `Long` | `0.1375` | 816,530.00 USD | 0.00 USD | 13,710.00 USD | `-16.68%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 802,820.00 USD | 0.00 USD | 6,100.00 USD | `-16.07%` | `44,042,700,000,000.00` |
| `Live` | `Long` | `0.1395` | 796,720.00 USD | 0.00 USD | 9,210.00 USD | `-15.46%` | `66,000,700,000,000.00` |
| `Live` | `Long` | `0.1405` | 787,510.00 USD | 0.00 USD | 14,550.00 USD | `-14.86%` | `103,574,900,000,000.00` |
| `Live` | `Long` | `0.1415` | 772,960.00 USD | 0.00 USD | 16,540.00 USD | `-14.25%` | `116,879,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 756,420.00 USD | 0.00 USD | 499,200.00 USD | `-13.65%` | `3,503,164,600,000,000.00` |
| `Live` | `Long` | `0.1435` | 257,220.00 USD | 0.00 USD | 18,970.00 USD | `-13.04%` | `132,163,100,000,000.00` |
| `Live` | `Long` | `0.1445` | 238,250.00 USD | 0.00 USD | 9,510.00 USD | `-12.43%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 228,740.00 USD | 0.00 USD | 92,080.00 USD | `-11.83%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 136,660.00 USD | 0.00 USD | 28,850.00 USD | `-11.22%` | `196,937,100,000,000.00` |
| `Live` | `Long` | `0.1475` | 107,810.00 USD | 0.00 USD | 82,880.00 USD | `-10.62%` | `561,883,500,000,000.00` |
| `Live` | `Long` | `0.1485` | 24,930.00 USD | 0.00 USD | 2,290.00 USD | `-10.01%` | `15,410,500,000,000.00` |
| `Live` | `Long` | `0.1495` | 22,640.00 USD | 0.00 USD | 937.17 USD | `-9.40%` | `6,268,700,000,000.00` |
| `Live` | `Long` | `0.1515` | 21,710.00 USD | 0.00 USD | 945.33 USD | `-8.19%` | `6,239,800,000,000.00` |
| `Live` | `Long` | `0.1535` | 20,760.00 USD | 0.00 USD | 8,650.00 USD | `-6.98%` | `56,373,000,000,000.00` |
| `Live` | `Long` | `0.1555` | 12,110.00 USD | 0.00 USD | 2,270.00 USD | `-5.77%` | `14,625,600,000,000.00` |
| `Live` | `Long` | `0.1565` | 9,830.00 USD | 0.00 USD | 9,830.00 USD | `-5.16%` | `62,834,200,000,000.00` |
| `Live` | `Short` | `0.1675` | 4,640.00 USD | 4,640.00 USD | 0.00 USD | `+1.50%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1705` | 5,090.00 USD | 448.16 USD | 0.00 USD | `+3.32%` | `2,628,500,000,000.00` |
| `Live` | `Short` | `0.1715` | 7,280.00 USD | 2,190.00 USD | 0.00 USD | `+3.93%` | `12,744,000,000,000.00` |
| `Live` | `Short` | `0.1725` | 8,720.00 USD | 1,440.00 USD | 0.00 USD | `+4.53%` | `8,369,900,000,000.00` |
| `Live` | `Short` | `0.1735` | 9,920.00 USD | 1,190.00 USD | 0.00 USD | `+5.14%` | `6,881,100,000,000.00` |
| `Live` | `Short` | `0.1785` | 10,840.00 USD | 921.36 USD | 0.00 USD | `+8.17%` | `5,161,700,000,000.00` |
| `Live` | `Short` | `0.1845` | 13,470.00 USD | 2,630.00 USD | 0.00 USD | `+11.80%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1855` | 14,080.00 USD | 616.01 USD | 0.00 USD | `+12.41%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 14,420.00 USD | 333.88 USD | 0.00 USD | `+13.62%` | `1,780,700,000,000.00` |
| `Live` | `Short` | `0.1945` | 18,430.00 USD | 4,010.00 USD | 0.00 USD | `+17.86%` | `20,600,200,000,000.00` |
| `Live` | `Short` | `0.1975` | 18,580.00 USD | 150.10 USD | 0.00 USD | `+19.68%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 30,170.00 USD | 11,590.00 USD | 0.00 USD | `+24.53%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2075` | 30,420.00 USD | 257.20 USD | 0.00 USD | `+25.74%` | `1,239,500,000,000.00` |
| `Live` | `Short` | `0.2085` | 30,900.00 USD | 474.40 USD | 0.00 USD | `+26.35%` | `2,275,300,000,000.00` |
| `Live` | `Short` | `0.2095` | 31,060.00 USD | 164.23 USD | 0.00 USD | `+26.95%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 31,250.00 USD | 190.73 USD | 0.00 USD | `+27.56%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2115` | 35,520.00 USD | 4,260.00 USD | 0.00 USD | `+28.17%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 51,210.00 USD | 15,690.00 USD | 0.00 USD | `+29.38%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 92,540.00 USD | 41,330.00 USD | 0.00 USD | `+30.59%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 92,760.00 USD | 213.22 USD | 0.00 USD | `+31.80%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 180,560.00 USD | 87,800.00 USD | 0.00 USD | `+33.01%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 180,670.00 USD | 114.52 USD | 0.00 USD | `+35.44%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 181,010.00 USD | 338.64 USD | 0.00 USD | `+36.04%` | `1,508,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 181,160.00 USD | 154.78 USD | 0.00 USD | `+36.65%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 188,150.00 USD | 6,980.00 USD | 0.00 USD | `+39.07%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 204,080.00 USD | 15,930.00 USD | 0.00 USD | `+42.71%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 204,180.00 USD | 102.62 USD | 0.00 USD | `+43.92%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 252,280.00 USD | 48,100.00 USD | 0.00 USD | `+45.74%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2425` | 275,110.00 USD | 22,840.00 USD | 0.00 USD | `+46.95%` | `94,166,000,000,000.00` |
| `Live` | `Short` | `0.2455` | 275,350.00 USD | 231.97 USD | 0.00 USD | `+48.77%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 275,890.00 USD | 546.54 USD | 0.00 USD | `+54.22%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 279,760.00 USD | 3,870.00 USD | 0.00 USD | `+55.44%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 306,330.00 USD | 26,570.00 USD | 0.00 USD | `+56.04%` | `103,191,700,000,000.00` |
| `Live` | `Short` | `0.2585` | 361,300.00 USD | 54,960.00 USD | 0.00 USD | `+56.65%` | `212,629,500,000,000.00` |
| `Live` | `Short` | `0.2615` | 361,450.00 USD | 154.94 USD | 0.00 USD | `+58.47%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2635` | 543,960.00 USD | 182,510.00 USD | 0.00 USD | `+59.68%` | `692,636,800,000,000.00` |
| `Live` | `Short` | `0.2685` | 544,190.00 USD | 226.51 USD | 0.00 USD | `+62.71%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 557,430.00 USD | 13,240.00 USD | 0.00 USD | `+64.53%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 557,640.00 USD | 214.21 USD | 0.00 USD | `+65.13%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 569,240.00 USD | 11,600.00 USD | 0.00 USD | `+66.34%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 569,720.00 USD | 482.84 USD | 0.00 USD | `+69.37%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2815` | 571,870.00 USD | 2,140.00 USD | 0.00 USD | `+70.59%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2865` | 584,440.00 USD | 12,580.00 USD | 0.00 USD | `+73.62%` | `43,905,000,000,000.00` |
| `Live` | `Short` | `0.2915` | 584,630.00 USD | 187.26 USD | 0.00 USD | `+76.65%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 585,430.00 USD | 794.52 USD | 0.00 USD | `+77.25%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2965` | 876,010.00 USD | 290,580.00 USD | 0.00 USD | `+79.68%` | `980,040,500,000,000.00` |
| `Live` | `Short` | `0.3015` | 877,920.00 USD | 1,910.00 USD | 0.00 USD | `+82.71%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3025` | 878,400.00 USD | 481.13 USD | 0.00 USD | `+83.31%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3075` | 884,690.00 USD | 6,290.00 USD | 0.00 USD | `+86.34%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 885,050.00 USD | 363.72 USD | 0.00 USD | `+86.95%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 896,980.00 USD | 11,930.00 USD | 0.00 USD | `+88.16%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3125` | 897,220.00 USD | 242.44 USD | 0.00 USD | `+89.37%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3175` | 897,450.00 USD | 227.49 USD | 0.00 USD | `+92.40%` | `716,500,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 821,640.00 USD | 0.00 USD | 355.00 USD | `-78.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 821,280.00 USD | 0.00 USD | 297.50 USD | `-74.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 820,980.00 USD | 0.00 USD | 353.50 USD | `-69.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 820,630.00 USD | 0.00 USD | 276.53 USD | `-66.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 820,350.00 USD | 0.00 USD | 4,310.00 USD | `-66.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 816,040.00 USD | 0.00 USD | 475.11 USD | `-61.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 815,570.00 USD | 0.00 USD | 131.16 USD | `-60.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 815,430.00 USD | 0.00 USD | 881.45 USD | `-59.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 814,550.00 USD | 0.00 USD | 1,070.00 USD | `-59.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 813,480.00 USD | 0.00 USD | 1,050.00 USD | `-58.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 812,430.00 USD | 0.00 USD | 1,010.00 USD | `-57.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 811,420.00 USD | 0.00 USD | 4,100.00 USD | `-57.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 807,320.00 USD | 0.00 USD | 529.04 USD | `-56.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 806,790.00 USD | 0.00 USD | 2,390.00 USD | `-56.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 804,400.00 USD | 0.00 USD | 757.39 USD | `-54.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 803,640.00 USD | 0.00 USD | 1,490.00 USD | `-52.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 802,160.00 USD | 0.00 USD | 277.37 USD | `-47.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 801,880.00 USD | 0.00 USD | 262.50 USD | `-46.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 801,620.00 USD | 0.00 USD | 795.57 USD | `-46.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 800,820.00 USD | 0.00 USD | 181.00 USD | `-45.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 800,640.00 USD | 0.00 USD | 3,810.00 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 796,830.00 USD | 0.00 USD | 1,550.00 USD | `-37.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 795,280.00 USD | 0.00 USD | 116.07 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 795,160.00 USD | 0.00 USD | 19,070.00 USD | `-34.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 776,090.00 USD | 0.00 USD | 1,240.00 USD | `-33.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 774,850.00 USD | 0.00 USD | 343.50 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 774,510.00 USD | 0.00 USD | 26,280.00 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 748,230.00 USD | 0.00 USD | 105.75 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 748,120.00 USD | 0.00 USD | 4,870.00 USD | `-26.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 743,260.00 USD | 0.00 USD | 83,620.00 USD | `-26.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 659,630.00 USD | 0.00 USD | 487.10 USD | `-25.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 659,140.00 USD | 0.00 USD | 14,940.00 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 644,210.00 USD | 0.00 USD | 129,320.00 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 514,890.00 USD | 0.00 USD | 2,670.00 USD | `-23.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 512,220.00 USD | 0.00 USD | 473.27 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 511,750.00 USD | 0.00 USD | 203,210.00 USD | `-22.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 308,540.00 USD | 0.00 USD | 1,670.00 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 306,860.00 USD | 0.00 USD | 1,590.00 USD | `-20.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 305,270.00 USD | 0.00 USD | 6,000.00 USD | `-19.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 299,270.00 USD | 0.00 USD | 625.78 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 298,640.00 USD | 0.00 USD | 502.28 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 298,140.00 USD | 0.00 USD | 162.60 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 297,980.00 USD | 0.00 USD | 700.86 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 297,280.00 USD | 0.00 USD | 13,710.00 USD | `-16.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 283,570.00 USD | 0.00 USD | 108.57 USD | `-16.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 283,460.00 USD | 0.00 USD | 3,520.00 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 279,930.00 USD | 0.00 USD | 127.35 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 279,810.00 USD | 0.00 USD | 24,850.00 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 254,960.00 USD | 0.00 USD | 1,300.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 253,660.00 USD | 0.00 USD | 25,960.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 227,700.00 USD | 0.00 USD | 46,010.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 181,700.00 USD | 0.00 USD | 16,980.00 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 164,710.00 USD | 0.00 USD | 2,400.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 162,310.00 USD | 0.00 USD | 2,610.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 159,700.00 USD | 0.00 USD | 2,390.00 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 157,310.00 USD | 0.00 USD | 3,010.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 154,300.00 USD | 0.00 USD | 401.02 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 153,900.00 USD | 0.00 USD | 2,990.00 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 150,910.00 USD | 0.00 USD | 33,910.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 116,990.00 USD | 0.00 USD | 5,420.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 111,580.00 USD | 0.00 USD | 500.87 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 111,080.00 USD | 0.00 USD | 14,340.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 96,740.00 USD | 0.00 USD | 499.16 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 96,240.00 USD | 0.00 USD | 9,980.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 86,260.00 USD | 0.00 USD | 2,570.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 83,690.00 USD | 0.00 USD | 19,290.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 64,400.00 USD | 0.00 USD | 516.91 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 63,880.00 USD | 0.00 USD | 107.35 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 63,780.00 USD | 0.00 USD | 1,040.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 62,730.00 USD | 0.00 USD | 62,730.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 3,190.00 USD | 3,190.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 46,840.00 USD | 43,650.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 47,990.00 USD | 1,140.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 49,130.00 USD | 1,150.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 49,290.00 USD | 153.58 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 49,850.00 USD | 564.90 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 51,650.00 USD | 1,800.00 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 62,980.00 USD | 11,330.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 63,500.00 USD | 524.32 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 63,720.00 USD | 219.54 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 64,820.00 USD | 1,100.00 USD | 0.00 USD | `+6.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 65,610.00 USD | 790.28 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 65,940.00 USD | 336.40 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 70,660.00 USD | 4,720.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 75,690.00 USD | 5,030.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 87,350.00 USD | 11,660.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 98,200.00 USD | 10,840.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 99,060.00 USD | 864.12 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 101,580.00 USD | 2,520.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 101,860.00 USD | 276.75 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 101,990.00 USD | 128.68 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 105,360.00 USD | 3,370.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 109,060.00 USD | 3,700.00 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 109,310.00 USD | 245.50 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 109,840.00 USD | 531.47 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 110,540.00 USD | 697.34 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 110,760.00 USD | 222.24 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 139,890.00 USD | 29,130.00 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 146,960.00 USD | 7,070.00 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 147,150.00 USD | 194.50 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 147,290.00 USD | 137.77 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 147,420.00 USD | 133.19 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 151,170.00 USD | 3,750.00 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 151,670.00 USD | 492.19 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 174,420.00 USD | 22,750.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 174,980.00 USD | 560.96 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 196,320.00 USD | 21,340.00 USD | 0.00 USD | `+22.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 196,690.00 USD | 371.35 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 282,590.00 USD | 85,900.00 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 284,050.00 USD | 1,470.00 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 284,230.00 USD | 174.20 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 286,300.00 USD | 2,080.00 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 286,550.00 USD | 252.51 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 288,920.00 USD | 2,370.00 USD | 0.00 USD | `+27.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 289,280.00 USD | 356.72 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 289,640.00 USD | 360.08 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 290,000.00 USD | 361.76 USD | 0.00 USD | `+30.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 290,370.00 USD | 363.44 USD | 0.00 USD | `+31.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 290,730.00 USD | 365.12 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 297,010.00 USD | 6,280.00 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 297,380.00 USD | 368.47 USD | 0.00 USD | `+33.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 319,870.00 USD | 22,490.00 USD | 0.00 USD | `+33.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 320,200.00 USD | 333.91 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 324,180.00 USD | 3,980.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 324,560.00 USD | 378.55 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 324,940.00 USD | 380.23 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 328,770.00 USD | 3,840.00 USD | 0.00 USD | `+38.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 362,590.00 USD | 33,820.00 USD | 0.00 USD | `+39.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 366,850.00 USD | 4,260.00 USD | 0.00 USD | `+40.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 368,370.00 USD | 1,520.00 USD | 0.00 USD | `+41.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 389,590.00 USD | 21,230.00 USD | 0.00 USD | `+43.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 392,120.00 USD | 2,530.00 USD | 0.00 USD | `+44.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 411,840.00 USD | 19,720.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 421,150.00 USD | 9,300.00 USD | 0.00 USD | `+46.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 423,060.00 USD | 1,910.00 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 441,810.00 USD | 18,750.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 442,360.00 USD | 551.23 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 442,760.00 USD | 397.90 USD | 0.00 USD | `+51.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 447,090.00 USD | 4,330.00 USD | 0.00 USD | `+51.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 447,410.00 USD | 320.66 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 463,300.00 USD | 15,880.00 USD | 0.00 USD | `+53.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 465,290.00 USD | 2,000.00 USD | 0.00 USD | `+54.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 467,850.00 USD | 2,550.00 USD | 0.00 USD | `+54.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 479,580.00 USD | 11,730.00 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 484,740.00 USD | 5,160.00 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 501,600.00 USD | 16,870.00 USD | 0.00 USD | `+57.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 528,390.00 USD | 26,790.00 USD | 0.00 USD | `+57.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 528,660.00 USD | 272.88 USD | 0.00 USD | `+63.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 528,780.00 USD | 114.99 USD | 0.00 USD | `+66.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 529,170.00 USD | 394.01 USD | 0.00 USD | `+67.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 529,550.00 USD | 375.53 USD | 0.00 USD | `+69.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 531,680.00 USD | 2,130.00 USD | 0.00 USD | `+73.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 532,260.00 USD | 579.27 USD | 0.00 USD | `+73.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 534,010.00 USD | 1,750.00 USD | 0.00 USD | `+76.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 534,110.00 USD | 101.21 USD | 0.00 USD | `+79.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 534,380.00 USD | 262.73 USD | 0.00 USD | `+79.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 535,820.00 USD | 1,440.00 USD | 0.00 USD | `+80.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 541,250.00 USD | 5,430.00 USD | 0.00 USD | `+82.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 546,670.00 USD | 5,430.00 USD | 0.00 USD | `+82.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 546,960.00 USD | 289.61 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 547,450.00 USD | 487.09 USD | 0.00 USD | `+85.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 554,020.00 USD | 6,570.00 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 559,200.00 USD | 5,180.00 USD | 0.00 USD | `+90.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 576,720.00 USD | 17,520.00 USD | 0.00 USD | `+93.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1310` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD |
| `7D` | `0.1313` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD |
| `7D` | `0.1325` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1397` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `0.1400` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1403` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1418` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `0.1421` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1430` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1436` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1439` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1442` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `0.1451` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `1D` | `0.1466` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD |
| `7D` | `0.1466` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1468` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 4,430.00 USD | 1,110.00 USD | 2,660.00 USD |
| `7D` | `0.1469` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1470` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD |
| `1D` | `0.1472` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 7,760.00 USD | 17,450.00 USD | 64,650.00 USD |
| `7D` | `0.1472` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1474` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 43,430.00 USD | 16,470.00 USD | 18,430.00 USD |
| `7D` | `0.1475` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD |
| `1D` | `0.1476` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 49,710.00 USD | 20,650.00 USD | 156,050.00 USD |
| `1D` | `0.1478` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 85,250.00 USD | 6,140.00 USD | 27,730.00 USD |
| `7D` | `0.1478` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1480` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 74,060.00 USD | 13,400.00 USD | 6,220.00 USD |
| `7D` | `0.1481` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD |
| `1D` | `0.1482` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 18,610.00 USD | 6,260.00 USD | 124,300.00 USD |
| `1D` | `0.1484` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 63,600.00 USD | 4,640.00 USD | 71,930.00 USD |
| `7D` | `0.1484` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD |
| `1D` | `0.1486` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 9,210.00 USD | 1,840.00 USD | 1,400.00 USD |
| `7D` | `0.1487` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1488` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 16,750.00 USD | 1,740.00 USD | 14,110.00 USD |
| `1D` | `0.1490` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 40,720.00 USD | 15,530.00 USD | 11,510.00 USD |
| `7D` | `0.1490` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD |
| `1D` | `0.1492` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 6,410.00 USD | 6,010.00 USD | 9,240.00 USD |
| `7D` | `0.1493` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1494` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 45,060.00 USD | 3,020.00 USD | 12,770.00 USD |
| `1D` | `0.1496` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 26,530.00 USD | 0.00 USD | 21,040.00 USD |
| `7D` | `0.1496` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1498` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 8,630.00 USD | 4,640.00 USD | 0.00 USD |
| `7D` | `0.1499` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1500` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 5,920.00 USD | 4,820.00 USD | 2,340.00 USD |
| `1D` | `0.1502` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 11,460.00 USD | 13,970.00 USD | 131,800.00 USD |
| `7D` | `0.1502` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1504` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 84,100.00 USD | 3,920.00 USD | 31,160.00 USD |
| `7D` | `0.1505` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1506` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 0.00 USD | 1,150.00 USD | 199,610.00 USD |
| `1D` | `0.1508` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 105,410.00 USD |
| `7D` | `0.1508` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1510` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 6,130.00 USD | 50,780.00 USD |
| `7D` | `0.1511` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1512` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 5,040.00 USD | 3,900.00 USD | 1,300.00 USD |
| `1D` | `0.1514` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 11,720.00 USD | 0.00 USD | 250,360.00 USD |
| `7D` | `0.1514` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1516` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 7,210.00 USD | 0.00 USD | 139,820.00 USD |
| `7D` | `0.1517` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1518` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 31,590.00 USD | 8,960.00 USD | 27,670.00 USD |
| `1D` | `0.1520` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 49,700.00 USD | 4,400.00 USD | 12,370.00 USD |
| `7D` | `0.1520` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1522` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 4,770.00 USD | 8,880.00 USD |
| `7D` | `0.1523` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1524` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1526` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1528` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 17,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1529` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1530` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 12,670.00 USD | 15,770.00 USD | 4,670.00 USD |
| `1D` | `0.1532` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD |
| `7D` | `0.1532` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1534` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 10,930.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `0.1535` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1536` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD |
| `1D` | `0.1538` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1538` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1540` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 27,770.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1542` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1544` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 10,090.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1544` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1546` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1547` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1548` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 16,200.00 USD | 12,300.00 USD | 9,340.00 USD |
| `1D` | `0.1550` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 8,630.00 USD | 14,430.00 USD | 20,380.00 USD |
| `7D` | `0.1550` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1552` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 1,680.00 USD | 5,050.00 USD |
| `7D` | `0.1553` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1554` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD |
| `1D` | `0.1556` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 7,120.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1556` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1558` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 6,990.00 USD | 11,690.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD |
| `1D` | `0.1562` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1564` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 11,460.00 USD | 38,290.00 USD | 2,050.00 USD |
| `7D` | `0.1565` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1566` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 70,570.00 USD | 1,850.00 USD | 16,410.00 USD |
| `1D` | `0.1568` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD |
| `7D` | `0.1568` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1570` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 27,380.00 USD | 5,080.00 USD | 105,410.00 USD |
| `7D` | `0.1571` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1572` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 48,950.00 USD | 5,380.00 USD | 82,520.00 USD |
| `1D` | `0.1574` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 11,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1574` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD |
| `1D` | `0.1576` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 4,460.00 USD | 0.00 USD | 11,190.00 USD |
| `7D` | `0.1577` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 30,670.00 USD | 29,200.00 USD | 22,140.00 USD |
| `1D` | `0.1580` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 9,050.00 USD | 6,060.00 USD | 7,610.00 USD |
| `7D` | `0.1580` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD |
| `1D` | `0.1582` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 49,700.00 USD | 14,280.00 USD | 16,650.00 USD |
| `7D` | `0.1583` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD |
| `1D` | `0.1584` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 60,550.00 USD | 19,610.00 USD | 12,850.00 USD |
| `1D` | `0.1586` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 18,000.00 USD | 28,750.00 USD | 47,690.00 USD |
| `7D` | `0.1586` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1588` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 10,670.00 USD | 19,300.00 USD | 37,340.00 USD |
| `7D` | `0.1589` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 18,670.00 USD | 8,510.00 USD | 22,390.00 USD |
| `1D` | `0.1592` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 24,520.00 USD | 44,770.00 USD |
| `7D` | `0.1592` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1594` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 10,260.00 USD | 20,310.00 USD | 19,310.00 USD |
| `7D` | `0.1595` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1598` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1600` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1601` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1602` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 44,810.00 USD | 10,160.00 USD | 0.00 USD |
| `1D` | `0.1604` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 3,850.00 USD | 12,790.00 USD |
| `7D` | `0.1604` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1606` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 21,600.00 USD | 0.00 USD | 23,340.00 USD |
| `7D` | `0.1607` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 166,880.00 USD | 0.00 USD | 381,740.00 USD |
| `1D` | `0.1608` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 34,860.00 USD | 7,790.00 USD | 90,310.00 USD |
| `1D` | `0.1610` | 998,950.00 USD | 0.00 USD | 998,950.00 USD | 71,710.00 USD | 58,400.00 USD | 28,810.00 USD |
| `7D` | `0.1610` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD |
| `1D` | `0.1612` | 840,020.00 USD | 0.00 USD | 840,020.00 USD | 23,810.00 USD | 23,830.00 USD | 25,000.00 USD |
| `7D` | `0.1613` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD |
| `1D` | `0.1614` | 767,380.00 USD | 0.00 USD | 767,380.00 USD | 6,760.00 USD | 34,180.00 USD | 5,700.00 USD |
| `1D` | `0.1616` | 720,750.00 USD | 0.00 USD | 720,750.00 USD | 0.00 USD | 29,840.00 USD | 46,960.00 USD |
| `7D` | `0.1616` | 910,620.00 USD | 0.00 USD | 910,620.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD |
| `1D` | `0.1618` | 643,950.00 USD | 0.00 USD | 643,950.00 USD | 21,220.00 USD | 12,770.00 USD | 0.00 USD |
| `7D` | `0.1619` | 638,790.00 USD | 0.00 USD | 638,790.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD |
| `1D` | `0.1620` | 609,950.00 USD | 0.00 USD | 609,950.00 USD | 10,990.00 USD | 8,710.00 USD | 30,970.00 USD |
| `1D` | `0.1622` | 559,290.00 USD | 0.00 USD | 559,290.00 USD | 34,840.00 USD | 5,660.00 USD | 43,860.00 USD |
| `7D` | `0.1622` | 562,130.00 USD | 0.00 USD | 562,130.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD |
| `1D` | `0.1624` | 474,930.00 USD | 0.00 USD | 474,930.00 USD | 63,030.00 USD | 17,020.00 USD | 27,920.00 USD |
| `7D` | `0.1625` | 406,910.00 USD | 0.00 USD | 406,910.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD |
| `1D` | `0.1626` | 366,960.00 USD | 0.00 USD | 366,960.00 USD | 38,240.00 USD | 20,350.00 USD | 50,930.00 USD |
| `1D` | `0.1628` | 257,440.00 USD | 0.00 USD | 257,440.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD |
| `7D` | `0.1628` | 147,720.00 USD | 0.00 USD | 147,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1630` | 122,300.00 USD | 0.00 USD | 122,300.00 USD | 23,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1631` | 70,940.00 USD | 0.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 98,410.00 USD | 0.00 USD | 98,410.00 USD | 98,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1633` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1634` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1634` | 17,390.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1636` | 32,260.00 USD | 32,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1661` | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 61,950.00 USD | 61,950.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD | 20,710.00 USD |
| `1D` | `0.1664` | 121,760.00 USD | 121,760.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | 50,530.00 USD |
| `7D` | `0.1664` | 265,580.00 USD | 265,580.00 USD | 0.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD |
| `1D` | `0.1666` | 159,460.00 USD | 159,460.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 32,360.00 USD |
| `7D` | `0.1667` | 320,830.00 USD | 320,830.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1668` | 178,780.00 USD | 178,780.00 USD | 0.00 USD | 0.00 USD | 11,890.00 USD | 7,440.00 USD |
| `1D` | `0.1670` | 200,020.00 USD | 200,020.00 USD | 0.00 USD | 4,600.00 USD | 3,850.00 USD | 12,790.00 USD |
| `7D` | `0.1670` | 657,080.00 USD | 657,080.00 USD | 0.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1672` | 284,180.00 USD | 284,180.00 USD | 0.00 USD | 56,860.00 USD | 3,960.00 USD | 23,340.00 USD |
| `7D` | `0.1673` | 770,180.00 USD | 770,180.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD |
| `1D` | `0.1674` | 346,260.00 USD | 346,260.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.1676` | 519,380.00 USD | 519,380.00 USD | 0.00 USD | 82,670.00 USD | 60,390.00 USD | 30,060.00 USD |
| `7D` | `0.1676` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD |
| `1D` | `0.1678` | 575,070.00 USD | 575,070.00 USD | 0.00 USD | 26,550.00 USD | 0.00 USD | 29,140.00 USD |
| `7D` | `0.1679` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD |
| `1D` | `0.1680` | 677,420.00 USD | 677,420.00 USD | 0.00 USD | 70,670.00 USD | 22,970.00 USD | 8,710.00 USD |
| `1D` | `0.1682` | 818,560.00 USD | 818,560.00 USD | 0.00 USD | 43,920.00 USD | 31,520.00 USD | 65,700.00 USD |
| `7D` | `0.1682` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD |
| `1D` | `0.1684` | 922,730.00 USD | 922,730.00 USD | 0.00 USD | 45,340.00 USD | 40,190.00 USD | 18,640.00 USD |
| `7D` | `0.1685` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1686` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 19,830.00 USD | 18,520.00 USD | 75,280.00 USD |
| `1D` | `0.1688` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 10,760.00 USD | 5,660.00 USD | 56,770.00 USD |
| `7D` | `0.1688` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD |
| `1D` | `0.1690` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 55,800.00 USD | 29,860.00 USD | 42,210.00 USD |
| `7D` | `0.1691` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD |
| `1D` | `0.1692` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 66,540.00 USD | 86,510.00 USD | 111,780.00 USD |
| `1D` | `0.1694` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 41,320.00 USD | 23,520.00 USD | 16,900.00 USD |
| `7D` | `0.1694` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1696` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 23,530.00 USD | 4,640.00 USD | 9,670.00 USD |
| `7D` | `0.1697` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1698` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 26,000.00 USD | 57,580.00 USD | 48,960.00 USD |
| `1D` | `0.1700` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD |
| `7D` | `0.1700` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1702` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 9,960.00 USD | 1,920.00 USD | 40,930.00 USD |
| `7D` | `0.1703` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1704` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 11,790.00 USD | 14,420.00 USD | 11,670.00 USD |
| `1D` | `0.1706` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 44,560.00 USD | 9,590.00 USD | 13,990.00 USD |
| `7D` | `0.1706` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD |
| `1D` | `0.1708` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 26,090.00 USD | 63,220.00 USD | 12,660.00 USD |
| `7D` | `0.1709` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 30,670.00 USD | 29,200.00 USD | 30,180.00 USD |
| `1D` | `0.1712` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 16,380.00 USD | 21,110.00 USD | 7,610.00 USD |
| `7D` | `0.1712` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD |
| `1D` | `0.1714` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 1,800.00 USD | 16,560.00 USD | 10,630.00 USD |
| `7D` | `0.1715` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD |
| `1D` | `0.1716` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 19,740.00 USD | 31,850.00 USD | 28,920.00 USD |
| `1D` | `0.1718` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 20,700.00 USD | 20,360.00 USD | 18,970.00 USD |
| `7D` | `0.1718` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1720` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 34,970.00 USD | 2,830.00 USD | 17,440.00 USD |
| `7D` | `0.1721` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD |
| `1D` | `0.1722` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 72,810.00 USD | 25,370.00 USD | 54,870.00 USD |
| `1D` | `0.1724` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 8,230.00 USD | 1,570.00 USD | 52,310.00 USD |
| `7D` | `0.1724` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD |
| `1D` | `0.1726` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 10,260.00 USD | 12,580.00 USD | 24,010.00 USD |
| `1D` | `0.1728` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1730` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1732` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 1,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `1D` | `0.1736` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1738` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1739` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1740` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | 5,180.00 USD |
| `1D` | `0.1742` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD |
| `1D` | `0.1744` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 2,660.00 USD |
| `7D` | `0.1745` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 9,500.00 USD |
| `1D` | `0.1748` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 36,350.00 USD |
| `7D` | `0.1748` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1750` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 8,710.00 USD |
| `7D` | `0.1751` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1752` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 25,110.00 USD |
| `1D` | `0.1754` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 14,700.00 USD |
| `7D` | `0.1754` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD |
| `1D` | `0.1756` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 6,850.00 USD | 3,540.00 USD | 47,910.00 USD |
| `7D` | `0.1757` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1758` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 37,400.00 USD | 14,260.00 USD | 15,330.00 USD |
| `1D` | `0.1760` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 20,970.00 USD | 73,590.00 USD | 12,260.00 USD |
| `7D` | `0.1760` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD |
| `1D` | `0.1762` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 50,470.00 USD | 2,140.00 USD | 60,400.00 USD |
| `7D` | `0.1763` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 203,430.00 USD | 119,360.00 USD | 12,330.00 USD |
| `1D` | `0.1764` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 8,260.00 USD | 25,840.00 USD | 38,630.00 USD |
| `1D` | `0.1766` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 7,570.00 USD | 3,150.00 USD | 32,550.00 USD |
| `7D` | `0.1766` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD |
| `1D` | `0.1768` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 19,860.00 USD | 70,050.00 USD | 25,200.00 USD |
| `7D` | `0.1769` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 32,300.00 USD | 12,060.00 USD | 14,520.00 USD |
| `1D` | `0.1772` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 4,900.00 USD | 9,310.00 USD | 21,240.00 USD |
| `7D` | `0.1772` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1774` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 12,400.00 USD | 14,420.00 USD | 5,300.00 USD |
| `7D` | `0.1775` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 22,060.00 USD | 12,480.00 USD | 9,130.00 USD |
| `1D` | `0.1778` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 26,670.00 USD | 70,980.00 USD | 11,450.00 USD |
| `7D` | `0.1778` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD |
| `1D` | `0.1780` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD | 9,410.00 USD |
| `7D` | `0.1781` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1782` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | 14,570.00 USD |
| `1D` | `0.1784` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 40,030.00 USD | 8,820.00 USD | 4,340.00 USD |
| `7D` | `0.1784` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1786` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 4,570.00 USD | 25,290.00 USD | 7,120.00 USD |
| `7D` | `0.1787` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 9,350.00 USD | 20,220.00 USD | 3,230.00 USD |
| `1D` | `0.1790` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `7D` | `0.1790` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1792` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 3,490.00 USD | 0.00 USD |
| `7D` | `0.1793` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1794` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 13,620.00 USD | 34,190.00 USD | 2,660.00 USD |
| `1D` | `0.1796` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD | 21,080.00 USD |
| `7D` | `0.1796` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1798` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 12,950.00 USD | 11,410.00 USD |
| `7D` | `0.1799` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1800` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 5,820.00 USD | 2,030.00 USD | 11,240.00 USD |
| `1D` | `0.1802` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 6,120.00 USD | 28,340.00 USD | 13,660.00 USD |
| `7D` | `0.1802` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD |
| `1D` | `0.1804` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 4,010.00 USD | 2,830.00 USD | 7,270.00 USD |
| `7D` | `0.1805` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1806` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,770.00 USD | 0.00 USD | 8,060.00 USD |
| `1D` | `0.1808` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 15,180.00 USD | 22,870.00 USD | 6,220.00 USD |
| `7D` | `0.1808` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1810` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 9,360.00 USD | 3,190.00 USD | 1,910.00 USD |
| `7D` | `0.1811` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD |
| `1D` | `0.1812` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 11,890.00 USD | 33,700.00 USD | 7,800.00 USD |
| `1D` | `0.1814` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 3,830.00 USD | 4,640.00 USD | 14,860.00 USD |
| `7D` | `0.1814` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD |
| `1D` | `0.1816` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 5,320.00 USD | 1,840.00 USD | 1,400.00 USD |
| `7D` | `0.1817` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1818` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 8,320.00 USD | 10,150.00 USD |
| `1D` | `0.1820` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 12,390.00 USD | 3,500.00 USD |
| `7D` | `0.1820` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1822` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 6,150.00 USD | 7,660.00 USD | 4,310.00 USD |
| `7D` | `0.1823` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD |
| `1D` | `0.1824` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 7,970.00 USD | 0.00 USD | 9,240.00 USD |
| `1D` | `0.1826` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 5,300.00 USD | 3,020.00 USD | 0.00 USD |
| `7D` | `0.1826` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 68,170.00 USD | 9,890.00 USD | 14,210.00 USD |
| `7D` | `0.1829` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD |
| `7D` | `0.1835` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 74,850.00 USD | 26,020.00 USD | 16,530.00 USD |
| `7D` | `0.1838` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `7D` | `0.1844` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD |
| `7D` | `0.1847` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD |
| `7D` | `0.1853` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD |
| `7D` | `0.1854` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `185.48M` | Total OI Tokens: `1,130,474,782.0 ARB`
  * 1h OI Change: `+0.93%` | 4h OI Change: `-1.45%` | 24h OI Change: `-13.24%`
  * Exchange Breakdown: Binance=`41.06M` | Bybit=`26.60M` | OKX=`14.19M` | Hyperliquid=`13.11M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.46K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0064%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0021%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0161%` | **USDT Bitget** | `-0.0034%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `48.32%` | `51.68%` | `0.93` | 860,560.00 USD |
| `15M` | `Binance` | `51.48%` | `48.52%` | `1.06` | 278,310.00 USD |
| `15M` | `OKX` | `41.52%` | `58.48%` | `0.71` | 96,730.00 USD |
| `15M` | `Bybit` | `40.05%` | `59.95%` | `0.67` | 169,150.00 USD |
| `15M` | `KuCoin` | `45.86%` | `54.14%` | `0.85` | 20,140.00 USD |
| `15M` | `Gate` | `54.3%` | `45.7%` | `1.19` | 7,490.00 USD |
| `15M` | `Bitget` | `58.58%` | `41.42%` | `1.41` | 25,390.00 USD |
| `15M` | `BingX` | `47.82%` | `52.18%` | `0.92` | 28,100.00 USD |
| `15M` | `MEXC` | `42.07%` | `57.93%` | `0.73` | 41,940.00 USD |
| `15M` | `Bitunix` | `50.22%` | `49.78%` | `1.01` | 7,840.00 USD |
| `15M` | `Hyperliquid` | `26.23%` | `73.77%` | `0.36` | 2,950.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.84%` | `53.16%` | `0.88` | 147,850.00 USD |
| `15M` | `Crypto.com` | `2.26%` | `97.74%` | `0.02` | 13.69 USD |
| `15M` | `WhiteBIT` | `92.15%` | `7.85%` | `11.74` | 29,820.00 USD |
| `15M` | `HTX` | `1.16%` | `98.84%` | `0.01` | 431.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `95.49%` | `4.51%` | `21.17` | 4,090.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.91%` | `85.09%` | `0.18` | 290.13 USD |
| `15M` | `Whale Positions` | `51.48%` | `48.52%` | `1.06` | 278,310.00 USD |
| `15M` | `Global Accounts` | `48.32%` | `51.68%` | `0.93` | 860,560.00 USD |
| `1H` | `ARB` | `50.93%` | `49.07%` | `1.04` | 3,560,000.00 USD |
| `1H` | `Binance` | `55.45%` | `44.55%` | `1.24` | 1,160,000.00 USD |
| `1H` | `OKX` | `53.1%` | `46.9%` | `1.13` | 525,990.00 USD |
| `1H` | `Bybit` | `48.22%` | `51.78%` | `0.93` | 448,400.00 USD |
| `1H` | `KuCoin` | `48.47%` | `51.53%` | `0.94` | 187,850.00 USD |
| `1H` | `Gate` | `42.96%` | `57.04%` | `0.75` | 31,330.00 USD |
| `1H` | `Bitget` | `65.69%` | `34.31%` | `1.91` | 111,410.00 USD |
| `1H` | `BingX` | `25.29%` | `74.71%` | `0.34` | 240,500.00 USD |
| `1H` | `MEXC` | `28.98%` | `71.02%` | `0.41` | 138,700.00 USD |
| `1H` | `Bitunix` | `53.35%` | `46.65%` | `1.14` | 30,400.00 USD |
| `1H` | `Hyperliquid` | `39.21%` | `60.79%` | `0.65` | 15,660.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.82%` | `48.18%` | `1.08` | 592,020.00 USD |
| `1H` | `Crypto.com` | `2.6%` | `97.4%` | `0.03` | 31.56 USD |
| `1H` | `WhiteBIT` | `84.66%` | `15.34%` | `5.52` | 72,970.00 USD |
| `1H` | `HTX` | `10.33%` | `89.67%` | `0.12` | 92.94 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `97.27%` | `2.73%` | `35.63` | 6,760.00 USD |
| `1H` | `Aster` | `37.4%` | `62.6%` | `0.60` | 53.24 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `28.39%` | `71.61%` | `0.40` | 3,180.00 USD |
| `1H` | `Whale Positions` | `55.45%` | `44.55%` | `1.24` | 1,160,000.00 USD |
| `1H` | `Global Accounts` | `50.93%` | `49.07%` | `1.04` | 3,560,000.00 USD |
| `4H` | `ARB` | `46.26%` | `53.74%` | `0.86` | 19,890,000.00 USD |
| `4H` | `Binance` | `46.95%` | `53.05%` | `0.89` | 6,330,000.00 USD |
| `4H` | `OKX` | `46.45%` | `53.55%` | `0.87` | 1,590,000.00 USD |
| `4H` | `Bybit` | `50.23%` | `49.77%` | `1.01` | 1,850,000.00 USD |
| `4H` | `KuCoin` | `49.83%` | `50.17%` | `0.99` | 2,170,000.00 USD |
| `4H` | `Gate` | `49.9%` | `50.1%` | `1.00` | 397,900.00 USD |
| `4H` | `Bitget` | `49.54%` | `50.46%` | `0.98` | 1,950,000.00 USD |
| `4H` | `BingX` | `31.62%` | `68.38%` | `0.46` | 2,510,000.00 USD |
| `4H` | `MEXC` | `47%` | `53%` | `0.89` | 1,010,000.00 USD |
| `4H` | `Bitunix` | `37.93%` | `62.07%` | `0.61` | 288,720.00 USD |
| `4H` | `Hyperliquid` | `46.85%` | `53.15%` | `0.88` | 295,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 954,540.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `69.41%` | `30.59%` | `2.27` | 373,770.00 USD |
| `4H` | `HTX` | `55.44%` | `44.56%` | `1.24` | 4,840.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `34.3%` | `65.7%` | `0.52` | 156.24 USD |
| `4H` | `Aster` | `37.1%` | `62.9%` | `0.59` | 152,200.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `16.49%` | `83.51%` | `0.20` | 6,140.00 USD |
| `4H` | `Whale Positions` | `46.95%` | `53.05%` | `0.89` | 6,330,000.00 USD |
| `4H` | `Global Accounts` | `46.26%` | `53.74%` | `0.86` | 19,890,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1655` | `0.1654` | `0.1655` | `0.1662` | `0.1649` | 537,572.77 USD | 291,685.33 USD | 245,887.44 USD | 45,797.89 USD | `+8.52%` | `30B / 31S` |
| `0:00 UTC` | `0.1645` | `0.1649` | `0.1645` | `0.1665` | `0.1640` | 670,553.64 USD | 218,902.16 USD | 451,651.48 USD | -232,749.32 USD | `-34.71%` | `13B / 45S` |
| `5:00 UTC` | `0.1638` | `0.1640` | `0.1638` | `0.1652` | `0.1630` | 1,202,076.92 USD | 758,820.83 USD | 443,256.09 USD | 315,564.74 USD | `+26.25%` | `32B / 9S` |
| `0:00 UTC` | `0.1645` | `0.1645` | `0.1645` | `0.1648` | `0.1643` | 452,925.03 USD | 201,772.00 USD | 251,153.02 USD | -49,381.02 USD | `-10.90%` | `9B / 8S` |
| `5:00 UTC` | `0.1638` | `0.1639` | `0.1638` | `0.1646` | `0.1633` | 719,818.68 USD | 449,264.79 USD | 270,553.89 USD | 178,710.91 USD | `+24.83%` | `32B / 24S` |
| `0:00 UTC` | `0.1638` | `0.1644` | `0.1638` | `0.1657` | `0.1634` | 1,167,470.68 USD | 690,008.18 USD | 477,462.51 USD | 212,545.67 USD | `+18.21%` | `32B / 3S` |
| `5:00 UTC` | `0.1650` | `0.1648` | `0.1650` | `0.1651` | `0.1640` | 1,330,863.86 USD | 714,476.79 USD | 616,387.06 USD | 98,089.73 USD | `+7.37%` | `15B / 7S` |
| `0:00 UTC` | `0.1641` | `0.1647` | `0.1641` | `0.1657` | `0.1639` | 2,406,571.88 USD | 1,201,675.03 USD | 1,204,896.84 USD | -3,221.81 USD | `-0.13%` | `31B / 55S` |
| `5:00 UTC` | `0.1641` | `0.1639` | `0.1641` | `0.1647` | `0.1634` | 780,398.32 USD | 282,316.37 USD | 498,081.96 USD | -215,765.59 USD | `-27.65%` | `7B / 50S` |
| `0:00 UTC` | `0.1633` | `0.1635` | `0.1633` | `0.1638` | `0.1632` | 365,768.05 USD | 183,473.84 USD | 182,294.21 USD | 1,179.63 USD | `+0.32%` | `9B / 14S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1671` | 1,100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1677` | 2,200,000.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1667` | 522,000.00 USD | 0.00 USD |
| `10-28 20:42` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1670` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1668` | 0.00 USD | 0.00 USD |
| `10-28 20:36` | `Volume 10M ARB` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1677` | 0.00 USD | 0.00 USD |
| `10-28 20:08` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1637` | 359,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1637` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1642` | 1,100,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,300,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1640` | 0.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1634` | 0.00 USD | 0.00 USD |
| `10-28 19:42` | `Volume 10M ARB` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,900,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1649` | 0.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 10M ARB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1659` | 2,200,000.00 USD | 0.00 USD |
| `10-28 18:55` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1652` | 0.00 USD | 0.00 USD |
| `10-28 18:43` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1646` | 0.00 USD | 0.00 USD |
| `10-28 18:23` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1641` | 0.00 USD | 0.00 USD |
| `10-28 18:08` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1654` | 0.00 USD | 0.00 USD |
| `10-28 17:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 2,000,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1658` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 504,000.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1659` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1676` | 294,000.00 USD | 0.00 USD |
| `10-28 16:55` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1685` | 413,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 15:42` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 751,000.00 USD | 0.00 USD |
| `10-28 14:07` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1701` | 750,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1705` | 3,300,000.00 USD | 0.00 USD |
| `10-28 13:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1683` | 1,800,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1677` | 434,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1677` | 1,900,000.00 USD | 0.00 USD |
| `10-28 12:29` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1684` | 0.00 USD | 0.00 USD |
| `10-28 11:54` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 11:22` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1688` | 1,200,000.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 513,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 09:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1681` | 1,300,000.00 USD | 0.00 USD |
| `10-28 09:09` | `Range 0.0005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.1708` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1688` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1688` | 843,000.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1694` | 0.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1699` | 422,000.00 USD | 0.00 USD |
| `10-28 07:57` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1691` | 1,100,000.00 USD | 0.00 USD |
| `10-28 07:35` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 06:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1691` | 1,600,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -3,980.00 USD | 37,470.00 USD | **`ACCUMULATION`** |
| `15m` | -20,150.00 USD | -165,310.00 USD | **`DISTRIBUTION`** |
| `30m` | -208,340.00 USD | -633,170.00 USD | **`DISTRIBUTION`** |
| `1h` | -162,120.00 USD | -654,600.00 USD | **`DISTRIBUTION`** |
| `2h` | -148,690.00 USD | -10,840.00 USD | **`DISTRIBUTION`** |
| `4h` | -363,340.00 USD | -3,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -343,890.00 USD | -2,150,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -163,640.00 USD | -2,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,390,000.00 USD | -5,100,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,850,000.00 USD | -11,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,830,000.00 USD | -38,570,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,570,000.00 USD | -165,750,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.98K` | 15m=`-20.15K` | 1h=`-162.12K` | 24h=`-1.85M`
* Futures Capital Netflows: 5m=`+37.47K` | 15m=`-165.31K` | 1h=`-654.60K` | 24h=`-11.00M`
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
  * `2026-10-30 13:52:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:16 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1695` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.03` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.17`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1705` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.37` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.83`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1714`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
