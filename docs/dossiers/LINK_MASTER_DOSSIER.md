# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-29 22:55:04 IST` (`2026-10-29 17:25:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.76` | **Live Ask Quote**: `11.84` | **Mid Price**: `11.80`
- **Spread Points**: `85.00` | **Spread BPS**: `72.04 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.80` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.88` | Lower -3.00σ Band: `11.72`
  * Upper +2.51σ Band: `11.86` | Lower -2.51σ Band: `11.73`
  * Upper +2.01σ Band: `11.85` | Lower -2.01σ Band: `11.75`
  * Upper +2.00σ Band: `11.85` | Lower -2.00σ Band: `11.75`
  * Upper +1.28σ Band: `11.83` | Lower -1.28σ Band: `11.77`
  * Upper +1.00σ Band: `11.82` | Lower -1.00σ Band: `11.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.80` | EMA-20=`11.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.80` (Slope: `+0.0000`) | EMA-100=`11.80`
  * Institutional Anchors: EMA-144=`11.80` | EMA-200=`11.80` (Slope: `+0.0000`) | EMA-233=`11.80`
- **Range Boundaries**: 24H High=`11.92` | 24H Low=`11.68` | Weekly High=`12.03` | Weekly Low=`11.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.92` (Distance: `-1.05%`)
  * Point of Control (POC) = `11.77` (Distance: `+0.22%`)
  * Value Area Low (VAL) = `11.43` (Distance: `+3.24%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `11.75` - `11.85`
  * Optimal Trade Entry (OTE 0.705): `11.82`
  * Structural Invalidation Anchor (0.786): `11.89`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.83` | `11.84` | `11.79` | `11.80` | `36,408` | 430,315.74 USD | -147,880.68 USD | `-34.37%` | 1,045,325.01 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.80` | `11.81` | `11.79` | `11.80` | `40,726` | 480,489.01 USD | -31,277.74 USD | `-6.51%` | 1,014,047.28 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `11.80` | `11.83` | `11.79` | `11.81` | `16,197` | 191,325.00 USD | 41,398.74 USD | `+21.64%` | 1,055,446.02 USD | `+0.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.86` | `11.87` | `11.82` | `11.86` | `77,975` | 923,896.67 USD | -200,671.96 USD | `-21.72%` | 1,302,488.68 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.86` | `11.87` | `11.79` | `11.80` | `106,626` | 1,261,426.96 USD | -205,186.20 USD | `-16.27%` | 1,097,302.48 USD | `-0.63` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.80` | `11.83` | `11.79` | `11.81` | `56,921` | 671,787.57 USD | 10,147.45 USD | `+1.51%` | 1,107,449.94 USD | `+0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.79` | `11.97` | `11.78` | `11.96` | `786,594` | 9,353,879.78 USD | 284,622.02 USD | `+3.04%` | 1,962,670.99 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.96` | `12.01` | `11.82` | `11.86` | `812,884` | 9,680,116.17 USD | -943,322.93 USD | `-9.74%` | 1,019,348.05 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.86` | `11.87` | `11.79` | `11.81` | `163,547` | 1,933,214.52 USD | -195,038.74 USD | `-10.09%` | 824,309.31 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.79` | `11.81` | `976,454` | 11,613,609.15 USD | -1,138,136.12 USD | `-9.80%` | -591,953.01 USD | `-0.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.79` | `11.81` | `976,454` | 11,613,609.15 USD | -1,138,136.12 USD | `-9.80%` | -591,953.01 USD | `-0.80` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `503` | `0x73ce...8ce9` | `LONG` | 4,733,337.26 USD | `400,011,600.00` | `12.05` | `11.80` | `9.13` | -86,416.44 USD | `-1.83%` | `5X Cross` |
| `646` | `0x5b5d...c060` | `SHORT` | 3,678,392.76 USD | `311,728,200.00` | `13.61` | `11.80` | `475.62` | 563,739.35 USD | `+15.33%` | `3X Cross` |
| `655` | `0xb83d...6e36` | `SHORT` | 3,634,652.84 USD | `308,152,000.00` | `12.93` | `11.80` | `404.71` | 350,600.66 USD | `+9.65%` | `3X Cross` |
| `875` | `0x458d...ab3b` | `LONG` | 2,679,313.28 USD | `227,156,700.00` | `13.13` | `11.80` | `9.34` | -302,917.12 USD | `-11.31%` | `3X Isolated` |
| `947` | `0xdd53...2b13` | `SHORT` | 2,436,408.54 USD | `206,475,300.00` | `11.92` | `11.80` | `264.06` | 24,814.39 USD | `+1.02%` | `3X Cross` |
| `974` | `0x3dc9...54b0` | `SHORT` | 2,366,800.00 USD | `200,000,000.00` | `7.56` | `11.80` | `77.37` | -855,641.58 USD | `-36.15%` | `10X Cross` |
| `1005` | `0x45d2...4029` | `SHORT` | 2,306,704.50 USD | `195,500,000.00` | `11.54` | `11.80` | `183.85` | -50,221.07 USD | `-2.18%` | `10X Cross` |
| `1193` | `0x6540...f7b7` | `LONG` | 1,934,653.44 USD | `164,051,000.00` | `12.48` | `11.80` | `8.01` | -112,162.94 USD | `-5.80%` | `5X Isolated` |
| `1249` | `0xeadc...9d55` | `LONG` | 1,860,445.50 USD | `157,691,600.00` | `9.43` | `11.80` | `0.000000` | 373,790.60 USD | `+20.09%` | `10X Cross` |
| `1619` | `0x9df2...c665` | `SHORT` | 1,396,506.87 USD | `118,217,800.00` | `11.48` | `11.80` | `245.78` | -38,903.31 USD | `-2.79%` | `10X Cross` |
| `1649` | `0xf6f3...47f8` | `SHORT` | 1,357,290.28 USD | `115,024,600.00` | `11.42` | `11.80` | `18.15` | -43,960.09 USD | `-3.24%` | `5X Cross` |
| `1810` | `0xfe7e...11b4` | `LONG` | 1,196,813.29 USD | `101,142,000.00` | `14.47` | `11.80` | `5.33` | -266,299.86 USD | `-22.25%` | `5X Isolated` |
| `1847` | `0x8af7...fa05` | `SHORT` | 1,163,511.53 USD | `98,661,200.00` | `14.08` | `11.80` | `203.07` | 225,671.01 USD | `+19.40%` | `10X Cross` |
| `1902` | `0xb7ec...5166` | `LONG` | 1,114,815.04 USD | `94,515,900.00` | `9.01` | `11.80` | `7.20` | 262,954.46 USD | `+23.59%` | `4X Cross` |

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
  * 24H Horizon: Short MP=`12.05` (Vol: 117,000.00 USD, Dist: `+2.10%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--5.24%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+2.10%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--4.43%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+3.53%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--5.51%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+3.55%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--5.48%`)
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
| `7D` | `Long Liquidation` | `10.42` | 18,360,000.00 USD | 18,360,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 18,280,000.00 USD | 18,280,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 14,500.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.46` | 18,230,000.00 USD | 18,230,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 18,120,000.00 USD | 18,120,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 18,060,000.00 USD | 18,060,000.00 USD | 42,030.00 USD | 16,000.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 17,990,000.00 USD | 17,990,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 17,950,000.00 USD | 17,950,000.00 USD | 25,600.00 USD | 72.80 USD | 12,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,960.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.56` | 17,910,000.00 USD | 17,910,000.00 USD | 51,230.00 USD | 16,690.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 17,830,000.00 USD | 17,830,000.00 USD | 84,220.00 USD | 6,710.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,870,000.00 USD | 6,870,000.00 USD | 14,760.00 USD | 6,390.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 17,720,000.00 USD | 17,720,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,840,000.00 USD | 6,840,000.00 USD | 23,000.00 USD | 7,080.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 17,680,000.00 USD | 17,680,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 6,800,000.00 USD | 6,800,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 17,650,000.00 USD | 17,650,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 6,760,000.00 USD | 6,760,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 17,600,000.00 USD | 17,600,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 6,730,000.00 USD | 6,730,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 17,580,000.00 USD | 17,580,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 6,720,000.00 USD | 6,720,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 17,550,000.00 USD | 17,550,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 6,710,000.00 USD | 6,710,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 17,530,000.00 USD | 17,530,000.00 USD | 21,070.00 USD | 4,880.00 USD | 264.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 6,690,000.00 USD | 6,690,000.00 USD | 13,200.00 USD | 8,380.00 USD | 7,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 17,510,000.00 USD | 17,510,000.00 USD | 25,580.00 USD | 3,690.00 USD | 315.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 999,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 6,660,000.00 USD | 6,660,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 17,480,000.00 USD | 17,480,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 6,640,000.00 USD | 6,640,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 17,460,000.00 USD | 17,460,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 6,630,000.00 USD | 6,630,000.00 USD | 4,760.00 USD | 0.00 USD | 113.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 17,410,000.00 USD | 17,410,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 6,630,000.00 USD | 6,630,000.00 USD | 2,030.00 USD | 0.00 USD | 110.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 17,270,000.00 USD | 17,270,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 6,630,000.00 USD | 6,630,000.00 USD | 2,330.00 USD | 160.15 USD | 31.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,100,000.00 USD | 17,100,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 81,870.00 USD | 785,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 6,620,000.00 USD | 6,620,000.00 USD | 976.86 USD | 4,520.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 16,930,000.00 USD | 16,930,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 6,610,000.00 USD | 6,610,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 16,580,000.00 USD | 16,580,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 6,580,000.00 USD | 6,580,000.00 USD | 5,680.00 USD | 3,770.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 16,120,000.00 USD | 16,120,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 6,550,000.00 USD | 6,550,000.00 USD | 67,690.00 USD | 28,790.00 USD | 58,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 15,680,000.00 USD | 15,680,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 6,390,000.00 USD | 6,390,000.00 USD | 47,180.00 USD | 17,110.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 14,780,000.00 USD | 14,780,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 703,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 6,320,000.00 USD | 6,320,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 14,190,000.00 USD | 14,190,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 6,170,000.00 USD | 6,170,000.00 USD | 24,400.00 USD | 2,590.00 USD | 27,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 13,630,000.00 USD | 13,630,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 6,120,000.00 USD | 6,120,000.00 USD | 18,580.00 USD | 7,740.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 13,260,000.00 USD | 13,260,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 6,070,000.00 USD | 6,070,000.00 USD | 96,430.00 USD | 24,240.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 12,880,000.00 USD | 12,880,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,910,000.00 USD | 5,910,000.00 USD | 21,360.00 USD | 12,540.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,370,000.00 USD | 12,370,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 23,500.00 USD | 145,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,880,000.00 USD | 5,880,000.00 USD | 18,980.00 USD | 5,700.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 11,720,000.00 USD | 11,720,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,830,000.00 USD | 5,830,000.00 USD | 37,640.00 USD | 15,180.00 USD | 29,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 11,310,000.00 USD | 11,310,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 5,750,000.00 USD | 5,750,000.00 USD | 71,900.00 USD | 32,070.00 USD | 61,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 10,500,000.00 USD | 10,500,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 5,580,000.00 USD | 5,580,000.00 USD | 55,540.00 USD | 39,050.00 USD | 102,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 9,310,000.00 USD | 9,310,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 5,390,000.00 USD | 5,390,000.00 USD | 184,320.00 USD | 79,200.00 USD | 142,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 8,260,000.00 USD | 8,260,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 49,590.00 USD | 122,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 4,980,000.00 USD | 4,980,000.00 USD | 193,330.00 USD | 56,510.00 USD | 88,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 6,780,000.00 USD | 6,780,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 4,640,000.00 USD | 4,640,000.00 USD | 127,360.00 USD | 41,100.00 USD | 44,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 5,480,000.00 USD | 5,480,000.00 USD | 641,660.00 USD | 214,580.00 USD | 541,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 4,430,000.00 USD | 4,430,000.00 USD | 200,280.00 USD | 47,820.00 USD | 96,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,080,000.00 USD | 4,080,000.00 USD | 371,240.00 USD | 239,970.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 4,090,000.00 USD | 4,090,000.00 USD | 90,990.00 USD | 30,210.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,340,000.00 USD | 3,340,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 3,920,000.00 USD | 3,920,000.00 USD | 126,690.00 USD | 67,320.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 2,690,000.00 USD | 2,690,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 21,540.00 USD | 72,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 3,650,000.00 USD | 3,650,000.00 USD | 195,380.00 USD | 46,420.00 USD | 64,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,410,000.00 USD | 2,410,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 3,340,000.00 USD | 3,340,000.00 USD | 53,900.00 USD | 14,850.00 USD | 35,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 1,860,000.00 USD | 1,860,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 3,230,000.00 USD | 3,230,000.00 USD | 83,100.00 USD | 25,330.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,460,000.00 USD | 1,460,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 3,090,000.00 USD | 3,090,000.00 USD | 120,360.00 USD | 16,200.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,390,000.00 USD | 1,390,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 2,930,000.00 USD | 2,930,000.00 USD | 227,540.00 USD | 40,510.00 USD | 17,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,270,000.00 USD | 1,270,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 46,360.00 USD | 51,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 2,640,000.00 USD | 2,640,000.00 USD | 253,660.00 USD | 93,280.00 USD | 82,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 927,160.00 USD | 927,160.00 USD | 170,150.00 USD | 48,220.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 2,210,000.00 USD | 2,210,000.00 USD | 22,780.00 USD | 44,850.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 663,400.00 USD | 663,400.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 2,090,000.00 USD | 2,090,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 572,020.00 USD | 572,020.00 USD | 116,360.00 USD | 2,880.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 1,900,000.00 USD | 1,900,000.00 USD | 87,050.00 USD | 20,670.00 USD | 32,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 435,960.00 USD | 435,960.00 USD | 30,910.00 USD | 0.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 1,760,000.00 USD | 1,760,000.00 USD | 87,760.00 USD | 43,710.00 USD | 71,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 380,330.00 USD | 380,330.00 USD | 104,540.00 USD | 29,600.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 1,550,000.00 USD | 1,550,000.00 USD | 117,740.00 USD | 17,790.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 1,390,000.00 USD | 1,390,000.00 USD | 16,710.00 USD | 11,070.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 208,250.00 USD | 208,250.00 USD | 0.00 USD | 364.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 1,360,000.00 USD | 1,360,000.00 USD | 63,350.00 USD | 38,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 207,890.00 USD | 207,890.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 1,260,000.00 USD | 1,260,000.00 USD | 13,090.00 USD | 26,540.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.52` | 166,910.00 USD | 166,910.00 USD | 0.00 USD | 617.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.54` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.54` | 166,290.00 USD | 166,290.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 1,190,000.00 USD | 1,190,000.00 USD | 31,990.00 USD | 16,480.00 USD | 73,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.56` | 131,520.00 USD | 131,520.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.58` | 1,060,000.00 USD | 1,060,000.00 USD | 45,400.00 USD | 15,060.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.58` | 120,890.00 USD | 120,890.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 985,690.00 USD | 985,690.00 USD | 78,360.00 USD | 9,700.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.62` | 883,930.00 USD | 883,930.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.64` | 870,010.00 USD | 870,010.00 USD | 44,970.00 USD | 21,590.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.64` | 89,270.00 USD | 89,270.00 USD | 0.00 USD | 56,880.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.65` | 4,910.00 USD | 4,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.66` | 786,290.00 USD | 786,290.00 USD | 15,560.00 USD | 13,520.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.68` | 732,340.00 USD | 732,340.00 USD | 30,920.00 USD | 24,620.00 USD | 45,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 381.10 USD | 381.10 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.70` | 631,170.00 USD | 631,170.00 USD | 186,010.00 USD | 75,640.00 USD | 45,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.72` | 324,400.00 USD | 324,400.00 USD | 164,600.00 USD | 46,140.00 USD | 56,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 185,060.00 USD | 185,060.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.74` | 57,430.00 USD | 57,430.00 USD | 0.00 USD | 24,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 208,130.00 USD | 208,130.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.76` | 32,750.00 USD | 32,750.00 USD | 0.00 USD | 15,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 275,570.00 USD | 275,570.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.78` | 17,030.00 USD | 17,030.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 744,880.00 USD | 744,880.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 1,070,000.00 USD | 1,070,000.00 USD | 158,640.00 USD | 77,820.00 USD | 91,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 145,230.00 USD | 145,230.00 USD | 101,190.00 USD | 1,130.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,590,000.00 USD | 1,590,000.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 239,160.00 USD | 239,160.00 USD | 232.40 USD | 43,150.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 2,510,000.00 USD | 2,510,000.00 USD | 607,590.00 USD | 38,220.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 240,690.00 USD | 240,690.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 3,200,000.00 USD | 3,200,000.00 USD | 392,850.00 USD | 20,500.00 USD | 271,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 241,920.00 USD | 241,920.00 USD | 1,170.00 USD | 59.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 3,670,000.00 USD | 3,670,000.00 USD | 282,480.00 USD | 31,020.00 USD | 158,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 242,370.00 USD | 242,370.00 USD | 0.00 USD | 430.44 USD | 20.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 4,170,000.00 USD | 4,170,000.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 244,770.00 USD | 244,770.00 USD | 1,220.00 USD | 1,140.00 USD | 43.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 4,690,000.00 USD | 4,690,000.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 262,860.00 USD | 262,860.00 USD | 1,410.00 USD | 3,120.00 USD | 13,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 5,200,000.00 USD | 5,200,000.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 354,760.00 USD | 354,760.00 USD | 61,680.00 USD | 87.08 USD | 30,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 5,780,000.00 USD | 5,780,000.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 510,410.00 USD | 510,410.00 USD | 113,530.00 USD | 469.84 USD | 41,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 6,290,000.00 USD | 6,290,000.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 684,140.00 USD | 684,140.00 USD | 94,390.00 USD | 34,630.00 USD | 44,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 6,830,000.00 USD | 6,830,000.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 1,080,000.00 USD | 1,080,000.00 USD | 211,740.00 USD | 79,430.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 7,380,000.00 USD | 7,380,000.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.05` | 2,600.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.06` | 1,570,000.00 USD | 1,570,000.00 USD | 237,200.00 USD | 89,280.00 USD | 160,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 7,860,000.00 USD | 7,860,000.00 USD | 234,210.00 USD | 101,560.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 1,820,000.00 USD | 1,820,000.00 USD | 146,690.00 USD | 45,990.00 USD | 60,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 8,490,000.00 USD | 8,490,000.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 1,890,000.00 USD | 1,890,000.00 USD | 19,140.00 USD | 14,280.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 8,620,000.00 USD | 8,620,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 2,110,000.00 USD | 2,110,000.00 USD | 132,110.00 USD | 47,150.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 8,850,000.00 USD | 8,850,000.00 USD | 89,810.00 USD | 44,490.00 USD | 95,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 2,280,000.00 USD | 2,280,000.00 USD | 88,560.00 USD | 28,780.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 9,070,000.00 USD | 9,070,000.00 USD | 118,920.00 USD | 64,740.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,130.00 USD | 5,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 2,490,000.00 USD | 2,490,000.00 USD | 90,620.00 USD | 57,300.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 9,320,000.00 USD | 9,320,000.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 2,710,000.00 USD | 2,710,000.00 USD | 132,660.00 USD | 47,620.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 9,420,000.00 USD | 9,420,000.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 2,870,000.00 USD | 2,870,000.00 USD | 89,740.00 USD | 40,990.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 9,690,000.00 USD | 9,690,000.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 2,970,000.00 USD | 2,970,000.00 USD | 29,450.00 USD | 39,070.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 10,070,000.00 USD | 10,070,000.00 USD | 261,490.00 USD | 19,920.00 USD | 93,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 3,030,000.00 USD | 3,030,000.00 USD | 35,430.00 USD | 14,730.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 10,320,000.00 USD | 10,320,000.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 872.20 USD | 6,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 3,130,000.00 USD | 3,130,000.00 USD | 51,100.00 USD | 27,170.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 10,580,000.00 USD | 10,580,000.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 3,280,000.00 USD | 3,280,000.00 USD | 101,040.00 USD | 24,800.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 11,050,000.00 USD | 11,050,000.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 3,410,000.00 USD | 3,410,000.00 USD | 59,030.00 USD | 22,230.00 USD | 42,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 11,390,000.00 USD | 11,390,000.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 3,410,000.00 USD | 3,410,000.00 USD | 391.20 USD | 7,100.00 USD | 37.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 11,580,000.00 USD | 11,580,000.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 3,470,000.00 USD | 3,470,000.00 USD | 29,830.00 USD | 8,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 11,810,000.00 USD | 11,810,000.00 USD | 140,600.00 USD | 75,950.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 941.07 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 3,500,000.00 USD | 3,500,000.00 USD | 19,510.00 USD | 9,040.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 11,920,000.00 USD | 11,920,000.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 3,550,000.00 USD | 3,550,000.00 USD | 29,950.00 USD | 6,420.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 12,070,000.00 USD | 12,070,000.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 3,620,000.00 USD | 3,620,000.00 USD | 19,630.00 USD | 23,720.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 12,540,000.00 USD | 12,540,000.00 USD | 176,820.00 USD | 40,380.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 3,690,000.00 USD | 3,690,000.00 USD | 51,980.00 USD | 13,980.00 USD | 9,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 13,120,000.00 USD | 13,120,000.00 USD | 135,510.00 USD | 33,450.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 3,730,000.00 USD | 3,730,000.00 USD | 18,760.00 USD | 10,270.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 13,620,000.00 USD | 13,620,000.00 USD | 159,890.00 USD | 70,960.00 USD | 272,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 6,490.00 USD | 13,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 3,760,000.00 USD | 3,760,000.00 USD | 4,980.00 USD | 15,260.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 13,870,000.00 USD | 13,870,000.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 3,780,000.00 USD | 3,780,000.00 USD | 3,100.00 USD | 2,560.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 14,110,000.00 USD | 14,110,000.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 3,790,000.00 USD | 3,790,000.00 USD | 1,320.00 USD | 4,320.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 14,360,000.00 USD | 14,360,000.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 3,830,000.00 USD | 3,830,000.00 USD | 20,590.00 USD | 5,020.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 14,700,000.00 USD | 14,700,000.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 3,850,000.00 USD | 3,850,000.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 14,960,000.00 USD | 14,960,000.00 USD | 96,800.00 USD | 59,960.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 193.27 USD | 14,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.56` | 3,890,000.00 USD | 3,890,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 15,150,000.00 USD | 15,150,000.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 3,910,000.00 USD | 3,910,000.00 USD | 6,740.00 USD | 1,030.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 15,350,000.00 USD | 15,350,000.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 3,920,000.00 USD | 3,920,000.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 15,470,000.00 USD | 15,470,000.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 3,950,000.00 USD | 3,950,000.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 15,540,000.00 USD | 15,540,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 3,980,000.00 USD | 3,980,000.00 USD | 21,870.00 USD | 4,240.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 15,840,000.00 USD | 15,840,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 4,380.00 USD | 18,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 3,990,000.00 USD | 3,990,000.00 USD | 648.46 USD | 23.77 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 15,990,000.00 USD | 15,990,000.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 4,000,000.00 USD | 4,000,000.00 USD | 3,670.00 USD | 1,540.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 16,290,000.00 USD | 16,290,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 4,010,000.00 USD | 4,010,000.00 USD | 2,940.00 USD | 1,140.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 16,500,000.00 USD | 16,500,000.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 4,040,000.00 USD | 4,040,000.00 USD | 24,470.00 USD | 3,750.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 16,690,000.00 USD | 16,690,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 4,090,000.00 USD | 4,090,000.00 USD | 20,500.00 USD | 10,520.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 16,760,000.00 USD | 16,760,000.00 USD | 38,570.00 USD | 18,330.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 4,160,000.00 USD | 4,160,000.00 USD | 43,450.00 USD | 12,260.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 16,820,000.00 USD | 16,820,000.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 4,200,000.00 USD | 4,200,000.00 USD | 19,150.00 USD | 3,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 16,930,000.00 USD | 16,930,000.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 4,220,000.00 USD | 4,220,000.00 USD | 12,430.00 USD | 5,860.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 16,980,000.00 USD | 16,980,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 4,230,000.00 USD | 4,230,000.00 USD | 2,680.00 USD | 1,230.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 17,000,000.00 USD | 17,000,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 4,250,000.00 USD | 4,250,000.00 USD | 14,360.00 USD | 5,860.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 17,060,000.00 USD | 17,060,000.00 USD | 29,710.00 USD | 15,870.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 4,280,000.00 USD | 4,280,000.00 USD | 19,070.00 USD | 1,990.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 17,100,000.00 USD | 17,100,000.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 4,300,000.00 USD | 4,300,000.00 USD | 7,890.00 USD | 3,720.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 17,140,000.00 USD | 17,140,000.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 4,330,000.00 USD | 4,330,000.00 USD | 19,260.00 USD | 7,240.00 USD | 2,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 17,210,000.00 USD | 17,210,000.00 USD | 41,140.00 USD | 16,610.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 4,340,000.00 USD | 4,340,000.00 USD | 6,680.00 USD | 2,610.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 4,360,000.00 USD | 4,360,000.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 4,370,000.00 USD | 4,370,000.00 USD | 114.70 USD | 5,090.00 USD | 3,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 4,400,000.00 USD | 4,400,000.00 USD | 22,080.00 USD | 7,080.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 4,450,000.00 USD | 4,450,000.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.02` | 4,470,000.00 USD | 4,470,000.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.04` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 18,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `13.06` | 4,480,000.00 USD | 4,480,000.00 USD | 9,530.00 USD | 1,380.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.08` | 4,490,000.00 USD | 4,490,000.00 USD | 7,640.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.10` | 4,510,000.00 USD | 4,510,000.00 USD | 6,340.00 USD | 5,500.00 USD | 7,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.12` | 4,540,000.00 USD | 4,540,000.00 USD | 11,610.00 USD | 8,380.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.14` | 4,550,000.00 USD | 4,550,000.00 USD | 6,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 18,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `13.16` | 4,560,000.00 USD | 4,560,000.00 USD | 4,170.00 USD | 4,090.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.18` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 4,870.00 USD | 2,940.00 USD | `Tier 1 CEX` |
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
| `1D` | `10.60` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 14,760.00 USD | 6,390.00 USD | 3,210.00 USD |
| `7D` | `10.60` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD |
| `1D` | `10.62` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 23,000.00 USD | 7,080.00 USD | 8,910.00 USD |
| `7D` | `10.62` | 17,680,000.00 USD | 0.00 USD | 17,680,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD |
| `1D` | `10.64` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD |
| `7D` | `10.64` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.66` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD |
| `7D` | `10.66` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.68` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.70` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `10.70` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.72` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD |
| `7D` | `10.72` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 21,070.00 USD | 4,880.00 USD | 264.88 USD |
| `1D` | `10.74` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 13,200.00 USD | 8,380.00 USD | 7,200.00 USD |
| `7D` | `10.74` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 25,580.00 USD | 3,690.00 USD | 315.57 USD |
| `1D` | `10.76` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD |
| `7D` | `10.76` | 17,480,000.00 USD | 0.00 USD | 17,480,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD |
| `1D` | `10.78` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD |
| `7D` | `10.78` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD |
| `1D` | `10.80` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 4,760.00 USD | 0.00 USD | 113.67 USD |
| `7D` | `10.80` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,260.00 USD |
| `1D` | `10.82` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 2,030.00 USD | 0.00 USD | 110.76 USD |
| `7D` | `10.82` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD |
| `1D` | `10.84` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 2,330.00 USD | 160.15 USD | 31.01 USD |
| `7D` | `10.84` | 17,100,000.00 USD | 0.00 USD | 17,100,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.86` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 976.86 USD | 4,520.00 USD | 3,840.00 USD |
| `7D` | `10.86` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,250.00 USD |
| `7D` | `10.88` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD |
| `1D` | `10.90` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 5,680.00 USD | 3,770.00 USD | 26,510.00 USD |
| `7D` | `10.90` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.92` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 67,690.00 USD | 28,790.00 USD | 58,390.00 USD |
| `7D` | `10.92` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.94` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 47,180.00 USD | 17,110.00 USD | 5,740.00 USD |
| `7D` | `10.94` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.96` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD |
| `7D` | `10.96` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.98` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 24,400.00 USD | 2,590.00 USD | 27,190.00 USD |
| `7D` | `10.98` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,720.00 USD |
| `1D` | `11.00` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 18,580.00 USD | 7,740.00 USD | 22,460.00 USD |
| `7D` | `11.00` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `1D` | `11.02` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 96,430.00 USD | 24,240.00 USD | 36,400.00 USD |
| `7D` | `11.02` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD |
| `1D` | `11.04` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 21,360.00 USD | 12,540.00 USD | 2,830.00 USD |
| `7D` | `11.04` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `1D` | `11.06` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 18,980.00 USD | 5,700.00 USD | 20,430.00 USD |
| `7D` | `11.06` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.08` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 37,640.00 USD | 15,180.00 USD | 29,470.00 USD |
| `7D` | `11.08` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD |
| `1D` | `11.10` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 71,900.00 USD | 32,070.00 USD | 61,920.00 USD |
| `7D` | `11.10` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD |
| `1D` | `11.12` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 55,540.00 USD | 39,050.00 USD | 102,450.00 USD |
| `7D` | `11.12` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.14` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 184,320.00 USD | 79,200.00 USD | 142,460.00 USD |
| `7D` | `11.14` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,760.00 USD |
| `1D` | `11.16` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 193,330.00 USD | 56,510.00 USD | 88,170.00 USD |
| `7D` | `11.16` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.18` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 127,360.00 USD | 41,100.00 USD | 44,560.00 USD |
| `7D` | `11.18` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 641,660.00 USD | 214,580.00 USD | 541,220.00 USD |
| `1D` | `11.20` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 200,280.00 USD | 47,820.00 USD | 96,770.00 USD |
| `7D` | `11.20` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 371,240.00 USD | 239,970.00 USD | 129,030.00 USD |
| `1D` | `11.22` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 90,990.00 USD | 30,210.00 USD | 48,500.00 USD |
| `7D` | `11.22` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD |
| `1D` | `11.24` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 126,690.00 USD | 67,320.00 USD | 76,300.00 USD |
| `7D` | `11.24` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 195,380.00 USD | 46,420.00 USD | 64,940.00 USD |
| `7D` | `11.26` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD |
| `1D` | `11.28` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 53,900.00 USD | 14,850.00 USD | 35,510.00 USD |
| `7D` | `11.28` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 83,100.00 USD | 25,330.00 USD | 31,710.00 USD |
| `7D` | `11.30` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD |
| `1D` | `11.32` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 120,360.00 USD | 16,200.00 USD | 28,360.00 USD |
| `7D` | `11.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD |
| `1D` | `11.34` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 227,540.00 USD | 40,510.00 USD | 17,330.00 USD |
| `7D` | `11.34` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD |
| `1D` | `11.36` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 253,660.00 USD | 93,280.00 USD | 82,220.00 USD |
| `7D` | `11.36` | 927,160.00 USD | 0.00 USD | 927,160.00 USD | 170,150.00 USD | 48,220.00 USD | 45,390.00 USD |
| `1D` | `11.38` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 22,780.00 USD | 44,850.00 USD | 58,270.00 USD |
| `7D` | `11.38` | 663,400.00 USD | 0.00 USD | 663,400.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD |
| `7D` | `11.40` | 572,020.00 USD | 0.00 USD | 572,020.00 USD | 116,360.00 USD | 2,880.00 USD | 16,820.00 USD |
| `1D` | `11.42` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 87,050.00 USD | 20,670.00 USD | 32,970.00 USD |
| `7D` | `11.42` | 435,960.00 USD | 0.00 USD | 435,960.00 USD | 30,910.00 USD | 0.00 USD | 24,730.00 USD |
| `1D` | `11.44` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 87,760.00 USD | 43,710.00 USD | 71,320.00 USD |
| `7D` | `11.44` | 380,330.00 USD | 0.00 USD | 380,330.00 USD | 104,540.00 USD | 29,600.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 117,740.00 USD | 17,790.00 USD | 24,850.00 USD |
| `1D` | `11.48` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 16,710.00 USD | 11,070.00 USD | 6,410.00 USD |
| `7D` | `11.48` | 208,250.00 USD | 0.00 USD | 208,250.00 USD | 0.00 USD | 364.00 USD | 0.00 USD |
| `1D` | `11.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 63,350.00 USD | 38,060.00 USD | 0.00 USD |
| `7D` | `11.50` | 207,890.00 USD | 0.00 USD | 207,890.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD |
| `1D` | `11.52` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 13,090.00 USD | 26,540.00 USD | 8,860.00 USD |
| `7D` | `11.52` | 166,910.00 USD | 0.00 USD | 166,910.00 USD | 0.00 USD | 617.33 USD | 0.00 USD |
| `1D` | `11.54` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD |
| `7D` | `11.54` | 166,290.00 USD | 0.00 USD | 166,290.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.56` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 31,990.00 USD | 16,480.00 USD | 73,020.00 USD |
| `7D` | `11.56` | 131,520.00 USD | 0.00 USD | 131,520.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD |
| `1D` | `11.58` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 45,400.00 USD | 15,060.00 USD | 17,550.00 USD |
| `7D` | `11.58` | 120,890.00 USD | 0.00 USD | 120,890.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 985,690.00 USD | 0.00 USD | 985,690.00 USD | 78,360.00 USD | 9,700.00 USD | 13,710.00 USD |
| `1D` | `11.62` | 883,930.00 USD | 0.00 USD | 883,930.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD |
| `1D` | `11.64` | 870,010.00 USD | 0.00 USD | 870,010.00 USD | 44,970.00 USD | 21,590.00 USD | 17,150.00 USD |
| `7D` | `11.64` | 89,270.00 USD | 0.00 USD | 89,270.00 USD | 0.00 USD | 56,880.00 USD | 32,380.00 USD |
| `1D` | `11.66` | 786,290.00 USD | 0.00 USD | 786,290.00 USD | 15,560.00 USD | 13,520.00 USD | 24,880.00 USD |
| `7D` | `11.67` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.68` | 732,340.00 USD | 0.00 USD | 732,340.00 USD | 30,920.00 USD | 24,620.00 USD | 45,630.00 USD |
| `7D` | `11.68` | 381.10 USD | 381.10 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.70` | 631,170.00 USD | 0.00 USD | 631,170.00 USD | 186,010.00 USD | 75,640.00 USD | 45,120.00 USD |
| `1D` | `11.72` | 324,400.00 USD | 0.00 USD | 324,400.00 USD | 164,600.00 USD | 46,140.00 USD | 56,230.00 USD |
| `7D` | `11.72` | 185,060.00 USD | 185,060.00 USD | 0.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 57,430.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 24,690.00 USD | 0.00 USD |
| `7D` | `11.74` | 208,130.00 USD | 208,130.00 USD | 0.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD |
| `1D` | `11.76` | 32,750.00 USD | 0.00 USD | 32,750.00 USD | 0.00 USD | 15,710.00 USD | 0.00 USD |
| `7D` | `11.76` | 275,570.00 USD | 275,570.00 USD | 0.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD |
| `1D` | `11.78` | 17,030.00 USD | 0.00 USD | 17,030.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD |
| `7D` | `11.78` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD |
| `1D` | `11.80` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `1D` | `11.80` | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `11.80` | 744,880.00 USD | 744,880.00 USD | 0.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD |
| `7D` | `11.82` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 158,640.00 USD | 77,820.00 USD | 91,580.00 USD |
| `1D` | `11.84` | 145,230.00 USD | 145,230.00 USD | 0.00 USD | 101,190.00 USD | 1,130.00 USD | 40,790.00 USD |
| `7D` | `11.84` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD |
| `1D` | `11.86` | 239,160.00 USD | 239,160.00 USD | 0.00 USD | 232.40 USD | 43,150.00 USD | 50,560.00 USD |
| `7D` | `11.86` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 607,590.00 USD | 38,220.00 USD | 272,680.00 USD |
| `1D` | `11.88` | 240,690.00 USD | 240,690.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD |
| `7D` | `11.88` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 392,850.00 USD | 20,500.00 USD | 271,780.00 USD |
| `1D` | `11.90` | 241,920.00 USD | 241,920.00 USD | 0.00 USD | 1,170.00 USD | 59.50 USD | 0.00 USD |
| `7D` | `11.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 282,480.00 USD | 31,020.00 USD | 158,670.00 USD |
| `1D` | `11.92` | 242,370.00 USD | 242,370.00 USD | 0.00 USD | 0.00 USD | 430.44 USD | 20.02 USD |
| `7D` | `11.92` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD |
| `1D` | `11.94` | 244,770.00 USD | 244,770.00 USD | 0.00 USD | 1,220.00 USD | 1,140.00 USD | 43.06 USD |
| `7D` | `11.94` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 262,860.00 USD | 262,860.00 USD | 0.00 USD | 1,410.00 USD | 3,120.00 USD | 13,560.00 USD |
| `7D` | `11.96` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD |
| `1D` | `11.98` | 354,760.00 USD | 354,760.00 USD | 0.00 USD | 61,680.00 USD | 87.08 USD | 30,130.00 USD |
| `7D` | `11.98` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD |
| `1D` | `12.00` | 510,410.00 USD | 510,410.00 USD | 0.00 USD | 113,530.00 USD | 469.84 USD | 41,650.00 USD |
| `7D` | `12.00` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD |
| `1D` | `12.02` | 684,140.00 USD | 684,140.00 USD | 0.00 USD | 94,390.00 USD | 34,630.00 USD | 44,710.00 USD |
| `7D` | `12.02` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD |
| `1D` | `12.04` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 211,740.00 USD | 79,430.00 USD | 108,800.00 USD |
| `7D` | `12.04` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD |
| `1D` | `12.06` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 237,200.00 USD | 89,280.00 USD | 160,340.00 USD |
| `7D` | `12.06` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 234,210.00 USD | 101,560.00 USD | 145,690.00 USD |
| `1D` | `12.08` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 146,690.00 USD | 45,990.00 USD | 60,130.00 USD |
| `7D` | `12.08` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD |
| `1D` | `12.10` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 19,140.00 USD | 14,280.00 USD | 31,090.00 USD |
| `7D` | `12.10` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 132,110.00 USD | 47,150.00 USD | 39,900.00 USD |
| `7D` | `12.12` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 89,810.00 USD | 44,490.00 USD | 95,850.00 USD |
| `1D` | `12.14` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 88,560.00 USD | 28,780.00 USD | 53,490.00 USD |
| `7D` | `12.14` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 118,920.00 USD | 64,740.00 USD | 31,180.00 USD |
| `1D` | `12.16` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 90,620.00 USD | 57,300.00 USD | 64,660.00 USD |
| `7D` | `12.16` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD |
| `1D` | `12.18` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 132,660.00 USD | 47,620.00 USD | 39,310.00 USD |
| `7D` | `12.18` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD |
| `1D` | `12.20` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 89,740.00 USD | 40,990.00 USD | 25,620.00 USD |
| `7D` | `12.20` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD |
| `1D` | `12.22` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 29,450.00 USD | 39,070.00 USD | 34,000.00 USD |
| `7D` | `12.22` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 261,490.00 USD | 19,920.00 USD | 93,540.00 USD |
| `1D` | `12.24` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 35,430.00 USD | 14,730.00 USD | 7,750.00 USD |
| `7D` | `12.24` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD |
| `1D` | `12.26` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 51,100.00 USD | 27,170.00 USD | 21,490.00 USD |
| `7D` | `12.26` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD |
| `1D` | `12.28` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 101,040.00 USD | 24,800.00 USD | 29,770.00 USD |
| `7D` | `12.28` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD |
| `1D` | `12.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 59,030.00 USD | 22,230.00 USD | 42,610.00 USD |
| `7D` | `12.30` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD |
| `1D` | `12.32` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 391.20 USD | 7,100.00 USD | 37.28 USD |
| `7D` | `12.32` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.34` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 29,830.00 USD | 8,560.00 USD | 17,040.00 USD |
| `7D` | `12.34` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 140,600.00 USD | 75,950.00 USD | 13,370.00 USD |
| `1D` | `12.36` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 19,510.00 USD | 9,040.00 USD | 5,420.00 USD |
| `7D` | `12.36` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD |
| `1D` | `12.38` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 29,950.00 USD | 6,420.00 USD | 12,800.00 USD |
| `7D` | `12.38` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD |
| `1D` | `12.40` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 19,630.00 USD | 23,720.00 USD | 22,980.00 USD |
| `7D` | `12.40` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 176,820.00 USD | 40,380.00 USD | 258,110.00 USD |
| `1D` | `12.42` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 51,980.00 USD | 13,980.00 USD | 9,750.00 USD |
| `7D` | `12.42` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 135,510.00 USD | 33,450.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 18,760.00 USD | 10,270.00 USD | 6,490.00 USD |
| `7D` | `12.44` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 159,890.00 USD | 70,960.00 USD | 272,130.00 USD |
| `1D` | `12.46` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 4,980.00 USD | 15,260.00 USD | 11,590.00 USD |
| `7D` | `12.46` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD |
| `1D` | `12.48` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 3,100.00 USD | 2,560.00 USD | 8,380.00 USD |
| `7D` | `12.48` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD |
| `1D` | `12.50` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 1,320.00 USD | 4,320.00 USD | 8,220.00 USD |
| `7D` | `12.50` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD |
| `1D` | `12.52` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 20,590.00 USD | 5,020.00 USD | 12,060.00 USD |
| `7D` | `12.52` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.54` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD |
| `7D` | `12.54` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 96,800.00 USD | 59,960.00 USD | 107,190.00 USD |
| `1D` | `12.56` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD |
| `7D` | `12.56` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD |
| `1D` | `12.58` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 6,740.00 USD | 1,030.00 USD | 11,120.00 USD |
| `7D` | `12.58` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD |
| `1D` | `12.60` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD |
| `7D` | `12.60` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.62` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.64` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 21,870.00 USD | 4,240.00 USD | 7,570.00 USD |
| `7D` | `12.64` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.66` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 648.46 USD | 23.77 USD | 3,290.00 USD |
| `7D` | `12.66` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.68` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 3,670.00 USD | 1,540.00 USD | 7,130.00 USD |
| `7D` | `12.68` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD |
| `1D` | `12.70` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 2,940.00 USD | 1,140.00 USD | 2,780.00 USD |
| `7D` | `12.70` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD |
| `1D` | `12.72` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 24,470.00 USD | 3,750.00 USD | 10,910.00 USD |
| `7D` | `12.72` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD |
| `1D` | `12.74` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 20,500.00 USD | 10,520.00 USD | 15,340.00 USD |
| `7D` | `12.74` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 21,020.00 USD |
| `1D` | `12.76` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 43,450.00 USD | 12,260.00 USD | 18,170.00 USD |
| `7D` | `12.76` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD |
| `1D` | `12.78` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 19,150.00 USD | 3,120.00 USD | 11,190.00 USD |
| `7D` | `12.78` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD |
| `1D` | `12.80` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 12,430.00 USD | 5,860.00 USD | 5,290.00 USD |
| `7D` | `12.80` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.82` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 2,680.00 USD | 1,230.00 USD | 1,980.00 USD |
| `7D` | `12.82` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.84` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 14,360.00 USD | 5,860.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 29,710.00 USD | 15,870.00 USD | 7,710.00 USD |
| `1D` | `12.86` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 19,070.00 USD | 1,990.00 USD | 7,570.00 USD |
| `7D` | `12.86` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD |
| `1D` | `12.88` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 7,890.00 USD | 3,720.00 USD | 8,010.00 USD |
| `7D` | `12.88` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD |
| `1D` | `12.90` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 19,260.00 USD | 7,240.00 USD | 2,960.00 USD |
| `7D` | `12.90` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 41,140.00 USD | 16,610.00 USD | 13,080.00 USD |
| `1D` | `12.92` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 6,680.00 USD | 2,610.00 USD | 1,980.00 USD |
| `1D` | `12.94` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD |
| `1D` | `12.96` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 114.70 USD | 5,090.00 USD | 3,160.00 USD |
| `1D` | `12.98` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 22,080.00 USD | 7,080.00 USD | 8,890.00 USD |
| `1D` | `13.00` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD |
| `1D` | `13.02` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD |
| `1D` | `13.04` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD |
| `1D` | `13.06` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 9,530.00 USD | 1,380.00 USD | 1,550.00 USD |
| `1D` | `13.08` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 7,640.00 USD | 2,280.00 USD | 0.00 USD |
| `1D` | `13.10` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 6,340.00 USD | 5,500.00 USD | 7,330.00 USD |
| `1D` | `13.12` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 11,610.00 USD | 8,380.00 USD | 7,170.00 USD |
| `1D` | `13.14` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 6,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `13.16` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 4,170.00 USD | 4,090.00 USD | 2,560.00 USD |
| `1D` | `13.18` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 4,870.00 USD | 2,940.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `564.38M` | Total OI Tokens: `47,834,333.3 LINK`
  * 1h OI Change: `-1.30%` | 4h OI Change: `+1.52%` | 24h OI Change: `+0.91%`
  * Exchange Breakdown: Binance=`107.29M` | Bybit=`66.29M` | OKX=`26.83M` | Hyperliquid=`57.60M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `18.65K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `41.83%` | `58.17%` | `0.72` | 816,660.00 USD |
| `15M` | `Binance` | `37.8%` | `62.2%` | `0.61` | 429,300.00 USD |
| `15M` | `OKX` | `36.21%` | `63.79%` | `0.57` | 72,800.00 USD |
| `15M` | `Bybit` | `26.03%` | `73.97%` | `0.35` | 38,630.00 USD |
| `15M` | `KuCoin` | `43.46%` | `56.54%` | `0.77` | 19,140.00 USD |
| `15M` | `Gate` | `50.73%` | `49.27%` | `1.03` | 31,120.00 USD |
| `15M` | `Bitget` | `19.75%` | `80.25%` | `0.25` | 25,590.00 USD |
| `15M` | `BingX` | `60.63%` | `39.37%` | `1.54` | 34,220.00 USD |
| `15M` | `MEXC` | `49.27%` | `50.73%` | `0.97` | 4,400.00 USD |
| `15M` | `Bitunix` | `43.06%` | `56.94%` | `0.76` | 12,110.00 USD |
| `15M` | `Hyperliquid` | `70.5%` | `29.5%` | `2.39` | 6,030.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.09%` | `56.91%` | `0.76` | 31,280.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 81,860.00 USD |
| `15M` | `HTX` | `85.46%` | `14.54%` | `5.88` | 12,420.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `36.44%` | `63.56%` | `0.57` | 10,040.00 USD |
| `15M` | `Aster` | `1.96%` | `98.04%` | `0.02` | 4,830.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 2,870.00 USD |
| `15M` | `Whale Positions` | `37.8%` | `62.2%` | `0.61` | 429,300.00 USD |
| `15M` | `Global Accounts` | `41.83%` | `58.17%` | `0.72` | 816,660.00 USD |
| `1H` | `LINK` | `46.35%` | `53.65%` | `0.86` | 27,850,000.00 USD |
| `1H` | `Binance` | `51.44%` | `48.56%` | `1.06` | 9,780,000.00 USD |
| `1H` | `OKX` | `38.04%` | `61.96%` | `0.61` | 2,230,000.00 USD |
| `1H` | `Bybit` | `41.03%` | `58.97%` | `0.70` | 1,710,000.00 USD |
| `1H` | `KuCoin` | `42.15%` | `57.85%` | `0.73` | 161,060.00 USD |
| `1H` | `Gate` | `51.86%` | `48.14%` | `1.08` | 1,390,000.00 USD |
| `1H` | `Bitget` | `38.31%` | `61.69%` | `0.62` | 1,170,000.00 USD |
| `1H` | `BingX` | `26.76%` | `73.24%` | `0.37` | 2,230,000.00 USD |
| `1H` | `MEXC` | `50.71%` | `49.29%` | `1.03` | 3,390,000.00 USD |
| `1H` | `Bitunix` | `45.59%` | `54.41%` | `0.84` | 526,670.00 USD |
| `1H` | `Hyperliquid` | `42.85%` | `57.15%` | `0.75` | 115,860.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.74%` | `48.26%` | `1.07` | 4,560,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.45%` | `91.55%` | `0.09` | 337,190.00 USD |
| `1H` | `HTX` | `47.19%` | `52.81%` | `0.89` | 88,380.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.42%` | `64.58%` | `0.55` | 138,570.00 USD |
| `1H` | `Aster` | `49.51%` | `50.49%` | `0.98` | 4,950.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.88%` | `68.12%` | `0.47` | 31,210.00 USD |
| `1H` | `Whale Positions` | `51.44%` | `48.56%` | `1.06` | 9,780,000.00 USD |
| `1H` | `Global Accounts` | `46.35%` | `53.65%` | `0.86` | 27,850,000.00 USD |
| `4H` | `LINK` | `45.49%` | `54.51%` | `0.83` | 22,100,000.00 USD |
| `4H` | `Binance` | `50.48%` | `49.52%` | `1.02` | 8,020,000.00 USD |
| `4H` | `OKX` | `44.7%` | `55.3%` | `0.81` | 1,580,000.00 USD |
| `4H` | `Bybit` | `44.14%` | `55.86%` | `0.79` | 1,190,000.00 USD |
| `4H` | `KuCoin` | `48.27%` | `51.73%` | `0.93` | 322,470.00 USD |
| `4H` | `Gate` | `33.25%` | `66.75%` | `0.50` | 2,860,000.00 USD |
| `4H` | `Bitget` | `32.37%` | `67.63%` | `0.48` | 666,210.00 USD |
| `4H` | `BingX` | `23.15%` | `76.85%` | `0.30` | 1,200,000.00 USD |
| `4H` | `MEXC` | `73.01%` | `26.99%` | `2.71` | 324,740.00 USD |
| `4H` | `Bitunix` | `47.41%` | `52.59%` | `0.90` | 245,590.00 USD |
| `4H` | `Hyperliquid` | `72.29%` | `27.71%` | `2.61` | 695,920.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.39%` | `49.61%` | `1.02` | 2,780,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `35.19%` | `64.81%` | `0.54` | 1,590,000.00 USD |
| `4H` | `HTX` | `50.89%` | `49.11%` | `1.04` | 215,560.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `66.19%` | `33.81%` | `1.96` | 251,020.00 USD |
| `4H` | `Aster` | `50.21%` | `49.79%` | `1.01` | 38,220.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.23%` | `50.77%` | `0.97` | 106,480.00 USD |
| `4H` | `Whale Positions` | `50.48%` | `49.52%` | `1.02` | 8,020,000.00 USD |
| `4H` | `Global Accounts` | `45.49%` | `54.51%` | `0.83` | 22,100,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.80` | `11.86` | `11.80` | `11.93` | `11.78` | 3,070,588.90 USD | 1,729,988.81 USD | 1,340,600.08 USD | 389,388.73 USD | `+12.68%` | `40B / 15S` |
| `5:00 UTC` | `11.89` | `11.88` | `11.89` | `11.94` | `11.84` | 2,496,218.56 USD | 1,096,746.34 USD | 1,399,472.22 USD | -302,725.88 USD | `-12.13%` | `13B / 26S` |
| `0:00 UTC` | `11.92` | `11.91` | `11.92` | `11.94` | `11.85` | 1,819,989.69 USD | 1,006,576.04 USD | 813,413.65 USD | 193,162.38 USD | `+10.61%` | `19B / 6S` |
| `5:00 UTC` | `11.96` | `11.95` | `11.96` | `11.97` | `11.91` | 1,967,082.63 USD | 985,939.71 USD | 981,142.92 USD | 4,796.79 USD | `+0.24%` | `10B / 4S` |
| `0:00 UTC` | `11.96` | `11.96` | `11.96` | `12.01` | `11.92` | 3,381,108.22 USD | 1,759,295.98 USD | 1,621,812.25 USD | 137,483.73 USD | `+4.07%` | `18B / 11S` |
| `5:00 UTC` | `11.90` | `11.91` | `11.90` | `11.96` | `11.87` | 2,958,884.05 USD | 1,214,340.67 USD | 1,744,543.38 USD | -530,202.70 USD | `-17.92%` | `12B / 26S` |
| `0:00 UTC` | `11.86` | `11.86` | `11.86` | `11.91` | `11.82` | 2,416,227.23 USD | 1,033,147.61 USD | 1,383,079.61 USD | -349,932.00 USD | `-14.48%` | `6B / 27S` |
| `5:00 UTC` | `11.84` | `11.85` | `11.84` | `11.87` | `11.83` | 923,896.67 USD | 361,612.35 USD | 562,284.32 USD | -200,671.96 USD | `-21.72%` | `4B / 14S` |
| `0:00 UTC` | `11.83` | `11.83` | `11.83` | `11.87` | `11.79` | 1,261,426.96 USD | 528,120.38 USD | 733,306.58 USD | -205,186.20 USD | `-16.27%` | `8B / 14S` |
| `5:00 UTC` | `11.80` | `11.80` | `11.80` | `11.81` | `11.79` | 539,459.77 USD | 264,359.91 USD | 275,099.86 USD | -10,739.95 USD | `-1.99%` | `6B / 1S` |

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
| `5m` | -22,140.00 USD | -350,340.00 USD | **`DISTRIBUTION`** |
| `15m` | -38,280.00 USD | -790,910.00 USD | **`DISTRIBUTION`** |
| `30m` | -334,750.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -56,000.00 USD | -2,370,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 322,670.00 USD | -1,710,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,140,000.00 USD | 219,830.00 USD | **`ACCUMULATION`** |
| `6h` | 913,280.00 USD | 14,170.00 USD | **`ACCUMULATION`** |
| `8h` | 1,080,000.00 USD | 927,290.00 USD | **`ACCUMULATION`** |
| `12h` | 1,100,000.00 USD | -84,030.00 USD | **`ACCUMULATION`** |
| `24h` | 1,260,000.00 USD | 134,390.00 USD | **`ACCUMULATION`** |
| `1w` | -7,820,000.00 USD | -21,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -70,410,000.00 USD | -182,240,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-22.14K` | 15m=`-38.28K` | 1h=`-56.00K` | 24h=`+1.26M`
* Futures Capital Netflows: 5m=`-350.34K` | 15m=`-790.91K` | 1h=`-2.37M` | 24h=`+134.39K`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.10` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `14.75`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `13.25` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `8.60`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
