# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 00:56:34 IST` (`2026-10-29 19:26:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.62` | **Live Ask Quote**: `11.70` | **Mid Price**: `11.66`
- **Spread Points**: `85.00` | **Spread BPS**: `72.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.66` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.74` | Lower -3.00σ Band: `11.58`
  * Upper +2.51σ Band: `11.73` | Lower -2.51σ Band: `11.60`
  * Upper +2.01σ Band: `11.71` | Lower -2.01σ Band: `11.61`
  * Upper +2.00σ Band: `11.71` | Lower -2.00σ Band: `11.61`
  * Upper +1.28σ Band: `11.69` | Lower -1.28σ Band: `11.63`
  * Upper +1.00σ Band: `11.68` | Lower -1.00σ Band: `11.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.66` | EMA-20=`11.66` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.66` (Slope: `+0.0000`) | EMA-100=`11.66`
  * Institutional Anchors: EMA-144=`11.66` | EMA-200=`11.66` (Slope: `+0.0000`) | EMA-233=`11.66`
- **Range Boundaries**: 24H High=`11.78` | 24H Low=`11.54` | Weekly High=`11.89` | Weekly Low=`11.43`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.91` (Distance: `-2.07%`)
  * Point of Control (POC) = `11.77` (Distance: `-0.94%`)
  * Value Area Low (VAL) = `11.44` (Distance: `+1.92%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.58` | Weekly POC=`11.41` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.96` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.61` - `11.71`
  * Optimal Trade Entry (OTE 0.705): `11.68`
  * Structural Invalidation Anchor (0.786): `11.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.64` | `11.67` | `11.64` | `11.64` | `30,176` | 351,374.69 USD | -183,156.43 USD | `-52.13%` | -122,214.67 USD | `-1.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.64` | `11.66` | `11.63` | `11.65` | `34,208` | 398,197.39 USD | -138,688.44 USD | `-34.83%` | -260,903.11 USD | `-0.78` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.65` | `11.67` | `11.64` | `11.67` | `7,132` | 83,180.64 USD | 2,686.45 USD | `+3.23%` | -258,216.67 USD | `+0.02` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `11.65` | `11.71` | `11.64` | `11.68` | `100,997` | 1,180,195.23 USD | 690,200.05 USD | `+58.48%` | 91,026.22 USD | `+1.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.68` | `11.69` | `11.64` | `11.64` | `73,796` | 859,560.77 USD | -257,858.72 USD | `-30.00%` | -166,832.51 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.64` | `11.67` | `11.63` | `11.67` | `41,339` | 481,378.03 USD | -136,001.99 USD | `-28.25%` | -302,834.50 USD | `-0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.86` | `11.87` | `11.66` | `11.74` | `476,252` | 5,603,289.28 USD | -228,969.33 USD | `-4.09%` | -626,109.15 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.68` | `461,460` | 5,390,854.94 USD | 388,230.26 USD | `+7.20%` | -237,878.89 USD | `+0.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.69` | `11.63` | `11.67` | `115,136` | 1,340,938.80 USD | -393,860.72 USD | `-29.37%` | -631,739.61 USD | `-0.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.67` | `1,865,733` | 22,015,219.72 USD | -1,177,943.26 USD | `-5.35%` | -631,760.14 USD | `-0.82` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.67` | `1,865,733` | 22,015,219.72 USD | -1,177,943.26 USD | `-5.35%` | -631,760.14 USD | `-0.82` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.66`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `490` | `0x73ce...8ce9` | `LONG` | 4,672,135.49 USD | `400,011,600.00` | `12.05` | `11.68` | `9.13` | -147,618.22 USD | `-3.16%` | `5X Cross` |
