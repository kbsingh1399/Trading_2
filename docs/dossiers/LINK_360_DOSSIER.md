# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.04` | **Live Ask Quote**: `11.14` | **Mid Price**: `11.09`
- **Spread Points**: `92.00` | **Spread BPS**: `82.96 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.63` | VWAP Z-Score: `+1.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0983` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.48` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.37` | Lower -3.00σ Band: `9.90`
  * Upper +2.51σ Band: `11.25` | Lower -2.51σ Band: `10.02`
  * Upper +2.01σ Band: `11.13` | Lower -2.01σ Band: `10.14`
  * Upper +2.00σ Band: `11.13` | Lower -2.00σ Band: `10.14`
  * Upper +1.28σ Band: `10.95` | Lower -1.28σ Band: `10.32`
  * Upper +1.00σ Band: `10.88` | Lower -1.00σ Band: `10.39`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.96` | EMA-20=`10.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.97` (Slope: `+0.0000`) | EMA-100=`11.15`
  * Institutional Anchors: EMA-144=`11.24` | EMA-200=`11.30` (Slope: `-0.4068`) | EMA-233=`11.32`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.94` (Distance: `+1.36%`)
  * Point of Control (POC) = `10.48` (Distance: `+5.79%`)
  * Value Area Low (VAL) = `10.35` (Distance: `+7.13%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.73` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.09` | Low=`10.96`
  * New York Session (13:00-21:00 UTC): High=`11.16` | Low=`11.02`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.05` - `11.13`
  * Optimal Trade Entry (OTE 0.705): `11.11`
  * Structural Invalidation Anchor (0.786): `11.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.06` | `11.07` | `11.03` | `11.05` | `79,087` | 873,757.45 USD | 24,583.46 USD | `+2.81%` | -11,401,938.44 USD | `+0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.05` | `11.09` | `11.05` | `11.08` | `65,679` | 727,113.29 USD | 97,663.10 USD | `+13.43%` | -11,304,275.34 USD | `+0.35` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.07` | `11.12` | `11.07` | `11.11` | `60,001` | 665,646.81 USD | 205,897.18 USD | `+30.93%` | -11,098,378.16 USD | `+0.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.12` | `11.15` | `11.09` | `11.13` | `136,477` | 1,517,756.15 USD | -11,671.83 USD | `-0.77%` | -11,174,197.41 USD | `-0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.13` | `11.14` | `11.05` | `11.05` | `124,938` | 1,386,195.17 USD | -252,324.50 USD | `-18.20%` | -11,426,521.91 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.06` | `11.12` | `11.03` | `11.11` | `204,766` | 2,266,517.55 USD | 328,143.75 USD | `+14.48%` | -11,098,378.16 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.96` | `11.09` | `10.90` | `11.05` | `1,032,622` | 11,357,751.81 USD | 314,374.20 USD | `+2.77%` | -11,594,831.35 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.05` | `11.16` | `11.05` | `11.05` | `560,462` | 6,227,534.15 USD | -214,869.46 USD | `-3.45%` | -11,809,700.81 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.06` | `11.12` | `11.03` | `11.11` | `204,766` | 2,266,517.55 USD | 328,143.75 USD | `+14.48%` | -11,481,557.07 USD | `+0.42` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.11` | `1,797,850` | 19,851,803.51 USD | 427,648.49 USD | `+2.15%` | -11,801,179.57 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,625,285.45 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 595,900.27 USD | `-1.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.11` | `1,797,850` | 19,851,803.51 USD | 427,648.49 USD | `+2.15%` | -11,801,179.57 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`11.09`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `420` | `0xecb6...2b00` | `SHORT` | 5,274,398.76 USD | `474,572,500.00` | `10.66` | `11.11` | `68.73` | -216,095.48 USD | `-4.10%` | `10X Cross` |
| `508` | `0x73ce...8ce9` | `LONG` | 4,444,528.89 USD | `400,011,600.00` | `12.05` | `11.11` | `7.82` | -375,224.82 USD | `-8.44%` | `5X Cross` |
| `845` | `0xb83d...6e36` | `SHORT` | 2,689,006.44 USD | `242,013,000.00` | `12.93` | `11.11` | `531.21` | 440,887.75 USD | `+16.40%` | `3X Cross` |
| `888` | `0x458d...ab3b` | `LONG` | 2,525,301.03 USD | `227,156,700.00` | `13.13` | `11.11` | `9.34` | -456,929.36 USD | `-18.09%` | `3X Isolated` |
| `969` | `0xdd53...2b13` | `SHORT` | 2,294,560.01 USD | `206,475,300.00` | `11.92` | `11.11` | `294.89` | 166,662.92 USD | `+7.26%` | `3X Cross` |
| `994` | `0x3dc9...54b0` | `SHORT` | 2,223,800.00 USD | `200,000,000.00` | `7.56` | `11.11` | `91.83` | -712,641.58 USD | `-32.05%` | `10X Cross` |
| `1008` | `0x45d2...4029` | `SHORT` | 2,172,005.00 USD | `195,500,000.00` | `11.54` | `11.11` | `213.47` | 84,478.43 USD | `+3.89%` | `10X Cross` |
| `1177` | `0x6540...f7b7` | `LONG` | 1,872,740.49 USD | `168,563,500.00` | `12.40` | `11.11` | `6.69` | -217,998.50 USD | `-11.64%` | `5X Isolated` |
| `1263` | `0xeadc...9d55` | `LONG` | 1,752,742.13 USD | `157,691,600.00` | `9.43` | `11.11` | `0.000000` | 266,087.23 USD | `+15.18%` | `10X Cross` |
| `1469` | `0x5b5d...c060` | `SHORT` | 1,464,684.68 USD | `131,775,500.00` | `13.61` | `11.11` | `1175.98` | 328,573.29 USD | `+22.43%` | `3X Cross` |
| `1645` | `0xf6f3...47f8` | `SHORT` | 1,277,578.23 USD | `115,024,600.00` | `11.42` | `11.11` | `19.05` | 35,751.95 USD | `+2.80%` | `5X Cross` |
| `1820` | `0xfe7e...11b4` | `LONG` | 1,123,687.62 USD | `101,142,000.00` | `14.47` | `11.11` | `5.32` | -339,425.53 USD | `-30.21%` | `5X Isolated` |
| `1829` | `0x9df2...c665` | `SHORT` | 1,120,204.35 USD | `100,819,400.00` | `11.48` | `11.11` | `307.52` | 37,303.90 USD | `+3.33%` | `10X Cross` |
| `1856` | `0x8af7...fa05` | `SHORT` | 1,096,125.93 USD | `98,661,200.00` | `14.08` | `11.11` | `202.25` | 293,056.61 USD | `+26.74%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.34` | 5,385.66 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.39K USD at 11.3430 USD [API] | `2026-10-29 03:41:10` |
| `ANNOUNCEMENT` | `INFO` | `11.34` | 7,509.07 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.3430 USD [API] | `2026-10-29 03:41:10` |
| `ANNOUNCEMENT` | `INFO` | `11.38` | 6,666.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.67K USD at 11.3800 USD [API] | `2026-10-29 03:43:32` |
| `ANNOUNCEMENT` | `INFO` | `18.50` | 3,700.00 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 3.70K USD at 18.5000 USD [API] | `2025-10-10 21:13:14` |
| `ANNOUNCEMENT` | `INFO` | `11.37` | 6,213.75 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.21K USD at 11.3680 USD [API] | `2026-10-29 04:01:21` |
| `ANNOUNCEMENT` | `INFO` | `11.36` | 8,887.56 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.89K USD at 11.3550 USD [API] | `2026-10-29 04:05:44` |
| `ANNOUNCEMENT` | `INFO` | `11.36` | 9,026.09 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 9.03K USD at 11.3550 USD [API] | `2026-10-29 04:05:44` |
| `ANNOUNCEMENT` | `INFO` | `11.41` | 7,236.98 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.24K USD at 11.4130 USD [API] | `2026-10-29 08:11:19` |
| `ANNOUNCEMENT` | `INFO` | `11.41` | 5,466.83 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.4130 USD [API] | `2026-10-29 08:11:19` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+0.97%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.31%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+0.96%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.32%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+0.96%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.32%`)
  * 7D Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+0.97%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.31%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 9,250.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 681.62 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 10,480.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,290.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 236.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,060.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 9,750.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 10,690.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 479.61 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 41,620.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,790.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,160.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 9,000.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 43,500.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 7,310.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 232,040.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 1,550.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 6,230.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 85,490.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 1,550.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,840.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 16,490.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 9,670.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 37,480.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 276.57 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 6,520.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 5,880.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 18,870.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 768.75 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 36,210.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 58,250.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 15,600.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 24,200.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 41,520.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 61,770.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 75,890.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 675,380.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 21,170.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 26,260.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 46,480.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 155,010.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 22,970.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 5,660.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 12,640.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,110.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 84,410.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 37,390.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 34,340.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 11,470.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 351,590.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,960.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,160.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 26,500.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 79,700.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 451,200.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 87,280.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.10` | 15,020,000.00 USD | 15,020,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.12` | 14,930,000.00 USD | 14,930,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.14` | 14,880,000.00 USD | 14,880,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.16` | 14,830,000.00 USD | 14,830,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.18` | 14,770,000.00 USD | 14,770,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.20` | 14,720,000.00 USD | 14,720,000.00 USD | 14,540.00 USD | 8,360.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.22` | 14,690,000.00 USD | 14,690,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.24` | 14,680,000.00 USD | 14,680,000.00 USD | 717.27 USD | 8,580.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,830.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.26` | 14,640,000.00 USD | 14,640,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.28` | 14,600,000.00 USD | 14,600,000.00 USD | 460.95 USD | 5,490.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.30` | 14,590,000.00 USD | 14,590,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.32` | 14,530,000.00 USD | 14,530,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 14,500,000.00 USD | 14,500,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 14,450,000.00 USD | 14,450,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 14,450,000.00 USD | 14,450,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 14,420,000.00 USD | 14,420,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 14,380,000.00 USD | 14,380,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 14,340,000.00 USD | 14,340,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 47,130.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 14,280,000.00 USD | 14,280,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 14,180,000.00 USD | 14,180,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 14,180,000.00 USD | 14,180,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 14,120,000.00 USD | 14,120,000.00 USD | 472.74 USD | 15,010.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 101,260.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 14,100,000.00 USD | 14,100,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 14,010,000.00 USD | 14,010,000.00 USD | 38,760.00 USD | 722.15 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 13,970,000.00 USD | 13,970,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 13,760,000.00 USD | 13,760,000.00 USD | 5,420.00 USD | 0.00 USD | 219.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 13,750,000.00 USD | 13,750,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 202,330.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 13,730,000.00 USD | 13,730,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 13,690,000.00 USD | 13,690,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 13,650,000.00 USD | 13,650,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 64,130.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 13,650,000.00 USD | 13,650,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 13,570,000.00 USD | 13,570,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 13,480,000.00 USD | 13,480,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 9,000,000.00 USD | 9,000,000.00 USD | 105,520.00 USD | 20,760.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 13,390,000.00 USD | 13,390,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.85` | 8,850,000.00 USD | 8,850,000.00 USD | 10,990.00 USD | 7,050.00 USD | 397.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 36,950.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.86` | 13,320,000.00 USD | 13,320,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.87` | 8,830,000.00 USD | 8,830,000.00 USD | 14,610.00 USD | 4,120.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 13,300,000.00 USD | 13,300,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.89` | 8,800,000.00 USD | 8,800,000.00 USD | 8,400.00 USD | 8,240.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 13,280,000.00 USD | 13,280,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 8,770,000.00 USD | 8,770,000.00 USD | 30,130.00 USD | 32,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 8,710,000.00 USD | 8,710,000.00 USD | 13,840.00 USD | 12,020.00 USD | 219.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 13,210,000.00 USD | 13,210,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 8,680,000.00 USD | 8,680,000.00 USD | 9,450.00 USD | 7,200.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 422,540.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.96` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 11,410.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.97` | 8,660,000.00 USD | 8,660,000.00 USD | 68,690.00 USD | 7,890.00 USD | 53,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 13,110,000.00 USD | 13,110,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 8,530,000.00 USD | 8,530,000.00 USD | 3,940.00 USD | 6,390.00 USD | 63,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 8,450,000.00 USD | 8,450,000.00 USD | 5,720.00 USD | 726.47 USD | 24,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 13,030,000.00 USD | 13,030,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 8,420,000.00 USD | 8,420,000.00 USD | 6,170.00 USD | 12,900.00 USD | 264.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 13,020,000.00 USD | 13,020,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 8,400,000.00 USD | 8,400,000.00 USD | 38,520.00 USD | 555.00 USD | 18,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 779,830.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.06` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.07` | 8,340,000.00 USD | 8,340,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 12,930,000.00 USD | 12,930,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 8,180,000.00 USD | 8,180,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 12,600,000.00 USD | 12,600,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 8,060,000.00 USD | 8,060,000.00 USD | 7,530.00 USD | 41,480.00 USD | 123.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 12,590,000.00 USD | 12,590,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 8,010,000.00 USD | 8,010,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 12,530,000.00 USD | 12,530,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 7,940,000.00 USD | 7,940,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 67,260.00 USD | 255,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.16` | 12,210,000.00 USD | 12,210,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.17` | 7,870,000.00 USD | 7,870,000.00 USD | 127,800.00 USD | 25,060.00 USD | 640.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 12,160,000.00 USD | 12,160,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 7,710,000.00 USD | 7,710,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 12,030,000.00 USD | 12,030,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 7,400,000.00 USD | 7,400,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 11,510,000.00 USD | 11,510,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 6,950,000.00 USD | 6,950,000.00 USD | 105,610.00 USD | 61,740.00 USD | 291,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 10,970,000.00 USD | 10,970,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 6,490,000.00 USD | 6,490,000.00 USD | 16,630.00 USD | 27,140.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 46,010.00 USD | 188,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 10,520,000.00 USD | 10,520,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.27` | 6,410,000.00 USD | 6,410,000.00 USD | 69,790.00 USD | 18,820.00 USD | 134,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 10,140,000.00 USD | 10,140,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 6,190,000.00 USD | 6,190,000.00 USD | 335,550.00 USD | 2,000.00 USD | 163,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 9,800,000.00 USD | 9,800,000.00 USD | 457,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 5,690,000.00 USD | 5,690,000.00 USD | 19,560.00 USD | 19,240.00 USD | 52,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 9,340,000.00 USD | 9,340,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 5,600,000.00 USD | 5,600,000.00 USD | 14,540.00 USD | 3,820.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 9,200,000.00 USD | 9,200,000.00 USD | 56,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 5,530,000.00 USD | 5,530,000.00 USD | 60,790.00 USD | 6,620.00 USD | 72,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,590.00 USD | 142,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 9,150,000.00 USD | 9,150,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.37` | 5,390,000.00 USD | 5,390,000.00 USD | 11,970.00 USD | 13,750.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 8,750,000.00 USD | 8,750,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 5,350,000.00 USD | 5,350,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 8,740,000.00 USD | 8,740,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 5,190,000.00 USD | 5,190,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 8,390,000.00 USD | 8,390,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 5,010,000.00 USD | 5,010,000.00 USD | 311,620.00 USD | 0.00 USD | 88,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 8,060,000.00 USD | 8,060,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 4,610,000.00 USD | 4,610,000.00 USD | 329,110.00 USD | 44,950.00 USD | 216,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 643.72 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.46` | 7,270,000.00 USD | 7,270,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.47` | 4,020,000.00 USD | 4,020,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 6,850,000.00 USD | 6,850,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 3,920,000.00 USD | 3,920,000.00 USD | 41,670.00 USD | 38,130.00 USD | 25,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 6,630,000.00 USD | 6,630,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 3,820,000.00 USD | 3,820,000.00 USD | 11,220.00 USD | 10,370.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 3,780,000.00 USD | 3,780,000.00 USD | 71.67 USD | 18,090.00 USD | 117,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 3,650,000.00 USD | 3,650,000.00 USD | 65,860.00 USD | 48,330.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 596.08 USD | 909.19 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.56` | 6,500,000.00 USD | 6,500,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.57` | 3,480,000.00 USD | 3,480,000.00 USD | 39,860.00 USD | 21,900.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 3,410,000.00 USD | 3,410,000.00 USD | 18,130.00 USD | 18,010.00 USD | 15,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 458.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 3,750.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 6,300,000.00 USD | 6,300,000.00 USD | 59,050.00 USD | 0.00 USD | 180.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 3,340,000.00 USD | 3,340,000.00 USD | 11,820.00 USD | 1,170.00 USD | 102,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 6,250,000.00 USD | 6,250,000.00 USD | 11,150.00 USD | 0.00 USD | 150.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 3,230,000.00 USD | 3,230,000.00 USD | 30,790.00 USD | 4,060.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 313.11 USD | 313.11 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.66` | 6,230,000.00 USD | 6,230,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.67` | 3,170,000.00 USD | 3,170,000.00 USD | 40,350.00 USD | 9,610.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 3,100,000.00 USD | 3,100,000.00 USD | 12,670.00 USD | 6,950.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 6,210,000.00 USD | 6,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 2,900,000.00 USD | 2,900,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 2,820,000.00 USD | 2,820,000.00 USD | 89,590.00 USD | 8,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 5,600,000.00 USD | 5,600,000.00 USD | 16,310.00 USD | 109,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.77` | 2,720,000.00 USD | 2,720,000.00 USD | 22,390.00 USD | 62,040.00 USD | 51,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 5,470,000.00 USD | 5,470,000.00 USD | 535,020.00 USD | 32,650.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 2,580,000.00 USD | 2,580,000.00 USD | 167,900.00 USD | 118,040.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 4,800,000.00 USD | 4,800,000.00 USD | 23,450.00 USD | 70,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 2,290,000.00 USD | 2,290,000.00 USD | 13,650.00 USD | 5,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 56,610.00 USD | 206,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.83` | 2,270,000.00 USD | 2,270,000.00 USD | 315,520.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 4,450,000.00 USD | 4,450,000.00 USD | 295,700.00 USD | 80,420.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.85` | 1,950,000.00 USD | 1,950,000.00 USD | 87,770.00 USD | 14,590.00 USD | 148,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 3,870,000.00 USD | 3,870,000.00 USD | 323,850.00 USD | 3,610.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.87` | 1,700,000.00 USD | 1,700,000.00 USD | 60,390.00 USD | 6,510.00 USD | 446.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 3,210,000.00 USD | 3,210,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.89` | 1,630,000.00 USD | 1,630,000.00 USD | 22,380.00 USD | 3,380.00 USD | 30,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 220,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.91` | 1,570,000.00 USD | 1,570,000.00 USD | 117,890.00 USD | 904.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 2,490,000.00 USD | 2,490,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.93` | 1,460,000.00 USD | 1,460,000.00 USD | 3,920.00 USD | 1,010.00 USD | 86.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 2,160,000.00 USD | 2,160,000.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.95` | 1,450,000.00 USD | 1,450,000.00 USD | 1,550.00 USD | 1,320.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 2,150,000.00 USD | 2,150,000.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.97` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 101.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 2,090,000.00 USD | 2,090,000.00 USD | 17,930.00 USD | 0.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.99` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 467.00 USD | 251.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 1,870,000.00 USD | 1,870,000.00 USD | 10,830.00 USD | 2,280.00 USD | 634.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.01` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 3,040.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 1,850,000.00 USD | 1,850,000.00 USD | 7,900.00 USD | 31,180.00 USD | 143,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.03` | 1,360,000.00 USD | 1,360,000.00 USD | 44,040.00 USD | 43,470.00 USD | 304,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 1,670,000.00 USD | 1,670,000.00 USD | 17,850.00 USD | 40,210.00 USD | 178,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.05` | 962,970.00 USD | 962,970.00 USD | 306,560.00 USD | 5,150.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 1,430,000.00 USD | 1,430,000.00 USD | 4,020.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.07` | 544,880.00 USD | 544,880.00 USD | 329,150.00 USD | 46,170.00 USD | 169,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 1,300,000.00 USD | 1,300,000.00 USD | 14,890.00 USD | 1,810.00 USD | 167,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 477,080.00 USD | 477,080.00 USD | 105,500.00 USD | 69,450.00 USD | 302,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 1,110,000.00 USD | 1,110,000.00 USD | 301,790.00 USD | 23,300.00 USD | 173,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 539,320.00 USD | 539,320.00 USD | 9,550.00 USD | 52,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 612,850.00 USD | 612,850.00 USD | 262,770.00 USD | 115,910.00 USD | 234,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 1,280,000.00 USD | 1,280,000.00 USD | 438,340.00 USD | 99,350.00 USD | 204,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 215,120.00 USD | 215,120.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 430,230.00 USD | 430,230.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 1,590,000.00 USD | 1,590,000.00 USD | 198,370.00 USD | 61,430.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.16` | 699,610.00 USD | 699,610.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 1,730,000.00 USD | 1,730,000.00 USD | 22,450.00 USD | 53,650.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 717,100.00 USD | 717,100.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 1,870,000.00 USD | 1,870,000.00 USD | 72,050.00 USD | 28,650.00 USD | 40,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 1,050,000.00 USD | 1,050,000.00 USD | 171,840.00 USD | 78,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 2,250,000.00 USD | 2,250,000.00 USD | 160,950.00 USD | 59,630.00 USD | 164,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 1,560,000.00 USD | 1,560,000.00 USD | 482,460.00 USD | 28,690.00 USD | 603.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 2,670,000.00 USD | 2,670,000.00 USD | 262,260.00 USD | 37,760.00 USD | 118,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 1,870,000.00 USD | 1,870,000.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 2,970,000.00 USD | 2,970,000.00 USD | 108,110.00 USD | 39,180.00 USD | 147,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 882.00 USD | 882.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.26` | 2,690,000.00 USD | 2,690,000.00 USD | 520,990.00 USD | 0.00 USD | 296,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.27` | 3,450,000.00 USD | 3,450,000.00 USD | 310,520.00 USD | 4,350.00 USD | 173,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 3,240,000.00 USD | 3,240,000.00 USD | 347,470.00 USD | 57,050.00 USD | 147,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 3,980,000.00 USD | 3,980,000.00 USD | 176,550.00 USD | 119,460.00 USD | 225,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 3,320,000.00 USD | 3,320,000.00 USD | 24,980.00 USD | 32,240.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 4,230,000.00 USD | 4,230,000.00 USD | 123,640.00 USD | 68,310.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 3,820,000.00 USD | 3,820,000.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 4,500,000.00 USD | 4,500,000.00 USD | 164,560.00 USD | 34,060.00 USD | 62,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 4,130,000.00 USD | 4,130,000.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 4,980,000.00 USD | 4,980,000.00 USD | 296,410.00 USD | 103,310.00 USD | 84,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.36` | 4,380,000.00 USD | 4,380,000.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.37` | 5,270,000.00 USD | 5,270,000.00 USD | 152,070.00 USD | 91,520.00 USD | 47,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 4,620,000.00 USD | 4,620,000.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 5,340,000.00 USD | 5,340,000.00 USD | 14,820.00 USD | 47,470.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 5,610,000.00 USD | 5,610,000.00 USD | 96,590.00 USD | 35,740.00 USD | 140,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 4,890,000.00 USD | 4,890,000.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 5,870,000.00 USD | 5,870,000.00 USD | 64,580.00 USD | 56,490.00 USD | 132,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 5,320,000.00 USD | 5,320,000.00 USD | 303,190.00 USD | 95,260.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 6,050,000.00 USD | 6,050,000.00 USD | 77,400.00 USD | 83,200.00 USD | 25,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 99,360.00 USD | 55,470.00 USD | 269.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.47` | 6,150,000.00 USD | 6,150,000.00 USD | 56,320.00 USD | 19,720.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 5,680,000.00 USD | 5,680,000.00 USD | 54,660.00 USD | 84,840.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 6,250,000.00 USD | 6,250,000.00 USD | 33,390.00 USD | 27,530.00 USD | 34,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 5,810,000.00 USD | 5,810,000.00 USD | 91,790.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 6,350,000.00 USD | 6,350,000.00 USD | 41,360.00 USD | 29,500.00 USD | 30,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 5,760.00 USD | 33,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 6,470,000.00 USD | 6,470,000.00 USD | 64,080.00 USD | 17,000.00 USD | 41,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 6,010,000.00 USD | 6,010,000.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 6,610,000.00 USD | 6,610,000.00 USD | 84,610.00 USD | 1,570.00 USD | 53,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 143.22 USD | 1,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.56` | 6,100,000.00 USD | 6,100,000.00 USD | 86,650.00 USD | 793.25 USD | 432.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.57` | 6,730,000.00 USD | 6,730,000.00 USD | 90,730.00 USD | 3,740.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 6,800,000.00 USD | 6,800,000.00 USD | 17,210.00 USD | 7,660.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 6,210,000.00 USD | 6,210,000.00 USD | 44,670.00 USD | 10,510.00 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 7,000,000.00 USD | 7,000,000.00 USD | 118,210.00 USD | 512.95 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 6,270,000.00 USD | 6,270,000.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 7,040,000.00 USD | 7,040,000.00 USD | 2,580.00 USD | 6,700.00 USD | 31,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 6,320,000.00 USD | 6,320,000.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 7,050,000.00 USD | 7,050,000.00 USD | 2,630.00 USD | 7,840.00 USD | 46.76 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 7,370.00 USD | 8,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.66` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.67` | 7,140,000.00 USD | 7,140,000.00 USD | 19,420.00 USD | 11,530.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 7,280,000.00 USD | 7,280,000.00 USD | 105,590.00 USD | 34,170.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 6,550,000.00 USD | 6,550,000.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 7,380,000.00 USD | 7,380,000.00 USD | 74,220.00 USD | 13,000.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 6,880,000.00 USD | 6,880,000.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 7,650,000.00 USD | 7,650,000.00 USD | 139,320.00 USD | 11,770.00 USD | 120,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 7,770,000.00 USD | 7,770,000.00 USD | 21,990.00 USD | 38,420.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 7,070,000.00 USD | 7,070,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 7,850,000.00 USD | 7,850,000.00 USD | 41,580.00 USD | 20,480.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 7,130,000.00 USD | 7,130,000.00 USD | 8,130.00 USD | 0.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 7,900,000.00 USD | 7,900,000.00 USD | 12,300.00 USD | 339.50 USD | 40,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 7,270,000.00 USD | 7,270,000.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 18,040.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 7,500,000.00 USD | 7,500,000.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 7,990,000.00 USD | 7,990,000.00 USD | 11,070.00 USD | 11,560.00 USD | 29,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 7,750,000.00 USD | 7,750,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 8,170,000.00 USD | 8,170,000.00 USD | 82,060.00 USD | 9,720.00 USD | 84,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 8,260,000.00 USD | 8,260,000.00 USD | 20,010.00 USD | 20,660.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 7,820,000.00 USD | 7,820,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 8,360,000.00 USD | 8,360,000.00 USD | 43,100.00 USD | 13,220.00 USD | 43,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 7,870,000.00 USD | 7,870,000.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 8,520,000.00 USD | 8,520,000.00 USD | 102,960.00 USD | 18,290.00 USD | 31,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 8,080,000.00 USD | 8,080,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 8,710,000.00 USD | 8,710,000.00 USD | 135,130.00 USD | 28,280.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 8,270,000.00 USD | 8,270,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 8,860,000.00 USD | 8,860,000.00 USD | 84,850.00 USD | 20,680.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 8,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.96` | 8,450,000.00 USD | 8,450,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 9,050,000.00 USD | 9,050,000.00 USD | 71,640.00 USD | 36,230.00 USD | 87,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 9,110,000.00 USD | 9,110,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 9,220,000.00 USD | 9,220,000.00 USD | 108,260.00 USD | 27,660.00 USD | 36,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 9,740,000.00 USD | 9,740,000.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 9,330,000.00 USD | 9,330,000.00 USD | 47,510.00 USD | 9,290.00 USD | 50,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 10,310,000.00 USD | 10,310,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 9,440,000.00 USD | 9,440,000.00 USD | 47,360.00 USD | 34,660.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 10,940,000.00 USD | 10,940,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 9,650,000.00 USD | 9,650,000.00 USD | 108,910.00 USD | 43,590.00 USD | 59,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 11,440,000.00 USD | 11,440,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 9,790,000.00 USD | 9,790,000.00 USD | 34,850.00 USD | 33,440.00 USD | 67,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 12,110,000.00 USD | 12,110,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 9,860,000.00 USD | 9,860,000.00 USD | 20,990.00 USD | 24,720.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 12,290,000.00 USD | 12,290,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 10,060,000.00 USD | 10,060,000.00 USD | 101,970.00 USD | 38,270.00 USD | 55,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 12,670,000.00 USD | 12,670,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 10,220,000.00 USD | 10,220,000.00 USD | 93,390.00 USD | 33,860.00 USD | 39,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 13,030,000.00 USD | 13,030,000.00 USD | 147,420.00 USD | 92,520.00 USD | 119,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 10,440,000.00 USD | 10,440,000.00 USD | 113,520.00 USD | 42,340.00 USD | 65,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 13,440,000.00 USD | 13,440,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 10,690,000.00 USD | 10,690,000.00 USD | 118,100.00 USD | 60,070.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 13,580,000.00 USD | 13,580,000.00 USD | 57,680.00 USD | 54,220.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 10,790,000.00 USD | 10,790,000.00 USD | 59,950.00 USD | 24,020.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 13,920,000.00 USD | 13,920,000.00 USD | 194,760.00 USD | 51,940.00 USD | 91,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 10,890,000.00 USD | 10,890,000.00 USD | 32,170.00 USD | 28,710.00 USD | 45,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 14,340,000.00 USD | 14,340,000.00 USD | 261,490.00 USD | 56,190.00 USD | 106,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 10,930,000.00 USD | 10,930,000.00 USD | 7,370.00 USD | 18,230.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 14,580,000.00 USD | 14,580,000.00 USD | 70,650.00 USD | 54,230.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 10,940,000.00 USD | 10,940,000.00 USD | 2,260.00 USD | 3,780.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 10,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.26` | 14,880,000.00 USD | 14,880,000.00 USD | 192,800.00 USD | 55,780.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.27` | 11,010,000.00 USD | 11,010,000.00 USD | 38,860.00 USD | 8,240.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 15,300,000.00 USD | 15,300,000.00 USD | 215,790.00 USD | 52,850.00 USD | 148,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 11,050,000.00 USD | 11,050,000.00 USD | 23,030.00 USD | 9,300.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 11,060,000.00 USD | 11,060,000.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 15,640,000.00 USD | 15,640,000.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 15,710,000.00 USD | 15,710,000.00 USD | 22,620.00 USD | 25,760.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 15,790,000.00 USD | 15,790,000.00 USD | 48,630.00 USD | 18,250.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 15,870,000.00 USD | 15,870,000.00 USD | 36,210.00 USD | 24,190.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 15,940,000.00 USD | 15,940,000.00 USD | 7,170.00 USD | 6,880.00 USD | 55,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 16,100,000.00 USD | 16,100,000.00 USD | 111,350.00 USD | 41,100.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 16,160,000.00 USD | 16,160,000.00 USD | 23,200.00 USD | 21,440.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 16,280,000.00 USD | 16,280,000.00 USD | 81,360.00 USD | 284.67 USD | 45,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 16,430,000.00 USD | 16,430,000.00 USD | 39,540.00 USD | 25,610.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 16,550,000.00 USD | 16,550,000.00 USD | 31,320.00 USD | 18,070.00 USD | 63,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 16,790,000.00 USD | 16,790,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 17,100,000.00 USD | 17,100,000.00 USD | 163,610.00 USD | 33,380.00 USD | 113,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 17,360,000.00 USD | 17,360,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,070.00 USD | 12,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.56` | 17,480,000.00 USD | 17,480,000.00 USD | 77,880.00 USD | 20,220.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 17,600,000.00 USD | 17,600,000.00 USD | 41,760.00 USD | 34,570.00 USD | 41,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 17,750,000.00 USD | 17,750,000.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 17,820,000.00 USD | 17,820,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 17,950,000.00 USD | 17,950,000.00 USD | 63,450.00 USD | 42,320.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 779.24 USD | 12,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.66` | 17,990,000.00 USD | 17,990,000.00 USD | 22,530.00 USD | 5,030.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 18,050,000.00 USD | 18,050,000.00 USD | 9,270.00 USD | 18,330.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 18,110,000.00 USD | 18,110,000.00 USD | 2,010.00 USD | 617.78 USD | 52,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 18,220,000.00 USD | 18,220,000.00 USD | 47,740.00 USD | 22,750.00 USD | 40,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 18,330,000.00 USD | 18,330,000.00 USD | 38,570.00 USD | 26,370.00 USD | 40,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 18,380,000.00 USD | 18,380,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 18,560,000.00 USD | 18,560,000.00 USD | 109,130.00 USD | 16,110.00 USD | 52,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 18,650,000.00 USD | 18,650,000.00 USD | 13,700.00 USD | 14,000.00 USD | 61,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 18,670,000.00 USD | 18,670,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 18,720,000.00 USD | 18,720,000.00 USD | 31,320.00 USD | 15,990.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 18,790,000.00 USD | 18,790,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 18,830,000.00 USD | 18,830,000.00 USD | 23,610.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 18,910,000.00 USD | 18,910,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 19,000,000.00 USD | 19,000,000.00 USD | 50,620.00 USD | 13,030.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 19,030,000.00 USD | 19,030,000.00 USD | 27,900.00 USD | 1,070.00 USD | 69.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 19,080,000.00 USD | 19,080,000.00 USD | 13,150.00 USD | 11,970.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 19,120,000.00 USD | 19,120,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 19,200,000.00 USD | 19,200,000.00 USD | 51,470.00 USD | 9,560.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 19,210,000.00 USD | 19,210,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 19,210,000.00 USD | 19,210,000.00 USD | 303.50 USD | 335.85 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 544.19 USD | 13,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.06` | 19,240,000.00 USD | 19,240,000.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.08` | 19,280,000.00 USD | 19,280,000.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 18,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 111,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 4,110.00 USD | 115,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 2,950.00 USD | 118,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 896.33 USD | 119,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 145,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 156.57 USD | 145,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 145,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 146,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 146,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 17,190.00 USD | 163,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 164,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 24,770.00 USD | 189,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 91,440.00 USD | 281,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 360,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 26,240.00 USD | 387,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 388,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 5,360.00 USD | 393,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 115.83 USD | 393,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 102.37 USD | 394,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 276,760.00 USD | 670,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 671,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 673,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 75,750.00 USD | 748,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 921.94 USD | 749,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 749,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 2,450.00 USD | 752,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 2,190,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 725,920.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 63,080.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 1,110.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,060,000.00 USD | 0.00 USD | 9,250.00 USD | `-79.69%` | `4,110,700.00` |
| `Live` | `Long` | `2.55` | 12,050,000.00 USD | 0.00 USD | 681.62 USD | `-76.99%` | `267,300.00` |
| `Live` | `Long` | `2.65` | 12,050,000.00 USD | 0.00 USD | 10,480.00 USD | `-76.09%` | `3,953,000.00` |
| `Live` | `Long` | `2.75` | 12,040,000.00 USD | 0.00 USD | 1,290.00 USD | `-75.18%` | `467,300.00` |
| `Live` | `Long` | `2.95` | 12,030,000.00 USD | 0.00 USD | 236.00 USD | `-73.38%` | `80,000.00` |
| `Live` | `Long` | `3.05` | 12,030,000.00 USD | 0.00 USD | 7,060.00 USD | `-72.48%` | `2,314,200.00` |
| `Live` | `Long` | `3.15` | 12,030,000.00 USD | 0.00 USD | 297.99 USD | `-71.57%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 12,030,000.00 USD | 0.00 USD | 9,750.00 USD | `-70.67%` | `2,999,500.00` |
| `Live` | `Long` | `3.35` | 12,020,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.77%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,020,000.00 USD | 0.00 USD | 10,690.00 USD | `-68.87%` | `3,099,300.00` |
| `Live` | `Long` | `3.55` | 12,000,000.00 USD | 0.00 USD | 479.61 USD | `-67.96%` | `135,100.00` |
| `Live` | `Long` | `3.65` | 12,000,000.00 USD | 0.00 USD | 2,190.00 USD | `-67.06%` | `600,000.00` |
| `Live` | `Long` | `3.75` | 12,000,000.00 USD | 0.00 USD | 41,620.00 USD | `-66.16%` | `11,097,900.00` |
| `Live` | `Long` | `3.95` | 11,960,000.00 USD | 0.00 USD | 4,790.00 USD | `-64.35%` | `1,211,500.00` |
| `Live` | `Long` | `4.05` | 11,960,000.00 USD | 0.00 USD | 6,160.00 USD | `-63.45%` | `1,521,700.00` |
| `Live` | `Long` | `4.25` | 11,950,000.00 USD | 0.00 USD | 9,000.00 USD | `-61.65%` | `2,117,900.00` |
| `Live` | `Long` | `4.35` | 11,940,000.00 USD | 0.00 USD | 43,500.00 USD | `-60.74%` | `10,000,000.00` |
| `Live` | `Long` | `4.45` | 11,900,000.00 USD | 0.00 USD | 7,310.00 USD | `-59.84%` | `1,642,500.00` |
| `Live` | `Long` | `4.65` | 11,890,000.00 USD | 0.00 USD | 232,040.00 USD | `-58.04%` | `49,900,600.00` |
| `Live` | `Long` | `4.75` | 11,660,000.00 USD | 0.00 USD | 1,550.00 USD | `-57.13%` | `326,000.00` |
| `Live` | `Long` | `4.85` | 11,660,000.00 USD | 0.00 USD | 6,230.00 USD | `-56.23%` | `1,284,400.00` |
| `Live` | `Long` | `4.95` | 11,650,000.00 USD | 0.00 USD | 85,490.00 USD | `-55.33%` | `17,270,100.00` |
| `Live` | `Long` | `5.05` | 11,560,000.00 USD | 0.00 USD | 217.66 USD | `-54.43%` | `43,100.00` |
| `Live` | `Long` | `5.15` | 11,560,000.00 USD | 0.00 USD | 1,550.00 USD | `-53.52%` | `301,800.00` |
| `Live` | `Long` | `5.25` | 11,560,000.00 USD | 0.00 USD | 5,840.00 USD | `-52.62%` | `1,111,800.00` |
| `Live` | `Long` | `5.35` | 11,560,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.72%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,010,000.00 USD | 0.00 USD | 16,490.00 USD | `-50.82%` | `3,025,500.00` |
| `Live` | `Long` | `5.55` | 11,000,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.91%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 10,990,000.00 USD | 0.00 USD | 37,480.00 USD | `-49.01%` | `6,632,800.00` |
| `Live` | `Long` | `5.75` | 10,950,000.00 USD | 0.00 USD | 276.57 USD | `-48.11%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 10,950,000.00 USD | 0.00 USD | 6,520.00 USD | `-47.21%` | `1,114,400.00` |
| `Live` | `Long` | `5.95` | 10,940,000.00 USD | 0.00 USD | 5,880.00 USD | `-46.30%` | `988,600.00` |
| `Live` | `Long` | `6.05` | 10,940,000.00 USD | 0.00 USD | 18,870.00 USD | `-45.40%` | `3,119,000.00` |
| `Live` | `Long` | `6.15` | 10,920,000.00 USD | 0.00 USD | 768.75 USD | `-44.50%` | `125,000.00` |
| `Live` | `Long` | `6.25` | 10,920,000.00 USD | 0.00 USD | 36,210.00 USD | `-43.60%` | `5,793,400.00` |
| `Live` | `Long` | `6.35` | 10,880,000.00 USD | 0.00 USD | 58,250.00 USD | `-42.69%` | `9,173,800.00` |
| `Live` | `Long` | `6.45` | 10,820,000.00 USD | 0.00 USD | 15,600.00 USD | `-41.79%` | `2,418,300.00` |
| `Live` | `Long` | `6.55` | 10,810,000.00 USD | 0.00 USD | 24,200.00 USD | `-40.89%` | `3,694,800.00` |
| `Live` | `Long` | `6.65` | 10,780,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.99%` | `170,064,000.00` |
| `Live` | `Long` | `6.75` | 9,650,000.00 USD | 0.00 USD | 41,520.00 USD | `-39.08%` | `6,151,700.00` |
| `Live` | `Long` | `6.85` | 9,610,000.00 USD | 0.00 USD | 61,770.00 USD | `-38.18%` | `9,017,500.00` |
| `Live` | `Long` | `6.95` | 9,550,000.00 USD | 0.00 USD | 75,890.00 USD | `-37.28%` | `10,919,300.00` |
| `Live` | `Long` | `7.05` | 9,470,000.00 USD | 0.00 USD | 675,380.00 USD | `-36.38%` | `95,799,200.00` |
| `Live` | `Long` | `7.15` | 8,800,000.00 USD | 0.00 USD | 21,170.00 USD | `-35.48%` | `2,960,800.00` |
| `Live` | `Long` | `7.25` | 8,780,000.00 USD | 0.00 USD | 26,260.00 USD | `-34.57%` | `3,622,600.00` |
| `Live` | `Long` | `7.35` | 8,750,000.00 USD | 0.00 USD | 46,480.00 USD | `-33.67%` | `6,323,200.00` |
| `Live` | `Long` | `7.45` | 8,710,000.00 USD | 0.00 USD | 155,010.00 USD | `-32.77%` | `20,806,700.00` |
| `Live` | `Long` | `7.55` | 8,550,000.00 USD | 0.00 USD | 22,970.00 USD | `-31.87%` | `3,043,000.00` |
| `Live` | `Long` | `7.65` | 8,530,000.00 USD | 0.00 USD | 5,660.00 USD | `-30.96%` | `739,900.00` |
| `Live` | `Long` | `7.75` | 8,520,000.00 USD | 0.00 USD | 12,640.00 USD | `-30.06%` | `1,630,600.00` |
| `Live` | `Long` | `7.85` | 8,510,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-29.16%` | `401,172,300.00` |
| `Live` | `Long` | `7.95` | 5,360,000.00 USD | 0.00 USD | 15,110.00 USD | `-28.26%` | `1,900,300.00` |
| `Live` | `Long` | `8.05` | 5,340,000.00 USD | 0.00 USD | 84,410.00 USD | `-27.35%` | `10,486,200.00` |
| `Live` | `Long` | `8.15` | 5,260,000.00 USD | 0.00 USD | 37,390.00 USD | `-26.45%` | `4,587,300.00` |
| `Live` | `Long` | `8.25` | 5,220,000.00 USD | 0.00 USD | 34,340.00 USD | `-25.55%` | `4,162,900.00` |
| `Live` | `Long` | `8.35` | 5,190,000.00 USD | 0.00 USD | 11,470.00 USD | `-24.65%` | `1,374,200.00` |
| `Live` | `Long` | `8.45` | 5,180,000.00 USD | 0.00 USD | 351,590.00 USD | `-23.74%` | `41,608,500.00` |
| `Live` | `Long` | `8.55` | 4,830,000.00 USD | 0.00 USD | 15,960.00 USD | `-22.84%` | `1,866,700.00` |
| `Live` | `Long` | `8.65` | 4,810,000.00 USD | 0.00 USD | 15,160.00 USD | `-21.94%` | `1,752,800.00` |
| `Live` | `Long` | `8.75` | 4,790,000.00 USD | 0.00 USD | 26,500.00 USD | `-21.04%` | `3,028,300.00` |
| `Live` | `Long` | `8.85` | 4,770,000.00 USD | 0.00 USD | 79,700.00 USD | `-20.13%` | `9,005,400.00` |
| `Live` | `Long` | `8.95` | 4,690,000.00 USD | 0.00 USD | 451,200.00 USD | `-19.23%` | `50,413,900.00` |
| `Live` | `Long` | `9.05` | 4,240,000.00 USD | 0.00 USD | 87,280.00 USD | `-18.33%` | `9,643,900.00` |
| `Live` | `Long` | `9.15` | 4,150,000.00 USD | 0.00 USD | 76,340.00 USD | `-17.43%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,070,000.00 USD | 0.00 USD | 17,830.00 USD | `-16.52%` | `1,928,000.00` |
| `Live` | `Long` | `9.35` | 4,060,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.62%` | `229,496,400.00` |
| `Live` | `Long` | `9.45` | 1,910,000.00 USD | 0.00 USD | 47,130.00 USD | `-14.72%` | `4,987,200.00` |
| `Live` | `Long` | `9.55` | 1,860,000.00 USD | 0.00 USD | 101,260.00 USD | `-13.82%` | `10,603,400.00` |
| `Live` | `Long` | `9.65` | 1,760,000.00 USD | 0.00 USD | 202,330.00 USD | `-12.91%` | `20,966,700.00` |
| `Live` | `Long` | `9.75` | 1,560,000.00 USD | 0.00 USD | 64,130.00 USD | `-12.01%` | `6,577,800.00` |
| `Live` | `Long` | `9.85` | 1,490,000.00 USD | 0.00 USD | 36,950.00 USD | `-11.11%` | `3,751,400.00` |
| `Live` | `Long` | `9.95` | 1,460,000.00 USD | 0.00 USD | 422,540.00 USD | `-10.21%` | `42,466,800.00` |
| `Live` | `Long` | `10.05` | 1,040,000.00 USD | 0.00 USD | 779,830.00 USD | `-9.30%` | `77,595,500.00` |
| `Live` | `Long` | `10.15` | 255,420.00 USD | 0.00 USD | 67,260.00 USD | `-8.40%` | `6,626,600.00` |
| `Live` | `Long` | `10.25` | 188,160.00 USD | 0.00 USD | 46,010.00 USD | `-7.50%` | `4,488,900.00` |
| `Live` | `Long` | `10.35` | 142,150.00 USD | 0.00 USD | 140,590.00 USD | `-6.60%` | `13,583,900.00` |
| `Live` | `Long` | `10.45` | 1,550.00 USD | 0.00 USD | 643.72 USD | `-5.69%` | `61,600.00` |
| `Live` | `Long` | `10.55` | 909.19 USD | 0.00 USD | 596.08 USD | `-4.79%` | `56,500.00` |
| `Live` | `Long` | `10.65` | 313.11 USD | 0.00 USD | 313.11 USD | `-3.89%` | `29,400.00` |
| `Live` | `Short` | `11.25` | 882.00 USD | 882.00 USD | 0.00 USD | `+1.53%` | `78,400.00` |
| `Live` | `Short` | `11.45` | 1,130.00 USD | 249.61 USD | 0.00 USD | `+3.33%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 1,270.00 USD | 143.22 USD | 0.00 USD | `+4.23%` | `12,400.00` |
| `Live` | `Short` | `11.65` | 8,650.00 USD | 7,370.00 USD | 0.00 USD | `+5.13%` | `632,900.00` |
| `Live` | `Short` | `11.95` | 8,930.00 USD | 283.21 USD | 0.00 USD | `+7.84%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 10,360.00 USD | 1,430.00 USD | 0.00 USD | `+10.55%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 11,100.00 USD | 736.06 USD | 0.00 USD | `+11.45%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 12,170.00 USD | 1,070.00 USD | 0.00 USD | `+13.26%` | `85,200.00` |
| `Live` | `Short` | `12.65` | 12,950.00 USD | 779.24 USD | 0.00 USD | `+14.16%` | `61,600.00` |
| `Live` | `Short` | `13.05` | 13,490.00 USD | 544.19 USD | 0.00 USD | `+17.77%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 18,920.00 USD | 5,430.00 USD | 0.00 USD | `+21.38%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 111,820.00 USD | 92,890.00 USD | 0.00 USD | `+22.28%` | `6,855,700.00` |
| `Live` | `Short` | `13.85` | 115,920.00 USD | 4,110.00 USD | 0.00 USD | `+24.99%` | `296,400.00` |
| `Live` | `Short` | `14.15` | 118,870.00 USD | 2,950.00 USD | 0.00 USD | `+27.70%` | `208,600.00` |
| `Live` | `Short` | `14.25` | 119,770.00 USD | 896.33 USD | 0.00 USD | `+28.60%` | `62,900.00` |
| `Live` | `Short` | `14.95` | 145,100.00 USD | 25,330.00 USD | 0.00 USD | `+34.92%` | `1,694,600.00` |
| `Live` | `Short` | `15.35` | 145,260.00 USD | 156.57 USD | 0.00 USD | `+38.53%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 145,840.00 USD | 578.46 USD | 0.00 USD | `+40.33%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 146,110.00 USD | 271.04 USD | 0.00 USD | `+43.04%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 146,250.00 USD | 138.76 USD | 0.00 USD | `+43.94%` | `8,700.00` |
| `Live` | `Short` | `16.25` | 163,440.00 USD | 17,190.00 USD | 0.00 USD | `+46.65%` | `1,058,000.00` |
| `Live` | `Short` | `16.35` | 164,830.00 USD | 1,390.00 USD | 0.00 USD | `+47.55%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 189,610.00 USD | 24,770.00 USD | 0.00 USD | `+49.35%` | `1,496,700.00` |
| `Live` | `Short` | `16.75` | 281,040.00 USD | 91,440.00 USD | 0.00 USD | `+51.16%` | `5,459,000.00` |
| `Live` | `Short` | `16.95` | 360,820.00 USD | 79,770.00 USD | 0.00 USD | `+52.96%` | `4,706,300.00` |
| `Live` | `Short` | `17.05` | 387,060.00 USD | 26,240.00 USD | 0.00 USD | `+53.87%` | `1,539,000.00` |
| `Live` | `Short` | `17.15` | 388,420.00 USD | 1,370.00 USD | 0.00 USD | `+54.77%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 393,780.00 USD | 5,360.00 USD | 0.00 USD | `+56.57%` | `309,000.00` |
| `Live` | `Short` | `17.55` | 393,900.00 USD | 115.83 USD | 0.00 USD | `+58.38%` | `6,600.00` |
| `Live` | `Short` | `17.65` | 394,000.00 USD | 102.37 USD | 0.00 USD | `+59.28%` | `5,800.00` |
| `Live` | `Short` | `17.85` | 670,770.00 USD | 276,760.00 USD | 0.00 USD | `+61.09%` | `15,505,000.00` |
| `Live` | `Short` | `17.95` | 671,120.00 USD | 351.82 USD | 0.00 USD | `+61.99%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 673,090.00 USD | 1,970.00 USD | 0.00 USD | `+62.89%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 748,840.00 USD | 75,750.00 USD | 0.00 USD | `+66.50%` | `4,105,800.00` |
| `Live` | `Short` | `18.55` | 749,760.00 USD | 921.94 USD | 0.00 USD | `+67.40%` | `49,700.00` |
| `Live` | `Short` | `18.65` | 749,950.00 USD | 186.50 USD | 0.00 USD | `+68.31%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 752,400.00 USD | 2,450.00 USD | 0.00 USD | `+70.11%` | `129,800.00` |
| `Live` | `Short` | `19.05` | 2,940,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+71.92%` | `115,024,600.00` |
| `Live` | `Short` | `19.25` | 3,670,000.00 USD | 725,920.00 USD | 0.00 USD | `+73.72%` | `37,710,000.00` |
| `Live` | `Short` | `19.55` | 3,670,000.00 USD | 316.71 USD | 0.00 USD | `+76.43%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,710,000.00 USD | 38,790.00 USD | 0.00 USD | `+77.33%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,710,000.00 USD | 359.45 USD | 0.00 USD | `+78.23%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,710,000.00 USD | 291.27 USD | 0.00 USD | `+80.04%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,710,000.00 USD | 1,260.00 USD | 0.00 USD | `+81.84%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,710,000.00 USD | 1,770.00 USD | 0.00 USD | `+84.55%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+85.45%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,720,000.00 USD | 114.68 USD | 0.00 USD | `+88.16%` | `5,500.00` |
| `Live` | `Short` | `21.75` | 3,780,000.00 USD | 63,080.00 USD | 0.00 USD | `+96.28%` | `2,900,400.00` |
| `Live` | `Short` | `21.95` | 3,780,000.00 USD | 1,110.00 USD | 0.00 USD | `+98.09%` | `50,600.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 470,320.00 USD | 0.00 USD | 182.03 USD | `-77.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 470,140.00 USD | 0.00 USD | 234.23 USD | `-73.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 469,900.00 USD | 0.00 USD | 209.48 USD | `-71.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 469,690.00 USD | 0.00 USD | 680.89 USD | `-67.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 469,010.00 USD | 0.00 USD | 290.29 USD | `-58.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 468,720.00 USD | 0.00 USD | 120.22 USD | `-52.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 468,600.00 USD | 0.00 USD | 251.68 USD | `-45.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 468,350.00 USD | 0.00 USD | 749.30 USD | `-42.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 467,600.00 USD | 0.00 USD | 772.71 USD | `-41.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 466,830.00 USD | 0.00 USD | 3,760.00 USD | `-40.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 463,060.00 USD | 0.00 USD | 133.00 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 462,930.00 USD | 0.00 USD | 1,320.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 461,610.00 USD | 0.00 USD | 3,770.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 457,850.00 USD | 0.00 USD | 2,070.00 USD | `-34.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 455,770.00 USD | 0.00 USD | 3,740.00 USD | `-32.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 452,030.00 USD | 0.00 USD | 1,050.00 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 450,980.00 USD | 0.00 USD | 120.90 USD | `-30.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 450,860.00 USD | 0.00 USD | 146.80 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 450,710.00 USD | 0.00 USD | 124.02 USD | `-28.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 450,590.00 USD | 0.00 USD | 5,000.00 USD | `-27.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 445,590.00 USD | 0.00 USD | 393.64 USD | `-26.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 445,190.00 USD | 0.00 USD | 10,680.00 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 434,510.00 USD | 0.00 USD | 60,230.00 USD | `-24.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 374,280.00 USD | 0.00 USD | 1,480.00 USD | `-23.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 372,800.00 USD | 0.00 USD | 52,990.00 USD | `-22.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 319,820.00 USD | 0.00 USD | 186.84 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 319,630.00 USD | 0.00 USD | 742.88 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 318,890.00 USD | 0.00 USD | 902.70 USD | `-20.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 317,980.00 USD | 0.00 USD | 1,570.00 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 316,410.00 USD | 0.00 USD | 3,440.00 USD | `-18.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 312,970.00 USD | 0.00 USD | 194.90 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 312,780.00 USD | 0.00 USD | 232.18 USD | `-16.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 312,540.00 USD | 0.00 USD | 9,010.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 303,540.00 USD | 0.00 USD | 518.80 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 303,020.00 USD | 0.00 USD | 19,590.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 283,420.00 USD | 0.00 USD | 686.12 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 282,740.00 USD | 0.00 USD | 3,010.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 279,730.00 USD | 0.00 USD | 25,100.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 254,630.00 USD | 0.00 USD | 13,400.00 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 241,230.00 USD | 0.00 USD | 42,800.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 198,440.00 USD | 0.00 USD | 5,540.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 192,900.00 USD | 0.00 USD | 67,510.00 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 125,390.00 USD | 0.00 USD | 1,720.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 123,670.00 USD | 0.00 USD | 1,880.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 121,790.00 USD | 0.00 USD | 15,160.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 106,640.00 USD | 0.00 USD | 4,270.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 102,370.00 USD | 0.00 USD | 19,680.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 82,690.00 USD | 0.00 USD | 1,980.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 80,710.00 USD | 0.00 USD | 2,760.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 77,950.00 USD | 0.00 USD | 77,950.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 24,120.00 USD | 24,120.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 36,550.00 USD | 12,430.00 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 43,500.00 USD | 6,950.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 44,930.00 USD | 1,420.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 68,620.00 USD | 23,690.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 70,610.00 USD | 1,990.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 72,050.00 USD | 1,440.00 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 79,290.00 USD | 7,240.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 83,110.00 USD | 3,820.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 110,820.00 USD | 27,710.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 112,760.00 USD | 1,930.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 206,040.00 USD | 93,280.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 206,640.00 USD | 597.74 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 211,290.00 USD | 4,650.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 268,070.00 USD | 56,780.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 274,250.00 USD | 6,180.00 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 274,930.00 USD | 679.57 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 295,290.00 USD | 20,360.00 USD | 0.00 USD | `+15.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 295,740.00 USD | 451.95 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 312,370.00 USD | 16,630.00 USD | 0.00 USD | `+17.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 313,290.00 USD | 919.19 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 314,610.00 USD | 1,320.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 322,400.00 USD | 7,790.00 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 324,930.00 USD | 2,540.00 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 325,100.00 USD | 165.31 USD | 0.00 USD | `+22.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 326,050.00 USD | 954.14 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 345,600.00 USD | 19,550.00 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 350,480.00 USD | 4,880.00 USD | 0.00 USD | `+24.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 350,750.00 USD | 266.44 USD | 0.00 USD | `+25.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 367,010.00 USD | 16,260.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 367,160.00 USD | 152.82 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 371,440.00 USD | 4,280.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 374,850.00 USD | 3,410.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 394,290.00 USD | 19,440.00 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 394,510.00 USD | 218.25 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 397,030.00 USD | 2,520.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 404,300.00 USD | 7,270.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 405,250.00 USD | 950.82 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 430,320.00 USD | 25,070.00 USD | 0.00 USD | `+35.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 432,770.00 USD | 2,450.00 USD | 0.00 USD | `+36.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 665,810.00 USD | 233,040.00 USD | 0.00 USD | `+37.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 666,740.00 USD | 924.07 USD | 0.00 USD | `+38.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 667,630.00 USD | 893.01 USD | 0.00 USD | `+39.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 692,370.00 USD | 24,740.00 USD | 0.00 USD | `+40.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 692,840.00 USD | 472.63 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 696,140.00 USD | 3,290.00 USD | 0.00 USD | `+42.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 699,310.00 USD | 3,170.00 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 704,440.00 USD | 5,130.00 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 719,880.00 USD | 15,440.00 USD | 0.00 USD | `+44.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 726,680.00 USD | 6,800.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 733,180.00 USD | 6,500.00 USD | 0.00 USD | `+46.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 739,720.00 USD | 6,540.00 USD | 0.00 USD | `+47.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 746,300.00 USD | 6,580.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 756,230.00 USD | 9,930.00 USD | 0.00 USD | `+49.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 860,210.00 USD | 103,980.00 USD | 0.00 USD | `+50.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 874,450.00 USD | 14,240.00 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 958,810.00 USD | 84,360.00 USD | 0.00 USD | `+52.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 960,500.00 USD | 1,700.00 USD | 0.00 USD | `+52.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 967,870.00 USD | 7,370.00 USD | 0.00 USD | `+53.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 984,560.00 USD | 16,690.00 USD | 0.00 USD | `+54.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 986,860.00 USD | 2,300.00 USD | 0.00 USD | `+55.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 988,590.00 USD | 1,740.00 USD | 0.00 USD | `+56.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,010,000.00 USD | 21,690.00 USD | 0.00 USD | `+57.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,010,000.00 USD | 4,390.00 USD | 0.00 USD | `+58.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,020,000.00 USD | 4,410.00 USD | 0.00 USD | `+59.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,020,000.00 USD | 4,440.00 USD | 0.00 USD | `+60.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,030,000.00 USD | 4,460.00 USD | 0.00 USD | `+61.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,030,000.00 USD | 448.75 USD | 0.00 USD | `+61.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,060,000.00 USD | 30,960.00 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,060,000.00 USD | 453.75 USD | 0.00 USD | `+63.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,060,000.00 USD | 456.25 USD | 0.00 USD | `+64.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,060,000.00 USD | 458.75 USD | 0.00 USD | `+65.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,060,000.00 USD | 461.25 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,070,000.00 USD | 4,540.00 USD | 0.00 USD | `+67.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,070,000.00 USD | 466.25 USD | 0.00 USD | `+68.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,070,000.00 USD | 468.75 USD | 0.00 USD | `+69.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,070,000.00 USD | 471.25 USD | 0.00 USD | `+70.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,070,000.00 USD | 473.75 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,130,000.00 USD | 67,000.00 USD | 0.00 USD | `+71.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,140,000.00 USD | 574.50 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,140,000.00 USD | 577.50 USD | 0.00 USD | `+73.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,140,000.00 USD | 2,710.00 USD | 0.00 USD | `+74.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,140,000.00 USD | 972.50 USD | 0.00 USD | `+75.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,150,000.00 USD | 7,680.00 USD | 0.00 USD | `+76.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,150,000.00 USD | 786.00 USD | 0.00 USD | `+77.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,150,000.00 USD | 790.00 USD | 0.00 USD | `+78.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,150,000.00 USD | 992.50 USD | 0.00 USD | `+79.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,150,000.00 USD | 997.50 USD | 0.00 USD | `+80.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,750,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+80.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,750,000.00 USD | 1,010.00 USD | 0.00 USD | `+81.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,760,000.00 USD | 1,010.00 USD | 0.00 USD | `+82.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+83.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,760,000.00 USD | 1,040.00 USD | 0.00 USD | `+87.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,760,000.00 USD | 1,410.00 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,760,000.00 USD | 1,050.00 USD | 0.00 USD | `+89.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,770,000.00 USD | 4,000.00 USD | 0.00 USD | `+89.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+90.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,820,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+92.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,820,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+94.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,820,000.00 USD | 1,090.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,820,000.00 USD | 3,280.00 USD | 0.00 USD | `+97.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+98.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+98.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,830,000.00 USD | 1,110.00 USD | 0.00 USD | `+99.89%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.10` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,170.00 USD |
| `7D` | `9.12` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,770.00 USD |
| `7D` | `9.14` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,960.00 USD |
| `7D` | `9.16` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD |
| `7D` | `9.18` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,180.00 USD |
| `7D` | `9.20` | 14,720,000.00 USD | 0.00 USD | 14,720,000.00 USD | 14,540.00 USD | 8,360.00 USD | 12.64 USD |
| `7D` | `9.22` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,450.00 USD |
| `7D` | `9.24` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 717.27 USD | 8,580.00 USD | 23,960.00 USD |
| `7D` | `9.26` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,760.00 USD |
| `7D` | `9.28` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 460.95 USD | 5,490.00 USD | 11,870.00 USD |
| `7D` | `9.30` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,520.00 USD |
| `7D` | `9.32` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,690.00 USD |
| `7D` | `9.34` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD |
| `7D` | `9.36` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD |
| `7D` | `9.40` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD |
| `7D` | `9.42` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD |
| `7D` | `9.44` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD |
| `7D` | `9.46` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD |
| `7D` | `9.48` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD |
| `7D` | `9.52` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD |
| `7D` | `9.54` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 472.74 USD | 15,010.00 USD | 10.22 USD |
| `7D` | `9.56` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD |
| `7D` | `9.58` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 38,760.00 USD | 722.15 USD | 4,210.00 USD |
| `7D` | `9.60` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD |
| `7D` | `9.62` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 5,420.00 USD | 0.00 USD | 219.95 USD |
| `7D` | `9.64` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,900.00 USD |
| `7D` | `9.66` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.68` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.70` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.74` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD |
| `7D` | `9.76` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD |
| `7D` | `9.78` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.80` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD |
| `7D` | `9.82` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `9.83` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 105,520.00 USD | 20,760.00 USD | 27,930.00 USD |
| `7D` | `9.84` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD |
| `1D` | `9.85` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 10,990.00 USD | 7,050.00 USD | 397.80 USD |
| `7D` | `9.86` | 13,320,000.00 USD | 0.00 USD | 13,320,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD |
| `1D` | `9.87` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 14,610.00 USD | 4,120.00 USD | 10,300.00 USD |
| `7D` | `9.88` | 13,300,000.00 USD | 0.00 USD | 13,300,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD |
| `1D` | `9.89` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 8,400.00 USD | 8,240.00 USD | 10,660.00 USD |
| `7D` | `9.90` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.91` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 30,130.00 USD | 32,910.00 USD | 0.00 USD |
| `7D` | `9.92` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD |
| `1D` | `9.93` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 13,840.00 USD | 12,020.00 USD | 219.74 USD |
| `7D` | `9.94` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,390.00 USD |
| `1D` | `9.95` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 9,450.00 USD | 7,200.00 USD | 8,890.00 USD |
| `7D` | `9.96` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 11,410.00 USD | 1,090.00 USD |
| `1D` | `9.97` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 68,690.00 USD | 7,890.00 USD | 53,930.00 USD |
| `7D` | `9.98` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD |
| `1D` | `9.99` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 3,940.00 USD | 6,390.00 USD | 63,670.00 USD |
| `7D` | `10.00` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 12,870.00 USD |
| `1D` | `10.01` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 5,720.00 USD | 726.47 USD | 24,690.00 USD |
| `7D` | `10.02` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD |
| `1D` | `10.03` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 6,170.00 USD | 12,900.00 USD | 264.22 USD |
| `7D` | `10.04` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD |
| `1D` | `10.05` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 38,520.00 USD | 555.00 USD | 18,800.00 USD |
| `7D` | `10.06` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD |
| `1D` | `10.07` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,450.00 USD |
| `7D` | `10.08` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.09` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,120.00 USD |
| `7D` | `10.10` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD |
| `1D` | `10.11` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 7,530.00 USD | 41,480.00 USD | 123.54 USD |
| `7D` | `10.12` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD |
| `1D` | `10.13` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD |
| `7D` | `10.14` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD |
| `1D` | `10.15` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,470.00 USD |
| `7D` | `10.16` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD |
| `1D` | `10.17` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 127,800.00 USD | 25,060.00 USD | 640.95 USD |
| `7D` | `10.18` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD |
| `1D` | `10.19` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,270.00 USD |
| `7D` | `10.20` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD |
| `1D` | `10.21` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,560.00 USD |
| `7D` | `10.22` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD |
| `1D` | `10.23` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 105,610.00 USD | 61,740.00 USD | 291,220.00 USD |
| `7D` | `10.24` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,360.00 USD |
| `1D` | `10.25` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 16,630.00 USD | 27,140.00 USD | 38,550.00 USD |
| `7D` | `10.26` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD |
| `1D` | `10.27` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 69,790.00 USD | 18,820.00 USD | 134,320.00 USD |
| `7D` | `10.28` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.29` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 335,550.00 USD | 2,000.00 USD | 163,340.00 USD |
| `7D` | `10.30` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 457,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.31` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 19,560.00 USD | 19,240.00 USD | 52,130.00 USD |
| `7D` | `10.32` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.33` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 14,540.00 USD | 3,820.00 USD | 52,610.00 USD |
| `7D` | `10.34` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 56,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.35` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 60,790.00 USD | 6,620.00 USD | 72,810.00 USD |
| `7D` | `10.36` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.37` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 11,970.00 USD | 13,750.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.39` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD |
| `7D` | `10.40` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.41` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,760.00 USD |
| `7D` | `10.42` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD |
| `1D` | `10.43` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 311,620.00 USD | 0.00 USD | 88,810.00 USD |
| `7D` | `10.44` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.45` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 329,110.00 USD | 44,950.00 USD | 216,590.00 USD |
| `7D` | `10.46` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.47` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,200.00 USD |
| `7D` | `10.48` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.49` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 41,670.00 USD | 38,130.00 USD | 25,100.00 USD |
| `7D` | `10.50` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.51` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 11,220.00 USD | 10,370.00 USD | 12,930.00 USD |
| `7D` | `10.52` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.53` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 71.67 USD | 18,090.00 USD | 117,650.00 USD |
| `7D` | `10.54` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD |
| `1D` | `10.55` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 65,860.00 USD | 48,330.00 USD | 52,300.00 USD |
| `7D` | `10.56` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD |
| `1D` | `10.57` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 39,860.00 USD | 21,900.00 USD | 4,980.00 USD |
| `1D` | `10.59` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 18,130.00 USD | 18,010.00 USD | 15,230.00 USD |
| `7D` | `10.60` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 458.05 USD |
| `1D` | `10.61` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 3,750.00 USD | 15,520.00 USD |
| `7D` | `10.62` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 59,050.00 USD | 0.00 USD | 180.54 USD |
| `1D` | `10.63` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 11,820.00 USD | 1,170.00 USD | 102,690.00 USD |
| `7D` | `10.64` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 11,150.00 USD | 0.00 USD | 150.41 USD |
| `1D` | `10.65` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 30,790.00 USD | 4,060.00 USD | 23,920.00 USD |
| `7D` | `10.66` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD |
| `1D` | `10.67` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 40,350.00 USD | 9,610.00 USD | 15,430.00 USD |
| `7D` | `10.68` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD |
| `1D` | `10.69` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 12,670.00 USD | 6,950.00 USD | 36,190.00 USD |
| `7D` | `10.70` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.71` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD |
| `7D` | `10.72` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.73` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD |
| `7D` | `10.74` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD |
| `1D` | `10.75` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 89,590.00 USD | 8,370.00 USD | 0.00 USD |
| `7D` | `10.76` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 16,310.00 USD | 109,140.00 USD | 0.00 USD |
| `1D` | `10.77` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 22,390.00 USD | 62,040.00 USD | 51,590.00 USD |
| `7D` | `10.78` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 535,020.00 USD | 32,650.00 USD | 103,760.00 USD |
| `1D` | `10.79` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 167,900.00 USD | 118,040.00 USD | 9,950.00 USD |
| `7D` | `10.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 23,450.00 USD | 70,260.00 USD | 0.00 USD |
| `1D` | `10.81` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 13,650.00 USD | 5,170.00 USD | 0.00 USD |
| `7D` | `10.82` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 56,610.00 USD | 206,380.00 USD |
| `1D` | `10.83` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 315,520.00 USD | 4,570.00 USD | 0.00 USD |
| `7D` | `10.84` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 295,700.00 USD | 80,420.00 USD | 196,240.00 USD |
| `1D` | `10.85` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 87,770.00 USD | 14,590.00 USD | 148,410.00 USD |
| `7D` | `10.86` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 323,850.00 USD | 3,610.00 USD | 333,920.00 USD |
| `1D` | `10.87` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 60,390.00 USD | 6,510.00 USD | 446.30 USD |
| `7D` | `10.88` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD |
| `1D` | `10.89` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 22,380.00 USD | 3,380.00 USD | 30,870.00 USD |
| `7D` | `10.90` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 220,890.00 USD |
| `1D` | `10.91` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 117,890.00 USD | 904.45 USD | 0.00 USD |
| `7D` | `10.92` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD |
| `1D` | `10.93` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 3,920.00 USD | 1,010.00 USD | 86.22 USD |
| `7D` | `10.94` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.95` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,550.00 USD | 1,320.00 USD | 87,750.00 USD |
| `7D` | `10.96` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD |
| `1D` | `10.97` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 101.06 USD |
| `7D` | `10.98` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 17,930.00 USD | 0.00 USD | 209,840.00 USD |
| `1D` | `10.99` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 467.00 USD | 251.76 USD |
| `7D` | `11.00` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 10,830.00 USD | 2,280.00 USD | 634.90 USD |
| `1D` | `11.01` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 3,040.00 USD | 103.72 USD |
| `7D` | `11.02` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,900.00 USD | 31,180.00 USD | 143,500.00 USD |
| `1D` | `11.03` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 44,040.00 USD | 43,470.00 USD | 304,940.00 USD |
| `7D` | `11.04` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 17,850.00 USD | 40,210.00 USD | 178,530.00 USD |
| `1D` | `11.05` | 962,970.00 USD | 0.00 USD | 962,970.00 USD | 306,560.00 USD | 5,150.00 USD | 106,380.00 USD |
| `7D` | `11.06` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 4,020.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 544,880.00 USD | 0.00 USD | 544,880.00 USD | 329,150.00 USD | 46,170.00 USD | 169,560.00 USD |
| `1D` | `11.08` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.08` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 14,890.00 USD | 1,810.00 USD | 167,460.00 USD |
| `1D` | `11.09` | 477,080.00 USD | 477,080.00 USD | 0.00 USD | 105,500.00 USD | 69,450.00 USD | 302,140.00 USD |
| `7D` | `11.10` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 301,790.00 USD | 23,300.00 USD | 173,360.00 USD |
| `1D` | `11.11` | 539,320.00 USD | 539,320.00 USD | 0.00 USD | 9,550.00 USD | 52,690.00 USD | 0.00 USD |
| `7D` | `11.12` | 612,850.00 USD | 0.00 USD | 612,850.00 USD | 262,770.00 USD | 115,910.00 USD | 234,170.00 USD |
| `1D` | `11.13` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 438,340.00 USD | 99,350.00 USD | 204,420.00 USD |
| `7D` | `11.14` | 215,120.00 USD | 215,120.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `7D` | `11.14` | 430,230.00 USD | 430,230.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `1D` | `11.15` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 198,370.00 USD | 61,430.00 USD | 50,270.00 USD |
| `7D` | `11.16` | 699,610.00 USD | 699,610.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD |
| `1D` | `11.17` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 22,450.00 USD | 53,650.00 USD | 59,080.00 USD |
| `7D` | `11.18` | 717,100.00 USD | 717,100.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD |
| `1D` | `11.19` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 72,050.00 USD | 28,650.00 USD | 40,560.00 USD |
| `7D` | `11.20` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 171,840.00 USD | 78,020.00 USD | 79,190.00 USD |
| `1D` | `11.21` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 160,950.00 USD | 59,630.00 USD | 164,200.00 USD |
| `7D` | `11.22` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 482,460.00 USD | 28,690.00 USD | 603.14 USD |
| `1D` | `11.23` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 262,260.00 USD | 37,760.00 USD | 118,670.00 USD |
| `7D` | `11.24` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 108,110.00 USD | 39,180.00 USD | 147,400.00 USD |
| `7D` | `11.26` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 520,990.00 USD | 0.00 USD | 296,010.00 USD |
| `1D` | `11.27` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 310,520.00 USD | 4,350.00 USD | 173,090.00 USD |
| `7D` | `11.28` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 347,470.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.29` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 176,550.00 USD | 119,460.00 USD | 225,580.00 USD |
| `7D` | `11.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 20,610.00 USD |
| `1D` | `11.31` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 123,640.00 USD | 68,310.00 USD | 66,970.00 USD |
| `7D` | `11.32` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD |
| `1D` | `11.33` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 164,560.00 USD | 34,060.00 USD | 62,480.00 USD |
| `7D` | `11.34` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD |
| `1D` | `11.35` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 296,410.00 USD | 103,310.00 USD | 84,490.00 USD |
| `7D` | `11.36` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.37` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 152,070.00 USD | 91,520.00 USD | 47,530.00 USD |
| `7D` | `11.38` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD |
| `1D` | `11.39` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 14,820.00 USD | 47,470.00 USD | 7,570.00 USD |
| `7D` | `11.40` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD |
| `1D` | `11.41` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 96,590.00 USD | 35,740.00 USD | 140,680.00 USD |
| `7D` | `11.42` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD |
| `1D` | `11.43` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 64,580.00 USD | 56,490.00 USD | 132,800.00 USD |
| `7D` | `11.44` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 303,190.00 USD | 95,260.00 USD | 38,210.00 USD |
| `1D` | `11.45` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 77,400.00 USD | 83,200.00 USD | 25,540.00 USD |
| `7D` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 99,360.00 USD | 55,470.00 USD | 269.04 USD |
| `1D` | `11.47` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 56,320.00 USD | 19,720.00 USD | 23,420.00 USD |
| `7D` | `11.48` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 54,660.00 USD | 84,840.00 USD | 64,610.00 USD |
| `1D` | `11.49` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 33,390.00 USD | 27,530.00 USD | 34,670.00 USD |
| `7D` | `11.50` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 91,790.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.51` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 41,360.00 USD | 29,500.00 USD | 30,920.00 USD |
| `7D` | `11.52` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 33,540.00 USD |
| `1D` | `11.53` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 64,080.00 USD | 17,000.00 USD | 41,220.00 USD |
| `7D` | `11.54` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD |
| `1D` | `11.55` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 84,610.00 USD | 1,570.00 USD | 53,750.00 USD |
| `7D` | `11.56` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 86,650.00 USD | 793.25 USD | 432.76 USD |
| `1D` | `11.57` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 90,730.00 USD | 3,740.00 USD | 23,920.00 USD |
| `7D` | `11.58` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.59` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 17,210.00 USD | 7,660.00 USD | 39,570.00 USD |
| `7D` | `11.60` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 44,670.00 USD | 10,510.00 USD | 23,030.00 USD |
| `1D` | `11.61` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 118,210.00 USD | 512.95 USD | 85,130.00 USD |
| `7D` | `11.62` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.63` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 2,580.00 USD | 6,700.00 USD | 31,270.00 USD |
| `7D` | `11.64` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD |
| `1D` | `11.65` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 2,630.00 USD | 7,840.00 USD | 46.76 USD |
| `7D` | `11.66` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.67` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 19,420.00 USD | 11,530.00 USD | 57,510.00 USD |
| `7D` | `11.68` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD |
| `1D` | `11.69` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 105,590.00 USD | 34,170.00 USD | 313.96 USD |
| `7D` | `11.70` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD |
| `1D` | `11.71` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 74,220.00 USD | 13,000.00 USD | 15,370.00 USD |
| `7D` | `11.72` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD |
| `1D` | `11.73` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 139,320.00 USD | 11,770.00 USD | 120,100.00 USD |
| `7D` | `11.74` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD |
| `1D` | `11.75` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 21,990.00 USD | 38,420.00 USD | 61,370.00 USD |
| `7D` | `11.76` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD |
| `1D` | `11.77` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 41,580.00 USD | 20,480.00 USD | 14,560.00 USD |
| `7D` | `11.78` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 56,750.00 USD |
| `1D` | `11.79` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 12,300.00 USD | 339.50 USD | 40,180.00 USD |
| `7D` | `11.80` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.81` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 18,040.00 USD | 17,880.00 USD |
| `7D` | `11.82` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.83` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 11,070.00 USD | 11,560.00 USD | 29,390.00 USD |
| `7D` | `11.84` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD |
| `1D` | `11.85` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 82,060.00 USD | 9,720.00 USD | 84,740.00 USD |
| `7D` | `11.86` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD |
| `1D` | `11.87` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 20,010.00 USD | 20,660.00 USD | 53,710.00 USD |
| `7D` | `11.88` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD |
| `1D` | `11.89` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 43,100.00 USD | 13,220.00 USD | 43,750.00 USD |
| `7D` | `11.90` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.91` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 102,960.00 USD | 18,290.00 USD | 31,690.00 USD |
| `7D` | `11.92` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD |
| `1D` | `11.93` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 135,130.00 USD | 28,280.00 USD | 28,570.00 USD |
| `7D` | `11.94` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD |
| `1D` | `11.95` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 84,850.00 USD | 20,680.00 USD | 43,540.00 USD |
| `7D` | `11.96` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD |
| `1D` | `11.97` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 71,640.00 USD | 36,230.00 USD | 87,420.00 USD |
| `7D` | `11.98` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD |
| `1D` | `11.99` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 108,260.00 USD | 27,660.00 USD | 36,360.00 USD |
| `7D` | `12.00` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD |
| `1D` | `12.01` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 47,510.00 USD | 9,290.00 USD | 50,020.00 USD |
| `7D` | `12.02` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD |
| `1D` | `12.03` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 47,360.00 USD | 34,660.00 USD | 24,300.00 USD |
| `7D` | `12.04` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD |
| `1D` | `12.05` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 108,910.00 USD | 43,590.00 USD | 59,560.00 USD |
| `7D` | `12.06` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,690.00 USD |
| `1D` | `12.07` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 34,850.00 USD | 33,440.00 USD | 67,870.00 USD |
| `7D` | `12.08` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD |
| `1D` | `12.09` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 20,990.00 USD | 24,720.00 USD | 27,880.00 USD |
| `7D` | `12.10` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.11` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 101,970.00 USD | 38,270.00 USD | 55,310.00 USD |
| `7D` | `12.12` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD |
| `1D` | `12.13` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 93,390.00 USD | 33,860.00 USD | 39,690.00 USD |
| `7D` | `12.14` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 147,420.00 USD | 92,520.00 USD | 119,290.00 USD |
| `1D` | `12.15` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 113,520.00 USD | 42,340.00 USD | 65,330.00 USD |
| `7D` | `12.16` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD |
| `1D` | `12.17` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 118,100.00 USD | 60,070.00 USD | 69,710.00 USD |
| `7D` | `12.18` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 57,680.00 USD | 54,220.00 USD | 32,160.00 USD |
| `1D` | `12.19` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 59,950.00 USD | 24,020.00 USD | 12,290.00 USD |
| `7D` | `12.20` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 91,300.00 USD |
| `1D` | `12.21` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 32,170.00 USD | 28,710.00 USD | 45,980.00 USD |
| `7D` | `12.22` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 106,120.00 USD |
| `1D` | `12.23` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 7,370.00 USD | 18,230.00 USD | 10,870.00 USD |
| `7D` | `12.24` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 70,650.00 USD | 54,230.00 USD | 115,100.00 USD |
| `1D` | `12.25` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 2,260.00 USD | 3,780.00 USD | 7,630.00 USD |
| `7D` | `12.26` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 192,800.00 USD | 55,780.00 USD | 50,600.00 USD |
| `1D` | `12.27` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 38,860.00 USD | 8,240.00 USD | 20,000.00 USD |
| `7D` | `12.28` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 215,790.00 USD | 52,850.00 USD | 148,350.00 USD |
| `1D` | `12.29` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 23,030.00 USD | 9,300.00 USD | 8,780.00 USD |
| `1D` | `12.30` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `12.30` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD |
| `7D` | `12.32` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 18,040.00 USD |
| `7D` | `12.34` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 48,630.00 USD | 18,250.00 USD | 13,590.00 USD |
| `7D` | `12.36` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 36,210.00 USD | 24,190.00 USD | 18,470.00 USD |
| `7D` | `12.38` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 7,170.00 USD | 6,880.00 USD | 55,410.00 USD |
| `7D` | `12.40` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 111,350.00 USD | 41,100.00 USD | 12,560.00 USD |
| `7D` | `12.42` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 23,200.00 USD | 21,440.00 USD | 10,400.00 USD |
| `7D` | `12.44` | 16,280,000.00 USD | 16,280,000.00 USD | 0.00 USD | 81,360.00 USD | 284.67 USD | 45,220.00 USD |
| `7D` | `12.46` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 39,540.00 USD | 25,610.00 USD | 86,160.00 USD |
| `7D` | `12.48` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 63,590.00 USD |
| `7D` | `12.50` | 16,790,000.00 USD | 16,790,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD |
| `7D` | `12.52` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 163,610.00 USD | 33,380.00 USD | 113,900.00 USD |
| `7D` | `12.54` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD |
| `7D` | `12.56` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 77,880.00 USD | 20,220.00 USD | 27,710.00 USD |
| `7D` | `12.58` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 41,760.00 USD | 34,570.00 USD | 41,450.00 USD |
| `7D` | `12.60` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD |
| `7D` | `12.62` | 17,820,000.00 USD | 17,820,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `7D` | `12.64` | 17,950,000.00 USD | 17,950,000.00 USD | 0.00 USD | 63,450.00 USD | 42,320.00 USD | 25,820.00 USD |
| `7D` | `12.66` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 22,530.00 USD | 5,030.00 USD | 8,780.00 USD |
| `7D` | `12.68` | 18,050,000.00 USD | 18,050,000.00 USD | 0.00 USD | 9,270.00 USD | 18,330.00 USD | 36,330.00 USD |
| `7D` | `12.70` | 18,110,000.00 USD | 18,110,000.00 USD | 0.00 USD | 2,010.00 USD | 617.78 USD | 52,460.00 USD |
| `7D` | `12.72` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 47,740.00 USD | 22,750.00 USD | 40,880.00 USD |
| `7D` | `12.74` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 38,570.00 USD | 26,370.00 USD | 40,430.00 USD |
| `7D` | `12.76` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 13,750.00 USD | 14,350.00 USD | 29,650.00 USD |
| `7D` | `12.78` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 109,130.00 USD | 16,110.00 USD | 52,020.00 USD |
| `7D` | `12.80` | 18,650,000.00 USD | 18,650,000.00 USD | 0.00 USD | 13,700.00 USD | 14,000.00 USD | 61,100.00 USD |
| `7D` | `12.82` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `7D` | `12.84` | 18,720,000.00 USD | 18,720,000.00 USD | 0.00 USD | 31,320.00 USD | 15,990.00 USD | 7,710.00 USD |
| `7D` | `12.86` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,210.00 USD |
| `7D` | `12.88` | 18,830,000.00 USD | 18,830,000.00 USD | 0.00 USD | 23,610.00 USD | 4,610.00 USD | 12,750.00 USD |
| `7D` | `12.90` | 18,910,000.00 USD | 18,910,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD |
| `7D` | `12.92` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 26,790.00 USD |
| `7D` | `12.94` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 69.74 USD |
| `7D` | `12.96` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 13,150.00 USD | 11,970.00 USD | 24,940.00 USD |
| `7D` | `12.98` | 19,120,000.00 USD | 19,120,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD |
| `7D` | `13.00` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 51,470.00 USD | 9,560.00 USD | 20,570.00 USD |
| `7D` | `13.02` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `7D` | `13.04` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 303.50 USD | 335.85 USD | 0.00 USD |
| `7D` | `13.06` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD |
| `7D` | `13.08` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `518.79M` | Total OI Tokens: `46,765,868.5 LINK`
  * 1h OI Change: `-0.16%` | 4h OI Change: `-2.40%` | 24h OI Change: `-5.82%`
  * Exchange Breakdown: Binance=`102.06M` | Bybit=`69.61M` | OKX=`26.79M` | Hyperliquid=`56.07M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `40.37` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0068%` |
| **USDT Bybit** | `-0.0121%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0028%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `56.65%` | `43.35%` | `1.31` | 6,640,000.00 USD |
| `15M` | `Binance` | `54.35%` | `45.65%` | `1.19` | 2,190,000.00 USD |
| `15M` | `OKX` | `55.39%` | `44.61%` | `1.24` | 528,940.00 USD |
| `15M` | `Bybit` | `53.13%` | `46.87%` | `1.13` | 624,000.00 USD |
| `15M` | `KuCoin` | `62.42%` | `37.58%` | `1.66` | 53,500.00 USD |
| `15M` | `Gate` | `36.62%` | `63.38%` | `0.58` | 83,560.00 USD |
| `15M` | `Bitget` | `38.8%` | `61.2%` | `0.63` | 149,420.00 USD |
| `15M` | `BingX` | `67.72%` | `32.28%` | `2.10` | 1,520,000.00 USD |
| `15M` | `MEXC` | `84.13%` | `15.87%` | `5.30` | 193,390.00 USD |
| `15M` | `Bitunix` | `60.01%` | `39.99%` | `1.50` | 119,690.00 USD |
| `15M` | `Hyperliquid` | `84.89%` | `15.11%` | `5.62` | 12,530.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.01%` | `49.99%` | `1.00` | 1,050,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `10.06%` | `89.94%` | `0.11` | 93,160.00 USD |
| `15M` | `HTX` | `70.33%` | `29.67%` | `2.37` | 23,420.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `97.65%` | `2.35%` | `41.55` | 238.54 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `99.94%` | `0.06%` | `1665.67` | 1,680.00 USD |
| `15M` | `Whale Positions` | `54.35%` | `45.65%` | `1.19` | 2,190,000.00 USD |
| `15M` | `Global Accounts` | `56.65%` | `43.35%` | `1.31` | 6,640,000.00 USD |
| `1H` | `LINK` | `48.80%` | `51.20%` | `0.95` | 35,080,000.00 USD |
| `1H` | `Binance` | `50.39%` | `49.61%` | `1.02` | 12,880,000.00 USD |
| `1H` | `OKX` | `47.55%` | `52.45%` | `0.91` | 6,960,000.00 USD |
| `1H` | `Bybit` | `49.55%` | `50.45%` | `0.98` | 2,240,000.00 USD |
| `1H` | `KuCoin` | `40.97%` | `59.03%` | `0.69` | 198,170.00 USD |
| `1H` | `Gate` | `48.35%` | `51.65%` | `0.94` | 5,970,000.00 USD |
| `1H` | `Bitget` | `27.54%` | `72.46%` | `0.38` | 867,860.00 USD |
| `1H` | `BingX` | `42.16%` | `57.84%` | `0.73` | 641,710.00 USD |
| `1H` | `MEXC` | `53.95%` | `46.05%` | `1.17` | 3,040,000.00 USD |
| `1H` | `Bitunix` | `57.75%` | `42.25%` | `1.37` | 1,210,000.00 USD |
| `1H` | `Hyperliquid` | `27.35%` | `72.65%` | `0.38` | 89,230.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.12%` | `49.88%` | `1.00` | 208,490.00 USD |
| `1H` | `Crypto.com` | `44.39%` | `55.61%` | `0.80` | 31,400.00 USD |
| `1H` | `WhiteBIT` | `28.53%` | `71.47%` | `0.40` | 405,720.00 USD |
| `1H` | `HTX` | `30.64%` | `69.36%` | `0.44` | 162,200.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `47.91%` | `52.09%` | `0.92` | 162,170.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.39%` | `56.61%` | `0.77` | 4,630.00 USD |
| `1H` | `Whale Positions` | `50.39%` | `49.61%` | `1.02` | 12,880,000.00 USD |
| `1H` | `Global Accounts` | `48.80%` | `51.20%` | `0.95` | 35,080,000.00 USD |
| `4H` | `LINK` | `45.92%` | `54.08%` | `0.85` | 157,340,000.00 USD |
| `4H` | `Binance` | `44.93%` | `55.07%` | `0.82` | 71,540,000.00 USD |
| `4H` | `OKX` | `45.83%` | `54.17%` | `0.85` | 21,900,000.00 USD |
| `4H` | `Bybit` | `48.98%` | `51.02%` | `0.96` | 28,230,000.00 USD |
| `4H` | `KuCoin` | `48.37%` | `51.63%` | `0.94` | 3,000,000.00 USD |
| `4H` | `Gate` | `39.52%` | `60.48%` | `0.65` | 8,130,000.00 USD |
| `4H` | `Bitget` | `44.59%` | `55.41%` | `0.80` | 6,620,000.00 USD |
| `4H` | `BingX` | `32.68%` | `67.32%` | `0.49` | 1,410,000.00 USD |
| `4H` | `MEXC` | `51.77%` | `48.23%` | `1.07` | 2,490,000.00 USD |
| `4H` | `Bitunix` | `44.04%` | `55.96%` | `0.79` | 2,950,000.00 USD |
| `4H` | `Hyperliquid` | `53.53%` | `46.47%` | `1.15` | 4,990,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.02%` | `51.98%` | `0.92` | 2,200,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `45.42%` | `54.58%` | `0.83` | 1,920,000.00 USD |
| `4H` | `HTX` | `44.74%` | `55.26%` | `0.81` | 886,680.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.29%` | `54.71%` | `0.83` | 42,610.00 USD |
| `4H` | `Aster` | `43.1%` | `56.9%` | `0.76` | 234,260.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `58.22%` | `41.78%` | `1.39` | 788,500.00 USD |
| `4H` | `Whale Positions` | `44.93%` | `55.07%` | `0.82` | 71,540,000.00 USD |
| `4H` | `Global Accounts` | `45.92%` | `54.08%` | `0.85` | 157,340,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `10.94` | `10.95` | `10.94` | `10.98` | `10.93` | 1,915,931.41 USD | 933,547.46 USD | 982,383.95 USD | -48,836.49 USD | `-2.55%` | `2B / 6S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `10.99` | `10.90` | 2,589,400.57 USD | 1,319,072.00 USD | 1,270,328.57 USD | 48,743.44 USD | `+1.88%` | `17B / 14S` |
| `5:00 UTC` | `10.99` | `10.99` | `10.99` | `11.02` | `10.96` | 1,907,525.28 USD | 901,785.44 USD | 1,005,739.84 USD | -103,954.39 USD | `-5.45%` | `12B / 13S` |
| `0:00 UTC` | `10.99` | `11.00` | `10.99` | `11.02` | `10.96` | 4,049,528.45 USD | 2,107,266.70 USD | 1,942,261.75 USD | 165,004.95 USD | `+4.07%` | `6B / 12S` |
| `5:00 UTC` | `11.08` | `11.06` | `11.08` | `11.09` | `11.01` | 2,811,297.51 USD | 1,507,938.86 USD | 1,303,358.65 USD | 204,580.21 USD | `+7.28%` | `16B / 8S` |
| `0:00 UTC` | `11.09` | `11.11` | `11.09` | `11.16` | `11.05` | 2,051,224.58 USD | 1,043,229.65 USD | 1,007,994.93 USD | 35,234.71 USD | `+1.72%` | `20B / 16S` |
| `5:00 UTC` | `11.12` | `11.13` | `11.12` | `11.15` | `11.11` | 1,272,358.25 USD | 643,125.20 USD | 629,233.05 USD | 13,892.16 USD | `+1.09%` | `3B / 5S` |
| `0:00 UTC` | `11.12` | `11.12` | `11.12` | `11.15` | `11.09` | 1,517,756.15 USD | 753,042.16 USD | 764,713.99 USD | -11,671.83 USD | `-0.77%` | `5B / 11S` |
| `5:00 UTC` | `11.09` | `11.10` | `11.09` | `11.14` | `11.05` | 1,386,195.17 USD | 566,935.34 USD | 819,259.83 USD | -252,324.50 USD | `-18.20%` | `12B / 24S` |
| `0:00 UTC` | `11.05` | `11.06` | `11.05` | `11.09` | `11.03` | 1,585,277.03 USD | 861,538.60 USD | 723,738.43 USD | 137,800.17 USD | `+8.69%` | `7B / 8S` |

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
| `5m` | 61,650.00 USD | 357,740.00 USD | **`ACCUMULATION`** |
| `15m` | 49,520.00 USD | 568,890.00 USD | **`ACCUMULATION`** |
| `30m` | -17,230.00 USD | -178,900.00 USD | **`DISTRIBUTION`** |
| `1h` | -51,940.00 USD | -612,510.00 USD | **`DISTRIBUTION`** |
| `2h` | -937,270.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -786,850.00 USD | 1,270,000.00 USD | **`ACCUMULATION`** |
| `6h` | 168,700.00 USD | -611,340.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,500,000.00 USD | -14,500,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -11,600,000.00 USD | -21,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,120,000.00 USD | -20,270,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,780,000.00 USD | -45,870,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,270,000.00 USD | -195,460,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+61.65K` | 15m=`+49.52K` | 1h=`-51.94K` | 24h=`-11.12M`
* Futures Capital Netflows: 5m=`+357.74K` | 15m=`+568.89K` | 1h=`-612.51K` | 24h=`-20.27M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.10` (Risk Distance: `0.2559` pts)
  * +2.5R Take Profit: `10.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.20` (Risk Distance: `0.2559` pts)
  * +2.5R Take Profit: `10.30`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
