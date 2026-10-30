# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 08:15:37 IST` (`2026-10-30 02:45:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.66` | **Live Ask Quote**: `10.74` | **Mid Price**: `10.70`
- **Spread Points**: `85.00` | **Spread BPS**: `79.43 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.45` | VWAP Z-Score: `+2.17` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1409` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `43.24` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `10.70` | Lower -3.00σ Band: `10.19`
  * Upper +2.51σ Band: `10.66` | Lower -2.51σ Band: `10.23`
  * Upper +2.01σ Band: `10.62` | Lower -2.01σ Band: `10.27`
  * Upper +2.00σ Band: `10.62` | Lower -2.00σ Band: `10.28`
  * Upper +1.28σ Band: `10.56` | Lower -1.28σ Band: `10.34`
  * Upper +1.00σ Band: `10.53` | Lower -1.00σ Band: `10.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.53` | EMA-20=`10.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.01` (Slope: `+0.0000`) | EMA-100=`11.23`
  * Institutional Anchors: EMA-144=`11.31` | EMA-200=`11.35` (Slope: `-0.9620`) | EMA-233=`11.37`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.79` (Distance: `-0.77%`)
  * Point of Control (POC) = `10.48` (Distance: `+2.11%`)
  * Value Area Low (VAL) = `10.22` (Distance: `+4.75%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.70` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`10.74` | Low=`10.66`
  * New York Session (13:00-21:00 UTC): High=`10.77` | Low=`10.64`
  * Initial Balance (First Hour): IB High=`10.73` | IB Low=`10.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.66` - `10.74`
  * Optimal Trade Entry (OTE 0.705): `10.72`
  * Structural Invalidation Anchor (0.786): `10.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.69` | `10.72` | `10.66` | `10.67` | `110,663` | 1,183,759.17 USD | -324,824.65 USD | `-27.44%` | -13,656,599.52 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.67` | `10.73` | `10.67` | `10.73` | `70,302` | 752,980.88 USD | 62,340.29 USD | `+8.28%` | -13,594,259.23 USD | `+0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `10.73` | `10.74` | `10.71` | `10.72` | `23,373` | 250,714.51 USD | -2,743.59 USD | `-1.09%` | -13,597,002.82 USD | `-0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `10.52` | `10.58` | `10.47` | `10.58` | `433,631` | 4,555,787.03 USD | -680,504.09 USD | `-14.94%` | -15,406,689.43 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `10.57` | `10.72` | `10.57` | `10.69` | `758,601` | 8,088,225.29 USD | 2,074,914.56 USD | `+25.65%` | -13,331,774.86 USD | `+1.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `10.69` | `10.74` | `10.66` | `10.72` | `204,338` | 2,187,454.56 USD | -265,227.96 USD | `-12.12%` | -13,597,002.82 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `10.61` | `10.65` | `10.25` | `10.50` | `3,619,167` | 37,791,802.16 USD | -189,145.75 USD | `-0.50%` | -14,965,278.40 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `10.50` | `10.64` | `10.41` | `10.52` | `1,696,592` | 17,877,795.02 USD | -222,167.06 USD | `-1.24%` | -15,187,445.46 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `10.52` | `10.74` | `10.47` | `10.72` | `1,396,538` | 14,831,116.56 USD | 1,128,832.19 USD | `+7.61%` | -14,058,613.27 USD | `+0.82` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.74` | `10.25` | `10.72` | `6,712,297` | 70,500,713.74 USD | 717,519.38 USD | `+1.02%` | -13,168,005.20 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | 329,195.75 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,661,099.58 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.74` | `10.25` | `10.72` | `6,712,297` | 70,500,713.74 USD | 717,519.38 USD | `+1.02%` | -13,168,005.20 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`10.70`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `421` | `0xecb6...2b00` | `SHORT` | 5,112,240.82 USD | `476,488,100.00` | `10.66` | `10.73` | `68.47` | -33,519.83 USD | `-0.66%` | `10X Cross` |
| `515` | `0x73ce...8ce9` | `LONG` | 4,291,016.44 USD | `400,011,600.00` | `12.05` | `10.73` | `7.82` | -528,737.27 USD | `-12.32%` | `5X Cross` |
| `870` | `0xb83d...6e36` | `SHORT` | 2,596,129.11 USD | `242,013,000.00` | `12.93` | `10.73` | `563.41` | 533,765.08 USD | `+20.56%` | `3X Cross` |
| `920` | `0x458d...ab3b` | `LONG` | 2,436,482.76 USD | `227,156,700.00` | `13.13` | `10.73` | `9.34` | -545,747.63 USD | `-22.40%` | `3X Isolated` |
| `991` | `0xdd53...2b13` | `SHORT` | 2,214,908.03 USD | `206,475,300.00` | `11.92` | `10.73` | `312.23` | 246,314.89 USD | `+11.12%` | `3X Cross` |
| `1016` | `0x3dc9...54b0` | `SHORT` | 2,145,400.00 USD | `200,000,000.00` | `7.56` | `10.73` | `98.42` | -634,241.58 USD | `-29.56%` | `10X Cross` |
| `1029` | `0x45d2...4029` | `SHORT` | 2,096,737.50 USD | `195,500,000.00` | `11.54` | `10.73` | `225.96` | 159,745.93 USD | `+7.62%` | `10X Cross` |
| `1203` | `0x6540...f7b7` | `LONG` | 1,822,391.52 USD | `169,935,800.00` | `12.40` | `10.73` | `6.69` | -285,368.48 USD | `-15.66%` | `5X Isolated` |
| `1276` | `0xeadc...9d55` | `LONG` | 1,691,400.10 USD | `157,691,600.00` | `9.43` | `10.73` | `0.000000` | 204,745.20 USD | `+12.11%` | `10X Cross` |
| `1519` | `0x5b5d...c060` | `SHORT` | 1,413,424.01 USD | `131,775,500.00` | `13.61` | `10.73` | `1245.50` | 379,833.96 USD | `+26.87%` | `3X Cross` |
| `1686` | `0xf6f3...47f8` | `SHORT` | 1,234,328.98 USD | `115,024,600.00` | `11.42` | `10.73` | `19.67` | 79,001.20 USD | `+6.40%` | `5X Cross` |
| `1745` | `0x9df2...c665` | `SHORT` | 1,178,156.85 USD | `109,810,500.00` | `11.48` | `10.73` | `295.14` | 82,578.28 USD | `+7.01%` | `10X Cross` |
| `1861` | `0xfe7e...11b4` | `LONG` | 1,084,161.33 USD | `101,142,000.00` | `14.47` | `10.73` | `5.32` | -378,951.82 USD | `-34.95%` | `5X Isolated` |
| `1886` | `0x8af7...fa05` | `SHORT` | 1,058,075.27 USD | `98,661,200.00` | `14.08` | `10.73` | `203.70` | 331,107.27 USD | `+31.29%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.77` | 7,505.19 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,466.45 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |
| `ANNOUNCEMENT` | `INFO` | `11.98` | 92.24 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.09K USD at 11.9790 USD [API] | `2026-10-28 20:01:53` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 7,028.87 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.03K USD at 11.7520 USD [API] | `2026-10-28 20:24:25` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 5,465.39 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.7510 USD [API] | `2026-10-28 20:24:25` |
| `ANNOUNCEMENT` | `INFO` | `11.76` | 9,227.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 9.23K USD at 11.7580 USD [API] | `2026-10-28 20:34:32` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,466.99 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8410 USD [API] | `2026-10-28 22:04:16` |
| `ANNOUNCEMENT` | `INFO` | `11.80` | 5,566.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.57K USD at 11.8030 USD [API] | `2026-10-28 22:22:09` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 5,465.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8230 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 10,243.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 10.24K USD at 11.8220 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 5,407.38 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.41K USD at 11.8220 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 7,904.59 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.90K USD at 11.8120 USD [API] | `2026-10-28 23:00:04` |
| `ANNOUNCEMENT` | `INFO` | `11.78` | 7,973.56 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.97K USD at 11.7830 USD [API] | `2026-10-28 23:01:30` |
| `ANNOUNCEMENT` | `INFO` | `11.80` | 9,848.97 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 9.85K USD at 11.7980 USD [API] | `2026-10-28 23:32:10` |
| `ANNOUNCEMENT` | `INFO` | `11.80` | 6,665.87 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.7980 USD [API] | `2026-10-28 23:32:10` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.09%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`11.11` (Vol: 502,000.00 USD, Dist: `+4.59%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.15` | 803.03 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 1,290.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 349.62 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 1,220.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 55,600.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 2,750.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 4,510.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 18,570.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,600.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 969.15 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,110.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 33,910.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 10,970.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,470.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 4,950.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 26,250.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 1,080.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 9,600.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 505.47 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 4,250.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 8,690.00 USD | 11,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 5,180.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 243,430.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 3,750.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 4,360.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 634,050.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 302.48 USD | 10,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 10,630.00 USD | 10,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 38,610.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 63,790.00 USD | 10,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 2,250.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 23,230.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 37,790.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 61,990.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 25,420.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 32,490.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 15,600.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 69,740.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,170,000.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 12,900.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 11,910.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 30,710.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 30,290.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 11,130.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 19,400.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 7,290.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 8,670.00 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 25,070.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,830.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 1,030.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 19,280.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 65,130.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 77,060.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 199,340.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 2,410.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 33,290.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 72,470.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 359,190.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 26,330.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 57,530.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 451,980.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 145,160.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 79,320.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,690.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.45` | 4,750,000.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 48,080.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.47` | 4,730,000.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.53` | 4,730,000.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.55` | 4,720,000.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 53,010.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.57` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 1,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.57` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.59` | 4,700,000.00 USD | 4,700,000.00 USD | 40,390.00 USD | 6,150.00 USD | 34,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 6,330,000.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.61` | 4,620,000.00 USD | 4,620,000.00 USD | 1,090.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.63` | 4,610,000.00 USD | 4,610,000.00 USD | 671.70 USD | 0.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 6,320,000.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.65` | 4,600,000.00 USD | 4,600,000.00 USD | 972.50 USD | 0.00 USD | 105.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 6,300,000.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 205,310.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.67` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.67` | 6,290,000.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.69` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 6,290,000.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.71` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.73` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.75` | 4,520,000.00 USD | 4,520,000.00 USD | 40,030.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 6,220,000.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 83,560.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.77` | 4,460,000.00 USD | 4,460,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.77` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.79` | 4,320,000.00 USD | 4,320,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 6,110,000.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.81` | 4,310,000.00 USD | 4,310,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 6,060,000.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 4,210,000.00 USD | 4,210,000.00 USD | 37,110.00 USD | 0.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 5,960,000.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.85` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 5,910,000.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 82,350.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 4,160,000.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 4,140,000.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 4,110,000.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 4,090,000.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 443,340.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 4,060,000.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 4,030,000.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 4,030,000.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 4,030,000.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 792,240.00 USD | 880,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 4,020,000.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 4,010,000.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 4,000,000.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 60,550.00 USD | 87,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.17` | 3,990,000.00 USD | 3,990,000.00 USD | 3,600.00 USD | 17,840.00 USD | 424.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 5,640,000.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 3,970,000.00 USD | 3,970,000.00 USD | 3,360.00 USD | 15,950.00 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 5,540,000.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 3,950,000.00 USD | 3,950,000.00 USD | 39,570.00 USD | 17,890.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 5,490,000.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 3,850,000.00 USD | 3,850,000.00 USD | 111,870.00 USD | 20,390.00 USD | 153,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 5,380,000.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 3,570,000.00 USD | 3,570,000.00 USD | 26,800.00 USD | 19,590.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 5,080,000.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 27,350.00 USD | 27,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.27` | 3,510,000.00 USD | 3,510,000.00 USD | 18,050.00 USD | 11,470.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 4,960,000.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 3,440,000.00 USD | 3,440,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 4,780,000.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 3,400,000.00 USD | 3,400,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 4,690,000.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 3,300,000.00 USD | 3,300,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 4,490,000.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 3,220,000.00 USD | 3,220,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 4,290,000.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.37` | 3,160,000.00 USD | 3,160,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 4,220,000.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 3,080,000.00 USD | 3,080,000.00 USD | 7,450.00 USD | 41,060.00 USD | 44,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 4,100,000.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 2,980,000.00 USD | 2,980,000.00 USD | 259,620.00 USD | 45,690.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 4,030,000.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 2,590,000.00 USD | 2,590,000.00 USD | 248,090.00 USD | 62,710.00 USD | 71,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 3,690,000.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 2,210,000.00 USD | 2,210,000.00 USD | 332,800.00 USD | 44,610.00 USD | 277,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 3,620,000.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.47` | 1,550,000.00 USD | 1,550,000.00 USD | 219,660.00 USD | 80,860.00 USD | 77,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 3,320,000.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 1,170,000.00 USD | 1,170,000.00 USD | 124,820.00 USD | 26,560.00 USD | 88,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 3,010,000.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 933,190.00 USD | 933,190.00 USD | 27,700.00 USD | 6,670.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 2,820,000.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 885,260.00 USD | 885,260.00 USD | 43,880.00 USD | 39,730.00 USD | 117,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 2,730,000.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 684,070.00 USD | 684,070.00 USD | 7,160.00 USD | 517.73 USD | 56,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 2,660,000.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.57` | 620,110.00 USD | 620,110.00 USD | 52,260.00 USD | 287.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 2,400,000.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 453,270.00 USD | 453,270.00 USD | 48,700.00 USD | 615.80 USD | 172,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 2,250,000.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 231,530.00 USD | 231,530.00 USD | 231,310.00 USD | 17.90 USD | 210.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 2,000,000.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.63` | 301,170.00 USD | 301,170.00 USD | 301,120.00 USD | 0.00 USD | 51.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 1,460,000.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.65` | 301,820.00 USD | 301,820.00 USD | 644.06 USD | 0.00 USD | 0.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 1,360,000.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.67` | 301,830.00 USD | 301,830.00 USD | 0.00 USD | 0.00 USD | 10.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 1,290,000.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.69` | 423,930.00 USD | 423,930.00 USD | 122,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 801,310.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.71` | 646,780.00 USD | 646,780.00 USD | 219,090.00 USD | 25.97 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 323,480.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.73` | 656,610.00 USD | 656,610.00 USD | 6,180.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 29,560.00 USD | 29,560.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 59,120.00 USD | 59,120.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.75` | 746,660.00 USD | 746,660.00 USD | 89,590.00 USD | 430.90 USD | 20.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.75` | 77,290.00 USD | 77,290.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.77` | 756,060.00 USD | 756,060.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.77` | 98,870.00 USD | 98,870.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.79` | 929,710.00 USD | 929,710.00 USD | 88,000.00 USD | 85,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.79` | 192,270.00 USD | 192,270.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.81` | 992,460.00 USD | 992,460.00 USD | 0.00 USD | 62,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.83` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 34,810.00 USD | 50,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.85` | 1,180,000.00 USD | 1,180,000.00 USD | 75,750.00 USD | 26,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.85` | 1,090.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 1,400.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.97` | 1,980,000.00 USD | 1,980,000.00 USD | 124.21 USD | 15,600.00 USD | 54,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.97` | 240,550.00 USD | 240,550.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.99` | 1,980,000.00 USD | 1,980,000.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 413,570.00 USD | 413,570.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.01` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 17,840.00 USD | 106,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 424,150.00 USD | 424,150.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.03` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 15,920.00 USD | 145,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 576,560.00 USD | 576,560.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.05` | 2,550,000.00 USD | 2,550,000.00 USD | 192,840.00 USD | 1,480.00 USD | 90,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 966,150.00 USD | 966,150.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.05` | 1,220.00 USD | 3,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.07` | 3,140,000.00 USD | 3,140,000.00 USD | 473,120.00 USD | 32,310.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 973,650.00 USD | 973,650.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 3,580,000.00 USD | 3,580,000.00 USD | 227,910.00 USD | 46,680.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 981,150.00 USD | 981,150.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 3,850,000.00 USD | 3,850,000.00 USD | 216,430.00 USD | 37,650.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 4,520,000.00 USD | 4,520,000.00 USD | 408,510.00 USD | 91,630.00 USD | 167,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 4,720,000.00 USD | 4,720,000.00 USD | 194,240.00 USD | 11,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 2,100.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.17` | 4,850,000.00 USD | 4,850,000.00 USD | 165.70 USD | 69,930.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 5,020,000.00 USD | 5,020,000.00 USD | 72,110.00 USD | 63,920.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 5,250,000.00 USD | 5,250,000.00 USD | 114,530.00 USD | 425.43 USD | 116,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 5,550,000.00 USD | 5,550,000.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 5,830,000.00 USD | 5,830,000.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.27` | 6,320,000.00 USD | 6,320,000.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 6,820,000.00 USD | 6,820,000.00 USD | 165,410.00 USD | 123,030.00 USD | 213,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 7,030,000.00 USD | 7,030,000.00 USD | 63,250.00 USD | 67,150.00 USD | 79,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 7,300,000.00 USD | 7,300,000.00 USD | 198,020.00 USD | 38,820.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 7,790,000.00 USD | 7,790,000.00 USD | 297,850.00 USD | 124,090.00 USD | 66,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 58,900.00 USD | 64,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.37` | 8,040,000.00 USD | 8,040,000.00 USD | 150,920.00 USD | 78,610.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 8,090,000.00 USD | 8,090,000.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 8,360,000.00 USD | 8,360,000.00 USD | 95,030.00 USD | 34,780.00 USD | 140,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 8,520,000.00 USD | 8,520,000.00 USD | 52,230.00 USD | 26,360.00 USD | 88,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 8,640,000.00 USD | 8,640,000.00 USD | 46,070.00 USD | 69,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 1,060.00 USD | 65,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.47` | 8,730,000.00 USD | 8,730,000.00 USD | 48,370.00 USD | 19,590.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 8,820,000.00 USD | 8,820,000.00 USD | 33,390.00 USD | 22,330.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 8,920,000.00 USD | 8,920,000.00 USD | 41,360.00 USD | 28,330.00 USD | 30,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 9,000,000.00 USD | 9,000,000.00 USD | 32,640.00 USD | 16,860.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 9,040,000.00 USD | 9,040,000.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 143.22 USD | 65,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.57` | 9,150,000.00 USD | 9,150,000.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 9,210,000.00 USD | 9,210,000.00 USD | 15,100.00 USD | 7,660.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 9,440,000.00 USD | 9,440,000.00 USD | 153,200.00 USD | 0.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 9,450,000.00 USD | 9,450,000.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 9,460,000.00 USD | 9,460,000.00 USD | 1,410.00 USD | 7,130.00 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 485.81 USD | 66,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.67` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 6,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 9,560,000.00 USD | 9,560,000.00 USD | 59,600.00 USD | 29,410.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 9,710,000.00 USD | 9,710,000.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 9,930,000.00 USD | 9,930,000.00 USD | 138,580.00 USD | 5,720.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 10,050,000.00 USD | 10,050,000.00 USD | 21,990.00 USD | 35,620.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 10,120,000.00 USD | 10,120,000.00 USD | 41,180.00 USD | 18,670.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 10,180,000.00 USD | 10,180,000.00 USD | 12,080.00 USD | 755.20 USD | 40,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 17,960.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 10,270,000.00 USD | 10,270,000.00 USD | 11,070.00 USD | 11,510.00 USD | 29,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 10,450,000.00 USD | 10,450,000.00 USD | 76,700.00 USD | 22,590.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 10,550,000.00 USD | 10,550,000.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 10,650,000.00 USD | 10,650,000.00 USD | 44,160.00 USD | 11,410.00 USD | 43,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 10,800,000.00 USD | 10,800,000.00 USD | 102,960.00 USD | 18,340.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 10,990,000.00 USD | 10,990,000.00 USD | 135,130.00 USD | 28,540.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 11,140,000.00 USD | 11,140,000.00 USD | 85,850.00 USD | 21,080.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 11,350,000.00 USD | 11,350,000.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 11,550,000.00 USD | 11,550,000.00 USD | 123,700.00 USD | 25,870.00 USD | 46,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 11,670,000.00 USD | 11,670,000.00 USD | 60,120.00 USD | 9,410.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 11,830,000.00 USD | 11,830,000.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 12,170,000.00 USD | 12,170,000.00 USD | 206,510.00 USD | 58,260.00 USD | 81,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 12,440,000.00 USD | 12,440,000.00 USD | 114,130.00 USD | 53,190.00 USD | 97,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 12,490,000.00 USD | 12,490,000.00 USD | 17,390.00 USD | 18,490.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 12,680,000.00 USD | 12,680,000.00 USD | 94,540.00 USD | 34,950.00 USD | 55,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 12,850,000.00 USD | 12,850,000.00 USD | 94,650.00 USD | 33,860.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 13,070,000.00 USD | 13,070,000.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,270.00 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.17` | 13,330,000.00 USD | 13,330,000.00 USD | 122,970.00 USD | 64,130.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 13,430,000.00 USD | 13,430,000.00 USD | 64,080.00 USD | 24,200.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 13,560,000.00 USD | 13,560,000.00 USD | 52,950.00 USD | 28,750.00 USD | 50,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 13,600,000.00 USD | 13,600,000.00 USD | 14,580.00 USD | 24,000.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 13,620,000.00 USD | 13,620,000.00 USD | 2,260.00 USD | 5,380.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 69,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.27` | 13,700,000.00 USD | 13,700,000.00 USD | 52,420.00 USD | 9,580.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 13,790,000.00 USD | 13,790,000.00 USD | 36,110.00 USD | 19,760.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 13,820,000.00 USD | 13,820,000.00 USD | 19,750.00 USD | 4,850.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 13,830,000.00 USD | 13,830,000.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 13,870,000.00 USD | 13,870,000.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 69,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.37` | 13,890,000.00 USD | 13,890,000.00 USD | 8,820.00 USD | 5,700.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 13,950,000.00 USD | 13,950,000.00 USD | 28,430.00 USD | 12,560.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 14,040,000.00 USD | 14,040,000.00 USD | 42,540.00 USD | 19,990.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 14,070,000.00 USD | 14,070,000.00 USD | 23,090.00 USD | 5,940.00 USD | 88.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 14,090,000.00 USD | 14,090,000.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 12,000.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 380.27 USD | 70,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 70,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.67` | 19,800,000.00 USD | 19,800,000.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 20,040,000.00 USD | 20,040,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 20,130,000.00 USD | 20,130,000.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 20,220,000.00 USD | 20,220,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 20,290,000.00 USD | 20,290,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 20,380,000.00 USD | 20,380,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 20,470,000.00 USD | 20,470,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 20,490,000.00 USD | 20,490,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 20,520,000.00 USD | 20,520,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 20,600,000.00 USD | 20,600,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 70,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.87` | 20,640,000.00 USD | 20,640,000.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 20,730,000.00 USD | 20,730,000.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 20,840,000.00 USD | 20,840,000.00 USD | 59,260.00 USD | 15,540.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 20,870,000.00 USD | 20,870,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 20,890,000.00 USD | 20,890,000.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 20,930,000.00 USD | 20,930,000.00 USD | 13,890.00 USD | 10,560.00 USD | 24,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 21,000,000.00 USD | 21,000,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 21,050,000.00 USD | 21,050,000.00 USD | 26,320.00 USD | 2,920.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 21,060,000.00 USD | 21,060,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 21,060,000.00 USD | 21,060,000.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.07` | 21,110,000.00 USD | 21,110,000.00 USD | 23,750.00 USD | 6,890.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 21,130,000.00 USD | 21,130,000.00 USD | 16,060.00 USD | 527.72 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 21,160,000.00 USD | 21,160,000.00 USD | 19,270.00 USD | 5,960.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 21,180,000.00 USD | 21,180,000.00 USD | 13,360.00 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.17` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 21,200,000.00 USD | 21,200,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 21,230,000.00 USD | 21,230,000.00 USD | 13,890.00 USD | 6,210.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 21,240,000.00 USD | 21,240,000.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 21,300,000.00 USD | 21,300,000.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.25` | 1,870.00 USD | 72,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 158.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 78,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.75` | 339.62 USD | 78,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 692.50 USD | 79,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 79,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,490.00 USD | 105,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.05` | 62,090.00 USD | 167,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 167,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 158.07 USD | 167,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 168,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 362.06 USD | 168,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 170,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,190.00 USD | 184,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 91,200.00 USD | 275,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 355,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 356,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 18,250.00 USD | 374,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 11,150.00 USD | 386,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 673,370.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 254,100.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 28,240.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 5,950.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 752.32 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 127.05 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 29,470.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 820,330.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 42,180.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 77,320.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 637.59 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,450.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.25` | 261.23 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 2,340,000.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,460.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 2,440.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.15` | 11,490,000.00 USD | 0.00 USD | 803.03 USD | `-79.56%` | `373,500.00` |
| `Live` | `Long` | `2.25` | 11,490,000.00 USD | 0.00 USD | 1,290.00 USD | `-78.61%` | `572,300.00` |
| `Live` | `Long` | `2.45` | 11,490,000.00 USD | 0.00 USD | 349.62 USD | `-76.71%` | `142,700.00` |
| `Live` | `Long` | `2.55` | 11,490,000.00 USD | 0.00 USD | 1,220.00 USD | `-75.76%` | `476,900.00` |
| `Live` | `Long` | `2.65` | 11,490,000.00 USD | 0.00 USD | 55,600.00 USD | `-74.81%` | `20,979,500.00` |
| `Live` | `Long` | `2.75` | 11,430,000.00 USD | 0.00 USD | 2,750.00 USD | `-73.86%` | `1,000,000.00` |
| `Live` | `Long` | `2.85` | 11,430,000.00 USD | 0.00 USD | 4,510.00 USD | `-72.91%` | `1,581,000.00` |
| `Live` | `Long` | `2.95` | 11,430,000.00 USD | 0.00 USD | 18,570.00 USD | `-71.96%` | `6,295,500.00` |
| `Live` | `Long` | `3.05` | 11,410,000.00 USD | 0.00 USD | 6,600.00 USD | `-71.01%` | `2,164,400.00` |
| `Live` | `Long` | `3.15` | 11,400,000.00 USD | 0.00 USD | 297.99 USD | `-70.06%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 11,400,000.00 USD | 0.00 USD | 969.15 USD | `-69.11%` | `298,200.00` |
| `Live` | `Long` | `3.35` | 11,400,000.00 USD | 0.00 USD | 2,110.00 USD | `-68.16%` | `629,300.00` |
| `Live` | `Long` | `3.45` | 11,400,000.00 USD | 0.00 USD | 33,910.00 USD | `-67.21%` | `9,829,500.00` |
| `Live` | `Long` | `3.55` | 11,360,000.00 USD | 0.00 USD | 126.73 USD | `-66.26%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 11,360,000.00 USD | 0.00 USD | 10,970.00 USD | `-65.31%` | `3,004,300.00` |
| `Live` | `Long` | `3.75` | 11,350,000.00 USD | 0.00 USD | 1,470.00 USD | `-64.36%` | `392,000.00` |
| `Live` | `Long` | `3.85` | 11,350,000.00 USD | 0.00 USD | 4,950.00 USD | `-63.41%` | `1,287,000.00` |
| `Live` | `Long` | `3.95` | 11,350,000.00 USD | 0.00 USD | 26,250.00 USD | `-62.46%` | `6,646,200.00` |
| `Live` | `Long` | `4.05` | 11,320,000.00 USD | 0.00 USD | 1,080.00 USD | `-61.51%` | `266,900.00` |
| `Live` | `Long` | `4.25` | 11,320,000.00 USD | 0.00 USD | 9,600.00 USD | `-59.60%` | `2,258,800.00` |
| `Live` | `Long` | `4.35` | 11,310,000.00 USD | 0.00 USD | 505.47 USD | `-58.65%` | `116,200.00` |
| `Live` | `Long` | `4.45` | 11,310,000.00 USD | 0.00 USD | 381.37 USD | `-57.70%` | `85,700.00` |
| `Live` | `Long` | `4.65` | 11,310,000.00 USD | 0.00 USD | 4,250.00 USD | `-55.80%` | `913,700.00` |
| `Live` | `Long` | `4.75` | 11,300,000.00 USD | 0.00 USD | 8,690.00 USD | `-54.85%` | `1,830,000.00` |
| `Live` | `Long` | `4.85` | 11,290,000.00 USD | 0.00 USD | 5,180.00 USD | `-53.90%` | `1,067,300.00` |
| `Live` | `Long` | `4.95` | 11,290,000.00 USD | 0.00 USD | 243,430.00 USD | `-52.95%` | `49,178,400.00` |
| `Live` | `Long` | `5.05` | 11,050,000.00 USD | 0.00 USD | 217.66 USD | `-52.00%` | `43,100.00` |
| `Live` | `Long` | `5.15` | 11,050,000.00 USD | 0.00 USD | 3,750.00 USD | `-51.05%` | `728,600.00` |
| `Live` | `Long` | `5.25` | 11,040,000.00 USD | 0.00 USD | 4,360.00 USD | `-50.10%` | `830,200.00` |
| `Live` | `Long` | `5.35` | 11,040,000.00 USD | 0.00 USD | 634,050.00 USD | `-49.15%` | `118,513,600.00` |
| `Live` | `Long` | `5.45` | 10,400,000.00 USD | 0.00 USD | 302.48 USD | `-48.20%` | `55,500.00` |
| `Live` | `Long` | `5.55` | 10,400,000.00 USD | 0.00 USD | 10,630.00 USD | `-47.25%` | `1,914,900.00` |
| `Live` | `Long` | `5.65` | 10,390,000.00 USD | 0.00 USD | 38,610.00 USD | `-46.30%` | `6,833,000.00` |
| `Live` | `Long` | `5.75` | 10,350,000.00 USD | 0.00 USD | 63,790.00 USD | `-45.35%` | `11,093,400.00` |
| `Live` | `Long` | `5.85` | 10,290,000.00 USD | 0.00 USD | 2,250.00 USD | `-44.40%` | `385,200.00` |
| `Live` | `Long` | `5.95` | 10,290,000.00 USD | 0.00 USD | 23,230.00 USD | `-43.45%` | `3,903,400.00` |
| `Live` | `Long` | `6.05` | 10,270,000.00 USD | 0.00 USD | 37,790.00 USD | `-42.50%` | `6,245,800.00` |
| `Live` | `Long` | `6.15` | 10,230,000.00 USD | 0.00 USD | 61,990.00 USD | `-41.55%` | `10,079,600.00` |
| `Live` | `Long` | `6.25` | 10,170,000.00 USD | 0.00 USD | 25,420.00 USD | `-40.60%` | `4,067,300.00` |
| `Live` | `Long` | `6.35` | 10,140,000.00 USD | 0.00 USD | 32,490.00 USD | `-39.64%` | `5,115,800.00` |
| `Live` | `Long` | `6.45` | 10,110,000.00 USD | 0.00 USD | 15,600.00 USD | `-38.69%` | `2,418,300.00` |
| `Live` | `Long` | `6.55` | 10,090,000.00 USD | 0.00 USD | 69,740.00 USD | `-37.74%` | `10,646,900.00` |
| `Live` | `Long` | `6.65` | 10,020,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-36.79%` | `175,281,000.00` |
| `Live` | `Long` | `6.75` | 8,860,000.00 USD | 0.00 USD | 12,900.00 USD | `-35.84%` | `1,911,400.00` |
| `Live` | `Long` | `6.85` | 8,840,000.00 USD | 0.00 USD | 11,910.00 USD | `-34.89%` | `1,738,400.00` |
| `Live` | `Long` | `6.95` | 8,830,000.00 USD | 0.00 USD | 30,710.00 USD | `-33.94%` | `4,419,300.00` |
| `Live` | `Long` | `7.05` | 8,800,000.00 USD | 0.00 USD | 30,290.00 USD | `-32.99%` | `4,295,900.00` |
| `Live` | `Long` | `7.15` | 8,770,000.00 USD | 0.00 USD | 11,130.00 USD | `-32.04%` | `1,556,900.00` |
| `Live` | `Long` | `7.25` | 8,760,000.00 USD | 0.00 USD | 19,400.00 USD | `-31.09%` | `2,676,300.00` |
| `Live` | `Long` | `7.35` | 8,740,000.00 USD | 0.00 USD | 7,290.00 USD | `-30.14%` | `992,500.00` |
| `Live` | `Long` | `7.45` | 8,730,000.00 USD | 0.00 USD | 8,670.00 USD | `-29.19%` | `1,163,300.00` |
| `Live` | `Long` | `7.55` | 8,720,000.00 USD | 0.00 USD | 25,070.00 USD | `-28.24%` | `3,320,900.00` |
| `Live` | `Long` | `7.65` | 8,700,000.00 USD | 0.00 USD | 1,830.00 USD | `-27.29%` | `239,400.00` |
| `Live` | `Long` | `7.75` | 8,700,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.34%` | `133,200.00` |
| `Live` | `Long` | `7.85` | 8,700,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-25.39%` | `400,765,200.00` |
| `Live` | `Long` | `7.95` | 5,550,000.00 USD | 0.00 USD | 19,280.00 USD | `-24.44%` | `2,425,200.00` |
| `Live` | `Long` | `8.05` | 5,530,000.00 USD | 0.00 USD | 65,130.00 USD | `-23.49%` | `8,090,600.00` |
| `Live` | `Long` | `8.15` | 5,470,000.00 USD | 0.00 USD | 77,060.00 USD | `-22.54%` | `9,454,900.00` |
| `Live` | `Long` | `8.25` | 5,390,000.00 USD | 0.00 USD | 199,340.00 USD | `-21.59%` | `24,162,900.00` |
| `Live` | `Long` | `8.35` | 5,190,000.00 USD | 0.00 USD | 2,410.00 USD | `-20.63%` | `288,600.00` |
| `Live` | `Long` | `8.45` | 5,190,000.00 USD | 0.00 USD | 33,290.00 USD | `-19.68%` | `3,939,600.00` |
| `Live` | `Long` | `8.55` | 5,150,000.00 USD | 0.00 USD | 72,470.00 USD | `-18.73%` | `8,476,300.00` |
| `Live` | `Long` | `8.65` | 5,080,000.00 USD | 0.00 USD | 359,190.00 USD | `-17.78%` | `41,524,600.00` |
| `Live` | `Long` | `8.75` | 4,720,000.00 USD | 0.00 USD | 26,330.00 USD | `-16.83%` | `3,008,700.00` |
| `Live` | `Long` | `8.85` | 4,700,000.00 USD | 0.00 USD | 57,530.00 USD | `-15.88%` | `6,500,000.00` |
| `Live` | `Long` | `8.95` | 4,640,000.00 USD | 0.00 USD | 451,980.00 USD | `-14.93%` | `50,501,100.00` |
| `Live` | `Long` | `9.05` | 4,190,000.00 USD | 0.00 USD | 145,160.00 USD | `-13.98%` | `16,040,200.00` |
| `Live` | `Long` | `9.15` | 4,040,000.00 USD | 0.00 USD | 79,320.00 USD | `-13.03%` | `8,668,900.00` |
| `Live` | `Long` | `9.25` | 3,960,000.00 USD | 0.00 USD | 17,690.00 USD | `-12.08%` | `1,912,100.00` |
| `Live` | `Long` | `9.35` | 3,940,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-11.13%` | `229,770,000.00` |
| `Live` | `Long` | `9.45` | 1,800,000.00 USD | 0.00 USD | 48,080.00 USD | `-10.18%` | `5,087,800.00` |
| `Live` | `Long` | `9.55` | 1,750,000.00 USD | 0.00 USD | 53,010.00 USD | `-9.23%` | `5,550,900.00` |
| `Live` | `Long` | `9.65` | 1,690,000.00 USD | 0.00 USD | 205,310.00 USD | `-8.28%` | `21,276,000.00` |
| `Live` | `Long` | `9.75` | 1,490,000.00 USD | 0.00 USD | 83,560.00 USD | `-7.33%` | `8,570,200.00` |
| `Live` | `Long` | `9.85` | 1,410,000.00 USD | 0.00 USD | 82,350.00 USD | `-6.38%` | `8,359,900.00` |
| `Live` | `Long` | `9.95` | 1,320,000.00 USD | 0.00 USD | 443,340.00 USD | `-5.43%` | `44,557,100.00` |
| `Live` | `Long` | `10.05` | 880,140.00 USD | 0.00 USD | 792,240.00 USD | `-4.48%` | `78,829,600.00` |
| `Live` | `Long` | `10.15` | 87,900.00 USD | 0.00 USD | 60,550.00 USD | `-3.53%` | `5,965,500.00` |
| `Live` | `Long` | `10.25` | 27,350.00 USD | 0.00 USD | 27,350.00 USD | `-2.58%` | `2,668,400.00` |
| `Live` | `Short` | `10.85` | 1,090.00 USD | 1,090.00 USD | 0.00 USD | `+3.13%` | `100,000.00` |
| `Live` | `Short` | `10.95` | 2,490.00 USD | 1,400.00 USD | 0.00 USD | `+4.08%` | `127,900.00` |
| `Live` | `Short` | `11.05` | 3,710.00 USD | 1,220.00 USD | 0.00 USD | `+5.03%` | `110,800.00` |
| `Live` | `Short` | `11.15` | 5,800.00 USD | 2,100.00 USD | 0.00 USD | `+5.98%` | `187,900.00` |
| `Live` | `Short` | `11.35` | 64,710.00 USD | 58,900.00 USD | 0.00 USD | `+7.88%` | `5,189,600.00` |
| `Live` | `Short` | `11.45` | 65,770.00 USD | 1,060.00 USD | 0.00 USD | `+8.83%` | `92,900.00` |
| `Live` | `Short` | `11.55` | 65,910.00 USD | 143.22 USD | 0.00 USD | `+9.78%` | `12,400.00` |
| `Live` | `Short` | `11.65` | 66,400.00 USD | 485.81 USD | 0.00 USD | `+10.73%` | `41,700.00` |
| `Live` | `Short` | `12.15` | 67,670.00 USD | 1,270.00 USD | 0.00 USD | `+15.48%` | `104,700.00` |
| `Live` | `Short` | `12.25` | 69,100.00 USD | 1,430.00 USD | 0.00 USD | `+16.43%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 69,840.00 USD | 736.06 USD | 0.00 USD | `+17.38%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 70,220.00 USD | 380.27 USD | 0.00 USD | `+19.29%` | `30,300.00` |
| `Live` | `Short` | `12.65` | 70,650.00 USD | 435.16 USD | 0.00 USD | `+20.24%` | `34,400.00` |
| `Live` | `Short` | `12.85` | 70,790.00 USD | 138.78 USD | 0.00 USD | `+22.14%` | `10,800.00` |
| `Live` | `Short` | `13.25` | 72,670.00 USD | 1,870.00 USD | 0.00 USD | `+25.94%` | `141,500.00` |
| `Live` | `Short` | `13.45` | 78,100.00 USD | 5,430.00 USD | 0.00 USD | `+27.84%` | `403,700.00` |
| `Live` | `Short` | `13.75` | 78,440.00 USD | 339.62 USD | 0.00 USD | `+30.69%` | `24,700.00` |
| `Live` | `Short` | `13.85` | 79,130.00 USD | 692.50 USD | 0.00 USD | `+31.64%` | `50,000.00` |
| `Live` | `Short` | `14.25` | 79,670.00 USD | 544.35 USD | 0.00 USD | `+35.44%` | `38,200.00` |
| `Live` | `Short` | `14.95` | 105,160.00 USD | 25,490.00 USD | 0.00 USD | `+42.10%` | `1,704,800.00` |
| `Live` | `Short` | `15.05` | 167,250.00 USD | 62,090.00 USD | 0.00 USD | `+43.05%` | `4,125,800.00` |
| `Live` | `Short` | `15.55` | 167,830.00 USD | 578.46 USD | 0.00 USD | `+47.80%` | `37,200.00` |
| `Live` | `Short` | `15.65` | 167,990.00 USD | 158.07 USD | 0.00 USD | `+48.75%` | `10,100.00` |
| `Live` | `Short` | `15.85` | 168,260.00 USD | 271.04 USD | 0.00 USD | `+50.65%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 168,620.00 USD | 362.06 USD | 0.00 USD | `+51.60%` | `22,700.00` |
| `Live` | `Short` | `16.35` | 170,150.00 USD | 1,530.00 USD | 0.00 USD | `+55.40%` | `93,400.00` |
| `Live` | `Short` | `16.55` | 184,350.00 USD | 14,190.00 USD | 0.00 USD | `+57.30%` | `857,700.00` |
| `Live` | `Short` | `16.75` | 275,550.00 USD | 91,200.00 USD | 0.00 USD | `+59.21%` | `5,445,000.00` |
| `Live` | `Short` | `16.95` | 355,320.00 USD | 79,770.00 USD | 0.00 USD | `+61.11%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 356,690.00 USD | 1,370.00 USD | 0.00 USD | `+63.01%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 374,940.00 USD | 18,250.00 USD | 0.00 USD | `+63.96%` | `1,058,000.00` |
| `Live` | `Short` | `17.45` | 386,090.00 USD | 11,150.00 USD | 0.00 USD | `+65.86%` | `639,000.00` |
| `Live` | `Short` | `17.85` | 1,060,000.00 USD | 673,370.00 USD | 0.00 USD | `+69.66%` | `37,724,000.00` |
| `Live` | `Short` | `17.95` | 1,060,000.00 USD | 351.82 USD | 0.00 USD | `+70.61%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 1,310,000.00 USD | 254,100.00 USD | 0.00 USD | `+71.56%` | `14,077,300.00` |
| `Live` | `Short` | `18.35` | 1,340,000.00 USD | 28,240.00 USD | 0.00 USD | `+74.41%` | `1,539,000.00` |
| `Live` | `Short` | `18.45` | 1,350,000.00 USD | 3,890.00 USD | 0.00 USD | `+75.36%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,350,000.00 USD | 185.50 USD | 0.00 USD | `+76.31%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 1,350,000.00 USD | 5,950.00 USD | 0.00 USD | `+77.26%` | `319,000.00` |
| `Live` | `Short` | `18.85` | 1,350,000.00 USD | 456.17 USD | 0.00 USD | `+79.17%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 1,350,000.00 USD | 752.32 USD | 0.00 USD | `+80.12%` | `39,700.00` |
| `Live` | `Short` | `19.25` | 1,350,000.00 USD | 127.05 USD | 0.00 USD | `+82.97%` | `6,600.00` |
| `Live` | `Short` | `19.35` | 1,380,000.00 USD | 29,470.00 USD | 0.00 USD | `+83.92%` | `1,523,000.00` |
| `Live` | `Short` | `19.55` | 2,200,000.00 USD | 820,330.00 USD | 0.00 USD | `+85.82%` | `41,960,800.00` |
| `Live` | `Short` | `19.65` | 2,250,000.00 USD | 42,180.00 USD | 0.00 USD | `+86.77%` | `2,146,500.00` |
| `Live` | `Short` | `19.75` | 2,250,000.00 USD | 359.45 USD | 0.00 USD | `+87.72%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 2,320,000.00 USD | 77,320.00 USD | 0.00 USD | `+88.67%` | `3,895,000.00` |
| `Live` | `Short` | `19.95` | 2,320,000.00 USD | 291.27 USD | 0.00 USD | `+89.62%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 2,320,000.00 USD | 637.59 USD | 0.00 USD | `+90.57%` | `31,800.00` |
| `Live` | `Short` | `20.15` | 2,330,000.00 USD | 1,450.00 USD | 0.00 USD | `+91.52%` | `71,900.00` |
| `Live` | `Short` | `20.25` | 2,330,000.00 USD | 261.23 USD | 0.00 USD | `+92.47%` | `12,900.00` |
| `Live` | `Short` | `20.35` | 4,670,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+93.42%` | `115,024,600.00` |
| `Live` | `Short` | `20.55` | 4,670,000.00 USD | 7,460.00 USD | 0.00 USD | `+95.32%` | `363,200.00` |
| `Live` | `Short` | `21.05` | 4,680,000.00 USD | 2,440.00 USD | 0.00 USD | `+100.08%` | `116,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 384,020.00 USD | 0.00 USD | 182.03 USD | `-76.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 383,830.00 USD | 0.00 USD | 209.48 USD | `-70.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 383,620.00 USD | 0.00 USD | 431.68 USD | `-66.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 383,190.00 USD | 0.00 USD | 290.29 USD | `-56.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 382,900.00 USD | 0.00 USD | 120.22 USD | `-50.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 382,780.00 USD | 0.00 USD | 251.68 USD | `-42.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 382,530.00 USD | 0.00 USD | 749.30 USD | `-39.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 381,780.00 USD | 0.00 USD | 186.41 USD | `-38.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 381,590.00 USD | 0.00 USD | 3,760.00 USD | `-37.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 377,830.00 USD | 0.00 USD | 133.00 USD | `-36.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 377,700.00 USD | 0.00 USD | 1,320.00 USD | `-33.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 376,380.00 USD | 0.00 USD | 3,770.00 USD | `-32.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 372,610.00 USD | 0.00 USD | 2,070.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 370,540.00 USD | 0.00 USD | 3,740.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 366,800.00 USD | 0.00 USD | 1,050.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 365,750.00 USD | 0.00 USD | 120.90 USD | `-26.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 365,620.00 USD | 0.00 USD | 269.25 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 365,360.00 USD | 0.00 USD | 166.95 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 365,190.00 USD | 0.00 USD | 5,000.00 USD | `-23.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 360,190.00 USD | 0.00 USD | 393.64 USD | `-22.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 359,790.00 USD | 0.00 USD | 10,560.00 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 349,230.00 USD | 0.00 USD | 3,110.00 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 346,120.00 USD | 0.00 USD | 1,480.00 USD | `-19.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 344,640.00 USD | 0.00 USD | 52,990.00 USD | `-18.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 291,660.00 USD | 0.00 USD | 186.84 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 291,470.00 USD | 0.00 USD | 742.88 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 290,730.00 USD | 0.00 USD | 4,510.00 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 286,220.00 USD | 0.00 USD | 1,570.00 USD | `-14.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 284,650.00 USD | 0.00 USD | 3,340.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 281,310.00 USD | 0.00 USD | 194.90 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 281,120.00 USD | 0.00 USD | 1,020.00 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 280,100.00 USD | 0.00 USD | 7,840.00 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 272,250.00 USD | 0.00 USD | 2,310.00 USD | `-10.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 269,940.00 USD | 0.00 USD | 19,570.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 250,370.00 USD | 0.00 USD | 1,230.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 249,140.00 USD | 0.00 USD | 292.50 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 248,850.00 USD | 0.00 USD | 24,670.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 224,180.00 USD | 0.00 USD | 14,650.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 209,540.00 USD | 0.00 USD | 42,800.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 166,740.00 USD | 0.00 USD | 51,860.00 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 114,880.00 USD | 0.00 USD | 113,510.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 1,370.00 USD | 0.00 USD | 245.30 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 1,130.00 USD | 0.00 USD | 1,130.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.55` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.65` | 68,180.00 USD | 67,120.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.75` | 75,050.00 USD | 6,870.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.85` | 80,470.00 USD | 5,430.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.95` | 86,600.00 USD | 6,130.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 164,600.00 USD | 78,000.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 190,410.00 USD | 25,810.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 204,440.00 USD | 14,040.00 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 211,250.00 USD | 6,800.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 211,640.00 USD | 396.17 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 231,140.00 USD | 19,500.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 233,390.00 USD | 2,250.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 234,140.00 USD | 746.12 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 234,390.00 USD | 253.59 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 238,040.00 USD | 3,650.00 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 266,020.00 USD | 27,980.00 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 268,100.00 USD | 2,080.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 277,580.00 USD | 9,490.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 278,180.00 USD | 597.74 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 283,080.00 USD | 4,890.00 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 339,850.00 USD | 56,780.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 424,420.00 USD | 84,570.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 425,100.00 USD | 679.57 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 445,470.00 USD | 20,360.00 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 445,920.00 USD | 451.95 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 462,550.00 USD | 16,630.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 482,170.00 USD | 19,620.00 USD | 0.00 USD | `+24.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 483,490.00 USD | 1,320.00 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 491,270.00 USD | 7,790.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 493,810.00 USD | 2,540.00 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 493,970.00 USD | 165.31 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 494,930.00 USD | 954.14 USD | 0.00 USD | `+29.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 496,990.00 USD | 2,060.00 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 501,870.00 USD | 4,880.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 502,140.00 USD | 266.44 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 518,400.00 USD | 16,260.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 518,550.00 USD | 152.82 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 522,830.00 USD | 4,280.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 526,240.00 USD | 3,410.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 545,680.00 USD | 19,440.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 545,900.00 USD | 218.25 USD | 0.00 USD | `+38.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 548,140.00 USD | 2,250.00 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 555,410.00 USD | 7,270.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 556,360.00 USD | 950.82 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 581,220.00 USD | 24,860.00 USD | 0.00 USD | `+43.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 583,670.00 USD | 2,450.00 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 816,710.00 USD | 233,040.00 USD | 0.00 USD | `+44.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 817,630.00 USD | 924.07 USD | 0.00 USD | `+45.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 818,520.00 USD | 893.01 USD | 0.00 USD | `+46.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 819,180.00 USD | 653.10 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 819,650.00 USD | 472.63 USD | 0.00 USD | `+48.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 822,940.00 USD | 3,290.00 USD | 0.00 USD | `+49.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 826,110.00 USD | 3,170.00 USD | 0.00 USD | `+50.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 831,250.00 USD | 5,130.00 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 846,320.00 USD | 15,080.00 USD | 0.00 USD | `+52.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 853,130.00 USD | 6,800.00 USD | 0.00 USD | `+53.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 859,630.00 USD | 6,500.00 USD | 0.00 USD | `+54.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 866,170.00 USD | 6,540.00 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 872,750.00 USD | 6,580.00 USD | 0.00 USD | `+56.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 882,680.00 USD | 9,930.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 986,660.00 USD | 103,980.00 USD | 0.00 USD | `+58.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 1,000,000.00 USD | 14,240.00 USD | 0.00 USD | `+59.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 1,090,000.00 USD | 84,360.00 USD | 0.00 USD | `+60.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 1,090,000.00 USD | 1,700.00 USD | 0.00 USD | `+61.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 1,090,000.00 USD | 7,370.00 USD | 0.00 USD | `+62.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 1,110,000.00 USD | 16,690.00 USD | 0.00 USD | `+63.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 1,110,000.00 USD | 2,300.00 USD | 0.00 USD | `+63.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,120,000.00 USD | 1,740.00 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,140,000.00 USD | 21,690.00 USD | 0.00 USD | `+65.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,140,000.00 USD | 4,390.00 USD | 0.00 USD | `+66.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,150,000.00 USD | 4,410.00 USD | 0.00 USD | `+67.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,150,000.00 USD | 4,440.00 USD | 0.00 USD | `+68.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,150,000.00 USD | 4,460.00 USD | 0.00 USD | `+69.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,150,000.00 USD | 448.75 USD | 0.00 USD | `+70.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,190,000.00 USD | 30,960.00 USD | 0.00 USD | `+71.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,190,000.00 USD | 453.75 USD | 0.00 USD | `+72.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,190,000.00 USD | 456.25 USD | 0.00 USD | `+73.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,190,000.00 USD | 458.75 USD | 0.00 USD | `+74.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,190,000.00 USD | 461.25 USD | 0.00 USD | `+75.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,190,000.00 USD | 4,540.00 USD | 0.00 USD | `+76.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,190,000.00 USD | 466.25 USD | 0.00 USD | `+77.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,190,000.00 USD | 468.75 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,190,000.00 USD | 471.25 USD | 0.00 USD | `+79.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,190,000.00 USD | 473.75 USD | 0.00 USD | `+80.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,260,000.00 USD | 67,000.00 USD | 0.00 USD | `+81.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,260,000.00 USD | 574.50 USD | 0.00 USD | `+82.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,260,000.00 USD | 577.50 USD | 0.00 USD | `+82.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,260,000.00 USD | 2,710.00 USD | 0.00 USD | `+83.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,270,000.00 USD | 972.50 USD | 0.00 USD | `+84.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,270,000.00 USD | 7,680.00 USD | 0.00 USD | `+85.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,270,000.00 USD | 786.00 USD | 0.00 USD | `+86.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,280,000.00 USD | 790.00 USD | 0.00 USD | `+87.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,280,000.00 USD | 992.50 USD | 0.00 USD | `+88.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,280,000.00 USD | 997.50 USD | 0.00 USD | `+89.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,880,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+90.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,880,000.00 USD | 1,010.00 USD | 0.00 USD | `+91.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,880,000.00 USD | 1,010.00 USD | 0.00 USD | `+92.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,880,000.00 USD | 1,020.00 USD | 0.00 USD | `+93.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,880,000.00 USD | 1,020.00 USD | 0.00 USD | `+94.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,890,000.00 USD | 1,030.00 USD | 0.00 USD | `+95.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,890,000.00 USD | 1,030.00 USD | 0.00 USD | `+96.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,890,000.00 USD | 1,040.00 USD | 0.00 USD | `+97.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,890,000.00 USD | 1,410.00 USD | 0.00 USD | `+98.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,890,000.00 USD | 1,050.00 USD | 0.00 USD | `+99.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,890,000.00 USD | 4,000.00 USD | 0.00 USD | `+100.08%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `9.45` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD |
| `1D` | `9.47` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD |
| `1D` | `9.53` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD |
| `7D` | `9.53` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD |
| `1D` | `9.55` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD |
| `7D` | `9.55` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD |
| `1D` | `9.57` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 1,780.00 USD | 0.00 USD |
| `7D` | `9.57` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD |
| `1D` | `9.59` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 40,390.00 USD | 6,150.00 USD | 34,990.00 USD |
| `7D` | `9.59` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `9.61` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,090.00 USD | 3,960.00 USD | 0.00 USD |
| `7D` | `9.61` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `1D` | `9.63` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 671.70 USD | 0.00 USD | 14,300.00 USD |
| `7D` | `9.63` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD |
| `1D` | `9.65` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 972.50 USD | 0.00 USD | 105.10 USD |
| `7D` | `9.65` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD |
| `1D` | `9.67` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD |
| `7D` | `9.67` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `9.69` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 10,890.00 USD |
| `7D` | `9.69` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.71` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD |
| `7D` | `9.71` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `1D` | `9.73` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD |
| `7D` | `9.73` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.75` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 40,030.00 USD | 0.00 USD | 13,160.00 USD |
| `7D` | `9.75` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD |
| `1D` | `9.77` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD |
| `7D` | `9.77` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.79` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD |
| `7D` | `9.79` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD |
| `1D` | `9.81` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,690.00 USD |
| `7D` | `9.81` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD |
| `1D` | `9.83` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 37,110.00 USD | 0.00 USD | 10,480.00 USD |
| `7D` | `9.83` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD |
| `1D` | `9.85` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD |
| `7D` | `9.85` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `9.87` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD |
| `7D` | `9.89` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.91` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD |
| `7D` | `9.91` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.93` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD |
| `7D` | `9.93` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.95` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD |
| `7D` | `9.95` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD |
| `1D` | `9.97` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD |
| `7D` | `9.97` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD |
| `1D` | `9.99` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD |
| `7D` | `9.99` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD |
| `1D` | `10.01` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD |
| `7D` | `10.01` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.03` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD |
| `1D` | `10.05` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD |
| `7D` | `10.05` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `7D` | `10.07` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `1D` | `10.09` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD |
| `7D` | `10.09` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD |
| `7D` | `10.11` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `10.13` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD |
| `7D` | `10.13` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.15` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD |
| `7D` | `10.15` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `1D` | `10.17` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 3,600.00 USD | 17,840.00 USD | 424.12 USD |
| `7D` | `10.17` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD |
| `1D` | `10.19` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 3,360.00 USD | 15,950.00 USD | 46.76 USD |
| `7D` | `10.19` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.21` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 39,570.00 USD | 17,890.00 USD | 37,590.00 USD |
| `7D` | `10.21` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.23` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 111,870.00 USD | 20,390.00 USD | 153,210.00 USD |
| `7D` | `10.23` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.25` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 26,800.00 USD | 19,590.00 USD | 11,020.00 USD |
| `7D` | `10.25` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.27` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 18,050.00 USD | 11,470.00 USD | 40,150.00 USD |
| `7D` | `10.27` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.29` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,860.00 USD |
| `7D` | `10.29` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD |
| `1D` | `10.31` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,300.00 USD |
| `7D` | `10.31` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD |
| `1D` | `10.33` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,350.00 USD |
| `7D` | `10.33` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD |
| `1D` | `10.35` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,090.00 USD |
| `7D` | `10.35` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.37` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,450.00 USD |
| `7D` | `10.37` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD |
| `1D` | `10.39` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 7,450.00 USD | 41,060.00 USD | 44,270.00 USD |
| `7D` | `10.39` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.41` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 259,620.00 USD | 45,690.00 USD | 90,040.00 USD |
| `7D` | `10.41` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD |
| `1D` | `10.43` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 248,090.00 USD | 62,710.00 USD | 71,990.00 USD |
| `7D` | `10.43` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.45` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 332,800.00 USD | 44,610.00 USD | 277,180.00 USD |
| `7D` | `10.45` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD |
| `1D` | `10.47` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 219,660.00 USD | 80,860.00 USD | 77,570.00 USD |
| `7D` | `10.47` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD |
| `1D` | `10.49` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 124,820.00 USD | 26,560.00 USD | 88,910.00 USD |
| `7D` | `10.49` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD |
| `1D` | `10.51` | 933,190.00 USD | 0.00 USD | 933,190.00 USD | 27,700.00 USD | 6,670.00 USD | 13,570.00 USD |
| `7D` | `10.51` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.53` | 885,260.00 USD | 0.00 USD | 885,260.00 USD | 43,880.00 USD | 39,730.00 USD | 117,580.00 USD |
| `7D` | `10.53` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD |
| `1D` | `10.55` | 684,070.00 USD | 0.00 USD | 684,070.00 USD | 7,160.00 USD | 517.73 USD | 56,280.00 USD |
| `7D` | `10.55` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD |
| `1D` | `10.57` | 620,110.00 USD | 0.00 USD | 620,110.00 USD | 52,260.00 USD | 287.00 USD | 114,300.00 USD |
| `7D` | `10.57` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD |
| `1D` | `10.59` | 453,270.00 USD | 0.00 USD | 453,270.00 USD | 48,700.00 USD | 615.80 USD | 172,420.00 USD |
| `7D` | `10.59` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD |
| `1D` | `10.61` | 231,530.00 USD | 0.00 USD | 231,530.00 USD | 231,310.00 USD | 17.90 USD | 210.16 USD |
| `7D` | `10.61` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD |
| `1D` | `10.62` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.63` | 301,170.00 USD | 301,170.00 USD | 0.00 USD | 301,120.00 USD | 0.00 USD | 51.48 USD |
| `7D` | `10.63` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD |
| `1D` | `10.65` | 301,820.00 USD | 301,820.00 USD | 0.00 USD | 644.06 USD | 0.00 USD | 0.40 USD |
| `7D` | `10.65` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD |
| `1D` | `10.67` | 301,830.00 USD | 301,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.09 USD |
| `7D` | `10.67` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD |
| `1D` | `10.69` | 423,930.00 USD | 423,930.00 USD | 0.00 USD | 122,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.69` | 801,310.00 USD | 0.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD |
| `1D` | `10.71` | 646,780.00 USD | 646,780.00 USD | 0.00 USD | 219,090.00 USD | 25.97 USD | 3,730.00 USD |
| `7D` | `10.71` | 323,480.00 USD | 0.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD |
| `1D` | `10.73` | 656,610.00 USD | 656,610.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `10.73` | 29,560.00 USD | 29,560.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `7D` | `10.73` | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `1D` | `10.75` | 746,660.00 USD | 746,660.00 USD | 0.00 USD | 89,590.00 USD | 430.90 USD | 20.58 USD |
| `7D` | `10.75` | 77,290.00 USD | 77,290.00 USD | 0.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD |
| `1D` | `10.77` | 756,060.00 USD | 756,060.00 USD | 0.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `10.77` | 98,870.00 USD | 98,870.00 USD | 0.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD |
| `1D` | `10.79` | 929,710.00 USD | 929,710.00 USD | 0.00 USD | 88,000.00 USD | 85,640.00 USD | 0.00 USD |
| `7D` | `10.79` | 192,270.00 USD | 192,270.00 USD | 0.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD |
| `1D` | `10.81` | 992,460.00 USD | 992,460.00 USD | 0.00 USD | 0.00 USD | 62,760.00 USD | 0.00 USD |
| `1D` | `10.83` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 34,810.00 USD | 50,360.00 USD |
| `1D` | `10.85` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 75,750.00 USD | 26,640.00 USD | 0.00 USD |
| `1D` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD |
| `1D` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD |
| `1D` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD |
| `1D` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD |
| `1D` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD |
| `7D` | `10.95` | 227,860.00 USD | 227,860.00 USD | 0.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD |
| `1D` | `10.97` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 124.21 USD | 15,600.00 USD | 54,460.00 USD |
| `7D` | `10.97` | 240,550.00 USD | 240,550.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 413,570.00 USD | 413,570.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD |
| `1D` | `11.01` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 17,840.00 USD | 106,110.00 USD |
| `7D` | `11.01` | 424,150.00 USD | 424,150.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.03` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 15,920.00 USD | 145,940.00 USD |
| `7D` | `11.03` | 576,560.00 USD | 576,560.00 USD | 0.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.05` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 192,840.00 USD | 1,480.00 USD | 90,760.00 USD |
| `7D` | `11.05` | 966,150.00 USD | 966,150.00 USD | 0.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 473,120.00 USD | 32,310.00 USD | 78,770.00 USD |
| `7D` | `11.07` | 973,650.00 USD | 973,650.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.09` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 227,910.00 USD | 46,680.00 USD | 170,030.00 USD |
| `7D` | `11.09` | 981,150.00 USD | 981,150.00 USD | 0.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `11.11` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 216,430.00 USD | 37,650.00 USD | 15,640.00 USD |
| `7D` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD |
| `1D` | `11.13` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 408,510.00 USD | 91,630.00 USD | 167,890.00 USD |
| `7D` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD |
| `1D` | `11.15` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 194,240.00 USD | 11,710.00 USD | 0.00 USD |
| `7D` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD |
| `1D` | `11.17` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 165.70 USD | 69,930.00 USD | 58,890.00 USD |
| `7D` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD |
| `1D` | `11.19` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 72,110.00 USD | 63,920.00 USD | 27,230.00 USD |
| `7D` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD |
| `1D` | `11.21` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 114,530.00 USD | 425.43 USD | 116,470.00 USD |
| `7D` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD |
| `1D` | `11.23` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD |
| `7D` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD |
| `7D` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD |
| `1D` | `11.27` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD |
| `7D` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.29` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 165,410.00 USD | 123,030.00 USD | 213,620.00 USD |
| `7D` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD |
| `1D` | `11.31` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 63,250.00 USD | 67,150.00 USD | 79,800.00 USD |
| `7D` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 198,020.00 USD | 38,820.00 USD | 31,620.00 USD |
| `7D` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD |
| `1D` | `11.35` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 297,850.00 USD | 124,090.00 USD | 66,390.00 USD |
| `7D` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD |
| `1D` | `11.37` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 150,920.00 USD | 78,610.00 USD | 22,240.00 USD |
| `7D` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD |
| `1D` | `11.39` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD |
| `7D` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 95,030.00 USD | 34,780.00 USD | 140,440.00 USD |
| `7D` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.43` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 52,230.00 USD | 26,360.00 USD | 88,640.00 USD |
| `7D` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD |
| `1D` | `11.45` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 46,070.00 USD | 69,710.00 USD | 0.00 USD |
| `7D` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.47` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 48,370.00 USD | 19,590.00 USD | 23,420.00 USD |
| `7D` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 33,390.00 USD | 22,330.00 USD | 34,640.00 USD |
| `7D` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 41,360.00 USD | 28,330.00 USD | 30,920.00 USD |
| `7D` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD |
| `1D` | `11.53` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 32,640.00 USD | 16,860.00 USD | 29,710.00 USD |
| `7D` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD |
| `1D` | `11.55` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD |
| `7D` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD |
| `1D` | `11.57` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD |
| `7D` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.59` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 15,100.00 USD | 7,660.00 USD | 39,570.00 USD |
| `7D` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.61` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 153,200.00 USD | 0.00 USD | 71,370.00 USD |
| `7D` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.63` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD |
| `7D` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.65` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 1,410.00 USD | 7,130.00 USD | 46.76 USD |
| `7D` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD |
| `1D` | `11.67` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 6,370.00 USD | 0.00 USD |
| `7D` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.69` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 59,600.00 USD | 29,410.00 USD | 313.96 USD |
| `7D` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.71` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD |
| `7D` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 138,580.00 USD | 5,720.00 USD | 76,780.00 USD |
| `7D` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.75` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 21,990.00 USD | 35,620.00 USD | 61,350.00 USD |
| `7D` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.77` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 41,180.00 USD | 18,670.00 USD | 14,480.00 USD |
| `7D` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 12,080.00 USD | 755.20 USD | 40,180.00 USD |
| `7D` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.81` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 17,960.00 USD | 17,880.00 USD |
| `7D` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 11,070.00 USD | 11,510.00 USD | 29,320.00 USD |
| `7D` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.85` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 76,700.00 USD | 22,590.00 USD | 82,330.00 USD |
| `7D` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.87` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD |
| `7D` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.89` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 44,160.00 USD | 11,410.00 USD | 43,750.00 USD |
| `7D` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.91` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 102,960.00 USD | 18,340.00 USD | 31,710.00 USD |
| `7D` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.93` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 135,130.00 USD | 28,540.00 USD | 28,590.00 USD |
| `7D` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 85,850.00 USD | 21,080.00 USD | 41,560.00 USD |
| `7D` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.97` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD |
| `7D` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.99` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 123,700.00 USD | 25,870.00 USD | 46,860.00 USD |
| `7D` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.01` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 60,120.00 USD | 9,410.00 USD | 52,780.00 USD |
| `7D` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD |
| `1D` | `12.03` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD |
| `7D` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD |
| `1D` | `12.05` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 206,510.00 USD | 58,260.00 USD | 81,190.00 USD |
| `7D` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.07` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 114,130.00 USD | 53,190.00 USD | 97,550.00 USD |
| `7D` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.09` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 17,390.00 USD | 18,490.00 USD | 17,590.00 USD |
| `7D` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.11` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 94,540.00 USD | 34,950.00 USD | 55,330.00 USD |
| `7D` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.13` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 94,650.00 USD | 33,860.00 USD | 39,740.00 USD |
| `7D` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.15` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD |
| `7D` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.17` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 122,970.00 USD | 64,130.00 USD | 69,710.00 USD |
| `7D` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.19` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 64,080.00 USD | 24,200.00 USD | 12,250.00 USD |
| `7D` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD |
| `1D` | `12.21` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 52,950.00 USD | 28,750.00 USD | 50,920.00 USD |
| `7D` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD |
| `1D` | `12.23` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 14,580.00 USD | 24,000.00 USD | 4,690.00 USD |
| `7D` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.25` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 2,260.00 USD | 5,380.00 USD | 7,630.00 USD |
| `7D` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.27` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 52,420.00 USD | 9,580.00 USD | 22,930.00 USD |
| `7D` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.29` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 36,110.00 USD | 19,760.00 USD | 30,020.00 USD |
| `7D` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.31` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 19,750.00 USD | 4,850.00 USD | 9,840.00 USD |
| `7D` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.33` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD |
| `7D` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD |
| `1D` | `12.35` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD |
| `7D` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.37` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 8,820.00 USD | 5,700.00 USD | 3,140.00 USD |
| `7D` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD |
| `1D` | `12.39` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 28,430.00 USD | 12,560.00 USD | 21,540.00 USD |
| `7D` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD |
| `1D` | `12.41` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 42,540.00 USD | 19,990.00 USD | 23,470.00 USD |
| `7D` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.43` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 23,090.00 USD | 5,940.00 USD | 88.63 USD |
| `7D` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.45` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD |
| `7D` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.47` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 12,000.00 USD | 12,400.00 USD |
| `7D` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD |
| `7D` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD |
| `7D` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 0.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD |
| `7D` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD |
| `7D` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD |
| `7D` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 0.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD |
| `7D` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 0.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD |
| `7D` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD |
| `7D` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD |
| `7D` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 0.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD |
| `7D` | `12.67` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD |
| `7D` | `12.69` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD |
| `7D` | `12.71` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD |
| `7D` | `12.73` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD |
| `7D` | `12.75` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD |
| `7D` | `12.77` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD |
| `7D` | `12.79` | 20,470,000.00 USD | 20,470,000.00 USD | 0.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD |
| `7D` | `12.81` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD |
| `7D` | `12.83` | 20,520,000.00 USD | 20,520,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD |
| `7D` | `12.85` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,810.00 USD |
| `7D` | `12.87` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD |
| `7D` | `12.89` | 20,730,000.00 USD | 20,730,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD |
| `7D` | `12.91` | 20,840,000.00 USD | 20,840,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 39,080.00 USD |
| `7D` | `12.93` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD |
| `7D` | `12.95` | 20,890,000.00 USD | 20,890,000.00 USD | 0.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD |
| `7D` | `12.97` | 20,930,000.00 USD | 20,930,000.00 USD | 0.00 USD | 13,890.00 USD | 10,560.00 USD | 24,350.00 USD |
| `7D` | `12.99` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD |
| `7D` | `13.01` | 21,050,000.00 USD | 21,050,000.00 USD | 0.00 USD | 26,320.00 USD | 2,920.00 USD | 13,340.00 USD |
| `7D` | `13.03` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD |
| `7D` | `13.07` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 23,750.00 USD | 6,890.00 USD | 17,780.00 USD |
| `7D` | `13.09` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 16,060.00 USD | 527.72 USD | 7,600.00 USD |
| `7D` | `13.11` | 21,160,000.00 USD | 21,160,000.00 USD | 0.00 USD | 19,270.00 USD | 5,960.00 USD | 20.43 USD |
| `7D` | `13.13` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 13,360.00 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD |
| `7D` | `13.19` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 13,890.00 USD | 6,210.00 USD | 8,930.00 USD |
| `7D` | `13.23` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD |
| `7D` | `13.25` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD |
| `7D` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD |
| `7D` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD |
| `7D` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 0.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD |
| `7D` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 158.65 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `537.51M` | Total OI Tokens: `50,207,691.3 LINK`
  * 1h OI Change: `+3.44%` | 4h OI Change: `+2.47%` | 24h OI Change: `-1.69%`
  * Exchange Breakdown: Binance=`100.69M` | Bybit=`68.67M` | OKX=`25.59M` | Hyperliquid=`54.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.39K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0034%` | **USDT OKX** | `0.0031%` |
| **USDT Bybit** | `0.0000%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0030%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `44.00%` | `56.00%` | `0.79` | 8,140,000.00 USD |
| `15M` | `Binance` | `46.03%` | `53.97%` | `0.85` | 2,780,000.00 USD |
| `15M` | `OKX` | `38.57%` | `61.43%` | `0.63` | 783,250.00 USD |
| `15M` | `Bybit` | `44.72%` | `55.28%` | `0.81` | 972,270.00 USD |
| `15M` | `KuCoin` | `23.58%` | `76.42%` | `0.31` | 90,270.00 USD |
| `15M` | `Gate` | `37.98%` | `62.02%` | `0.61` | 162,190.00 USD |
| `15M` | `Bitget` | `34.35%` | `65.65%` | `0.52` | 263,350.00 USD |
| `15M` | `BingX` | `59.63%` | `40.37%` | `1.48` | 196,350.00 USD |
| `15M` | `MEXC` | `46.02%` | `53.98%` | `0.85` | 2,240,000.00 USD |
| `15M` | `Bitunix` | `30.37%` | `69.63%` | `0.44` | 266,750.00 USD |
| `15M` | `Hyperliquid` | `59.09%` | `40.91%` | `1.44` | 125,380.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.64%` | `52.36%` | `0.91` | 146,840.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `14.62%` | `85.38%` | `0.17` | 79,410.00 USD |
| `15M` | `HTX` | `12.83%` | `87.17%` | `0.15` | 2,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `1.35%` | `98.65%` | `0.01` | 9,960.00 USD |
| `15M` | `Aster` | `80.44%` | `19.56%` | `4.11` | 1,130.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.28%` | `74.72%` | `0.34` | 16,740.00 USD |
| `15M` | `Whale Positions` | `46.03%` | `53.97%` | `0.85` | 2,780,000.00 USD |
| `15M` | `Global Accounts` | `44.00%` | `56.00%` | `0.79` | 8,140,000.00 USD |
| `1H` | `LINK` | `51.16%` | `48.84%` | `1.05` | 47,960,000.00 USD |
| `1H` | `Binance` | `53.43%` | `46.57%` | `1.15` | 18,830,000.00 USD |
| `1H` | `OKX` | `44.13%` | `55.87%` | `0.79` | 3,260,000.00 USD |
| `1H` | `Bybit` | `38.2%` | `61.8%` | `0.62` | 6,630,000.00 USD |
| `1H` | `KuCoin` | `45.64%` | `54.36%` | `0.84` | 224,860.00 USD |
| `1H` | `Gate` | `47.31%` | `52.69%` | `0.90` | 931,650.00 USD |
| `1H` | `Bitget` | `64.28%` | `35.72%` | `1.80` | 2,160,000.00 USD |
| `1H` | `BingX` | `58.76%` | `41.24%` | `1.42` | 635,000.00 USD |
| `1H` | `MEXC` | `52.23%` | `47.77%` | `1.09` | 11,410,000.00 USD |
| `1H` | `Bitunix` | `39.2%` | `60.8%` | `0.64` | 1,290,000.00 USD |
| `1H` | `Hyperliquid` | `70.28%` | `29.72%` | `2.36` | 735,090.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.92%` | `50.08%` | `1.00` | 664,720.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `56.34%` | `43.66%` | `1.29` | 206,180.00 USD |
| `1H` | `HTX` | `49.28%` | `50.72%` | `0.97` | 17,530.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `84.88%` | `15.12%` | `5.61` | 748,660.00 USD |
| `1H` | `Aster` | `75.88%` | `24.12%` | `3.15` | 52,480.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.49%` | `46.51%` | `1.15` | 135,270.00 USD |
| `1H` | `Whale Positions` | `53.43%` | `46.57%` | `1.15` | 18,830,000.00 USD |
| `1H` | `Global Accounts` | `51.16%` | `48.84%` | `1.05` | 47,960,000.00 USD |
| `4H` | `LINK` | `48.63%` | `51.37%` | `0.95` | 334,070,000.00 USD |
| `4H` | `Binance` | `49.87%` | `50.13%` | `0.99` | 130,370,000.00 USD |
| `4H` | `OKX` | `48.78%` | `51.22%` | `0.95` | 28,290,000.00 USD |
| `4H` | `Bybit` | `46.08%` | `53.92%` | `0.85` | 35,210,000.00 USD |
| `4H` | `KuCoin` | `43%` | `57%` | `0.75` | 2,100,000.00 USD |
| `4H` | `Gate` | `48.28%` | `51.72%` | `0.93` | 6,850,000.00 USD |
| `4H` | `Bitget` | `53.42%` | `46.58%` | `1.15` | 13,470,000.00 USD |
| `4H` | `BingX` | `40.98%` | `59.02%` | `0.69` | 6,660,000.00 USD |
| `4H` | `MEXC` | `49.94%` | `50.06%` | `1.00` | 64,460,000.00 USD |
| `4H` | `Bitunix` | `41.36%` | `58.64%` | `0.71` | 12,330,000.00 USD |
| `4H` | `Hyperliquid` | `39.69%` | `60.31%` | `0.66` | 19,680,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.49%` | `51.51%` | `0.94` | 6,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `72.23%` | `27.77%` | `2.60` | 2,350,000.00 USD |
| `4H` | `HTX` | `42.71%` | `57.29%` | `0.75` | 145,460.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `61.91%` | `38.09%` | `1.63` | 3,800,000.00 USD |
| `4H` | `Aster` | `49.98%` | `50.02%` | `1.00` | 877,340.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.44%` | `51.56%` | `0.94` | 1,320,000.00 USD |
| `4H` | `Whale Positions` | `49.87%` | `50.13%` | `0.99` | 130,370,000.00 USD |
| `4H` | `Global Accounts` | `48.63%` | `51.37%` | `0.95` | 334,070,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `10.40` | `10.41` | `10.40` | `10.62` | `10.25` | 19,570,725.78 USD | 8,859,712.52 USD | 10,711,013.26 USD | -1,851,300.74 USD | `-9.46%` | `9B / 30S` |
| `0:00 UTC` | `10.43` | `10.38` | `10.43` | `10.45` | `10.27` | 6,950,172.42 USD | 3,875,231.69 USD | 3,074,940.73 USD | 800,290.97 USD | `+11.51%` | `19B / 7S` |
| `5:00 UTC` | `10.50` | `10.48` | `10.50` | `10.51` | `10.41` | 5,814,722.50 USD | 3,409,188.77 USD | 2,405,533.73 USD | 1,003,655.04 USD | `+17.26%` | `9B / 12S` |
| `0:00 UTC` | `10.54` | `10.54` | `10.54` | `10.64` | `10.48` | 6,172,753.46 USD | 2,942,540.47 USD | 3,230,212.99 USD | -287,672.51 USD | `-4.66%` | `40B / 12S` |
| `5:00 UTC` | `10.52` | `10.54` | `10.52` | `10.62` | `10.50` | 3,349,266.76 USD | 1,613,684.48 USD | 1,735,582.28 USD | -121,897.81 USD | `-3.64%` | `14B / 13S` |
| `0:00 UTC` | `10.61` | `10.54` | `10.61` | `10.62` | `10.42` | 5,937,236.51 USD | 3,058,190.15 USD | 2,879,046.36 USD | 179,143.78 USD | `+3.02%` | `7B / 7S` |
| `5:00 UTC` | `10.49` | `10.50` | `10.49` | `10.54` | `10.47` | 2,418,538.29 USD | 1,213,398.88 USD | 1,205,139.41 USD | 8,259.48 USD | `+0.34%` | `5B / 7S` |
| `0:00 UTC` | `10.49` | `10.51` | `10.49` | `10.58` | `10.47` | 4,555,787.03 USD | 1,937,641.47 USD | 2,618,145.56 USD | -680,504.09 USD | `-14.94%` | `34B / 12S` |
| `5:00 UTC` | `10.66` | `10.66` | `10.66` | `10.72` | `10.57` | 8,088,225.29 USD | 5,081,569.93 USD | 3,006,655.36 USD | 2,074,914.56 USD | `+25.65%` | `34B / 2S` |
| `0:00 UTC` | `10.71` | `10.70` | `10.71` | `10.73` | `10.66` | 1,927,070.92 USD | 836,968.96 USD | 1,090,101.96 USD | -253,133.01 USD | `-13.14%` | `5B / 12S` |

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
| `5m` | -8,720.00 USD | -399,140.00 USD | **`DISTRIBUTION`** |
| `15m` | -457,050.00 USD | -270,310.00 USD | **`DISTRIBUTION`** |
| `30m` | -147,510.00 USD | 1,450,000.00 USD | **`ACCUMULATION`** |
| `1h` | -633,200.00 USD | -114,980.00 USD | **`DISTRIBUTION`** |
| `2h` | 642,070.00 USD | 3,040,000.00 USD | **`ACCUMULATION`** |
| `4h` | -4,390,000.00 USD | -5,670,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -9,120,000.00 USD | -19,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,970,000.00 USD | -22,520,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,600,000.00 USD | -23,100,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,850,000.00 USD | -21,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,020,000.00 USD | -48,960,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,550,000.00 USD | -199,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-8.72K` | 15m=`-457.05K` | 1h=`-633.20K` | 24h=`-9.85M`
* Futures Capital Netflows: 5m=`-399.14K` | 15m=`-270.31K` | 1h=`-114.98K` | 24h=`-21.84M`
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
  * Execution Entry: `10.22` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `9.92` (Risk Distance: `0.2966` pts)
  * +2.5R Take Profit: `10.96`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.08` (Risk Distance: `0.2966` pts)
  * +2.5R Take Profit: `10.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