| `642` | `0x5b5d...c060` | `SHORT` | 3,641,297.10 USD | `311,728,200.00` | `13.61` | `11.68` | `493.38` | 600,835.00 USD | `+16.50%` | `3X Cross` |
| `645` | `0xb83d...6e36` | `SHORT` | 3,599,215.36 USD | `308,152,000.00` | `12.93` | `11.68` | `420.35` | 386,038.14 USD | `+10.73%` | `3X Cross` |
| `863` | `0x458d...ab3b` | `LONG` | 2,653,530.99 USD | `227,156,700.00` | `13.13` | `11.68` | `9.34` | -328,699.41 USD | `-12.39%` | `3X Isolated` |
| `947` | `0xdd53...2b13` | `SHORT` | 2,411,631.50 USD | `206,475,300.00` | `11.92` | `11.68` | `274.09` | 49,591.42 USD | `+2.06%` | `3X Cross` |
| `981` | `0x3dc9...54b0` | `SHORT` | 2,336,000.00 USD | `200,000,000.00` | `7.56` | `11.68` | `81.53` | -824,841.58 USD | `-35.31%` | `10X Cross` |
| `1001` | `0x45d2...4029` | `SHORT` | 2,283,440.00 USD | `195,500,000.00` | `11.54` | `11.68` | `191.83` | -26,956.57 USD | `-1.18%` | `10X Cross` |
| `1198` | `0x6540...f7b7` | `LONG` | 1,912,668.79 USD | `163,762,900.00` | `12.48` | `11.68` | `8.01` | -130,553.05 USD | `-6.83%` | `5X Isolated` |
| `1256` | `0xeadc...9d55` | `LONG` | 1,840,891.74 USD | `157,691,600.00` | `9.43` | `11.68` | `0.000000` | 354,236.84 USD | `+19.24%` | `10X Cross` |
| `1613` | `0x9df2...c665` | `SHORT` | 1,377,137.41 USD | `117,905,600.00` | `11.48` | `11.68` | `252.74` | -23,119.13 USD | `-1.68%` | `10X Cross` |
| `1637` | `0xf6f3...47f8` | `SHORT` | 1,343,372.30 USD | `115,024,600.00` | `11.42` | `11.68` | `18.71` | -30,042.12 USD | `-2.24%` | `5X Cross` |
| `1797` | `0xfe7e...11b4` | `LONG` | 1,181,237.42 USD | `101,142,000.00` | `14.47` | `11.68` | `5.33` | -281,875.73 USD | `-23.86%` | `5X Isolated` |
| `1830` | `0x8af7...fa05` | `SHORT` | 1,152,264.15 USD | `98,661,200.00` | `14.08` | `11.68` | `203.99` | 236,918.39 USD | `+20.56%` | `10X Cross` |
| `1883` | `0xb7ec...5166` | `LONG` | 1,104,087.49 USD | `94,515,900.00` | `9.01` | `11.68` | `7.20` | 252,226.91 USD | `+22.84%` | `4X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.53` | 5,184.59 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.18K USD at 11.5290 USD [API] | `2026-10-27 22:22:38` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,130.50 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.13K USD at 11.5370 USD [API] | `2026-10-27 23:02:34` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 6,217.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.22K USD at 11.5370 USD [API] | `2026-10-27 23:02:31` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,831.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.83K USD at 11.5370 USD [API] | `2026-10-27 23:01:48` |
| `ANNOUNCEMENT` | `INFO` | `12.10` | 421.08 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.42K USD at 12.1000 USD [API] | `2026-10-08 17:26:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`12.05` (Vol: 117,000.00 USD, Dist: `+3.17%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.25%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+3.17%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.42%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.62%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.51%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.64%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 2,500.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 2,250.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 442.68 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 34,400.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 632.50 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 269.90 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 8,210.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 951.40 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 345.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,300.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,340.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 4,160.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 15,960.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 19,980.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,940.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 745.59 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 651.48 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 222,950.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 5,810.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 55,670.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 15,450.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 90,620.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 542,530.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 27,350.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 8,390.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 18,730.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 20,310.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 11,220.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,180.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,910.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 141,810.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,840.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 22,560.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 6,770.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 810.37 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 3,760.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 730,260.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,080.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 45,460.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 6,940.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 21,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 660.96 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 244.12 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 726.91 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,130.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,420,000.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,010.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 33,960.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,770.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 10,670.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 23,380.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 33,160.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 304,290.00 USD | 10,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 34,730.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,940.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 35,420.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,760,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 25,310.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 25,230.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 16,760.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 8,830.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 103,770.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 17,500.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 773,910.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 645,910.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 60,410.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.25` | 271,590.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.27` | 20,170,000.00 USD | 20,170,000.00 USD | 92,330.00 USD | 32,960.00 USD | 72,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 19,970,000.00 USD | 19,970,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 19,890,000.00 USD | 19,890,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 19,700,000.00 USD | 19,700,000.00 USD | 57,270.00 USD | 28,270.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 19,590,000.00 USD | 19,590,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 9,660.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.37` | 19,530,000.00 USD | 19,530,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 19,480,000.00 USD | 19,480,000.00 USD | 4,240.00 USD | 648.05 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 19,430,000.00 USD | 19,430,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 19,280,000.00 USD | 19,280,000.00 USD | 32,710.00 USD | 14,710.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 19,220,000.00 USD | 19,220,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 14,500.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 6,300,000.00 USD | 6,300,000.00 USD | 27,560.00 USD | 8,350.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 19,130,000.00 USD | 19,130,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 6,250,000.00 USD | 6,250,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 19,050,000.00 USD | 19,050,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 6,220,000.00 USD | 6,220,000.00 USD | 23,170.00 USD | 7,140.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 19,000,000.00 USD | 19,000,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 6,180,000.00 USD | 6,180,000.00 USD | 22,700.00 USD | 3,770.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 18,910,000.00 USD | 18,910,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 6,150,000.00 USD | 6,150,000.00 USD | 4,030.00 USD | 2,310.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 18,870,000.00 USD | 18,870,000.00 USD | 55,490.00 USD | 18,800.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 198,380.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 6,140,000.00 USD | 6,140,000.00 USD | 22,600.00 USD | 7,180.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 18,780,000.00 USD | 18,780,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 6,110,000.00 USD | 6,110,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 18,670,000.00 USD | 18,670,000.00 USD | 33,510.00 USD | 9,440.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,070,000.00 USD | 6,070,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 18,620,000.00 USD | 18,620,000.00 USD | 26,680.00 USD | 10,560.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,060,000.00 USD | 6,060,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 18,580,000.00 USD | 18,580,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 6,020,000.00 USD | 6,020,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 18,500,000.00 USD | 18,500,000.00 USD | 6,380.00 USD | 2,920.00 USD | 168.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 48,560.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 5,970,000.00 USD | 5,970,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 18,490,000.00 USD | 18,490,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 5,950,000.00 USD | 5,950,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 18,460,000.00 USD | 18,460,000.00 USD | 18,290.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 5,930,000.00 USD | 5,930,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 18,430,000.00 USD | 18,430,000.00 USD | 14,600.00 USD | 0.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 5,920,000.00 USD | 5,920,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 18,410,000.00 USD | 18,410,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 5,900,000.00 USD | 5,900,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 18,380,000.00 USD | 18,380,000.00 USD | 17,290.00 USD | 4,010.00 USD | 318.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 5,880,000.00 USD | 5,880,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 18,360,000.00 USD | 18,360,000.00 USD | 16,290.00 USD | 3,960.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 5,860,000.00 USD | 5,860,000.00 USD | 1,070.00 USD | 4,870.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 18,330,000.00 USD | 18,330,000.00 USD | 57,970.00 USD | 1,400.00 USD | 24,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 5,850,000.00 USD | 5,850,000.00 USD | 4,360.00 USD | 0.00 USD | 97.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 18,240,000.00 USD | 18,240,000.00 USD | 86,860.00 USD | 28,970.00 USD | 60,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 5,840,000.00 USD | 5,840,000.00 USD | 2,030.00 USD | 0.00 USD | 58.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 18,070,000.00 USD | 18,070,000.00 USD | 123,460.00 USD | 23,810.00 USD | 45,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 5,840,000.00 USD | 5,840,000.00 USD | 1,520.00 USD | 160.15 USD | 48.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 17,870,000.00 USD | 17,870,000.00 USD | 231,910.00 USD | 26,480.00 USD | 83,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 85,390.00 USD | 843,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 5,840,000.00 USD | 5,840,000.00 USD | 976.86 USD | 4,520.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 17,530,000.00 USD | 17,530,000.00 USD | 86,700.00 USD | 41,310.00 USD | 99,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 5,830,000.00 USD | 5,830,000.00 USD | 1,740.00 USD | 10,400.00 USD | 16,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 17,300,000.00 USD | 17,300,000.00 USD | 235,210.00 USD | 62,890.00 USD | 175,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 5,800,000.00 USD | 5,800,000.00 USD | 1,120.00 USD | 3,770.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 16,830,000.00 USD | 16,830,000.00 USD | 271,580.00 USD | 48,930.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 5,770,000.00 USD | 5,770,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 16,300,000.00 USD | 16,300,000.00 USD | 395,920.00 USD | 107,040.00 USD | 316,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 5,620,000.00 USD | 5,620,000.00 USD | 46,880.00 USD | 17,110.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 15,480,000.00 USD | 15,480,000.00 USD | 308,350.00 USD | 107,220.00 USD | 305,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 757,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 5,550,000.00 USD | 5,550,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 14,760,000.00 USD | 14,760,000.00 USD | 165,580.00 USD | 96,900.00 USD | 114,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 5,400,000.00 USD | 5,400,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 14,380,000.00 USD | 14,380,000.00 USD | 94,430.00 USD | 117,780.00 USD | 249,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 5,340,000.00 USD | 5,340,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 13,920,000.00 USD | 13,920,000.00 USD | 141,200.00 USD | 39,420.00 USD | 103,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 5,300,000.00 USD | 5,300,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.03` | 13,630,000.00 USD | 13,630,000.00 USD | 423,180.00 USD | 178,040.00 USD | 207,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,140,000.00 USD | 5,140,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.05` | 12,830,000.00 USD | 12,830,000.00 USD | 260,170.00 USD | 70,790.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 122,470.00 USD | 199,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,110,000.00 USD | 5,110,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.07` | 12,340,000.00 USD | 12,340,000.00 USD | 437,450.00 USD | 53,630.00 USD | 223,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,070,000.00 USD | 5,070,000.00 USD | 28,790.00 USD | 15,060.00 USD | 29,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.09` | 11,620,000.00 USD | 11,620,000.00 USD | 170,080.00 USD | 126,860.00 USD | 397,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 5,000,000.00 USD | 5,000,000.00 USD | 31,390.00 USD | 30,270.00 USD | 32,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.11` | 10,930,000.00 USD | 10,930,000.00 USD | 575,850.00 USD | 145,120.00 USD | 441,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 4,900,000.00 USD | 4,900,000.00 USD | 53,430.00 USD | 33,090.00 USD | 76,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.13` | 9,770,000.00 USD | 9,770,000.00 USD | 618,260.00 USD | 148,900.00 USD | 476,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 4,740,000.00 USD | 4,740,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.15` | 8,520,000.00 USD | 8,520,000.00 USD | 809,230.00 USD | 195,340.00 USD | 593,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 26,420.00 USD | 77,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 4,360,000.00 USD | 4,360,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.17` | 6,930,000.00 USD | 6,930,000.00 USD | 527,700.00 USD | 265,230.00 USD | 520,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 4,060,000.00 USD | 4,060,000.00 USD | 137,180.00 USD | 43,130.00 USD | 63,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.19` | 5,610,000.00 USD | 5,610,000.00 USD | 597,320.00 USD | 148,650.00 USD | 279,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 3,820,000.00 USD | 3,820,000.00 USD | 222,000.00 USD | 47,730.00 USD | 92,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.21` | 4,590,000.00 USD | 4,590,000.00 USD | 319,760.00 USD | 249,060.00 USD | 282,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 3,450,000.00 USD | 3,450,000.00 USD | 97,140.00 USD | 31,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.23` | 3,740,000.00 USD | 3,740,000.00 USD | 201,470.00 USD | 197,890.00 USD | 58,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 3,290,000.00 USD | 3,290,000.00 USD | 111,250.00 USD | 59,440.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.25` | 3,280,000.00 USD | 3,280,000.00 USD | 332,220.00 USD | 106,830.00 USD | 101,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 41,990.00 USD | 50,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 3,030,000.00 USD | 3,030,000.00 USD | 185,010.00 USD | 46,310.00 USD | 55,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.27` | 2,740,000.00 USD | 2,740,000.00 USD | 181,530.00 USD | 128,400.00 USD | 101,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 2,750,000.00 USD | 2,750,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.29` | 2,330,000.00 USD | 2,330,000.00 USD | 104,970.00 USD | 43,570.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 2,620,000.00 USD | 2,620,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.31` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 13,590.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 2,490,000.00 USD | 2,490,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.33` | 2,010,000.00 USD | 2,010,000.00 USD | 190,980.00 USD | 11,560.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 2,370,000.00 USD | 2,370,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.35` | 1,790,000.00 USD | 1,790,000.00 USD | 310,190.00 USD | 58,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 8,900.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 2,100,000.00 USD | 2,100,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.37` | 1,420,000.00 USD | 1,420,000.00 USD | 44,290.00 USD | 10,650.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 1,700,000.00 USD | 1,700,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.39` | 1,270,000.00 USD | 1,270,000.00 USD | 142,620.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 1,570,000.00 USD | 1,570,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.41` | 1,090,000.00 USD | 1,090,000.00 USD | 34,370.00 USD | 14,250.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 1,380,000.00 USD | 1,380,000.00 USD | 106,690.00 USD | 34,500.00 USD | 70,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.43` | 1,000,000.00 USD | 1,000,000.00 USD | 133,220.00 USD | 15,440.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 1,170,000.00 USD | 1,170,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.45` | 800,190.00 USD | 800,190.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 923,270.00 USD | 923,270.00 USD | 177,600.00 USD | 30,500.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.47` | 545,660.00 USD | 545,660.00 USD | 17,370.00 USD | 14,370.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 690,320.00 USD | 690,320.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.49` | 475,150.00 USD | 475,150.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 612,960.00 USD | 612,960.00 USD | 74,140.00 USD | 46,450.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.51` | 442,030.00 USD | 442,030.00 USD | 40,840.00 USD | 33,270.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 478,070.00 USD | 478,070.00 USD | 13,090.00 USD | 34,130.00 USD | 46,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.53` | 330,680.00 USD | 330,680.00 USD | 34,770.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.54` | 384,520.00 USD | 384,520.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.55` | 291,640.00 USD | 291,640.00 USD | 0.00 USD | 55,650.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 361,920.00 USD | 361,920.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.57` | 184,470.00 USD | 184,470.00 USD | 0.00 USD | 0.00 USD | 69,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.58` | 202,960.00 USD | 202,960.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.59` | 114,970.00 USD | 114,970.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 121,320.00 USD | 121,320.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.62` | 13,920.00 USD | 13,920.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.63` | 92,190.00 USD | 92,190.00 USD | 34,910.00 USD | 57,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 22,350.00 USD | 22,350.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.66` | 37,590.00 USD | 37,590.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 88,590.00 USD | 88,590.00 USD | 0.00 USD | 4,270.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 83,510.00 USD | 83,510.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 88,970.00 USD | 88,970.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 83,740.00 USD | 83,740.00 USD | 0.00 USD | 230.72 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 284,910.00 USD | 284,910.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 261,160.00 USD | 261,160.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 261,490.00 USD | 261,490.00 USD | 0.00 USD | 324.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 302,290.00 USD | 302,290.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 261,830.00 USD | 261,830.00 USD | 0.00 USD | 342.56 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 333,100.00 USD | 333,100.00 USD | 30,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 278,860.00 USD | 278,860.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 408,500.00 USD | 408,500.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 279,920.00 USD | 279,920.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 573,010.00 USD | 573,010.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 637,190.00 USD | 637,190.00 USD | 58,850.00 USD | 5,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 363,810.00 USD | 363,810.00 USD | 55,360.00 USD | 1,130.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 855,210.00 USD | 855,210.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 435,990.00 USD | 435,990.00 USD | 232.40 USD | 33,940.00 USD | 38,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 884,260.00 USD | 884,260.00 USD | 438.10 USD | 5,400.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 508,830.00 USD | 508,830.00 USD | 19,640.00 USD | 15,360.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 926,690.00 USD | 926,690.00 USD | 40,020.00 USD | 2,340.00 USD | 71.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 553,050.00 USD | 553,050.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 1,010,000.00 USD | 1,010,000.00 USD | 82,030.00 USD | 0.00 USD | 165.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 625,920.00 USD | 625,920.00 USD | 59,860.00 USD | 12,990.00 USD | 20.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 1,080,000.00 USD | 1,080,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 671,520.00 USD | 671,520.00 USD | 1,220.00 USD | 15,870.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 1,320,000.00 USD | 1,320,000.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 738,250.00 USD | 738,250.00 USD | 12,210.00 USD | 26,690.00 USD | 27,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 1,920,000.00 USD | 1,920,000.00 USD | 354,730.00 USD | 35,140.00 USD | 213,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 875,210.00 USD | 875,210.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 2,290,000.00 USD | 2,290,000.00 USD | 242,400.00 USD | 3,330.00 USD | 119,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 1,020,000.00 USD | 1,020,000.00 USD | 106,180.00 USD | 351.59 USD | 41,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 2,680,000.00 USD | 2,680,000.00 USD | 164,140.00 USD | 5,360.00 USD | 219,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 1,130,000.00 USD | 1,130,000.00 USD | 59,970.00 USD | 32,820.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 3,330,000.00 USD | 3,330,000.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 1,540,000.00 USD | 1,540,000.00 USD | 233,510.00 USD | 73,470.00 USD | 97,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 3,960,000.00 USD | 3,960,000.00 USD | 330,170.00 USD | 106,020.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 2,000,000.00 USD | 2,000,000.00 USD | 221,050.00 USD | 88,350.00 USD | 155,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 4,530,000.00 USD | 4,530,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 2,220,000.00 USD | 2,220,000.00 USD | 123,260.00 USD | 45,990.00 USD | 52,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 4,820,000.00 USD | 4,820,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 2,280,000.00 USD | 2,280,000.00 USD | 19,140.00 USD | 9,670.00 USD | 31,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 5,090,000.00 USD | 5,090,000.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 2,530,000.00 USD | 2,530,000.00 USD | 141,930.00 USD | 49,190.00 USD | 58,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 5,330,000.00 USD | 5,330,000.00 USD | 148,530.00 USD | 56,000.00 USD | 36,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 2,720,000.00 USD | 2,720,000.00 USD | 109,520.00 USD | 28,690.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 5,890,000.00 USD | 5,890,000.00 USD | 310,620.00 USD | 114,540.00 USD | 131,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 2,930,000.00 USD | 2,930,000.00 USD | 96,770.00 USD | 58,750.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 6,030,000.00 USD | 6,030,000.00 USD | 26,820.00 USD | 61,400.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 3,130,000.00 USD | 3,130,000.00 USD | 117,230.00 USD | 39,740.00 USD | 45,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 6,370,000.00 USD | 6,370,000.00 USD | 196,200.00 USD | 58,210.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 3,290,000.00 USD | 3,290,000.00 USD | 89,220.00 USD | 40,880.00 USD | 25,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 6,750,000.00 USD | 6,750,000.00 USD | 200,760.00 USD | 62,900.00 USD | 115,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 3,410,000.00 USD | 3,410,000.00 USD | 29,450.00 USD | 42,870.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 6,960,000.00 USD | 6,960,000.00 USD | 140,270.00 USD | 19,410.00 USD | 57,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 3,470,000.00 USD | 3,470,000.00 USD | 33,920.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 7,260,000.00 USD | 7,260,000.00 USD | 134,500.00 USD | 56,330.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 5,040.00 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 3,570,000.00 USD | 3,570,000.00 USD | 55,900.00 USD | 27,170.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 7,510,000.00 USD | 7,510,000.00 USD | 141,400.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 3,740,000.00 USD | 3,740,000.00 USD | 99,490.00 USD | 24,800.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 8,040,000.00 USD | 8,040,000.00 USD | 235,780.00 USD | 118,830.00 USD | 175,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 3,860,000.00 USD | 3,860,000.00 USD | 58,090.00 USD | 24,040.00 USD | 45,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 8,310,000.00 USD | 8,310,000.00 USD | 157,240.00 USD | 53,480.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 3,870,000.00 USD | 3,870,000.00 USD | 1,610.00 USD | 7,100.00 USD | 20.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 8,590,000.00 USD | 8,590,000.00 USD | 191,980.00 USD | 89,700.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 3,930,000.00 USD | 3,930,000.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 8,750,000.00 USD | 8,750,000.00 USD | 116,830.00 USD | 15,980.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 7,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 3,960,000.00 USD | 3,960,000.00 USD | 19,510.00 USD | 9,040.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 8,820,000.00 USD | 8,820,000.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 4,010,000.00 USD | 4,010,000.00 USD | 30,170.00 USD | 6,420.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 9,360,000.00 USD | 9,360,000.00 USD | 160,660.00 USD | 42,540.00 USD | 338,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 4,080,000.00 USD | 4,080,000.00 USD | 18,820.00 USD | 23,720.00 USD | 22,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 9,670,000.00 USD | 9,670,000.00 USD | 80,100.00 USD | 32,410.00 USD | 195,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 4,150,000.00 USD | 4,150,000.00 USD | 51,980.00 USD | 13,980.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 10,260,000.00 USD | 10,260,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 4,190,000.00 USD | 4,190,000.00 USD | 17,630.00 USD | 10,270.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 10,690,000.00 USD | 10,690,000.00 USD | 57,130.00 USD | 118,850.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,930.00 USD | 12,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 4,210,000.00 USD | 4,210,000.00 USD | 411.51 USD | 15,260.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 10,980,000.00 USD | 10,980,000.00 USD | 66,870.00 USD | 29,080.00 USD | 192,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 4,230,000.00 USD | 4,230,000.00 USD | 2,220.00 USD | 2,560.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 11,150,000.00 USD | 11,150,000.00 USD | 91,900.00 USD | 17,840.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 4,240,000.00 USD | 4,240,000.00 USD | 620.31 USD | 4,320.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 11,400,000.00 USD | 11,400,000.00 USD | 136,260.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 4,280,000.00 USD | 4,280,000.00 USD | 21,510.00 USD | 5,020.00 USD | 12,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 11,720,000.00 USD | 11,720,000.00 USD | 131,510.00 USD | 57,030.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 4,300,000.00 USD | 4,300,000.00 USD | 14,970.00 USD | 2,830.00 USD | 28.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 11,970,000.00 USD | 11,970,000.00 USD | 126,130.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.56` | 4,340,000.00 USD | 4,340,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.57` | 12,180,000.00 USD | 12,180,000.00 USD | 131,970.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 4,360,000.00 USD | 4,360,000.00 USD | 6,910.00 USD | 1,030.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 12,300,000.00 USD | 12,300,000.00 USD | 65,910.00 USD | 17,430.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 4,370,000.00 USD | 4,370,000.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 12,430,000.00 USD | 12,430,000.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 4,400,000.00 USD | 4,400,000.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 12,600,000.00 USD | 12,600,000.00 USD | 62,580.00 USD | 28,520.00 USD | 81,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 4,430,000.00 USD | 4,430,000.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 12,840,000.00 USD | 12,840,000.00 USD | 76,240.00 USD | 26,110.00 USD | 131,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.66` | 4,430,000.00 USD | 4,430,000.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 13,150,000.00 USD | 13,150,000.00 USD | 66,110.00 USD | 19,940.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 4,450,000.00 USD | 4,450,000.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 13,380,000.00 USD | 13,380,000.00 USD | 44,600.00 USD | 34,670.00 USD | 154,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 1,140.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 13,480,000.00 USD | 13,480,000.00 USD | 31,960.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 4,470,000.00 USD | 4,470,000.00 USD | 13,460.00 USD | 3,750.00 USD | 107.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 13,630,000.00 USD | 13,630,000.00 USD | 54,040.00 USD | 11,090.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 4,500,000.00 USD | 4,500,000.00 USD | 20,500.00 USD | 8,140.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 13,690,000.00 USD | 13,690,000.00 USD | 33,680.00 USD | 14,710.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 4,570,000.00 USD | 4,570,000.00 USD | 39,130.00 USD | 11,090.00 USD | 16,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 13,780,000.00 USD | 13,780,000.00 USD | 36,060.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 4,590,000.00 USD | 4,590,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 13,870,000.00 USD | 13,870,000.00 USD | 56,200.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 4,620,000.00 USD | 4,620,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 13,900,000.00 USD | 13,900,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 4,620,000.00 USD | 4,620,000.00 USD | 2,680.00 USD | 1,320.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 13,920,000.00 USD | 13,920,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 4,660,000.00 USD | 4,660,000.00 USD | 20,500.00 USD | 5,820.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 14,010,000.00 USD | 14,010,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 12,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 4,690,000.00 USD | 4,690,000.00 USD | 22,700.00 USD | 3,770.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.87` | 14,040,000.00 USD | 14,040,000.00 USD | 10,160.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 4,700,000.00 USD | 4,700,000.00 USD | 3,410.00 USD | 2,310.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 14,130,000.00 USD | 14,130,000.00 USD | 48,720.00 USD | 18,800.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 4,730,000.00 USD | 4,730,000.00 USD | 21,720.00 USD | 7,180.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 14,230,000.00 USD | 14,230,000.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 4,750,000.00 USD | 4,750,000.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 14,260,000.00 USD | 14,260,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 4,770,000.00 USD | 4,770,000.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 14,270,000.00 USD | 14,270,000.00 USD | 2,290.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 4,770,000.00 USD | 4,770,000.00 USD | 227.00 USD | 5,090.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 14,310,000.00 USD | 14,310,000.00 USD | 15,020.00 USD | 10,560.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 4,820,000.00 USD | 4,820,000.00 USD | 24,650.00 USD | 7,080.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 14,380,000.00 USD | 14,380,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 4,860,000.00 USD | 4,860,000.00 USD | 17,330.00 USD | 7,780.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 14,380,000.00 USD | 14,380,000.00 USD | 2,070.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.02` | 4,880,000.00 USD | 4,880,000.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 14,390,000.00 USD | 14,390,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.04` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 14,400,000.00 USD | 14,400,000.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 12,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.07` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 14,410,000.00 USD | 14,410,000.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 14,430,000.00 USD | 14,430,000.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 14,440,000.00 USD | 14,440,000.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 12,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.17` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 14,460,000.00 USD | 14,460,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 14,490,000.00 USD | 14,490,000.00 USD | 13,890.00 USD | 259.77 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 14,500,000.00 USD | 14,500,000.00 USD | 15,330.00 USD | 0.00 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 14,530,000.00 USD | 14,530,000.00 USD | 18,020.00 USD | 4,640.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 14,570,000.00 USD | 14,570,000.00 USD | 10,290.00 USD | 11,080.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.35` | 113.48 USD | 12,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 7,500.00 USD | 20,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 22,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 1,170.00 USD | 23,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 37,130.00 USD | 60,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 598.40 USD | 60,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 898.79 USD | 61,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 621.16 USD | 62,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 87,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 16,240.00 USD | 104,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 1,180.00 USD | 105,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 10,220.00 USD | 115,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 80,740.00 USD | 196,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 196,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 455.43 USD | 196,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 5,020.00 USD | 201,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 203,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 25,210.00 USD | 228,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 469.00 USD | 228,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 145,790.00 USD | 374,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 375,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 241.50 USD | 376,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 471,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 246,540.00 USD | 717,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 718,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 718,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 720,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 724,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 724,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 724,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 2,170,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 319.55 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 1,880.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 39,370.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 422.65 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 756,090.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.75` | 168.07 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 2,900.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 74,290.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.15` | 336,130.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.25` | 890.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 13,900,000.00 USD | 0.00 USD | 2,500.00 USD | `-79.88%` | `1,065,000.00` |
| `Live` | `Long` | `2.45` | 13,900,000.00 USD | 0.00 USD | 2,250.00 USD | `-79.03%` | `920,000.00` |
| `Live` | `Long` | `2.55` | 13,900,000.00 USD | 0.00 USD | 442.68 USD | `-78.17%` | `173,600.00` |
| `Live` | `Long` | `2.65` | 13,900,000.00 USD | 0.00 USD | 34,400.00 USD | `-77.31%` | `12,980,800.00` |
| `Live` | `Long` | `2.75` | 13,860,000.00 USD | 0.00 USD | 632.50 USD | `-76.46%` | `230,000.00` |
| `Live` | `Long` | `2.85` | 13,860,000.00 USD | 0.00 USD | 269.90 USD | `-75.60%` | `94,700.00` |
| `Live` | `Long` | `3.05` | 13,860,000.00 USD | 0.00 USD | 6,390.00 USD | `-73.89%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 13,860,000.00 USD | 0.00 USD | 297.99 USD | `-73.03%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 13,860,000.00 USD | 0.00 USD | 8,210.00 USD | `-72.18%` | `2,527,300.00` |
| `Live` | `Long` | `3.35` | 13,850,000.00 USD | 0.00 USD | 951.40 USD | `-71.32%` | `284,000.00` |
| `Live` | `Long` | `3.45` | 13,850,000.00 USD | 0.00 USD | 345.00 USD | `-70.47%` | `100,000.00` |
| `Live` | `Long` | `3.65` | 13,850,000.00 USD | 0.00 USD | 2,300.00 USD | `-68.75%` | `631,400.00` |
| `Live` | `Long` | `3.75` | 13,840,000.00 USD | 0.00 USD | 3,340.00 USD | `-67.90%` | `890,200.00` |
| `Live` | `Long` | `3.85` | 13,840,000.00 USD | 0.00 USD | 4,160.00 USD | `-67.04%` | `1,080,500.00` |
| `Live` | `Long` | `3.95` | 13,840,000.00 USD | 0.00 USD | 15,960.00 USD | `-66.19%` | `4,040,700.00` |
| `Live` | `Long` | `4.05` | 13,820,000.00 USD | 0.00 USD | 950.54 USD | `-65.33%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 13,820,000.00 USD | 0.00 USD | 19,980.00 USD | `-64.47%` | `4,813,700.00` |
| `Live` | `Long` | `4.25` | 13,800,000.00 USD | 0.00 USD | 5,940.00 USD | `-63.62%` | `1,398,100.00` |
| `Live` | `Long` | `4.35` | 13,790,000.00 USD | 0.00 USD | 745.59 USD | `-62.76%` | `171,400.00` |
| `Live` | `Long` | `4.45` | 13,790,000.00 USD | 0.00 USD | 651.48 USD | `-61.91%` | `146,400.00` |
| `Live` | `Long` | `4.55` | 13,790,000.00 USD | 0.00 USD | 222,950.00 USD | `-61.05%` | `49,000,000.00` |
| `Live` | `Long` | `4.65` | 13,570,000.00 USD | 0.00 USD | 383.63 USD | `-60.19%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,570,000.00 USD | 0.00 USD | 418.95 USD | `-59.34%` | `88,200.00` |
| `Live` | `Long` | `4.85` | 13,570,000.00 USD | 0.00 USD | 5,810.00 USD | `-58.48%` | `1,198,700.00` |
| `Live` | `Long` | `4.95` | 13,560,000.00 USD | 0.00 USD | 883.08 USD | `-57.62%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 13,560,000.00 USD | 0.00 USD | 55,670.00 USD | `-56.77%` | `11,024,400.00` |
| `Live` | `Long` | `5.15` | 13,510,000.00 USD | 0.00 USD | 15,450.00 USD | `-55.91%` | `3,000,000.00` |
| `Live` | `Long` | `5.25` | 13,490,000.00 USD | 0.00 USD | 90,620.00 USD | `-55.06%` | `17,260,600.00` |
| `Live` | `Long` | `5.35` | 13,400,000.00 USD | 0.00 USD | 542,530.00 USD | `-54.20%` | `101,407,400.00` |
| `Live` | `Long` | `5.45` | 12,860,000.00 USD | 0.00 USD | 138.97 USD | `-53.34%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 12,860,000.00 USD | 0.00 USD | 27,350.00 USD | `-52.49%` | `4,927,500.00` |
| `Live` | `Long` | `5.65` | 12,830,000.00 USD | 0.00 USD | 35,600.00 USD | `-51.63%` | `6,300,800.00` |
| `Live` | `Long` | `5.75` | 12,790,000.00 USD | 0.00 USD | 8,390.00 USD | `-50.78%` | `1,458,900.00` |
| `Live` | `Long` | `5.85` | 12,790,000.00 USD | 0.00 USD | 18,730.00 USD | `-49.92%` | `3,202,100.00` |
| `Live` | `Long` | `5.95` | 12,770,000.00 USD | 0.00 USD | 20,310.00 USD | `-49.06%` | `3,413,400.00` |
| `Live` | `Long` | `6.05` | 12,750,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.21%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,680,000.00 USD | 0.00 USD | 11,220.00 USD | `-47.35%` | `1,825,000.00` |
| `Live` | `Long` | `6.25` | 12,670,000.00 USD | 0.00 USD | 42,180.00 USD | `-46.50%` | `6,748,700.00` |
| `Live` | `Long` | `6.35` | 12,630,000.00 USD | 0.00 USD | 16,910.00 USD | `-45.64%` | `2,663,400.00` |
| `Live` | `Long` | `6.45` | 12,610,000.00 USD | 0.00 USD | 141,810.00 USD | `-44.78%` | `21,986,200.00` |
| `Live` | `Long` | `6.55` | 12,470,000.00 USD | 0.00 USD | 2,840.00 USD | `-43.93%` | `433,500.00` |
| `Live` | `Long` | `6.65` | 12,470,000.00 USD | 0.00 USD | 22,560.00 USD | `-43.07%` | `3,391,800.00` |
| `Live` | `Long` | `6.75` | 12,450,000.00 USD | 0.00 USD | 4,130.00 USD | `-42.22%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,440,000.00 USD | 0.00 USD | 6,770.00 USD | `-41.36%` | `987,800.00` |
| `Live` | `Long` | `6.95` | 12,440,000.00 USD | 0.00 USD | 810.37 USD | `-40.50%` | `116,600.00` |
| `Live` | `Long` | `7.05` | 12,430,000.00 USD | 0.00 USD | 3,760.00 USD | `-39.65%` | `533,400.00` |
| `Live` | `Long` | `7.15` | 12,430,000.00 USD | 0.00 USD | 730,260.00 USD | `-38.79%` | `102,134,200.00` |
| `Live` | `Long` | `7.25` | 11,700,000.00 USD | 0.00 USD | 21,080.00 USD | `-37.94%` | `2,906,900.00` |
| `Live` | `Long` | `7.35` | 11,680,000.00 USD | 0.00 USD | 45,460.00 USD | `-37.08%` | `6,185,500.00` |
| `Live` | `Long` | `7.45` | 11,630,000.00 USD | 0.00 USD | 6,940.00 USD | `-36.22%` | `931,100.00` |
| `Live` | `Long` | `7.55` | 11,630,000.00 USD | 0.00 USD | 21,000.00 USD | `-35.37%` | `2,782,100.00` |
| `Live` | `Long` | `7.65` | 11,610,000.00 USD | 0.00 USD | 660.96 USD | `-34.51%` | `86,400.00` |
| `Live` | `Long` | `7.75` | 11,610,000.00 USD | 0.00 USD | 244.12 USD | `-33.66%` | `31,500.00` |
| `Live` | `Long` | `7.85` | 11,610,000.00 USD | 0.00 USD | 726.91 USD | `-32.80%` | `92,600.00` |
| `Live` | `Long` | `7.95` | 11,600,000.00 USD | 0.00 USD | 15,130.00 USD | `-31.94%` | `1,903,400.00` |
| `Live` | `Long` | `8.05` | 11,590,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-31.09%` | `175,847,600.00` |
| `Live` | `Long` | `8.15` | 10,170,000.00 USD | 0.00 USD | 16,010.00 USD | `-30.23%` | `1,964,500.00` |
| `Live` | `Long` | `8.25` | 10,160,000.00 USD | 0.00 USD | 33,960.00 USD | `-29.37%` | `4,116,000.00` |
| `Live` | `Long` | `8.35` | 10,120,000.00 USD | 0.00 USD | 7,770.00 USD | `-28.52%` | `930,800.00` |
| `Live` | `Long` | `8.45` | 10,120,000.00 USD | 0.00 USD | 10,670.00 USD | `-27.66%` | `1,263,100.00` |
| `Live` | `Long` | `8.55` | 10,110,000.00 USD | 0.00 USD | 23,380.00 USD | `-26.81%` | `2,734,400.00` |
| `Live` | `Long` | `8.65` | 10,080,000.00 USD | 0.00 USD | 33,160.00 USD | `-25.95%` | `3,833,800.00` |
| `Live` | `Long` | `8.75` | 10,050,000.00 USD | 0.00 USD | 304,290.00 USD | `-25.09%` | `34,776,300.00` |
| `Live` | `Long` | `8.85` | 9,740,000.00 USD | 0.00 USD | 34,730.00 USD | `-24.24%` | `3,924,300.00` |
| `Live` | `Long` | `8.95` | 9,710,000.00 USD | 0.00 USD | 486,940.00 USD | `-23.38%` | `54,406,700.00` |
| `Live` | `Long` | `9.05` | 9,220,000.00 USD | 0.00 USD | 35,420.00 USD | `-22.53%` | `3,913,700.00` |
| `Live` | `Long` | `9.15` | 9,190,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-21.67%` | `410,576,400.00` |
| `Live` | `Long` | `9.25` | 5,430,000.00 USD | 0.00 USD | 25,310.00 USD | `-20.81%` | `2,736,500.00` |
| `Live` | `Long` | `9.35` | 5,410,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-19.96%` | `230,268,400.00` |
| `Live` | `Long` | `9.45` | 3,250,000.00 USD | 0.00 USD | 25,230.00 USD | `-19.10%` | `2,669,400.00` |
| `Live` | `Long` | `9.55` | 3,230,000.00 USD | 0.00 USD | 16,760.00 USD | `-18.25%` | `1,755,400.00` |
| `Live` | `Long` | `9.65` | 3,210,000.00 USD | 0.00 USD | 8,830.00 USD | `-17.39%` | `914,600.00` |
| `Live` | `Long` | `9.75` | 3,200,000.00 USD | 0.00 USD | 103,770.00 USD | `-16.53%` | `10,642,900.00` |
| `Live` | `Long` | `9.85` | 3,100,000.00 USD | 0.00 USD | 17,500.00 USD | `-15.68%` | `1,777,000.00` |
| `Live` | `Long` | `9.95` | 3,080,000.00 USD | 0.00 USD | 773,910.00 USD | `-14.82%` | `77,780,400.00` |
| `Live` | `Long` | `10.05` | 2,310,000.00 USD | 0.00 USD | 645,910.00 USD | `-13.97%` | `64,270,100.00` |
| `Live` | `Long` | `10.15` | 1,660,000.00 USD | 0.00 USD | 60,410.00 USD | `-13.11%` | `5,952,000.00` |
| `Live` | `Long` | `10.25` | 1,600,000.00 USD | 0.00 USD | 271,590.00 USD | `-12.25%` | `26,497,000.00` |
| `Live` | `Long` | `10.35` | 1,330,000.00 USD | 0.00 USD | 9,660.00 USD | `-11.40%` | `933,500.00` |
| `Live` | `Long` | `10.45` | 1,320,000.00 USD | 0.00 USD | 14,500.00 USD | `-10.54%` | `1,387,200.00` |
| `Live` | `Long` | `10.55` | 1,300,000.00 USD | 0.00 USD | 198,380.00 USD | `-9.69%` | `18,803,600.00` |
| `Live` | `Long` | `10.65` | 1,110,000.00 USD | 0.00 USD | 48,560.00 USD | `-8.83%` | `4,560,000.00` |
| `Live` | `Long` | `10.75` | 1,060,000.00 USD | 0.00 USD | 214,040.00 USD | `-7.97%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 843,260.00 USD | 0.00 USD | 85,390.00 USD | `-7.12%` | `7,870,500.00` |
| `Live` | `Long` | `10.95` | 757,870.00 USD | 0.00 USD | 558,090.00 USD | `-6.26%` | `50,966,800.00` |
| `Live` | `Long` | `11.05` | 199,780.00 USD | 0.00 USD | 122,470.00 USD | `-5.41%` | `11,083,400.00` |
| `Live` | `Long` | `11.15` | 77,310.00 USD | 0.00 USD | 26,420.00 USD | `-4.55%` | `2,369,500.00` |
| `Live` | `Long` | `11.25` | 50,890.00 USD | 0.00 USD | 41,990.00 USD | `-3.69%` | `3,732,700.00` |
| `Live` | `Long` | `11.35` | 8,900.00 USD | 0.00 USD | 8,900.00 USD | `-2.84%` | `784,000.00` |
| `Live` | `Short` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | `+4.01%` | `114,600.00` |
| `Live` | `Short` | `12.25` | 6,440.00 USD | 5,040.00 USD | 0.00 USD | `+4.87%` | `411,700.00` |
| `Live` | `Short` | `12.35` | 7,170.00 USD | 736.06 USD | 0.00 USD | `+5.72%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 12,100.00 USD | 4,930.00 USD | 0.00 USD | `+6.58%` | `395,700.00` |
| `Live` | `Short` | `12.85` | 12,240.00 USD | 138.78 USD | 0.00 USD | `+10.00%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 12,350.00 USD | 113.53 USD | 0.00 USD | `+11.72%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 12,630.00 USD | 274.84 USD | 0.00 USD | `+12.57%` | `20,900.00` |
| `Live` | `Short` | `13.35` | 12,740.00 USD | 113.48 USD | 0.00 USD | `+14.28%` | `8,500.00` |
| `Live` | `Short` | `13.45` | 20,240.00 USD | 7,500.00 USD | 0.00 USD | `+15.14%` | `557,600.00` |
| `Live` | `Short` | `13.55` | 22,000.00 USD | 1,760.00 USD | 0.00 USD | `+16.00%` | `130,100.00` |
| `Live` | `Short` | `13.85` | 23,170.00 USD | 1,170.00 USD | 0.00 USD | `+18.56%` | `84,500.00` |
| `Live` | `Short` | `13.95` | 60,310.00 USD | 37,130.00 USD | 0.00 USD | `+19.42%` | `2,661,900.00` |
| `Live` | `Short` | `14.35` | 60,900.00 USD | 598.40 USD | 0.00 USD | `+22.84%` | `41,700.00` |
| `Live` | `Short` | `14.45` | 61,800.00 USD | 898.79 USD | 0.00 USD | `+23.70%` | `62,200.00` |
| `Live` | `Short` | `14.65` | 62,420.00 USD | 621.16 USD | 0.00 USD | `+25.41%` | `42,400.00` |
| `Live` | `Short` | `14.95` | 87,760.00 USD | 25,330.00 USD | 0.00 USD | `+27.98%` | `1,694,600.00` |
| `Live` | `Short` | `15.35` | 104,000.00 USD | 16,240.00 USD | 0.00 USD | `+31.41%` | `1,058,000.00` |
| `Live` | `Short` | `15.55` | 105,180.00 USD | 1,180.00 USD | 0.00 USD | `+33.12%` | `75,700.00` |
| `Live` | `Short` | `15.75` | 115,400.00 USD | 10,220.00 USD | 0.00 USD | `+34.83%` | `649,200.00` |
| `Live` | `Short` | `15.85` | 196,140.00 USD | 80,740.00 USD | 0.00 USD | `+35.69%` | `5,093,900.00` |
| `Live` | `Short` | `15.95` | 196,280.00 USD | 138.76 USD | 0.00 USD | `+36.54%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 196,730.00 USD | 455.43 USD | 0.00 USD | `+38.25%` | `28,200.00` |
| `Live` | `Short` | `16.25` | 201,750.00 USD | 5,020.00 USD | 0.00 USD | `+39.11%` | `309,000.00` |
| `Live` | `Short` | `16.35` | 203,150.00 USD | 1,390.00 USD | 0.00 USD | `+39.97%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 228,350.00 USD | 25,210.00 USD | 0.00 USD | `+41.68%` | `1,523,000.00` |
| `Live` | `Short` | `16.75` | 228,820.00 USD | 469.00 USD | 0.00 USD | `+43.39%` | `28,000.00` |
| `Live` | `Short` | `16.95` | 374,620.00 USD | 145,790.00 USD | 0.00 USD | `+45.10%` | `8,601,300.00` |
| `Live` | `Short` | `17.15` | 375,980.00 USD | 1,370.00 USD | 0.00 USD | `+46.81%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 376,220.00 USD | 241.50 USD | 0.00 USD | `+47.67%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 471,240.00 USD | 95,020.00 USD | 0.00 USD | `+49.38%` | `5,445,000.00` |
| `Live` | `Short` | `17.65` | 717,770.00 USD | 246,540.00 USD | 0.00 USD | `+51.10%` | `13,968,000.00` |
| `Live` | `Short` | `17.85` | 718,020.00 USD | 249.90 USD | 0.00 USD | `+52.81%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 718,650.00 USD | 621.07 USD | 0.00 USD | `+53.66%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 720,620.00 USD | 1,970.00 USD | 0.00 USD | `+54.52%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 724,510.00 USD | 3,890.00 USD | 0.00 USD | `+57.94%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 724,690.00 USD | 185.50 USD | 0.00 USD | `+58.80%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 724,880.00 USD | 186.50 USD | 0.00 USD | `+59.66%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 2,890,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+61.37%` | `115,048,800.00` |
| `Live` | `Short` | `18.95` | 2,910,000.00 USD | 16,250.00 USD | 0.00 USD | `+62.22%` | `857,700.00` |
| `Live` | `Short` | `19.25` | 2,910,000.00 USD | 319.55 USD | 0.00 USD | `+64.79%` | `16,600.00` |
| `Live` | `Short` | `19.35` | 2,910,000.00 USD | 1,880.00 USD | 0.00 USD | `+65.65%` | `96,900.00` |
| `Live` | `Short` | `19.65` | 2,950,000.00 USD | 39,370.00 USD | 0.00 USD | `+68.22%` | `2,003,700.00` |
| `Live` | `Short` | `19.75` | 2,950,000.00 USD | 422.65 USD | 0.00 USD | `+69.07%` | `21,400.00` |
| `Live` | `Short` | `19.95` | 2,950,000.00 USD | 291.27 USD | 0.00 USD | `+70.78%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,710,000.00 USD | 756,090.00 USD | 0.00 USD | `+71.64%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+75.92%` | `353,000.00` |
| `Live` | `Short` | `20.75` | 3,720,000.00 USD | 168.07 USD | 0.00 USD | `+77.63%` | `8,100.00` |
| `Live` | `Short` | `21.75` | 3,720,000.00 USD | 2,900.00 USD | 0.00 USD | `+86.19%` | `133,300.00` |
| `Live` | `Short` | `21.85` | 3,790,000.00 USD | 74,290.00 USD | 0.00 USD | `+87.05%` | `3,400,000.00` |
| `Live` | `Short` | `22.15` | 4,130,000.00 USD | 336,130.00 USD | 0.00 USD | `+89.62%` | `15,175,000.00` |
| `Live` | `Short` | `22.25` | 4,130,000.00 USD | 890.00 USD | 0.00 USD | `+90.47%` | `40,000.00` |
| `Live` | `Short` | `23.35` | 4,130,000.00 USD | 238.17 USD | 0.00 USD | `+99.89%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 771,010.00 USD | 0.00 USD | 431.68 USD | `-69.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 770,580.00 USD | 0.00 USD | 290.29 USD | `-61.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 770,290.00 USD | 0.00 USD | 120.22 USD | `-55.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 770,170.00 USD | 0.00 USD | 107.09 USD | `-48.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 770,060.00 USD | 0.00 USD | 3,760.00 USD | `-43.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 766,300.00 USD | 0.00 USD | 133.00 USD | `-43.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 766,170.00 USD | 0.00 USD | 3,770.00 USD | `-39.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 762,400.00 USD | 0.00 USD | 2,070.00 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 760,330.00 USD | 0.00 USD | 3,740.00 USD | `-36.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 756,580.00 USD | 0.00 USD | 1,050.00 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 755,530.00 USD | 0.00 USD | 146.80 USD | `-32.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 755,390.00 USD | 0.00 USD | 5,000.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 750,380.00 USD | 0.00 USD | 393.64 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 749,990.00 USD | 0.00 USD | 10,660.00 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 739,320.00 USD | 0.00 USD | 1,360.00 USD | `-27.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 737,970.00 USD | 0.00 USD | 30,250.00 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 707,720.00 USD | 0.00 USD | 186.84 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 707,530.00 USD | 0.00 USD | 742.88 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 706,790.00 USD | 0.00 USD | 196.47 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 706,590.00 USD | 0.00 USD | 1,320.00 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 705,280.00 USD | 0.00 USD | 2,240.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 703,030.00 USD | 0.00 USD | 194.90 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 702,840.00 USD | 0.00 USD | 4,940.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 697,890.00 USD | 0.00 USD | 9,870.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 688,030.00 USD | 0.00 USD | 3,550.00 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 684,480.00 USD | 0.00 USD | 25,950.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 658,530.00 USD | 0.00 USD | 19,100.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 639,430.00 USD | 0.00 USD | 299,650.00 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 339,770.00 USD | 0.00 USD | 2,590.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 337,180.00 USD | 0.00 USD | 1,050.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 336,130.00 USD | 0.00 USD | 2,820.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 333,310.00 USD | 0.00 USD | 6,330.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 326,990.00 USD | 0.00 USD | 19,650.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 307,330.00 USD | 0.00 USD | 5,160.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 302,170.00 USD | 0.00 USD | 4,590.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 297,580.00 USD | 0.00 USD | 5,470.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 292,100.00 USD | 0.00 USD | 3,780.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 288,320.00 USD | 0.00 USD | 3,270.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 285,050.00 USD | 0.00 USD | 18,860.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 266,180.00 USD | 0.00 USD | 26,990.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 239,190.00 USD | 0.00 USD | 47,110.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 192,080.00 USD | 0.00 USD | 12,810.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 179,280.00 USD | 0.00 USD | 48,420.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 130,860.00 USD | 0.00 USD | 11,000.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 119,870.00 USD | 0.00 USD | 119,870.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 10,530.00 USD | 6,070.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 10,690.00 USD | 156.55 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 66,960.00 USD | 56,270.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 68,920.00 USD | 1,960.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 79,340.00 USD | 10,420.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 80,680.00 USD | 1,340.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 80,780.00 USD | 100.84 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 91,890.00 USD | 11,110.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 148,420.00 USD | 56,530.00 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 189,900.00 USD | 41,470.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 210,630.00 USD | 20,730.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 211,090.00 USD | 461.02 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 217,590.00 USD | 6,500.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 218,630.00 USD | 1,050.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 222,480.00 USD | 3,840.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 227,470.00 USD | 4,990.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 241,870.00 USD | 14,400.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 244,500.00 USD | 2,630.00 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 246,520.00 USD | 2,020.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 248,580.00 USD | 2,060.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 248,700.00 USD | 120.50 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 248,970.00 USD | 266.44 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 274,430.00 USD | 25,460.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 275,220.00 USD | 798.06 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 282,210.00 USD | 6,990.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 282,430.00 USD | 218.25 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 285,040.00 USD | 2,610.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 297,970.00 USD | 12,920.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 298,920.00 USD | 950.82 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 310,420.00 USD | 11,500.00 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 314,600.00 USD | 4,180.00 USD | 0.00 USD | `+29.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 547,640.00 USD | 233,040.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 552,030.00 USD | 4,380.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 552,920.00 USD | 893.01 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 553,310.00 USD | 388.75 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 580,360.00 USD | 27,050.00 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 582,700.00 USD | 2,330.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 588,040.00 USD | 5,340.00 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 593,350.00 USD | 5,320.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 602,520.00 USD | 9,170.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 609,320.00 USD | 6,800.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 628,090.00 USD | 18,760.00 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 634,630.00 USD | 6,540.00 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 641,210.00 USD | 6,580.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 651,140.00 USD | 9,930.00 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 664,460.00 USD | 13,320.00 USD | 0.00 USD | `+42.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 678,690.00 USD | 14,240.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 763,050.00 USD | 84,360.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 764,740.00 USD | 1,700.00 USD | 0.00 USD | `+45.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 774,250.00 USD | 9,510.00 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 775,970.00 USD | 1,710.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 778,220.00 USD | 2,250.00 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 876,550.00 USD | 98,330.00 USD | 0.00 USD | `+48.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 898,220.00 USD | 21,670.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 904,650.00 USD | 6,430.00 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 909,060.00 USD | 4,410.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 913,500.00 USD | 4,440.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 917,960.00 USD | 4,460.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 918,410.00 USD | 448.75 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 954,000.00 USD | 35,590.00 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 954,450.00 USD | 453.75 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 955,280.00 USD | 830.38 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 955,740.00 USD | 458.75 USD | 0.00 USD | `+57.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 956,200.00 USD | 461.25 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 960,740.00 USD | 4,540.00 USD | 0.00 USD | `+58.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 961,210.00 USD | 466.25 USD | 0.00 USD | `+59.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 961,680.00 USD | 468.75 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 962,150.00 USD | 471.25 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 962,620.00 USD | 473.75 USD | 0.00 USD | `+62.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,030,000.00 USD | 67,000.00 USD | 0.00 USD | `+63.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,030,000.00 USD | 574.50 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,030,000.00 USD | 577.50 USD | 0.00 USD | `+64.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,030,000.00 USD | 2,710.00 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,030,000.00 USD | 972.50 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,040,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,040,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,050,000.00 USD | 1,690.00 USD | 0.00 USD | `+69.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,050,000.00 USD | 992.50 USD | 0.00 USD | `+69.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,050,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,670,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+75.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,670,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,670,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,670,000.00 USD | 1,860.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,680,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,680,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,680,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,680,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,680,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,730,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,730,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,730,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,740,000.00 USD | 3,280.00 USD | 0.00 USD | `+87.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,740,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,740,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,740,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,750,000.00 USD | 1,150.00 USD | 0.00 USD | `+96.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,880,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,880,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,880,000.00 USD | 1,160.00 USD | 0.00 USD | `+99.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,880,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.89%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.27` | 20,170,000.00 USD | 0.00 USD | 20,170,000.00 USD | 92,330.00 USD | 32,960.00 USD | 72,620.00 USD |
| `7D` | `10.29` | 19,970,000.00 USD | 0.00 USD | 19,970,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD |
| `7D` | `10.31` | 19,890,000.00 USD | 0.00 USD | 19,890,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD |
| `7D` | `10.33` | 19,700,000.00 USD | 0.00 USD | 19,700,000.00 USD | 57,270.00 USD | 28,270.00 USD | 25,780.00 USD |
| `7D` | `10.35` | 19,590,000.00 USD | 0.00 USD | 19,590,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,660.00 USD |
| `7D` | `10.37` | 19,530,000.00 USD | 0.00 USD | 19,530,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD |
| `7D` | `10.39` | 19,480,000.00 USD | 0.00 USD | 19,480,000.00 USD | 4,240.00 USD | 648.05 USD | 52,480.00 USD |
| `7D` | `10.41` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,570.00 USD |
| `7D` | `10.43` | 19,280,000.00 USD | 0.00 USD | 19,280,000.00 USD | 32,710.00 USD | 14,710.00 USD | 14,950.00 USD |
| `7D` | `10.45` | 19,220,000.00 USD | 0.00 USD | 19,220,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,160.00 USD |
| `1D` | `10.46` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 27,560.00 USD | 8,350.00 USD | 16,550.00 USD |
| `7D` | `10.47` | 19,130,000.00 USD | 0.00 USD | 19,130,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,560.00 USD |
| `1D` | `10.48` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,830.00 USD |
| `7D` | `10.49` | 19,050,000.00 USD | 0.00 USD | 19,050,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD |
| `1D` | `10.50` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 23,170.00 USD | 7,140.00 USD | 8,180.00 USD |
| `7D` | `10.51` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.52` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 22,700.00 USD | 3,770.00 USD | 3,070.00 USD |
| `7D` | `10.53` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD |
| `1D` | `10.54` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 4,030.00 USD | 2,310.00 USD | 9,600.00 USD |
| `7D` | `10.55` | 18,870,000.00 USD | 0.00 USD | 18,870,000.00 USD | 55,490.00 USD | 18,800.00 USD | 20,850.00 USD |
| `1D` | `10.56` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 22,600.00 USD | 7,180.00 USD | 1,810.00 USD |
| `7D` | `10.57` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD |
| `1D` | `10.58` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,200.00 USD |
| `7D` | `10.59` | 18,670,000.00 USD | 0.00 USD | 18,670,000.00 USD | 33,510.00 USD | 9,440.00 USD | 4,290.00 USD |
| `1D` | `10.60` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,280.00 USD |
| `7D` | `10.61` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 26,680.00 USD | 10,560.00 USD | 10,080.00 USD |
| `1D` | `10.62` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,010.00 USD |
| `7D` | `10.63` | 18,580,000.00 USD | 0.00 USD | 18,580,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,840.00 USD |
| `1D` | `10.64` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,550.00 USD |
| `7D` | `10.65` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 6,380.00 USD | 2,920.00 USD | 168.26 USD |
| `1D` | `10.66` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,670.00 USD |
| `7D` | `10.67` | 18,490,000.00 USD | 0.00 USD | 18,490,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,300.00 USD |
| `1D` | `10.68` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,560.00 USD |
| `7D` | `10.69` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 18,290.00 USD | 0.00 USD | 5,490.00 USD |
| `1D` | `10.70` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.18 USD |
| `7D` | `10.71` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 14,600.00 USD | 0.00 USD | 7,840.00 USD |
| `1D` | `10.72` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,350.00 USD |
| `7D` | `10.73` | 18,410,000.00 USD | 0.00 USD | 18,410,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD |
| `1D` | `10.74` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,220.00 USD |
| `7D` | `10.75` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 17,290.00 USD | 4,010.00 USD | 318.86 USD |
| `1D` | `10.76` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,600.00 USD |
| `7D` | `10.77` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 16,290.00 USD | 3,960.00 USD | 8,860.00 USD |
| `1D` | `10.78` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 1,070.00 USD | 4,870.00 USD | 2,980.00 USD |
| `7D` | `10.79` | 18,330,000.00 USD | 0.00 USD | 18,330,000.00 USD | 57,970.00 USD | 1,400.00 USD | 24,900.00 USD |
| `1D` | `10.80` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 4,360.00 USD | 0.00 USD | 97.20 USD |
| `7D` | `10.81` | 18,240,000.00 USD | 0.00 USD | 18,240,000.00 USD | 86,860.00 USD | 28,970.00 USD | 60,740.00 USD |
| `1D` | `10.82` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 2,030.00 USD | 0.00 USD | 58.52 USD |
| `7D` | `10.83` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 123,460.00 USD | 23,810.00 USD | 45,040.00 USD |
| `1D` | `10.84` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 1,520.00 USD | 160.15 USD | 48.80 USD |
| `7D` | `10.85` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 231,910.00 USD | 26,480.00 USD | 83,030.00 USD |
| `1D` | `10.86` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 976.86 USD | 4,520.00 USD | 3,720.00 USD |
| `7D` | `10.87` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 86,700.00 USD | 41,310.00 USD | 99,990.00 USD |
| `1D` | `10.88` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 1,740.00 USD | 10,400.00 USD | 16,290.00 USD |
| `7D` | `10.89` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 235,210.00 USD | 62,890.00 USD | 175,400.00 USD |
| `1D` | `10.90` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 1,120.00 USD | 3,770.00 USD | 26,480.00 USD |
| `7D` | `10.91` | 16,830,000.00 USD | 0.00 USD | 16,830,000.00 USD | 271,580.00 USD | 48,930.00 USD | 212,340.00 USD |
| `1D` | `10.92` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,430.00 USD |
| `7D` | `10.93` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 395,920.00 USD | 107,040.00 USD | 316,050.00 USD |
| `1D` | `10.94` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 46,880.00 USD | 17,110.00 USD | 5,730.00 USD |
| `7D` | `10.95` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 308,350.00 USD | 107,220.00 USD | 305,220.00 USD |
| `1D` | `10.96` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,960.00 USD |
| `7D` | `10.97` | 14,760,000.00 USD | 0.00 USD | 14,760,000.00 USD | 165,580.00 USD | 96,900.00 USD | 114,960.00 USD |
| `1D` | `10.98` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,190.00 USD |
| `7D` | `10.99` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 94,430.00 USD | 117,780.00 USD | 249,120.00 USD |
| `1D` | `11.00` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,480.00 USD |
| `7D` | `11.01` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 141,200.00 USD | 39,420.00 USD | 103,810.00 USD |
| `1D` | `11.02` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,990.00 USD |
| `7D` | `11.03` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 423,180.00 USD | 178,040.00 USD | 207,850.00 USD |
| `1D` | `11.04` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,850.00 USD |
| `7D` | `11.05` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 260,170.00 USD | 70,790.00 USD | 155,310.00 USD |
| `1D` | `11.06` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,280.00 USD |
| `7D` | `11.07` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 437,450.00 USD | 53,630.00 USD | 223,940.00 USD |
| `1D` | `11.08` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 28,790.00 USD | 15,060.00 USD | 29,510.00 USD |
| `7D` | `11.09` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 170,080.00 USD | 126,860.00 USD | 397,660.00 USD |
| `1D` | `11.10` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 31,390.00 USD | 30,270.00 USD | 32,320.00 USD |
| `7D` | `11.11` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 575,850.00 USD | 145,120.00 USD | 441,960.00 USD |
| `1D` | `11.12` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 53,430.00 USD | 33,090.00 USD | 76,010.00 USD |
| `7D` | `11.13` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 618,260.00 USD | 148,900.00 USD | 476,250.00 USD |
| `1D` | `11.14` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,810.00 USD |
| `7D` | `11.15` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 809,230.00 USD | 195,340.00 USD | 593,130.00 USD |
| `1D` | `11.16` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD |
| `7D` | `11.17` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 527,700.00 USD | 265,230.00 USD | 520,600.00 USD |
| `1D` | `11.18` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 137,180.00 USD | 43,130.00 USD | 63,480.00 USD |
| `7D` | `11.19` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 597,320.00 USD | 148,650.00 USD | 279,490.00 USD |
| `1D` | `11.20` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 222,000.00 USD | 47,730.00 USD | 92,560.00 USD |
| `7D` | `11.21` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 319,760.00 USD | 249,060.00 USD | 282,270.00 USD |
| `1D` | `11.22` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 97,140.00 USD | 31,660.00 USD | 37,230.00 USD |
| `7D` | `11.23` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 201,470.00 USD | 197,890.00 USD | 58,390.00 USD |
| `1D` | `11.24` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 111,250.00 USD | 59,440.00 USD | 83,000.00 USD |
| `7D` | `11.25` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 332,220.00 USD | 106,830.00 USD | 101,000.00 USD |
| `1D` | `11.26` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 185,010.00 USD | 46,310.00 USD | 55,920.00 USD |
| `7D` | `11.27` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 181,530.00 USD | 128,400.00 USD | 101,750.00 USD |
| `1D` | `11.28` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD |
| `7D` | `11.29` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 104,970.00 USD | 43,570.00 USD | 55,980.00 USD |
| `1D` | `11.30` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,570.00 USD |
| `7D` | `11.31` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 13,590.00 USD | 95,360.00 USD |
| `1D` | `11.32` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,500.00 USD |
| `7D` | `11.33` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 190,980.00 USD | 11,560.00 USD | 18,940.00 USD |
| `1D` | `11.34` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD |
| `7D` | `11.35` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 310,190.00 USD | 58,690.00 USD | 0.00 USD |
| `1D` | `11.36` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD |
| `7D` | `11.37` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 44,290.00 USD | 10,650.00 USD | 99,100.00 USD |
| `1D` | `11.38` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD |
| `7D` | `11.39` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 142,620.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD |
| `7D` | `11.41` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 34,370.00 USD | 14,250.00 USD | 34,700.00 USD |
| `1D` | `11.42` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 106,690.00 USD | 34,500.00 USD | 70,800.00 USD |
| `7D` | `11.43` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 133,220.00 USD | 15,440.00 USD | 55,710.00 USD |
| `1D` | `11.44` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD |
| `7D` | `11.45` | 800,190.00 USD | 0.00 USD | 800,190.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 923,270.00 USD | 0.00 USD | 923,270.00 USD | 177,600.00 USD | 30,500.00 USD | 24,850.00 USD |
| `7D` | `11.47` | 545,660.00 USD | 0.00 USD | 545,660.00 USD | 17,370.00 USD | 14,370.00 USD | 38,770.00 USD |
| `1D` | `11.48` | 690,320.00 USD | 0.00 USD | 690,320.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD |
| `7D` | `11.49` | 475,150.00 USD | 0.00 USD | 475,150.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD |
| `1D` | `11.50` | 612,960.00 USD | 0.00 USD | 612,960.00 USD | 74,140.00 USD | 46,450.00 USD | 14,300.00 USD |
| `7D` | `11.51` | 442,030.00 USD | 0.00 USD | 442,030.00 USD | 40,840.00 USD | 33,270.00 USD | 37,240.00 USD |
| `1D` | `11.52` | 478,070.00 USD | 0.00 USD | 478,070.00 USD | 13,090.00 USD | 34,130.00 USD | 46,330.00 USD |
| `7D` | `11.53` | 330,680.00 USD | 0.00 USD | 330,680.00 USD | 34,770.00 USD | 4,270.00 USD | 0.00 USD |
| `1D` | `11.54` | 384,520.00 USD | 0.00 USD | 384,520.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD |
| `7D` | `11.55` | 291,640.00 USD | 0.00 USD | 291,640.00 USD | 0.00 USD | 55,650.00 USD | 51,530.00 USD |
| `1D` | `11.56` | 361,920.00 USD | 0.00 USD | 361,920.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD |
| `7D` | `11.57` | 184,470.00 USD | 0.00 USD | 184,470.00 USD | 0.00 USD | 0.00 USD | 69,500.00 USD |
| `1D` | `11.58` | 202,960.00 USD | 0.00 USD | 202,960.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD |
| `7D` | `11.59` | 114,970.00 USD | 0.00 USD | 114,970.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.60` | 121,320.00 USD | 0.00 USD | 121,320.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD |
| `1D` | `11.62` | 13,920.00 USD | 0.00 USD | 13,920.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD |
| `1D` | `11.63` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.63` | 92,190.00 USD | 0.00 USD | 92,190.00 USD | 34,910.00 USD | 57,280.00 USD | 0.00 USD |
| `7D` | `11.64` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.65` | 22,350.00 USD | 22,350.00 USD | 0.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD |
| `1D` | `11.66` | 37,590.00 USD | 37,590.00 USD | 0.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD |
| `7D` | `11.67` | 88,590.00 USD | 88,590.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 83,510.00 USD | 83,510.00 USD | 0.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD |
| `7D` | `11.69` | 88,970.00 USD | 88,970.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.70` | 83,740.00 USD | 83,740.00 USD | 0.00 USD | 0.00 USD | 230.72 USD | 0.00 USD |
| `7D` | `11.71` | 284,910.00 USD | 284,910.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.72` | 261,160.00 USD | 261,160.00 USD | 0.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD |
| `1D` | `11.74` | 261,490.00 USD | 261,490.00 USD | 0.00 USD | 0.00 USD | 324.58 USD | 0.00 USD |
| `7D` | `11.75` | 302,290.00 USD | 302,290.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.76` | 261,830.00 USD | 261,830.00 USD | 0.00 USD | 0.00 USD | 342.56 USD | 0.00 USD |
| `7D` | `11.77` | 333,100.00 USD | 333,100.00 USD | 0.00 USD | 30,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 278,860.00 USD | 278,860.00 USD | 0.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD |
| `7D` | `11.79` | 408,500.00 USD | 408,500.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.80` | 279,920.00 USD | 279,920.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `11.81` | 573,010.00 USD | 573,010.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.83` | 637,190.00 USD | 637,190.00 USD | 0.00 USD | 58,850.00 USD | 5,340.00 USD | 0.00 USD |
| `1D` | `11.84` | 363,810.00 USD | 363,810.00 USD | 0.00 USD | 55,360.00 USD | 1,130.00 USD | 27,400.00 USD |
| `7D` | `11.85` | 855,210.00 USD | 855,210.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD |
| `1D` | `11.86` | 435,990.00 USD | 435,990.00 USD | 0.00 USD | 232.40 USD | 33,940.00 USD | 38,000.00 USD |
| `7D` | `11.87` | 884,260.00 USD | 884,260.00 USD | 0.00 USD | 438.10 USD | 5,400.00 USD | 23,210.00 USD |
| `1D` | `11.88` | 508,830.00 USD | 508,830.00 USD | 0.00 USD | 19,640.00 USD | 15,360.00 USD | 37,840.00 USD |
| `7D` | `11.89` | 926,690.00 USD | 926,690.00 USD | 0.00 USD | 40,020.00 USD | 2,340.00 USD | 71.80 USD |
| `1D` | `11.90` | 553,050.00 USD | 553,050.00 USD | 0.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD |
| `7D` | `11.91` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | 165.74 USD |
| `1D` | `11.92` | 625,920.00 USD | 625,920.00 USD | 0.00 USD | 59,860.00 USD | 12,990.00 USD | 20.02 USD |
| `7D` | `11.93` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.94` | 671,520.00 USD | 671,520.00 USD | 0.00 USD | 1,220.00 USD | 15,870.00 USD | 28,510.00 USD |
| `7D` | `11.95` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 738,250.00 USD | 738,250.00 USD | 0.00 USD | 12,210.00 USD | 26,690.00 USD | 27,820.00 USD |
| `7D` | `11.97` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 354,730.00 USD | 35,140.00 USD | 213,090.00 USD |
| `1D` | `11.98` | 875,210.00 USD | 875,210.00 USD | 0.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD |
| `7D` | `11.99` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 242,400.00 USD | 3,330.00 USD | 119,980.00 USD |
| `1D` | `12.00` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 106,180.00 USD | 351.59 USD | 41,640.00 USD |
| `7D` | `12.01` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 164,140.00 USD | 5,360.00 USD | 219,400.00 USD |
| `1D` | `12.02` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 59,970.00 USD | 32,820.00 USD | 15,280.00 USD |
| `7D` | `12.03` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD |
| `1D` | `12.04` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 233,510.00 USD | 73,470.00 USD | 97,880.00 USD |
| `7D` | `12.05` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 330,170.00 USD | 106,020.00 USD | 188,430.00 USD |
| `1D` | `12.06` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 221,050.00 USD | 88,350.00 USD | 155,710.00 USD |
| `7D` | `12.07` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.08` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 123,260.00 USD | 45,990.00 USD | 52,790.00 USD |
| `7D` | `12.09` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,270.00 USD |
| `1D` | `12.10` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 19,140.00 USD | 9,670.00 USD | 31,070.00 USD |
| `7D` | `12.11` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD |
| `1D` | `12.12` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 141,930.00 USD | 49,190.00 USD | 58,790.00 USD |
| `7D` | `12.13` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 148,530.00 USD | 56,000.00 USD | 36,080.00 USD |
| `1D` | `12.14` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 109,520.00 USD | 28,690.00 USD | 49,210.00 USD |
| `7D` | `12.15` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 310,620.00 USD | 114,540.00 USD | 131,290.00 USD |
| `1D` | `12.16` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 96,770.00 USD | 58,750.00 USD | 53,290.00 USD |
| `7D` | `12.17` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 26,820.00 USD | 61,400.00 USD | 53,310.00 USD |
| `1D` | `12.18` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 117,230.00 USD | 39,740.00 USD | 45,980.00 USD |
| `7D` | `12.19` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 196,200.00 USD | 58,210.00 USD | 79,450.00 USD |
| `1D` | `12.20` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 89,220.00 USD | 40,880.00 USD | 25,370.00 USD |
| `7D` | `12.21` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 115,460.00 USD |
| `1D` | `12.22` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 29,450.00 USD | 42,870.00 USD | 52,590.00 USD |
| `7D` | `12.23` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 140,270.00 USD | 19,410.00 USD | 57,260.00 USD |
| `1D` | `12.24` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 33,920.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.25` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 134,500.00 USD | 56,330.00 USD | 102,920.00 USD |
| `1D` | `12.26` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 55,900.00 USD | 27,170.00 USD | 21,450.00 USD |
| `7D` | `12.27` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 141,400.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.28` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 99,490.00 USD | 24,800.00 USD | 37,690.00 USD |
| `7D` | `12.29` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 235,780.00 USD | 118,830.00 USD | 175,160.00 USD |
| `1D` | `12.30` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 58,090.00 USD | 24,040.00 USD | 45,420.00 USD |
| `7D` | `12.31` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 157,240.00 USD | 53,480.00 USD | 55,040.00 USD |
| `1D` | `12.32` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 20.46 USD |
| `7D` | `12.33` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 191,980.00 USD | 89,700.00 USD | 5,250.00 USD |
| `1D` | `12.34` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD |
| `7D` | `12.35` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 116,830.00 USD | 15,980.00 USD | 19,280.00 USD |
| `1D` | `12.36` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 19,510.00 USD | 9,040.00 USD | 5,380.00 USD |
| `7D` | `12.37` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD |
| `1D` | `12.38` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 30,170.00 USD | 6,420.00 USD | 12,890.00 USD |
| `7D` | `12.39` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 160,660.00 USD | 42,540.00 USD | 338,190.00 USD |
| `1D` | `12.40` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 18,820.00 USD | 23,720.00 USD | 22,990.00 USD |
| `7D` | `12.41` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 80,100.00 USD | 32,410.00 USD | 195,310.00 USD |
| `1D` | `12.42` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 51,980.00 USD | 13,980.00 USD | 9,640.00 USD |
| `7D` | `12.43` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,100.00 USD |
| `1D` | `12.44` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 17,630.00 USD | 10,270.00 USD | 6,520.00 USD |
| `7D` | `12.45` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 57,130.00 USD | 118,850.00 USD | 258,810.00 USD |
| `1D` | `12.46` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 411.51 USD | 15,260.00 USD | 11,560.00 USD |
| `7D` | `12.47` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 66,870.00 USD | 29,080.00 USD | 192,400.00 USD |
| `1D` | `12.48` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 2,220.00 USD | 2,560.00 USD | 8,270.00 USD |
| `7D` | `12.49` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 91,900.00 USD | 17,840.00 USD | 60,380.00 USD |
| `1D` | `12.50` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 620.31 USD | 4,320.00 USD | 8,220.00 USD |
| `7D` | `12.51` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 136,260.00 USD | 26,650.00 USD | 85,850.00 USD |
| `1D` | `12.52` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 21,510.00 USD | 5,020.00 USD | 12,220.00 USD |
| `7D` | `12.53` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 131,510.00 USD | 57,030.00 USD | 128,240.00 USD |
| `1D` | `12.54` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 14,970.00 USD | 2,830.00 USD | 28.77 USD |
| `7D` | `12.55` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 126,130.00 USD | 45,060.00 USD | 82,010.00 USD |
| `1D` | `12.56` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD |
| `7D` | `12.57` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 131,970.00 USD | 65,650.00 USD | 10,850.00 USD |
| `1D` | `12.58` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 11,190.00 USD |
| `7D` | `12.59` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 65,910.00 USD | 17,430.00 USD | 36,480.00 USD |
| `1D` | `12.60` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD |
| `7D` | `12.61` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD |
| `1D` | `12.62` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.63` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 62,580.00 USD | 28,520.00 USD | 81,370.00 USD |
| `1D` | `12.64` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD |
| `7D` | `12.65` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 76,240.00 USD | 26,110.00 USD | 131,430.00 USD |
| `1D` | `12.66` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD |
| `7D` | `12.67` | 13,150,000.00 USD | 13,150,000.00 USD | 0.00 USD | 66,110.00 USD | 19,940.00 USD | 223,860.00 USD |
| `1D` | `12.68` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD |
| `7D` | `12.69` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 44,600.00 USD | 34,670.00 USD | 154,500.00 USD |
| `1D` | `12.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 2,660.00 USD |
| `7D` | `12.71` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 31,960.00 USD | 43,220.00 USD | 24,430.00 USD |
| `1D` | `12.72` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 107.28 USD |
| `7D` | `12.73` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 86,570.00 USD |
| `1D` | `12.74` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 20,500.00 USD | 8,140.00 USD | 6,530.00 USD |
| `7D` | `12.75` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 33,680.00 USD | 14,710.00 USD | 14,980.00 USD |
| `1D` | `12.76` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 39,130.00 USD | 11,090.00 USD | 16,300.00 USD |
| `7D` | `12.77` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 36,060.00 USD | 11,060.00 USD | 42,330.00 USD |
| `1D` | `12.78` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,020.00 USD |
| `7D` | `12.79` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 56,200.00 USD | 22,760.00 USD | 6,590.00 USD |
| `1D` | `12.80` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 12,430.00 USD | 4,740.00 USD | 12,830.00 USD |
| `7D` | `12.81` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD |
| `1D` | `12.82` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 2,680.00 USD | 1,320.00 USD | 2,000.00 USD |
| `7D` | `12.83` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD |
| `1D` | `12.84` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 20,500.00 USD | 5,820.00 USD | 6,190.00 USD |
| `7D` | `12.85` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD |
| `1D` | `12.86` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 22,700.00 USD | 3,770.00 USD | 3,060.00 USD |
| `7D` | `12.87` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 10,160.00 USD | 6,560.00 USD | 21,060.00 USD |
| `1D` | `12.88` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 3,410.00 USD | 2,310.00 USD | 9,580.00 USD |
| `7D` | `12.89` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 21,040.00 USD |
| `1D` | `12.90` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 21,720.00 USD | 7,180.00 USD | 1,810.00 USD |
| `7D` | `12.91` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD |
| `1D` | `12.92` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD |
| `7D` | `12.93` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD |
| `1D` | `12.94` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.95` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 2,290.00 USD | 9,210.00 USD | 4,200.00 USD |
| `1D` | `12.96` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,270.00 USD |
| `7D` | `12.97` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 15,020.00 USD | 10,560.00 USD | 10,050.00 USD |
| `1D` | `12.98` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 24,650.00 USD | 7,080.00 USD | 11,950.00 USD |
| `7D` | `12.99` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD |
| `1D` | `13.00` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 17,330.00 USD | 7,780.00 USD | 16,530.00 USD |
| `7D` | `13.01` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 2,070.00 USD | 2,920.00 USD | 0.00 USD |
| `1D` | `13.02` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD |
| `7D` | `13.03` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `1D` | `13.04` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `13.05` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD |
| `7D` | `13.07` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `13.09` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `13.11` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD |
| `7D` | `13.13` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD |
| `7D` | `13.19` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 13,890.00 USD | 259.77 USD | 8,930.00 USD |
| `7D` | `13.23` | 14,500,000.00 USD | 14,500,000.00 USD | 0.00 USD | 15,330.00 USD | 0.00 USD | 22.55 USD |
| `7D` | `13.25` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 18,020.00 USD | 4,640.00 USD | 11,590.00 USD |
| `7D` | `13.27` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 10,290.00 USD | 11,080.00 USD | 10,920.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `554.28M` | Total OI Tokens: `47,640,331.1 LINK`
  * 1h OI Change: `-1.17%` | 4h OI Change: `-2.32%` | 24h OI Change: `-2.52%`
  * Exchange Breakdown: Binance=`105.26M` | Bybit=`65.53M` | OKX=`26.38M` | Hyperliquid=`56.39M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.51K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0013%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0057%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `44.02%` | `55.98%` | `0.79` | 719,660.00 USD |
| `15M` | `Binance` | `34.61%` | `65.39%` | `0.53` | 198,940.00 USD |
| `15M` | `OKX` | `69.51%` | `30.49%` | `2.28` | 47,910.00 USD |
| `15M` | `Bybit` | `49.71%` | `50.29%` | `0.99` | 55,750.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 15,300.00 USD |
| `15M` | `Gate` | `52.9%` | `47.1%` | `1.12` | 18,950.00 USD |
| `15M` | `Bitget` | `67.56%` | `32.44%` | `2.08` | 7,060.00 USD |
| `15M` | `BingX` | `21.54%` | `78.46%` | `0.27` | 97,400.00 USD |
| `15M` | `MEXC` | `50.4%` | `49.6%` | `1.02` | 4,500.00 USD |
| `15M` | `Bitunix` | `51.6%` | `48.4%` | `1.07` | 5,610.00 USD |
| `15M` | `Hyperliquid` | `78.91%` | `21.09%` | `3.74` | 11,670.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.2%` | `47.8%` | `1.09` | 138,610.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 104,580.00 USD |
| `15M` | `HTX` | `43.58%` | `56.42%` | `0.77` | 12,090.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.56%` | `22.44%` | `3.46` | 886.46 USD |
| `15M` | `Aster` | `34.1%` | `65.9%` | `0.52` | 389.30 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.35%` | `53.65%` | `0.86` | 8.42 USD |
| `15M` | `Whale Positions` | `34.61%` | `65.39%` | `0.53` | 198,940.00 USD |
| `15M` | `Global Accounts` | `44.02%` | `55.98%` | `0.79` | 719,660.00 USD |
| `1H` | `LINK` | `50.44%` | `49.56%` | `1.02` | 2,440,000.00 USD |
| `1H` | `Binance` | `62.23%` | `37.77%` | `1.65` | 817,700.00 USD |
| `1H` | `OKX` | `49.7%` | `50.3%` | `0.99` | 158,250.00 USD |
| `1H` | `Bybit` | `81.95%` | `18.05%` | `4.54` | 179,750.00 USD |
| `1H` | `KuCoin` | `46.8%` | `53.2%` | `0.88` | 60,450.00 USD |
| `1H` | `Gate` | `47.95%` | `52.05%` | `0.92` | 61,630.00 USD |
| `1H` | `Bitget` | `58.9%` | `41.1%` | `1.43` | 15,570.00 USD |
| `1H` | `BingX` | `33.21%` | `66.79%` | `0.50` | 190,400.00 USD |
| `1H` | `MEXC` | `67.08%` | `32.92%` | `2.04` | 18,530.00 USD |
| `1H` | `Bitunix` | `56.67%` | `43.33%` | `1.31` | 21,800.00 USD |
| `1H` | `Hyperliquid` | `86.45%` | `13.55%` | `6.38` | 44,830.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 374,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.27%` | `80.73%` | `0.24` | 441,970.00 USD |
| `1H` | `HTX` | `57.76%` | `42.24%` | `1.37` | 45,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.12%` | `42.88%` | `1.33` | 3,630.00 USD |
| `1H` | `Aster` | `19.85%` | `80.15%` | `0.25` | 782.82 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.67%` | `94.33%` | `0.06` | 2,320.00 USD |
| `1H` | `Whale Positions` | `62.23%` | `37.77%` | `1.65` | 817,700.00 USD |
| `1H` | `Global Accounts` | `50.44%` | `49.56%` | `1.02` | 2,440,000.00 USD |
| `4H` | `LINK` | `45.83%` | `54.17%` | `0.85` | 11,130,000.00 USD |
| `4H` | `Binance` | `52.92%` | `47.08%` | `1.12` | 4,010,000.00 USD |
| `4H` | `OKX` | `46.13%` | `53.87%` | `0.86` | 683,750.00 USD |
| `4H` | `Bybit` | `56.8%` | `43.2%` | `1.31` | 563,860.00 USD |
| `4H` | `KuCoin` | `49.38%` | `50.62%` | `0.98` | 270,030.00 USD |
| `4H` | `Gate` | `56.98%` | `43.02%` | `1.32` | 287,860.00 USD |
| `4H` | `Bitget` | `58.43%` | `41.57%` | `1.41` | 145,880.00 USD |
| `4H` | `BingX` | `30.34%` | `69.66%` | `0.44` | 882,820.00 USD |
| `4H` | `MEXC` | `61.92%` | `38.08%` | `1.63` | 145,420.00 USD |
| `4H` | `Bitunix` | `52.1%` | `47.9%` | `1.09` | 116,760.00 USD |
| `4H` | `Hyperliquid` | `82.25%` | `17.75%` | `4.63` | 369,020.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.2%` | `49.8%` | `1.01` | 1,740,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.99%` | `89.01%` | `0.12` | 1,560,000.00 USD |
| `4H` | `HTX` | `54.91%` | `45.09%` | `1.22` | 195,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `77.6%` | `22.4%` | `3.46` | 91,200.00 USD |
| `4H` | `Aster` | `13.3%` | `86.7%` | `0.15` | 8,010.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `28.43%` | `71.57%` | `0.40` | 61,730.00 USD |
| `4H` | `Whale Positions` | `52.92%` | `47.08%` | `1.12` | 4,010,000.00 USD |
| `4H` | `Global Accounts` | `45.83%` | `54.17%` | `0.85` | 11,130,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.83` | `11.83` | `11.83` | `11.87` | `11.79` | 1,261,426.96 USD | 528,120.38 USD | 733,306.58 USD | -205,186.20 USD | `-16.27%` | `8B / 14S` |
| `5:00 UTC` | `11.80` | `11.80` | `11.80` | `11.83` | `11.79` | 889,528.52 USD | 480,169.70 USD | 409,358.82 USD | 70,810.88 USD | `+7.96%` | `8B / 3S` |
| `0:00 UTC` | `11.78` | `11.76` | `11.78` | `11.84` | `11.71` | 1,746,825.55 USD | 823,777.15 USD | 923,048.41 USD | -99,271.26 USD | `-5.68%` | `22B / 37S` |
| `5:00 UTC` | `11.71` | `11.70` | `11.71` | `11.74` | `11.66` | 1,705,508.25 USD | 855,092.75 USD | 850,415.50 USD | 4,677.25 USD | `+0.27%` | `14B / 10S` |
| `0:00 UTC` | `11.73` | `11.73` | `11.73` | `11.75` | `11.71` | 756,364.68 USD | 311,101.50 USD | 445,263.18 USD | -134,161.69 USD | `-17.74%` | `6B / 13S` |
| `5:00 UTC` | `11.74` | `11.73` | `11.74` | `11.76` | `11.69` | 1,033,883.46 USD | 539,127.77 USD | 494,755.69 USD | 44,372.08 USD | `+4.29%` | `15B / 13S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.64` | `11.64` | `11.64` | `11.66` | `11.63` | 408,062.57 USD | 135,244.47 USD | 272,818.10 USD | -137,573.63 USD | `-33.71%` | `6B / 11S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -2,420.00 USD | 92,370.00 USD | **`ACCUMULATION`** |
| `15m` | -47,900.00 USD | -318,750.00 USD | **`DISTRIBUTION`** |
| `30m` | -94,310.00 USD | 146,710.00 USD | **`ACCUMULATION`** |
| `1h` | -141,640.00 USD | -548,180.00 USD | **`DISTRIBUTION`** |
| `2h` | -629,520.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -391,870.00 USD | -2,710,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 183,710.00 USD | -1,090,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 270,450.00 USD | -917,460.00 USD | **`DISTRIBUTION`** |
| `12h` | 146,900.00 USD | 1,000.00 USD | **`ACCUMULATION`** |
| `24h` | 544,540.00 USD | -3,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,980,000.00 USD | -24,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -68,940,000.00 USD | -187,700,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-2.42K` | 15m=`-47.90K` | 1h=`-141.64K` | 24h=`+544.54K`
* Futures Capital Netflows: 5m=`+92.37K` | 15m=`-318.75K` | 1h=`-548.18K` | 24h=`-3.84M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.44` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.11` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `14.76`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `13.24` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `8.59`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
