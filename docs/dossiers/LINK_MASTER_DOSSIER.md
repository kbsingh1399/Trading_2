# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 10:52:59 IST` (`2026-10-30 05:22:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.06` | **Live Ask Quote**: `11.15` | **Mid Price**: `11.11`
- **Spread Points**: `86.00` | **Spread BPS**: `77.44 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.59` | VWAP Z-Score: `+2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1068` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `65.19` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.25` | Lower -3.00σ Band: `9.94`
  * Upper +2.51σ Band: `11.15` | Lower -2.51σ Band: `10.04`
  * Upper +2.01σ Band: `11.04` | Lower -2.01σ Band: `10.15`
  * Upper +2.00σ Band: `11.03` | Lower -2.00σ Band: `10.15`
  * Upper +1.28σ Band: `10.88` | Lower -1.28σ Band: `10.31`
  * Upper +1.00σ Band: `10.81` | Lower -1.00σ Band: `10.37`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.90` | EMA-20=`10.82` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.96` (Slope: `+0.0000`) | EMA-100=`11.16`
  * Institutional Anchors: EMA-144=`11.24` | EMA-200=`11.30` (Slope: `-0.5193`) | EMA-233=`11.33`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.91` (Distance: `+1.91%`)
  * Point of Control (POC) = `10.48` (Distance: `+6.02%`)
  * Value Area Low (VAL) = `10.35` (Distance: `+7.37%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.73` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.09` | Low=`10.98`
  * New York Session (13:00-21:00 UTC): High=`11.17` | Low=`11.04`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.06` - `11.15`
  * Optimal Trade Entry (OTE 0.705): `11.13`
  * Structural Invalidation Anchor (0.786): `11.19`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.13` | `11.16` | `11.12` | `11.12` | `51,104` | 569,298.19 USD | -91,697.73 USD | `-16.11%` | -11,887,873.15 USD | `-0.47` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.12` | `11.13` | `11.11` | `11.13` | `42,931` | 477,225.10 USD | 38,971.86 USD | `+8.17%` | -11,848,901.29 USD | `+0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.13` | `11.13` | `11.11` | `11.13` | `18,911` | 210,332.65 USD | -950.12 USD | `-0.45%` | -11,849,851.41 USD | `-0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `11.01` | `11.09` | `11.01` | `11.05` | `254,188` | 2,811,297.51 USD | 204,580.21 USD | `+7.28%` | -11,754,249.98 USD | `+0.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `11.05` | `11.16` | `11.05` | `11.12` | `184,689` | 2,051,224.58 USD | 35,234.71 USD | `+1.72%` | -11,719,015.27 USD | `-0.10` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `11.12` | `11.13` | `11.11` | `11.13` | `61,841` | 687,557.75 USD | 38,021.74 USD | `+5.53%` | -11,680,993.53 USD | `-0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.72` | `10.98` | `10.71` | `10.96` | `806,147` | 8,746,362.36 USD | 866,493.31 USD | `+9.91%` | -11,617,870.44 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.96` | `11.09` | `10.90` | `11.05` | `1,032,622` | 11,357,751.81 USD | 314,374.20 USD | `+2.77%` | -11,303,496.23 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.05` | `11.16` | `11.05` | `11.13` | `248,846` | 2,764,547.24 USD | 52,190.53 USD | `+1.89%` | -11,251,305.70 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.13` | `1,279,152` | 14,096,534.14 USD | 387,630.66 USD | `+2.75%` | -11,841,197.41 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,625,285.45 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 595,900.27 USD | `-1.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.13` | `1,279,152` | 14,096,534.14 USD | 387,630.66 USD | `+2.75%` | -11,841,197.41 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`11.11`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `423` | `0xecb6...2b00` | `SHORT` | 5,282,193.70 USD | `474,932,000.00` | `10.66` | `11.12` | `72.03` | -220,058.64 USD | `-4.17%` | `10X Cross` |
| `509` | `0x73ce...8ce9` | `LONG` | 4,451,729.10 USD | `400,011,600.00` | `12.05` | `11.12` | `7.82` | -368,024.61 USD | `-8.27%` | `5X Cross` |
| `851` | `0xb83d...6e36` | `SHORT` | 2,693,362.68 USD | `242,013,000.00` | `12.93` | `11.12` | `528.88` | 436,531.51 USD | `+16.21%` | `3X Cross` |
| `896` | `0x458d...ab3b` | `LONG` | 2,527,799.76 USD | `227,156,700.00` | `13.13` | `11.12` | `9.34` | -454,430.64 USD | `-17.98%` | `3X Isolated` |
| `976` | `0xdd53...2b13` | `SHORT` | 2,298,070.09 USD | `206,475,300.00` | `11.92` | `11.12` | `295.68` | 163,152.84 USD | `+7.10%` | `3X Cross` |
| `999` | `0x3dc9...54b0` | `SHORT` | 2,225,600.00 USD | `200,000,000.00` | `7.56` | `11.12` | `92.80` | -714,441.58 USD | `-32.10%` | `10X Cross` |
| `1011` | `0x45d2...4029` | `SHORT` | 2,175,915.00 USD | `195,500,000.00` | `11.54` | `11.12` | `212.35` | 80,568.43 USD | `+3.70%` | `10X Cross` |
| `1181` | `0x6540...f7b7` | `LONG` | 1,876,363.29 USD | `168,586,100.00` | `12.40` | `11.12` | `6.69` | -214,656.01 USD | `-11.44%` | `5X Isolated` |
| `1260` | `0xeadc...9d55` | `LONG` | 1,753,845.98 USD | `157,691,600.00` | `9.43` | `11.12` | `0.000000` | 267,191.07 USD | `+15.23%` | `10X Cross` |
| `1488` | `0x5b5d...c060` | `SHORT` | 1,465,607.11 USD | `131,775,500.00` | `13.61` | `11.12` | `1173.63` | 327,650.86 USD | `+22.36%` | `3X Cross` |
| `1656` | `0xf6f3...47f8` | `SHORT` | 1,280,223.80 USD | `115,024,600.00` | `11.42` | `11.12` | `18.97` | 33,106.39 USD | `+2.59%` | `5X Cross` |
| `1817` | `0x9df2...c665` | `SHORT` | 1,145,033.87 USD | `102,887,400.00` | `11.48` | `11.12` | `299.16` | 36,217.10 USD | `+3.16%` | `10X Cross` |
| `1836` | `0xfe7e...11b4` | `LONG` | 1,125,609.32 USD | `101,142,000.00` | `14.47` | `11.12` | `5.32` | -337,503.83 USD | `-29.98%` | `5X Isolated` |
| `1876` | `0x8af7...fa05` | `SHORT` | 1,098,099.16 USD | `98,661,200.00` | `14.08` | `11.12` | `202.49` | 291,083.38 USD | `+26.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.42` | 4,438.93 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 4.44K USD at 11.4170 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `11.29` | 5,507.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.51K USD at 11.2880 USD [API] | `2026-10-29 02:37:09` |
| `ANNOUNCEMENT` | `INFO` | `11.29` | 5,463.88 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.2890 USD [API] | `2026-10-29 02:37:09` |
| `ANNOUNCEMENT` | `INFO` | `11.37` | 5,443.96 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.44K USD at 11.3700 USD [API] | `2026-10-29 03:13:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+0.50%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.76%`)
  * 48H Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+0.49%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.77%`)
  * 3D Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+0.49%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.77%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.76%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 3,400.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,110.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 272.85 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,550.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 166.93 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 236.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,060.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 11,700.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,720.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 2,650.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 46,090.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 5,340.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,490.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 51,580.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 4,190.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 2,200.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 236,150.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 246.87 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 1,320.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 90,930.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 1,550.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,840.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 43,340.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 38,100.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 639.98 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 1,700.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,620.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 14,100.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 12,010.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 74,330.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 19,810.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 15,600.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 12,460.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 48,080.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 109,290.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 675,380.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 32,650.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 4,450.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 18,570.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 8,530.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 172,030.00 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 6,640.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 12,640.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 67,910.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 64,760.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 38,290.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 53,580.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 12,500.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 24,380.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 361,440.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 26,130.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 67,660.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 451,940.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 86,680.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.10` | 13,440,000.00 USD | 13,440,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.12` | 13,350,000.00 USD | 13,350,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.14` | 13,300,000.00 USD | 13,300,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.16` | 13,250,000.00 USD | 13,250,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.18` | 13,190,000.00 USD | 13,190,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.20` | 13,140,000.00 USD | 13,140,000.00 USD | 14,540.00 USD | 8,360.00 USD | 89.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.22` | 13,110,000.00 USD | 13,110,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.24` | 13,100,000.00 USD | 13,100,000.00 USD | 717.27 USD | 8,580.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,830.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.26` | 13,060,000.00 USD | 13,060,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.28` | 13,020,000.00 USD | 13,020,000.00 USD | 460.95 USD | 5,490.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.30` | 13,010,000.00 USD | 13,010,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.32` | 12,950,000.00 USD | 12,950,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 12,920,000.00 USD | 12,920,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 12,870,000.00 USD | 12,870,000.00 USD | 312.15 USD | 1,970.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 12,870,000.00 USD | 12,870,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 12,840,000.00 USD | 12,840,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 12,800,000.00 USD | 12,800,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 12,760,000.00 USD | 12,760,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 47,390.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 12,700,000.00 USD | 12,700,000.00 USD | 94,230.00 USD | 0.00 USD | 5.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 12,600,000.00 USD | 12,600,000.00 USD | 133.83 USD | 1,630.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 12,600,000.00 USD | 12,600,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 911.85 USD | 207.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 12,540,000.00 USD | 12,540,000.00 USD | 472.74 USD | 15,010.00 USD | 217.03 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 53,950.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 12,520,000.00 USD | 12,520,000.00 USD | 160.73 USD | 16,080.00 USD | 71,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 12,430,000.00 USD | 12,430,000.00 USD | 38,760.00 USD | 722.15 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 12,390,000.00 USD | 12,390,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 12,180,000.00 USD | 12,180,000.00 USD | 5,420.00 USD | 0.00 USD | 11.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 12,170,000.00 USD | 12,170,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.65` | 10,140,000.00 USD | 10,140,000.00 USD | 7,190.00 USD | 2,710.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 201,620.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 12,150,000.00 USD | 12,150,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.67` | 10,120,000.00 USD | 10,120,000.00 USD | 2,470.00 USD | 4,140.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.69` | 10,090,000.00 USD | 10,090,000.00 USD | 13,270.00 USD | 112.73 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 12,110,000.00 USD | 12,110,000.00 USD | 7,710.00 USD | 0.00 USD | 379.91 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.71` | 10,060,000.00 USD | 10,060,000.00 USD | 2,940.00 USD | 1,430.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.73` | 10,040,000.00 USD | 10,040,000.00 USD | 927.37 USD | 1,920.00 USD | 29,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 12,070,000.00 USD | 12,070,000.00 USD | 2,070.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.75` | 10,010,000.00 USD | 10,010,000.00 USD | 40,030.00 USD | 0.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 64,130.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 12,070,000.00 USD | 12,070,000.00 USD | 50,080.00 USD | 0.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.77` | 9,960,000.00 USD | 9,960,000.00 USD | 112,940.00 USD | 7,910.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 671.70 USD | 1,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.79` | 9,810,000.00 USD | 9,810,000.00 USD | 21,960.00 USD | 146.87 USD | 136.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 11,990,000.00 USD | 11,990,000.00 USD | 47,490.00 USD | 14,120.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.81` | 9,790,000.00 USD | 9,790,000.00 USD | 82,520.00 USD | 20,340.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 11,900,000.00 USD | 11,900,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 9,670,000.00 USD | 9,670,000.00 USD | 43,540.00 USD | 266.60 USD | 10,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 11,810,000.00 USD | 11,810,000.00 USD | 50,980.00 USD | 456.90 USD | 13,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.85` | 9,610,000.00 USD | 9,610,000.00 USD | 10,990.00 USD | 7,050.00 USD | 96.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 37,190.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.86` | 11,740,000.00 USD | 11,740,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.87` | 9,600,000.00 USD | 9,600,000.00 USD | 14,610.00 USD | 4,120.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 11,720,000.00 USD | 11,720,000.00 USD | 10,280.00 USD | 15,600.00 USD | 786.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.89` | 9,570,000.00 USD | 9,570,000.00 USD | 8,400.00 USD | 8,240.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 11,700,000.00 USD | 11,700,000.00 USD | 48,670.00 USD | 0.00 USD | 703.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 9,540,000.00 USD | 9,540,000.00 USD | 30,130.00 USD | 32,910.00 USD | 251.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 12,280.00 USD | 551.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 9,480,000.00 USD | 9,480,000.00 USD | 13,840.00 USD | 12,020.00 USD | 225.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 11,630,000.00 USD | 11,630,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 9,450,000.00 USD | 9,450,000.00 USD | 9,450.00 USD | 7,200.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 444,140.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.96` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 11,410.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.97` | 9,420,000.00 USD | 9,420,000.00 USD | 68,690.00 USD | 7,890.00 USD | 53,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 11,530,000.00 USD | 11,530,000.00 USD | 4,830.00 USD | 598.17 USD | 59,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 9,290,000.00 USD | 9,290,000.00 USD | 3,940.00 USD | 6,390.00 USD | 63,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 9,220,000.00 USD | 9,220,000.00 USD | 5,720.00 USD | 584.10 USD | 19,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 11,450,000.00 USD | 11,450,000.00 USD | 8,880.00 USD | 317.30 USD | 415.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 9,200,000.00 USD | 9,200,000.00 USD | 6,170.00 USD | 12,900.00 USD | 414.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 11,440,000.00 USD | 11,440,000.00 USD | 7,200.00 USD | 1,210.00 USD | 146.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 9,180,000.00 USD | 9,180,000.00 USD | 38,520.00 USD | 555.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 787,200.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.06` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 83,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.07` | 9,120,000.00 USD | 9,120,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 11,350,000.00 USD | 11,350,000.00 USD | 218,980.00 USD | 351.10 USD | 111,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 8,950,000.00 USD | 8,950,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 11,020,000.00 USD | 11,020,000.00 USD | 6,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 8,830,000.00 USD | 8,830,000.00 USD | 7,530.00 USD | 41,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 11,010,000.00 USD | 11,010,000.00 USD | 10,140.00 USD | 559.40 USD | 55,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 8,780,000.00 USD | 8,780,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 10,950,000.00 USD | 10,950,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 8,710,000.00 USD | 8,710,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 67,470.00 USD | 249,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.16` | 10,630,000.00 USD | 10,630,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.17` | 8,640,000.00 USD | 8,640,000.00 USD | 127,800.00 USD | 25,060.00 USD | 597.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 10,580,000.00 USD | 10,580,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 8,490,000.00 USD | 8,490,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 10,450,000.00 USD | 10,450,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 8,170,000.00 USD | 8,170,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 9,930,000.00 USD | 9,930,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 7,730,000.00 USD | 7,730,000.00 USD | 105,610.00 USD | 61,740.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 9,390,000.00 USD | 9,390,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 7,270,000.00 USD | 7,270,000.00 USD | 16,630.00 USD | 27,140.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 43,100.00 USD | 182,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 8,940,000.00 USD | 8,940,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.27` | 7,190,000.00 USD | 7,190,000.00 USD | 69,790.00 USD | 18,820.00 USD | 134,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 8,560,000.00 USD | 8,560,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 6,960,000.00 USD | 6,960,000.00 USD | 335,160.00 USD | 2,000.00 USD | 163,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 8,220,000.00 USD | 8,220,000.00 USD | 457,980.00 USD | 0.00 USD | 267.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 6,460,000.00 USD | 6,460,000.00 USD | 19,560.00 USD | 19,240.00 USD | 51,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 7,760,000.00 USD | 7,760,000.00 USD | 43,210.00 USD | 0.00 USD | 99,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 6,370,000.00 USD | 6,370,000.00 USD | 14,540.00 USD | 3,820.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 7,620,000.00 USD | 7,620,000.00 USD | 56,680.00 USD | 0.00 USD | 146.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 6,300,000.00 USD | 6,300,000.00 USD | 60,790.00 USD | 6,620.00 USD | 72,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 139,080.00 USD | 139,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 7,560,000.00 USD | 7,560,000.00 USD | 294,520.00 USD | 0.00 USD | 103,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.37` | 6,160,000.00 USD | 6,160,000.00 USD | 11,590.00 USD | 13,750.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 7,170,000.00 USD | 7,170,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 6,130,000.00 USD | 6,130,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 7,160,000.00 USD | 7,160,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 5,970,000.00 USD | 5,970,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 6,810,000.00 USD | 6,810,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 5,790,000.00 USD | 5,790,000.00 USD | 328,050.00 USD | 0.00 USD | 88,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 6,480,000.00 USD | 6,480,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 5,370,000.00 USD | 5,370,000.00 USD | 329,110.00 USD | 44,950.00 USD | 216,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 152.57 USD | 152.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.46` | 5,690,000.00 USD | 5,690,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.47` | 4,780,000.00 USD | 4,780,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 5,270,000.00 USD | 5,270,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 4,680,000.00 USD | 4,680,000.00 USD | 41,140.00 USD | 38,130.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 5,050,000.00 USD | 5,050,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 4,580,000.00 USD | 4,580,000.00 USD | 11,220.00 USD | 10,370.00 USD | 13,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 4,540,000.00 USD | 4,540,000.00 USD | 71.67 USD | 18,090.00 USD | 117,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 4,410,000.00 USD | 4,410,000.00 USD | 65,860.00 USD | 48,330.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 4,920,000.00 USD | 4,920,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.57` | 4,240,000.00 USD | 4,240,000.00 USD | 39,360.00 USD | 21,900.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 4,170,000.00 USD | 4,170,000.00 USD | 18,130.00 USD | 18,010.00 USD | 15,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 3,670.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 4,720,000.00 USD | 4,720,000.00 USD | 8,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 4,100,000.00 USD | 4,100,000.00 USD | 11,820.00 USD | 1,170.00 USD | 102,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 4,720,000.00 USD | 4,720,000.00 USD | 11,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 3,990,000.00 USD | 3,990,000.00 USD | 30,790.00 USD | 4,060.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 4,700,000.00 USD | 4,700,000.00 USD | 9,470.00 USD | 0.00 USD | 57.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.67` | 3,930,000.00 USD | 3,930,000.00 USD | 29,160.00 USD | 9,040.00 USD | 0.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 2,430.00 USD | 253.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 3,890,000.00 USD | 3,890,000.00 USD | 12,670.00 USD | 6,950.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 4,680,000.00 USD | 4,680,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 3,690,000.00 USD | 3,690,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 877.75 USD | 100,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 3,600,000.00 USD | 3,600,000.00 USD | 89,590.00 USD | 8,370.00 USD | 72.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 4,070,000.00 USD | 4,070,000.00 USD | 16,310.00 USD | 109,140.00 USD | 364.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.77` | 3,510,000.00 USD | 3,510,000.00 USD | 22,390.00 USD | 62,040.00 USD | 51,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 3,940,000.00 USD | 3,940,000.00 USD | 535,020.00 USD | 32,650.00 USD | 104,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 3,370,000.00 USD | 3,370,000.00 USD | 167,900.00 USD | 118,040.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 3,270,000.00 USD | 3,270,000.00 USD | 23,450.00 USD | 70,260.00 USD | 429.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 3,070,000.00 USD | 3,070,000.00 USD | 13,650.00 USD | 5,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 56,610.00 USD | 206,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.83` | 3,050,000.00 USD | 3,050,000.00 USD | 315,520.00 USD | 4,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 2,910,000.00 USD | 2,910,000.00 USD | 193,810.00 USD | 80,420.00 USD | 196,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.85` | 2,730,000.00 USD | 2,730,000.00 USD | 87,770.00 USD | 14,590.00 USD | 148,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 2,440,000.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 334,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.87` | 2,480,000.00 USD | 2,480,000.00 USD | 60,390.00 USD | 6,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 1,780,000.00 USD | 1,780,000.00 USD | 111,430.00 USD | 39,120.00 USD | 347,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.89` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 2,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 221,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.91` | 2,410,000.00 USD | 2,410,000.00 USD | 117,890.00 USD | 904.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 1,060,000.00 USD | 1,060,000.00 USD | 226,910.00 USD | 0.00 USD | 111,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.93` | 2,300,000.00 USD | 2,300,000.00 USD | 3,920.00 USD | 1,010.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 725,060.00 USD | 725,060.00 USD | 2,480.00 USD | 0.00 USD | 380.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.95` | 2,290,000.00 USD | 2,290,000.00 USD | 1,550.00 USD | 1,320.00 USD | 88,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 722,200.00 USD | 722,200.00 USD | 10,430.00 USD | 0.00 USD | 50,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.97` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 178.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 660,910.00 USD | 660,910.00 USD | 17,930.00 USD | 0.00 USD | 209,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.99` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 467.00 USD | 93.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 433,230.00 USD | 433,230.00 USD | 10,830.00 USD | 2,280.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.01` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 3,040.00 USD | 252.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 418,050.00 USD | 418,050.00 USD | 7,900.00 USD | 31,180.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.03` | 2,200,000.00 USD | 2,200,000.00 USD | 51,180.00 USD | 43,470.00 USD | 304,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 235,930.00 USD | 235,930.00 USD | 17,850.00 USD | 40,210.00 USD | 177,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.05` | 1,800,000.00 USD | 1,800,000.00 USD | 310,310.00 USD | 5,150.00 USD | 106,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.06` | 483,970.00 USD | 483,970.00 USD | 351,320.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.07` | 1,370,000.00 USD | 1,370,000.00 USD | 329,150.00 USD | 46,170.00 USD | 169,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.08` | 825,050.00 USD | 825,050.00 USD | 171,900.00 USD | 1,810.00 USD | 167,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.09` | 829,070.00 USD | 829,070.00 USD | 105,500.00 USD | 69,450.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.10` | 1,320,000.00 USD | 1,320,000.00 USD | 301,790.00 USD | 23,300.00 USD | 173,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.11` | 351,890.00 USD | 351,890.00 USD | 254,740.00 USD | 53,870.00 USD | 43,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.12` | 1,940,000.00 USD | 1,940,000.00 USD | 262,770.00 USD | 115,910.00 USD | 234,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 744,030.00 USD | 744,030.00 USD | 440,100.00 USD | 99,350.00 USD | 204,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 2,150,000.00 USD | 2,150,000.00 USD | 204,650.00 USD | 9,980.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 1,050,000.00 USD | 1,050,000.00 USD | 198,370.00 USD | 61,430.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.16` | 2,420,000.00 USD | 2,420,000.00 USD | 131,250.00 USD | 72,860.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 1,190,000.00 USD | 1,190,000.00 USD | 22,450.00 USD | 53,650.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 2,440,000.00 USD | 2,440,000.00 USD | 3,130.00 USD | 13,890.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 1,330,000.00 USD | 1,330,000.00 USD | 72,050.00 USD | 28,650.00 USD | 40,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 2,770,000.00 USD | 2,770,000.00 USD | 171,840.00 USD | 78,020.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 1,720,000.00 USD | 1,720,000.00 USD | 160,950.00 USD | 59,630.00 USD | 164,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 3,280,000.00 USD | 3,280,000.00 USD | 482,460.00 USD | 28,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 2,130,000.00 USD | 2,130,000.00 USD | 262,260.00 USD | 37,760.00 USD | 118,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 3,600,000.00 USD | 3,600,000.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 2,430,000.00 USD | 2,430,000.00 USD | 108,110.00 USD | 39,180.00 USD | 147,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 1,530.00 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.26` | 4,410,000.00 USD | 4,410,000.00 USD | 520,990.00 USD | 0.00 USD | 296,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.27` | 2,920,000.00 USD | 2,920,000.00 USD | 310,520.00 USD | 4,170.00 USD | 172,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 4,860,000.00 USD | 4,860,000.00 USD | 245,580.00 USD | 57,050.00 USD | 147,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 3,440,000.00 USD | 3,440,000.00 USD | 176,550.00 USD | 119,460.00 USD | 225,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 4,940,000.00 USD | 4,940,000.00 USD | 24,980.00 USD | 32,240.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 3,700,000.00 USD | 3,700,000.00 USD | 123,640.00 USD | 68,560.00 USD | 66,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 5,440,000.00 USD | 5,440,000.00 USD | 194,150.00 USD | 23,000.00 USD | 280,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 3,900,000.00 USD | 3,900,000.00 USD | 142,190.00 USD | 33,330.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 5,750,000.00 USD | 5,750,000.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 4,410,000.00 USD | 4,410,000.00 USD | 296,410.00 USD | 121,810.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 1,460.00 USD | 5,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.36` | 6,000,000.00 USD | 6,000,000.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.37` | 4,700,000.00 USD | 4,700,000.00 USD | 152,070.00 USD | 91,520.00 USD | 47,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 6,240,000.00 USD | 6,240,000.00 USD | 70,120.00 USD | 91,810.00 USD | 74,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 4,770,000.00 USD | 4,770,000.00 USD | 14,820.00 USD | 47,470.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 5,040,000.00 USD | 5,040,000.00 USD | 96,590.00 USD | 35,740.00 USD | 140,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 6,510,000.00 USD | 6,510,000.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 5,290,000.00 USD | 5,290,000.00 USD | 64,580.00 USD | 56,490.00 USD | 132,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 6,940,000.00 USD | 6,940,000.00 USD | 303,190.00 USD | 95,260.00 USD | 38,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 5,480,000.00 USD | 5,480,000.00 USD | 77,400.00 USD | 83,200.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 19.46 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.46` | 7,100,000.00 USD | 7,100,000.00 USD | 99,360.00 USD | 55,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.47` | 5,580,000.00 USD | 5,580,000.00 USD | 56,320.00 USD | 19,720.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 7,300,000.00 USD | 7,300,000.00 USD | 54,660.00 USD | 84,840.00 USD | 64,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 5,680,000.00 USD | 5,680,000.00 USD | 33,390.00 USD | 27,450.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 7,380,000.00 USD | 7,380,000.00 USD | 40,840.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 5,780,000.00 USD | 5,780,000.00 USD | 41,360.00 USD | 29,500.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 5,760.00 USD | 33,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 5,900,000.00 USD | 5,900,000.00 USD | 64,080.00 USD | 17,000.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 7,580,000.00 USD | 7,580,000.00 USD | 53,520.00 USD | 0.00 USD | 108,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 6,010,000.00 USD | 6,010,000.00 USD | 73,420.00 USD | 993.85 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 143.22 USD | 6,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.56` | 7,670,000.00 USD | 7,670,000.00 USD | 86,650.00 USD | 793.25 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.57` | 6,130,000.00 USD | 6,130,000.00 USD | 90,730.00 USD | 3,740.00 USD | 23,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 6,190,000.00 USD | 6,190,000.00 USD | 16,690.00 USD | 7,660.00 USD | 39,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 7,780,000.00 USD | 7,780,000.00 USD | 44,670.00 USD | 10,510.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 6,400,000.00 USD | 6,400,000.00 USD | 118,210.00 USD | 512.95 USD | 84,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 7,840,000.00 USD | 7,840,000.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 6,440,000.00 USD | 6,440,000.00 USD | 2,580.00 USD | 6,700.00 USD | 31,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 7,880,000.00 USD | 7,880,000.00 USD | 39,380.00 USD | 1,790.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 6,450,000.00 USD | 6,450,000.00 USD | 2,630.00 USD | 7,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 16,970.00 USD | 23,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.66` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 23,400.00 USD | 80,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.67` | 6,540,000.00 USD | 6,540,000.00 USD | 19,420.00 USD | 11,530.00 USD | 57,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 20,730.00 USD | 71,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 6,680,000.00 USD | 6,680,000.00 USD | 105,090.00 USD | 34,170.00 USD | 491.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 8,120,000.00 USD | 8,120,000.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 6,780,000.00 USD | 6,780,000.00 USD | 74,220.00 USD | 13,000.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 8,450,000.00 USD | 8,450,000.00 USD | 209,440.00 USD | 0.00 USD | 116,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 7,050,000.00 USD | 7,050,000.00 USD | 139,320.00 USD | 11,870.00 USD | 120,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 1,030.00 USD | 90,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 7,170,000.00 USD | 7,170,000.00 USD | 21,990.00 USD | 38,420.00 USD | 61,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 8,640,000.00 USD | 8,640,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 7,250,000.00 USD | 7,250,000.00 USD | 41,180.00 USD | 20,930.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 8,700,000.00 USD | 8,700,000.00 USD | 8,130.00 USD | 0.00 USD | 57,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 7,300,000.00 USD | 7,300,000.00 USD | 12,300.00 USD | 745.35 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 8,840,000.00 USD | 8,840,000.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 18,080.00 USD | 17,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 9,070,000.00 USD | 9,070,000.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 7,390,000.00 USD | 7,390,000.00 USD | 11,070.00 USD | 11,560.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 9,320,000.00 USD | 9,320,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 7,570,000.00 USD | 7,570,000.00 USD | 82,060.00 USD | 9,720.00 USD | 84,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 6,180.00 USD | 100.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 7,660,000.00 USD | 7,660,000.00 USD | 19,640.00 USD | 20,660.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 9,390,000.00 USD | 9,390,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 7,760,000.00 USD | 7,760,000.00 USD | 43,100.00 USD | 13,220.00 USD | 44,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 9,440,000.00 USD | 9,440,000.00 USD | 40,470.00 USD | 14,650.00 USD | 298.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 7,920,000.00 USD | 7,920,000.00 USD | 102,960.00 USD | 18,290.00 USD | 31,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 9,650,000.00 USD | 9,650,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 8,110,000.00 USD | 8,110,000.00 USD | 135,130.00 USD | 28,280.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 9,840,000.00 USD | 9,840,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 8,260,000.00 USD | 8,260,000.00 USD | 84,850.00 USD | 20,720.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 23,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.96` | 10,020,000.00 USD | 10,020,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 8,450,000.00 USD | 8,450,000.00 USD | 71,640.00 USD | 36,280.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 10,680,000.00 USD | 10,680,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 8,630,000.00 USD | 8,630,000.00 USD | 113,870.00 USD | 27,760.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 11,310,000.00 USD | 11,310,000.00 USD | 379,630.00 USD | 31,630.00 USD | 221,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 8,740,000.00 USD | 8,740,000.00 USD | 47,510.00 USD | 9,510.00 USD | 49,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 11,880,000.00 USD | 11,880,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 8,860,000.00 USD | 8,860,000.00 USD | 47,360.00 USD | 41,460.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 12,510,000.00 USD | 12,510,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 9,110,000.00 USD | 9,110,000.00 USD | 149,970.00 USD | 46,150.00 USD | 62,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 13,010,000.00 USD | 13,010,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 9,250,000.00 USD | 9,250,000.00 USD | 34,850.00 USD | 33,440.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 13,680,000.00 USD | 13,680,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 9,320,000.00 USD | 9,320,000.00 USD | 20,990.00 USD | 24,720.00 USD | 27,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 13,860,000.00 USD | 13,860,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 9,520,000.00 USD | 9,520,000.00 USD | 101,970.00 USD | 38,270.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 14,240,000.00 USD | 14,240,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 9,690,000.00 USD | 9,690,000.00 USD | 93,390.00 USD | 33,860.00 USD | 39,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 14,600,000.00 USD | 14,600,000.00 USD | 147,420.00 USD | 92,520.00 USD | 119,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 9,910,000.00 USD | 9,910,000.00 USD | 114,330.00 USD | 42,340.00 USD | 65,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 15,010,000.00 USD | 15,010,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 10,160,000.00 USD | 10,160,000.00 USD | 118,100.00 USD | 60,070.00 USD | 69,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 15,150,000.00 USD | 15,150,000.00 USD | 57,680.00 USD | 54,220.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 10,250,000.00 USD | 10,250,000.00 USD | 59,950.00 USD | 24,020.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 15,490,000.00 USD | 15,490,000.00 USD | 194,760.00 USD | 51,940.00 USD | 91,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 10,360,000.00 USD | 10,360,000.00 USD | 32,170.00 USD | 28,710.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 15,910,000.00 USD | 15,910,000.00 USD | 261,490.00 USD | 56,190.00 USD | 106,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 10,390,000.00 USD | 10,390,000.00 USD | 7,370.00 USD | 18,090.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 16,150,000.00 USD | 16,150,000.00 USD | 70,650.00 USD | 54,230.00 USD | 114,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 10,400,000.00 USD | 10,400,000.00 USD | 2,260.00 USD | 3,780.00 USD | 7,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.26` | 16,450,000.00 USD | 16,450,000.00 USD | 192,800.00 USD | 55,780.00 USD | 50,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.27` | 10,470,000.00 USD | 10,470,000.00 USD | 38,860.00 USD | 8,240.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 16,900,000.00 USD | 16,900,000.00 USD | 215,790.00 USD | 64,650.00 USD | 171,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 10,510,000.00 USD | 10,510,000.00 USD | 23,030.00 USD | 9,340.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 17,240,000.00 USD | 17,240,000.00 USD | 178,010.00 USD | 66,120.00 USD | 97,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 10,530,000.00 USD | 10,530,000.00 USD | 5,780.00 USD | 4,850.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 17,340,000.00 USD | 17,340,000.00 USD | 40,210.00 USD | 38,250.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 17,420,000.00 USD | 17,420,000.00 USD | 48,630.00 USD | 18,250.00 USD | 13,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 25,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 17,500,000.00 USD | 17,500,000.00 USD | 36,210.00 USD | 24,190.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 17,570,000.00 USD | 17,570,000.00 USD | 7,170.00 USD | 6,880.00 USD | 54,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 17,730,000.00 USD | 17,730,000.00 USD | 111,350.00 USD | 41,100.00 USD | 12,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 17,790,000.00 USD | 17,790,000.00 USD | 23,200.00 USD | 21,440.00 USD | 10,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 17,920,000.00 USD | 17,920,000.00 USD | 81,360.00 USD | 284.67 USD | 45,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 18,070,000.00 USD | 18,070,000.00 USD | 39,540.00 USD | 25,610.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 18,180,000.00 USD | 18,180,000.00 USD | 31,320.00 USD | 18,070.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 18,420,000.00 USD | 18,420,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 18,750,000.00 USD | 18,750,000.00 USD | 163,610.00 USD | 39,290.00 USD | 125,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 19,010,000.00 USD | 19,010,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,310.00 USD | 26,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.56` | 19,150,000.00 USD | 19,150,000.00 USD | 86,680.00 USD | 26,470.00 USD | 27,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 19,270,000.00 USD | 19,270,000.00 USD | 41,760.00 USD | 34,570.00 USD | 41,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 19,420,000.00 USD | 19,420,000.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 19,490,000.00 USD | 19,490,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 19,620,000.00 USD | 19,620,000.00 USD | 63,450.00 USD | 42,320.00 USD | 26,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 27,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.66` | 19,660,000.00 USD | 19,660,000.00 USD | 22,530.00 USD | 5,030.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 19,720,000.00 USD | 19,720,000.00 USD | 9,270.00 USD | 18,330.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 19,780,000.00 USD | 19,780,000.00 USD | 2,010.00 USD | 617.78 USD | 52,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 19,890,000.00 USD | 19,890,000.00 USD | 47,740.00 USD | 22,750.00 USD | 40,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 19,990,000.00 USD | 19,990,000.00 USD | 38,570.00 USD | 26,370.00 USD | 40,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 20,050,000.00 USD | 20,050,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 20,230,000.00 USD | 20,230,000.00 USD | 109,130.00 USD | 16,110.00 USD | 52,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 20,320,000.00 USD | 20,320,000.00 USD | 13,700.00 USD | 14,000.00 USD | 60,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 20,340,000.00 USD | 20,340,000.00 USD | 14,750.00 USD | 132.05 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 20,390,000.00 USD | 20,390,000.00 USD | 31,320.00 USD | 15,990.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 535.85 USD | 27,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.86` | 20,460,000.00 USD | 20,460,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 20,500,000.00 USD | 20,500,000.00 USD | 23,610.00 USD | 4,610.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 20,580,000.00 USD | 20,580,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 20,670,000.00 USD | 20,670,000.00 USD | 50,620.00 USD | 13,030.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 20,700,000.00 USD | 20,700,000.00 USD | 27,900.00 USD | 1,070.00 USD | 199.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 20,750,000.00 USD | 20,750,000.00 USD | 13,150.00 USD | 11,970.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 20,780,000.00 USD | 20,780,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 20,870,000.00 USD | 20,870,000.00 USD | 51,470.00 USD | 9,560.00 USD | 20,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 20,880,000.00 USD | 20,880,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 20,880,000.00 USD | 20,880,000.00 USD | 303.50 USD | 335.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.06` | 20,910,000.00 USD | 20,910,000.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.08` | 20,940,000.00 USD | 20,940,000.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 33,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 126,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 126,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 3,520.00 USD | 130,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 29,770.00 USD | 159,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 159,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 160,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 160,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 160,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 162,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 17,400.00 USD | 179,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,430.00 USD | 194,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 296,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 375,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 377,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 26,650.00 USD | 403,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,450.00 USD | 409,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 367.71 USD | 409,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,080.00 USD | 660,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 662,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 27,640.00 USD | 690,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 728.50 USD | 691,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 694,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 695,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 73,030.00 USD | 768,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 713,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.15` | 2,200,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 289.81 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 637.59 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 63,080.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 117.99 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.05` | 1,120.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,040,000.00 USD | 0.00 USD | 3,400.00 USD | `-79.65%` | `1,513,300.00` |
