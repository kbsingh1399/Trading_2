# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-29 22:39:55 IST` (`2026-10-29 17:09:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.79` | **Live Ask Quote**: `11.88` | **Mid Price**: `11.83`
- **Spread Points**: `90.00` | **Spread BPS**: `76.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.55` | VWAP Z-Score: `+1.36` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0764` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.10` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.11` | Lower -3.00σ Band: `10.99`
  * Upper +2.51σ Band: `12.02` | Lower -2.51σ Band: `11.08`
  * Upper +2.01σ Band: `11.92` | Lower -2.01σ Band: `11.17`
  * Upper +2.00σ Band: `11.92` | Lower -2.00σ Band: `11.18`
  * Upper +1.28σ Band: `11.79` | Lower -1.28σ Band: `11.31`
  * Upper +1.00σ Band: `11.74` | Lower -1.00σ Band: `11.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.81` | EMA-20=`11.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.62` (Slope: `+0.0000`) | EMA-100=`11.58`
  * Institutional Anchors: EMA-144=`11.56` | EMA-200=`11.52` (Slope: `+0.3028`) | EMA-233=`11.50`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`11.23` | Weekly High=`11.96` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.92` (Distance: `-0.83%`)
  * Point of Control (POC) = `11.77` (Distance: `+0.44%`)
  * Value Area Low (VAL) = `11.42` (Distance: `+3.51%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.56` | Weekly POC=`11.41` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.96` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.78` - `11.88`
  * Optimal Trade Entry (OTE 0.705): `11.85`
  * Structural Invalidation Anchor (0.786): `11.93`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.85` | `11.87` | `11.83` | `11.86` | `37,358` | 442,669.46 USD | -165,475.47 USD | `-37.38%` | 1,367,637.96 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.86` | `11.87` | `11.84` | `11.86` | `14,076` | 166,864.21 USD | 12,278.43 USD | `+7.36%` | 1,379,916.39 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.86` | `11.87` | `11.84` | `11.84` | `20,211` | 239,572.18 USD | -57,178.18 USD | `-23.87%` | 1,322,738.21 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.90` | `11.91` | `11.82` | `11.86` | `203,767` | 2,416,227.23 USD | -349,932.00 USD | `-14.48%` | 1,573,287.14 USD | `-1.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `11.86` | `11.87` | `11.82` | `11.86` | `77,975` | 923,896.67 USD | -200,671.96 USD | `-21.72%` | 1,372,615.17 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.86` | `11.87` | `11.84` | `11.84` | `20,208` | 239,532.04 USD | -57,218.31 USD | `-23.89%` | 1,315,396.86 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `11.79` | `11.97` | `11.78` | `11.96` | `786,594` | 9,353,879.78 USD | 284,622.02 USD | `+3.04%` | 1,962,670.99 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.96` | `12.01` | `11.82` | `11.86` | `812,884` | 9,680,116.17 USD | -943,322.93 USD | `-9.74%` | 1,019,348.05 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.86` | `11.87` | `11.84` | `11.84` | `20,208` | 239,532.04 USD | -57,218.31 USD | `-23.89%` | 962,129.75 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.82` | `11.83` | `833,535` | 9,924,894.70 USD | -1,005,707.47 USD | `-10.13%` | -459,524.35 USD | `-0.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.82` | `11.83` | `833,535` | 9,924,894.70 USD | -1,005,707.47 USD | `-10.13%` | -459,524.35 USD | `-0.72` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.83`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `504` | `0x73ce...8ce9` | `LONG` | 4,732,537.24 USD | `400,011,600.00` | `12.05` | `11.83` | `9.13` | -87,216.46 USD | `-1.84%` | `5X Cross` |
| `645` | `0x5b5d...c060` | `SHORT` | 3,687,744.61 USD | `311,728,200.00` | `13.61` | `11.83` | `474.87` | 554,387.50 USD | `+15.03%` | `3X Cross` |
| `653` | `0xb83d...6e36` | `SHORT` | 3,645,746.31 USD | `308,152,000.00` | `12.93` | `11.83` | `403.13` | 339,507.18 USD | `+9.31%` | `3X Cross` |
| `874` | `0x458d...ab3b` | `LONG` | 2,689,542.14 USD | `227,156,700.00` | `13.13` | `11.83` | `9.34` | -292,688.25 USD | `-10.88%` | `3X Isolated` |
| `945` | `0xdd53...2b13` | `SHORT` | 2,442,189.85 USD | `206,475,300.00` | `11.92` | `11.83` | `262.73` | 19,033.08 USD | `+0.78%` | `3X Cross` |
| `976` | `0x3dc9...54b0` | `SHORT` | 2,372,200.00 USD | `200,000,000.00` | `7.56` | `11.83` | `76.29` | -861,041.58 USD | `-36.30%` | `10X Cross` |
| `1005` | `0x45d2...4029` | `SHORT` | 2,314,133.50 USD | `195,500,000.00` | `11.54` | `11.83` | `181.37` | -57,650.07 USD | `-2.49%` | `10X Cross` |
| `1196` | `0x6540...f7b7` | `LONG` | 1,940,395.23 USD | `164,051,000.00` | `12.48` | `11.83` | `8.01` | -106,421.16 USD | `-5.48%` | `5X Isolated` |
| `1253` | `0xeadc...9d55` | `LONG` | 1,868,172.39 USD | `157,691,600.00` | `9.43` | `11.83` | `0.000000` | 381,517.48 USD | `+20.42%` | `10X Cross` |
| `1616` | `0x9df2...c665` | `SHORT` | 1,398,634.79 USD | `118,217,800.00` | `11.48` | `11.83` | `244.69` | -41,031.23 USD | `-2.93%` | `10X Cross` |
| `1642` | `0xf6f3...47f8` | `SHORT` | 1,362,466.39 USD | `115,024,600.00` | `11.42` | `11.83` | `18.15` | -49,136.20 USD | `-3.61%` | `5X Cross` |
| `1813` | `0xfe7e...11b4` | `LONG` | 1,196,408.72 USD | `101,142,000.00` | `14.47` | `11.83` | `5.33` | -266,704.43 USD | `-22.29%` | `5X Isolated` |
| `1845` | `0x8af7...fa05` | `SHORT` | 1,166,964.67 USD | `98,661,200.00` | `14.08` | `11.83` | `203.12` | 222,217.87 USD | `+19.04%` | `10X Cross` |
| `1901` | `0xb7ec...5166` | `LONG` | 1,119,729.87 USD | `94,515,900.00` | `9.01` | `11.83` | `7.20` | 267,869.29 USD | `+23.92%` | `4X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.45` | 7,522.65 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.52K USD at 11.4500 USD [API] | `2026-10-27 19:31:15` |
| `ANNOUNCEMENT` | `INFO` | `11.48` | 6,640.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.64K USD at 11.4850 USD [API] | `2026-10-27 19:58:25` |
| `ANNOUNCEMENT` | `INFO` | `11.46` | 5,830.72 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.83K USD at 11.4620 USD [API] | `2026-10-27 20:52:10` |
| `ANNOUNCEMENT` | `INFO` | `11.46` | 5,830.34 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.83K USD at 11.4590 USD [API] | `2026-10-27 20:53:18` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 5,463.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.5510 USD [API] | `2026-10-27 21:32:55` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 5,037.83 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.04K USD at 11.5520 USD [API] | `2026-10-27 21:32:55` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.80` (Vol: 215,600.00 USD, Dist: `+1.12%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.20%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+3.23%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.37%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.68%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.46%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.69%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.65` | 4,740.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 7,110.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 13,490.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 927.99 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 3,290.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 14,850.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 355.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 83,460.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 5,640.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 5,770.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 101.26 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 220,660.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 46,260.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,200.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 17,120.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 40,010.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 9,450.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 90,620.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 546,570.00 USD | 13,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 243.62 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 748.14 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 290.38 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 19,570.00 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 120,390.00 USD | 12,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 12,060.00 USD | 12,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,180.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,590.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 101,560.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 3,830.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,920.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 9,270.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 43,330.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 3,190.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 687,620.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 8,460.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 31,820.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 4,710.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 16,920.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 9,820.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 2,770.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 1,090.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,130.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,390,000.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,750.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 90,750.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,840.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 11,180.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 16,760.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 11,540.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 331,990.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,050.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,640.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 23,010.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,750,000.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 1,620.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,200,000.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 28,660.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 40,810.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 11,030.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 54,080.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 243,780.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 778,350.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 647,220.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 171,050.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.20` | 19,770,000.00 USD | 19,770,000.00 USD | 35,120.00 USD | 15,990.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 19,650,000.00 USD | 19,650,000.00 USD | 101,890.00 USD | 28,560.00 USD | 86,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 19,430,000.00 USD | 19,430,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 33,280.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 19,240,000.00 USD | 19,240,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 19,100,000.00 USD | 19,100,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 18,970,000.00 USD | 18,970,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 18,870,000.00 USD | 18,870,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 18,730,000.00 USD | 18,730,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 14,120.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 18,600,000.00 USD | 18,600,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 18,560,000.00 USD | 18,560,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 18,510,000.00 USD | 18,510,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 6,470,000.00 USD | 6,470,000.00 USD | 79,170.00 USD | 22,500.00 USD | 45,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 18,360,000.00 USD | 18,360,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 6,320,000.00 USD | 6,320,000.00 USD | 43,450.00 USD | 12,260.00 USD | 18,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 18,280,000.00 USD | 18,280,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 14,500.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 6,250,000.00 USD | 6,250,000.00 USD | 19,150.00 USD | 3,120.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 18,230,000.00 USD | 18,230,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 6,210,000.00 USD | 6,210,000.00 USD | 12,430.00 USD | 5,860.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 18,120,000.00 USD | 18,120,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 6,190,000.00 USD | 6,190,000.00 USD | 14,440.00 USD | 4,760.00 USD | 8,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 18,060,000.00 USD | 18,060,000.00 USD | 42,030.00 USD | 16,000.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 6,160,000.00 USD | 6,160,000.00 USD | 19,070.00 USD | 1,990.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 17,990,000.00 USD | 17,990,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 6,130,000.00 USD | 6,130,000.00 USD | 8,510.00 USD | 3,720.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 17,950,000.00 USD | 17,950,000.00 USD | 25,600.00 USD | 72.80 USD | 12,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,960.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 6,110,000.00 USD | 6,110,000.00 USD | 20,140.00 USD | 6,800.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 17,910,000.00 USD | 17,910,000.00 USD | 51,230.00 USD | 16,690.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 6,080,000.00 USD | 6,080,000.00 USD | 20,460.00 USD | 3,900.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 17,830,000.00 USD | 17,830,000.00 USD | 84,220.00 USD | 6,710.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,060,000.00 USD | 6,060,000.00 USD | 927.38 USD | 3,630.00 USD | 13.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 17,720,000.00 USD | 17,720,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,050,000.00 USD | 6,050,000.00 USD | 18,310.00 USD | 4,690.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 17,680,000.00 USD | 17,680,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 6,020,000.00 USD | 6,020,000.00 USD | 9,170.00 USD | 5,650.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 17,650,000.00 USD | 17,650,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 6,000,000.00 USD | 6,000,000.00 USD | 17,480.00 USD | 3,100.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 17,600,000.00 USD | 17,600,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 5,970,000.00 USD | 5,970,000.00 USD | 4,580.00 USD | 1,380.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 17,580,000.00 USD | 17,580,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 5,970,000.00 USD | 5,970,000.00 USD | 8,580.00 USD | 0.00 USD | 10.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 17,550,000.00 USD | 17,550,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 5,960,000.00 USD | 5,960,000.00 USD | 48.73 USD | 2,350.00 USD | 12.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 17,530,000.00 USD | 17,530,000.00 USD | 21,070.00 USD | 4,880.00 USD | 264.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 5,950,000.00 USD | 5,950,000.00 USD | 1,880.00 USD | 2,320.00 USD | 142.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 17,510,000.00 USD | 17,510,000.00 USD | 25,580.00 USD | 3,690.00 USD | 315.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 999,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 5,950,000.00 USD | 5,950,000.00 USD | 1,820.00 USD | 0.00 USD | 150.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 17,480,000.00 USD | 17,480,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 5,950,000.00 USD | 5,950,000.00 USD | 1,070.00 USD | 2,330.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 17,460,000.00 USD | 17,460,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 5,940,000.00 USD | 5,940,000.00 USD | 4,760.00 USD | 0.00 USD | 76.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 17,410,000.00 USD | 17,410,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 5,940,000.00 USD | 5,940,000.00 USD | 2,030.00 USD | 0.00 USD | 55.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 17,270,000.00 USD | 17,270,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 5,930,000.00 USD | 5,930,000.00 USD | 2,330.00 USD | 160.15 USD | 45.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,100,000.00 USD | 17,100,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 81,870.00 USD | 785,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 5,930,000.00 USD | 5,930,000.00 USD | 976.86 USD | 4,520.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 16,930,000.00 USD | 16,930,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 5,920,000.00 USD | 5,920,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 16,580,000.00 USD | 16,580,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 5,890,000.00 USD | 5,890,000.00 USD | 6,580.00 USD | 3,770.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 16,120,000.00 USD | 16,120,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 5,860,000.00 USD | 5,860,000.00 USD | 67,690.00 USD | 28,790.00 USD | 58,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 15,680,000.00 USD | 15,680,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 5,700,000.00 USD | 5,700,000.00 USD | 47,820.00 USD | 17,110.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 14,780,000.00 USD | 14,780,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 703,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 5,630,000.00 USD | 5,630,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 14,190,000.00 USD | 14,190,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 5,480,000.00 USD | 5,480,000.00 USD | 24,400.00 USD | 2,590.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 13,630,000.00 USD | 13,630,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 5,430,000.00 USD | 5,430,000.00 USD | 16,000.00 USD | 7,740.00 USD | 22,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 13,260,000.00 USD | 13,260,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 5,380,000.00 USD | 5,380,000.00 USD | 95,850.00 USD | 30,950.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 12,880,000.00 USD | 12,880,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,220,000.00 USD | 5,220,000.00 USD | 26,860.00 USD | 21,620.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,370,000.00 USD | 12,370,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 23,500.00 USD | 145,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,130,000.00 USD | 5,130,000.00 USD | 48,320.00 USD | 8,320.00 USD | 38,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 11,720,000.00 USD | 11,720,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,030,000.00 USD | 5,030,000.00 USD | 65,540.00 USD | 39,710.00 USD | 125,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 11,310,000.00 USD | 11,310,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 4,800,000.00 USD | 4,800,000.00 USD | 146,640.00 USD | 48,060.00 USD | 113,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 10,500,000.00 USD | 10,500,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 4,500,000.00 USD | 4,500,000.00 USD | 72,050.00 USD | 45,820.00 USD | 108,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 9,310,000.00 USD | 9,310,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 4,270,000.00 USD | 4,270,000.00 USD | 184,030.00 USD | 79,200.00 USD | 142,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 8,260,000.00 USD | 8,260,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 49,590.00 USD | 122,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 3,860,000.00 USD | 3,860,000.00 USD | 193,330.00 USD | 56,510.00 USD | 88,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 6,780,000.00 USD | 6,780,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 3,530,000.00 USD | 3,530,000.00 USD | 117,090.00 USD | 41,100.00 USD | 44,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 5,480,000.00 USD | 5,480,000.00 USD | 641,660.00 USD | 214,580.00 USD | 541,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 3,320,000.00 USD | 3,320,000.00 USD | 190,060.00 USD | 42,000.00 USD | 93,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,080,000.00 USD | 4,080,000.00 USD | 371,240.00 USD | 239,970.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 3,000,000.00 USD | 3,000,000.00 USD | 90,220.00 USD | 30,210.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,340,000.00 USD | 3,340,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 2,830,000.00 USD | 2,830,000.00 USD | 126,690.00 USD | 67,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 2,690,000.00 USD | 2,690,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 21,540.00 USD | 72,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 2,560,000.00 USD | 2,560,000.00 USD | 206,400.00 USD | 76,800.00 USD | 120,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,410,000.00 USD | 2,410,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 2,150,000.00 USD | 2,150,000.00 USD | 47,350.00 USD | 18,970.00 USD | 68,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 1,860,000.00 USD | 1,860,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 2,020,000.00 USD | 2,020,000.00 USD | 152,430.00 USD | 22,430.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,460,000.00 USD | 1,460,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 1,820,000.00 USD | 1,820,000.00 USD | 259,460.00 USD | 7,960.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,390,000.00 USD | 1,390,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 1,540,000.00 USD | 1,540,000.00 USD | 244,400.00 USD | 33,020.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,270,000.00 USD | 1,270,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 46,360.00 USD | 51,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 1,250,000.00 USD | 1,250,000.00 USD | 281,440.00 USD | 90,890.00 USD | 70,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 927,160.00 USD | 927,160.00 USD | 170,150.00 USD | 48,220.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 802,600.00 USD | 802,600.00 USD | 22,780.00 USD | 38,670.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 663,400.00 USD | 663,400.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 682,870.00 USD | 682,870.00 USD | 68,450.00 USD | 12,830.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 572,020.00 USD | 572,020.00 USD | 116,360.00 USD | 2,880.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 534,770.00 USD | 534,770.00 USD | 58,720.00 USD | 14,250.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 435,960.00 USD | 435,960.00 USD | 30,910.00 USD | 0.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 441,290.00 USD | 441,290.00 USD | 58,750.00 USD | 20,030.00 USD | 42,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 380,330.00 USD | 380,330.00 USD | 104,540.00 USD | 29,600.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 319,640.00 USD | 319,640.00 USD | 66,120.00 USD | 3,810.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 234,480.00 USD | 234,480.00 USD | 0.00 USD | 834.95 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 208,250.00 USD | 208,250.00 USD | 0.00 USD | 364.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 233,650.00 USD | 233,650.00 USD | 63,350.00 USD | 29,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 207,890.00 USD | 207,890.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 140,830.00 USD | 140,830.00 USD | 0.00 USD | 23,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.52` | 166,910.00 USD | 166,910.00 USD | 0.00 USD | 617.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.54` | 166,290.00 USD | 166,290.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 116,850.00 USD | 116,850.00 USD | 0.00 USD | 0.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.56` | 131,520.00 USD | 131,520.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.58` | 120,890.00 USD | 120,890.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 68,110.00 USD | 68,110.00 USD | 66,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.64` | 89,270.00 USD | 89,270.00 USD | 0.00 USD | 56,880.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.65` | 4,910.00 USD | 4,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.66` | 1,220.00 USD | 1,220.00 USD | 0.00 USD | 677.25 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.68` | 542.34 USD | 542.34 USD | 0.00 USD | 542.34 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 381.10 USD | 381.10 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 156,330.00 USD | 156,330.00 USD | 82,770.00 USD | 47,670.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 356,850.00 USD | 356,850.00 USD | 131,190.00 USD | 25,910.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 185,060.00 USD | 185,060.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 410,610.00 USD | 410,610.00 USD | 25,420.00 USD | 11,980.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 208,130.00 USD | 208,130.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 675,120.00 USD | 675,120.00 USD | 107,680.00 USD | 15,900.00 USD | 140,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 275,570.00 USD | 275,570.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 935,180.00 USD | 935,180.00 USD | 16,180.00 USD | 18,030.00 USD | 225,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 1,110,000.00 USD | 1,110,000.00 USD | 103,560.00 USD | 36,200.00 USD | 39,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 744,880.00 USD | 744,880.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 1,530,000.00 USD | 1,530,000.00 USD | 209,070.00 USD | 90,430.00 USD | 120,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 1,070,000.00 USD | 1,070,000.00 USD | 158,640.00 USD | 77,820.00 USD | 91,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 1,880,000.00 USD | 1,880,000.00 USD | 189,720.00 USD | 56,750.00 USD | 98,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,590,000.00 USD | 1,590,000.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 2,120,000.00 USD | 2,120,000.00 USD | 113,730.00 USD | 43,150.00 USD | 85,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 2,510,000.00 USD | 2,510,000.00 USD | 607,590.00 USD | 38,220.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 2,360,000.00 USD | 2,360,000.00 USD | 155,380.00 USD | 37,550.00 USD | 49,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 3,200,000.00 USD | 3,200,000.00 USD | 392,850.00 USD | 20,500.00 USD | 271,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 2,550,000.00 USD | 2,550,000.00 USD | 82,190.00 USD | 22,830.00 USD | 78,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 3,670,000.00 USD | 3,670,000.00 USD | 282,480.00 USD | 31,020.00 USD | 158,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 2,720,000.00 USD | 2,720,000.00 USD | 92,450.00 USD | 17,780.00 USD | 59,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 4,170,000.00 USD | 4,170,000.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 3,000,000.00 USD | 3,000,000.00 USD | 153,170.00 USD | 55,770.00 USD | 76,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 4,690,000.00 USD | 4,690,000.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 3,160,000.00 USD | 3,160,000.00 USD | 130,630.00 USD | 13,270.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 5,200,000.00 USD | 5,200,000.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 3,280,000.00 USD | 3,280,000.00 USD | 91,030.00 USD | 3,430.00 USD | 30,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 5,780,000.00 USD | 5,780,000.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 3,580,000.00 USD | 3,580,000.00 USD | 129,420.00 USD | 33,920.00 USD | 128,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 6,290,000.00 USD | 6,290,000.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 3,880,000.00 USD | 3,880,000.00 USD | 169,130.00 USD | 50,620.00 USD | 81,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 6,830,000.00 USD | 6,830,000.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 4,240,000.00 USD | 4,240,000.00 USD | 197,410.00 USD | 69,720.00 USD | 90,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 7,380,000.00 USD | 7,380,000.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.05` | 2,600.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.06` | 4,640,000.00 USD | 4,640,000.00 USD | 191,800.00 USD | 74,220.00 USD | 142,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 7,860,000.00 USD | 7,860,000.00 USD | 234,210.00 USD | 101,560.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 4,860,000.00 USD | 4,860,000.00 USD | 135,610.00 USD | 36,290.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 8,490,000.00 USD | 8,490,000.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 4,910,000.00 USD | 4,910,000.00 USD | 19,390.00 USD | 6,920.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 8,620,000.00 USD | 8,620,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 5,040,000.00 USD | 5,040,000.00 USD | 76,860.00 USD | 25,560.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 8,850,000.00 USD | 8,850,000.00 USD | 89,810.00 USD | 44,490.00 USD | 95,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 5,140,000.00 USD | 5,140,000.00 USD | 66,230.00 USD | 10,120.00 USD | 25,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 9,070,000.00 USD | 9,070,000.00 USD | 118,920.00 USD | 64,740.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,130.00 USD | 5,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 5,250,000.00 USD | 5,250,000.00 USD | 59,700.00 USD | 33,220.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 9,320,000.00 USD | 9,320,000.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 5,320,000.00 USD | 5,320,000.00 USD | 29,420.00 USD | 19,650.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 9,420,000.00 USD | 9,420,000.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 5,410,000.00 USD | 5,410,000.00 USD | 56,330.00 USD | 19,400.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 9,690,000.00 USD | 9,690,000.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 5,490,000.00 USD | 5,490,000.00 USD | 22,910.00 USD | 26,360.00 USD | 29,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 10,070,000.00 USD | 10,070,000.00 USD | 261,490.00 USD | 19,920.00 USD | 93,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 5,530,000.00 USD | 5,530,000.00 USD | 36,100.00 USD | 5,930.00 USD | 180.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 10,320,000.00 USD | 10,320,000.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 872.20 USD | 6,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 5,610,000.00 USD | 5,610,000.00 USD | 51,100.00 USD | 18,930.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 10,580,000.00 USD | 10,580,000.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 5,720,000.00 USD | 5,720,000.00 USD | 62,640.00 USD | 17,310.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 11,050,000.00 USD | 11,050,000.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 5,820,000.00 USD | 5,820,000.00 USD | 53,480.00 USD | 19,840.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 11,390,000.00 USD | 11,390,000.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 5,820,000.00 USD | 5,820,000.00 USD | 391.20 USD | 927.78 USD | 103.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 11,580,000.00 USD | 11,580,000.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 5,850,000.00 USD | 5,850,000.00 USD | 14,920.00 USD | 3,460.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 11,810,000.00 USD | 11,810,000.00 USD | 140,600.00 USD | 75,950.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 941.07 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 5,870,000.00 USD | 5,870,000.00 USD | 11,940.00 USD | 3,340.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 11,920,000.00 USD | 11,920,000.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 5,890,000.00 USD | 5,890,000.00 USD | 18,720.00 USD | 0.00 USD | 29.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 12,070,000.00 USD | 12,070,000.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 5,900,000.00 USD | 5,900,000.00 USD | 3,400.00 USD | 11,690.00 USD | 44.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 12,540,000.00 USD | 12,540,000.00 USD | 176,820.00 USD | 40,380.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 5,900,000.00 USD | 5,900,000.00 USD | 359.83 USD | 0.00 USD | 20.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 13,120,000.00 USD | 13,120,000.00 USD | 135,510.00 USD | 33,450.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 5,900,000.00 USD | 5,900,000.00 USD | 2,060.00 USD | 29.65 USD | 360.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 13,620,000.00 USD | 13,620,000.00 USD | 159,890.00 USD | 70,960.00 USD | 272,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 6,490.00 USD | 13,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 5,930,000.00 USD | 5,930,000.00 USD | 4,980.00 USD | 8,910.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 13,870,000.00 USD | 13,870,000.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 5,940,000.00 USD | 5,940,000.00 USD | 1,650.00 USD | 0.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 14,110,000.00 USD | 14,110,000.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 5,950,000.00 USD | 5,950,000.00 USD | 1,320.00 USD | 4,320.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 14,360,000.00 USD | 14,360,000.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 5,990,000.00 USD | 5,990,000.00 USD | 20,270.00 USD | 5,020.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 14,700,000.00 USD | 14,700,000.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 6,010,000.00 USD | 6,010,000.00 USD | 14,590.00 USD | 2,830.00 USD | 92.11 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 14,960,000.00 USD | 14,960,000.00 USD | 96,800.00 USD | 59,960.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 193.27 USD | 14,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.56` | 6,050,000.00 USD | 6,050,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 15,150,000.00 USD | 15,150,000.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 6,070,000.00 USD | 6,070,000.00 USD | 4,160.00 USD | 1,030.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 15,350,000.00 USD | 15,350,000.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 6,070,000.00 USD | 6,070,000.00 USD | 3,410.00 USD | 1,310.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 15,470,000.00 USD | 15,470,000.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 6,110,000.00 USD | 6,110,000.00 USD | 12,890.00 USD | 9,540.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 15,540,000.00 USD | 15,540,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 6,160,000.00 USD | 6,160,000.00 USD | 24,070.00 USD | 10,540.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 15,840,000.00 USD | 15,840,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 4,380.00 USD | 18,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 6,170,000.00 USD | 6,170,000.00 USD | 845.26 USD | 888.70 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 15,990,000.00 USD | 15,990,000.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 6,210,000.00 USD | 6,210,000.00 USD | 15,690.00 USD | 5,120.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 16,290,000.00 USD | 16,290,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 6,250,000.00 USD | 6,250,000.00 USD | 5,910.00 USD | 5,550.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 16,500,000.00 USD | 16,500,000.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 6,340,000.00 USD | 6,340,000.00 USD | 52,250.00 USD | 9,620.00 USD | 29,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 16,690,000.00 USD | 16,690,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 6,400,000.00 USD | 6,400,000.00 USD | 26,930.00 USD | 12,730.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 16,760,000.00 USD | 16,760,000.00 USD | 38,570.00 USD | 18,330.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 6,470,000.00 USD | 6,470,000.00 USD | 43,450.00 USD | 12,260.00 USD | 18,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 16,820,000.00 USD | 16,820,000.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 6,500,000.00 USD | 6,500,000.00 USD | 19,150.00 USD | 3,120.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 16,930,000.00 USD | 16,930,000.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 6,530,000.00 USD | 6,530,000.00 USD | 12,430.00 USD | 5,860.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 16,980,000.00 USD | 16,980,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 6,530,000.00 USD | 6,530,000.00 USD | 84.60 USD | 1,230.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 17,000,000.00 USD | 17,000,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 6,550,000.00 USD | 6,550,000.00 USD | 14,360.00 USD | 3,530.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 17,060,000.00 USD | 17,060,000.00 USD | 29,710.00 USD | 15,870.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 6,580,000.00 USD | 6,580,000.00 USD | 19,070.00 USD | 1,990.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 17,100,000.00 USD | 17,100,000.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 6,600,000.00 USD | 6,600,000.00 USD | 7,490.00 USD | 3,610.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 17,140,000.00 USD | 17,140,000.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 17,210,000.00 USD | 17,210,000.00 USD | 41,140.00 USD | 16,610.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 18,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 18,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.35` | 431.20 USD | 19,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,480.00 USD | 24,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 26,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 781.14 USD | 27,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 1,190.00 USD | 28,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 37,670.00 USD | 66,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 604.20 USD | 66,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 359.38 USD | 67,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 147,690.00 USD | 215,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.85` | 15,710.00 USD | 231,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.05` | 23,160.00 USD | 254,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 10,450.00 USD | 264,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 5,640.00 USD | 270,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 23,990.00 USD | 294,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,690.00 USD | 351,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 301.45 USD | 351,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 62,900.00 USD | 414,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 1,280.00 USD | 415,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 104.64 USD | 415,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 471.80 USD | 416,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 81,410.00 USD | 497,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 498,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 241.50 USD | 499,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 594,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 245,140.00 USD | 839,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 839,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 840,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 842,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 2,090,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 151.88 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 883.79 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.25` | 763,630.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 71,570.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 870.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 331,570.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.15` | 1,710.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.85` | 431,590.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.05` | 3,070.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.15` | 1,620.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.25` | 101,460.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.65` | 13,870,000.00 USD | 0.00 USD | 4,740.00 USD | `-77.65%` | `1,787,700.00` |
| `Live` | `Long` | `2.75` | 13,870,000.00 USD | 0.00 USD | 7,110.00 USD | `-76.80%` | `2,585,200.00` |
| `Live` | `Long` | `3.05` | 13,860,000.00 USD | 0.00 USD | 13,490.00 USD | `-74.27%` | `4,423,300.00` |
| `Live` | `Long` | `3.15` | 13,850,000.00 USD | 0.00 USD | 927.99 USD | `-73.43%` | `294,600.00` |
| `Live` | `Long` | `3.35` | 13,840,000.00 USD | 0.00 USD | 3,290.00 USD | `-71.74%` | `982,000.00` |
| `Live` | `Long` | `3.45` | 13,840,000.00 USD | 0.00 USD | 14,850.00 USD | `-70.90%` | `4,305,200.00` |
| `Live` | `Long` | `3.55` | 13,830,000.00 USD | 0.00 USD | 355.00 USD | `-70.05%` | `100,000.00` |
| `Live` | `Long` | `3.65` | 13,830,000.00 USD | 0.00 USD | 83,460.00 USD | `-69.21%` | `22,865,900.00` |
| `Live` | `Long` | `3.75` | 13,740,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.37%` | `1,505,100.00` |
| `Live` | `Long` | `3.95` | 13,740,000.00 USD | 0.00 USD | 5,770.00 USD | `-66.68%` | `1,460,300.00` |
| `Live` | `Long` | `4.05` | 13,730,000.00 USD | 0.00 USD | 950.54 USD | `-65.84%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 13,730,000.00 USD | 0.00 USD | 101.26 USD | `-64.99%` | `24,400.00` |
| `Live` | `Long` | `4.25` | 13,730,000.00 USD | 0.00 USD | 5,090.00 USD | `-64.15%` | `1,198,100.00` |
| `Live` | `Long` | `4.45` | 13,730,000.00 USD | 0.00 USD | 220,660.00 USD | `-62.46%` | `49,585,700.00` |
| `Live` | `Long` | `4.55` | 13,500,000.00 USD | 0.00 USD | 46,260.00 USD | `-61.62%` | `10,167,900.00` |
| `Live` | `Long` | `4.65` | 13,460,000.00 USD | 0.00 USD | 383.63 USD | `-60.78%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,460,000.00 USD | 0.00 USD | 418.95 USD | `-59.93%` | `88,200.00` |
| `Live` | `Long` | `4.85` | 13,460,000.00 USD | 0.00 USD | 1,200.00 USD | `-59.09%` | `247,100.00` |
| `Live` | `Long` | `4.95` | 13,460,000.00 USD | 0.00 USD | 17,120.00 USD | `-58.25%` | `3,458,900.00` |
| `Live` | `Long` | `5.05` | 13,440,000.00 USD | 0.00 USD | 40,010.00 USD | `-57.40%` | `7,923,200.00` |
| `Live` | `Long` | `5.15` | 13,400,000.00 USD | 0.00 USD | 9,450.00 USD | `-56.56%` | `1,834,400.00` |
| `Live` | `Long` | `5.25` | 13,390,000.00 USD | 0.00 USD | 90,620.00 USD | `-55.71%` | `17,260,600.00` |
| `Live` | `Long` | `5.35` | 13,300,000.00 USD | 0.00 USD | 546,570.00 USD | `-54.87%` | `102,162,000.00` |
| `Live` | `Long` | `5.45` | 12,750,000.00 USD | 0.00 USD | 243.62 USD | `-54.03%` | `44,700.00` |
| `Live` | `Long` | `5.55` | 12,750,000.00 USD | 0.00 USD | 748.14 USD | `-53.18%` | `134,800.00` |
| `Live` | `Long` | `5.65` | 12,750,000.00 USD | 0.00 USD | 35,600.00 USD | `-52.34%` | `6,300,800.00` |
| `Live` | `Long` | `5.75` | 12,720,000.00 USD | 0.00 USD | 290.38 USD | `-51.50%` | `50,500.00` |
| `Live` | `Long` | `5.85` | 12,720,000.00 USD | 0.00 USD | 19,570.00 USD | `-50.65%` | `3,346,100.00` |
| `Live` | `Long` | `5.95` | 12,700,000.00 USD | 0.00 USD | 120,390.00 USD | `-49.81%` | `20,234,300.00` |
| `Live` | `Long` | `6.05` | 12,580,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.97%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,510,000.00 USD | 0.00 USD | 12,060.00 USD | `-48.12%` | `1,961,500.00` |
| `Live` | `Long` | `6.25` | 12,500,000.00 USD | 0.00 USD | 42,180.00 USD | `-47.28%` | `6,748,700.00` |
| `Live` | `Long` | `6.35` | 12,460,000.00 USD | 0.00 USD | 16,590.00 USD | `-46.44%` | `2,612,900.00` |
| `Live` | `Long` | `6.45` | 12,440,000.00 USD | 0.00 USD | 101,560.00 USD | `-45.59%` | `15,746,100.00` |
| `Live` | `Long` | `6.55` | 12,340,000.00 USD | 0.00 USD | 3,830.00 USD | `-44.75%` | `584,300.00` |
| `Live` | `Long` | `6.65` | 12,340,000.00 USD | 0.00 USD | 9,920.00 USD | `-43.91%` | `1,492,100.00` |
| `Live` | `Long` | `6.75` | 12,330,000.00 USD | 0.00 USD | 4,130.00 USD | `-43.06%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,320,000.00 USD | 0.00 USD | 9,270.00 USD | `-42.22%` | `1,353,600.00` |
| `Live` | `Long` | `6.95` | 12,310,000.00 USD | 0.00 USD | 43,330.00 USD | `-41.37%` | `6,234,100.00` |
| `Live` | `Long` | `7.05` | 12,270,000.00 USD | 0.00 USD | 3,190.00 USD | `-40.53%` | `452,900.00` |
| `Live` | `Long` | `7.15` | 12,270,000.00 USD | 0.00 USD | 687,620.00 USD | `-39.69%` | `96,170,300.00` |
| `Live` | `Long` | `7.25` | 11,580,000.00 USD | 0.00 USD | 8,460.00 USD | `-38.84%` | `1,167,100.00` |
| `Live` | `Long` | `7.35` | 11,570,000.00 USD | 0.00 USD | 31,820.00 USD | `-38.00%` | `4,329,400.00` |
| `Live` | `Long` | `7.45` | 11,540,000.00 USD | 0.00 USD | 4,710.00 USD | `-37.16%` | `631,800.00` |
| `Live` | `Long` | `7.55` | 11,530,000.00 USD | 0.00 USD | 16,920.00 USD | `-36.31%` | `2,240,400.00` |
| `Live` | `Long` | `7.65` | 11,520,000.00 USD | 0.00 USD | 9,820.00 USD | `-35.47%` | `1,283,200.00` |
| `Live` | `Long` | `7.75` | 11,510,000.00 USD | 0.00 USD | 2,770.00 USD | `-34.63%` | `357,400.00` |
| `Live` | `Long` | `7.85` | 11,500,000.00 USD | 0.00 USD | 1,090.00 USD | `-33.78%` | `139,400.00` |
| `Live` | `Long` | `7.95` | 11,500,000.00 USD | 0.00 USD | 15,130.00 USD | `-32.94%` | `1,903,400.00` |
| `Live` | `Long` | `8.05` | 11,490,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-32.10%` | `172,528,800.00` |
| `Live` | `Long` | `8.15` | 10,100,000.00 USD | 0.00 USD | 16,750.00 USD | `-31.25%` | `2,055,800.00` |
| `Live` | `Long` | `8.25` | 10,080,000.00 USD | 0.00 USD | 90,750.00 USD | `-30.41%` | `11,000,200.00` |
| `Live` | `Long` | `8.35` | 9,990,000.00 USD | 0.00 USD | 7,840.00 USD | `-29.57%` | `939,000.00` |
| `Live` | `Long` | `8.45` | 9,980,000.00 USD | 0.00 USD | 11,180.00 USD | `-28.72%` | `1,322,500.00` |
| `Live` | `Long` | `8.55` | 9,970,000.00 USD | 0.00 USD | 16,760.00 USD | `-27.88%` | `1,960,800.00` |
| `Live` | `Long` | `8.65` | 9,960,000.00 USD | 0.00 USD | 11,540.00 USD | `-27.04%` | `1,333,800.00` |
| `Live` | `Long` | `8.75` | 9,950,000.00 USD | 0.00 USD | 331,990.00 USD | `-26.19%` | `37,941,400.00` |
| `Live` | `Long` | `8.85` | 9,610,000.00 USD | 0.00 USD | 28,050.00 USD | `-25.35%` | `3,169,300.00` |
| `Live` | `Long` | `8.95` | 9,590,000.00 USD | 0.00 USD | 486,640.00 USD | `-24.50%` | `54,373,700.00` |
| `Live` | `Long` | `9.05` | 9,100,000.00 USD | 0.00 USD | 23,010.00 USD | `-23.66%` | `2,542,900.00` |
| `Live` | `Long` | `9.15` | 9,080,000.00 USD | 0.00 USD | 3,750,000.00 USD | `-22.82%` | `410,204,100.00` |
| `Live` | `Long` | `9.25` | 5,320,000.00 USD | 0.00 USD | 1,620.00 USD | `-21.97%` | `175,400.00` |
| `Live` | `Long` | `9.35` | 5,320,000.00 USD | 0.00 USD | 2,200,000.00 USD | `-21.13%` | `235,141,400.00` |
| `Live` | `Long` | `9.45` | 3,120,000.00 USD | 0.00 USD | 28,660.00 USD | `-20.29%` | `3,033,200.00` |
| `Live` | `Long` | `9.55` | 3,090,000.00 USD | 0.00 USD | 40,810.00 USD | `-19.44%` | `4,272,800.00` |
| `Live` | `Long` | `9.65` | 3,050,000.00 USD | 0.00 USD | 11,030.00 USD | `-18.60%` | `1,142,500.00` |
| `Live` | `Long` | `9.75` | 3,040,000.00 USD | 0.00 USD | 54,080.00 USD | `-17.76%` | `5,546,900.00` |
| `Live` | `Long` | `9.85` | 2,990,000.00 USD | 0.00 USD | 243,780.00 USD | `-16.91%` | `24,749,500.00` |
| `Live` | `Long` | `9.95` | 2,740,000.00 USD | 0.00 USD | 778,350.00 USD | `-16.07%` | `78,225,900.00` |
| `Live` | `Long` | `10.05` | 1,970,000.00 USD | 0.00 USD | 647,220.00 USD | `-15.23%` | `64,399,600.00` |
| `Live` | `Long` | `10.15` | 1,320,000.00 USD | 0.00 USD | 171,050.00 USD | `-14.38%` | `16,852,500.00` |
| `Live` | `Long` | `10.25` | 1,150,000.00 USD | 0.00 USD | 33,280.00 USD | `-13.54%` | `3,247,200.00` |
| `Live` | `Long` | `10.35` | 1,110,000.00 USD | 0.00 USD | 14,120.00 USD | `-12.70%` | `1,364,000.00` |
| `Live` | `Long` | `10.45` | 1,100,000.00 USD | 0.00 USD | 14,500.00 USD | `-11.85%` | `1,387,200.00` |
| `Live` | `Long` | `10.55` | 1,080,000.00 USD | 0.00 USD | 40,960.00 USD | `-11.01%` | `3,882,000.00` |
| `Live` | `Long` | `10.65` | 1,040,000.00 USD | 0.00 USD | 44,080.00 USD | `-10.16%` | `4,138,800.00` |
| `Live` | `Long` | `10.75` | 999,890.00 USD | 0.00 USD | 214,040.00 USD | `-9.32%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 785,850.00 USD | 0.00 USD | 81,870.00 USD | `-8.48%` | `7,545,900.00` |
| `Live` | `Long` | `10.95` | 703,980.00 USD | 0.00 USD | 558,090.00 USD | `-7.63%` | `50,966,800.00` |
| `Live` | `Long` | `11.05` | 145,890.00 USD | 0.00 USD | 23,500.00 USD | `-6.79%` | `2,126,400.00` |
| `Live` | `Long` | `11.15` | 122,400.00 USD | 0.00 USD | 49,590.00 USD | `-5.95%` | `4,447,400.00` |
| `Live` | `Long` | `11.25` | 72,810.00 USD | 0.00 USD | 21,540.00 USD | `-5.10%` | `1,914,900.00` |
| `Live` | `Long` | `11.35` | 51,260.00 USD | 0.00 USD | 46,360.00 USD | `-4.26%` | `4,084,400.00` |
| `Live` | `Long` | `11.65` | 4,910.00 USD | 0.00 USD | 4,910.00 USD | `-1.73%` | `421,200.00` |
| `Live` | `Short` | `11.95` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | `+0.80%` | `150,000.00` |
| `Live` | `Short` | `12.05` | 4,390.00 USD | 2,600.00 USD | 0.00 USD | `+1.64%` | `215,800.00` |
| `Live` | `Short` | `12.15` | 5,520.00 USD | 1,130.00 USD | 0.00 USD | `+2.49%` | `93,000.00` |
| `Live` | `Short` | `12.25` | 6,400.00 USD | 872.20 USD | 0.00 USD | `+3.33%` | `71,200.00` |
| `Live` | `Short` | `12.35` | 7,340.00 USD | 941.07 USD | 0.00 USD | `+4.18%` | `76,200.00` |
| `Live` | `Short` | `12.45` | 13,830.00 USD | 6,490.00 USD | 0.00 USD | `+5.02%` | `521,400.00` |
| `Live` | `Short` | `12.55` | 14,020.00 USD | 193.27 USD | 0.00 USD | `+5.86%` | `15,400.00` |
| `Live` | `Short` | `12.65` | 18,400.00 USD | 4,380.00 USD | 0.00 USD | `+6.71%` | `346,000.00` |
| `Live` | `Short` | `12.85` | 18,540.00 USD | 138.78 USD | 0.00 USD | `+8.39%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 18,650.00 USD | 113.53 USD | 0.00 USD | `+10.08%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 18,920.00 USD | 274.84 USD | 0.00 USD | `+10.92%` | `20,900.00` |
| `Live` | `Short` | `13.35` | 19,360.00 USD | 431.20 USD | 0.00 USD | `+12.61%` | `32,300.00` |
| `Live` | `Short` | `13.45` | 24,830.00 USD | 5,480.00 USD | 0.00 USD | `+13.45%` | `407,200.00` |
| `Live` | `Short` | `13.55` | 26,600.00 USD | 1,760.00 USD | 0.00 USD | `+14.30%` | `130,100.00` |
| `Live` | `Short` | `13.85` | 27,380.00 USD | 781.14 USD | 0.00 USD | `+16.83%` | `56,400.00` |
| `Live` | `Short` | `14.05` | 28,560.00 USD | 1,190.00 USD | 0.00 USD | `+18.52%` | `84,500.00` |
| `Live` | `Short` | `14.15` | 66,230.00 USD | 37,670.00 USD | 0.00 USD | `+19.36%` | `2,661,900.00` |
| `Live` | `Short` | `14.25` | 66,830.00 USD | 604.20 USD | 0.00 USD | `+20.20%` | `42,400.00` |
| `Live` | `Short` | `14.45` | 67,380.00 USD | 541.88 USD | 0.00 USD | `+21.89%` | `37,500.00` |
| `Live` | `Short` | `14.55` | 67,740.00 USD | 359.38 USD | 0.00 USD | `+22.73%` | `24,700.00` |
| `Live` | `Short` | `14.75` | 215,420.00 USD | 147,690.00 USD | 0.00 USD | `+24.42%` | `10,012,800.00` |
| `Live` | `Short` | `14.85` | 231,140.00 USD | 15,710.00 USD | 0.00 USD | `+25.26%` | `1,058,000.00` |
| `Live` | `Short` | `15.05` | 254,300.00 USD | 23,160.00 USD | 0.00 USD | `+26.95%` | `1,539,000.00` |
| `Live` | `Short` | `15.35` | 264,750.00 USD | 10,450.00 USD | 0.00 USD | `+29.48%` | `680,700.00` |
| `Live` | `Short` | `15.55` | 270,390.00 USD | 5,640.00 USD | 0.00 USD | `+31.17%` | `362,900.00` |
| `Live` | `Short` | `15.75` | 294,380.00 USD | 23,990.00 USD | 0.00 USD | `+32.86%` | `1,523,000.00` |
| `Live` | `Short` | `15.85` | 351,070.00 USD | 56,690.00 USD | 0.00 USD | `+33.70%` | `3,576,700.00` |
| `Live` | `Short` | `15.95` | 351,370.00 USD | 301.45 USD | 0.00 USD | `+34.54%` | `18,900.00` |
| `Live` | `Short` | `16.15` | 414,270.00 USD | 62,900.00 USD | 0.00 USD | `+36.23%` | `3,895,000.00` |
| `Live` | `Short` | `16.25` | 415,560.00 USD | 1,280.00 USD | 0.00 USD | `+37.07%` | `78,900.00` |
| `Live` | `Short` | `16.35` | 415,660.00 USD | 104.64 USD | 0.00 USD | `+37.92%` | `6,400.00` |
| `Live` | `Short` | `16.85` | 416,130.00 USD | 471.80 USD | 0.00 USD | `+42.13%` | `28,000.00` |
| `Live` | `Short` | `16.95` | 497,550.00 USD | 81,410.00 USD | 0.00 USD | `+42.98%` | `4,803,200.00` |
| `Live` | `Short` | `17.15` | 498,910.00 USD | 1,370.00 USD | 0.00 USD | `+44.66%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 499,150.00 USD | 241.50 USD | 0.00 USD | `+45.51%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 594,170.00 USD | 95,020.00 USD | 0.00 USD | `+47.20%` | `5,445,000.00` |
| `Live` | `Short` | `17.55` | 839,310.00 USD | 245,140.00 USD | 0.00 USD | `+48.04%` | `13,968,000.00` |
| `Live` | `Short` | `17.85` | 839,560.00 USD | 249.90 USD | 0.00 USD | `+50.57%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 840,180.00 USD | 621.07 USD | 0.00 USD | `+51.41%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 842,150.00 USD | 1,970.00 USD | 0.00 USD | `+52.26%` | `109,300.00` |
| `Live` | `Short` | `18.15` | 2,930,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+53.10%` | `115,024,600.00` |
| `Live` | `Short` | `18.45` | 2,930,000.00 USD | 3,890.00 USD | 0.00 USD | `+55.63%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 2,930,000.00 USD | 185.50 USD | 0.00 USD | `+56.47%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,930,000.00 USD | 186.50 USD | 0.00 USD | `+57.32%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 2,930,000.00 USD | 151.88 USD | 0.00 USD | `+58.16%` | `8,100.00` |
| `Live` | `Short` | `18.85` | 2,930,000.00 USD | 456.17 USD | 0.00 USD | `+59.00%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,950,000.00 USD | 16,250.00 USD | 0.00 USD | `+59.85%` | `857,700.00` |
| `Live` | `Short` | `19.65` | 2,990,000.00 USD | 38,790.00 USD | 0.00 USD | `+65.75%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,990,000.00 USD | 883.79 USD | 0.00 USD | `+68.28%` | `44,300.00` |
| `Live` | `Short` | `20.25` | 3,750,000.00 USD | 763,630.00 USD | 0.00 USD | `+70.81%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,760,000.00 USD | 7,250.00 USD | 0.00 USD | `+73.34%` | `353,000.00` |
| `Live` | `Short` | `21.05` | 3,830,000.00 USD | 71,570.00 USD | 0.00 USD | `+77.56%` | `3,400,000.00` |
| `Live` | `Short` | `21.75` | 3,830,000.00 USD | 870.00 USD | 0.00 USD | `+83.47%` | `40,000.00` |
| `Live` | `Short` | `21.85` | 4,170,000.00 USD | 331,570.00 USD | 0.00 USD | `+84.31%` | `15,175,000.00` |
| `Live` | `Short` | `22.15` | 4,170,000.00 USD | 1,710.00 USD | 0.00 USD | `+86.84%` | `77,300.00` |
| `Live` | `Short` | `22.85` | 4,600,000.00 USD | 431,590.00 USD | 0.00 USD | `+92.75%` | `18,888,000.00` |
| `Live` | `Short` | `23.05` | 4,600,000.00 USD | 3,070.00 USD | 0.00 USD | `+94.43%` | `133,300.00` |
| `Live` | `Short` | `23.15` | 4,600,000.00 USD | 1,620.00 USD | 0.00 USD | `+95.28%` | `69,800.00` |
| `Live` | `Short` | `23.25` | 4,700,000.00 USD | 101,460.00 USD | 0.00 USD | `+96.12%` | `4,364,000.00` |
| `Live` | `Short` | `23.35` | 4,710,000.00 USD | 238.17 USD | 0.00 USD | `+96.96%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 1,040,000.00 USD | 0.00 USD | 431.68 USD | `-70.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 1,040,000.00 USD | 0.00 USD | 290.29 USD | `-61.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 1,040,000.00 USD | 0.00 USD | 120.22 USD | `-55.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 1,040,000.00 USD | 0.00 USD | 107.09 USD | `-48.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 1,040,000.00 USD | 0.00 USD | 3,760.00 USD | `-44.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 1,040,000.00 USD | 0.00 USD | 133.00 USD | `-43.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 1,040,000.00 USD | 0.00 USD | 3,770.00 USD | `-40.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-38.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 1,030,000.00 USD | 0.00 USD | 3,740.00 USD | `-37.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 1,030,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 1,020,000.00 USD | 0.00 USD | 146.80 USD | `-33.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 1,020,000.00 USD | 0.00 USD | 5,000.00 USD | `-32.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 1,020,000.00 USD | 0.00 USD | 393.64 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 1,020,000.00 USD | 0.00 USD | 10,660.00 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 1,010,000.00 USD | 0.00 USD | 1,360.00 USD | `-28.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 1,010,000.00 USD | 0.00 USD | 30,250.00 USD | `-27.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 977,020.00 USD | 0.00 USD | 186.84 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 976,830.00 USD | 0.00 USD | 742.88 USD | `-26.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 976,090.00 USD | 0.00 USD | 180.54 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 975,900.00 USD | 0.00 USD | 1,320.00 USD | `-24.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 974,590.00 USD | 0.00 USD | 2,440.00 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 972,140.00 USD | 0.00 USD | 194.90 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 971,950.00 USD | 0.00 USD | 4,940.00 USD | `-21.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 967,000.00 USD | 0.00 USD | 9,870.00 USD | `-19.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 957,140.00 USD | 0.00 USD | 3,550.00 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 953,590.00 USD | 0.00 USD | 25,950.00 USD | `-17.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 927,640.00 USD | 0.00 USD | 19,100.00 USD | `-16.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 908,540.00 USD | 0.00 USD | 299,650.00 USD | `-16.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 608,880.00 USD | 0.00 USD | 2,590.00 USD | `-15.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 606,290.00 USD | 0.00 USD | 1,050.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 605,240.00 USD | 0.00 USD | 2,820.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 602,420.00 USD | 0.00 USD | 2,000.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 600,430.00 USD | 0.00 USD | 19,450.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 580,980.00 USD | 0.00 USD | 5,160.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 575,810.00 USD | 0.00 USD | 4,590.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 571,220.00 USD | 0.00 USD | 5,470.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 565,740.00 USD | 0.00 USD | 4,370.00 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 561,380.00 USD | 0.00 USD | 6,510.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 554,870.00 USD | 0.00 USD | 16,530.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 538,330.00 USD | 0.00 USD | 24,830.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 513,500.00 USD | 0.00 USD | 46,190.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 467,310.00 USD | 0.00 USD | 14,120.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 453,190.00 USD | 0.00 USD | 19,680.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 433,510.00 USD | 0.00 USD | 7,530.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 425,980.00 USD | 0.00 USD | 410,470.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.75` | 15,500.00 USD | 0.00 USD | 15,120.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.85` | 382.75 USD | 0.00 USD | 382.75 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 156.55 USD | 156.55 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 39,410.00 USD | 39,260.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 73,910.00 USD | 34,500.00 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 84,740.00 USD | 10,830.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 86,080.00 USD | 1,340.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 86,390.00 USD | 307.52 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 97,500.00 USD | 11,110.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 154,030.00 USD | 56,530.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 195,500.00 USD | 41,470.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 216,230.00 USD | 20,730.00 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 217,020.00 USD | 784.77 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 223,520.00 USD | 6,500.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 224,560.00 USD | 1,050.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 228,410.00 USD | 3,840.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 233,400.00 USD | 4,990.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 247,920.00 USD | 14,520.00 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 250,550.00 USD | 2,630.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 252,570.00 USD | 2,020.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 254,630.00 USD | 2,060.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 254,750.00 USD | 120.50 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 255,020.00 USD | 266.44 USD | 0.00 USD | `+17.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 272,130.00 USD | 17,110.00 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 273,190.00 USD | 1,060.00 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 280,180.00 USD | 6,990.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 280,400.00 USD | 218.25 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 283,010.00 USD | 2,610.00 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 295,940.00 USD | 12,920.00 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 296,890.00 USD | 950.82 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 308,110.00 USD | 11,220.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 309,940.00 USD | 1,830.00 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 542,980.00 USD | 233,040.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 556,480.00 USD | 13,500.00 USD | 0.00 USD | `+29.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 557,370.00 USD | 893.01 USD | 0.00 USD | `+30.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 557,760.00 USD | 388.75 USD | 0.00 USD | `+31.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 583,860.00 USD | 26,100.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 585,970.00 USD | 2,110.00 USD | 0.00 USD | `+32.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 591,310.00 USD | 5,340.00 USD | 0.00 USD | `+33.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 596,620.00 USD | 5,320.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 605,790.00 USD | 9,170.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 612,600.00 USD | 6,800.00 USD | 0.00 USD | `+36.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 631,360.00 USD | 18,760.00 USD | 0.00 USD | `+37.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 637,900.00 USD | 6,540.00 USD | 0.00 USD | `+37.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 644,480.00 USD | 6,580.00 USD | 0.00 USD | `+38.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 654,410.00 USD | 9,930.00 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 667,730.00 USD | 13,320.00 USD | 0.00 USD | `+40.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 681,970.00 USD | 14,240.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 766,320.00 USD | 84,360.00 USD | 0.00 USD | `+42.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 768,020.00 USD | 1,700.00 USD | 0.00 USD | `+42.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 777,520.00 USD | 9,510.00 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 779,240.00 USD | 1,710.00 USD | 0.00 USD | `+44.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 781,490.00 USD | 2,250.00 USD | 0.00 USD | `+45.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 879,820.00 USD | 98,330.00 USD | 0.00 USD | `+46.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 901,490.00 USD | 21,670.00 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 907,920.00 USD | 6,430.00 USD | 0.00 USD | `+48.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 912,330.00 USD | 4,410.00 USD | 0.00 USD | `+48.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 916,770.00 USD | 4,440.00 USD | 0.00 USD | `+49.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 921,230.00 USD | 4,460.00 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 921,680.00 USD | 448.75 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 957,270.00 USD | 35,590.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 957,720.00 USD | 453.75 USD | 0.00 USD | `+53.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 958,550.00 USD | 830.38 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 959,010.00 USD | 458.75 USD | 0.00 USD | `+54.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 959,470.00 USD | 461.25 USD | 0.00 USD | `+55.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 964,020.00 USD | 4,540.00 USD | 0.00 USD | `+56.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 964,480.00 USD | 466.25 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 964,950.00 USD | 468.75 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 965,420.00 USD | 471.25 USD | 0.00 USD | `+59.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 965,900.00 USD | 473.75 USD | 0.00 USD | `+59.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,030,000.00 USD | 67,000.00 USD | 0.00 USD | `+60.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,030,000.00 USD | 574.50 USD | 0.00 USD | `+61.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,030,000.00 USD | 577.50 USD | 0.00 USD | `+62.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,040,000.00 USD | 2,710.00 USD | 0.00 USD | `+63.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,040,000.00 USD | 972.50 USD | 0.00 USD | `+64.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,050,000.00 USD | 7,680.00 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,050,000.00 USD | 1,680.00 USD | 0.00 USD | `+65.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,050,000.00 USD | 1,690.00 USD | 0.00 USD | `+66.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,050,000.00 USD | 992.50 USD | 0.00 USD | `+67.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,050,000.00 USD | 5,170.00 USD | 0.00 USD | `+68.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,670,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+69.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+70.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+71.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+72.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,670,000.00 USD | 1,030.00 USD | 0.00 USD | `+73.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,680,000.00 USD | 1,030.00 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,680,000.00 USD | 1,860.00 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,680,000.00 USD | 1,410.00 USD | 0.00 USD | `+75.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,680,000.00 USD | 1,050.00 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,680,000.00 USD | 4,000.00 USD | 0.00 USD | `+77.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,680,000.00 USD | 1,060.00 USD | 0.00 USD | `+78.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,690,000.00 USD | 1,060.00 USD | 0.00 USD | `+79.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,730,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+80.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,730,000.00 USD | 1,070.00 USD | 0.00 USD | `+80.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+81.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,740,000.00 USD | 1,080.00 USD | 0.00 USD | `+82.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,740,000.00 USD | 1,090.00 USD | 0.00 USD | `+83.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,740,000.00 USD | 3,280.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+85.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+86.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+86.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+87.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,750,000.00 USD | 1,120.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,750,000.00 USD | 1,120.00 USD | 0.00 USD | `+89.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+90.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+91.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+91.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+92.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,750,000.00 USD | 1,150.00 USD | 0.00 USD | `+93.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,880,000.00 USD | 129,920.00 USD | 0.00 USD | `+94.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,880,000.00 USD | 1,160.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,890,000.00 USD | 1,160.00 USD | 0.00 USD | `+96.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,890,000.00 USD | 1,170.00 USD | 0.00 USD | `+96.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.45` | 3,890,000.00 USD | 1,170.00 USD | 0.00 USD | `+97.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.55` | 3,900,000.00 USD | 9,490.00 USD | 0.00 USD | `+98.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.65` | 3,900,000.00 USD | 1,180.00 USD | 0.00 USD | `+99.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.75` | 3,900,000.00 USD | 3,560.00 USD | 0.00 USD | `+100.34%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 35,120.00 USD | 15,990.00 USD | 74,890.00 USD |
| `7D` | `10.22` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 101,890.00 USD | 28,560.00 USD | 86,110.00 USD |
| `7D` | `10.24` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,760.00 USD |
| `7D` | `10.26` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD |
| `7D` | `10.28` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD |
| `7D` | `10.30` | 18,970,000.00 USD | 0.00 USD | 18,970,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD |
| `7D` | `10.32` | 18,870,000.00 USD | 0.00 USD | 18,870,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `7D` | `10.34` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD |
| `7D` | `10.36` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD |
| `7D` | `10.38` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD |
| `7D` | `10.40` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,850.00 USD |
| `7D` | `10.42` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD |
| `7D` | `10.44` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,560.00 USD |
| `7D` | `10.46` | 18,230,000.00 USD | 0.00 USD | 18,230,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD |
| `7D` | `10.48` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD |
| `7D` | `10.50` | 18,060,000.00 USD | 0.00 USD | 18,060,000.00 USD | 42,030.00 USD | 16,000.00 USD | 12,670.00 USD |
| `7D` | `10.52` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD |
| `7D` | `10.54` | 17,950,000.00 USD | 0.00 USD | 17,950,000.00 USD | 25,600.00 USD | 72.80 USD | 12,910.00 USD |
| `7D` | `10.56` | 17,910,000.00 USD | 0.00 USD | 17,910,000.00 USD | 51,230.00 USD | 16,690.00 USD | 12,830.00 USD |
| `7D` | `10.58` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 84,220.00 USD | 6,710.00 USD | 11,250.00 USD |
| `7D` | `10.60` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD |
| `7D` | `10.62` | 17,680,000.00 USD | 0.00 USD | 17,680,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD |
| `1D` | `10.63` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 40,420.00 USD | 11,120.00 USD | 12,320.00 USD |
| `7D` | `10.64` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.65` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 18,690.00 USD | 6,860.00 USD | 10,380.00 USD |
| `7D` | `10.66` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.67` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 442.43 USD | 1,480.00 USD | 10.09 USD |
| `7D` | `10.68` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.69` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 15,240.00 USD | 3,650.00 USD | 1,550.00 USD |
| `7D` | `10.70` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.71` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 3,410.00 USD | 1,570.00 USD | 3,730.00 USD |
| `7D` | `10.72` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 21,070.00 USD | 4,880.00 USD | 264.88 USD |
| `1D` | `10.73` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 7,000.00 USD | 7,680.00 USD | 6,980.00 USD |
| `7D` | `10.74` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 25,580.00 USD | 3,690.00 USD | 315.57 USD |
| `1D` | `10.75` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 20,270.00 USD | 4,650.00 USD | 3,870.00 USD |
| `7D` | `10.76` | 17,480,000.00 USD | 0.00 USD | 17,480,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD |
| `1D` | `10.77` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,310.00 USD | 6,420.00 USD | 5,600.00 USD |
| `7D` | `10.78` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD |
| `1D` | `10.79` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 3,200.00 USD | 2,540.00 USD | 93.45 USD |
| `7D` | `10.80` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,260.00 USD |
| `1D` | `10.81` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 1,970.00 USD | 0.00 USD | 64.40 USD |
| `7D` | `10.82` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD |
| `1D` | `10.83` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 3,650.00 USD | 160.15 USD | 76.98 USD |
| `7D` | `10.84` | 17,100,000.00 USD | 0.00 USD | 17,100,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.85` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 1,690.00 USD | 4,450.00 USD | 3,740.00 USD |
| `7D` | `10.86` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD |
| `1D` | `10.87` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 493.01 USD | 2,760.00 USD | 216.86 USD |
| `7D` | `10.88` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD |
| `1D` | `10.89` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 6,320.00 USD | 11,320.00 USD | 36,650.00 USD |
| `7D` | `10.90` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.91` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 2,680.00 USD | 10,840.00 USD | 25,780.00 USD |
| `7D` | `10.92` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.93` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 98,300.00 USD | 28,100.00 USD | 41,520.00 USD |
| `7D` | `10.94` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.95` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 44,540.00 USD | 14,550.00 USD | 17,220.00 USD |
| `7D` | `10.96` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.97` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 80,360.00 USD | 15,940.00 USD | 33,990.00 USD |
| `7D` | `10.98` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,720.00 USD |
| `1D` | `10.99` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 19,350.00 USD | 10,180.00 USD | 15,010.00 USD |
| `7D` | `11.00` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `1D` | `11.01` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 53,160.00 USD | 23,840.00 USD | 28,290.00 USD |
| `7D` | `11.02` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD |
| `1D` | `11.03` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 80,130.00 USD | 12,950.00 USD | 30,850.00 USD |
| `7D` | `11.04` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `1D` | `11.05` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 14,150.00 USD | 402.52 USD | 8,210.00 USD |
| `7D` | `11.06` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.07` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 25,170.00 USD | 16,760.00 USD | 30,870.00 USD |
| `7D` | `11.08` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD |
| `1D` | `11.09` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 45,010.00 USD | 9,350.00 USD | 18,750.00 USD |
| `7D` | `11.10` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD |
| `1D` | `11.11` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 67,090.00 USD | 40,730.00 USD | 124,180.00 USD |
| `7D` | `11.12` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.13` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 101,350.00 USD | 62,700.00 USD | 98,610.00 USD |
| `7D` | `11.14` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,760.00 USD |
| `1D` | `11.15` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 216,180.00 USD | 64,850.00 USD | 118,910.00 USD |
| `7D` | `11.16` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.17` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 143,330.00 USD | 55,010.00 USD | 53,880.00 USD |
| `7D` | `11.18` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 641,660.00 USD | 214,580.00 USD | 541,220.00 USD |
| `1D` | `11.19` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 235,410.00 USD | 57,950.00 USD | 84,120.00 USD |
| `7D` | `11.20` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 371,240.00 USD | 239,970.00 USD | 129,030.00 USD |
| `1D` | `11.21` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 114,450.00 USD | 18,290.00 USD | 71,980.00 USD |
| `7D` | `11.22` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD |
| `1D` | `11.23` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 38,220.00 USD | 29,800.00 USD | 63,080.00 USD |
| `7D` | `11.24` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD |
| `1D` | `11.25` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 233,570.00 USD | 64,810.00 USD | 90,350.00 USD |
| `7D` | `11.26` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD |
| `1D` | `11.27` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 101,350.00 USD | 52,140.00 USD | 31,740.00 USD |
| `7D` | `11.28` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD |
| `1D` | `11.29` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 77,300.00 USD | 19,370.00 USD | 37,070.00 USD |
| `7D` | `11.30` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD |
| `1D` | `11.31` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 82,660.00 USD | 16,060.00 USD | 37,070.00 USD |
| `7D` | `11.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD |
| `1D` | `11.33` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 211,010.00 USD | 28,000.00 USD | 4,720.00 USD |
| `7D` | `11.34` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD |
| `1D` | `11.35` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 163,970.00 USD | 82,450.00 USD | 49,910.00 USD |
| `7D` | `11.36` | 927,160.00 USD | 0.00 USD | 927,160.00 USD | 170,150.00 USD | 48,220.00 USD | 45,390.00 USD |
| `1D` | `11.37` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 175,960.00 USD | 45,400.00 USD | 84,040.00 USD |
| `7D` | `11.38` | 663,400.00 USD | 0.00 USD | 663,400.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.39` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 54,830.00 USD | 37,490.00 USD | 50,880.00 USD |
| `7D` | `11.40` | 572,020.00 USD | 0.00 USD | 572,020.00 USD | 116,360.00 USD | 2,880.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 95,330.00 USD | 21,120.00 USD | 45,870.00 USD |
| `7D` | `11.42` | 435,960.00 USD | 0.00 USD | 435,960.00 USD | 30,910.00 USD | 0.00 USD | 24,730.00 USD |
| `1D` | `11.43` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 108,720.00 USD | 35,250.00 USD | 73,750.00 USD |
| `7D` | `11.44` | 380,330.00 USD | 0.00 USD | 380,330.00 USD | 104,540.00 USD | 29,600.00 USD | 37,930.00 USD |
| `1D` | `11.45` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 130,980.00 USD | 41,150.00 USD | 49,780.00 USD |
| `1D` | `11.47` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 22,690.00 USD | 5,940.00 USD | 0.00 USD |
| `7D` | `11.48` | 208,250.00 USD | 0.00 USD | 208,250.00 USD | 0.00 USD | 364.00 USD | 0.00 USD |
| `1D` | `11.49` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 10,420.00 USD | 7,360.00 USD | 6,410.00 USD |
| `7D` | `11.50` | 207,890.00 USD | 0.00 USD | 207,890.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD |
| `1D` | `11.51` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 63,350.00 USD | 62,370.00 USD | 0.00 USD |
| `7D` | `11.52` | 166,910.00 USD | 0.00 USD | 166,910.00 USD | 0.00 USD | 617.33 USD | 0.00 USD |
| `1D` | `11.53` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 13,090.00 USD | 7,330.00 USD | 24,130.00 USD |
| `7D` | `11.54` | 166,290.00 USD | 0.00 USD | 166,290.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.55` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 16,480.00 USD | 9,440.00 USD |
| `7D` | `11.56` | 131,520.00 USD | 0.00 USD | 131,520.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD |
| `1D` | `11.57` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 77,390.00 USD | 14,980.00 USD | 57,180.00 USD |
| `7D` | `11.58` | 120,890.00 USD | 0.00 USD | 120,890.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.61` | 957,900.00 USD | 0.00 USD | 957,900.00 USD | 66,890.00 USD | 12,350.00 USD | 0.00 USD |
| `1D` | `11.63` | 878,650.00 USD | 0.00 USD | 878,650.00 USD | 29,820.00 USD | 10,200.00 USD | 17,650.00 USD |
| `7D` | `11.64` | 89,270.00 USD | 0.00 USD | 89,270.00 USD | 0.00 USD | 56,880.00 USD | 32,380.00 USD |
| `1D` | `11.65` | 820,980.00 USD | 0.00 USD | 820,980.00 USD | 15,150.00 USD | 11,950.00 USD | 6,070.00 USD |
| `1D` | `11.67` | 787,810.00 USD | 0.00 USD | 787,810.00 USD | 46,480.00 USD | 25,490.00 USD | 42,890.00 USD |
| `7D` | `11.67` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.68` | 381.10 USD | 381.10 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.69` | 672,960.00 USD | 0.00 USD | 672,960.00 USD | 70,440.00 USD | 40,230.00 USD | 46,850.00 USD |
| `1D` | `11.71` | 515,440.00 USD | 0.00 USD | 515,440.00 USD | 233,730.00 USD | 60,320.00 USD | 63,740.00 USD |
| `7D` | `11.72` | 185,060.00 USD | 185,060.00 USD | 0.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 157,660.00 USD | 0.00 USD | 157,660.00 USD | 46,440.00 USD | 45,270.00 USD | 18,390.00 USD |
| `7D` | `11.74` | 208,130.00 USD | 208,130.00 USD | 0.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD |
| `1D` | `11.75` | 47,560.00 USD | 0.00 USD | 47,560.00 USD | 0.00 USD | 27,930.00 USD | 0.00 USD |
| `7D` | `11.76` | 275,570.00 USD | 275,570.00 USD | 0.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD |
| `1D` | `11.77` | 19,630.00 USD | 0.00 USD | 19,630.00 USD | 16,180.00 USD | 1,010.00 USD | 0.00 USD |
| `7D` | `11.78` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD |
| `1D` | `11.79` | 2,430.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD | 755.20 USD | 0.00 USD |
| `7D` | `11.80` | 744,880.00 USD | 744,880.00 USD | 0.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD |
| `1D` | `11.81` | 1,670.00 USD | 0.00 USD | 1,670.00 USD | 0.00 USD | 1,670.00 USD | 0.00 USD |
| `7D` | `11.82` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 158,640.00 USD | 77,820.00 USD | 91,580.00 USD |
| `1D` | `11.83` | 147,330.00 USD | 147,330.00 USD | 0.00 USD | 88,530.00 USD | 1,250.00 USD | 57,550.00 USD |
| `1D` | `11.83` | 294,650.00 USD | 294,650.00 USD | 0.00 USD | 88,530.00 USD | 1,250.00 USD | 57,550.00 USD |
| `7D` | `11.84` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD |
| `1D` | `11.85` | 510,010.00 USD | 510,010.00 USD | 0.00 USD | 101,420.00 USD | 22,590.00 USD | 91,350.00 USD |
| `7D` | `11.86` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 607,590.00 USD | 38,220.00 USD | 272,680.00 USD |
| `1D` | `11.87` | 532,140.00 USD | 532,140.00 USD | 0.00 USD | 0.00 USD | 22,130.00 USD | 0.00 USD |
| `7D` | `11.88` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 392,850.00 USD | 20,500.00 USD | 271,780.00 USD |
| `1D` | `11.89` | 533,650.00 USD | 533,650.00 USD | 0.00 USD | 1,170.00 USD | 338.62 USD | 0.00 USD |
| `7D` | `11.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 282,480.00 USD | 31,020.00 USD | 158,670.00 USD |
| `1D` | `11.91` | 533,970.00 USD | 533,970.00 USD | 0.00 USD | 0.00 USD | 303.23 USD | 20.02 USD |
| `7D` | `11.92` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD |
| `1D` | `11.93` | 534,400.00 USD | 534,400.00 USD | 0.00 USD | 0.00 USD | 411.11 USD | 20.74 USD |
| `7D` | `11.94` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD |
| `1D` | `11.95` | 552,360.00 USD | 552,360.00 USD | 0.00 USD | 1,220.00 USD | 3,230.00 USD | 13,510.00 USD |
| `7D` | `11.96` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD |
| `1D` | `11.97` | 628,680.00 USD | 628,680.00 USD | 0.00 USD | 57,420.00 USD | 804.05 USD | 18,090.00 USD |
| `7D` | `11.98` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD |
| `1D` | `11.99` | 710,260.00 USD | 710,260.00 USD | 0.00 USD | 38,440.00 USD | 252.46 USD | 42,890.00 USD |
| `7D` | `12.00` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD |
| `1D` | `12.01` | 847,850.00 USD | 847,850.00 USD | 0.00 USD | 103,200.00 USD | 467.98 USD | 33,920.00 USD |
| `7D` | `12.02` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD |
| `1D` | `12.03` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 155,200.00 USD | 72,410.00 USD | 78,900.00 USD |
| `7D` | `12.04` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD |
| `1D` | `12.05` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 297,590.00 USD | 90,620.00 USD | 106,600.00 USD |
| `7D` | `12.06` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 234,210.00 USD | 101,560.00 USD | 145,690.00 USD |
| `1D` | `12.07` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 185,870.00 USD | 68,300.00 USD | 103,920.00 USD |
| `7D` | `12.08` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD |
| `1D` | `12.09` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 17,900.00 USD | 20,350.00 USD | 23,890.00 USD |
| `7D` | `12.10` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.11` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 92,880.00 USD | 31,760.00 USD | 52,750.00 USD |
| `7D` | `12.12` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 89,810.00 USD | 44,490.00 USD | 95,850.00 USD |
| `1D` | `12.13` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 95,100.00 USD | 29,420.00 USD | 36,930.00 USD |
| `7D` | `12.14` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 118,920.00 USD | 64,740.00 USD | 31,180.00 USD |
| `1D` | `12.15` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 135,050.00 USD | 50,010.00 USD | 60,530.00 USD |
| `7D` | `12.16` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD |
| `1D` | `12.17` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 82,260.00 USD | 65,690.00 USD | 65,710.00 USD |
| `7D` | `12.18` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD |
| `1D` | `12.19` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 93,720.00 USD | 28,210.00 USD | 17,870.00 USD |
| `7D` | `12.20` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD |
| `1D` | `12.21` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 75,460.00 USD | 47,330.00 USD | 44,240.00 USD |
| `7D` | `12.22` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 261,490.00 USD | 19,920.00 USD | 93,540.00 USD |
| `1D` | `12.23` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 40,720.00 USD | 26,450.00 USD | 10,130.00 USD |
| `7D` | `12.24` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD |
| `1D` | `12.25` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 20,430.00 USD | 15,340.00 USD | 7,630.00 USD |
| `7D` | `12.26` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD |
| `1D` | `12.27` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 82,590.00 USD | 23,960.00 USD | 22,290.00 USD |
| `7D` | `12.28` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD |
| `1D` | `12.29` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 61,180.00 USD | 28,430.00 USD | 47,900.00 USD |
| `7D` | `12.30` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD |
| `1D` | `12.31` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 43,710.00 USD | 11,190.00 USD | 4,890.00 USD |
| `7D` | `12.32` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.33` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,680.00 USD | 3,700.00 USD | 7,630.00 USD |
| `7D` | `12.34` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 140,600.00 USD | 75,950.00 USD | 13,370.00 USD |
| `1D` | `12.35` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 28,910.00 USD | 8,540.00 USD | 9,470.00 USD |
| `7D` | `12.36` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD |
| `1D` | `12.37` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 26,750.00 USD | 9,040.00 USD | 5,620.00 USD |
| `7D` | `12.38` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD |
| `1D` | `12.39` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 39,170.00 USD | 18,440.00 USD | 21,580.00 USD |
| `7D` | `12.40` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 176,820.00 USD | 40,380.00 USD | 258,110.00 USD |
| `1D` | `12.41` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 36,820.00 USD | 25,680.00 USD | 23,480.00 USD |
| `7D` | `12.42` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 135,510.00 USD | 33,450.00 USD | 408,100.00 USD |
| `1D` | `12.43` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 23,450.00 USD | 5,940.00 USD | 203.40 USD |
| `7D` | `12.44` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 159,890.00 USD | 70,960.00 USD | 272,130.00 USD |
| `1D` | `12.45` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 15,620.00 USD | 10,150.00 USD | 13,760.00 USD |
| `7D` | `12.46` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD |
| `1D` | `12.47` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 3,620.00 USD | 12,000.00 USD | 12,450.00 USD |
| `7D` | `12.48` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD |
| `1D` | `12.49` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 1,710.00 USD | 63.95 USD | 1,520.00 USD |
| `7D` | `12.50` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD |
| `1D` | `12.51` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 11,360.00 USD | 7,590.00 USD | 14,720.00 USD |
| `7D` | `12.52` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.53` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 18,870.00 USD | 1,680.00 USD | 4,270.00 USD |
| `7D` | `12.54` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 96,800.00 USD | 59,960.00 USD | 107,190.00 USD |
| `1D` | `12.55` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 17,070.00 USD | 5,800.00 USD | 4,080.00 USD |
| `7D` | `12.56` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD |
| `1D` | `12.57` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 15,370.00 USD | 6,380.00 USD | 13,760.00 USD |
| `7D` | `12.58` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD |
| `1D` | `12.59` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 6,450.00 USD | 1,010.00 USD | 3,220.00 USD |
| `7D` | `12.60` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.61` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 5,510.00 USD | 1,350.00 USD | 7,170.00 USD |
| `7D` | `12.62` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.63` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 26,060.00 USD | 9,500.00 USD | 11,720.00 USD |
| `7D` | `12.64` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.65` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 8,750.00 USD | 4,250.00 USD | 4.92 USD |
| `7D` | `12.66` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.67` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 156.89 USD | 825.45 USD | 5,960.00 USD |
| `7D` | `12.68` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD |
| `1D` | `12.69` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 6,610.00 USD | 1,860.00 USD | 7,240.00 USD |
| `7D` | `12.70` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD |
| `1D` | `12.71` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 9,120.00 USD | 31.80 USD | 2,250.00 USD |
| `7D` | `12.72` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD |
| `1D` | `12.73` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 24,260.00 USD | 6,490.00 USD | 15,900.00 USD |
| `7D` | `12.74` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 21,020.00 USD |
| `1D` | `12.75` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 36,920.00 USD | 13,680.00 USD | 15,780.00 USD |
| `7D` | `12.76` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD |
| `1D` | `12.77` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 32,530.00 USD | 8,300.00 USD | 13,180.00 USD |
| `7D` | `12.78` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD |
| `1D` | `12.79` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 9,880.00 USD | 3,890.00 USD | 13,780.00 USD |
| `7D` | `12.80` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.81` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 7,290.00 USD | 3,110.00 USD | 28.70 USD |
| `7D` | `12.82` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.83` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 9,320.00 USD | 3,560.00 USD | 8,170.00 USD |
| `7D` | `12.84` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 29,710.00 USD | 15,870.00 USD | 7,710.00 USD |
| `1D` | `12.85` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 26,200.00 USD | 4,310.00 USD | 3,060.00 USD |
| `7D` | `12.86` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD |
| `1D` | `12.87` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 582.95 USD | 3,370.00 USD | 7,520.00 USD |
| `7D` | `12.88` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD |
| `1D` | `12.89` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 14,480.00 USD | 3,730.00 USD | 5,000.00 USD |
| `7D` | `12.90` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 41,140.00 USD | 16,610.00 USD | 13,080.00 USD |
| `1D` | `12.91` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 19,350.00 USD | 7,680.00 USD | 4,940.00 USD |
| `1D` | `12.93` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 212.28 USD | 0.00 USD | 0.00 USD |
| `1D` | `12.95` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 13,070.00 USD | 2,760.00 USD | 3,050.00 USD |
| `1D` | `12.97` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 8,530.00 USD | 7,830.00 USD | 2,670.00 USD |
| `1D` | `12.99` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 29,400.00 USD | 6,880.00 USD | 9,540.00 USD |
| `1D` | `13.01` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 18,040.00 USD | 6,860.00 USD | 10,380.00 USD |
| `1D` | `13.03` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 110.40 USD | 0.00 USD | 0.00 USD |
| `1D` | `13.05` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 141.55 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `13.07` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 14,050.00 USD | 3,650.00 USD | 1,550.00 USD |
| `1D` | `13.09` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 2,990.00 USD | 1,570.00 USD | 3,730.00 USD |
| `1D` | `13.11` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 6,340.00 USD | 7,680.00 USD | 6,930.00 USD |
| `1D` | `13.13` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 18,180.00 USD | 4,650.00 USD | 3,850.00 USD |
| `1D` | `13.15` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 2,380.00 USD | 0.00 USD |
| `1D` | `13.17` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 4,170.00 USD | 4,050.00 USD | 5,500.00 USD |
| `1D` | `13.19` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 2,540.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `565.93M` | Total OI Tokens: `47,853,495.5 LINK`
  * 1h OI Change: `-1.12%` | 4h OI Change: `+2.19%` | 24h OI Change: `+0.86%`
  * Exchange Breakdown: Binance=`107.51M` | Bybit=`66.43M` | OKX=`26.88M` | Hyperliquid=`57.78M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `17.40K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0097%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `32.46%` | `67.54%` | `0.48` | 537,270.00 USD |
| `15M` | `Binance` | `28.57%` | `71.43%` | `0.40` | 208,840.00 USD |
| `15M` | `OKX` | `23.96%` | `76.04%` | `0.32` | 32,920.00 USD |
| `15M` | `Bybit` | `38.39%` | `61.61%` | `0.62` | 24,310.00 USD |
| `15M` | `KuCoin` | `44.3%` | `55.7%` | `0.80` | 15,690.00 USD |
| `15M` | `Gate` | `42.13%` | `57.87%` | `0.73` | 12,850.00 USD |
| `15M` | `Bitget` | `5.47%` | `94.53%` | `0.06` | 5,100.00 USD |
| `15M` | `BingX` | `43.88%` | `56.12%` | `0.78` | 34,570.00 USD |
| `15M` | `MEXC` | `36.01%` | `63.99%` | `0.56` | 4,250.00 USD |
| `15M` | `Bitunix` | `32.65%` | `67.35%` | `0.48` | 5,700.00 USD |
| `15M` | `Hyperliquid` | `92.57%` | `7.43%` | `12.46` | 20,620.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.98%` | `50.02%` | `1.00` | 73,140.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.16%` | `99.84%` | `0.00` | 80,060.00 USD |
| `15M` | `HTX` | `53.82%` | `46.18%` | `1.17` | 15,220.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `61.24%` | `38.76%` | `1.58` | 3,480.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 295.63 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `92.9%` | `7.1%` | `13.08` | 210.64 USD |
| `15M` | `Whale Positions` | `28.57%` | `71.43%` | `0.40` | 208,840.00 USD |
| `15M` | `Global Accounts` | `32.46%` | `67.54%` | `0.48` | 537,270.00 USD |
| `1H` | `LINK` | `38.52%` | `61.48%` | `0.63` | 3,080,000.00 USD |
| `1H` | `Binance` | `42.55%` | `57.45%` | `0.74` | 1,060,000.00 USD |
| `1H` | `OKX` | `32.56%` | `67.44%` | `0.48` | 154,380.00 USD |
| `1H` | `Bybit` | `30.8%` | `69.2%` | `0.45` | 142,120.00 USD |
| `1H` | `KuCoin` | `47.22%` | `52.78%` | `0.89` | 67,900.00 USD |
| `1H` | `Gate` | `57.7%` | `42.3%` | `1.36` | 67,260.00 USD |
| `1H` | `Bitget` | `37.53%` | `62.47%` | `0.60` | 31,620.00 USD |
| `1H` | `BingX` | `16.1%` | `83.9%` | `0.19` | 424,200.00 USD |
| `1H` | `MEXC` | `62.12%` | `37.88%` | `1.64` | 51,570.00 USD |
| `1H` | `Bitunix` | `45.2%` | `54.8%` | `0.82` | 32,080.00 USD |
| `1H` | `Hyperliquid` | `89.06%` | `10.94%` | `8.14` | 141,820.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.61%` | `49.39%` | `1.02` | 435,220.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `12.16%` | `87.84%` | `0.14` | 364,550.00 USD |
| `1H` | `HTX` | `62.35%` | `37.65%` | `1.66` | 51,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `74.63%` | `25.37%` | `2.94` | 24,650.00 USD |
| `1H` | `Aster` | `10.93%` | `89.07%` | `0.12` | 5,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `1.84%` | `98.16%` | `0.02` | 23,080.00 USD |
| `1H` | `Whale Positions` | `42.55%` | `57.45%` | `0.74` | 1,060,000.00 USD |
| `1H` | `Global Accounts` | `38.52%` | `61.48%` | `0.63` | 3,080,000.00 USD |
| `4H` | `LINK` | `49.83%` | `50.17%` | `0.99` | 135,920,000.00 USD |
| `4H` | `Binance` | `53.41%` | `46.59%` | `1.15` | 47,890,000.00 USD |
| `4H` | `OKX` | `47.99%` | `52.01%` | `0.92` | 12,510,000.00 USD |
| `4H` | `Bybit` | `51.87%` | `48.13%` | `1.08` | 10,580,000.00 USD |
| `4H` | `KuCoin` | `44.8%` | `55.2%` | `0.81` | 1,030,000.00 USD |
| `4H` | `Gate` | `44.22%` | `55.78%` | `0.79` | 7,540,000.00 USD |
| `4H` | `Bitget` | `45.42%` | `54.58%` | `0.83` | 5,840,000.00 USD |
| `4H` | `BingX` | `36.4%` | `63.6%` | `0.57` | 6,600,000.00 USD |
| `4H` | `MEXC` | `50.76%` | `49.24%` | `1.03` | 13,590,000.00 USD |
| `4H` | `Bitunix` | `56.97%` | `43.03%` | `1.32` | 3,550,000.00 USD |
| `4H` | `Hyperliquid` | `63.61%` | `36.39%` | `1.75` | 1,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.01%` | `48.99%` | `1.04` | 22,560,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.79%` | `97.21%` | `0.03` | 1,920,000.00 USD |
| `4H` | `HTX` | `49.64%` | `50.36%` | `0.99` | 421,040.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.57%` | `50.43%` | `0.98` | 500,560.00 USD |
| `4H` | `Aster` | `61.56%` | `38.44%` | `1.60` | 38,810.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.18%` | `58.82%` | `0.70` | 44,860.00 USD |
| `4H` | `Whale Positions` | `53.41%` | `46.59%` | `1.15` | 47,890,000.00 USD |
| `4H` | `Global Accounts` | `49.83%` | `50.17%` | `0.99` | 135,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.61` | `11.62` | `11.61` | `11.64` | `11.60` | 1,343,341.40 USD | 918,798.02 USD | 424,543.38 USD | 494,254.64 USD | `+36.79%` | `16B / 2S` |
| `0:00 UTC` | `11.57` | `11.60` | `11.57` | `11.65` | `11.56` | 1,580,207.85 USD | 669,053.47 USD | 911,154.38 USD | -242,100.91 USD | `-15.32%` | `20B / 30S` |
| `5:00 UTC` | `11.58` | `11.60` | `11.58` | `11.63` | `11.58` | 1,099,120.73 USD | 704,449.96 USD | 394,670.77 USD | 309,779.19 USD | `+28.18%` | `12B / 8S` |
| `0:00 UTC` | `11.64` | `11.63` | `11.64` | `11.66` | `11.59` | 1,673,558.77 USD | 971,773.96 USD | 701,784.82 USD | 269,989.14 USD | `+16.13%` | `15B / 5S` |
| `5:00 UTC` | `11.64` | `11.62` | `11.64` | `11.65` | `11.61` | 856,800.01 USD | 412,856.03 USD | 443,943.98 USD | -31,087.96 USD | `-3.63%` | `5B / 13S` |
| `0:00 UTC` | `11.68` | `11.66` | `11.68` | `11.69` | `11.63` | 1,476,075.54 USD | 585,647.20 USD | 890,428.34 USD | -304,781.14 USD | `-20.65%` | `5B / 9S` |
| `5:00 UTC` | `11.67` | `11.67` | `11.67` | `11.70` | `11.65` | 1,710,411.82 USD | 917,052.89 USD | 793,358.93 USD | 123,693.95 USD | `+7.23%` | `6B / 7S` |
| `0:00 UTC` | `11.59` | `11.62` | `11.59` | `11.69` | `11.57` | 2,167,857.89 USD | 905,701.30 USD | 1,262,156.60 USD | -356,455.30 USD | `-16.44%` | `11B / 32S` |
| `5:00 UTC` | `11.61` | `11.62` | `11.61` | `11.68` | `11.57` | 1,501,963.10 USD | 797,959.25 USD | 704,003.85 USD | 93,955.40 USD | `+6.26%` | `26B / 12S` |
| `0:00 UTC` | `11.66` | `11.65` | `11.66` | `11.68` | `11.63` | 895,782.28 USD | 489,905.36 USD | 405,876.92 USD | 84,028.43 USD | `+9.38%` | `13B / 4S` |

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
| `5m` | 19,150.00 USD | -122,230.00 USD | **`DISTRIBUTION`** |
| `15m` | -77,140.00 USD | -197,010.00 USD | **`DISTRIBUTION`** |
| `30m` | 300,750.00 USD | -343,420.00 USD | **`DISTRIBUTION`** |
| `1h` | 194,580.00 USD | -1,490,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 643,300.00 USD | -504,700.00 USD | **`ACCUMULATION`** |
| `4h` | 1,120,000.00 USD | 655,960.00 USD | **`ACCUMULATION`** |
| `6h` | 1,130,000.00 USD | 630,770.00 USD | **`ACCUMULATION`** |
| `8h` | 1,280,000.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `12h` | 1,480,000.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `24h` | 1,480,000.00 USD | 847,010.00 USD | **`ACCUMULATION`** |
| `1w` | -7,780,000.00 USD | -21,240,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -70,370,000.00 USD | -181,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+19.15K` | 15m=`-77.14K` | 1h=`+194.58K` | 24h=`+1.48M`
* Futures Capital Netflows: 5m=`-122.23K` | 15m=`-197.01K` | 1h=`-1.49M` | 24h=`+847.01K`
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
  * Execution Entry: `11.42` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `11.20` (Risk Distance: `0.2267` pts)
  * +2.5R Take Profit: `11.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.15` (Risk Distance: `0.2267` pts)
  * +2.5R Take Profit: `11.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.93`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
