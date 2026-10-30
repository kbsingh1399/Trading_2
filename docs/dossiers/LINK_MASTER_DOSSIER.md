# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 16:51:57 IST` (`2026-10-30 11:21:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.04` | **Live Ask Quote**: `11.12` | **Mid Price**: `11.08`
- **Spread Points**: `85.00` | **Spread BPS**: `76.71 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.77` | VWAP Z-Score: `+1.16` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0801` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.84` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.56` | Lower -3.00σ Band: `9.98`
  * Upper +2.51σ Band: `11.43` | Lower -2.51σ Band: `10.11`
  * Upper +2.01σ Band: `11.30` | Lower -2.01σ Band: `10.24`
  * Upper +2.00σ Band: `11.30` | Lower -2.00σ Band: `10.25`
  * Upper +1.28σ Band: `11.11` | Lower -1.28σ Band: `10.44`
  * Upper +1.00σ Band: `11.04` | Lower -1.00σ Band: `10.51`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.99` | EMA-20=`10.97` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.98` (Slope: `+0.0000`) | EMA-100=`11.10`
  * Institutional Anchors: EMA-144=`11.18` | EMA-200=`11.25` (Slope: `-0.3141`) | EMA-233=`11.27`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-0.33%`)
  * Point of Control (POC) = `10.96` (Distance: `+1.12%`)
  * Value Area Low (VAL) = `10.57` (Distance: `+4.90%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.79` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.89`
  * New York Session (13:00-21:00 UTC): High=`11.10` | Low=`10.93`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.04` - `11.12`
  * Optimal Trade Entry (OTE 0.705): `11.10`
  * Structural Invalidation Anchor (0.786): `11.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.14` | `11.15` | `11.10` | `11.11` | `75,267` | 837,254.68 USD | 59.55 USD | `+0.01%` | -11,920,231.35 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.11` | `11.12` | `11.09` | `11.10` | `35,208` | 390,916.51 USD | -53,191.51 USD | `-13.61%` | -11,973,422.86 USD | `-0.82` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `11.10` | `11.10` | `11.09` | `11.10` | `11,557` | 128,252.23 USD | 21,617.50 USD | `+16.86%` | -11,951,805.36 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.02` | `11.10` | `11.01` | `11.08` | `332,021` | 3,673,451.57 USD | 555,106.73 USD | `+15.11%` | -12,058,821.22 USD | `+2.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.08` | `11.14` | `11.05` | `11.14` | `97,425` | 1,081,659.44 USD | 138,530.32 USD | `+12.81%` | -11,920,290.90 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `11.14` | `11.15` | `11.09` | `11.10` | `122,032` | 1,356,423.42 USD | -31,514.46 USD | `-2.32%` | -11,951,805.36 USD | `-0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.01` | `11.05` | `10.95` | `11.04` | `483,549` | 5,317,760.14 USD | -566,832.14 USD | `-10.66%` | -12,789,634.39 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.14` | `10.98` | `11.14` | `612,753` | 6,774,517.77 USD | 614,711.14 USD | `+9.07%` | -12,174,923.26 USD | `+0.59` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `11.14` | `11.15` | `11.09` | `11.10` | `122,032` | 1,356,423.42 USD | -31,514.46 USD | `-2.32%` | -12,206,437.72 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.15` | `10.95` | `11.10` | `1,765,166` | 19,485,929.60 USD | -331,332.43 USD | `-1.70%` | -12,206,437.72 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.15` | `10.95` | `11.10` | `1,765,166` | 19,485,929.60 USD | -331,332.43 USD | `-1.70%` | -12,206,437.72 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`11.08`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `421` | `0xecb6...2b00` | `SHORT` | 5,265,570.08 USD | `473,735,500.00` | `10.66` | `11.11` | `79.35` | -216,188.09 USD | `-4.11%` | `10X Cross` |
| `502` | `0x73ce...8ce9` | `LONG` | 4,445,596.92 USD | `400,011,600.00` | `12.05` | `11.11` | `7.82` | -374,156.79 USD | `-8.42%` | `5X Cross` |
| `844` | `0xb83d...6e36` | `SHORT` | 2,689,652.62 USD | `242,013,000.00` | `12.93` | `11.11` | `429.77` | 440,241.57 USD | `+16.37%` | `3X Cross` |
| `881` | `0x458d...ab3b` | `LONG` | 2,525,982.50 USD | `227,156,700.00` | `13.13` | `11.11` | `9.34` | -456,247.89 USD | `-18.06%` | `3X Isolated` |
| `968` | `0xdd53...2b13` | `SHORT` | 2,295,179.43 USD | `206,475,300.00` | `11.92` | `11.11` | `295.21` | 166,043.49 USD | `+7.23%` | `3X Cross` |
| `993` | `0x3dc9...54b0` | `SHORT` | 2,219,200.00 USD | `200,000,000.00` | `7.56` | `11.11` | `93.56` | -708,041.58 USD | `-31.91%` | `10X Cross` |
| `1003` | `0x45d2...4029` | `SHORT` | 2,172,591.50 USD | `195,500,000.00` | `11.54` | `11.11` | `216.95` | 83,891.93 USD | `+3.86%` | `10X Cross` |
| `1176` | `0x6540...f7b7` | `LONG` | 1,860,865.09 USD | `167,404,200.00` | `12.40` | `11.11` | `6.70` | -214,941.02 USD | `-11.55%` | `5X Isolated` |
| `1256` | `0xeadc...9d55` | `LONG` | 1,752,584.44 USD | `157,691,600.00` | `9.43` | `11.11` | `0.000000` | 265,929.54 USD | `+15.17%` | `10X Cross` |
| `1470` | `0x5b5d...c060` | `SHORT` | 1,464,421.13 USD | `131,775,500.00` | `13.61` | `11.11` | `1087.50` | 328,836.84 USD | `+22.46%` | `3X Cross` |
| `1651` | `0xf6f3...47f8` | `SHORT` | 1,278,498.43 USD | `115,024,600.00` | `11.42` | `11.11` | `18.20` | 34,831.76 USD | `+2.72%` | `5X Cross` |
| `1836` | `0xfe7e...11b4` | `LONG` | 1,124,193.33 USD | `101,142,000.00` | `14.47` | `11.11` | `5.33` | -338,919.82 USD | `-30.15%` | `5X Isolated` |
| `1875` | `0x8af7...fa05` | `SHORT` | 1,096,717.90 USD | `98,661,200.00` | `14.08` | `11.11` | `201.28` | 292,464.64 USD | `+26.67%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.71` | 6,883.73 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.88K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 8,500.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.50K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 10,014.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 10.01K USD at 11.6670 USD [API] | `2026-10-29 19:26:32` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 6,067.82 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.07K USD at 11.7230 USD [API] | `2026-10-29 19:32:49` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 5,463.85 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.7250 USD [API] | `2026-10-29 19:36:14` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 5,465.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.5260 USD [API] | `2026-10-29 20:13:31` |
| `ANNOUNCEMENT` | `INFO` | `11.57` | 9,266.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 9.27K USD at 11.5660 USD [API] | `2026-10-29 20:20:22` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 8,615.28 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 8.62K USD at 11.5270 USD [API] | `2026-10-29 20:22:55` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 7,507.92 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.51K USD at 11.5400 USD [API] | `2026-10-29 20:31:15` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 16,712.86 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 16.71K USD at 11.5540 USD [API] | `2026-09-10 12:47:06` |
| `ANNOUNCEMENT` | `INFO` | `11.35` | 6,261.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.26K USD at 11.3500 USD [API] | `2026-10-29 20:38:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+1.46%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.85%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.45%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.86%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.45%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.86%`)
  * 7D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.36%`) | Long MP=`10.30` (Vol: 866,700.00 USD, Dist: `--6.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 45,640.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,880.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 3,740.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,200.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,180.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 1,490.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,580.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 770.49 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 9,760.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 2,780.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 357.49 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 299.15 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 17,500.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,770.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 45,660.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 9,000.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 411.94 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 7,310.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 13,650.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 4,380.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 314,350.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 425.83 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 1,010.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 2,240.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 3,730.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 3,120.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 26,320.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 36,220.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 1,500.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 10,650.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 5,020.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 16,220.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 646.98 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 66,750.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 15,990.00 USD | 11,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 13,030.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 3,050.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,140,000.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 20,240.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 58,250.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 689,770.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 21,170.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 187,570.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 29,610.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 5,120.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 55,670.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,830.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 23,520.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,610.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 226,650.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 33,720.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 31,200.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 351,270.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,820.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,440.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 19,610.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 74,610.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 453,100.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 105,400.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 19,930.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.32` | 13,800,000.00 USD | 13,800,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 13,720,000.00 USD | 13,720,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 13,680,000.00 USD | 13,680,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 13,670,000.00 USD | 13,670,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 13,640,000.00 USD | 13,640,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 13,610,000.00 USD | 13,610,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 13,560,000.00 USD | 13,560,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 127,760.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 13,510,000.00 USD | 13,510,000.00 USD | 94,230.00 USD | 0.00 USD | 317.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 13,410,000.00 USD | 13,410,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 13,410,000.00 USD | 13,410,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 911.85 USD | 10.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 13,340,000.00 USD | 13,340,000.00 USD | 136.92 USD | 12,570.00 USD | 10.76 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 102,930.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 13,330,000.00 USD | 13,330,000.00 USD | 160.73 USD | 16,080.00 USD | 71,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 13,240,000.00 USD | 13,240,000.00 USD | 38,760.00 USD | 722.15 USD | 201.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 13,200,000.00 USD | 13,200,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 13,000,000.00 USD | 13,000,000.00 USD | 8,500.00 USD | 0.00 USD | 143.89 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 193,100.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 12,990,000.00 USD | 12,990,000.00 USD | 7,370.00 USD | 0.00 USD | 379.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 0.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 12,950,000.00 USD | 12,950,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 12,920,000.00 USD | 12,920,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 94,920.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 12,920,000.00 USD | 12,920,000.00 USD | 50,080.00 USD | 0.00 USD | 27,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 671.70 USD | 487.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 12,840,000.00 USD | 12,840,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 12,750,000.00 USD | 12,750,000.00 USD | 84,900.00 USD | 10,390.00 USD | 506.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 12,650,000.00 USD | 12,650,000.00 USD | 50,980.00 USD | 456.90 USD | 13,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 29,740.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 9,190,000.00 USD | 9,190,000.00 USD | 29,590.00 USD | 11,120.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.86` | 12,590,000.00 USD | 12,590,000.00 USD | 5,390.00 USD | 14,570.00 USD | 612.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 9,140,000.00 USD | 9,140,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 12,570,000.00 USD | 12,570,000.00 USD | 10,280.00 USD | 15,600.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 9,110,000.00 USD | 9,110,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 12,540,000.00 USD | 12,540,000.00 USD | 48,670.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 9,020,000.00 USD | 9,020,000.00 USD | 23,540.00 USD | 20,070.00 USD | 467.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 12,280.00 USD | 279.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 8,980,000.00 USD | 8,980,000.00 USD | 1,960.00 USD | 5,150.00 USD | 263.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 12,480,000.00 USD | 12,480,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 433,320.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 8,970,000.00 USD | 8,970,000.00 USD | 75,160.00 USD | 15,490.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.96` | 12,380,000.00 USD | 12,380,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 8,850,000.00 USD | 8,850,000.00 USD | 37,260.00 USD | 6,830.00 USD | 67,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 12,340,000.00 USD | 12,340,000.00 USD | 4,830.00 USD | 6,160.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,740,000.00 USD | 8,740,000.00 USD | 5,670.00 USD | 4,500.00 USD | 64,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 12,270,000.00 USD | 12,270,000.00 USD | 641.95 USD | 7,630.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,670,000.00 USD | 8,670,000.00 USD | 17,880.00 USD | 19,650.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 12,250,000.00 USD | 12,250,000.00 USD | 8,880.00 USD | 317.30 USD | 415.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,610,000.00 USD | 8,610,000.00 USD | 18,000.00 USD | 4,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 12,240,000.00 USD | 12,240,000.00 USD | 7,200.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 774,770.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,590,000.00 USD | 8,590,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.06` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 83,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 8,510,000.00 USD | 8,510,000.00 USD | 167,250.00 USD | 701.42 USD | 76,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 12,140,000.00 USD | 12,140,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 8,270,000.00 USD | 8,270,000.00 USD | 7,570.00 USD | 42,810.00 USD | 531.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 11,810,000.00 USD | 11,810,000.00 USD | 6,580.00 USD | 0.00 USD | 372.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 8,220,000.00 USD | 8,220,000.00 USD | 1,150.00 USD | 20,910.00 USD | 195.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 11,810,000.00 USD | 11,810,000.00 USD | 10,140.00 USD | 559.40 USD | 56,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 8,190,000.00 USD | 8,190,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 11,740,000.00 USD | 11,740,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 71,300.00 USD | 258,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 8,130,000.00 USD | 8,130,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.16` | 11,420,000.00 USD | 11,420,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 8,010,000.00 USD | 8,010,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 11,380,000.00 USD | 11,380,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,740,000.00 USD | 7,740,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 11,240,000.00 USD | 11,240,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 7,260,000.00 USD | 7,260,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 10,720,000.00 USD | 10,720,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 6,860,000.00 USD | 6,860,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 10,180,000.00 USD | 10,180,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 34,240.00 USD | 187,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,670,000.00 USD | 6,670,000.00 USD | 63,830.00 USD | 8,070.00 USD | 101,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 9,730,000.00 USD | 9,730,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 6,500,000.00 USD | 6,500,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 9,350,000.00 USD | 9,350,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 6,150,000.00 USD | 6,150,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 9,020,000.00 USD | 9,020,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 5,920,000.00 USD | 5,920,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 8,560,000.00 USD | 8,560,000.00 USD | 43,210.00 USD | 0.00 USD | 100,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 5,840,000.00 USD | 5,840,000.00 USD | 66,410.00 USD | 9,100.00 USD | 85,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 8,420,000.00 USD | 8,420,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 138,450.00 USD | 152,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,680,000.00 USD | 5,680,000.00 USD | 6,270.00 USD | 3,580.00 USD | 128.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 8,360,000.00 USD | 8,360,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,670,000.00 USD | 5,670,000.00 USD | 42,350.00 USD | 45,170.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 7,960,000.00 USD | 7,960,000.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,570,000.00 USD | 5,570,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 7,950,000.00 USD | 7,950,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 5,390,000.00 USD | 5,390,000.00 USD | 244,890.00 USD | 0.00 USD | 154.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 7,600,000.00 USD | 7,600,000.00 USD | 229,660.00 USD | 97,940.00 USD | 258.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 5,140,000.00 USD | 5,140,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 7,270,000.00 USD | 7,270,000.00 USD | 439,060.00 USD | 13,410.00 USD | 334,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 10,350.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,610,000.00 USD | 4,610,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 6,490,000.00 USD | 6,490,000.00 USD | 323,570.00 USD | 103,810.00 USD | 385.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 4,280,000.00 USD | 4,280,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 6,060,000.00 USD | 6,060,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 4,170,000.00 USD | 4,170,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 5,840,000.00 USD | 5,840,000.00 USD | 4,770.00 USD | 52,370.00 USD | 236.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 4,100,000.00 USD | 4,100,000.00 USD | 1,200.00 USD | 12,710.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 5,790,000.00 USD | 5,790,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 4,040,000.00 USD | 4,040,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 4,100.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,800,000.00 USD | 3,800,000.00 USD | 110,630.00 USD | 38,520.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 5,700,000.00 USD | 5,700,000.00 USD | 122,960.00 USD | 81,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,620,000.00 USD | 3,620,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 5,500,000.00 USD | 5,500,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,510,000.00 USD | 3,510,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 24,130.00 USD | 59.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 3,470,000.00 USD | 3,470,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 5,450,000.00 USD | 5,450,000.00 USD | 99,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 3,280,000.00 USD | 3,280,000.00 USD | 109,830.00 USD | 9,030.00 USD | 59,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 5,350,000.00 USD | 5,350,000.00 USD | 11,150.00 USD | 0.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 3,100,000.00 USD | 3,100,000.00 USD | 59,930.00 USD | 10,280.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 5,310,000.00 USD | 5,310,000.00 USD | 9,470.00 USD | 19,620.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,990,000.00 USD | 2,990,000.00 USD | 67,250.00 USD | 37,570.00 USD | 70,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 5,270,000.00 USD | 5,270,000.00 USD | 16,330.00 USD | 27,190.00 USD | 148.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,820,000.00 USD | 2,820,000.00 USD | 12,670.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,780,000.00 USD | 2,780,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 5,210,000.00 USD | 5,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,570,000.00 USD | 2,570,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 877.75 USD | 100,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,460,000.00 USD | 2,460,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 4,610,000.00 USD | 4,610,000.00 USD | 16,310.00 USD | 120,930.00 USD | 261.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 2,280,000.00 USD | 2,280,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 4,470,000.00 USD | 4,470,000.00 USD | 535,020.00 USD | 46,010.00 USD | 104,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,830,000.00 USD | 1,830,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 3,780,000.00 USD | 3,780,000.00 USD | 69,540.00 USD | 70,260.00 USD | 463.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,720,000.00 USD | 1,720,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 104,870.00 USD | 207,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,560,000.00 USD | 1,560,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 3,330,000.00 USD | 3,330,000.00 USD | 377,580.00 USD | 80,420.00 USD | 196,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.86` | 1,110,000.00 USD | 1,110,000.00 USD | 203,140.00 USD | 34,420.00 USD | 219,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 2,680,000.00 USD | 2,680,000.00 USD | 323,850.00 USD | 3,610.00 USD | 391,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 648,680.00 USD | 648,680.00 USD | 61,520.00 USD | 15,030.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 1,960,000.00 USD | 1,960,000.00 USD | 111,430.00 USD | 78,360.00 USD | 365,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 504,790.00 USD | 504,790.00 USD | 114,210.00 USD | 53,630.00 USD | 67,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 1,400,000.00 USD | 1,400,000.00 USD | 32,650.00 USD | 49,530.00 USD | 221,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 269,030.00 USD | 269,030.00 USD | 138,180.00 USD | 33,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 1,100,000.00 USD | 1,100,000.00 USD | 226,910.00 USD | 0.00 USD | 110,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 97,040.00 USD | 97,040.00 USD | 4,370.00 USD | 1,550.00 USD | 103.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 760,120.00 USD | 760,120.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.96` | 91,010.00 USD | 91,010.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 757,640.00 USD | 757,640.00 USD | 10,430.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 260.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 697,290.00 USD | 697,290.00 USD | 17,930.00 USD | 0.00 USD | 209,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 3,000.00 USD | 3,000.00 USD | 0.00 USD | 0.00 USD | 238.07 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 469,420.00 USD | 469,420.00 USD | 10,830.00 USD | 0.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 457,530.00 USD | 457,530.00 USD | 0.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 2,760.00 USD | 2,760.00 USD | 0.00 USD | 2,200.00 USD | 120.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 314,490.00 USD | 314,490.00 USD | 0.00 USD | 0.00 USD | 178,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.06` | 438.64 USD | 438.64 USD | 0.00 USD | 0.00 USD | 438.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 135,600.00 USD | 135,600.00 USD | 0.00 USD | 0.00 USD | 133,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 2,480.00 USD | 2,480.00 USD | 0.00 USD | 1,810.00 USD | 678.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 4,580.00 USD | 4,580.00 USD | 4,520.00 USD | 0.00 USD | 60.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.10` | 7,300.00 USD | 7,300.00 USD | 0.00 USD | 6,920.00 USD | 373.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 143,190.00 USD | 143,190.00 USD | 0.00 USD | 2,260.00 USD | 136,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.12` | 121,030.00 USD | 121,030.00 USD | 0.00 USD | 5,170.00 USD | 108,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 211,320.00 USD | 211,320.00 USD | 0.00 USD | 0.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 131,000.00 USD | 131,000.00 USD | 0.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 391,250.00 USD | 391,250.00 USD | 127,020.00 USD | 2,100.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.16` | 270,410.00 USD | 270,410.00 USD | 838.30 USD | 72,860.00 USD | 65,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 563,890.00 USD | 563,890.00 USD | 71,610.00 USD | 14,380.00 USD | 86,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 288,520.00 USD | 288,520.00 USD | 3,130.00 USD | 13,890.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 817,300.00 USD | 817,300.00 USD | 76,580.00 USD | 85,800.00 USD | 91,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 629,340.00 USD | 629,340.00 USD | 171,840.00 USD | 89,800.00 USD | 79,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,380,000.00 USD | 1,380,000.00 USD | 344,290.00 USD | 76,600.00 USD | 142,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 1,150,000.00 USD | 1,150,000.00 USD | 482,460.00 USD | 42,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 1,760,000.00 USD | 1,760,000.00 USD | 163,340.00 USD | 58,590.00 USD | 155,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 1,520,000.00 USD | 1,520,000.00 USD | 231,960.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 2,040,000.00 USD | 2,040,000.00 USD | 154,720.00 USD | 54,310.00 USD | 71,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.26` | 2,380,000.00 USD | 2,380,000.00 USD | 520,990.00 USD | 48,250.00 USD | 295,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 2,760,000.00 USD | 2,760,000.00 USD | 388,220.00 USD | 67,290.00 USD | 262,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 3,020,000.00 USD | 3,020,000.00 USD | 429,350.00 USD | 57,050.00 USD | 148,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,260,000.00 USD | 3,260,000.00 USD | 261,740.00 USD | 81,010.00 USD | 160,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 3,150,000.00 USD | 3,150,000.00 USD | 24,980.00 USD | 32,240.00 USD | 77,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 3,660,000.00 USD | 3,660,000.00 USD | 181,160.00 USD | 72,950.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 3,710,000.00 USD | 3,710,000.00 USD | 194,150.00 USD | 62,240.00 USD | 298,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,290,000.00 USD | 4,290,000.00 USD | 376,310.00 USD | 128,380.00 USD | 126,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 4,100,000.00 USD | 4,100,000.00 USD | 159,840.00 USD | 127,800.00 USD | 101,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,610,000.00 USD | 4,610,000.00 USD | 173,620.00 USD | 87,180.00 USD | 56,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.36` | 4,350,000.00 USD | 4,350,000.00 USD | 107,330.00 USD | 93,800.00 USD | 57,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 4,820,000.00 USD | 4,820,000.00 USD | 118,230.00 USD | 63,980.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 4,590,000.00 USD | 4,590,000.00 USD | 70,120.00 USD | 91,810.00 USD | 75,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 5,000,000.00 USD | 5,000,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,320,000.00 USD | 5,320,000.00 USD | 126,960.00 USD | 83,740.00 USD | 113,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 4,860,000.00 USD | 4,860,000.00 USD | 66,800.00 USD | 46,660.00 USD | 115,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,580,000.00 USD | 5,580,000.00 USD | 96,590.00 USD | 54,990.00 USD | 109,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 5,310,000.00 USD | 5,310,000.00 USD | 303,190.00 USD | 101,940.00 USD | 38,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 5,800,000.00 USD | 5,800,000.00 USD | 86,190.00 USD | 77,320.00 USD | 50,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 122,890.00 USD | 55,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 5,860,000.00 USD | 5,860,000.00 USD | 26,740.00 USD | 35,780.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 5,710,000.00 USD | 5,710,000.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,040,000.00 USD | 6,040,000.00 USD | 78,340.00 USD | 38,760.00 USD | 63,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 5,880,000.00 USD | 5,880,000.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,250,000.00 USD | 6,250,000.00 USD | 127,920.00 USD | 22,260.00 USD | 55,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 5,760.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,470,000.00 USD | 6,470,000.00 USD | 92,850.00 USD | 23,030.00 USD | 105,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 6,140,000.00 USD | 6,140,000.00 USD | 53,520.00 USD | 19,620.00 USD | 117,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 12,700.00 USD | 12,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,690,000.00 USD | 6,690,000.00 USD | 128,820.00 USD | 29,910.00 USD | 57,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 6,270,000.00 USD | 6,270,000.00 USD | 102,980.00 USD | 25,560.00 USD | 626.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,780,000.00 USD | 6,780,000.00 USD | 76,330.00 USD | 2,950.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 6,930,000.00 USD | 6,930,000.00 USD | 59,780.00 USD | 21,610.00 USD | 67,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 6,380,000.00 USD | 6,380,000.00 USD | 46,010.00 USD | 10,510.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 7,020,000.00 USD | 7,020,000.00 USD | 45,260.00 USD | 512.95 USD | 47,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 6,450,000.00 USD | 6,450,000.00 USD | 65,150.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 7,070,000.00 USD | 7,070,000.00 USD | 5,660.00 USD | 7,410.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 6,490,000.00 USD | 6,490,000.00 USD | 39,380.00 USD | 1,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 6,220.00 USD | 19,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,110,000.00 USD | 7,110,000.00 USD | 1,070.00 USD | 12,290.00 USD | 25,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,300,000.00 USD | 7,300,000.00 USD | 127,580.00 USD | 35,770.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 6,690,000.00 USD | 6,690,000.00 USD | 1,280.00 USD | 20,730.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,320,000.00 USD | 7,320,000.00 USD | 239.66 USD | 4,760.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 6,730,000.00 USD | 6,730,000.00 USD | 38,760.00 USD | 722.15 USD | 201.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,530,000.00 USD | 7,530,000.00 USD | 91,840.00 USD | 17,160.00 USD | 98,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 7,050,000.00 USD | 7,050,000.00 USD | 209,440.00 USD | 0.00 USD | 116,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,710,000.00 USD | 7,710,000.00 USD | 76,690.00 USD | 30,280.00 USD | 73,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 1,030.00 USD | 90,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,780,000.00 USD | 7,780,000.00 USD | 26,330.00 USD | 14,880.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 7,240,000.00 USD | 7,240,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 7,850,000.00 USD | 7,850,000.00 USD | 11,750.00 USD | 20,510.00 USD | 40,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 7,310,000.00 USD | 7,310,000.00 USD | 9,130.00 USD | 0.00 USD | 56,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 7,870,000.00 USD | 7,870,000.00 USD | 1,350.00 USD | 17,720.00 USD | 176.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 7,450,000.00 USD | 7,450,000.00 USD | 140,120.00 USD | 0.00 USD | 176.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 7,920,000.00 USD | 7,920,000.00 USD | 12,610.00 USD | 53.10 USD | 36,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 7,670,000.00 USD | 7,670,000.00 USD | 182,750.00 USD | 41,910.00 USD | 36.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 8,020,000.00 USD | 8,020,000.00 USD | 44,510.00 USD | 11,870.00 USD | 45,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 7,930,000.00 USD | 7,930,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 169.46 USD | 19,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,100,000.00 USD | 8,100,000.00 USD | 11,490.00 USD | 12,970.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 7,930,000.00 USD | 7,930,000.00 USD | 962.44 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,210,000.00 USD | 8,210,000.00 USD | 21,500.00 USD | 28,990.00 USD | 60,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 8,000,000.00 USD | 8,000,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,290,000.00 USD | 8,290,000.00 USD | 43,700.00 USD | 8,690.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 8,050,000.00 USD | 8,050,000.00 USD | 40,470.00 USD | 14,650.00 USD | 174.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,560,000.00 USD | 8,560,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 8,260,000.00 USD | 8,260,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,670,000.00 USD | 8,670,000.00 USD | 48,030.00 USD | 15,260.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 8,450,000.00 USD | 8,450,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 19,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,820,000.00 USD | 8,820,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 8,630,000.00 USD | 8,630,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 8,980,000.00 USD | 8,980,000.00 USD | 59,940.00 USD | 29,050.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 9,290,000.00 USD | 9,290,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,140,000.00 USD | 9,140,000.00 USD | 102,680.00 USD | 23,880.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 9,920,000.00 USD | 9,920,000.00 USD | 379,630.00 USD | 31,630.00 USD | 222,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,190,000.00 USD | 9,190,000.00 USD | 13,680.00 USD | 7,110.00 USD | 31,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 10,490,000.00 USD | 10,490,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,350,000.00 USD | 9,350,000.00 USD | 77,630.00 USD | 36,810.00 USD | 46,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 11,120,000.00 USD | 11,120,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,520,000.00 USD | 9,520,000.00 USD | 76,750.00 USD | 28,460.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 11,620,000.00 USD | 11,620,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,650,000.00 USD | 9,650,000.00 USD | 43,090.00 USD | 35,930.00 USD | 52,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 12,290,000.00 USD | 12,290,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 9,760,000.00 USD | 9,760,000.00 USD | 50,850.00 USD | 25,300.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 12,470,000.00 USD | 12,470,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 9,990,000.00 USD | 9,990,000.00 USD | 116,870.00 USD | 54,580.00 USD | 50,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 12,850,000.00 USD | 12,850,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,150,000.00 USD | 10,150,000.00 USD | 75,170.00 USD | 37,540.00 USD | 55,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 13,220,000.00 USD | 13,220,000.00 USD | 148,090.00 USD | 102,170.00 USD | 119,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,390,000.00 USD | 10,390,000.00 USD | 131,220.00 USD | 34,710.00 USD | 67,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 13,550,000.00 USD | 13,550,000.00 USD | 182,020.00 USD | 69,310.00 USD | 75,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,600,000.00 USD | 10,600,000.00 USD | 112,670.00 USD | 48,310.00 USD | 50,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 13,720,000.00 USD | 13,720,000.00 USD | 74,850.00 USD | 54,220.00 USD | 43,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,760,000.00 USD | 10,760,000.00 USD | 77,250.00 USD | 43,870.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 14,050,000.00 USD | 14,050,000.00 USD | 194,760.00 USD | 57,500.00 USD | 75,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 10,830,000.00 USD | 10,830,000.00 USD | 10,510.00 USD | 21,000.00 USD | 36,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 14,440,000.00 USD | 14,440,000.00 USD | 262,140.00 USD | 63,820.00 USD | 64,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 10,870,000.00 USD | 10,870,000.00 USD | 14,540.00 USD | 15,320.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 14,540,000.00 USD | 14,540,000.00 USD | 50,300.00 USD | 45,440.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 5,060.00 USD | 24,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 10,910,000.00 USD | 10,910,000.00 USD | 12,590.00 USD | 12,870.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 14,720,000.00 USD | 14,720,000.00 USD | 73,660.00 USD | 54,120.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 10,970,000.00 USD | 10,970,000.00 USD | 49,100.00 USD | 7,490.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 15,000,000.00 USD | 15,000,000.00 USD | 156,680.00 USD | 27,340.00 USD | 90,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 15,120,000.00 USD | 15,120,000.00 USD | 70,240.00 USD | 24,020.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 15,180,000.00 USD | 15,180,000.00 USD | 22,620.00 USD | 25,760.00 USD | 17,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 15,240,000.00 USD | 15,240,000.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 25,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 15,320,000.00 USD | 15,320,000.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 15,330,000.00 USD | 15,330,000.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 27,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,480.00 USD | 28,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 124,040.00 USD | 152,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 158,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 768.29 USD | 159,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 758.88 USD | 159,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 160,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 3,520.00 USD | 163,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 868.18 USD | 164,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 293.00 USD | 164,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 190,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 190,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 191,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 191,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 17,420.00 USD | 208,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 210,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 24,770.00 USD | 234,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 91,200.00 USD | 326,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 405,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 26,240.00 USD | 432,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 433,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 5,460.00 USD | 438,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 276,760.00 USD | 715,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 715,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 717,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 2,090,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 62,390.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 72,440.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 926.90 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 713,280.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 1,200.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 202.08 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.55` | 2,870.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.65` | 220.83 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,250,000.00 USD | 0.00 USD | 45,640.00 USD | `-79.79%` | `20,285,500.00` |
| `Live` | `Long` | `2.45` | 12,200,000.00 USD | 0.00 USD | 1,880.00 USD | `-78.00%` | `767,300.00` |
| `Live` | `Long` | `2.55` | 12,200,000.00 USD | 0.00 USD | 3,740.00 USD | `-77.10%` | `1,466,000.00` |
| `Live` | `Long` | `2.65` | 12,190,000.00 USD | 0.00 USD | 2,200.00 USD | `-76.20%` | `831,000.00` |
| `Live` | `Long` | `2.75` | 12,190,000.00 USD | 0.00 USD | 1,180.00 USD | `-75.30%` | `428,800.00` |
| `Live` | `Long` | `2.95` | 12,190,000.00 USD | 0.00 USD | 1,490.00 USD | `-73.50%` | `505,200.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 6,580.00 USD | `-72.61%` | `2,156,700.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 770.49 USD | `-71.71%` | `244,600.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 9,760.00 USD | `-69.91%` | `2,913,900.00` |
| `Live` | `Long` | `3.45` | 12,170,000.00 USD | 0.00 USD | 2,780.00 USD | `-69.01%` | `806,400.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 357.49 USD | `-68.12%` | `100,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-67.22%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,170,000.00 USD | 0.00 USD | 299.15 USD | `-65.42%` | `77,700.00` |
| `Live` | `Long` | `3.95` | 12,170,000.00 USD | 0.00 USD | 17,500.00 USD | `-64.52%` | `4,429,200.00` |
| `Live` | `Long` | `4.05` | 12,150,000.00 USD | 0.00 USD | 6,770.00 USD | `-63.62%` | `1,671,700.00` |
| `Live` | `Long` | `4.15` | 12,140,000.00 USD | 0.00 USD | 45,660.00 USD | `-62.73%` | `11,003,200.00` |
| `Live` | `Long` | `4.25` | 12,100,000.00 USD | 0.00 USD | 9,000.00 USD | `-61.83%` | `2,117,900.00` |
| `Live` | `Long` | `4.35` | 12,090,000.00 USD | 0.00 USD | 411.94 USD | `-60.93%` | `94,700.00` |
| `Live` | `Long` | `4.45` | 12,090,000.00 USD | 0.00 USD | 7,310.00 USD | `-60.03%` | `1,641,700.00` |
| `Live` | `Long` | `4.55` | 12,080,000.00 USD | 0.00 USD | 13,650.00 USD | `-59.13%` | `3,000,000.00` |
| `Live` | `Long` | `4.65` | 12,070,000.00 USD | 0.00 USD | 4,380.00 USD | `-58.24%` | `942,700.00` |
| `Live` | `Long` | `4.75` | 12,060,000.00 USD | 0.00 USD | 314,350.00 USD | `-57.34%` | `66,179,900.00` |
| `Live` | `Long` | `4.85` | 11,750,000.00 USD | 0.00 USD | 425.83 USD | `-56.44%` | `87,800.00` |
| `Live` | `Long` | `4.95` | 11,750,000.00 USD | 0.00 USD | 1,010.00 USD | `-55.54%` | `204,800.00` |
| `Live` | `Long` | `5.05` | 11,750,000.00 USD | 0.00 USD | 2,240.00 USD | `-54.64%` | `443,900.00` |
| `Live` | `Long` | `5.25` | 11,740,000.00 USD | 0.00 USD | 3,730.00 USD | `-52.85%` | `711,000.00` |
| `Live` | `Long` | `5.35` | 11,740,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.95%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,200,000.00 USD | 0.00 USD | 3,120.00 USD | `-51.05%` | `573,100.00` |
| `Live` | `Long` | `5.55` | 11,200,000.00 USD | 0.00 USD | 26,320.00 USD | `-50.15%` | `4,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 36,220.00 USD | `-49.25%` | `6,411,400.00` |
| `Live` | `Long` | `5.75` | 11,130,000.00 USD | 0.00 USD | 1,500.00 USD | `-48.36%` | `260,900.00` |
| `Live` | `Long` | `5.85` | 11,130,000.00 USD | 0.00 USD | 10,650.00 USD | `-47.46%` | `1,820,400.00` |
| `Live` | `Long` | `5.95` | 11,120,000.00 USD | 0.00 USD | 5,020.00 USD | `-46.56%` | `843,400.00` |
| `Live` | `Long` | `6.05` | 11,120,000.00 USD | 0.00 USD | 16,220.00 USD | `-45.66%` | `2,681,500.00` |
| `Live` | `Long` | `6.15` | 11,100,000.00 USD | 0.00 USD | 646.98 USD | `-44.76%` | `105,200.00` |
| `Live` | `Long` | `6.25` | 11,100,000.00 USD | 0.00 USD | 66,750.00 USD | `-43.87%` | `10,679,400.00` |
| `Live` | `Long` | `6.35` | 11,030,000.00 USD | 0.00 USD | 15,990.00 USD | `-42.97%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 11,020,000.00 USD | 0.00 USD | 13,030.00 USD | `-42.07%` | `2,019,900.00` |
| `Live` | `Long` | `6.55` | 11,000,000.00 USD | 0.00 USD | 3,050.00 USD | `-41.17%` | `465,300.00` |
| `Live` | `Long` | `6.65` | 11,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-40.27%` | `171,908,200.00` |
| `Live` | `Long` | `6.75` | 9,860,000.00 USD | 0.00 USD | 20,240.00 USD | `-39.37%` | `2,997,900.00` |
| `Live` | `Long` | `6.85` | 9,840,000.00 USD | 0.00 USD | 5,060.00 USD | `-38.48%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,830,000.00 USD | 0.00 USD | 58,250.00 USD | `-37.58%` | `8,380,600.00` |
| `Live` | `Long` | `7.05` | 9,770,000.00 USD | 0.00 USD | 689,770.00 USD | `-36.68%` | `97,839,700.00` |
| `Live` | `Long` | `7.15` | 9,080,000.00 USD | 0.00 USD | 21,170.00 USD | `-35.78%` | `2,960,800.00` |
| `Live` | `Long` | `7.25` | 9,060,000.00 USD | 0.00 USD | 187,570.00 USD | `-34.88%` | `25,871,900.00` |
| `Live` | `Long` | `7.35` | 8,870,000.00 USD | 0.00 USD | 29,610.00 USD | `-33.99%` | `4,028,300.00` |
| `Live` | `Long` | `7.45` | 8,850,000.00 USD | 0.00 USD | 5,120.00 USD | `-33.09%` | `686,600.00` |
| `Live` | `Long` | `7.55` | 8,840,000.00 USD | 0.00 USD | 55,670.00 USD | `-32.19%` | `7,373,200.00` |
| `Live` | `Long` | `7.65` | 8,780,000.00 USD | 0.00 USD | 1,830.00 USD | `-31.29%` | `239,400.00` |
| `Live` | `Long` | `7.75` | 8,780,000.00 USD | 0.00 USD | 23,520.00 USD | `-30.39%` | `3,034,800.00` |
| `Live` | `Long` | `7.85` | 8,760,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-29.50%` | `401,506,400.00` |
| `Live` | `Long` | `7.95` | 5,610,000.00 USD | 0.00 USD | 15,610.00 USD | `-28.60%` | `1,963,900.00` |
| `Live` | `Long` | `8.05` | 5,590,000.00 USD | 0.00 USD | 226,650.00 USD | `-27.70%` | `28,155,100.00` |
| `Live` | `Long` | `8.15` | 5,360,000.00 USD | 0.00 USD | 33,720.00 USD | `-26.80%` | `4,138,000.00` |
| `Live` | `Long` | `8.25` | 5,330,000.00 USD | 0.00 USD | 31,200.00 USD | `-25.90%` | `3,781,500.00` |
| `Live` | `Long` | `8.35` | 5,300,000.00 USD | 0.00 USD | 6,370.00 USD | `-25.00%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,290,000.00 USD | 0.00 USD | 351,270.00 USD | `-24.11%` | `41,570,800.00` |
| `Live` | `Long` | `8.55` | 4,940,000.00 USD | 0.00 USD | 15,820.00 USD | `-23.21%` | `1,849,800.00` |
| `Live` | `Long` | `8.65` | 4,930,000.00 USD | 0.00 USD | 15,440.00 USD | `-22.31%` | `1,784,900.00` |
| `Live` | `Long` | `8.75` | 4,910,000.00 USD | 0.00 USD | 19,610.00 USD | `-21.41%` | `2,241,100.00` |
| `Live` | `Long` | `8.85` | 4,890,000.00 USD | 0.00 USD | 74,610.00 USD | `-20.51%` | `8,430,900.00` |
| `Live` | `Long` | `8.95` | 4,820,000.00 USD | 0.00 USD | 453,100.00 USD | `-19.62%` | `50,626,000.00` |
| `Live` | `Long` | `9.05` | 4,360,000.00 USD | 0.00 USD | 105,400.00 USD | `-18.72%` | `11,646,400.00` |
| `Live` | `Long` | `9.15` | 4,260,000.00 USD | 0.00 USD | 76,340.00 USD | `-17.82%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,180,000.00 USD | 0.00 USD | 19,930.00 USD | `-16.92%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,160,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-16.02%` | `229,624,700.00` |
| `Live` | `Long` | `9.45` | 2,010,000.00 USD | 0.00 USD | 127,760.00 USD | `-15.12%` | `13,519,700.00` |
| `Live` | `Long` | `9.55` | 1,890,000.00 USD | 0.00 USD | 102,930.00 USD | `-14.23%` | `10,778,200.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 193,100.00 USD | `-13.33%` | `20,010,500.00` |
| `Live` | `Long` | `9.75` | 1,590,000.00 USD | 0.00 USD | 94,920.00 USD | `-12.43%` | `9,735,600.00` |
| `Live` | `Long` | `9.85` | 1,500,000.00 USD | 0.00 USD | 29,740.00 USD | `-11.53%` | `3,019,300.00` |
| `Live` | `Long` | `9.95` | 1,470,000.00 USD | 0.00 USD | 433,320.00 USD | `-10.63%` | `43,549,800.00` |
| `Live` | `Long` | `10.05` | 1,030,000.00 USD | 0.00 USD | 774,770.00 USD | `-9.74%` | `77,091,800.00` |
| `Live` | `Long` | `10.15` | 258,440.00 USD | 0.00 USD | 71,300.00 USD | `-8.84%` | `7,024,300.00` |
| `Live` | `Long` | `10.25` | 187,140.00 USD | 0.00 USD | 34,240.00 USD | `-7.94%` | `3,340,300.00` |
| `Live` | `Long` | `10.35` | 152,900.00 USD | 0.00 USD | 138,450.00 USD | `-7.04%` | `13,377,100.00` |
| `Live` | `Long` | `10.45` | 14,450.00 USD | 0.00 USD | 10,350.00 USD | `-6.14%` | `990,700.00` |
| `Live` | `Long` | `10.55` | 4,100.00 USD | 0.00 USD | 4,100.00 USD | `-5.25%` | `388,300.00` |
| `Live` | `Short` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | `+2.84%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 12,950.00 USD | 12,700.00 USD | 0.00 USD | `+3.74%` | `1,099,500.00` |
| `Live` | `Short` | `11.65` | 19,170.00 USD | 6,220.00 USD | 0.00 USD | `+4.63%` | `534,000.00` |
| `Live` | `Short` | `11.85` | 19,340.00 USD | 169.46 USD | 0.00 USD | `+6.43%` | `14,300.00` |
| `Live` | `Short` | `11.95` | 19,620.00 USD | 283.21 USD | 0.00 USD | `+7.33%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 24,680.00 USD | 5,060.00 USD | 0.00 USD | `+10.02%` | `413,200.00` |
| `Live` | `Short` | `12.35` | 25,420.00 USD | 736.06 USD | 0.00 USD | `+10.92%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 27,400.00 USD | 1,980.00 USD | 0.00 USD | `+11.82%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 28,880.00 USD | 1,480.00 USD | 0.00 USD | `+12.72%` | `117,900.00` |
| `Live` | `Short` | `12.65` | 152,920.00 USD | 124,040.00 USD | 0.00 USD | `+13.62%` | `9,805,900.00` |
| `Live` | `Short` | `13.45` | 158,350.00 USD | 5,430.00 USD | 0.00 USD | `+20.80%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 159,120.00 USD | 768.29 USD | 0.00 USD | `+21.70%` | `56,700.00` |
| `Live` | `Short` | `13.95` | 159,880.00 USD | 758.88 USD | 0.00 USD | `+25.29%` | `54,400.00` |
| `Live` | `Short` | `14.15` | 160,230.00 USD | 349.51 USD | 0.00 USD | `+27.09%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 163,750.00 USD | 3,520.00 USD | 0.00 USD | `+27.99%` | `246,800.00` |
| `Live` | `Short` | `14.35` | 164,610.00 USD | 868.18 USD | 0.00 USD | `+28.88%` | `60,500.00` |
| `Live` | `Short` | `14.65` | 164,910.00 USD | 293.00 USD | 0.00 USD | `+31.58%` | `20,000.00` |
| `Live` | `Short` | `14.95` | 190,240.00 USD | 25,330.00 USD | 0.00 USD | `+34.27%` | `1,694,600.00` |
| `Live` | `Short` | `15.55` | 190,820.00 USD | 578.46 USD | 0.00 USD | `+39.66%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 191,090.00 USD | 271.04 USD | 0.00 USD | `+42.36%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 191,230.00 USD | 138.76 USD | 0.00 USD | `+43.25%` | `8,700.00` |
| `Live` | `Short` | `16.25` | 208,650.00 USD | 17,420.00 USD | 0.00 USD | `+45.95%` | `1,072,000.00` |
| `Live` | `Short` | `16.35` | 210,040.00 USD | 1,390.00 USD | 0.00 USD | `+46.85%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 234,810.00 USD | 24,770.00 USD | 0.00 USD | `+48.64%` | `1,496,700.00` |
| `Live` | `Short` | `16.75` | 326,020.00 USD | 91,200.00 USD | 0.00 USD | `+50.44%` | `5,445,000.00` |
| `Live` | `Short` | `16.95` | 405,790.00 USD | 79,770.00 USD | 0.00 USD | `+52.24%` | `4,706,300.00` |
| `Live` | `Short` | `17.05` | 432,030.00 USD | 26,240.00 USD | 0.00 USD | `+53.13%` | `1,539,000.00` |
| `Live` | `Short` | `17.15` | 433,400.00 USD | 1,370.00 USD | 0.00 USD | `+54.03%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 438,860.00 USD | 5,460.00 USD | 0.00 USD | `+55.83%` | `314,800.00` |
| `Live` | `Short` | `17.85` | 715,620.00 USD | 276,760.00 USD | 0.00 USD | `+60.32%` | `15,505,000.00` |
| `Live` | `Short` | `17.95` | 715,970.00 USD | 351.82 USD | 0.00 USD | `+61.22%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 717,950.00 USD | 1,970.00 USD | 0.00 USD | `+62.12%` | `109,300.00` |
| `Live` | `Short` | `18.15` | 2,810,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+63.01%` | `115,031,200.00` |
| `Live` | `Short` | `18.35` | 2,870,000.00 USD | 62,390.00 USD | 0.00 USD | `+64.81%` | `3,400,000.00` |
| `Live` | `Short` | `18.45` | 2,870,000.00 USD | 3,890.00 USD | 0.00 USD | `+65.71%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 2,940,000.00 USD | 72,440.00 USD | 0.00 USD | `+66.61%` | `3,905,000.00` |
| `Live` | `Short` | `18.65` | 2,950,000.00 USD | 926.90 USD | 0.00 USD | `+67.50%` | `49,700.00` |
| `Live` | `Short` | `18.85` | 3,660,000.00 USD | 713,280.00 USD | 0.00 USD | `+69.30%` | `37,839,800.00` |
| `Live` | `Short` | `19.55` | 3,660,000.00 USD | 316.71 USD | 0.00 USD | `+75.59%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,700,000.00 USD | 38,790.00 USD | 0.00 USD | `+76.49%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,700,000.00 USD | 359.45 USD | 0.00 USD | `+77.38%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,700,000.00 USD | 1,200.00 USD | 0.00 USD | `+79.18%` | `59,900.00` |
| `Live` | `Short` | `20.15` | 3,700,000.00 USD | 1,260.00 USD | 0.00 USD | `+80.98%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,700,000.00 USD | 1,770.00 USD | 0.00 USD | `+83.67%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,710,000.00 USD | 7,250.00 USD | 0.00 USD | `+84.57%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,710,000.00 USD | 114.68 USD | 0.00 USD | `+87.26%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,710,000.00 USD | 202.08 USD | 0.00 USD | `+89.06%` | `9,600.00` |
| `Live` | `Short` | `21.55` | 3,710,000.00 USD | 2,870.00 USD | 0.00 USD | `+93.55%` | `133,300.00` |
| `Live` | `Short` | `21.65` | 3,710,000.00 USD | 220.83 USD | 0.00 USD | `+94.45%` | `10,200.00` |
| `Live` | `Short` | `21.75` | 3,780,000.00 USD | 65,060.00 USD | 0.00 USD | `+95.35%` | `2,991,400.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 433,540.00 USD | 0.00 USD | 182.03 USD | `-78.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 433,360.00 USD | 0.00 USD | 221.45 USD | `-74.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 433,140.00 USD | 0.00 USD | 234.23 USD | `-73.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 432,910.00 USD | 0.00 USD | 209.48 USD | `-71.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 432,700.00 USD | 0.00 USD | 236.33 USD | `-69.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 432,460.00 USD | 0.00 USD | 431.68 USD | `-68.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 432,030.00 USD | 0.00 USD | 290.29 USD | `-59.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 431,740.00 USD | 0.00 USD | 120.22 USD | `-52.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 431,620.00 USD | 0.00 USD | 3,790.00 USD | `-49.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 427,830.00 USD | 0.00 USD | 251.68 USD | `-45.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 427,570.00 USD | 0.00 USD | 749.94 USD | `-42.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 426,820.00 USD | 0.00 USD | 772.71 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 426,050.00 USD | 0.00 USD | 3,760.00 USD | `-41.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 422,290.00 USD | 0.00 USD | 133.00 USD | `-40.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 422,150.00 USD | 0.00 USD | 1,320.00 USD | `-37.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 420,840.00 USD | 0.00 USD | 3,770.00 USD | `-36.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 417,070.00 USD | 0.00 USD | 2,070.00 USD | `-34.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 415,000.00 USD | 0.00 USD | 3,740.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 411,250.00 USD | 0.00 USD | 1,050.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 410,200.00 USD | 0.00 USD | 120.90 USD | `-30.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 410,080.00 USD | 0.00 USD | 146.80 USD | `-29.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 409,930.00 USD | 0.00 USD | 124.02 USD | `-28.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 409,810.00 USD | 0.00 USD | 5,030.00 USD | `-27.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 404,780.00 USD | 0.00 USD | 393.64 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 404,380.00 USD | 0.00 USD | 10,560.00 USD | `-25.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 393,820.00 USD | 0.00 USD | 83,680.00 USD | `-25.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 310,140.00 USD | 0.00 USD | 1,590.00 USD | `-24.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 308,550.00 USD | 0.00 USD | 52,990.00 USD | `-23.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 255,560.00 USD | 0.00 USD | 186.84 USD | `-22.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 255,380.00 USD | 0.00 USD | 742.88 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 254,630.00 USD | 0.00 USD | 902.70 USD | `-20.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 253,730.00 USD | 0.00 USD | 1,570.00 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 252,160.00 USD | 0.00 USD | 3,440.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 248,720.00 USD | 0.00 USD | 194.90 USD | `-17.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 248,520.00 USD | 0.00 USD | 1,360.00 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 247,160.00 USD | 0.00 USD | 9,010.00 USD | `-16.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 238,160.00 USD | 0.00 USD | 518.80 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 237,640.00 USD | 0.00 USD | 19,590.00 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 218,040.00 USD | 0.00 USD | 884.91 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 217,160.00 USD | 0.00 USD | 2,870.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 214,290.00 USD | 0.00 USD | 24,100.00 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 190,180.00 USD | 0.00 USD | 3,450.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 186,740.00 USD | 0.00 USD | 47,890.00 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 138,850.00 USD | 0.00 USD | 5,540.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 133,310.00 USD | 0.00 USD | 30,030.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 103,270.00 USD | 0.00 USD | 3,480.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 99,800.00 USD | 0.00 USD | 18,670.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 81,130.00 USD | 0.00 USD | 23,690.00 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 57,440.00 USD | 0.00 USD | 4,210.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 53,230.00 USD | 0.00 USD | 11,440.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 41,790.00 USD | 0.00 USD | 33,570.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 8,210.00 USD | 0.00 USD | 3,180.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 5,030.00 USD | 0.00 USD | 5,030.00 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 1,440.00 USD | 1,440.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 28,490.00 USD | 27,050.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 45,650.00 USD | 17,160.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 52,250.00 USD | 6,610.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 78,120.00 USD | 25,870.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 80,960.00 USD | 2,840.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 82,600.00 USD | 1,630.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 89,730.00 USD | 7,130.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 94,040.00 USD | 4,310.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 124,310.00 USD | 30,280.00 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 126,250.00 USD | 1,930.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 219,530.00 USD | 93,280.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 259,260.00 USD | 39,730.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 263,920.00 USD | 4,650.00 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 266,410.00 USD | 2,500.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 272,590.00 USD | 6,180.00 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 273,270.00 USD | 679.57 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 293,640.00 USD | 20,360.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 294,090.00 USD | 451.95 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 301,850.00 USD | 7,760.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 302,770.00 USD | 919.19 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 304,090.00 USD | 1,320.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 311,870.00 USD | 7,790.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 314,410.00 USD | 2,540.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 315,880.00 USD | 1,470.00 USD | 0.00 USD | `+21.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 316,830.00 USD | 954.14 USD | 0.00 USD | `+22.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 336,390.00 USD | 19,550.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 342,020.00 USD | 5,640.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 342,290.00 USD | 266.44 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 358,550.00 USD | 16,260.00 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 358,710.00 USD | 152.82 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 362,980.00 USD | 4,280.00 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 366,390.00 USD | 3,410.00 USD | 0.00 USD | `+28.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 380,060.00 USD | 13,670.00 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 380,280.00 USD | 218.25 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 382,130.00 USD | 1,850.00 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 389,390.00 USD | 7,270.00 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 390,340.00 USD | 950.82 USD | 0.00 USD | `+34.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 416,290.00 USD | 25,940.00 USD | 0.00 USD | `+35.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 418,740.00 USD | 2,450.00 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 656,050.00 USD | 237,310.00 USD | 0.00 USD | `+36.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 656,970.00 USD | 924.07 USD | 0.00 USD | `+37.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 657,870.00 USD | 893.01 USD | 0.00 USD | `+38.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 682,610.00 USD | 24,740.00 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 682,850.00 USD | 237.88 USD | 0.00 USD | `+40.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 686,140.00 USD | 3,290.00 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 689,310.00 USD | 3,170.00 USD | 0.00 USD | `+42.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 694,440.00 USD | 5,130.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 709,880.00 USD | 15,440.00 USD | 0.00 USD | `+44.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 716,680.00 USD | 6,800.00 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 723,180.00 USD | 6,500.00 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 729,720.00 USD | 6,540.00 USD | 0.00 USD | `+46.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 736,300.00 USD | 6,580.00 USD | 0.00 USD | `+47.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 746,230.00 USD | 9,930.00 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 850,210.00 USD | 103,980.00 USD | 0.00 USD | `+49.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 864,450.00 USD | 14,240.00 USD | 0.00 USD | `+50.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 948,810.00 USD | 84,360.00 USD | 0.00 USD | `+51.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 950,500.00 USD | 1,700.00 USD | 0.00 USD | `+52.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 957,590.00 USD | 7,080.00 USD | 0.00 USD | `+53.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 959,300.00 USD | 1,710.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 961,600.00 USD | 2,300.00 USD | 0.00 USD | `+54.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 963,340.00 USD | 1,740.00 USD | 0.00 USD | `+55.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 985,900.00 USD | 22,560.00 USD | 0.00 USD | `+56.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 990,290.00 USD | 4,390.00 USD | 0.00 USD | `+57.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 994,700.00 USD | 4,410.00 USD | 0.00 USD | `+58.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 999,140.00 USD | 4,440.00 USD | 0.00 USD | `+59.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,000,000.00 USD | 4,460.00 USD | 0.00 USD | `+60.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,000,000.00 USD | 448.75 USD | 0.00 USD | `+61.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,040,000.00 USD | 30,960.00 USD | 0.00 USD | `+62.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,040,000.00 USD | 453.75 USD | 0.00 USD | `+63.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,040,000.00 USD | 456.25 USD | 0.00 USD | `+63.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,040,000.00 USD | 458.75 USD | 0.00 USD | `+64.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,040,000.00 USD | 461.25 USD | 0.00 USD | `+65.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,040,000.00 USD | 4,540.00 USD | 0.00 USD | `+66.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,040,000.00 USD | 466.25 USD | 0.00 USD | `+67.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,040,000.00 USD | 468.75 USD | 0.00 USD | `+68.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,040,000.00 USD | 471.25 USD | 0.00 USD | `+69.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,040,000.00 USD | 473.75 USD | 0.00 USD | `+70.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,110,000.00 USD | 67,000.00 USD | 0.00 USD | `+71.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,110,000.00 USD | 574.50 USD | 0.00 USD | `+72.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,110,000.00 USD | 577.50 USD | 0.00 USD | `+72.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,110,000.00 USD | 2,710.00 USD | 0.00 USD | `+73.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,120,000.00 USD | 972.50 USD | 0.00 USD | `+74.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,120,000.00 USD | 7,680.00 USD | 0.00 USD | `+75.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,120,000.00 USD | 786.00 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,120,000.00 USD | 790.00 USD | 0.00 USD | `+77.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,130,000.00 USD | 992.50 USD | 0.00 USD | `+78.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,130,000.00 USD | 997.50 USD | 0.00 USD | `+79.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,730,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+80.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,730,000.00 USD | 1,010.00 USD | 0.00 USD | `+80.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,730,000.00 USD | 1,010.00 USD | 0.00 USD | `+81.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,730,000.00 USD | 1,020.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,730,000.00 USD | 1,020.00 USD | 0.00 USD | `+83.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,730,000.00 USD | 1,030.00 USD | 0.00 USD | `+84.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,740,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,740,000.00 USD | 1,040.00 USD | 0.00 USD | `+86.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,740,000.00 USD | 1,410.00 USD | 0.00 USD | `+87.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,740,000.00 USD | 1,050.00 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,740,000.00 USD | 4,000.00 USD | 0.00 USD | `+89.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,740,000.00 USD | 1,060.00 USD | 0.00 USD | `+89.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,750,000.00 USD | 1,060.00 USD | 0.00 USD | `+90.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,790,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+91.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,790,000.00 USD | 1,070.00 USD | 0.00 USD | `+92.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,790,000.00 USD | 1,080.00 USD | 0.00 USD | `+93.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,800,000.00 USD | 1,080.00 USD | 0.00 USD | `+94.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,800,000.00 USD | 1,090.00 USD | 0.00 USD | `+95.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,800,000.00 USD | 3,280.00 USD | 0.00 USD | `+96.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,800,000.00 USD | 1,100.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,800,000.00 USD | 1,100.00 USD | 0.00 USD | `+98.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,800,000.00 USD | 1,110.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,800,000.00 USD | 1,110.00 USD | 0.00 USD | `+99.84%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.32` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,840.00 USD |
| `7D` | `9.34` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,850.00 USD |
| `7D` | `9.36` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,380.00 USD |
| `7D` | `9.40` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,040.00 USD |
| `7D` | `9.42` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,520.00 USD |
| `7D` | `9.44` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,080.00 USD |
| `7D` | `9.46` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 94,230.00 USD | 0.00 USD | 317.45 USD |
| `7D` | `9.48` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,690.00 USD |
| `7D` | `9.52` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 0.00 USD | 911.85 USD | 10.22 USD |
| `7D` | `9.54` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 136.92 USD | 12,570.00 USD | 10.76 USD |
| `7D` | `9.56` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 160.73 USD | 16,080.00 USD | 71,350.00 USD |
| `7D` | `9.58` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 38,760.00 USD | 722.15 USD | 201.05 USD |
| `7D` | `9.60` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD |
| `7D` | `9.62` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD |
| `7D` | `9.64` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 8,500.00 USD | 0.00 USD | 143.89 USD |
| `7D` | `9.66` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 7,370.00 USD | 0.00 USD | 379.91 USD |
| `7D` | `9.68` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 0.00 USD | 0.00 USD | 31,940.00 USD |
| `7D` | `9.70` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.74` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.76` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 50,080.00 USD | 0.00 USD | 27,020.00 USD |
| `7D` | `9.78` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 0.00 USD | 671.70 USD | 487.81 USD |
| `7D` | `9.80` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,080.00 USD |
| `7D` | `9.82` | 12,750,000.00 USD | 0.00 USD | 12,750,000.00 USD | 84,900.00 USD | 10,390.00 USD | 506.80 USD |
| `7D` | `9.84` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 50,980.00 USD | 456.90 USD | 13,280.00 USD |
| `1D` | `9.86` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 29,590.00 USD | 11,120.00 USD | 11,090.00 USD |
| `7D` | `9.86` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 5,390.00 USD | 14,570.00 USD | 612.08 USD |
| `1D` | `9.88` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,130.00 USD |
| `7D` | `9.88` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 10,280.00 USD | 15,600.00 USD | 107.02 USD |
| `1D` | `9.90` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,950.00 USD |
| `7D` | `9.90` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 48,670.00 USD | 0.00 USD | 154.66 USD |
| `1D` | `9.92` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 23,540.00 USD | 20,070.00 USD | 467.72 USD |
| `7D` | `9.92` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 0.00 USD | 12,280.00 USD | 279.33 USD |
| `1D` | `9.94` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 1,960.00 USD | 5,150.00 USD | 263.16 USD |
| `7D` | `9.94` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,950.00 USD |
| `1D` | `9.96` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 75,160.00 USD | 15,490.00 USD | 25,730.00 USD |
| `7D` | `9.96` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,160.00 USD |
| `1D` | `9.98` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 37,260.00 USD | 6,830.00 USD | 67,870.00 USD |
| `7D` | `9.98` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 4,830.00 USD | 6,160.00 USD | 59,850.00 USD |
| `1D` | `10.00` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 5,670.00 USD | 4,500.00 USD | 64,590.00 USD |
| `7D` | `10.00` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 641.95 USD | 7,630.00 USD | 12,800.00 USD |
| `1D` | `10.02` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 17,880.00 USD | 19,650.00 USD | 18,740.00 USD |
| `7D` | `10.02` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 8,880.00 USD | 317.30 USD | 415.56 USD |
| `1D` | `10.04` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 18,000.00 USD | 4,820.00 USD | 0.00 USD |
| `7D` | `10.04` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 7,200.00 USD | 1,210.00 USD | 0.00 USD |
| `1D` | `10.06` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,090.00 USD |
| `7D` | `10.06` | 12,230,000.00 USD | 0.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 83,330.00 USD |
| `1D` | `10.08` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 167,250.00 USD | 701.42 USD | 76,040.00 USD |
| `7D` | `10.08` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.10` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 7,570.00 USD | 42,810.00 USD | 531.42 USD |
| `7D` | `10.10` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 6,580.00 USD | 0.00 USD | 372.62 USD |
| `1D` | `10.12` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 1,150.00 USD | 20,910.00 USD | 195.46 USD |
| `7D` | `10.12` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 10,140.00 USD | 559.40 USD | 56,470.00 USD |
| `1D` | `10.14` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,480.00 USD |
| `7D` | `10.14` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,320.00 USD |
| `1D` | `10.16` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,350.00 USD |
| `7D` | `10.16` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,370.00 USD |
| `1D` | `10.18` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,390.00 USD |
| `7D` | `10.18` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,270.00 USD |
| `1D` | `10.20` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,250.00 USD |
| `7D` | `10.20` | 11,240,000.00 USD | 0.00 USD | 11,240,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,650.00 USD |
| `1D` | `10.22` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,760.00 USD |
| `7D` | `10.22` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,030.00 USD |
| `1D` | `10.24` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,270.00 USD |
| `7D` | `10.24` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,040.00 USD |
| `1D` | `10.26` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 63,830.00 USD | 8,070.00 USD | 101,240.00 USD |
| `7D` | `10.26` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,410.00 USD |
| `1D` | `10.28` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,230.00 USD |
| `7D` | `10.28` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.30` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,780.00 USD |
| `7D` | `10.30` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,210.00 USD |
| `7D` | `10.32` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 43,210.00 USD | 0.00 USD | 100,020.00 USD |
| `1D` | `10.34` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 66,410.00 USD | 9,100.00 USD | 85,960.00 USD |
| `7D` | `10.34` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.36` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 6,270.00 USD | 3,580.00 USD | 128.63 USD |
| `7D` | `10.36` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.38` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 42,350.00 USD | 45,170.00 USD | 7,610.00 USD |
| `7D` | `10.38` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,730.00 USD |
| `7D` | `10.40` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 244,890.00 USD | 0.00 USD | 154.00 USD |
| `7D` | `10.42` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 229,660.00 USD | 97,940.00 USD | 258.06 USD |
| `1D` | `10.44` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,420.00 USD |
| `7D` | `10.44` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 439,060.00 USD | 13,410.00 USD | 334,240.00 USD |
| `1D` | `10.46` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,170.00 USD |
| `7D` | `10.46` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 323,570.00 USD | 103,810.00 USD | 385.15 USD |
| `1D` | `10.48` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,100.00 USD |
| `7D` | `10.48` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,160.00 USD |
| `7D` | `10.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 4,770.00 USD | 52,370.00 USD | 236.06 USD |
| `1D` | `10.52` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 1,200.00 USD | 12,710.00 USD | 38,250.00 USD |
| `7D` | `10.52` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,260.00 USD |
| `7D` | `10.54` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 110,630.00 USD | 38,520.00 USD | 38,270.00 USD |
| `7D` | `10.56` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 122,960.00 USD | 81,670.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,090.00 USD |
| `7D` | `10.58` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.60` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,900.00 USD |
| `7D` | `10.60` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 0.00 USD | 24,130.00 USD | 59.60 USD |
| `1D` | `10.62` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,030.00 USD |
| `7D` | `10.62` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 99,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.64` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 109,830.00 USD | 9,030.00 USD | 59,670.00 USD |
| `7D` | `10.64` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 11,150.00 USD | 0.00 USD | 28,480.00 USD |
| `1D` | `10.66` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 59,930.00 USD | 10,280.00 USD | 33,460.00 USD |
| `7D` | `10.66` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 9,470.00 USD | 19,620.00 USD | 9,470.00 USD |
| `1D` | `10.68` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 67,250.00 USD | 37,570.00 USD | 70,060.00 USD |
| `7D` | `10.68` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 16,330.00 USD | 27,190.00 USD | 148.26 USD |
| `1D` | `10.70` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 12,670.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `10.70` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,300.00 USD |
| `7D` | `10.72` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.74` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 877.75 USD | 100,010.00 USD |
| `1D` | `10.76` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD |
| `7D` | `10.76` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 16,310.00 USD | 120,930.00 USD | 261.17 USD |
| `1D` | `10.78` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,550.00 USD |
| `7D` | `10.78` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 535,020.00 USD | 46,010.00 USD | 104,150.00 USD |
| `1D` | `10.80` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,640.00 USD |
| `7D` | `10.80` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 69,540.00 USD | 70,260.00 USD | 463.06 USD |
| `1D` | `10.82` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,820.00 USD |
| `7D` | `10.82` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 0.00 USD | 104,870.00 USD | 207,140.00 USD |
| `1D` | `10.84` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,780.00 USD |
| `7D` | `10.84` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 377,580.00 USD | 80,420.00 USD | 196,090.00 USD |
| `1D` | `10.86` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 203,140.00 USD | 34,420.00 USD | 219,940.00 USD |
| `7D` | `10.86` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 323,850.00 USD | 3,610.00 USD | 391,730.00 USD |
| `1D` | `10.88` | 648,680.00 USD | 0.00 USD | 648,680.00 USD | 61,520.00 USD | 15,030.00 USD | 67,330.00 USD |
| `7D` | `10.88` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 111,430.00 USD | 78,360.00 USD | 365,650.00 USD |
| `1D` | `10.90` | 504,790.00 USD | 0.00 USD | 504,790.00 USD | 114,210.00 USD | 53,630.00 USD | 67,920.00 USD |
| `7D` | `10.90` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 32,650.00 USD | 49,530.00 USD | 221,500.00 USD |
| `1D` | `10.92` | 269,030.00 USD | 0.00 USD | 269,030.00 USD | 138,180.00 USD | 33,800.00 USD | 0.00 USD |
| `7D` | `10.92` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 226,910.00 USD | 0.00 USD | 110,860.00 USD |
| `1D` | `10.94` | 97,040.00 USD | 0.00 USD | 97,040.00 USD | 4,370.00 USD | 1,550.00 USD | 103.92 USD |
| `7D` | `10.94` | 760,120.00 USD | 0.00 USD | 760,120.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 91,010.00 USD | 0.00 USD | 91,010.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `10.96` | 757,640.00 USD | 0.00 USD | 757,640.00 USD | 10,430.00 USD | 0.00 USD | 49,920.00 USD |
| `1D` | `10.98` | 3,260.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 260.69 USD |
| `7D` | `10.98` | 697,290.00 USD | 0.00 USD | 697,290.00 USD | 17,930.00 USD | 0.00 USD | 209,940.00 USD |
| `1D` | `11.00` | 3,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | 0.00 USD | 238.07 USD |
| `7D` | `11.00` | 469,420.00 USD | 0.00 USD | 469,420.00 USD | 10,830.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `11.02` | 457,530.00 USD | 0.00 USD | 457,530.00 USD | 0.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.04` | 2,760.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 2,200.00 USD | 120.16 USD |
| `7D` | `11.04` | 314,490.00 USD | 0.00 USD | 314,490.00 USD | 0.00 USD | 0.00 USD | 178,890.00 USD |
| `1D` | `11.06` | 438.64 USD | 0.00 USD | 438.64 USD | 0.00 USD | 0.00 USD | 438.64 USD |
| `7D` | `11.06` | 135,600.00 USD | 0.00 USD | 135,600.00 USD | 0.00 USD | 0.00 USD | 133,110.00 USD |
| `1D` | `11.08` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.08` | 2,480.00 USD | 0.00 USD | 2,480.00 USD | 0.00 USD | 1,810.00 USD | 678.13 USD |
| `7D` | `11.09` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.10` | 4,580.00 USD | 4,580.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | 60.85 USD |
| `7D` | `11.10` | 7,300.00 USD | 7,300.00 USD | 0.00 USD | 0.00 USD | 6,920.00 USD | 373.87 USD |
| `1D` | `11.12` | 143,190.00 USD | 143,190.00 USD | 0.00 USD | 0.00 USD | 2,260.00 USD | 136,360.00 USD |
| `7D` | `11.12` | 121,030.00 USD | 121,030.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | 108,550.00 USD |
| `1D` | `11.14` | 211,320.00 USD | 211,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 68,140.00 USD |
| `7D` | `11.14` | 131,000.00 USD | 131,000.00 USD | 0.00 USD | 0.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `11.16` | 391,250.00 USD | 391,250.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,810.00 USD |
| `7D` | `11.16` | 270,410.00 USD | 270,410.00 USD | 0.00 USD | 838.30 USD | 72,860.00 USD | 65,710.00 USD |
| `1D` | `11.18` | 563,890.00 USD | 563,890.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,650.00 USD |
| `7D` | `11.18` | 288,520.00 USD | 288,520.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 1,090.00 USD |
| `1D` | `11.20` | 817,300.00 USD | 817,300.00 USD | 0.00 USD | 76,580.00 USD | 85,800.00 USD | 91,030.00 USD |
| `7D` | `11.20` | 629,340.00 USD | 629,340.00 USD | 0.00 USD | 171,840.00 USD | 89,800.00 USD | 79,180.00 USD |
| `1D` | `11.22` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 344,290.00 USD | 76,600.00 USD | 142,360.00 USD |
| `7D` | `11.22` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 482,460.00 USD | 42,050.00 USD | 0.00 USD |
| `1D` | `11.24` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 163,340.00 USD | 58,590.00 USD | 155,450.00 USD |
| `7D` | `11.24` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 231,960.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.26` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 154,720.00 USD | 54,310.00 USD | 71,610.00 USD |
| `7D` | `11.26` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 520,990.00 USD | 48,250.00 USD | 295,860.00 USD |
| `1D` | `11.28` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 388,220.00 USD | 67,290.00 USD | 262,900.00 USD |
| `7D` | `11.28` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 429,350.00 USD | 57,050.00 USD | 148,080.00 USD |
| `1D` | `11.30` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 261,740.00 USD | 81,010.00 USD | 160,170.00 USD |
| `7D` | `11.30` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 77,260.00 USD |
| `1D` | `11.32` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 181,160.00 USD | 72,950.00 USD | 149,910.00 USD |
| `7D` | `11.32` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 194,150.00 USD | 62,240.00 USD | 298,540.00 USD |
| `1D` | `11.34` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 376,310.00 USD | 128,380.00 USD | 126,280.00 USD |
| `7D` | `11.34` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 159,840.00 USD | 127,800.00 USD | 101,950.00 USD |
| `1D` | `11.36` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 173,620.00 USD | 87,180.00 USD | 56,190.00 USD |
| `7D` | `11.36` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 57,230.00 USD |
| `1D` | `11.38` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 118,230.00 USD | 63,980.00 USD | 25,170.00 USD |
| `7D` | `11.38` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,000.00 USD |
| `1D` | `11.40` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,640.00 USD |
| `7D` | `11.40` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 126,960.00 USD | 83,740.00 USD | 113,570.00 USD |
| `7D` | `11.42` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 66,800.00 USD | 46,660.00 USD | 115,000.00 USD |
| `1D` | `11.44` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 96,590.00 USD | 54,990.00 USD | 109,120.00 USD |
| `7D` | `11.44` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 303,190.00 USD | 101,940.00 USD | 38,420.00 USD |
| `1D` | `11.46` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 86,190.00 USD | 77,320.00 USD | 50,920.00 USD |
| `7D` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 122,890.00 USD | 55,470.00 USD | 0.00 USD |
| `1D` | `11.48` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 26,740.00 USD | 35,780.00 USD | 2,120.00 USD |
| `7D` | `11.48` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD |
| `1D` | `11.50` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 78,340.00 USD | 38,760.00 USD | 63,750.00 USD |
| `7D` | `11.50` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 127,920.00 USD | 22,260.00 USD | 55,280.00 USD |
| `7D` | `11.52` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 61,970.00 USD |
| `1D` | `11.54` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 92,850.00 USD | 23,030.00 USD | 105,040.00 USD |
| `7D` | `11.54` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 53,520.00 USD | 19,620.00 USD | 117,820.00 USD |
| `1D` | `11.56` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 128,820.00 USD | 29,910.00 USD | 57,190.00 USD |
| `7D` | `11.56` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 102,980.00 USD | 25,560.00 USD | 626.77 USD |
| `1D` | `11.58` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 76,330.00 USD | 2,950.00 USD | 17,680.00 USD |
| `7D` | `11.58` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 59,780.00 USD | 21,610.00 USD | 67,420.00 USD |
| `7D` | `11.60` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 46,010.00 USD | 10,510.00 USD | 23,010.00 USD |
| `1D` | `11.62` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 45,260.00 USD | 512.95 USD | 47,780.00 USD |
| `7D` | `11.62` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.64` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 5,660.00 USD | 7,410.00 USD | 31,230.00 USD |
| `7D` | `11.64` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 0.00 USD |
| `1D` | `11.66` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 1,070.00 USD | 12,290.00 USD | 25,920.00 USD |
| `7D` | `11.66` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.68` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 127,580.00 USD | 35,770.00 USD | 32,400.00 USD |
| `7D` | `11.68` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 1,280.00 USD | 20,730.00 USD | 71,340.00 USD |
| `1D` | `11.70` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,490.00 USD |
| `7D` | `11.70` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 201.05 USD |
| `1D` | `11.72` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 91,840.00 USD | 17,160.00 USD | 98,150.00 USD |
| `7D` | `11.72` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,330.00 USD |
| `1D` | `11.74` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 76,690.00 USD | 30,280.00 USD | 73,410.00 USD |
| `7D` | `11.74` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,550.00 USD |
| `1D` | `11.76` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 26,330.00 USD | 14,880.00 USD | 24,680.00 USD |
| `7D` | `11.76` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,300.00 USD |
| `1D` | `11.78` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 11,750.00 USD | 20,510.00 USD | 40,070.00 USD |
| `7D` | `11.78` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 9,130.00 USD | 0.00 USD | 56,710.00 USD |
| `1D` | `11.80` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 1,350.00 USD | 17,720.00 USD | 176.08 USD |
| `7D` | `11.80` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 176.96 USD |
| `1D` | `11.82` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 12,610.00 USD | 53.10 USD | 36,030.00 USD |
| `7D` | `11.82` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 182,750.00 USD | 41,910.00 USD | 36.54 USD |
| `1D` | `11.84` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 44,510.00 USD | 11,870.00 USD | 45,650.00 USD |
| `7D` | `11.84` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,740.00 USD |
| `1D` | `11.86` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 11,490.00 USD | 12,970.00 USD | 51,000.00 USD |
| `7D` | `11.86` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 962.44 USD | 6,180.00 USD | 0.00 USD |
| `1D` | `11.88` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 21,500.00 USD | 28,990.00 USD | 60,560.00 USD |
| `7D` | `11.88` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,650.00 USD |
| `1D` | `11.90` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 27,960.00 USD |
| `7D` | `11.90` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 174.36 USD |
| `1D` | `11.92` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,010.00 USD |
| `7D` | `11.92` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,670.00 USD |
| `1D` | `11.94` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 48,030.00 USD | 15,260.00 USD | 40,150.00 USD |
| `7D` | `11.94` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,430.00 USD |
| `1D` | `11.96` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD |
| `7D` | `11.96` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,020.00 USD |
| `1D` | `11.98` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 59,940.00 USD | 29,050.00 USD | 68,140.00 USD |
| `7D` | `11.98` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,760.00 USD |
| `1D` | `12.00` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 102,680.00 USD | 23,880.00 USD | 36,270.00 USD |
| `7D` | `12.00` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,040.00 USD |
| `1D` | `12.02` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 13,680.00 USD | 7,110.00 USD | 31,530.00 USD |
| `7D` | `12.02` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,280.00 USD |
| `1D` | `12.04` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 77,630.00 USD | 36,810.00 USD | 46,090.00 USD |
| `7D` | `12.04` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,950.00 USD |
| `1D` | `12.06` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 76,750.00 USD | 28,460.00 USD | 63,410.00 USD |
| `7D` | `12.06` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,810.00 USD |
| `1D` | `12.08` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 43,090.00 USD | 35,930.00 USD | 52,270.00 USD |
| `7D` | `12.08` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,640.00 USD |
| `1D` | `12.10` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 50,850.00 USD | 25,300.00 USD | 35,010.00 USD |
| `7D` | `12.10` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,380.00 USD |
| `1D` | `12.12` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 116,870.00 USD | 54,580.00 USD | 50,420.00 USD |
| `7D` | `12.12` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,650.00 USD |
| `1D` | `12.14` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 75,170.00 USD | 37,540.00 USD | 55,690.00 USD |
| `7D` | `12.14` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 148,090.00 USD | 102,170.00 USD | 119,060.00 USD |
| `1D` | `12.16` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 131,220.00 USD | 34,710.00 USD | 67,700.00 USD |
| `7D` | `12.16` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 182,020.00 USD | 69,310.00 USD | 75,030.00 USD |
| `1D` | `12.18` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 112,670.00 USD | 48,310.00 USD | 50,550.00 USD |
| `7D` | `12.18` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 74,850.00 USD | 54,220.00 USD | 43,380.00 USD |
| `1D` | `12.20` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 77,250.00 USD | 43,870.00 USD | 41,940.00 USD |
| `7D` | `12.20` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 194,760.00 USD | 57,500.00 USD | 75,340.00 USD |
| `1D` | `12.22` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 10,510.00 USD | 21,000.00 USD | 36,060.00 USD |
| `7D` | `12.22` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 262,140.00 USD | 63,820.00 USD | 64,270.00 USD |
| `1D` | `12.24` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 14,540.00 USD | 15,320.00 USD | 7,630.00 USD |
| `7D` | `12.24` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 50,300.00 USD | 45,440.00 USD | 10,330.00 USD |
| `1D` | `12.26` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 12,590.00 USD | 12,870.00 USD | 12,140.00 USD |
| `7D` | `12.26` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 73,660.00 USD | 54,120.00 USD | 51,020.00 USD |
| `1D` | `12.28` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 49,100.00 USD | 7,490.00 USD | 12,080.00 USD |
| `7D` | `12.28` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 156,680.00 USD | 27,340.00 USD | 90,550.00 USD |
| `1D` | `12.29` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD |
| `7D` | `12.30` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 70,240.00 USD | 24,020.00 USD | 23,400.00 USD |
| `7D` | `12.32` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 17,900.00 USD |
| `7D` | `12.34` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD |
| `7D` | `12.36` | 15,320,000.00 USD | 15,320,000.00 USD | 0.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD |
| `7D` | `12.38` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `511.51M` | Total OI Tokens: `46,027,591.1 LINK`
  * 1h OI Change: `+1.00%` | 4h OI Change: `-1.23%` | 24h OI Change: `-7.32%`
  * Exchange Breakdown: Binance=`100.66M` | Bybit=`69.09M` | OKX=`27.08M` | Hyperliquid=`56.04M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.79K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0078%` |
| **USDT Bybit** | `0.0003%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0043%` | **USDT Bitget** | `0.0063%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `51.06%` | `48.94%` | `1.04` | 55,450,000.00 USD |
| `15M` | `Binance` | `50.69%` | `49.31%` | `1.03` | 17,360,000.00 USD |
| `15M` | `OKX` | `50.19%` | `49.81%` | `1.01` | 9,160,000.00 USD |
| `15M` | `Bybit` | `56.23%` | `43.77%` | `1.28` | 5,430,000.00 USD |
| `15M` | `KuCoin` | `47.24%` | `52.76%` | `0.90` | 41,130.00 USD |
| `15M` | `Gate` | `53.65%` | `46.35%` | `1.16` | 5,420,000.00 USD |
| `15M` | `Bitget` | `41.03%` | `58.97%` | `0.70` | 1,400,000.00 USD |
| `15M` | `BingX` | `46.02%` | `53.98%` | `0.85` | 4,350,000.00 USD |
| `15M` | `MEXC` | `46.12%` | `53.88%` | `0.86` | 3,010,000.00 USD |
| `15M` | `Bitunix` | `58.91%` | `41.09%` | `1.43` | 1,920,000.00 USD |
| `15M` | `Hyperliquid` | `54.9%` | `45.1%` | `1.22` | 487,790.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `42.01%` | `57.99%` | `0.72` | 2,500,000.00 USD |
| `15M` | `Crypto.com` | `41.29%` | `58.71%` | `0.70` | 78,620.00 USD |
| `15M` | `WhiteBIT` | `5.09%` | `94.91%` | `0.05` | 1,350,000.00 USD |
| `15M` | `HTX` | `38.81%` | `61.19%` | `0.63` | 49,840.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.2%` | `9.8%` | `9.20` | 2,410,000.00 USD |
| `15M` | `Aster` | `50.26%` | `49.74%` | `1.01` | 216,640.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.83%` | `55.17%` | `0.81` | 272,280.00 USD |
| `15M` | `Whale Positions` | `50.69%` | `49.31%` | `1.03` | 17,360,000.00 USD |
| `15M` | `Global Accounts` | `51.06%` | `48.94%` | `1.04` | 55,450,000.00 USD |
| `1H` | `LINK` | `53.76%` | `46.24%` | `1.16` | 241,180,000.00 USD |
| `1H` | `Binance` | `53.38%` | `46.62%` | `1.15` | 75,930,000.00 USD |
| `1H` | `OKX` | `52.74%` | `47.26%` | `1.12` | 49,450,000.00 USD |
| `1H` | `Bybit` | `58.68%` | `41.32%` | `1.42` | 18,680,000.00 USD |
| `1H` | `KuCoin` | `36.08%` | `63.92%` | `0.56` | 486,680.00 USD |
| `1H` | `Gate` | `56.24%` | `43.76%` | `1.29` | 19,970,000.00 USD |
| `1H` | `Bitget` | `54.74%` | `45.26%` | `1.21` | 7,270,000.00 USD |
| `1H` | `BingX` | `54.99%` | `45.01%` | `1.22` | 13,650,000.00 USD |
| `1H` | `MEXC` | `61%` | `39%` | `1.56` | 15,890,000.00 USD |
| `1H` | `Bitunix` | `52.62%` | `47.38%` | `1.11` | 9,790,000.00 USD |
| `1H` | `Hyperliquid` | `71.21%` | `28.79%` | `2.47` | 5,040,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.95%` | `50.05%` | `1.00` | 9,470,000.00 USD |
| `1H` | `Crypto.com` | `47.35%` | `52.65%` | `0.90` | 577,420.00 USD |
| `1H` | `WhiteBIT` | `6.63%` | `93.37%` | `0.07` | 5,590,000.00 USD |
| `1H` | `HTX` | `73.65%` | `26.35%` | `2.80` | 424,140.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `66.1%` | `33.9%` | `1.95` | 5,310,000.00 USD |
| `1H` | `Aster` | `36.04%` | `63.96%` | `0.56` | 1,660,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.23%` | `51.77%` | `0.93` | 1,990,000.00 USD |
| `1H` | `Whale Positions` | `53.38%` | `46.62%` | `1.15` | 75,930,000.00 USD |
| `1H` | `Global Accounts` | `53.76%` | `46.24%` | `1.16` | 241,180,000.00 USD |
| `4H` | `LINK` | `44.63%` | `55.37%` | `0.81` | 176,930,000.00 USD |
| `4H` | `Binance` | `45.05%` | `54.95%` | `0.82` | 62,730,000.00 USD |
| `4H` | `OKX` | `48%` | `52%` | `0.92` | 34,600,000.00 USD |
| `4H` | `Bybit` | `44.08%` | `55.92%` | `0.79` | 13,020,000.00 USD |
| `4H` | `KuCoin` | `45.87%` | `54.13%` | `0.85` | 1,190,000.00 USD |
| `4H` | `Gate` | `45.95%` | `54.05%` | `0.85` | 30,470,000.00 USD |
| `4H` | `Bitget` | `46.18%` | `53.82%` | `0.86` | 2,660,000.00 USD |
| `4H` | `BingX` | `37.81%` | `62.19%` | `0.61` | 3,630,000.00 USD |
| `4H` | `MEXC` | `48.47%` | `51.53%` | `0.94` | 8,810,000.00 USD |
| `4H` | `Bitunix` | `47.75%` | `52.25%` | `0.91` | 4,280,000.00 USD |
| `4H` | `Hyperliquid` | `74.38%` | `25.62%` | `2.90` | 2,530,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.23%` | `47.77%` | `1.09` | 1,110,000.00 USD |
| `4H` | `Crypto.com` | `41.74%` | `58.26%` | `0.72` | 263,770.00 USD |
| `4H` | `WhiteBIT` | `9.28%` | `90.72%` | `0.10` | 8,500,000.00 USD |
| `4H` | `HTX` | `50.64%` | `49.36%` | `1.03` | 1,010,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `55.49%` | `44.51%` | `1.25` | 1,170,000.00 USD |
| `4H` | `Aster` | `37.68%` | `62.32%` | `0.60` | 875,660.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `61.82%` | `38.18%` | `1.62` | 93,100.00 USD |
| `4H` | `Whale Positions` | `45.05%` | `54.95%` | `0.82` | 62,730,000.00 USD |
| `4H` | `Global Accounts` | `44.63%` | `55.37%` | `0.81` | 176,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.01` | `11.00` | `11.01` | `11.03` | `10.97` | 1,915,299.28 USD | 805,989.55 USD | 1,109,309.72 USD | -303,320.17 USD | `-15.84%` | `3B / 10S` |
| `5:00 UTC` | `10.97` | `10.99` | `10.97` | `11.01` | `10.96` | 1,089,442.23 USD | 506,886.53 USD | 582,555.71 USD | -75,669.18 USD | `-6.95%` | `5B / 8S` |
| `0:00 UTC` | `10.98` | `10.99` | `10.98` | `11.03` | `10.95` | 1,226,717.62 USD | 576,497.16 USD | 650,220.46 USD | -73,723.30 USD | `-6.01%` | `21B / 13S` |
| `5:00 UTC` | `11.03` | `11.02` | `11.03` | `11.05` | `10.99` | 1,086,301.02 USD | 486,090.76 USD | 600,210.26 USD | -114,119.49 USD | `-10.51%` | `11B / 6S` |
| `0:00 UTC` | `11.02` | `11.02` | `11.02` | `11.04` | `10.99` | 1,056,195.55 USD | 514,499.98 USD | 541,695.57 USD | -27,195.58 USD | `-2.57%` | `3B / 5S` |
| `5:00 UTC` | `11.00` | `11.02` | `11.00` | `11.06` | `10.99` | 963,211.20 USD | 455,740.43 USD | 507,470.77 USD | -51,730.34 USD | `-5.37%` | `9B / 12S` |
| `0:00 UTC` | `11.05` | `11.06` | `11.05` | `11.10` | `11.01` | 3,673,451.57 USD | 2,114,279.15 USD | 1,559,172.42 USD | 555,106.73 USD | `+15.11%` | `18B / 10S` |
| `5:00 UTC` | `11.12` | `11.10` | `11.12` | `11.14` | `11.05` | 1,081,659.44 USD | 610,094.88 USD | 471,564.56 USD | 138,530.32 USD | `+12.81%` | `17B / 11S` |
| `0:00 UTC` | `11.11` | `11.12` | `11.11` | `11.15` | `11.09` | 1,525,673.69 USD | 765,847.62 USD | 759,826.07 USD | 6,021.54 USD | `+0.39%` | `8B / 12S` |
| `5:00 UTC` | `11.11` | `11.10` | `11.11` | `11.12` | `11.08` | 261,819.42 USD | 113,058.48 USD | 148,760.95 USD | -35,702.47 USD | `-13.64%` | `6B / 7S` |

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
| `5m` | 1,200.00 USD | -62,620.00 USD | **`DISTRIBUTION`** |
| `15m` | -31,170.00 USD | 93,230.00 USD | **`ACCUMULATION`** |
| `30m` | 180,420.00 USD | 763,760.00 USD | **`ACCUMULATION`** |
| `1h` | 672,000.00 USD | 660,400.00 USD | **`ACCUMULATION`** |
| `2h` | 831,420.00 USD | 449,560.00 USD | **`ACCUMULATION`** |
| `4h` | 280,650.00 USD | -572,290.00 USD | **`DISTRIBUTION`** |
| `6h` | 302,730.00 USD | -981,320.00 USD | **`DISTRIBUTION`** |
| `8h` | -270,890.00 USD | -277,590.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,390,000.00 USD | -701,350.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,900,000.00 USD | -22,390,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -19,760,000.00 USD | -41,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,530,000.00 USD | -192,750,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.20K` | 15m=`-31.17K` | 1h=`+672.00K` | 24h=`-10.90M`
* Futures Capital Netflows: 5m=`-62.62K` | 15m=`+93.23K` | 1h=`+660.40K` | 24h=`-22.39M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.57` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.34` (Risk Distance: `0.2237` pts)
  * +2.5R Take Profit: `11.13`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.34` (Risk Distance: `0.2237` pts)
  * +2.5R Take Profit: `10.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
