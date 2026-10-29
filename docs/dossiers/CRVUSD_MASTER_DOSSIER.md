# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:27:39 IST` (`2026-10-29 20:57:39 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3010` | **Live Ask Quote**: `0.3230` | **Mid Price**: `0.3120`
- **Spread Points**: `22.00` | **Spread BPS**: `705.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3155` | VWAP Z-Score: `-3.32` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0036` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `19.12` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3314` | Lower -3.00σ Band: `0.2997`
  * Upper +2.51σ Band: `0.3288` | Lower -2.51σ Band: `0.3023`
  * Upper +2.01σ Band: `0.3262` | Lower -2.01σ Band: `0.3049`
  * Upper +2.00σ Band: `0.3261` | Lower -2.00σ Band: `0.3050`
  * Upper +1.28σ Band: `0.3223` | Lower -1.28σ Band: `0.3088`
  * Upper +1.00σ Band: `0.3208` | Lower -1.00σ Band: `0.3103`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3101` | EMA-20=`0.3135` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3160` (Slope: `+0.0000`) | EMA-100=`0.3181`
  * Institutional Anchors: EMA-144=`0.3194` | EMA-200=`0.3207` (Slope: `-0.3552`) | EMA-233=`0.3215`
- **Range Boundaries**: 24H High=`0.3330` | 24H Low=`0.2960` | Weekly High=`0.3340` | Weekly Low=`0.2960`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3230` (Distance: `-3.28%`)
  * Point of Control (POC) = `0.3160` (Distance: `-1.31%`)
  * Value Area Low (VAL) = `0.3100` (Distance: `+0.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3300` | POC=`0.3270` | VAL=`0.3240`
  * Prior Day Extremes: PDH=`0.3340` | PDL=`0.3210` | PDC=`0.3300`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3370` | Weekly POC=`0.3290` | Weekly VAL=`0.3200`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3330` | Low=`0.3090`
  * London Session (08:00-16:00 UTC): High=`0.3210` | Low=`0.3120`
  * New York Session (13:00-21:00 UTC): High=`0.3270` | Low=`0.3120`
  * Initial Balance (First Hour): IB High=`0.3190` | IB Low=`0.3140`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3108` - `0.3132`
  * Optimal Trade Entry (OTE 0.705): `0.3126`
  * Structural Invalidation Anchor (0.786): `0.3145`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

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
  * 24H Horizon: Short MP=`0.3453` (Vol: 74,017.03 USD, Dist: `+2.95%`) | Long MP=`0.3285` (Vol: 54,223.53 USD, Dist: `--2.06%`)
  * 48H Horizon: Short MP=`0.3451` (Vol: 61,276.63 USD, Dist: `+2.89%`) | Long MP=`0.3266` (Vol: 86,480.44 USD, Dist: `--2.62%`)
  * 3D Horizon: Short MP=`0.3454` (Vol: 78,069.95 USD, Dist: `+2.98%`) | Long MP=`0.3267` (Vol: 81,272.05 USD, Dist: `--2.59%`)
  * 7D Horizon: Short MP=`0.3626` (Vol: 135,917.70 USD, Dist: `+8.67%`) | Long MP=`0.3267` (Vol: 96,300.06 USD, Dist: `--2.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0675` | 5,870,000.00 USD | 0.00 USD | 627.59 USD | `-79.24%` | `9,297.60` |
| `Live` | `Long` | `0.0735` | 5,870,000.00 USD | 0.00 USD | 4,180.00 USD | `-77.40%` | `56,846.60` |
| `Live` | `Long` | `0.0785` | 5,860,000.00 USD | 0.00 USD | 2,330.00 USD | `-75.86%` | `29,622.60` |
| `Live` | `Long` | `0.0805` | 5,860,000.00 USD | 0.00 USD | 241.50 USD | `-75.25%` | `3,000.00` |
| `Live` | `Long` | `0.0865` | 5,860,000.00 USD | 0.00 USD | 485.44 USD | `-73.40%` | `5,612.00` |
| `Live` | `Long` | `0.0875` | 5,860,000.00 USD | 0.00 USD | 1,580.00 USD | `-73.10%` | `18,050.00` |
| `Live` | `Long` | `0.0925` | 5,860,000.00 USD | 0.00 USD | 35,950.00 USD | `-71.56%` | `388,690.50` |
| `Live` | `Long` | `0.0935` | 5,820,000.00 USD | 0.00 USD | 751.98 USD | `-71.25%` | `8,042.60` |
| `Live` | `Long` | `0.1055` | 5,820,000.00 USD | 0.00 USD | 651.53 USD | `-67.56%` | `6,175.60` |
| `Live` | `Long` | `0.1225` | 5,820,000.00 USD | 0.00 USD | 116.35 USD | `-62.33%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,820,000.00 USD | 0.00 USD | 4,300.00 USD | `-61.41%` | `34,264.40` |
| `Live` | `Long` | `0.1335` | 5,820,000.00 USD | 0.00 USD | 6,280.00 USD | `-58.95%` | `47,058.80` |
| `Live` | `Long` | `0.1365` | 5,810,000.00 USD | 0.00 USD | 862.88 USD | `-58.03%` | `6,321.50` |
| `Live` | `Long` | `0.1375` | 5,810,000.00 USD | 0.00 USD | 1,150.00 USD | `-57.72%` | `8,365.30` |
| `Live` | `Long` | `0.1415` | 5,810,000.00 USD | 0.00 USD | 1,810.00 USD | `-56.49%` | `12,814.90` |
| `Live` | `Long` | `0.1425` | 5,810,000.00 USD | 0.00 USD | 427.50 USD | `-56.18%` | `3,000.00` |
| `Live` | `Long` | `0.1495` | 5,810,000.00 USD | 0.00 USD | 202.18 USD | `-54.03%` | `1,352.40` |
| `Live` | `Long` | `0.1555` | 5,810,000.00 USD | 0.00 USD | 592.63 USD | `-52.19%` | `3,811.10` |
| `Live` | `Long` | `0.1645` | 5,810,000.00 USD | 0.00 USD | 397.60 USD | `-49.42%` | `2,417.00` |
| `Live` | `Long` | `0.1665` | 5,810,000.00 USD | 0.00 USD | 4,930.00 USD | `-48.80%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 5,800,000.00 USD | 0.00 USD | 6,780.00 USD | `-47.88%` | `40,000.00` |
| `Live` | `Long` | `0.1715` | 5,790,000.00 USD | 0.00 USD | 464.68 USD | `-47.27%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,790,000.00 USD | 0.00 USD | 5,430.00 USD | `-46.96%` | `31,498.20` |
| `Live` | `Long` | `0.1745` | 5,790,000.00 USD | 0.00 USD | 31,240.00 USD | `-46.34%` | `179,000.00` |
| `Live` | `Long` | `0.1755` | 5,760,000.00 USD | 0.00 USD | 8,210.00 USD | `-46.04%` | `46,797.00` |
| `Live` | `Long` | `0.1765` | 5,750,000.00 USD | 0.00 USD | 28,580.00 USD | `-45.73%` | `161,927.10` |
| `Live` | `Long` | `0.1775` | 5,720,000.00 USD | 0.00 USD | 14,130.00 USD | `-45.42%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,710,000.00 USD | 0.00 USD | 12,900.00 USD | `-45.11%` | `72,270.30` |
| `Live` | `Long` | `0.1795` | 5,690,000.00 USD | 0.00 USD | 13,180.00 USD | `-44.81%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,680,000.00 USD | 0.00 USD | 16,880.00 USD | `-44.50%` | `93,542.70` |
| `Live` | `Long` | `0.1815` | 5,660,000.00 USD | 0.00 USD | 4,540.00 USD | `-44.19%` | `25,000.00` |
| `Live` | `Long` | `0.1835` | 5,660,000.00 USD | 0.00 USD | 179.10 USD | `-43.58%` | `976.00` |
| `Live` | `Long` | `0.1845` | 5,660,000.00 USD | 0.00 USD | 1,480.00 USD | `-43.27%` | `8,024.00` |
| `Live` | `Long` | `0.1865` | 5,660,000.00 USD | 0.00 USD | 14,120.00 USD | `-42.65%` | `75,699.40` |
| `Live` | `Long` | `0.1875` | 5,640,000.00 USD | 0.00 USD | 5,840.00 USD | `-42.35%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 5,640,000.00 USD | 0.00 USD | 7,310.00 USD | `-42.04%` | `38,802.20` |
| `Live` | `Long` | `0.1895` | 5,630,000.00 USD | 0.00 USD | 1,050.00 USD | `-41.73%` | `5,539.20` |
| `Live` | `Long` | `0.1925` | 5,630,000.00 USD | 0.00 USD | 3,040.00 USD | `-40.81%` | `15,809.20` |
| `Live` | `Long` | `0.1935` | 5,620,000.00 USD | 0.00 USD | 2,660.00 USD | `-40.50%` | `13,738.00` |
| `Live` | `Long` | `0.1955` | 5,620,000.00 USD | 0.00 USD | 13,190.00 USD | `-39.89%` | `67,459.20` |
| `Live` | `Long` | `0.1985` | 5,610,000.00 USD | 0.00 USD | 1,100.00 USD | `-38.96%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 5,610,000.00 USD | 0.00 USD | 146,050.00 USD | `-38.66%` | `732,075.00` |
| `Live` | `Long` | `0.2015` | 5,460,000.00 USD | 0.00 USD | 2,280.00 USD | `-38.04%` | `11,332.30` |
| `Live` | `Long` | `0.2045` | 5,460,000.00 USD | 0.00 USD | 39,410.00 USD | `-37.12%` | `192,692.50` |
| `Live` | `Long` | `0.2055` | 5,420,000.00 USD | 0.00 USD | 1,060.00 USD | `-36.81%` | `5,147.80` |
| `Live` | `Long` | `0.2085` | 5,420,000.00 USD | 0.00 USD | 2,390.00 USD | `-35.89%` | `11,465.50` |
| `Live` | `Long` | `0.2105` | 5,420,000.00 USD | 0.00 USD | 30,380.00 USD | `-35.27%` | `144,300.00` |
| `Live` | `Long` | `0.2125` | 5,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-34.66%` | `31,784.00` |
| `Live` | `Long` | `0.2135` | 5,380,000.00 USD | 0.00 USD | 28,230.00 USD | `-34.35%` | `132,229.20` |
| `Live` | `Long` | `0.2145` | 5,350,000.00 USD | 0.00 USD | 1,730.00 USD | `-34.04%` | `8,080.80` |
| `Live` | `Long` | `0.2195` | 5,350,000.00 USD | 0.00 USD | 153.87 USD | `-32.51%` | `701.00` |
| `Live` | `Long` | `0.2205` | 5,350,000.00 USD | 0.00 USD | 130,550.00 USD | `-32.20%` | `592,044.70` |
| `Live` | `Long` | `0.2215` | 5,220,000.00 USD | 0.00 USD | 37,620.00 USD | `-31.89%` | `169,853.10` |
| `Live` | `Long` | `0.2225` | 5,180,000.00 USD | 0.00 USD | 667.50 USD | `-31.58%` | `3,000.00` |
| `Live` | `Long` | `0.2235` | 5,180,000.00 USD | 0.00 USD | 8,940.00 USD | `-31.28%` | `39,998.20` |
| `Live` | `Long` | `0.2285` | 5,170,000.00 USD | 0.00 USD | 11,880.00 USD | `-29.74%` | `51,980.20` |
| `Live` | `Long` | `0.2295` | 5,160,000.00 USD | 0.00 USD | 599.45 USD | `-29.43%` | `2,612.00` |
| `Live` | `Long` | `0.2305` | 5,160,000.00 USD | 0.00 USD | 45,270.00 USD | `-29.12%` | `196,402.90` |
| `Live` | `Long` | `0.2315` | 5,110,000.00 USD | 0.00 USD | 19,940.00 USD | `-28.82%` | `86,139.70` |
| `Live` | `Long` | `0.2325` | 5,090,000.00 USD | 0.00 USD | 23,290.00 USD | `-28.51%` | `100,162.80` |
| `Live` | `Long` | `0.2335` | 5,070,000.00 USD | 0.00 USD | 1,940.00 USD | `-28.20%` | `8,326.10` |
| `Live` | `Long` | `0.2345` | 5,070,000.00 USD | 0.00 USD | 18,940.00 USD | `-27.89%` | `80,768.90` |
| `Live` | `Long` | `0.2385` | 5,050,000.00 USD | 0.00 USD | 92,210.00 USD | `-26.67%` | `386,645.00` |
| `Live` | `Long` | `0.2405` | 4,960,000.00 USD | 0.00 USD | 13,650.00 USD | `-26.05%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,940,000.00 USD | 0.00 USD | 36,950.00 USD | `-25.74%` | `153,010.30` |
| `Live` | `Long` | `0.2425` | 4,910,000.00 USD | 0.00 USD | 109,880.00 USD | `-25.44%` | `453,105.40` |
| `Live` | `Long` | `0.2435` | 4,800,000.00 USD | 0.00 USD | 50,810.00 USD | `-25.13%` | `208,669.00` |
| `Live` | `Long` | `0.2445` | 4,750,000.00 USD | 0.00 USD | 637.31 USD | `-24.82%` | `2,606.60` |
| `Live` | `Long` | `0.2455` | 4,750,000.00 USD | 0.00 USD | 23,020.00 USD | `-24.51%` | `93,774.40` |
| `Live` | `Long` | `0.2475` | 4,720,000.00 USD | 0.00 USD | 9,480.00 USD | `-23.90%` | `38,294.10` |
| `Live` | `Long` | `0.2485` | 4,710,000.00 USD | 0.00 USD | 277,380.00 USD | `-23.59%` | `1,116,203.80` |
| `Live` | `Long` | `0.2495` | 4,440,000.00 USD | 0.00 USD | 28,290.00 USD | `-23.28%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,410,000.00 USD | 0.00 USD | 151,180.00 USD | `-22.98%` | `603,515.90` |
| `Live` | `Long` | `0.2515` | 4,260,000.00 USD | 0.00 USD | 16,230.00 USD | `-22.67%` | `64,516.00` |
| `Live` | `Long` | `0.2525` | 4,240,000.00 USD | 0.00 USD | 5,390.00 USD | `-22.36%` | `21,359.60` |
| `Live` | `Long` | `0.2535` | 4,230,000.00 USD | 0.00 USD | 68,280.00 USD | `-22.05%` | `269,343.30` |
| `Live` | `Long` | `0.2545` | 4,170,000.00 USD | 0.00 USD | 22,030.00 USD | `-21.75%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 4,140,000.00 USD | 0.00 USD | 59,960.00 USD | `-21.44%` | `234,689.20` |
| `Live` | `Long` | `0.2565` | 4,080,000.00 USD | 0.00 USD | 18,780.00 USD | `-21.13%` | `73,212.10` |
| `Live` | `Long` | `0.2585` | 4,070,000.00 USD | 0.00 USD | 18,900.00 USD | `-20.52%` | `73,130.00` |
| `Live` | `Long` | `0.2595` | 4,050,000.00 USD | 0.00 USD | 46,140.00 USD | `-20.21%` | `177,797.60` |
| `Live` | `Long` | `0.2605` | 4,000,000.00 USD | 0.00 USD | 175,840.00 USD | `-19.90%` | `675,000.00` |
| `Live` | `Long` | `0.2615` | 3,820,000.00 USD | 0.00 USD | 1,700.00 USD | `-19.59%` | `6,486.80` |
| `Live` | `Long` | `0.2635` | 3,820,000.00 USD | 0.00 USD | 56,020.00 USD | `-18.98%` | `212,594.20` |
| `Live` | `Long` | `0.2645` | 3,770,000.00 USD | 0.00 USD | 5,390.00 USD | `-18.67%` | `20,384.10` |
| `Live` | `Long` | `0.2655` | 3,760,000.00 USD | 0.00 USD | 10,710.00 USD | `-18.36%` | `40,345.40` |
| `Live` | `Long` | `0.2665` | 3,750,000.00 USD | 0.00 USD | 25,020.00 USD | `-18.06%` | `93,885.20` |
| `Live` | `Long` | `0.2675` | 3,730,000.00 USD | 0.00 USD | 5,980.00 USD | `-17.75%` | `22,343.80` |
| `Live` | `Long` | `0.2685` | 3,720,000.00 USD | 0.00 USD | 20,470.00 USD | `-17.44%` | `76,236.40` |
| `Live` | `Long` | `0.2695` | 3,700,000.00 USD | 0.00 USD | 7,750.00 USD | `-17.13%` | `28,742.90` |
| `Live` | `Long` | `0.2705` | 3,690,000.00 USD | 0.00 USD | 7,870.00 USD | `-16.83%` | `29,086.50` |
| `Live` | `Long` | `0.2715` | 3,680,000.00 USD | 0.00 USD | 46,010.00 USD | `-16.52%` | `169,467.20` |
| `Live` | `Long` | `0.2735` | 3,640,000.00 USD | 0.00 USD | 39,180.00 USD | `-15.90%` | `143,237.00` |
| `Live` | `Long` | `0.2745` | 3,600,000.00 USD | 0.00 USD | 303,830.00 USD | `-15.60%` | `1,106,858.30` |
| `Live` | `Long` | `0.2755` | 3,300,000.00 USD | 0.00 USD | 92,550.00 USD | `-15.29%` | `335,951.70` |
| `Live` | `Long` | `0.2765` | 3,200,000.00 USD | 0.00 USD | 61,300.00 USD | `-14.98%` | `221,700.60` |
| `Live` | `Long` | `0.2775` | 3,140,000.00 USD | 0.00 USD | 76,570.00 USD | `-14.67%` | `275,926.10` |
| `Live` | `Long` | `0.2785` | 3,060,000.00 USD | 0.00 USD | 3,950.00 USD | `-14.37%` | `14,195.20` |
| `Live` | `Long` | `0.2795` | 3,060,000.00 USD | 0.00 USD | 70,670.00 USD | `-14.06%` | `252,856.00` |
| `Live` | `Long` | `0.2805` | 2,990,000.00 USD | 0.00 USD | 129,920.00 USD | `-13.75%` | `463,183.60` |
| `Live` | `Long` | `0.2815` | 2,860,000.00 USD | 0.00 USD | 2,990.00 USD | `-13.44%` | `10,607.70` |
| `Live` | `Long` | `0.2825` | 2,860,000.00 USD | 0.00 USD | 84,670.00 USD | `-13.14%` | `299,723.00` |
| `Live` | `Long` | `0.2835` | 2,770,000.00 USD | 0.00 USD | 332,980.00 USD | `-12.83%` | `1,174,526.90` |
| `Live` | `Long` | `0.2845` | 2,440,000.00 USD | 0.00 USD | 17,510.00 USD | `-12.52%` | `61,548.90` |
| `Live` | `Long` | `0.2855` | 2,420,000.00 USD | 0.00 USD | 23,820.00 USD | `-12.21%` | `83,420.90` |
| `Live` | `Long` | `0.2865` | 2,400,000.00 USD | 0.00 USD | 387,500.00 USD | `-11.91%` | `1,352,543.70` |
| `Live` | `Long` | `0.2875` | 2,010,000.00 USD | 0.00 USD | 124,400.00 USD | `-11.60%` | `432,709.60` |
| `Live` | `Long` | `0.2885` | 1,890,000.00 USD | 0.00 USD | 566,580.00 USD | `-11.29%` | `1,963,870.80` |
| `Live` | `Long` | `0.2895` | 1,320,000.00 USD | 0.00 USD | 14,440.00 USD | `-10.98%` | `49,895.00` |
| `Live` | `Long` | `0.2905` | 1,310,000.00 USD | 0.00 USD | 203,170.00 USD | `-10.68%` | `699,392.20` |
| `Live` | `Long` | `0.2915` | 1,100,000.00 USD | 0.00 USD | 30,170.00 USD | `-10.37%` | `103,482.00` |
| `Live` | `Long` | `0.2925` | 1,070,000.00 USD | 0.00 USD | 10,690.00 USD | `-10.06%` | `36,560.50` |
| `Live` | `Long` | `0.2935` | 1,060,000.00 USD | 0.00 USD | 7,460.00 USD | `-9.75%` | `25,431.30` |
| `Live` | `Long` | `0.2945` | 1,050,000.00 USD | 0.00 USD | 45,430.00 USD | `-9.45%` | `154,265.90` |
| `Live` | `Long` | `0.2955` | 1,010,000.00 USD | 0.00 USD | 12,930.00 USD | `-9.14%` | `43,740.70` |
| `Live` | `Long` | `0.2965` | 995,310.00 USD | 0.00 USD | 12,410.00 USD | `-8.83%` | `41,857.00` |
| `Live` | `Long` | `0.2975` | 982,900.00 USD | 0.00 USD | 270,290.00 USD | `-8.52%` | `908,536.40` |
| `Live` | `Long` | `0.2985` | 712,610.00 USD | 0.00 USD | 65,840.00 USD | `-8.22%` | `220,553.00` |
| `Live` | `Long` | `0.2995` | 646,770.00 USD | 0.00 USD | 8,320.00 USD | `-7.91%` | `27,778.80` |
| `Live` | `Long` | `0.3005` | 638,450.00 USD | 0.00 USD | 25,600.00 USD | `-7.60%` | `85,188.40` |
| `Live` | `Long` | `0.3015` | 612,850.00 USD | 0.00 USD | 4,260.00 USD | `-7.29%` | `14,122.10` |
| `Live` | `Long` | `0.3025` | 608,590.00 USD | 0.00 USD | 5,630.00 USD | `-6.99%` | `18,610.70` |
| `Live` | `Long` | `0.3035` | 602,960.00 USD | 0.00 USD | 11,520.00 USD | `-6.68%` | `37,948.50` |
| `Live` | `Long` | `0.3045` | 591,450.00 USD | 0.00 USD | 768.34 USD | `-6.37%` | `2,523.30` |
| `Live` | `Long` | `0.3055` | 590,680.00 USD | 0.00 USD | 72,810.00 USD | `-6.06%` | `238,322.70` |
| `Live` | `Long` | `0.3065` | 517,870.00 USD | 0.00 USD | 202,300.00 USD | `-5.76%` | `660,045.70` |
| `Live` | `Long` | `0.3075` | 315,570.00 USD | 0.00 USD | 61,790.00 USD | `-5.45%` | `200,954.20` |
| `Live` | `Long` | `0.3085` | 253,770.00 USD | 0.00 USD | 23,710.00 USD | `-5.14%` | `76,867.60` |
| `Live` | `Long` | `0.3095` | 230,060.00 USD | 0.00 USD | 19,620.00 USD | `-4.83%` | `63,403.90` |
| `Live` | `Long` | `0.3105` | 210,440.00 USD | 0.00 USD | 40,680.00 USD | `-4.53%` | `131,020.90` |
| `Live` | `Long` | `0.3115` | 169,760.00 USD | 0.00 USD | 81,680.00 USD | `-4.22%` | `262,212.50` |
| `Live` | `Long` | `0.3135` | 88,080.00 USD | 0.00 USD | 568.38 USD | `-3.60%` | `1,813.00` |
| `Live` | `Long` | `0.3155` | 87,510.00 USD | 0.00 USD | 14,410.00 USD | `-2.99%` | `45,681.90` |
| `Live` | `Long` | `0.3165` | 73,090.00 USD | 0.00 USD | 2,080.00 USD | `-2.68%` | `6,582.50` |
| `Live` | `Long` | `0.3175` | 71,010.00 USD | 0.00 USD | 27,670.00 USD | `-2.37%` | `87,153.10` |
| `Live` | `Long` | `0.3185` | 43,340.00 USD | 0.00 USD | 41,290.00 USD | `-2.07%` | `129,650.90` |
| `Live` | `Long` | `0.3195` | 2,050.00 USD | 0.00 USD | 2,050.00 USD | `-1.76%` | `6,405.40` |
| `Live` | `Short` | `0.3425` | 12,100.00 USD | 12,100.00 USD | 0.00 USD | `+5.31%` | `35,339.80` |
| `Live` | `Short` | `0.3455` | 13,500.00 USD | 1,400.00 USD | 0.00 USD | `+6.24%` | `4,046.20` |
| `Live` | `Short` | `0.3465` | 14,020.00 USD | 522.80 USD | 0.00 USD | `+6.54%` | `1,508.80` |
| `Live` | `Short` | `0.3495` | 14,850.00 USD | 830.24 USD | 0.00 USD | `+7.47%` | `2,375.50` |
| `Live` | `Short` | `0.3505` | 18,300.00 USD | 3,440.00 USD | 0.00 USD | `+7.77%` | `9,825.80` |
| `Live` | `Short` | `0.3575` | 18,800.00 USD | 497.00 USD | 0.00 USD | `+9.93%` | `1,390.20` |
| `Live` | `Short` | `0.3625` | 20,890.00 USD | 2,100.00 USD | 0.00 USD | `+11.46%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 22,990.00 USD | 2,100.00 USD | 0.00 USD | `+13.00%` | `5,705.10` |
| `Live` | `Short` | `0.3685` | 23,110.00 USD | 118.44 USD | 0.00 USD | `+13.31%` | `321.40` |
| `Live` | `Short` | `0.3885` | 23,210.00 USD | 103.81 USD | 0.00 USD | `+19.46%` | `267.20` |
| `Live` | `Short` | `0.4025` | 23,690.00 USD | 477.49 USD | 0.00 USD | `+23.76%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 23,930.00 USD | 236.85 USD | 0.00 USD | `+24.07%` | `587.00` |
| `Live` | `Short` | `0.4205` | 25,620.00 USD | 1,700.00 USD | 0.00 USD | `+29.30%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 25,740.00 USD | 115.25 USD | 0.00 USD | `+30.53%` | `271.50` |
| `Live` | `Short` | `0.4265` | 27,100.00 USD | 1,370.00 USD | 0.00 USD | `+31.14%` | `3,205.50` |
| `Live` | `Short` | `0.4445` | 27,990.00 USD | 889.00 USD | 0.00 USD | `+36.68%` | `2,000.00` |
| `Live` | `Short` | `0.4475` | 28,990.00 USD | 996.58 USD | 0.00 USD | `+37.60%` | `2,227.00` |
| `Live` | `Short` | `0.4575` | 39,470.00 USD | 10,480.00 USD | 0.00 USD | `+40.67%` | `22,906.80` |
| `Live` | `Short` | `0.4665` | 39,790.00 USD | 325.01 USD | 0.00 USD | `+43.44%` | `696.70` |
| `Live` | `Short` | `0.5015` | 39,950.00 USD | 160.23 USD | 0.00 USD | `+54.20%` | `319.50` |
| `Live` | `Short` | `0.5065` | 100,730.00 USD | 60,780.00 USD | 0.00 USD | `+55.74%` | `120,000.00` |
| `Live` | `Short` | `0.5105` | 472,890.00 USD | 372,150.00 USD | 0.00 USD | `+56.97%` | `729,000.00` |
| `Live` | `Short` | `0.5155` | 473,320.00 USD | 428.28 USD | 0.00 USD | `+58.51%` | `830.80` |
| `Live` | `Short` | `0.5315` | 487,830.00 USD | 14,510.00 USD | 0.00 USD | `+63.43%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 490,690.00 USD | 2,860.00 USD | 0.00 USD | `+71.11%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 508,080.00 USD | 17,400.00 USD | 0.00 USD | `+79.42%` | `29,816.80` |
| `Live` | `Short` | `0.5875` | 938,130.00 USD | 430,050.00 USD | 0.00 USD | `+80.65%` | `732,000.00` |
| `Live` | `Short` | `0.6215` | 1,060,000.00 USD | 125,110.00 USD | 0.00 USD | `+91.10%` | `201,296.00` |
| `Live` | `Short` | `0.6315` | 1,060,000.00 USD | 463.33 USD | 0.00 USD | `+94.18%` | `733.70` |
| `Live` | `Short` | `0.6465` | 1,060,000.00 USD | 121.61 USD | 0.00 USD | `+98.79%` | `188.10` |
| `Live` | `Short` | `0.6475` | 1,070,000.00 USD | 5,730.00 USD | 0.00 USD | `+99.10%` | `8,843.60` |
| `Live` | `Short` | `0.6485` | 1,070,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.40%` | `1,692.90` |

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
  * Current Rate: `-1.12K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0022%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0062%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0036%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

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
| `5m` | -11,820.00 USD | 593,970.00 USD | **`ACCUMULATION`** |
| `15m` | -42,240.00 USD | -931,360.00 USD | **`DISTRIBUTION`** |
| `30m` | -124,680.00 USD | -1,240,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -208,460.00 USD | -2,100,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -240,170.00 USD | -1,920,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -532,570.00 USD | -3,630,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -487,390.00 USD | -4,320,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -288,490.00 USD | -4,500,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -525,090.00 USD | -4,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -558,290.00 USD | -6,780,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,900,000.00 USD | -17,420,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,520,000.00 USD | -60,250,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.82K` | 15m=`-42.24K` | 1h=`-208.46K` | 24h=`-558.29K`
* Futures Capital Netflows: 5m=`+593.97K` | 15m=`-931.36K` | 1h=`-2.10M` | 24h=`-6.78M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3100` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2727` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.4200`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3230` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3603` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.2130`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3145`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
