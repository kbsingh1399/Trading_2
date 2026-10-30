# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:53:54 IST` (`2026-10-30 09:23:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2720` | **Live Ask Quote**: `0.2950` | **Mid Price**: `0.2835`
- **Spread Points**: `23.00` | **Spread BPS**: `811.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2712` | VWAP Z-Score: `+0.08` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0042` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `53.63` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3027` | Lower -3.00σ Band: `0.2397`
  * Upper +2.51σ Band: `0.2975` | Lower -2.51σ Band: `0.2448`
  * Upper +2.01σ Band: `0.2923` | Lower -2.01σ Band: `0.2501`
  * Upper +2.00σ Band: `0.2922` | Lower -2.00σ Band: `0.2502`
  * Upper +1.28σ Band: `0.2846` | Lower -1.28σ Band: `0.2577`
  * Upper +1.00σ Band: `0.2817` | Lower -1.00σ Band: `0.2607`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2695` | EMA-20=`0.2687` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2773` (Slope: `+0.0000`) | EMA-100=`0.2900`
  * Institutional Anchors: EMA-144=`0.2970` | EMA-200=`0.3031` (Slope: `-1.4410`) | EMA-233=`0.3058`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2880` (Distance: `-1.51%`)
  * Point of Control (POC) = `0.2630` (Distance: `+7.78%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+10.35%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3130`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2750` | Low=`0.2570`
  * New York Session (13:00-21:00 UTC): High=`0.2852` | Low=`0.2818`
  * Initial Balance (First Hour): IB High=`0.2640` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2824` - `0.2846`
  * Optimal Trade Entry (OTE 0.705): `0.2841`
  * Structural Invalidation Anchor (0.786): `0.2858`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:52:21 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1833` | `0x12d2...f97f` | `LONG` | 1,125,780.47 USD | `3,972,828.70` | `0.3272` | `0.2832` | `0.000000` | -174,058.27 USD | `-15.46%` | `10X Cross` |

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
| `Live` | `Long` | `0.0575` | 2,420,000.00 USD | 0.00 USD | 129.20 USD | `-79.75%` | `2,246.90` |
| `Live` | `Long` | `0.0585` | 2,420,000.00 USD | 0.00 USD | 219.49 USD | `-79.39%` | `3,752.00` |
| `Live` | `Long` | `0.0665` | 2,420,000.00 USD | 0.00 USD | 2,240.00 USD | `-76.58%` | `33,687.90` |
| `Live` | `Long` | `0.0685` | 2,420,000.00 USD | 0.00 USD | 2,640.00 USD | `-75.87%` | `38,602.60` |
| `Live` | `Long` | `0.0735` | 2,420,000.00 USD | 0.00 USD | 116.27 USD | `-74.11%` | `1,581.90` |
| `Live` | `Long` | `0.0745` | 2,420,000.00 USD | 0.00 USD | 374.44 USD | `-73.76%` | `5,026.00` |
| `Live` | `Long` | `0.0755` | 2,420,000.00 USD | 0.00 USD | 3,840.00 USD | `-73.41%` | `50,846.60` |
| `Live` | `Long` | `0.0765` | 2,410,000.00 USD | 0.00 USD | 13,880.00 USD | `-73.05%` | `181,411.80` |
| `Live` | `Long` | `0.0795` | 2,400,000.00 USD | 0.00 USD | 2,350.00 USD | `-72.00%` | `29,622.60` |
| `Live` | `Long` | `0.0865` | 2,400,000.00 USD | 0.00 USD | 9,710.00 USD | `-69.53%` | `112,309.00` |
| `Live` | `Long` | `0.0915` | 2,390,000.00 USD | 0.00 USD | 687.55 USD | `-67.77%` | `7,514.20` |
| `Live` | `Long` | `0.0965` | 2,390,000.00 USD | 0.00 USD | 460.38 USD | `-66.01%` | `4,770.80` |
| `Live` | `Long` | `0.1105` | 2,390,000.00 USD | 0.00 USD | 1,080.00 USD | `-61.08%` | `9,765.50` |
| `Live` | `Long` | `0.1175` | 2,390,000.00 USD | 0.00 USD | 1,380.00 USD | `-58.61%` | `11,739.70` |
| `Live` | `Long` | `0.1215` | 2,390,000.00 USD | 0.00 USD | 7,770.00 USD | `-57.20%` | `63,917.90` |
| `Live` | `Long` | `0.1225` | 2,380,000.00 USD | 0.00 USD | 116.35 USD | `-56.85%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,380,000.00 USD | 0.00 USD | 4,300.00 USD | `-55.80%` | `34,264.40` |
| `Live` | `Long` | `0.1275` | 2,370,000.00 USD | 0.00 USD | 335.02 USD | `-55.09%` | `2,627.60` |
| `Live` | `Long` | `0.1365` | 2,370,000.00 USD | 0.00 USD | 21,840.00 USD | `-51.92%` | `160,000.00` |
| `Live` | `Long` | `0.1435` | 2,350,000.00 USD | 0.00 USD | 6,200.00 USD | `-49.46%` | `43,210.20` |
| `Live` | `Long` | `0.1455` | 2,340,000.00 USD | 0.00 USD | 1,160.00 USD | `-48.75%` | `8,000.00` |
| `Live` | `Long` | `0.1465` | 2,340,000.00 USD | 0.00 USD | 12,380.00 USD | `-48.40%` | `84,498.00` |
| `Live` | `Long` | `0.1495` | 2,330,000.00 USD | 0.00 USD | 1,200.00 USD | `-47.34%` | `8,042.60` |
| `Live` | `Long` | `0.1545` | 2,330,000.00 USD | 0.00 USD | 3,860.00 USD | `-45.58%` | `25,000.00` |
| `Live` | `Long` | `0.1595` | 2,330,000.00 USD | 0.00 USD | 21,090.00 USD | `-43.82%` | `132,229.20` |
| `Live` | `Long` | `0.1625` | 2,310,000.00 USD | 0.00 USD | 19,500.00 USD | `-42.76%` | `120,000.00` |
| `Live` | `Long` | `0.1645` | 2,290,000.00 USD | 0.00 USD | 2,500.00 USD | `-42.06%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,280,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.35%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 2,280,000.00 USD | 0.00 USD | 278.30 USD | `-40.30%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,280,000.00 USD | 0.00 USD | 33,220.00 USD | `-39.59%` | `193,709.50` |
| `Live` | `Long` | `0.1725` | 2,240,000.00 USD | 0.00 USD | 5,200.00 USD | `-39.24%` | `30,143.90` |
| `Live` | `Long` | `0.1735` | 2,240,000.00 USD | 0.00 USD | 3,990.00 USD | `-38.89%` | `22,973.90` |
| `Live` | `Long` | `0.1755` | 2,240,000.00 USD | 0.00 USD | 136.98 USD | `-38.18%` | `780.50` |
| `Live` | `Long` | `0.1765` | 2,240,000.00 USD | 0.00 USD | 1,340.00 USD | `-37.83%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,230,000.00 USD | 0.00 USD | 14,130.00 USD | `-37.48%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,220,000.00 USD | 0.00 USD | 12,010.00 USD | `-37.13%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 2,210,000.00 USD | 0.00 USD | 5,890.00 USD | `-36.78%` | `32,795.10` |
| `Live` | `Long` | `0.1805` | 2,200,000.00 USD | 0.00 USD | 14,020.00 USD | `-36.42%` | `77,683.60` |
| `Live` | `Long` | `0.1815` | 2,190,000.00 USD | 0.00 USD | 27,810.00 USD | `-36.07%` | `153,246.60` |
| `Live` | `Long` | `0.1825` | 2,160,000.00 USD | 0.00 USD | 16,120.00 USD | `-35.72%` | `88,308.30` |
| `Live` | `Long` | `0.1835` | 2,140,000.00 USD | 0.00 USD | 179.10 USD | `-35.37%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,140,000.00 USD | 0.00 USD | 25,400.00 USD | `-35.01%` | `137,653.50` |
| `Live` | `Long` | `0.1875` | 2,120,000.00 USD | 0.00 USD | 5,840.00 USD | `-33.96%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 2,110,000.00 USD | 0.00 USD | 1,660.00 USD | `-33.61%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.25%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,110,000.00 USD | 0.00 USD | 39,050.00 USD | `-32.90%` | `205,000.00` |
| `Live` | `Long` | `0.1925` | 2,070,000.00 USD | 0.00 USD | 3,050.00 USD | `-32.20%` | `15,821.40` |
| `Live` | `Long` | `0.1935` | 2,070,000.00 USD | 0.00 USD | 2,600.00 USD | `-31.84%` | `13,453.50` |
| `Live` | `Long` | `0.1945` | 2,070,000.00 USD | 0.00 USD | 6,140.00 USD | `-31.49%` | `31,561.00` |
| `Live` | `Long` | `0.1955` | 2,060,000.00 USD | 0.00 USD | 13,830.00 USD | `-31.14%` | `70,734.60` |
| `Live` | `Long` | `0.1975` | 2,050,000.00 USD | 0.00 USD | 7,900.00 USD | `-30.44%` | `40,000.00` |
| `Live` | `Long` | `0.1985` | 2,040,000.00 USD | 0.00 USD | 1,100.00 USD | `-30.08%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 2,040,000.00 USD | 0.00 USD | 3,430.00 USD | `-29.73%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 2,030,000.00 USD | 0.00 USD | 119,060.00 USD | `-29.03%` | `590,886.10` |
| `Live` | `Long` | `0.2045` | 1,910,000.00 USD | 0.00 USD | 18,550.00 USD | `-27.97%` | `90,714.00` |
| `Live` | `Long` | `0.2065` | 1,900,000.00 USD | 0.00 USD | 1,040.00 USD | `-27.27%` | `5,050.00` |
| `Live` | `Long` | `0.2075` | 1,890,000.00 USD | 0.00 USD | 41,500.00 USD | `-26.91%` | `200,000.00` |
| `Live` | `Long` | `0.2085` | 1,850,000.00 USD | 0.00 USD | 3,330.00 USD | `-26.56%` | `15,982.60` |
| `Live` | `Long` | `0.2095` | 1,850,000.00 USD | 0.00 USD | 70,590.00 USD | `-26.21%` | `336,947.40` |
| `Live` | `Long` | `0.2115` | 1,780,000.00 USD | 0.00 USD | 55,550.00 USD | `-25.50%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,720,000.00 USD | 0.00 USD | 1,240.00 USD | `-25.15%` | `5,840.90` |
| `Live` | `Long` | `0.2145` | 1,720,000.00 USD | 0.00 USD | 68,790.00 USD | `-24.45%` | `320,696.20` |
| `Live` | `Long` | `0.2165` | 1,650,000.00 USD | 0.00 USD | 6,720.00 USD | `-23.74%` | `31,044.10` |
| `Live` | `Long` | `0.2175` | 1,650,000.00 USD | 0.00 USD | 9,060.00 USD | `-23.39%` | `41,666.50` |
| `Live` | `Long` | `0.2195` | 1,640,000.00 USD | 0.00 USD | 899.88 USD | `-22.69%` | `4,099.70` |
| `Live` | `Long` | `0.2205` | 1,640,000.00 USD | 0.00 USD | 8,750.00 USD | `-22.33%` | `39,694.10` |
| `Live` | `Long` | `0.2215` | 1,630,000.00 USD | 0.00 USD | 128,040.00 USD | `-21.98%` | `578,059.90` |
| `Live` | `Long` | `0.2245` | 1,500,000.00 USD | 0.00 USD | 7,870.00 USD | `-20.93%` | `35,072.00` |
| `Live` | `Long` | `0.2255` | 1,490,000.00 USD | 0.00 USD | 676.50 USD | `-20.57%` | `3,000.00` |
| `Live` | `Long` | `0.2285` | 1,490,000.00 USD | 0.00 USD | 19,240.00 USD | `-19.52%` | `84,190.60` |
| `Live` | `Long` | `0.2295` | 1,470,000.00 USD | 0.00 USD | 160.65 USD | `-19.16%` | `700.00` |
| `Live` | `Long` | `0.2305` | 1,470,000.00 USD | 0.00 USD | 74,180.00 USD | `-18.81%` | `321,829.10` |
| `Live` | `Long` | `0.2315` | 1,400,000.00 USD | 0.00 USD | 25,460.00 USD | `-18.46%` | `109,988.70` |
| `Live` | `Long` | `0.2325` | 1,370,000.00 USD | 0.00 USD | 11,400.00 USD | `-18.11%` | `49,039.80` |
| `Live` | `Long` | `0.2335` | 1,360,000.00 USD | 0.00 USD | 1,940.00 USD | `-17.76%` | `8,326.10` |
| `Live` | `Long` | `0.2345` | 1,360,000.00 USD | 0.00 USD | 336.32 USD | `-17.40%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,360,000.00 USD | 0.00 USD | 20,670.00 USD | `-17.05%` | `87,761.90` |
| `Live` | `Long` | `0.2365` | 1,340,000.00 USD | 0.00 USD | 25,230.00 USD | `-16.70%` | `106,660.90` |
| `Live` | `Long` | `0.2375` | 1,310,000.00 USD | 0.00 USD | 5,610.00 USD | `-16.35%` | `23,636.90` |
| `Live` | `Long` | `0.2385` | 1,310,000.00 USD | 0.00 USD | 92,430.00 USD | `-15.99%` | `387,531.30` |
| `Live` | `Long` | `0.2395` | 1,210,000.00 USD | 0.00 USD | 3,620.00 USD | `-15.64%` | `15,104.80` |
| `Live` | `Long` | `0.2405` | 1,210,000.00 USD | 0.00 USD | 37,700.00 USD | `-15.29%` | `156,745.50` |
| `Live` | `Long` | `0.2415` | 1,170,000.00 USD | 0.00 USD | 32,410.00 USD | `-14.94%` | `134,189.70` |
| `Live` | `Long` | `0.2425` | 1,140,000.00 USD | 0.00 USD | 108,620.00 USD | `-14.59%` | `447,937.20` |
| `Live` | `Long` | `0.2435` | 1,030,000.00 USD | 0.00 USD | 45,960.00 USD | `-14.23%` | `188,765.20` |
| `Live` | `Long` | `0.2445` | 986,150.00 USD | 0.00 USD | 123,540.00 USD | `-13.88%` | `505,283.30` |
| `Live` | `Long` | `0.2455` | 862,610.00 USD | 0.00 USD | 306,750.00 USD | `-13.53%` | `1,249,500.00` |
| `Live` | `Long` | `0.2465` | 555,860.00 USD | 0.00 USD | 5,140.00 USD | `-13.18%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 550,720.00 USD | 0.00 USD | 10,700.00 USD | `-12.82%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 540,020.00 USD | 0.00 USD | 74,760.00 USD | `-12.47%` | `300,834.70` |
| `Live` | `Long` | `0.2495` | 465,270.00 USD | 0.00 USD | 28,290.00 USD | `-12.12%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 436,970.00 USD | 0.00 USD | 113.35 USD | `-11.77%` | `452.50` |
| `Live` | `Long` | `0.2515` | 436,860.00 USD | 0.00 USD | 18,010.00 USD | `-11.42%` | `71,592.20` |
| `Live` | `Long` | `0.2535` | 418,850.00 USD | 0.00 USD | 6,370.00 USD | `-10.71%` | `25,132.30` |
| `Live` | `Long` | `0.2545` | 412,480.00 USD | 0.00 USD | 56,730.00 USD | `-10.36%` | `222,905.40` |
| `Live` | `Long` | `0.2555` | 355,750.00 USD | 0.00 USD | 48,600.00 USD | `-10.01%` | `190,199.50` |
| `Live` | `Long` | `0.2565` | 307,160.00 USD | 0.00 USD | 1,640.00 USD | `-9.65%` | `6,408.20` |
| `Live` | `Long` | `0.2575` | 305,510.00 USD | 0.00 USD | 60,880.00 USD | `-9.30%` | `236,436.40` |
| `Live` | `Long` | `0.2585` | 244,630.00 USD | 0.00 USD | 29,970.00 USD | `-8.95%` | `115,931.80` |
| `Live` | `Long` | `0.2595` | 214,660.00 USD | 0.00 USD | 101,500.00 USD | `-8.60%` | `391,140.80` |
| `Live` | `Long` | `0.2605` | 113,160.00 USD | 0.00 USD | 92,800.00 USD | `-8.25%` | `356,229.60` |
| `Live` | `Long` | `0.2615` | 20,360.00 USD | 0.00 USD | 6,160.00 USD | `-7.89%` | `23,568.20` |
| `Live` | `Long` | `0.2625` | 14,200.00 USD | 0.00 USD | 342.09 USD | `-7.54%` | `1,303.20` |
| `Live` | `Long` | `0.2635` | 13,860.00 USD | 0.00 USD | 126.69 USD | `-7.19%` | `480.80` |
| `Live` | `Long` | `0.2645` | 13,730.00 USD | 0.00 USD | 3,030.00 USD | `-6.84%` | `11,437.60` |
| `Live` | `Long` | `0.2695` | 10,710.00 USD | 0.00 USD | 9,840.00 USD | `-5.08%` | `36,528.30` |
| `Live` | `Long` | `0.2805` | 863.38 USD | 0.00 USD | 863.38 USD | `-1.20%` | `3,078.00` |
| `Live` | `Short` | `0.2965` | 384.41 USD | 384.41 USD | 0.00 USD | `+4.43%` | `1,296.50` |
| `Live` | `Short` | `0.2975` | 5,880.00 USD | 5,500.00 USD | 0.00 USD | `+4.79%` | `18,482.00` |
| `Live` | `Short` | `0.3035` | 22,100.00 USD | 16,220.00 USD | 0.00 USD | `+6.90%` | `53,428.40` |
| `Live` | `Short` | `0.3065` | 23,220.00 USD | 1,120.00 USD | 0.00 USD | `+7.96%` | `3,643.80` |
| `Live` | `Short` | `0.3215` | 28,600.00 USD | 5,380.00 USD | 0.00 USD | `+13.24%` | `16,745.80` |
| `Live` | `Short` | `0.3235` | 29,350.00 USD | 747.16 USD | 0.00 USD | `+13.94%` | `2,309.60` |
| `Live` | `Short` | `0.3415` | 29,450.00 USD | 103.54 USD | 0.00 USD | `+20.28%` | `303.20` |
| `Live` | `Short` | `0.3485` | 29,860.00 USD | 413.95 USD | 0.00 USD | `+22.75%` | `1,187.80` |
| `Live` | `Short` | `0.3575` | 29,960.00 USD | 100.14 USD | 0.00 USD | `+25.92%` | `280.10` |
| `Live` | `Short` | `0.3625` | 32,060.00 USD | 2,100.00 USD | 0.00 USD | `+27.68%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 34,160.00 USD | 2,100.00 USD | 0.00 USD | `+29.44%` | `5,705.10` |
| `Live` | `Short` | `0.3865` | 34,280.00 USD | 119.35 USD | 0.00 USD | `+36.13%` | `308.80` |
| `Live` | `Short` | `0.3885` | 34,380.00 USD | 103.81 USD | 0.00 USD | `+36.84%` | `267.20` |
| `Live` | `Short` | `0.3965` | 81,960.00 USD | 47,580.00 USD | 0.00 USD | `+39.66%` | `120,000.00` |
| `Live` | `Short` | `0.4025` | 82,200.00 USD | 238.76 USD | 0.00 USD | `+41.77%` | `593.20` |
| `Live` | `Short` | `0.4035` | 82,360.00 USD | 165.84 USD | 0.00 USD | `+42.12%` | `411.00` |
| `Live` | `Short` | `0.4205` | 84,060.00 USD | 1,700.00 USD | 0.00 USD | `+48.11%` | `4,032.60` |
| `Live` | `Short` | `0.4385` | 403,730.00 USD | 319,670.00 USD | 0.00 USD | `+54.45%` | `729,000.00` |
| `Live` | `Short` | `0.4445` | 404,390.00 USD | 666.75 USD | 0.00 USD | `+56.56%` | `1,500.00` |
| `Live` | `Short` | `0.4515` | 404,610.00 USD | 212.84 USD | 0.00 USD | `+59.03%` | `471.40` |
| `Live` | `Short` | `0.4525` | 406,060.00 USD | 1,450.00 USD | 0.00 USD | `+59.38%` | `3,205.50` |
| `Live` | `Short` | `0.4565` | 407,070.00 USD | 1,020.00 USD | 0.00 USD | `+60.79%` | `2,227.00` |
| `Live` | `Short` | `0.4725` | 430,920.00 USD | 23,840.00 USD | 0.00 USD | `+66.43%` | `50,463.70` |
| `Live` | `Short` | `0.5085` | 431,040.00 USD | 120.62 USD | 0.00 USD | `+79.11%` | `237.20` |
| `Live` | `Short` | `0.5155` | 431,470.00 USD | 428.28 USD | 0.00 USD | `+81.57%` | `830.80` |
| `Live` | `Short` | `0.5315` | 445,980.00 USD | 14,510.00 USD | 0.00 USD | `+87.21%` | `27,300.00` |
| `Live` | `Short` | `0.5455` | 446,090.00 USD | 108.72 USD | 0.00 USD | `+92.14%` | `199.30` |
| `Live` | `Short` | `0.5565` | 448,940.00 USD | 2,860.00 USD | 0.00 USD | `+96.01%` | `5,135.90` |
| `Live` | `Short` | `0.5675` | 449,500.00 USD | 552.97 USD | 0.00 USD | `+99.89%` | `974.40` |

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
  * Current Rate: `-3.80K` | Last 24h: `968.79` | Last 3d: `19.73K` | Last 7d: `53.52K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0161%` | **USDT OKX** | `-0.0303%` |
| **USDT Bybit** | `-0.0043%` | **USDT KuCoin** | `-0.0444%` |
| **USDT MEXC** | `-0.0298%` | **USDT BingX** | `0.0079%` |
| **USDT Gate** | `-0.0071%` | **USDT Bitget** | `0.0069%` |
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
| `5m` | -21,810.00 USD | 59,010.00 USD | **`ACCUMULATION`** |
| `15m` | -28,690.00 USD | 80,990.00 USD | **`ACCUMULATION`** |
| `30m` | 27,910.00 USD | 390,740.00 USD | **`ACCUMULATION`** |
| `1h` | 18,340.00 USD | 240,300.00 USD | **`ACCUMULATION`** |
| `2h` | 372,730.00 USD | 2,170,000.00 USD | **`ACCUMULATION`** |
| `4h` | 462,800.00 USD | 2,100,000.00 USD | **`ACCUMULATION`** |
| `6h` | 459,900.00 USD | 2,290,000.00 USD | **`ACCUMULATION`** |
| `8h` | 148,400.00 USD | -3,310,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 97,770.00 USD | -4,350,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -308,540.00 USD | -9,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,750,000.00 USD | -20,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,780,000.00 USD | -65,540,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-21.81K` | 15m=`-28.69K` | 1h=`+18.34K` | 24h=`-308.54K`
* Futures Capital Netflows: 5m=`+59.01K` | 15m=`+80.99K` | 1h=`+240.30K` | 24h=`-9.52M`
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
  * `2026-10-30 14:41:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:10:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2570` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2174` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.3720`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2880` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3276` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.1730`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2858`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