| `Live` | `Long` | `2.45` | 12,040,000.00 USD | 0.00 USD | 1,110.00 USD | `-77.84%` | `452,300.00` |
| `Live` | `Long` | `2.55` | 12,040,000.00 USD | 0.00 USD | 272.85 USD | `-76.94%` | `107,000.00` |
| `Live` | `Long` | `2.65` | 12,040,000.00 USD | 0.00 USD | 2,550.00 USD | `-76.04%` | `961,300.00` |
| `Live` | `Long` | `2.75` | 12,040,000.00 USD | 0.00 USD | 166.93 USD | `-75.13%` | `60,700.00` |
| `Live` | `Long` | `2.95` | 12,030,000.00 USD | 0.00 USD | 236.00 USD | `-73.32%` | `80,000.00` |
| `Live` | `Long` | `3.05` | 12,030,000.00 USD | 0.00 USD | 7,060.00 USD | `-72.42%` | `2,314,200.00` |
| `Live` | `Long` | `3.15` | 12,030,000.00 USD | 0.00 USD | 11,700.00 USD | `-71.51%` | `3,713,900.00` |
| `Live` | `Long` | `3.35` | 12,020,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.71%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,010,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.80%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,010,000.00 USD | 0.00 USD | 126.73 USD | `-67.90%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,010,000.00 USD | 0.00 USD | 2,720.00 USD | `-66.99%` | `744,400.00` |
| `Live` | `Long` | `3.75` | 12,000,000.00 USD | 0.00 USD | 2,650.00 USD | `-66.09%` | `707,000.00` |
| `Live` | `Long` | `3.95` | 12,000,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.28%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,000,000.00 USD | 0.00 USD | 46,090.00 USD | `-63.37%` | `11,379,400.00` |
| `Live` | `Long` | `4.15` | 11,950,000.00 USD | 0.00 USD | 5,340.00 USD | `-62.47%` | `1,287,000.00` |
| `Live` | `Long` | `4.25` | 11,940,000.00 USD | 0.00 USD | 5,490.00 USD | `-61.57%` | `1,292,800.00` |
| `Live` | `Long` | `4.45` | 11,940,000.00 USD | 0.00 USD | 51,580.00 USD | `-59.76%` | `11,590,800.00` |
| `Live` | `Long` | `4.55` | 11,890,000.00 USD | 0.00 USD | 4,190.00 USD | `-58.85%` | `919,800.00` |
| `Live` | `Long` | `4.65` | 11,880,000.00 USD | 0.00 USD | 2,200.00 USD | `-57.95%` | `473,800.00` |
| `Live` | `Long` | `4.75` | 11,880,000.00 USD | 0.00 USD | 236,150.00 USD | `-57.04%` | `49,716,700.00` |
| `Live` | `Long` | `4.85` | 11,650,000.00 USD | 0.00 USD | 246.87 USD | `-56.14%` | `50,900.00` |
| `Live` | `Long` | `4.95` | 11,640,000.00 USD | 0.00 USD | 1,320.00 USD | `-55.24%` | `266,200.00` |
| `Live` | `Long` | `5.05` | 11,640,000.00 USD | 0.00 USD | 90,930.00 USD | `-54.33%` | `18,006,100.00` |
| `Live` | `Long` | `5.15` | 11,550,000.00 USD | 0.00 USD | 1,550.00 USD | `-53.43%` | `301,800.00` |
| `Live` | `Long` | `5.25` | 11,550,000.00 USD | 0.00 USD | 5,840.00 USD | `-52.52%` | `1,111,800.00` |
| `Live` | `Long` | `5.35` | 11,550,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.62%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,000,000.00 USD | 0.00 USD | 138.97 USD | `-50.71%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 11,000,000.00 USD | 0.00 USD | 43,340.00 USD | `-49.81%` | `7,808,700.00` |
| `Live` | `Long` | `5.65` | 10,960,000.00 USD | 0.00 USD | 38,100.00 USD | `-48.91%` | `6,743,300.00` |
| `Live` | `Long` | `5.75` | 10,920,000.00 USD | 0.00 USD | 639.98 USD | `-48.00%` | `111,300.00` |
| `Live` | `Long` | `5.85` | 10,920,000.00 USD | 0.00 USD | 1,700.00 USD | `-47.10%` | `290,500.00` |
| `Live` | `Long` | `5.95` | 10,920,000.00 USD | 0.00 USD | 10,620.00 USD | `-46.19%` | `1,784,100.00` |
| `Live` | `Long` | `6.05` | 10,910,000.00 USD | 0.00 USD | 14,100.00 USD | `-45.29%` | `2,331,000.00` |
| `Live` | `Long` | `6.15` | 10,890,000.00 USD | 0.00 USD | 12,010.00 USD | `-44.38%` | `1,952,800.00` |
| `Live` | `Long` | `6.25` | 10,880,000.00 USD | 0.00 USD | 74,330.00 USD | `-43.48%` | `11,892,600.00` |
| `Live` | `Long` | `6.35` | 10,810,000.00 USD | 0.00 USD | 19,810.00 USD | `-42.58%` | `3,120,000.00` |
| `Live` | `Long` | `6.45` | 10,790,000.00 USD | 0.00 USD | 15,600.00 USD | `-41.67%` | `2,418,300.00` |
| `Live` | `Long` | `6.55` | 10,770,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.77%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 10,770,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.86%` | `170,234,200.00` |
| `Live` | `Long` | `6.75` | 9,640,000.00 USD | 0.00 USD | 12,460.00 USD | `-38.96%` | `1,846,500.00` |
| `Live` | `Long` | `6.85` | 9,630,000.00 USD | 0.00 USD | 48,080.00 USD | `-38.05%` | `7,018,900.00` |
| `Live` | `Long` | `6.95` | 9,580,000.00 USD | 0.00 USD | 109,290.00 USD | `-37.15%` | `15,724,500.00` |
| `Live` | `Long` | `7.05` | 9,470,000.00 USD | 0.00 USD | 675,380.00 USD | `-36.25%` | `95,799,200.00` |
| `Live` | `Long` | `7.15` | 8,790,000.00 USD | 0.00 USD | 32,650.00 USD | `-35.34%` | `4,565,800.00` |
| `Live` | `Long` | `7.25` | 8,760,000.00 USD | 0.00 USD | 4,450.00 USD | `-34.44%` | `613,700.00` |
| `Live` | `Long` | `7.35` | 8,760,000.00 USD | 0.00 USD | 18,570.00 USD | `-33.53%` | `2,526,400.00` |
| `Live` | `Long` | `7.45` | 8,740,000.00 USD | 0.00 USD | 8,530.00 USD | `-32.63%` | `1,145,600.00` |
| `Live` | `Long` | `7.55` | 8,730,000.00 USD | 0.00 USD | 172,030.00 USD | `-31.72%` | `22,784,800.00` |
| `Live` | `Long` | `7.65` | 8,560,000.00 USD | 0.00 USD | 6,640.00 USD | `-30.82%` | `868,100.00` |
| `Live` | `Long` | `7.75` | 8,550,000.00 USD | 0.00 USD | 12,640.00 USD | `-29.91%` | `1,630,600.00` |
| `Live` | `Long` | `7.85` | 8,540,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-29.01%` | `401,109,100.00` |
| `Live` | `Long` | `7.95` | 5,390,000.00 USD | 0.00 USD | 67,910.00 USD | `-28.11%` | `8,542,600.00` |
| `Live` | `Long` | `8.05` | 5,320,000.00 USD | 0.00 USD | 64,760.00 USD | `-27.20%` | `8,044,600.00` |
| `Live` | `Long` | `8.15` | 5,260,000.00 USD | 0.00 USD | 38,290.00 USD | `-26.30%` | `4,697,800.00` |
| `Live` | `Long` | `8.25` | 5,220,000.00 USD | 0.00 USD | 53,580.00 USD | `-25.39%` | `6,494,000.00` |
| `Live` | `Long` | `8.35` | 5,160,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.49%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,160,000.00 USD | 0.00 USD | 12,500.00 USD | `-23.58%` | `1,478,800.00` |
| `Live` | `Long` | `8.55` | 5,150,000.00 USD | 0.00 USD | 24,380.00 USD | `-22.68%` | `2,851,500.00` |
| `Live` | `Long` | `8.65` | 5,120,000.00 USD | 0.00 USD | 361,440.00 USD | `-21.78%` | `41,785,400.00` |
| `Live` | `Long` | `8.75` | 4,760,000.00 USD | 0.00 USD | 26,130.00 USD | `-20.87%` | `2,986,200.00` |
| `Live` | `Long` | `8.85` | 4,730,000.00 USD | 0.00 USD | 67,660.00 USD | `-19.97%` | `7,644,700.00` |
| `Live` | `Long` | `8.95` | 4,670,000.00 USD | 0.00 USD | 451,940.00 USD | `-19.06%` | `50,496,300.00` |
| `Live` | `Long` | `9.05` | 4,210,000.00 USD | 0.00 USD | 86,680.00 USD | `-18.16%` | `9,577,800.00` |
| `Live` | `Long` | `9.15` | 4,130,000.00 USD | 0.00 USD | 76,340.00 USD | `-17.25%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,050,000.00 USD | 0.00 USD | 17,830.00 USD | `-16.35%` | `1,928,000.00` |
| `Live` | `Long` | `9.35` | 4,030,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.45%` | `229,680,600.00` |
| `Live` | `Long` | `9.45` | 1,890,000.00 USD | 0.00 USD | 47,390.00 USD | `-14.54%` | `5,015,000.00` |
| `Live` | `Long` | `9.55` | 1,840,000.00 USD | 0.00 USD | 53,950.00 USD | `-13.64%` | `5,648,900.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 201,620.00 USD | `-12.73%` | `20,893,400.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 64,130.00 USD | `-11.83%` | `6,577,800.00` |
| `Live` | `Long` | `9.85` | 1,520,000.00 USD | 0.00 USD | 37,190.00 USD | `-10.92%` | `3,775,800.00` |
| `Live` | `Long` | `9.95` | 1,480,000.00 USD | 0.00 USD | 444,140.00 USD | `-10.02%` | `44,637,000.00` |
| `Live` | `Long` | `10.05` | 1,040,000.00 USD | 0.00 USD | 787,200.00 USD | `-9.12%` | `78,328,800.00` |
| `Live` | `Long` | `10.15` | 249,810.00 USD | 0.00 USD | 67,470.00 USD | `-8.21%` | `6,647,400.00` |
| `Live` | `Long` | `10.25` | 182,340.00 USD | 0.00 USD | 43,100.00 USD | `-7.31%` | `4,205,100.00` |
| `Live` | `Long` | `10.35` | 139,230.00 USD | 0.00 USD | 139,080.00 USD | `-6.40%` | `13,437,900.00` |
| `Live` | `Long` | `10.45` | 152.57 USD | 0.00 USD | 152.57 USD | `-5.50%` | `14,600.00` |
| `Live` | `Short` | `11.15` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | `+0.83%` | `266,300.00` |
| `Live` | `Short` | `11.25` | 4,500.00 USD | 1,530.00 USD | 0.00 USD | `+1.74%` | `135,800.00` |
| `Live` | `Short` | `11.35` | 5,960.00 USD | 1,460.00 USD | 0.00 USD | `+2.64%` | `129,000.00` |
| `Live` | `Short` | `11.45` | 5,980.00 USD | 19.46 USD | 0.00 USD | `+3.54%` | `1,700.00` |
| `Live` | `Short` | `11.55` | 6,120.00 USD | 143.22 USD | 0.00 USD | `+4.45%` | `12,400.00` |
| `Live` | `Short` | `11.65` | 23,100.00 USD | 16,970.00 USD | 0.00 USD | `+5.35%` | `1,456,900.00` |
| `Live` | `Short` | `11.95` | 23,380.00 USD | 283.21 USD | 0.00 USD | `+8.07%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 24,810.00 USD | 1,430.00 USD | 0.00 USD | `+10.78%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 25,550.00 USD | 736.06 USD | 0.00 USD | `+11.68%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 26,860.00 USD | 1,310.00 USD | 0.00 USD | `+13.49%` | `104,500.00` |
| `Live` | `Short` | `12.65` | 27,290.00 USD | 435.16 USD | 0.00 USD | `+14.40%` | `34,400.00` |
| `Live` | `Short` | `12.85` | 27,830.00 USD | 535.85 USD | 0.00 USD | `+16.21%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 33,260.00 USD | 5,430.00 USD | 0.00 USD | `+21.63%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 126,150.00 USD | 92,890.00 USD | 0.00 USD | `+22.54%` | `6,855,700.00` |
| `Live` | `Short` | `14.15` | 126,500.00 USD | 349.51 USD | 0.00 USD | `+27.96%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 130,020.00 USD | 3,520.00 USD | 0.00 USD | `+28.87%` | `246,800.00` |
| `Live` | `Short` | `14.95` | 159,790.00 USD | 29,770.00 USD | 0.00 USD | `+35.20%` | `1,991,000.00` |
| `Live` | `Short` | `15.25` | 159,940.00 USD | 155.55 USD | 0.00 USD | `+37.91%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 160,520.00 USD | 578.46 USD | 0.00 USD | `+40.62%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 160,790.00 USD | 271.04 USD | 0.00 USD | `+43.34%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 160,930.00 USD | 138.76 USD | 0.00 USD | `+44.24%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 162,320.00 USD | 1,390.00 USD | 0.00 USD | `+47.86%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 179,730.00 USD | 17,400.00 USD | 0.00 USD | `+48.76%` | `1,058,000.00` |
| `Live` | `Short` | `16.55` | 194,150.00 USD | 14,430.00 USD | 0.00 USD | `+49.67%` | `871,700.00` |
| `Live` | `Short` | `16.75` | 296,060.00 USD | 101,910.00 USD | 0.00 USD | `+51.47%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 375,830.00 USD | 79,770.00 USD | 0.00 USD | `+53.28%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 377,200.00 USD | 1,370.00 USD | 0.00 USD | `+55.09%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 403,850.00 USD | 26,650.00 USD | 0.00 USD | `+56.00%` | `1,544,800.00` |
| `Live` | `Short` | `17.65` | 409,300.00 USD | 5,450.00 USD | 0.00 USD | `+59.61%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 409,670.00 USD | 367.71 USD | 0.00 USD | `+61.42%` | `20,600.00` |
| `Live` | `Short` | `17.95` | 660,750.00 USD | 251,080.00 USD | 0.00 USD | `+62.33%` | `13,987,600.00` |
| `Live` | `Short` | `18.05` | 662,720.00 USD | 1,970.00 USD | 0.00 USD | `+63.23%` | `109,300.00` |
| `Live` | `Short` | `18.15` | 690,360.00 USD | 27,640.00 USD | 0.00 USD | `+64.13%` | `1,523,000.00` |
| `Live` | `Short` | `18.35` | 691,090.00 USD | 728.50 USD | 0.00 USD | `+65.94%` | `39,700.00` |
| `Live` | `Short` | `18.45` | 694,980.00 USD | 3,890.00 USD | 0.00 USD | `+66.85%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 695,170.00 USD | 185.50 USD | 0.00 USD | `+67.75%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 695,350.00 USD | 186.50 USD | 0.00 USD | `+68.66%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 768,380.00 USD | 73,030.00 USD | 0.00 USD | `+69.56%` | `3,895,000.00` |
| `Live` | `Short` | `18.85` | 1,480,000.00 USD | 713,280.00 USD | 0.00 USD | `+70.46%` | `37,839,800.00` |
| `Live` | `Short` | `19.15` | 3,680,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+73.18%` | `115,024,600.00` |
| `Live` | `Short` | `19.55` | 3,680,000.00 USD | 316.71 USD | 0.00 USD | `+76.80%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,720,000.00 USD | 38,790.00 USD | 0.00 USD | `+77.70%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,720,000.00 USD | 359.45 USD | 0.00 USD | `+78.60%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 3,720,000.00 USD | 289.81 USD | 0.00 USD | `+79.51%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,720,000.00 USD | 637.59 USD | 0.00 USD | `+81.32%` | `31,800.00` |
| `Live` | `Short` | `20.15` | 3,730,000.00 USD | 1,260.00 USD | 0.00 USD | `+82.22%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,730,000.00 USD | 1,770.00 USD | 0.00 USD | `+84.93%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,740,000.00 USD | 7,250.00 USD | 0.00 USD | `+85.84%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,740,000.00 USD | 114.68 USD | 0.00 USD | `+88.55%` | `5,500.00` |
| `Live` | `Short` | `21.75` | 3,800,000.00 USD | 63,080.00 USD | 0.00 USD | `+96.69%` | `2,900,400.00` |
| `Live` | `Short` | `21.85` | 3,800,000.00 USD | 117.99 USD | 0.00 USD | `+97.59%` | `5,400.00` |
| `Live` | `Short` | `22.05` | 3,800,000.00 USD | 1,120.00 USD | 0.00 USD | `+99.40%` | `50,600.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 549,930.00 USD | 0.00 USD | 182.03 USD | `-77.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 549,750.00 USD | 0.00 USD | 234.23 USD | `-73.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 549,520.00 USD | 0.00 USD | 209.48 USD | `-71.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 549,310.00 USD | 0.00 USD | 680.89 USD | `-67.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 548,630.00 USD | 0.00 USD | 290.29 USD | `-58.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 548,340.00 USD | 0.00 USD | 120.22 USD | `-52.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 548,220.00 USD | 0.00 USD | 251.68 USD | `-45.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 547,960.00 USD | 0.00 USD | 749.30 USD | `-42.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 547,210.00 USD | 0.00 USD | 772.71 USD | `-41.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 546,440.00 USD | 0.00 USD | 3,760.00 USD | `-40.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 542,680.00 USD | 0.00 USD | 133.00 USD | `-39.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 542,540.00 USD | 0.00 USD | 1,320.00 USD | `-37.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 541,230.00 USD | 0.00 USD | 3,770.00 USD | `-36.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 537,460.00 USD | 0.00 USD | 2,070.00 USD | `-34.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 535,390.00 USD | 0.00 USD | 3,740.00 USD | `-32.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 531,650.00 USD | 0.00 USD | 1,050.00 USD | `-31.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 530,590.00 USD | 0.00 USD | 120.90 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 530,470.00 USD | 0.00 USD | 146.80 USD | `-29.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 530,330.00 USD | 0.00 USD | 124.02 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 530,200.00 USD | 0.00 USD | 5,000.00 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 525,200.00 USD | 0.00 USD | 520.78 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 524,680.00 USD | 0.00 USD | 10,560.00 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 514,110.00 USD | 0.00 USD | 60,230.00 USD | `-24.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 453,890.00 USD | 0.00 USD | 1,480.00 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 452,410.00 USD | 0.00 USD | 52,990.00 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 399,420.00 USD | 0.00 USD | 186.84 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 399,240.00 USD | 0.00 USD | 742.88 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 398,490.00 USD | 0.00 USD | 902.70 USD | `-19.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 397,590.00 USD | 0.00 USD | 1,570.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 396,020.00 USD | 0.00 USD | 4,460.00 USD | `-18.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 391,570.00 USD | 0.00 USD | 194.90 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 391,370.00 USD | 0.00 USD | 232.18 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 391,140.00 USD | 0.00 USD | 7,060.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 384,080.00 USD | 0.00 USD | 518.80 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 383,560.00 USD | 0.00 USD | 19,460.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 364,100.00 USD | 0.00 USD | 686.12 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 363,420.00 USD | 0.00 USD | 2,370.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 361,040.00 USD | 0.00 USD | 24,850.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 336,190.00 USD | 0.00 USD | 13,710.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 322,480.00 USD | 0.00 USD | 42,800.00 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 279,680.00 USD | 0.00 USD | 51,460.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 228,230.00 USD | 0.00 USD | 107,370.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 120,860.00 USD | 0.00 USD | 731.75 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 120,130.00 USD | 0.00 USD | 2,220.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 117,900.00 USD | 0.00 USD | 12,710.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 105,190.00 USD | 0.00 USD | 19,870.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 85,320.00 USD | 0.00 USD | 1,760.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 83,560.00 USD | 0.00 USD | 5,430.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 78,140.00 USD | 0.00 USD | 188.34 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 77,950.00 USD | 0.00 USD | 77,950.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 24,230.00 USD | 24,230.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 38,780.00 USD | 14,550.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 60,420.00 USD | 21,640.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 60,820.00 USD | 396.17 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 98,890.00 USD | 38,070.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 101,670.00 USD | 2,790.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 103,120.00 USD | 1,440.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 103,230.00 USD | 110.21 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 107,050.00 USD | 3,820.00 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 135,020.00 USD | 27,980.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 136,850.00 USD | 1,820.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 230,240.00 USD | 93,390.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 230,840.00 USD | 597.74 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 235,730.00 USD | 4,890.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 292,510.00 USD | 56,780.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 298,690.00 USD | 6,180.00 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 299,370.00 USD | 679.57 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 319,730.00 USD | 20,360.00 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 320,180.00 USD | 451.95 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 336,810.00 USD | 16,630.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 337,730.00 USD | 919.19 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 339,050.00 USD | 1,320.00 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 346,830.00 USD | 7,790.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 349,370.00 USD | 2,540.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 349,540.00 USD | 165.31 USD | 0.00 USD | `+22.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 350,490.00 USD | 954.14 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 370,040.00 USD | 19,550.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 374,920.00 USD | 4,880.00 USD | 0.00 USD | `+25.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 375,190.00 USD | 266.44 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 391,450.00 USD | 16,260.00 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 391,600.00 USD | 152.82 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 395,880.00 USD | 4,280.00 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 399,290.00 USD | 3,410.00 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 418,730.00 USD | 19,440.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 418,950.00 USD | 218.25 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 421,470.00 USD | 2,520.00 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 428,740.00 USD | 7,270.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 429,690.00 USD | 950.82 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 454,540.00 USD | 24,860.00 USD | 0.00 USD | `+36.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 456,990.00 USD | 2,450.00 USD | 0.00 USD | `+37.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 690,030.00 USD | 233,040.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 690,960.00 USD | 924.07 USD | 0.00 USD | `+38.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 691,850.00 USD | 893.01 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 692,500.00 USD | 653.10 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 692,970.00 USD | 472.63 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 696,270.00 USD | 3,290.00 USD | 0.00 USD | `+42.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 699,440.00 USD | 3,170.00 USD | 0.00 USD | `+43.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 704,570.00 USD | 5,130.00 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 719,650.00 USD | 15,080.00 USD | 0.00 USD | `+45.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 726,450.00 USD | 6,800.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 732,950.00 USD | 6,500.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 739,490.00 USD | 6,540.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 746,070.00 USD | 6,580.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 756,000.00 USD | 9,930.00 USD | 0.00 USD | `+49.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 859,980.00 USD | 103,980.00 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 874,220.00 USD | 14,240.00 USD | 0.00 USD | `+51.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 958,580.00 USD | 84,360.00 USD | 0.00 USD | `+52.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 960,270.00 USD | 1,700.00 USD | 0.00 USD | `+53.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 967,640.00 USD | 7,370.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 984,330.00 USD | 16,690.00 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 986,630.00 USD | 2,300.00 USD | 0.00 USD | `+56.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 988,360.00 USD | 1,740.00 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,010,000.00 USD | 21,690.00 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,010,000.00 USD | 4,390.00 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,020,000.00 USD | 4,410.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,020,000.00 USD | 4,440.00 USD | 0.00 USD | `+60.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,030,000.00 USD | 4,460.00 USD | 0.00 USD | `+61.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,030,000.00 USD | 448.75 USD | 0.00 USD | `+62.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,060,000.00 USD | 30,960.00 USD | 0.00 USD | `+63.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,060,000.00 USD | 453.75 USD | 0.00 USD | `+64.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,060,000.00 USD | 456.25 USD | 0.00 USD | `+65.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,060,000.00 USD | 458.75 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,060,000.00 USD | 461.25 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,070,000.00 USD | 4,540.00 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,070,000.00 USD | 466.25 USD | 0.00 USD | `+68.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,070,000.00 USD | 468.75 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,070,000.00 USD | 471.25 USD | 0.00 USD | `+70.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,070,000.00 USD | 473.75 USD | 0.00 USD | `+71.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,130,000.00 USD | 67,000.00 USD | 0.00 USD | `+72.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,130,000.00 USD | 574.50 USD | 0.00 USD | `+73.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,140,000.00 USD | 577.50 USD | 0.00 USD | `+74.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,140,000.00 USD | 2,710.00 USD | 0.00 USD | `+74.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,140,000.00 USD | 972.50 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,150,000.00 USD | 7,680.00 USD | 0.00 USD | `+76.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,150,000.00 USD | 786.00 USD | 0.00 USD | `+77.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,150,000.00 USD | 790.00 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,150,000.00 USD | 992.50 USD | 0.00 USD | `+79.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,150,000.00 USD | 997.50 USD | 0.00 USD | `+80.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,750,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+81.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,750,000.00 USD | 1,010.00 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,760,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,760,000.00 USD | 1,040.00 USD | 0.00 USD | `+87.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,760,000.00 USD | 1,410.00 USD | 0.00 USD | `+88.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,760,000.00 USD | 1,050.00 USD | 0.00 USD | `+89.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,770,000.00 USD | 4,000.00 USD | 0.00 USD | `+90.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,820,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,820,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+94.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,820,000.00 USD | 1,090.00 USD | 0.00 USD | `+96.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,820,000.00 USD | 3,280.00 USD | 0.00 USD | `+97.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+98.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,830,000.00 USD | 1,110.00 USD | 0.00 USD | `+100.31%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.10` | 13,440,000.00 USD | 0.00 USD | 13,440,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,220.00 USD |
| `7D` | `9.12` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,760.00 USD |
| `7D` | `9.14` | 13,300,000.00 USD | 0.00 USD | 13,300,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,970.00 USD |
| `7D` | `9.16` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD |
| `7D` | `9.18` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,160.00 USD |
| `7D` | `9.20` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 14,540.00 USD | 8,360.00 USD | 89.68 USD |
| `7D` | `9.22` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,420.00 USD |
| `7D` | `9.24` | 13,100,000.00 USD | 0.00 USD | 13,100,000.00 USD | 717.27 USD | 8,580.00 USD | 23,920.00 USD |
| `7D` | `9.26` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,640.00 USD |
| `7D` | `9.28` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 460.95 USD | 5,490.00 USD | 11,830.00 USD |
| `7D` | `9.30` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,560.00 USD |
| `7D` | `9.32` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,670.00 USD |
| `7D` | `9.34` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,860.00 USD |
| `7D` | `9.36` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 312.15 USD | 1,970.00 USD | 4,660.00 USD |
| `7D` | `9.38` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,350.00 USD |
| `7D` | `9.40` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,350.00 USD |
| `7D` | `9.42` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,300.00 USD |
| `7D` | `9.44` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD |
| `7D` | `9.46` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 94,230.00 USD | 0.00 USD | 5.92 USD |
| `7D` | `9.48` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 133.83 USD | 1,630.00 USD | 2,570.00 USD |
| `7D` | `9.50` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,620.00 USD |
| `7D` | `9.52` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 0.00 USD | 911.85 USD | 207.05 USD |
| `7D` | `9.54` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 472.74 USD | 15,010.00 USD | 217.03 USD |
| `7D` | `9.56` | 12,520,000.00 USD | 0.00 USD | 12,520,000.00 USD | 160.73 USD | 16,080.00 USD | 71,290.00 USD |
| `7D` | `9.58` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 38,760.00 USD | 722.15 USD | 4,200.00 USD |
| `7D` | `9.60` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD |
| `7D` | `9.62` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 5,420.00 USD | 0.00 USD | 11.28 USD |
| `7D` | `9.64` | 12,170,000.00 USD | 0.00 USD | 12,170,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,460.00 USD |
| `1D` | `9.65` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 7,190.00 USD | 2,710.00 USD | 14,650.00 USD |
| `7D` | `9.66` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.67` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 2,470.00 USD | 4,140.00 USD | 17,550.00 USD |
| `7D` | `9.68` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.69` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 13,270.00 USD | 112.73 USD | 16,240.00 USD |
| `7D` | `9.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 7,710.00 USD | 0.00 USD | 379.91 USD |
| `1D` | `9.71` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 2,940.00 USD | 1,430.00 USD | 15,950.00 USD |
| `7D` | `9.72` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.73` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 927.37 USD | 1,920.00 USD | 29,420.00 USD |
| `7D` | `9.74` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 2,070.00 USD | 0.00 USD | 413.42 USD |
| `1D` | `9.75` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 40,030.00 USD | 0.00 USD | 13,440.00 USD |
| `7D` | `9.76` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 50,080.00 USD | 0.00 USD | 26,530.00 USD |
| `1D` | `9.77` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 112,940.00 USD | 7,910.00 USD | 24,590.00 USD |
| `7D` | `9.78` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 0.00 USD | 671.70 USD | 1,420.00 USD |
| `1D` | `9.79` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 21,960.00 USD | 146.87 USD | 136.96 USD |
| `7D` | `9.80` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 47,490.00 USD | 14,120.00 USD | 25,050.00 USD |
| `1D` | `9.81` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 82,520.00 USD | 20,340.00 USD | 17,170.00 USD |
| `7D` | `9.82` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `9.83` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 43,540.00 USD | 266.60 USD | 10,810.00 USD |
| `7D` | `9.84` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 50,980.00 USD | 456.90 USD | 13,280.00 USD |
| `1D` | `9.85` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 10,990.00 USD | 7,050.00 USD | 96.26 USD |
| `7D` | `9.86` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD |
| `1D` | `9.87` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 14,610.00 USD | 4,120.00 USD | 10,090.00 USD |
| `7D` | `9.88` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 10,280.00 USD | 15,600.00 USD | 786.13 USD |
| `1D` | `9.89` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 8,400.00 USD | 8,240.00 USD | 10,580.00 USD |
| `7D` | `9.90` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 48,670.00 USD | 0.00 USD | 703.81 USD |
| `1D` | `9.91` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 30,130.00 USD | 32,910.00 USD | 251.76 USD |
| `7D` | `9.92` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 0.00 USD | 12,280.00 USD | 551.50 USD |
| `1D` | `9.93` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 13,840.00 USD | 12,020.00 USD | 225.54 USD |
| `7D` | `9.94` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,000.00 USD |
| `1D` | `9.95` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 9,450.00 USD | 7,200.00 USD | 8,550.00 USD |
| `7D` | `9.96` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 0.00 USD | 11,410.00 USD | 1,900.00 USD |
| `1D` | `9.97` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 68,690.00 USD | 7,890.00 USD | 53,900.00 USD |
| `7D` | `9.98` | 11,530,000.00 USD | 0.00 USD | 11,530,000.00 USD | 4,830.00 USD | 598.17 USD | 59,210.00 USD |
| `1D` | `9.99` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 3,940.00 USD | 6,390.00 USD | 63,520.00 USD |
| `7D` | `10.00` | 11,460,000.00 USD | 0.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 13,240.00 USD |
| `1D` | `10.01` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 5,720.00 USD | 584.10 USD | 19,000.00 USD |
| `7D` | `10.02` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 8,880.00 USD | 317.30 USD | 415.56 USD |
| `1D` | `10.03` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 6,170.00 USD | 12,900.00 USD | 414.03 USD |
| `7D` | `10.04` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 7,200.00 USD | 1,210.00 USD | 146.67 USD |
| `1D` | `10.05` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 38,520.00 USD | 555.00 USD | 18,830.00 USD |
| `7D` | `10.06` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 83,650.00 USD |
| `1D` | `10.07` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 80,530.00 USD | 2,910.00 USD | 84,320.00 USD |
| `7D` | `10.08` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 218,980.00 USD | 351.10 USD | 111,570.00 USD |
| `1D` | `10.09` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 87,890.00 USD | 10,060.00 USD | 20,020.00 USD |
| `7D` | `10.10` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 6,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 7,530.00 USD | 41,480.00 USD | 0.00 USD |
| `7D` | `10.12` | 11,010,000.00 USD | 0.00 USD | 11,010,000.00 USD | 10,140.00 USD | 559.40 USD | 55,860.00 USD |
| `1D` | `10.13` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 16,580.00 USD | 23,610.00 USD | 34,430.00 USD |
| `7D` | `10.14` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,210.00 USD |
| `1D` | `10.15` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 10,060.00 USD | 18,770.00 USD | 38,630.00 USD |
| `7D` | `10.16` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,210.00 USD |
| `1D` | `10.17` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 127,800.00 USD | 25,060.00 USD | 597.86 USD |
| `7D` | `10.18` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,940.00 USD |
| `1D` | `10.19` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 48,570.00 USD | 30,250.00 USD | 235,260.00 USD |
| `7D` | `10.20` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,660.00 USD |
| `1D` | `10.21` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 194,140.00 USD | 34,280.00 USD | 218,680.00 USD |
| `7D` | `10.22` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,080.00 USD |
| `1D` | `10.23` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 105,610.00 USD | 61,740.00 USD | 290,870.00 USD |
| `7D` | `10.24` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,090.00 USD |
| `1D` | `10.25` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 16,630.00 USD | 27,140.00 USD | 38,550.00 USD |
| `7D` | `10.26` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,490.00 USD |
| `1D` | `10.27` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 69,790.00 USD | 18,820.00 USD | 134,000.00 USD |
| `7D` | `10.28` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,580.00 USD |
| `1D` | `10.29` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 335,160.00 USD | 2,000.00 USD | 163,000.00 USD |
| `7D` | `10.30` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 457,980.00 USD | 0.00 USD | 267.66 USD |
| `1D` | `10.31` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 19,560.00 USD | 19,240.00 USD | 51,980.00 USD |
| `7D` | `10.32` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 43,210.00 USD | 0.00 USD | 99,860.00 USD |
| `1D` | `10.33` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 14,540.00 USD | 3,820.00 USD | 52,280.00 USD |
| `7D` | `10.34` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 56,680.00 USD | 0.00 USD | 146.32 USD |
| `1D` | `10.35` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 60,790.00 USD | 6,620.00 USD | 72,730.00 USD |
| `7D` | `10.36` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 294,520.00 USD | 0.00 USD | 103,880.00 USD |
| `1D` | `10.37` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 11,590.00 USD | 13,750.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.39` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 34,090.00 USD | 66,760.00 USD | 59,000.00 USD |
| `7D` | `10.40` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.41` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 169,800.00 USD | 1,830.00 USD | 7,760.00 USD |
| `7D` | `10.42` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD |
| `1D` | `10.43` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 328,050.00 USD | 0.00 USD | 88,810.00 USD |
| `7D` | `10.44` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.45` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 329,110.00 USD | 44,950.00 USD | 216,610.00 USD |
| `7D` | `10.46` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.47` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 12,800.00 USD | 14,910.00 USD | 73,380.00 USD |
| `7D` | `10.48` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.49` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 41,140.00 USD | 38,130.00 USD | 25,320.00 USD |
| `7D` | `10.50` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.51` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 11,220.00 USD | 10,370.00 USD | 13,350.00 USD |
| `7D` | `10.52` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.53` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 71.67 USD | 18,090.00 USD | 117,550.00 USD |
| `7D` | `10.54` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD |
| `1D` | `10.55` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 65,860.00 USD | 48,330.00 USD | 52,300.00 USD |
| `7D` | `10.56` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD |
| `1D` | `10.57` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 39,360.00 USD | 21,900.00 USD | 5,470.00 USD |
| `1D` | `10.59` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 18,130.00 USD | 18,010.00 USD | 15,230.00 USD |
| `1D` | `10.61` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 0.00 USD | 3,670.00 USD | 15,520.00 USD |
| `7D` | `10.62` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 8,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.63` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 11,820.00 USD | 1,170.00 USD | 102,690.00 USD |
| `7D` | `10.64` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 11,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.65` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 30,790.00 USD | 4,060.00 USD | 23,950.00 USD |
| `7D` | `10.66` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 9,470.00 USD | 0.00 USD | 57.50 USD |
| `1D` | `10.67` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 29,160.00 USD | 9,040.00 USD | 0.39 USD |
| `7D` | `10.68` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 2,430.00 USD | 253.63 USD |
| `1D` | `10.69` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 12,670.00 USD | 6,950.00 USD | 36,190.00 USD |
| `7D` | `10.70` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.71` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 0.00 USD | 51,150.00 USD | 93,670.00 USD |
| `7D` | `10.72` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.73` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 28,630.00 USD | 52,680.00 USD | 3,600.00 USD |
| `7D` | `10.74` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 877.75 USD | 100,050.00 USD |
| `1D` | `10.75` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 89,590.00 USD | 8,370.00 USD | 72.16 USD |
| `7D` | `10.76` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 16,310.00 USD | 109,140.00 USD | 364.26 USD |
| `1D` | `10.77` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 22,390.00 USD | 62,040.00 USD | 51,880.00 USD |
| `7D` | `10.78` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 535,020.00 USD | 32,650.00 USD | 104,040.00 USD |
| `1D` | `10.79` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 167,900.00 USD | 118,040.00 USD | 9,970.00 USD |
| `7D` | `10.80` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 23,450.00 USD | 70,260.00 USD | 429.69 USD |
| `1D` | `10.81` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 13,650.00 USD | 5,170.00 USD | 0.00 USD |
| `7D` | `10.82` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 56,610.00 USD | 206,610.00 USD |
| `1D` | `10.83` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 315,520.00 USD | 4,400.00 USD | 0.00 USD |
| `7D` | `10.84` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 193,810.00 USD | 80,420.00 USD | 196,250.00 USD |
| `1D` | `10.85` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 87,770.00 USD | 14,590.00 USD | 148,590.00 USD |
| `7D` | `10.86` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 334,140.00 USD |
| `1D` | `10.87` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 60,390.00 USD | 6,510.00 USD | 0.00 USD |
| `7D` | `10.88` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 111,430.00 USD | 39,120.00 USD | 347,180.00 USD |
| `1D` | `10.89` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 2,230.00 USD | 0.00 USD |
| `7D` | `10.90` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 221,070.00 USD |
| `1D` | `10.91` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 117,890.00 USD | 904.45 USD | 0.00 USD |
| `7D` | `10.92` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 226,910.00 USD | 0.00 USD | 111,880.00 USD |
| `1D` | `10.93` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,920.00 USD | 1,010.00 USD | 103.72 USD |
| `7D` | `10.94` | 725,060.00 USD | 0.00 USD | 725,060.00 USD | 2,480.00 USD | 0.00 USD | 380.88 USD |
| `1D` | `10.95` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,550.00 USD | 1,320.00 USD | 88,190.00 USD |
| `7D` | `10.96` | 722,200.00 USD | 0.00 USD | 722,200.00 USD | 10,430.00 USD | 0.00 USD | 50,870.00 USD |
| `1D` | `10.97` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 178.95 USD |
| `7D` | `10.98` | 660,910.00 USD | 0.00 USD | 660,910.00 USD | 17,930.00 USD | 0.00 USD | 209,750.00 USD |
| `1D` | `10.99` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 467.00 USD | 93.30 USD |
| `7D` | `11.00` | 433,230.00 USD | 0.00 USD | 433,230.00 USD | 10,830.00 USD | 2,280.00 USD | 2,070.00 USD |
| `1D` | `11.01` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 3,040.00 USD | 252.61 USD |
| `7D` | `11.02` | 418,050.00 USD | 0.00 USD | 418,050.00 USD | 7,900.00 USD | 31,180.00 USD | 143,040.00 USD |
| `1D` | `11.03` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 51,180.00 USD | 43,470.00 USD | 304,630.00 USD |
| `7D` | `11.04` | 235,930.00 USD | 0.00 USD | 235,930.00 USD | 17,850.00 USD | 40,210.00 USD | 177,880.00 USD |
| `1D` | `11.05` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 310,310.00 USD | 5,150.00 USD | 106,280.00 USD |
| `7D` | `11.05` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.06` | 483,970.00 USD | 483,970.00 USD | 0.00 USD | 351,320.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 329,150.00 USD | 46,170.00 USD | 169,910.00 USD |
| `7D` | `11.08` | 825,050.00 USD | 825,050.00 USD | 0.00 USD | 171,900.00 USD | 1,810.00 USD | 167,370.00 USD |
| `1D` | `11.09` | 829,070.00 USD | 0.00 USD | 829,070.00 USD | 105,500.00 USD | 69,450.00 USD | 302,240.00 USD |
| `7D` | `11.10` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 301,790.00 USD | 23,300.00 USD | 173,740.00 USD |
| `1D` | `11.11` | 351,890.00 USD | 0.00 USD | 351,890.00 USD | 254,740.00 USD | 53,870.00 USD | 43,270.00 USD |
| `1D` | `11.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.12` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 262,770.00 USD | 115,910.00 USD | 234,130.00 USD |
| `1D` | `11.13` | 744,030.00 USD | 744,030.00 USD | 0.00 USD | 440,100.00 USD | 99,350.00 USD | 204,580.00 USD |
| `7D` | `11.14` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 1,350.00 USD |
| `1D` | `11.15` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 198,370.00 USD | 61,430.00 USD | 50,270.00 USD |
| `7D` | `11.16` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 64,850.00 USD |
| `1D` | `11.17` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 22,450.00 USD | 53,650.00 USD | 59,000.00 USD |
| `7D` | `11.18` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 1,420.00 USD |
| `1D` | `11.19` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 72,050.00 USD | 28,650.00 USD | 40,660.00 USD |
| `7D` | `11.20` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 171,840.00 USD | 78,020.00 USD | 78,710.00 USD |
| `1D` | `11.21` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 160,950.00 USD | 59,630.00 USD | 164,150.00 USD |
| `7D` | `11.22` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 482,460.00 USD | 28,690.00 USD | 0.00 USD |
| `1D` | `11.23` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 262,260.00 USD | 37,760.00 USD | 118,480.00 USD |
| `7D` | `11.24` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 108,110.00 USD | 39,180.00 USD | 147,850.00 USD |
| `7D` | `11.26` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 520,990.00 USD | 0.00 USD | 296,480.00 USD |
| `1D` | `11.27` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 310,520.00 USD | 4,170.00 USD | 172,970.00 USD |
| `7D` | `11.28` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 245,580.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.29` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 176,550.00 USD | 119,460.00 USD | 225,830.00 USD |
| `7D` | `11.30` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 20,580.00 USD |
| `1D` | `11.31` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 123,640.00 USD | 68,560.00 USD | 66,830.00 USD |
| `7D` | `11.32` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 280,300.00 USD |
| `1D` | `11.33` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 142,190.00 USD | 33,330.00 USD | 31,760.00 USD |
| `7D` | `11.34` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD |
| `1D` | `11.35` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 296,410.00 USD | 121,810.00 USD | 84,450.00 USD |
| `7D` | `11.36` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.37` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 152,070.00 USD | 91,520.00 USD | 47,240.00 USD |
| `7D` | `11.38` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 74,750.00 USD |
| `1D` | `11.39` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 14,820.00 USD | 47,470.00 USD | 7,580.00 USD |
| `7D` | `11.40` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.41` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 96,590.00 USD | 35,740.00 USD | 140,630.00 USD |
| `7D` | `11.42` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD |
| `1D` | `11.43` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 64,580.00 USD | 56,490.00 USD | 132,810.00 USD |
| `7D` | `11.44` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 303,190.00 USD | 95,260.00 USD | 38,840.00 USD |
| `1D` | `11.45` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 77,400.00 USD | 83,200.00 USD | 25,650.00 USD |
| `7D` | `11.46` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 99,360.00 USD | 55,470.00 USD | 0.00 USD |
| `1D` | `11.47` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 56,320.00 USD | 19,720.00 USD | 23,580.00 USD |
| `7D` | `11.48` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 54,660.00 USD | 84,840.00 USD | 64,880.00 USD |
| `1D` | `11.49` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 33,390.00 USD | 27,450.00 USD | 34,750.00 USD |
| `7D` | `11.50` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 40,840.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.51` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 41,360.00 USD | 29,500.00 USD | 30,570.00 USD |
| `7D` | `11.52` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 33,270.00 USD |
| `1D` | `11.53` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 64,080.00 USD | 17,000.00 USD | 41,010.00 USD |
| `7D` | `11.54` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,340.00 USD |
| `1D` | `11.55` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 73,420.00 USD | 993.85 USD | 38,210.00 USD |
| `7D` | `11.56` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 86,650.00 USD | 793.25 USD | 0.00 USD |
| `1D` | `11.57` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 90,730.00 USD | 3,740.00 USD | 23,790.00 USD |
| `7D` | `11.58` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `11.59` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 16,690.00 USD | 7,660.00 USD | 39,860.00 USD |
| `7D` | `11.60` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 44,670.00 USD | 10,510.00 USD | 22,780.00 USD |
| `1D` | `11.61` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 118,210.00 USD | 512.95 USD | 84,960.00 USD |
| `7D` | `11.62` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.63` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 2,580.00 USD | 6,700.00 USD | 31,290.00 USD |
| `7D` | `11.64` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 186.31 USD |
| `1D` | `11.65` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 2,630.00 USD | 7,840.00 USD | 0.00 USD |
| `7D` | `11.66` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,310.00 USD |
| `1D` | `11.67` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 19,420.00 USD | 11,530.00 USD | 57,440.00 USD |
| `7D` | `11.68` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,290.00 USD |
| `1D` | `11.69` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 105,090.00 USD | 34,170.00 USD | 491.43 USD |
| `7D` | `11.70` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD |
| `1D` | `11.71` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 74,220.00 USD | 13,000.00 USD | 15,370.00 USD |
| `7D` | `11.72` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,380.00 USD |
| `1D` | `11.73` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 139,320.00 USD | 11,870.00 USD | 120,020.00 USD |
| `7D` | `11.74` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,340.00 USD |
| `1D` | `11.75` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 21,990.00 USD | 38,420.00 USD | 61,430.00 USD |
| `7D` | `11.76` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,610.00 USD |
| `1D` | `11.77` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 41,180.00 USD | 20,930.00 USD | 14,650.00 USD |
| `7D` | `11.78` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 57,000.00 USD |
| `1D` | `11.79` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 12,300.00 USD | 745.35 USD | 39,930.00 USD |
| `7D` | `11.80` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.81` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 18,080.00 USD | 17,860.00 USD |
| `7D` | `11.82` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.83` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 11,070.00 USD | 11,560.00 USD | 29,460.00 USD |
| `7D` | `11.84` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,560.00 USD |
| `1D` | `11.85` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 82,060.00 USD | 9,720.00 USD | 84,740.00 USD |
| `7D` | `11.86` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 100.22 USD |
| `1D` | `11.87` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 19,640.00 USD | 20,660.00 USD | 53,710.00 USD |
| `7D` | `11.88` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,830.00 USD |
| `1D` | `11.89` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 43,100.00 USD | 13,220.00 USD | 44,150.00 USD |
| `7D` | `11.90` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 298.16 USD |
| `1D` | `11.91` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 102,960.00 USD | 18,290.00 USD | 31,640.00 USD |
| `7D` | `11.92` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,850.00 USD |
| `1D` | `11.93` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 135,130.00 USD | 28,280.00 USD | 28,440.00 USD |
| `7D` | `11.94` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,550.00 USD |
| `1D` | `11.95` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 84,850.00 USD | 20,720.00 USD | 43,540.00 USD |
| `7D` | `11.96` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,020.00 USD |
| `1D` | `11.97` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 71,640.00 USD | 36,280.00 USD | 87,450.00 USD |
| `7D` | `11.98` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,840.00 USD |
| `1D` | `11.99` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 113,870.00 USD | 27,760.00 USD | 36,450.00 USD |
| `7D` | `12.00` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 221,970.00 USD |
| `1D` | `12.01` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 47,510.00 USD | 9,510.00 USD | 49,990.00 USD |
| `7D` | `12.02` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,420.00 USD |
| `1D` | `12.03` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 47,360.00 USD | 41,460.00 USD | 30,850.00 USD |
| `7D` | `12.04` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,730.00 USD |
| `1D` | `12.05` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 149,970.00 USD | 46,150.00 USD | 62,600.00 USD |
| `7D` | `12.06` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,770.00 USD |
| `1D` | `12.07` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 34,850.00 USD | 33,440.00 USD | 67,670.00 USD |
| `7D` | `12.08` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,470.00 USD |
| `1D` | `12.09` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 20,990.00 USD | 24,720.00 USD | 27,940.00 USD |
| `7D` | `12.10` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,130.00 USD |
| `1D` | `12.11` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 101,970.00 USD | 38,270.00 USD | 55,270.00 USD |
| `7D` | `12.12` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,520.00 USD |
| `1D` | `12.13` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 93,390.00 USD | 33,860.00 USD | 39,610.00 USD |
| `7D` | `12.14` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 147,420.00 USD | 92,520.00 USD | 119,100.00 USD |
| `1D` | `12.15` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 114,330.00 USD | 42,340.00 USD | 65,360.00 USD |
| `7D` | `12.16` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,180.00 USD |
| `1D` | `12.17` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 118,100.00 USD | 60,070.00 USD | 69,650.00 USD |
| `7D` | `12.18` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 57,680.00 USD | 54,220.00 USD | 32,140.00 USD |
| `1D` | `12.19` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 59,950.00 USD | 24,020.00 USD | 12,380.00 USD |
| `7D` | `12.20` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 91,440.00 USD |
| `1D` | `12.21` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 32,170.00 USD | 28,710.00 USD | 45,960.00 USD |
| `7D` | `12.22` | 15,910,000.00 USD | 15,910,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 106,040.00 USD |
| `1D` | `12.23` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 7,370.00 USD | 18,090.00 USD | 4,580.00 USD |
| `7D` | `12.24` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 70,650.00 USD | 54,230.00 USD | 114,730.00 USD |
| `1D` | `12.25` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 2,260.00 USD | 3,780.00 USD | 7,930.00 USD |
| `7D` | `12.26` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 192,800.00 USD | 55,780.00 USD | 50,780.00 USD |
| `1D` | `12.27` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 38,860.00 USD | 8,240.00 USD | 20,000.00 USD |
| `7D` | `12.28` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 215,790.00 USD | 64,650.00 USD | 171,450.00 USD |
| `1D` | `12.29` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 23,030.00 USD | 9,340.00 USD | 8,780.00 USD |
| `7D` | `12.30` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 97,010.00 USD |
| `1D` | `12.31` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 5,780.00 USD | 4,850.00 USD | 9,670.00 USD |
| `7D` | `12.32` | 17,340,000.00 USD | 17,340,000.00 USD | 0.00 USD | 40,210.00 USD | 38,250.00 USD | 17,950.00 USD |
| `7D` | `12.34` | 17,420,000.00 USD | 17,420,000.00 USD | 0.00 USD | 48,630.00 USD | 18,250.00 USD | 13,630.00 USD |
| `7D` | `12.36` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 36,210.00 USD | 24,190.00 USD | 17,940.00 USD |
| `7D` | `12.38` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 7,170.00 USD | 6,880.00 USD | 54,980.00 USD |
| `7D` | `12.40` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 111,350.00 USD | 41,100.00 USD | 12,780.00 USD |
| `7D` | `12.42` | 17,790,000.00 USD | 17,790,000.00 USD | 0.00 USD | 23,200.00 USD | 21,440.00 USD | 10,260.00 USD |
| `7D` | `12.44` | 17,920,000.00 USD | 17,920,000.00 USD | 0.00 USD | 81,360.00 USD | 284.67 USD | 45,060.00 USD |
| `7D` | `12.46` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 39,540.00 USD | 25,610.00 USD | 86,300.00 USD |
| `7D` | `12.48` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 64,380.00 USD |
| `7D` | `12.50` | 18,420,000.00 USD | 18,420,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,810.00 USD |
| `7D` | `12.52` | 18,750,000.00 USD | 18,750,000.00 USD | 0.00 USD | 163,610.00 USD | 39,290.00 USD | 125,070.00 USD |
| `7D` | `12.54` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,210.00 USD |
| `7D` | `12.56` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 86,680.00 USD | 26,470.00 USD | 27,220.00 USD |
| `7D` | `12.58` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 41,760.00 USD | 34,570.00 USD | 41,230.00 USD |
| `7D` | `12.60` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD |
| `7D` | `12.62` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,050.00 USD |
| `7D` | `12.64` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 63,450.00 USD | 42,320.00 USD | 26,040.00 USD |
| `7D` | `12.66` | 19,660,000.00 USD | 19,660,000.00 USD | 0.00 USD | 22,530.00 USD | 5,030.00 USD | 8,760.00 USD |
| `7D` | `12.68` | 19,720,000.00 USD | 19,720,000.00 USD | 0.00 USD | 9,270.00 USD | 18,330.00 USD | 36,250.00 USD |
| `7D` | `12.70` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 2,010.00 USD | 617.78 USD | 52,580.00 USD |
| `7D` | `12.72` | 19,890,000.00 USD | 19,890,000.00 USD | 0.00 USD | 47,740.00 USD | 22,750.00 USD | 40,750.00 USD |
| `7D` | `12.74` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 38,570.00 USD | 26,370.00 USD | 40,400.00 USD |
| `7D` | `12.76` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 13,750.00 USD | 14,350.00 USD | 29,500.00 USD |
| `7D` | `12.78` | 20,230,000.00 USD | 20,230,000.00 USD | 0.00 USD | 109,130.00 USD | 16,110.00 USD | 52,110.00 USD |
| `7D` | `12.80` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 13,700.00 USD | 14,000.00 USD | 60,940.00 USD |
| `7D` | `12.82` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,020.00 USD |
| `7D` | `12.84` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 31,320.00 USD | 15,990.00 USD | 7,680.00 USD |
| `7D` | `12.86` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,350.00 USD |
| `7D` | `12.88` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 23,610.00 USD | 4,610.00 USD | 12,920.00 USD |
| `7D` | `12.90` | 20,580,000.00 USD | 20,580,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,170.00 USD |
| `7D` | `12.92` | 20,670,000.00 USD | 20,670,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 26,770.00 USD |
| `7D` | `12.94` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 199.13 USD |
| `7D` | `12.96` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 13,150.00 USD | 11,970.00 USD | 24,770.00 USD |
| `7D` | `12.98` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,870.00 USD |
| `7D` | `13.00` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 51,470.00 USD | 9,560.00 USD | 20,510.00 USD |
| `7D` | `13.02` | 20,880,000.00 USD | 20,880,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `7D` | `13.04` | 20,880,000.00 USD | 20,880,000.00 USD | 0.00 USD | 303.50 USD | 335.85 USD | 0.00 USD |
| `7D` | `13.06` | 20,910,000.00 USD | 20,910,000.00 USD | 0.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD |
| `7D` | `13.08` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `519.74M` | Total OI Tokens: `46,782,942.3 LINK`
  * 1h OI Change: `+0.52%` | 4h OI Change: `-1.35%` | 24h OI Change: `-6.51%`
  * Exchange Breakdown: Binance=`102.57M` | Bybit=`70.28M` | OKX=`26.99M` | Hyperliquid=`56.12M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.69K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0073%` | **USDT OKX** | `-0.0065%` |
