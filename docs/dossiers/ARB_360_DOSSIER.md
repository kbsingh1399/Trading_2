# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 14:35:45 IST` (`2026-10-30 09:05:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1635` | `0.1640` | `0.1631` | `0.1639` | `1,482,423` | 242,243.92 USD | 12,255.41 USD | `+5.06%` | -7,427,330.89 USD | `-0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1639` | `0.1639` | `0.1623` | `0.1629` | `2,407,876` | 391,968.09 USD | -93,305.80 USD | `-23.80%` | -7,520,636.69 USD | `-1.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1629` | `0.1632` | `0.1626` | `0.1626` | `674,358` | 109,841.08 USD | -48,158.24 USD | `-43.84%` | -7,568,794.93 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1637` | `0.1646` | `0.1631` | `0.1640` | `5,782,732` | 946,588.03 USD | 50,345.45 USD | `+5.32%` | -7,495,867.48 USD | `+0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1640` | `0.1640` | `0.1623` | `0.1629` | `4,771,869` | 778,400.97 USD | -146,938.51 USD | `-18.88%` | -7,642,805.99 USD | `-0.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1629` | `0.1632` | `0.1625` | `0.1628` | `811,135` | 132,087.10 USD | -35,473.87 USD | `-26.86%` | -7,678,279.87 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1646` | `0.1657` | `0.1633` | `0.1649` | `22,323,310` | 3,671,078.25 USD | 439,965.29 USD | `+11.98%` | -7,388,117.42 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1650` | `0.1657` | `0.1623` | `0.1629` | `29,928,265` | 4,911,959.21 USD | -315,580.46 USD | `-6.42%` | -7,703,697.88 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1629` | `0.1632` | `0.1625` | `0.1628` | `811,135` | 132,087.10 USD | -35,473.87 USD | `-26.86%` | -7,739,171.75 USD | `+0.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1623` | `0.1626` | `30,602,624` | 5,021,800.29 USD | -363,738.70 USD | `-7.24%` | -7,211,253.33 USD | `+0.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1623` | `0.1626` | `30,602,624` | 5,021,800.29 USD | -363,738.70 USD | `-7.24%` | -7,211,253.33 USD | `+0.70` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `7D` | `Long Liquidation` | `0.1310` | 8,970,000.00 USD | 8,970,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 18,320.00 USD | 941,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,950,000.00 USD | 8,950,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,930,000.00 USD | 8,930,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,910,000.00 USD | 8,910,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 923,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,870,000.00 USD | 8,870,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,840,000.00 USD | 8,840,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,810,000.00 USD | 8,810,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 59,240.00 USD | 918,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,800,000.00 USD | 8,800,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,770,000.00 USD | 8,770,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 30,990.00 USD | 859,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,730,000.00 USD | 8,730,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,670,000.00 USD | 8,670,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,640,000.00 USD | 8,640,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,610,000.00 USD | 8,610,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 2,830.00 USD | 828,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,590,000.00 USD | 8,590,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,550,000.00 USD | 8,550,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,530,000.00 USD | 8,530,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 8,920.00 USD | 825,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 8,510,000.00 USD | 8,510,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 8,490,000.00 USD | 8,490,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 816,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 8,450,000.00 USD | 8,450,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 8,440,000.00 USD | 8,440,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 6,100.00 USD | 802,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 8,380,000.00 USD | 8,380,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 9,210.00 USD | 796,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 8,280,000.00 USD | 8,280,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 8,270,000.00 USD | 8,270,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,550.00 USD | 787,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,540.00 USD | 772,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,200.00 USD | 756,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1430` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 257,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 8,220,000.00 USD | 8,220,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 8,190,000.00 USD | 8,190,000.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 238,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1451` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 228,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,850.00 USD | 136,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 8,150,000.00 USD | 8,150,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1467` | 5,080,000.00 USD | 5,080,000.00 USD | 4,180.00 USD | 6,960.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 5,070,000.00 USD | 5,070,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 8,040,000.00 USD | 8,040,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 5,060,000.00 USD | 5,060,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 8,030,000.00 USD | 8,030,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 5,050,000.00 USD | 5,050,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,920,000.00 USD | 4,920,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 8,000,000.00 USD | 8,000,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 82,880.00 USD | 107,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 4,890,000.00 USD | 4,890,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,960,000.00 USD | 7,960,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,610,000.00 USD | 4,610,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 4,490,000.00 USD | 4,490,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,690,000.00 USD | 7,690,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 4,440,000.00 USD | 4,440,000.00 USD | 28,260.00 USD | 8,210.00 USD | 127,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,590,000.00 USD | 7,590,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 4,280,000.00 USD | 4,280,000.00 USD | 47,900.00 USD | 1,040.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 24,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 4,160,000.00 USD | 4,160,000.00 USD | 8,840.00 USD | 3,580.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 7,380,000.00 USD | 7,380,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 4,140,000.00 USD | 4,140,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 7,280,000.00 USD | 7,280,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 4,110,000.00 USD | 4,110,000.00 USD | 23,780.00 USD | 15,530.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 4,050,000.00 USD | 4,050,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 7,140,000.00 USD | 7,140,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 4,010,000.00 USD | 4,010,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 22,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 7,080,000.00 USD | 7,080,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,930,000.00 USD | 3,930,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,920,000.00 USD | 3,920,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,840,000.00 USD | 6,840,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,900,000.00 USD | 3,900,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,750,000.00 USD | 6,750,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,880,000.00 USD | 3,880,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,670,000.00 USD | 3,670,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,740,000.00 USD | 6,740,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,600,000.00 USD | 6,600,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 6,190,000.00 USD | 6,190,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 3,260,000.00 USD | 3,260,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 3,000,000.00 USD | 3,000,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 21,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,870,000.00 USD | 2,870,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,670,000.00 USD | 5,670,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,820,000.00 USD | 2,820,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,750,000.00 USD | 2,750,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,690,000.00 USD | 2,690,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,690,000.00 USD | 2,690,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,640,000.00 USD | 2,640,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,630,000.00 USD | 2,630,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,600,000.00 USD | 2,600,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,560,000.00 USD | 2,560,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 5,200,000.00 USD | 5,200,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,650.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,540,000.00 USD | 2,540,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,520,000.00 USD | 2,520,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,480,000.00 USD | 2,480,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 2,440,000.00 USD | 2,440,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 2,420,000.00 USD | 2,420,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,370,000.00 USD | 2,370,000.00 USD | 8,630.00 USD | 10,490.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 2,350,000.00 USD | 2,350,000.00 USD | 4,960.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 2,340,000.00 USD | 2,340,000.00 USD | 29,960.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 2,270.00 USD | 12,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1556` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 11,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 2,280,000.00 USD | 2,280,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 2,270,000.00 USD | 2,270,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 2,260,000.00 USD | 2,260,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 2,220,000.00 USD | 2,220,000.00 USD | 48,710.00 USD | 19,210.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,790,000.00 USD | 4,790,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,830.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 2,140,000.00 USD | 2,140,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,690,000.00 USD | 4,690,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 2,110,000.00 USD | 2,110,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,980,000.00 USD | 1,980,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 4,410,000.00 USD | 4,410,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,870,000.00 USD | 1,870,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 4,150,000.00 USD | 4,150,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,790,000.00 USD | 1,790,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,950,000.00 USD | 3,950,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 1,720,000.00 USD | 1,720,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,810,000.00 USD | 3,810,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,700,000.00 USD | 1,700,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,670,000.00 USD | 1,670,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,520,000.00 USD | 3,520,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 1,530,000.00 USD | 1,530,000.00 USD | 10,610.00 USD | 17,270.00 USD | 6,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 3,410,000.00 USD | 3,410,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,490,000.00 USD | 1,490,000.00 USD | 26,090.00 USD | 26,600.00 USD | 49,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 1,390,000.00 USD | 1,390,000.00 USD | 3,300.00 USD | 10,830.00 USD | 43,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 3,320,000.00 USD | 3,320,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 1,330,000.00 USD | 1,330,000.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1592` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 32,920.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 1,200,000.00 USD | 1,200,000.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 1,170,000.00 USD | 1,170,000.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 1,140,000.00 USD | 1,140,000.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,900,000.00 USD | 2,900,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 1,100,000.00 USD | 1,100,000.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 1,050,000.00 USD | 1,050,000.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,500,000.00 USD | 2,500,000.00 USD | 166,880.00 USD | 0.00 USD | 381,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 1,030,000.00 USD | 1,030,000.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,960,000.00 USD | 1,960,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 877,680.00 USD | 877,680.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 702,130.00 USD | 702,130.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,590,000.00 USD | 1,590,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 638,760.00 USD | 638,760.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 839,680.00 USD | 839,680.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1617` | 576,450.00 USD | 576,450.00 USD | 16,070.00 USD | 8,790.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 525,900.00 USD | 525,900.00 USD | 16,140.00 USD | 17,910.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1619` | 567,850.00 USD | 567,850.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 460,870.00 USD | 460,870.00 USD | 0.00 USD | 5,660.00 USD | 24,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 491,190.00 USD | 491,190.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 430,400.00 USD | 430,400.00 USD | 72,120.00 USD | 17,020.00 USD | 19,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 322,210.00 USD | 322,210.00 USD | 63,990.00 USD | 0.00 USD | 47,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 335,970.00 USD | 335,970.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1627` | 211,010.00 USD | 211,010.00 USD | 20,520.00 USD | 20,350.00 USD | 41,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 76,780.00 USD | 76,780.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 129,020.00 USD | 129,020.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 23,880.00 USD | 23,880.00 USD | 23,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1631` | 70,940.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1631` | 141,880.00 USD | 141,880.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1635` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 245,630.00 USD | 245,630.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 92,860.00 USD | 92,860.00 USD | 0.00 USD | 14,550.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 407,460.00 USD | 407,460.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 130,200.00 USD | 130,200.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 172,110.00 USD | 172,110.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 462,710.00 USD | 462,710.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 199,880.00 USD | 199,880.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 798,960.00 USD | 798,960.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 261,910.00 USD | 261,910.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 346,160.00 USD | 346,160.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 912,060.00 USD | 912,060.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 379,450.00 USD | 379,450.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,150,000.00 USD | 1,150,000.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 569,600.00 USD | 569,600.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 627,270.00 USD | 627,270.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,360,000.00 USD | 1,360,000.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 772,030.00 USD | 772,030.00 USD | 88,700.00 USD | 34,810.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,600,000.00 USD | 1,600,000.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 888,450.00 USD | 888,450.00 USD | 53,980.00 USD | 12,810.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 1,020,000.00 USD | 1,020,000.00 USD | 30,330.00 USD | 48,480.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,690,000.00 USD | 1,690,000.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,100,000.00 USD | 1,100,000.00 USD | 4,160.00 USD | 8,320.00 USD | 69,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,780,000.00 USD | 1,780,000.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 1,200,000.00 USD | 1,200,000.00 USD | 44,020.00 USD | 26,970.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,440,000.00 USD | 1,440,000.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,960,000.00 USD | 1,960,000.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,580,000.00 USD | 1,580,000.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 2,080,000.00 USD | 2,080,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,630,000.00 USD | 1,630,000.00 USD | 12,440.00 USD | 17,530.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 1,690,000.00 USD | 1,690,000.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 1,790,000.00 USD | 1,790,000.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 1,830,000.00 USD | 1,830,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 2,380,000.00 USD | 2,380,000.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 1,910,000.00 USD | 1,910,000.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 5,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1706` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,050,000.00 USD | 2,050,000.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 2,130,000.00 USD | 2,130,000.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,170,000.00 USD | 2,170,000.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1712` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,200,000.00 USD | 2,200,000.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 2,280,000.00 USD | 2,280,000.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 2,190.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,320,000.00 USD | 2,320,000.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,700,000.00 USD | 2,700,000.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,390,000.00 USD | 2,390,000.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 2,510,000.00 USD | 2,510,000.00 USD | 57,110.00 USD | 19,690.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 3,040,000.00 USD | 3,040,000.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,610,000.00 USD | 2,610,000.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 3,240,000.00 USD | 3,240,000.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 2,670,000.00 USD | 2,670,000.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 1,440.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1727` | 2,680,000.00 USD | 2,680,000.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,700,000.00 USD | 2,700,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 3,550,000.00 USD | 3,550,000.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 2,720,000.00 USD | 2,720,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,690,000.00 USD | 3,690,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,750,000.00 USD | 2,750,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 1,190.00 USD | 9,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,770,000.00 USD | 2,770,000.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 2,810,000.00 USD | 2,810,000.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,890,000.00 USD | 3,890,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 2,930,000.00 USD | 2,930,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 2,960,000.00 USD | 2,960,000.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,000,000.00 USD | 3,000,000.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 4,330,000.00 USD | 4,330,000.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,050,000.00 USD | 3,050,000.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 3,120,000.00 USD | 3,120,000.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 4,510,000.00 USD | 4,510,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,200,000.00 USD | 3,200,000.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,760,000.00 USD | 4,760,000.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,340,000.00 USD | 3,340,000.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 3,400,000.00 USD | 3,400,000.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 5,100,000.00 USD | 5,100,000.00 USD | 203,430.00 USD | 119,360.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,470,000.00 USD | 3,470,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,440,000.00 USD | 5,440,000.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 3,570,000.00 USD | 3,570,000.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 3,660,000.00 USD | 3,660,000.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,630,000.00 USD | 5,630,000.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,680,000.00 USD | 3,680,000.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,840,000.00 USD | 5,840,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,730,000.00 USD | 3,730,000.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 3,760,000.00 USD | 3,760,000.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 6,040,000.00 USD | 6,040,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 3,880,000.00 USD | 3,880,000.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 6,250,000.00 USD | 6,250,000.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 3,900,000.00 USD | 3,900,000.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,300,000.00 USD | 6,300,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 3,970,000.00 USD | 3,970,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,520,000.00 USD | 6,520,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,010,000.00 USD | 4,010,000.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 921.36 USD | 10,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1787` | 4,040,000.00 USD | 4,040,000.00 USD | 4,570.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,690,000.00 USD | 6,690,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,050,000.00 USD | 4,050,000.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,810,000.00 USD | 6,810,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 4,070,000.00 USD | 4,070,000.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,950,000.00 USD | 6,950,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,130,000.00 USD | 4,130,000.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 7,010,000.00 USD | 7,010,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 4,160,000.00 USD | 4,160,000.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 4,180,000.00 USD | 4,180,000.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,220,000.00 USD | 4,220,000.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 7,210,000.00 USD | 7,210,000.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 4,250,000.00 USD | 4,250,000.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 4,260,000.00 USD | 4,260,000.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 7,260,000.00 USD | 7,260,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,290,000.00 USD | 4,290,000.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,410,000.00 USD | 7,410,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 4,310,000.00 USD | 4,310,000.00 USD | 2,490.00 USD | 8,450.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 4,330,000.00 USD | 4,330,000.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,520,000.00 USD | 7,520,000.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 4,380,000.00 USD | 4,380,000.00 USD | 7,950.00 USD | 35,640.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,640,000.00 USD | 7,640,000.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 4,400,000.00 USD | 4,400,000.00 USD | 9,140.00 USD | 1,040.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1817` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 9,410.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,750,000.00 USD | 7,750,000.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,890,000.00 USD | 7,890,000.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 10,520.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 4,470,000.00 USD | 4,470,000.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 8,080,000.00 USD | 8,080,000.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 4,480,000.00 USD | 4,480,000.00 USD | 3,290.00 USD | 3,020.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1826` | 4,480,000.00 USD | 4,480,000.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 8,170,000.00 USD | 8,170,000.00 USD | 68,170.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,270,000.00 USD | 8,270,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,410,000.00 USD | 8,410,000.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,520,000.00 USD | 8,520,000.00 USD | 74,850.00 USD | 26,020.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,700,000.00 USD | 8,700,000.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,770,000.00 USD | 8,770,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,850,000.00 USD | 8,850,000.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,630.00 USD | 13,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1847` | 8,890,000.00 USD | 8,890,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,070,000.00 USD | 9,070,000.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,170,000.00 USD | 9,170,000.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,180,000.00 USD | 9,180,000.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0345` | 1,820,000.00 USD | 0.00 USD | 105.57 USD | `-78.82%` | `3,060,100,000,000.00` |
| `Live` | `Long` | `0.0365` | 1,820,000.00 USD | 0.00 USD | 356.31 USD | `-77.59%` | `9,761,800,000,000.00` |
| `Live` | `Long` | `0.0375` | 1,820,000.00 USD | 0.00 USD | 242.53 USD | `-76.98%` | `6,467,400,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,820,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.36%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,820,000.00 USD | 0.00 USD | 110.22 USD | `-74.52%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,820,000.00 USD | 0.00 USD | 170.00 USD | `-73.91%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0465` | 1,820,000.00 USD | 0.00 USD | 4,650.00 USD | `-71.45%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,810,000.00 USD | 0.00 USD | 109.52 USD | `-69.61%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,810,000.00 USD | 0.00 USD | 100.47 USD | `-69.00%` | `1,989,600,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,810,000.00 USD | 0.00 USD | 156.28 USD | `-68.38%` | `3,034,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,810,000.00 USD | 0.00 USD | 924.32 USD | `-67.77%` | `17,606,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,810,000.00 USD | 0.00 USD | 2,270.00 USD | `-66.54%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,810,000.00 USD | 0.00 USD | 16,160.00 USD | `-65.31%` | `285,941,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,790,000.00 USD | 0.00 USD | 205,030.00 USD | `-64.70%` | `3,565,715,900,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,590,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.47%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,590,000.00 USD | 0.00 USD | 1,250.00 USD | `-61.63%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,590,000.00 USD | 0.00 USD | 11,240.00 USD | `-59.17%` | `169,053,400,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 99,790.00 USD | `-58.56%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-57.95%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,470,000.00 USD | 0.00 USD | 976.14 USD | `-57.33%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,470,000.00 USD | 0.00 USD | 2,970.00 USD | `-56.72%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,470,000.00 USD | 0.00 USD | 5,840.00 USD | `-56.11%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,470,000.00 USD | 0.00 USD | 111.58 USD | `-55.49%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,470,000.00 USD | 0.00 USD | 3,000.00 USD | `-54.88%` | `40,770,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,460,000.00 USD | 0.00 USD | 226.17 USD | `-54.26%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,460,000.00 USD | 0.00 USD | 79,110.00 USD | `-53.04%` | `1,034,100,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,380,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.19%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,380,000.00 USD | 0.00 USD | 14,220.00 USD | `-49.35%` | `172,303,200,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,360,000.00 USD | 0.00 USD | 4,980.00 USD | `-48.74%` | `59,604,600,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,360,000.00 USD | 0.00 USD | 19,460.00 USD | `-46.90%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,340,000.00 USD | 0.00 USD | 280.45 USD | `-46.28%` | `3,205,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,340,000.00 USD | 0.00 USD | 362.62 USD | `-45.67%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,340,000.00 USD | 0.00 USD | 4,780.00 USD | `-45.05%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,330,000.00 USD | 0.00 USD | 2,180.00 USD | `-43.83%` | `23,867,500,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,330,000.00 USD | 0.00 USD | 2,040.00 USD | `-43.21%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,330,000.00 USD | 0.00 USD | 814.24 USD | `-42.60%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,330,000.00 USD | 0.00 USD | 1,510.00 USD | `-41.99%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,330,000.00 USD | 0.00 USD | 2,750.00 USD | `-41.37%` | `28,821,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,320,000.00 USD | 0.00 USD | 1,600.00 USD | `-40.76%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,320,000.00 USD | 0.00 USD | 396.66 USD | `-40.14%` | `4,068,300,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,320,000.00 USD | 0.00 USD | 13,020.00 USD | `-39.53%` | `132,186,200,000,000.02` |
| `Live` | `Long` | `0.0995` | 1,310,000.00 USD | 0.00 USD | 7,670.00 USD | `-38.92%` | `77,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,300,000.00 USD | 0.00 USD | 3,860.00 USD | `-38.30%` | `38,436,400,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,300,000.00 USD | 0.00 USD | 8,870.00 USD | `-37.69%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,290,000.00 USD | 0.00 USD | 414.83 USD | `-37.07%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 802.14 USD | `-36.46%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,290,000.00 USD | 0.00 USD | 13,280.00 USD | `-35.85%` | `127,068,000,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,270,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.23%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,270,000.00 USD | 0.00 USD | 1,620.00 USD | `-34.62%` | `15,202,300,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,260,000.00 USD | 0.00 USD | 2,230.00 USD | `-34.00%` | `20,784,700,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,260,000.00 USD | 0.00 USD | 11,210.00 USD | `-33.39%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,250,000.00 USD | 0.00 USD | 13,820.00 USD | `-32.16%` | `125,027,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,240,000.00 USD | 0.00 USD | 425.50 USD | `-31.55%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,240,000.00 USD | 0.00 USD | 118,120.00 USD | `-30.93%` | `1,050,000,000,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,120,000.00 USD | 0.00 USD | 281.48 USD | `-30.32%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,120,000.00 USD | 0.00 USD | 8,950.00 USD | `-29.71%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,110,000.00 USD | 0.00 USD | 1,450.00 USD | `-29.09%` | `12,552,800,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,110,000.00 USD | 0.00 USD | 14,280.00 USD | `-27.87%` | `121,510,100,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,090,000.00 USD | 0.00 USD | 25,800.00 USD | `-27.25%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,070,000.00 USD | 0.00 USD | 1,830.00 USD | `-26.64%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,070,000.00 USD | 0.00 USD | 1,240.00 USD | `-25.41%` | `10,238,400,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,070,000.00 USD | 0.00 USD | 19,220.00 USD | `-24.80%` | `156,903,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,050,000.00 USD | 0.00 USD | 50,430.00 USD | `-24.18%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 995,710.00 USD | 0.00 USD | 377.05 USD | `-23.57%` | `3,028,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 995,340.00 USD | 0.00 USD | 348.01 USD | `-22.95%` | `2,773,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 994,990.00 USD | 0.00 USD | 16,720.00 USD | `-22.34%` | `132,151,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 978,270.00 USD | 0.00 USD | 10,250.00 USD | `-21.73%` | `80,425,800,000,000.00` |
| `Live` | `Long` | `0.1295` | 968,020.00 USD | 0.00 USD | 2,010.00 USD | `-20.50%` | `15,486,600,000,000.00` |
| `Live` | `Long` | `0.1305` | 966,010.00 USD | 0.00 USD | 17,000.00 USD | `-19.88%` | `130,296,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 949,010.00 USD | 0.00 USD | 19,580.00 USD | `-19.27%` | `148,881,700,000,000.00` |
| `Live` | `Long` | `0.1325` | 929,430.00 USD | 0.00 USD | 4,640.00 USD | `-18.66%` | `35,013,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 924,790.00 USD | 0.00 USD | 51,860.00 USD | `-18.04%` | `388,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 872,930.00 USD | 0.00 USD | 39,090.00 USD | `-17.43%` | `290,617,800,000,000.00` |
| `Live` | `Long` | `0.1355` | 833,840.00 USD | 0.00 USD | 1,440.00 USD | `-16.82%` | `10,635,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 832,400.00 USD | 0.00 USD | 10,320.00 USD | `-16.20%` | `75,610,600,000,000.00` |
| `Live` | `Long` | `0.1375` | 822,080.00 USD | 0.00 USD | 18,260.00 USD | `-15.59%` | `132,828,700,000,000.02` |
| `Live` | `Long` | `0.1385` | 803,810.00 USD | 0.00 USD | 4,330.00 USD | `-14.97%` | `31,259,100,000,000.00` |
| `Live` | `Long` | `0.1395` | 799,480.00 USD | 0.00 USD | 9,210.00 USD | `-14.36%` | `66,000,700,000,000.00` |
| `Live` | `Long` | `0.1405` | 790,280.00 USD | 0.00 USD | 14,550.00 USD | `-13.75%` | `103,574,900,000,000.00` |
| `Live` | `Long` | `0.1415` | 775,720.00 USD | 0.00 USD | 16,540.00 USD | `-13.13%` | `116,879,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 759,190.00 USD | 0.00 USD | 499,030.00 USD | `-12.52%` | `3,501,939,200,000,000.00` |
| `Live` | `Long` | `0.1435` | 260,160.00 USD | 0.00 USD | 19,140.00 USD | `-11.90%` | `133,388,500,000,000.00` |
| `Live` | `Long` | `0.1445` | 241,020.00 USD | 0.00 USD | 9,510.00 USD | `-11.29%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 231,500.00 USD | 0.00 USD | 92,080.00 USD | `-10.68%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 139,430.00 USD | 0.00 USD | 28,360.00 USD | `-10.06%` | `193,592,500,000,000.00` |
| `Live` | `Long` | `0.1475` | 111,060.00 USD | 0.00 USD | 83,410.00 USD | `-9.45%` | `565,466,200,000,000.00` |
| `Live` | `Long` | `0.1485` | 27,660.00 USD | 0.00 USD | 3,340.00 USD | `-8.83%` | `22,502,000,000,000.00` |
| `Live` | `Long` | `0.1495` | 24,320.00 USD | 0.00 USD | 937.17 USD | `-8.22%` | `6,268,700,000,000.00` |
| `Live` | `Long` | `0.1515` | 23,380.00 USD | 0.00 USD | 945.33 USD | `-6.99%` | `6,239,800,000,000.00` |
| `Live` | `Long` | `0.1535` | 22,430.00 USD | 0.00 USD | 8,620.00 USD | `-5.76%` | `56,165,700,000,000.00` |
| `Live` | `Long` | `0.1555` | 13,810.00 USD | 0.00 USD | 4,150.00 USD | `-4.54%` | `26,689,100,000,000.00` |
| `Live` | `Long` | `0.1565` | 9,660.00 USD | 0.00 USD | 9,660.00 USD | `-3.92%` | `61,740,200,000,000.00` |
| `Live` | `Short` | `0.1635` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | `+0.37%` | `12,093,900,000,000.00` |
| `Live` | `Short` | `0.1675` | 6,620.00 USD | 4,640.00 USD | 0.00 USD | `+2.83%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1705` | 7,070.00 USD | 448.16 USD | 0.00 USD | `+4.67%` | `2,628,500,000,000.00` |
| `Live` | `Short` | `0.1715` | 8,220.00 USD | 1,150.00 USD | 0.00 USD | `+5.29%` | `6,703,900,000,000.00` |
| `Live` | `Short` | `0.1725` | 18,770.00 USD | 10,550.00 USD | 0.00 USD | `+5.90%` | `61,173,800,000,000.00` |
| `Live` | `Short` | `0.1735` | 19,970.00 USD | 1,190.00 USD | 0.00 USD | `+6.51%` | `6,881,100,000,000.00` |
| `Live` | `Short` | `0.1785` | 21,950.00 USD | 1,980.00 USD | 0.00 USD | `+9.58%` | `11,107,700,000,000.00` |
| `Live` | `Short` | `0.1815` | 22,080.00 USD | 135.29 USD | 0.00 USD | `+11.42%` | `745,400,000,000.00` |
| `Live` | `Short` | `0.1845` | 24,470.00 USD | 2,390.00 USD | 0.00 USD | `+13.27%` | `12,933,500,000,000.00` |
| `Live` | `Short` | `0.1855` | 25,090.00 USD | 616.01 USD | 0.00 USD | `+13.88%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 26,540.00 USD | 1,450.00 USD | 0.00 USD | `+15.11%` | `7,754,100,000,000.00` |
| `Live` | `Short` | `0.1945` | 30,550.00 USD | 4,010.00 USD | 0.00 USD | `+19.41%` | `20,600,200,000,000.00` |
| `Live` | `Short` | `0.1975` | 30,700.00 USD | 150.10 USD | 0.00 USD | `+21.25%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 42,290.00 USD | 11,590.00 USD | 0.00 USD | `+26.16%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2075` | 55,860.00 USD | 13,570.00 USD | 0.00 USD | `+27.39%` | `65,394,900,000,000.00` |
| `Live` | `Short` | `0.2085` | 56,330.00 USD | 474.40 USD | 0.00 USD | `+28.00%` | `2,275,300,000,000.00` |
| `Live` | `Short` | `0.2095` | 56,500.00 USD | 164.23 USD | 0.00 USD | `+28.61%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 56,690.00 USD | 190.73 USD | 0.00 USD | `+29.23%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2135` | 72,380.00 USD | 15,690.00 USD | 0.00 USD | `+31.07%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2145` | 76,700.00 USD | 4,320.00 USD | 0.00 USD | `+31.68%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2155` | 118,040.00 USD | 41,330.00 USD | 0.00 USD | `+32.30%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 118,250.00 USD | 213.22 USD | 0.00 USD | `+33.53%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 206,050.00 USD | 87,800.00 USD | 0.00 USD | `+34.75%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 206,160.00 USD | 114.52 USD | 0.00 USD | `+37.21%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 206,500.00 USD | 338.64 USD | 0.00 USD | `+37.82%` | `1,508,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 206,660.00 USD | 154.78 USD | 0.00 USD | `+38.44%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 213,640.00 USD | 6,980.00 USD | 0.00 USD | `+40.89%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 229,570.00 USD | 15,930.00 USD | 0.00 USD | `+44.58%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 229,670.00 USD | 102.62 USD | 0.00 USD | `+45.80%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 251,670.00 USD | 22,000.00 USD | 0.00 USD | `+47.65%` | `91,476,700,000,000.00` |
| `Live` | `Short` | `0.2425` | 300,970.00 USD | 49,300.00 USD | 0.00 USD | `+48.87%` | `203,286,500,000,000.00` |
| `Live` | `Short` | `0.2455` | 301,200.00 USD | 231.97 USD | 0.00 USD | `+50.72%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 301,750.00 USD | 546.54 USD | 0.00 USD | `+56.24%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 305,610.00 USD | 3,870.00 USD | 0.00 USD | `+57.47%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 332,190.00 USD | 26,570.00 USD | 0.00 USD | `+58.08%` | `103,191,700,000,000.00` |
| `Live` | `Short` | `0.2585` | 387,150.00 USD | 54,960.00 USD | 0.00 USD | `+58.70%` | `212,629,500,000,000.00` |
| `Live` | `Short` | `0.2615` | 387,310.00 USD | 154.94 USD | 0.00 USD | `+60.54%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 387,530.00 USD | 226.51 USD | 0.00 USD | `+64.84%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2695` | 399,360.00 USD | 11,830.00 USD | 0.00 USD | `+65.45%` | `43,905,000,000,000.00` |
| `Live` | `Short` | `0.2715` | 600,660.00 USD | 201,290.00 USD | 0.00 USD | `+66.68%` | `741,414,900,000,000.00` |
| `Live` | `Short` | `0.2725` | 600,870.00 USD | 214.21 USD | 0.00 USD | `+67.29%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 612,470.00 USD | 11,600.00 USD | 0.00 USD | `+68.52%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 612,950.00 USD | 482.84 USD | 0.00 USD | `+71.59%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2835` | 615,110.00 USD | 2,160.00 USD | 0.00 USD | `+74.04%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2915` | 615,300.00 USD | 187.26 USD | 0.00 USD | `+78.96%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 616,090.00 USD | 794.52 USD | 0.00 USD | `+79.57%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2985` | 903,180.00 USD | 287,090.00 USD | 0.00 USD | `+83.25%` | `961,767,500,000,000.00` |
| `Live` | `Short` | `0.3015` | 905,090.00 USD | 1,910.00 USD | 0.00 USD | `+85.09%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3055` | 905,570.00 USD | 485.90 USD | 0.00 USD | `+87.55%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3075` | 911,860.00 USD | 6,290.00 USD | 0.00 USD | `+88.78%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 912,470.00 USD | 603.06 USD | 0.00 USD | `+89.39%` | `1,954,800,000,000.00` |
| `Live` | `Short` | `0.3105` | 924,390.00 USD | 11,930.00 USD | 0.00 USD | `+90.62%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3125` | 925,920.00 USD | 1,530.00 USD | 0.00 USD | `+91.85%` | `4,897,100,000,000.00` |
| `Live` | `Short` | `0.3155` | 926,570.00 USD | 649.11 USD | 0.00 USD | `+93.69%` | `2,057,400,000,000.00` |
| `Live` | `Short` | `0.3175` | 926,800.00 USD | 227.49 USD | 0.00 USD | `+94.92%` | `716,500,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 757,760.00 USD | 0.00 USD | 355.00 USD | `-78.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 757,400.00 USD | 0.00 USD | 297.50 USD | `-73.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 757,100.00 USD | 0.00 USD | 353.50 USD | `-69.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 756,750.00 USD | 0.00 USD | 276.53 USD | `-66.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 756,470.00 USD | 0.00 USD | 4,310.00 USD | `-65.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 752,160.00 USD | 0.00 USD | 475.11 USD | `-61.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 751,680.00 USD | 0.00 USD | 131.16 USD | `-59.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 751,550.00 USD | 0.00 USD | 881.45 USD | `-59.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 750,670.00 USD | 0.00 USD | 1,070.00 USD | `-58.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 749,600.00 USD | 0.00 USD | 1,050.00 USD | `-57.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 748,550.00 USD | 0.00 USD | 1,010.00 USD | `-57.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 747,540.00 USD | 0.00 USD | 4,100.00 USD | `-56.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 743,430.00 USD | 0.00 USD | 529.04 USD | `-56.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 742,910.00 USD | 0.00 USD | 2,390.00 USD | `-55.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 740,520.00 USD | 0.00 USD | 757.39 USD | `-53.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 739,760.00 USD | 0.00 USD | 1,490.00 USD | `-51.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 738,270.00 USD | 0.00 USD | 277.37 USD | `-46.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 738,000.00 USD | 0.00 USD | 262.50 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 737,730.00 USD | 0.00 USD | 795.57 USD | `-45.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 736,940.00 USD | 0.00 USD | 181.00 USD | `-44.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 736,760.00 USD | 0.00 USD | 3,810.00 USD | `-38.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 732,940.00 USD | 0.00 USD | 1,550.00 USD | `-37.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 731,400.00 USD | 0.00 USD | 116.07 USD | `-34.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 731,280.00 USD | 0.00 USD | 19,070.00 USD | `-33.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 712,210.00 USD | 0.00 USD | 1,240.00 USD | `-32.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 710,970.00 USD | 0.00 USD | 343.50 USD | `-29.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 710,630.00 USD | 0.00 USD | 26,280.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 684,350.00 USD | 0.00 USD | 4,870.00 USD | `-26.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 679,480.00 USD | 0.00 USD | 83,620.00 USD | `-25.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 595,860.00 USD | 0.00 USD | 487.10 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 595,370.00 USD | 0.00 USD | 14,940.00 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 580,430.00 USD | 0.00 USD | 129,320.00 USD | `-22.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 451,110.00 USD | 0.00 USD | 2,670.00 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 448,440.00 USD | 0.00 USD | 473.27 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 447,970.00 USD | 0.00 USD | 203,210.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 244,760.00 USD | 0.00 USD | 1,670.00 USD | `-19.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 243,090.00 USD | 0.00 USD | 1,590.00 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 241,500.00 USD | 0.00 USD | 6,000.00 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 235,490.00 USD | 0.00 USD | 625.78 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 234,870.00 USD | 0.00 USD | 502.28 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 234,370.00 USD | 0.00 USD | 162.60 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 234,200.00 USD | 0.00 USD | 700.86 USD | `-16.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 233,500.00 USD | 0.00 USD | 13,710.00 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 219,790.00 USD | 0.00 USD | 108.57 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 219,680.00 USD | 0.00 USD | 3,520.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 216,160.00 USD | 0.00 USD | 127.35 USD | `-13.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 216,030.00 USD | 0.00 USD | 24,850.00 USD | `-12.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 191,190.00 USD | 0.00 USD | 1,300.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 189,880.00 USD | 0.00 USD | 25,960.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 163,930.00 USD | 0.00 USD | 46,010.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 117,920.00 USD | 0.00 USD | 16,980.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 100,940.00 USD | 0.00 USD | 2,400.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 98,540.00 USD | 0.00 USD | 2,610.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 95,920.00 USD | 0.00 USD | 2,390.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 93,540.00 USD | 0.00 USD | 3,010.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 90,530.00 USD | 0.00 USD | 401.02 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 90,120.00 USD | 0.00 USD | 2,990.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 87,130.00 USD | 0.00 USD | 33,910.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 53,220.00 USD | 0.00 USD | 5,420.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 47,800.00 USD | 0.00 USD | 500.87 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 47,300.00 USD | 0.00 USD | 14,340.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 32,960.00 USD | 0.00 USD | 499.16 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 32,460.00 USD | 0.00 USD | 9,980.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 22,480.00 USD | 0.00 USD | 2,570.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 19,910.00 USD | 0.00 USD | 19,290.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 624.26 USD | 0.00 USD | 516.91 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 107.35 USD | 0.00 USD | 107.35 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 63,780.00 USD | 62,730.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 66,970.00 USD | 3,190.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 110,620.00 USD | 43,650.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 111,760.00 USD | 1,140.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 112,910.00 USD | 1,150.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 113,060.00 USD | 153.58 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 113,630.00 USD | 564.90 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 115,430.00 USD | 1,800.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 126,750.00 USD | 11,330.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 127,280.00 USD | 524.32 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 127,500.00 USD | 219.54 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 128,590.00 USD | 1,100.00 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 129,380.00 USD | 790.28 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 129,720.00 USD | 336.40 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 134,440.00 USD | 4,720.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 139,470.00 USD | 5,030.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 151,130.00 USD | 11,660.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 161,970.00 USD | 10,840.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 162,840.00 USD | 864.12 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 165,360.00 USD | 2,520.00 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 165,640.00 USD | 276.75 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 165,770.00 USD | 128.68 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 169,140.00 USD | 3,370.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 172,840.00 USD | 3,700.00 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 173,080.00 USD | 245.50 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 173,620.00 USD | 531.47 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 174,310.00 USD | 697.34 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 174,540.00 USD | 222.24 USD | 0.00 USD | `+17.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 203,660.00 USD | 29,130.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 210,730.00 USD | 7,070.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 210,930.00 USD | 194.50 USD | 0.00 USD | `+19.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 211,070.00 USD | 137.77 USD | 0.00 USD | `+20.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 211,200.00 USD | 133.19 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 214,950.00 USD | 3,750.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 215,440.00 USD | 492.19 USD | 0.00 USD | `+22.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 238,190.00 USD | 22,750.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 238,760.00 USD | 560.96 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 260,090.00 USD | 21,340.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 260,470.00 USD | 371.35 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 346,360.00 USD | 85,900.00 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 347,830.00 USD | 1,470.00 USD | 0.00 USD | `+26.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 348,000.00 USD | 174.20 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 350,080.00 USD | 2,080.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 350,330.00 USD | 252.51 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 352,700.00 USD | 2,370.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 353,060.00 USD | 356.72 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 353,420.00 USD | 360.08 USD | 0.00 USD | `+31.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 353,780.00 USD | 361.76 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 354,140.00 USD | 363.44 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 354,510.00 USD | 365.12 USD | 0.00 USD | `+33.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 360,780.00 USD | 6,280.00 USD | 0.00 USD | `+34.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 361,150.00 USD | 368.47 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 383,640.00 USD | 22,490.00 USD | 0.00 USD | `+35.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 383,980.00 USD | 333.91 USD | 0.00 USD | `+36.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 387,950.00 USD | 3,980.00 USD | 0.00 USD | `+37.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 388,330.00 USD | 378.55 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 388,710.00 USD | 380.23 USD | 0.00 USD | `+39.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 392,550.00 USD | 3,840.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 426,370.00 USD | 33,820.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 430,630.00 USD | 4,260.00 USD | 0.00 USD | `+42.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 432,140.00 USD | 1,520.00 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 453,370.00 USD | 21,230.00 USD | 0.00 USD | `+45.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 455,900.00 USD | 2,530.00 USD | 0.00 USD | `+46.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 475,620.00 USD | 19,720.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 484,920.00 USD | 9,300.00 USD | 0.00 USD | `+48.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 486,830.00 USD | 1,910.00 USD | 0.00 USD | `+50.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 505,580.00 USD | 18,750.00 USD | 0.00 USD | `+51.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 506,140.00 USD | 551.23 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 506,530.00 USD | 397.90 USD | 0.00 USD | `+53.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 510,870.00 USD | 4,330.00 USD | 0.00 USD | `+53.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 511,190.00 USD | 320.66 USD | 0.00 USD | `+54.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 527,070.00 USD | 15,880.00 USD | 0.00 USD | `+55.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 529,070.00 USD | 2,000.00 USD | 0.00 USD | `+56.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 531,620.00 USD | 2,550.00 USD | 0.00 USD | `+56.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 543,350.00 USD | 11,730.00 USD | 0.00 USD | `+57.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 548,510.00 USD | 5,160.00 USD | 0.00 USD | `+58.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 565,380.00 USD | 16,870.00 USD | 0.00 USD | `+59.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 592,170.00 USD | 26,790.00 USD | 0.00 USD | `+59.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 592,440.00 USD | 272.88 USD | 0.00 USD | `+66.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 592,560.00 USD | 114.99 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 592,950.00 USD | 394.01 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 593,330.00 USD | 375.53 USD | 0.00 USD | `+72.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 595,460.00 USD | 2,130.00 USD | 0.00 USD | `+75.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 596,040.00 USD | 579.27 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 597,790.00 USD | 1,750.00 USD | 0.00 USD | `+78.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 597,890.00 USD | 101.21 USD | 0.00 USD | `+81.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 598,150.00 USD | 262.73 USD | 0.00 USD | `+82.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 599,590.00 USD | 1,440.00 USD | 0.00 USD | `+82.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 605,020.00 USD | 5,430.00 USD | 0.00 USD | `+84.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 610,450.00 USD | 5,430.00 USD | 0.00 USD | `+85.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 610,740.00 USD | 289.61 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 611,230.00 USD | 487.09 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 617,800.00 USD | 6,570.00 USD | 0.00 USD | `+90.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 622,970.00 USD | 5,180.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 640,490.00 USD | 17,520.00 USD | 0.00 USD | `+95.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1310` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD |
| `7D` | `0.1313` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD |
| `7D` | `0.1325` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1397` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `0.1400` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1403` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1418` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `0.1421` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1430` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1436` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1439` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1442` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `0.1451` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `7D` | `0.1466` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 4,180.00 USD | 6,960.00 USD | 2,660.00 USD |
| `1D` | `0.1469` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD |
| `7D` | `0.1469` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1471` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD |
| `7D` | `0.1472` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD |
| `1D` | `0.1475` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD |
| `7D` | `0.1475` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD |
| `1D` | `0.1477` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD |
| `7D` | `0.1478` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1479` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD |
| `1D` | `0.1481` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD |
| `7D` | `0.1481` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD |
| `1D` | `0.1483` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 28,260.00 USD | 8,210.00 USD | 127,490.00 USD |
| `7D` | `0.1484` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD |
| `1D` | `0.1485` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 47,900.00 USD | 1,040.00 USD | 66,840.00 USD |
| `1D` | `0.1487` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 8,840.00 USD | 3,580.00 USD | 13,500.00 USD |
| `7D` | `0.1487` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1489` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD |
| `7D` | `0.1490` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD |
| `1D` | `0.1491` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 23,780.00 USD | 15,530.00 USD | 13,390.00 USD |
| `1D` | `0.1493` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD |
| `7D` | `0.1493` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1495` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1496` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1497` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD |
| `1D` | `0.1499` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD |
| `7D` | `0.1499` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1501` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD |
| `7D` | `0.1502` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1503` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD |
| `1D` | `0.1505` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD |
| `7D` | `0.1505` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1507` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD |
| `7D` | `0.1508` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1509` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD |
| `1D` | `0.1511` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `0.1511` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1513` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD |
| `7D` | `0.1514` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1515` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD |
| `1D` | `0.1517` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD |
| `7D` | `0.1517` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1519` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD |
| `7D` | `0.1520` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1521` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `1D` | `0.1523` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1523` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1525` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1529` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD |
| `7D` | `0.1529` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1531` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD |
| `1D` | `0.1535` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD |
| `7D` | `0.1535` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD |
| `7D` | `0.1538` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1541` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `7D` | `0.1544` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1547` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1547` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1549` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD |
| `7D` | `0.1550` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1551` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 8,630.00 USD | 10,490.00 USD | 5,050.00 USD |
| `1D` | `0.1553` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 4,960.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1553` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1555` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 29,960.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1556` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 0.00 USD | 11,690.00 USD | 0.00 USD |
| `1D` | `0.1559` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1561` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1563` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD |
| `1D` | `0.1565` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 48,710.00 USD | 19,210.00 USD | 16,410.00 USD |
| `7D` | `0.1565` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1567` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD |
| `7D` | `0.1568` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1569` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD |
| `1D` | `0.1571` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD |
| `7D` | `0.1571` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD |
| `7D` | `0.1574` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD |
| `1D` | `0.1575` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD |
| `1D` | `0.1577` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD |
| `7D` | `0.1577` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD |
| `1D` | `0.1579` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD |
| `7D` | `0.1580` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD |
| `1D` | `0.1581` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD |
| `1D` | `0.1583` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD |
| `7D` | `0.1583` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD |
| `1D` | `0.1585` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 10,610.00 USD | 17,270.00 USD | 6,620.00 USD |
| `7D` | `0.1586` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1587` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 26,090.00 USD | 26,600.00 USD | 49,230.00 USD |
| `1D` | `0.1589` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 3,300.00 USD | 10,830.00 USD | 43,520.00 USD |
| `7D` | `0.1589` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD |
| `1D` | `0.1591` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD |
| `7D` | `0.1592` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1593` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 32,920.00 USD | 30,140.00 USD |
| `1D` | `0.1595` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD |
| `7D` | `0.1595` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1597` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1599` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD |
| `1D` | `0.1601` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1603` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1605` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1607` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.1607` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 166,880.00 USD | 0.00 USD | 381,740.00 USD |
| `1D` | `0.1609` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD |
| `7D` | `0.1610` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD |
| `1D` | `0.1611` | 877,680.00 USD | 0.00 USD | 877,680.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD |
| `1D` | `0.1613` | 702,130.00 USD | 0.00 USD | 702,130.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD |
| `7D` | `0.1613` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD |
| `1D` | `0.1615` | 638,760.00 USD | 0.00 USD | 638,760.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD |
| `7D` | `0.1616` | 839,680.00 USD | 0.00 USD | 839,680.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD |
| `1D` | `0.1617` | 576,450.00 USD | 0.00 USD | 576,450.00 USD | 16,070.00 USD | 8,790.00 USD | 25,700.00 USD |
| `1D` | `0.1619` | 525,900.00 USD | 0.00 USD | 525,900.00 USD | 16,140.00 USD | 17,910.00 USD | 30,970.00 USD |
| `7D` | `0.1619` | 567,850.00 USD | 0.00 USD | 567,850.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD |
| `1D` | `0.1621` | 460,870.00 USD | 0.00 USD | 460,870.00 USD | 0.00 USD | 5,660.00 USD | 24,810.00 USD |
| `7D` | `0.1622` | 491,190.00 USD | 0.00 USD | 491,190.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD |
| `1D` | `0.1623` | 430,400.00 USD | 0.00 USD | 430,400.00 USD | 72,120.00 USD | 17,020.00 USD | 19,050.00 USD |
| `1D` | `0.1625` | 322,210.00 USD | 0.00 USD | 322,210.00 USD | 63,990.00 USD | 0.00 USD | 47,210.00 USD |
| `7D` | `0.1625` | 335,970.00 USD | 0.00 USD | 335,970.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD |
| `1D` | `0.1627` | 211,010.00 USD | 0.00 USD | 211,010.00 USD | 20,520.00 USD | 20,350.00 USD | 41,120.00 USD |
| `7D` | `0.1628` | 76,780.00 USD | 0.00 USD | 76,780.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1629` | 129,020.00 USD | 0.00 USD | 129,020.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD |
| `1D` | `0.1631` | 23,880.00 USD | 0.00 USD | 23,880.00 USD | 23,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1631` | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1631` | 141,880.00 USD | 141,880.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1637` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1661` | 245,630.00 USD | 245,630.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1663` | 92,860.00 USD | 92,860.00 USD | 0.00 USD | 0.00 USD | 14,550.00 USD | 54,750.00 USD |
| `7D` | `0.1664` | 407,460.00 USD | 407,460.00 USD | 0.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD |
| `1D` | `0.1665` | 130,200.00 USD | 130,200.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD |
| `1D` | `0.1667` | 172,110.00 USD | 172,110.00 USD | 0.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD |
| `7D` | `0.1667` | 462,710.00 USD | 462,710.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1669` | 199,880.00 USD | 199,880.00 USD | 0.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 798,960.00 USD | 798,960.00 USD | 0.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 261,910.00 USD | 261,910.00 USD | 0.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1673` | 346,160.00 USD | 346,160.00 USD | 0.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD |
| `7D` | `0.1673` | 912,060.00 USD | 912,060.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD |
| `1D` | `0.1675` | 379,450.00 USD | 379,450.00 USD | 0.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD |
| `7D` | `0.1676` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD |
| `1D` | `0.1677` | 569,600.00 USD | 569,600.00 USD | 0.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD |
| `1D` | `0.1679` | 627,270.00 USD | 627,270.00 USD | 0.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD |
| `7D` | `0.1679` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD |
| `1D` | `0.1681` | 772,030.00 USD | 772,030.00 USD | 0.00 USD | 88,700.00 USD | 34,810.00 USD | 21,260.00 USD |
| `7D` | `0.1682` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD |
| `1D` | `0.1683` | 888,450.00 USD | 888,450.00 USD | 0.00 USD | 53,980.00 USD | 12,810.00 USD | 49,630.00 USD |
| `1D` | `0.1685` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 30,330.00 USD | 48,480.00 USD | 52,800.00 USD |
| `7D` | `0.1685` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1687` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 4,160.00 USD | 8,320.00 USD | 69,240.00 USD |
| `7D` | `0.1688` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 44,020.00 USD | 26,970.00 USD | 23,460.00 USD |
| `1D` | `0.1691` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD |
| `7D` | `0.1691` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD |
| `1D` | `0.1693` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD |
| `7D` | `0.1694` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1695` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 12,440.00 USD | 17,530.00 USD | 19,580.00 USD |
| `1D` | `0.1697` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD |
| `7D` | `0.1697` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1699` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1701` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `1D` | `0.1703` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD |
| `7D` | `0.1703` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1705` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD |
| `7D` | `0.1706` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD |
| `1D` | `0.1707` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD |
| `1D` | `0.1709` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD |
| `7D` | `0.1709` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD |
| `7D` | `0.1712` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD |
| `1D` | `0.1713` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD |
| `1D` | `0.1715` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD |
| `7D` | `0.1715` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD |
| `1D` | `0.1717` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD |
| `7D` | `0.1718` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1719` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD |
| `1D` | `0.1721` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 57,110.00 USD | 19,690.00 USD | 47,610.00 USD |
| `7D` | `0.1721` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD |
| `1D` | `0.1723` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD |
| `7D` | `0.1724` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD |
| `1D` | `0.1725` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD |
| `1D` | `0.1727` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD |
| `1D` | `0.1729` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1730` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1735` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD |
| `1D` | `0.1737` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD |
| `1D` | `0.1739` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD |
| `7D` | `0.1739` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1741` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `0.1743` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `1D` | `0.1745` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD |
| `7D` | `0.1745` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD |
| `7D` | `0.1748` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD |
| `1D` | `0.1751` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1751` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1753` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD |
| `7D` | `0.1754` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD |
| `1D` | `0.1755` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD |
| `1D` | `0.1757` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD |
| `7D` | `0.1757` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD |
| `7D` | `0.1760` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD |
| `1D` | `0.1763` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD |
| `7D` | `0.1763` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 203,430.00 USD | 119,360.00 USD | 12,330.00 USD |
| `1D` | `0.1765` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD |
| `7D` | `0.1766` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD |
| `1D` | `0.1767` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD |
| `1D` | `0.1769` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD |
| `7D` | `0.1769` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD |
| `1D` | `0.1771` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD |
| `7D` | `0.1772` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD |
| `1D` | `0.1775` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD |
| `7D` | `0.1775` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1777` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD |
| `1D` | `0.1779` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD |
| `1D` | `0.1781` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD | 2,080.00 USD |
| `7D` | `0.1781` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1783` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD |
| `1D` | `0.1787` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 4,570.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1787` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1790` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1791` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `1D` | `0.1793` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD |
| `7D` | `0.1793` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1795` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD |
| `7D` | `0.1796` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1797` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD |
| `1D` | `0.1799` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD |
| `7D` | `0.1799` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1801` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD |
| `7D` | `0.1802` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD |
| `1D` | `0.1803` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD |
| `1D` | `0.1805` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD |
| `7D` | `0.1805` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1807` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD |
| `7D` | `0.1808` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 2,490.00 USD | 8,450.00 USD | 1,970.00 USD |
| `1D` | `0.1811` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD |
| `7D` | `0.1811` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD |
| `1D` | `0.1813` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 7,950.00 USD | 35,640.00 USD | 10,820.00 USD |
| `7D` | `0.1814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD |
| `1D` | `0.1815` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 9,140.00 USD | 1,040.00 USD | 9,760.00 USD |
| `1D` | `0.1817` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 9,410.00 USD | 9,530.00 USD |
| `7D` | `0.1817` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1819` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD |
| `7D` | `0.1820` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1821` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | 4,310.00 USD |
| `1D` | `0.1823` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD |
| `7D` | `0.1823` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD |
| `1D` | `0.1825` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 3,290.00 USD | 3,020.00 USD | 3,860.00 USD |
| `1D` | `0.1826` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1826` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 68,170.00 USD | 9,890.00 USD | 14,210.00 USD |
| `7D` | `0.1829` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD |
| `7D` | `0.1835` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 74,850.00 USD | 26,020.00 USD | 16,530.00 USD |
| `7D` | `0.1838` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `7D` | `0.1844` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD |
| `7D` | `0.1847` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD |
| `7D` | `0.1853` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD |
| `7D` | `0.1854` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `185.05M` | Total OI Tokens: `1,129,265,013.3 ARB`
  * 1h OI Change: `+0.03%` | 4h OI Change: `-2.05%` | 24h OI Change: `-12.91%`
  * Exchange Breakdown: Binance=`40.96M` | Bybit=`26.57M` | OKX=`14.17M` | Hyperliquid=`13.09M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.25K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0054%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0129%` | **USDT Bitget** | `-0.0039%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `58.06%` | `41.94%` | `1.38` | 1,260,000.00 USD |
| `15M` | `Binance` | `52.76%` | `47.24%` | `1.12` | 372,060.00 USD |
| `15M` | `OKX` | `72.89%` | `27.11%` | `2.69` | 277,520.00 USD |
| `15M` | `Bybit` | `47.43%` | `52.57%` | `0.90` | 114,820.00 USD |
| `15M` | `KuCoin` | `49.39%` | `50.61%` | `0.98` | 124,810.00 USD |
| `15M` | `Gate` | `78.29%` | `21.71%` | `3.61` | 40,530.00 USD |
| `15M` | `Bitget` | `40.53%` | `59.47%` | `0.68` | 51,070.00 USD |
| `15M` | `BingX` | `38.75%` | `61.25%` | `0.63` | 63,200.00 USD |
| `15M` | `MEXC` | `64.85%` | `35.15%` | `1.84` | 40,900.00 USD |
| `15M` | `Bitunix` | `59.84%` | `40.16%` | `1.49` | 15,530.00 USD |
| `15M` | `Hyperliquid` | `83.24%` | `16.76%` | `4.97` | 22,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.14%` | `49.86%` | `1.01` | 44,510.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `68.47%` | `31.53%` | `2.17` | 90,360.00 USD |
| `15M` | `HTX` | `80.03%` | `19.97%` | `4.01` | 0.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.2%` | `33.8%` | `1.96` | 1,840.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 13.05 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 9.95 USD |
| `15M` | `Whale Positions` | `52.76%` | `47.24%` | `1.12` | 372,060.00 USD |
| `15M` | `Global Accounts` | `58.06%` | `41.94%` | `1.38` | 1,260,000.00 USD |
| `1H` | `ARB` | `45.27%` | `54.73%` | `0.83` | 15,730,000.00 USD |
| `1H` | `Binance` | `53.63%` | `46.37%` | `1.16` | 5,310,000.00 USD |
| `1H` | `OKX` | `50.3%` | `49.7%` | `1.01` | 3,060,000.00 USD |
| `1H` | `Bybit` | `57.79%` | `42.21%` | `1.37` | 1,030,000.00 USD |
| `1H` | `KuCoin` | `48.6%` | `51.4%` | `0.95` | 658,220.00 USD |
| `1H` | `Gate` | `52.87%` | `47.13%` | `1.12` | 308,660.00 USD |
| `1H` | `Bitget` | `45.89%` | `54.11%` | `0.85` | 499,100.00 USD |
| `1H` | `BingX` | `10.4%` | `89.6%` | `0.12` | 1,080,000.00 USD |
| `1H` | `MEXC` | `35.76%` | `64.24%` | `0.56` | 133,240.00 USD |
| `1H` | `Bitunix` | `51.62%` | `48.38%` | `1.07` | 200,880.00 USD |
| `1H` | `Hyperliquid` | `33.39%` | `66.61%` | `0.50` | 24,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.74%` | `50.26%` | `0.99` | 2,310,000.00 USD |
| `1H` | `Crypto.com` | `0.48%` | `99.52%` | `0.00` | 3,490.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,080,000.00 USD |
| `1H` | `HTX` | `39.22%` | `60.78%` | `0.65` | 19,070.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `13.36%` | `86.64%` | `0.15` | 25,810.00 USD |
| `1H` | `Aster` | `25.29%` | `74.71%` | `0.34` | 4,270.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.96%` | `48.04%` | `1.08` | 4,780.00 USD |
| `1H` | `Whale Positions` | `53.63%` | `46.37%` | `1.16` | 5,310,000.00 USD |
| `1H` | `Global Accounts` | `45.27%` | `54.73%` | `0.83` | 15,730,000.00 USD |
| `4H` | `ARB` | `47.15%` | `52.85%` | `0.89` | 47,740,000.00 USD |
| `4H` | `Binance` | `48.44%` | `51.56%` | `0.94` | 15,470,000.00 USD |
| `4H` | `OKX` | `53.37%` | `46.63%` | `1.14` | 8,890,000.00 USD |
| `4H` | `Bybit` | `50.06%` | `49.94%` | `1.00` | 4,080,000.00 USD |
| `4H` | `KuCoin` | `49.76%` | `50.24%` | `0.99` | 2,340,000.00 USD |
| `4H` | `Gate` | `53.59%` | `46.41%` | `1.15` | 987,540.00 USD |
| `4H` | `Bitget` | `47.84%` | `52.16%` | `0.92` | 1,350,000.00 USD |
| `4H` | `BingX` | `28.25%` | `71.75%` | `0.39` | 3,740,000.00 USD |
| `4H` | `MEXC` | `46.71%` | `53.29%` | `0.88` | 869,470.00 USD |
| `4H` | `Bitunix` | `40.48%` | `59.52%` | `0.68` | 874,440.00 USD |
| `4H` | `Hyperliquid` | `47.63%` | `52.37%` | `0.91` | 394,640.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.89%` | `50.11%` | `1.00` | 6,310,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 3,680.00 USD |
| `4H` | `WhiteBIT` | `72.07%` | `27.93%` | `2.58` | 2,320,000.00 USD |
| `4H` | `HTX` | `52.05%` | `47.95%` | `1.09` | 35,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.28%` | `56.72%` | `0.76` | 25,810.00 USD |
| `4H` | `Aster` | `46.2%` | `53.8%` | `0.86` | 30,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `13.2%` | `86.8%` | `0.15` | 16,660.00 USD |
| `4H` | `Whale Positions` | `48.44%` | `51.56%` | `0.94` | 15,470,000.00 USD |
| `4H` | `Global Accounts` | `47.15%` | `52.85%` | `0.89` | 47,740,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1645` | `0.1649` | `0.1645` | `0.1665` | `0.1640` | 670,553.64 USD | 218,902.16 USD | 451,651.48 USD | -232,749.32 USD | `-34.71%` | `13B / 45S` |
| `5:00 UTC` | `0.1638` | `0.1640` | `0.1638` | `0.1652` | `0.1630` | 1,202,076.92 USD | 758,820.83 USD | 443,256.09 USD | 315,564.74 USD | `+26.25%` | `32B / 9S` |
| `0:00 UTC` | `0.1645` | `0.1645` | `0.1645` | `0.1648` | `0.1643` | 452,925.03 USD | 201,772.00 USD | 251,153.02 USD | -49,381.02 USD | `-10.90%` | `9B / 8S` |
| `5:00 UTC` | `0.1638` | `0.1639` | `0.1638` | `0.1646` | `0.1633` | 719,818.68 USD | 449,264.79 USD | 270,553.89 USD | 178,710.91 USD | `+24.83%` | `32B / 24S` |
| `0:00 UTC` | `0.1638` | `0.1644` | `0.1638` | `0.1657` | `0.1634` | 1,167,470.68 USD | 690,008.18 USD | 477,462.51 USD | 212,545.67 USD | `+18.21%` | `32B / 3S` |
| `5:00 UTC` | `0.1650` | `0.1648` | `0.1650` | `0.1651` | `0.1640` | 1,330,863.86 USD | 714,476.79 USD | 616,387.06 USD | 98,089.73 USD | `+7.37%` | `15B / 7S` |
| `0:00 UTC` | `0.1641` | `0.1647` | `0.1641` | `0.1657` | `0.1639` | 2,406,571.88 USD | 1,201,675.03 USD | 1,204,896.84 USD | -3,221.81 USD | `-0.13%` | `31B / 55S` |
| `5:00 UTC` | `0.1641` | `0.1639` | `0.1641` | `0.1647` | `0.1634` | 780,398.32 USD | 282,316.37 USD | 498,081.96 USD | -215,765.59 USD | `-27.65%` | `7B / 50S` |
| `0:00 UTC` | `0.1639` | `0.1637` | `0.1639` | `0.1646` | `0.1631` | 946,588.03 USD | 498,466.74 USD | 448,121.29 USD | 50,345.45 USD | `+5.32%` | `36B / 23S` |
| `5:00 UTC` | `0.1625` | `0.1631` | `0.1625` | `0.1640` | `0.1624` | 735,809.16 USD | 293,706.97 USD | 442,102.20 USD | -148,395.23 USD | `-20.17%` | `19B / 55S` |

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
| `5m` | -242,220.00 USD | -186,080.00 USD | **`DISTRIBUTION`** |
| `15m` | -282,340.00 USD | -231,770.00 USD | **`DISTRIBUTION`** |
| `30m` | -115,570.00 USD | 12,140.00 USD | **`DISTRIBUTION`** |
| `1h` | -213,660.00 USD | -503,340.00 USD | **`DISTRIBUTION`** |
| `2h` | -291,330.00 USD | -309,810.00 USD | **`DISTRIBUTION`** |
| `4h` | -421,900.00 USD | -2,100,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -441,930.00 USD | -2,410,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -459,550.00 USD | -2,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -322,370.00 USD | 162,500.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,950,000.00 USD | -10,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,890,000.00 USD | -37,280,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,600,000.00 USD | -165,390,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-242.22K` | 15m=`-282.34K` | 1h=`-213.66K` | 24h=`-1.95M`
* Futures Capital Netflows: 5m=`-186.08K` | 15m=`-231.77K` | 1h=`-503.34K` | 24h=`-10.85M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