| **USDT Bybit** | `-0.0166%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0072%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0080%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `43.84%` | `56.16%` | `0.78` | 11,860,000.00 USD |
| `15M` | `Binance` | `36.21%` | `63.79%` | `0.57` | 5,470,000.00 USD |
| `15M` | `OKX` | `42.59%` | `57.41%` | `0.74` | 1,450,000.00 USD |
| `15M` | `Bybit` | `57.79%` | `42.21%` | `1.37` | 2,800,000.00 USD |
| `15M` | `KuCoin` | `43.81%` | `56.19%` | `0.78` | 201,700.00 USD |
| `15M` | `Gate` | `54.09%` | `45.91%` | `1.18` | 237,790.00 USD |
| `15M` | `Bitget` | `43.43%` | `56.57%` | `0.77` | 670,550.00 USD |
| `15M` | `BingX` | `29.51%` | `70.49%` | `0.42` | 101,710.00 USD |
| `15M` | `MEXC` | `59.7%` | `40.3%` | `1.48` | 42,830.00 USD |
| `15M` | `Bitunix` | `51.01%` | `48.99%` | `1.04` | 148,240.00 USD |
| `15M` | `Hyperliquid` | `52.27%` | `47.73%` | `1.10` | 305,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 24,080.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `30.08%` | `69.92%` | `0.43` | 250,920.00 USD |
| `15M` | `HTX` | `32.22%` | `67.78%` | `0.48` | 36,220.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `23.9%` | `76.1%` | `0.31` | 24,840.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `84.63%` | `15.37%` | `5.51` | 92,110.00 USD |
| `15M` | `Whale Positions` | `36.21%` | `63.79%` | `0.57` | 5,470,000.00 USD |
| `15M` | `Global Accounts` | `43.84%` | `56.16%` | `0.78` | 11,860,000.00 USD |
| `1H` | `LINK` | `47.85%` | `52.15%` | `0.92` | 30,970,000.00 USD |
| `1H` | `Binance` | `46.9%` | `53.1%` | `0.88` | 14,090,000.00 USD |
| `1H` | `OKX` | `43.11%` | `56.89%` | `0.76` | 4,910,000.00 USD |
| `1H` | `Bybit` | `54.82%` | `45.18%` | `1.21` | 5,420,000.00 USD |
| `1H` | `KuCoin` | `49.67%` | `50.33%` | `0.99` | 748,740.00 USD |
| `1H` | `Gate` | `51.23%` | `48.77%` | `1.05` | 991,370.00 USD |
| `1H` | `Bitget` | `49.41%` | `50.59%` | `0.98` | 1,410,000.00 USD |
| `1H` | `BingX` | `46.41%` | `53.59%` | `0.87` | 225,530.00 USD |
| `1H` | `MEXC` | `54.01%` | `45.99%` | `1.17` | 434,310.00 USD |
| `1H` | `Bitunix` | `49.73%` | `50.27%` | `0.99` | 452,720.00 USD |
| `1H` | `Hyperliquid` | `37.06%` | `62.94%` | `0.59` | 1,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.82%` | `49.18%` | `1.03` | 370,140.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `47.31%` | `52.69%` | `0.90` | 410,250.00 USD |
| `1H` | `HTX` | `45.9%` | `54.1%` | `0.85` | 127,060.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `26.42%` | `73.58%` | `0.36` | 30,060.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.93%` | `39.07%` | `1.56` | 151,160.00 USD |
| `1H` | `Whale Positions` | `46.9%` | `53.1%` | `0.88` | 14,090,000.00 USD |
| `1H` | `Global Accounts` | `47.85%` | `52.15%` | `0.92` | 30,970,000.00 USD |
| `4H` | `LINK` | `50.84%` | `49.16%` | `1.03` | 148,380,000.00 USD |
| `4H` | `Binance` | `52.19%` | `47.81%` | `1.09` | 55,610,000.00 USD |
| `4H` | `OKX` | `48.52%` | `51.48%` | `0.94` | 16,320,000.00 USD |
| `4H` | `Bybit` | `46.25%` | `53.75%` | `0.86` | 16,050,000.00 USD |
| `4H` | `KuCoin` | `48.02%` | `51.98%` | `0.92` | 979,910.00 USD |
| `4H` | `Gate` | `44.59%` | `55.41%` | `0.80` | 2,650,000.00 USD |
| `4H` | `Bitget` | `58%` | `42%` | `1.38` | 6,120,000.00 USD |
| `4H` | `BingX` | `32.63%` | `67.37%` | `0.48` | 4,120,000.00 USD |
| `4H` | `MEXC` | `51.02%` | `48.98%` | `1.04` | 33,030,000.00 USD |
| `4H` | `Bitunix` | `46.48%` | `53.52%` | `0.87` | 4,190,000.00 USD |
| `4H` | `Hyperliquid` | `63.16%` | `36.84%` | `1.71` | 4,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 2,360,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `70.15%` | `29.85%` | `2.35` | 682,440.00 USD |
| `4H` | `HTX` | `56.46%` | `43.54%` | `1.30` | 88,120.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `81.76%` | `18.24%` | `4.48` | 1,120,000.00 USD |
| `4H` | `Aster` | `55.27%` | `44.73%` | `1.24` | 535,610.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.07%` | `50.93%` | `0.96` | 213,030.00 USD |
| `4H` | `Whale Positions` | `52.19%` | `47.81%` | `1.09` | 55,610,000.00 USD |
| `4H` | `Global Accounts` | `50.84%` | `49.16%` | `1.03` | 148,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `10.77` | `10.75` | `10.77` | `10.78` | `10.71` | 1,791,807.07 USD | 1,021,807.03 USD | 770,000.04 USD | 251,806.99 USD | `+14.05%` | `17B / 3S` |
| `5:00 UTC` | `10.80` | `10.78` | `10.80` | `10.81` | `10.74` | 1,669,099.58 USD | 861,868.55 USD | 807,231.03 USD | 54,637.51 USD | `+3.27%` | `11B / 7S` |
| `0:00 UTC` | `10.91` | `10.88` | `10.91` | `10.95` | `10.78` | 3,369,524.30 USD | 1,989,204.80 USD | 1,380,319.50 USD | 608,885.30 USD | `+18.07%` | `47B / 26S` |
| `5:00 UTC` | `10.94` | `10.95` | `10.94` | `10.98` | `10.93` | 1,915,931.41 USD | 933,547.46 USD | 982,383.95 USD | -48,836.49 USD | `-2.55%` | `2B / 6S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `10.99` | `10.90` | 2,589,400.57 USD | 1,319,072.00 USD | 1,270,328.57 USD | 48,743.44 USD | `+1.88%` | `17B / 14S` |
| `5:00 UTC` | `10.99` | `10.99` | `10.99` | `11.02` | `10.96` | 1,907,525.28 USD | 901,785.44 USD | 1,005,739.84 USD | -103,954.39 USD | `-5.45%` | `12B / 13S` |
| `0:00 UTC` | `10.99` | `11.00` | `10.99` | `11.02` | `10.96` | 4,049,528.45 USD | 2,107,266.70 USD | 1,942,261.75 USD | 165,004.95 USD | `+4.07%` | `6B / 12S` |
| `5:00 UTC` | `11.08` | `11.06` | `11.08` | `11.09` | `11.01` | 2,811,297.51 USD | 1,507,938.86 USD | 1,303,358.65 USD | 204,580.21 USD | `+7.28%` | `16B / 8S` |
| `0:00 UTC` | `11.09` | `11.11` | `11.09` | `11.16` | `11.05` | 2,051,224.58 USD | 1,043,229.65 USD | 1,007,994.93 USD | 35,234.71 USD | `+1.72%` | `20B / 16S` |
| `5:00 UTC` | `11.12` | `11.12` | `11.12` | `11.13` | `11.11` | 462,611.92 USD | 250,051.97 USD | 212,559.95 USD | 37,492.02 USD | `+8.10%` | `4B / 2S` |

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
| `5m` | -104,700.00 USD | 304,060.00 USD | **`ACCUMULATION`** |
| `15m` | -299,420.00 USD | 205,780.00 USD | **`DISTRIBUTION`** |
| `30m` | -273,790.00 USD | 548,950.00 USD | **`ACCUMULATION`** |
| `1h` | -842,220.00 USD | -48,410.00 USD | **`DISTRIBUTION`** |
| `2h` | -667,860.00 USD | 205,790.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,010,000.00 USD | 1,920,000.00 USD | **`ACCUMULATION`** |
| `6h` | -3,680,000.00 USD | 218,290.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,830,000.00 USD | -21,200,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,190,000.00 USD | -21,760,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,030,000.00 USD | -21,660,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,720,000.00 USD | -45,090,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,220,000.00 USD | -198,510,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-104.70K` | 15m=`-299.42K` | 1h=`-842.22K` | 24h=`-11.03M`
* Futures Capital Netflows: 5m=`+304.06K` | 15m=`+205.78K` | 1h=`-48.41K` | 24h=`-21.66M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `10.09` (Risk Distance: `0.2572` pts)
  * +2.5R Take Profit: `10.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.16` (Risk Distance: `0.2572` pts)
  * +2.5R Take Profit: `10.26`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.19`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
