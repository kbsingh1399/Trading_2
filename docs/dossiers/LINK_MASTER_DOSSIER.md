# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 17:10:08 IST` (`2026-10-30 11:40:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.04` | **Live Ask Quote**: `11.13` | **Mid Price**: `11.09`
- **Spread Points**: `84.00` | **Spread BPS**: `75.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.09` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.16` | Lower -3.00σ Band: `11.01`
  * Upper +2.51σ Band: `11.15` | Lower -2.51σ Band: `11.02`
  * Upper +2.01σ Band: `11.13` | Lower -2.01σ Band: `11.04`
  * Upper +2.00σ Band: `11.13` | Lower -2.00σ Band: `11.04`
  * Upper +1.28σ Band: `11.12` | Lower -1.28σ Band: `11.05`
  * Upper +1.00σ Band: `11.11` | Lower -1.00σ Band: `11.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.09` | EMA-20=`11.09` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.09` (Slope: `+0.0000`) | EMA-100=`11.09`
  * Institutional Anchors: EMA-144=`11.09` | EMA-200=`11.09` (Slope: `+0.0000`) | EMA-233=`11.09`
- **Range Boundaries**: 24H High=`11.20` | 24H Low=`10.97` | Weekly High=`11.31` | Weekly Low=`10.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-0.32%`)
  * Point of Control (POC) = `10.96` (Distance: `+1.13%`)
  * Value Area Low (VAL) = `10.57` (Distance: `+4.91%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `11.04` - `11.13`
  * Optimal Trade Entry (OTE 0.705): `11.11`
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
| --- | **`11.09`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `422` | `0xecb6...2b00` | `SHORT` | 5,259,899.29 USD | `473,694,100.00` | `10.66` | `11.10` | `79.49` | -210,958.56 USD | `-4.01%` | `10X Cross` |
| `507` | `0x73ce...8ce9` | `LONG` | 4,440,528.77 USD | `400,011,600.00` | `12.05` | `11.10` | `7.82` | -379,224.93 USD | `-8.54%` | `5X Cross` |
| `844` | `0xb83d...6e36` | `SHORT` | 2,686,586.31 USD | `242,013,000.00` | `12.93` | `11.10` | `430.11` | 443,307.88 USD | `+16.50%` | `3X Cross` |
| `883` | `0x458d...ab3b` | `LONG` | 2,522,345.73 USD | `227,156,700.00` | `13.13` | `11.10` | `9.34` | -459,884.67 USD | `-18.23%` | `3X Isolated` |
| `970` | `0xdd53...2b13` | `SHORT` | 2,292,908.21 USD | `206,475,300.00` | `11.92` | `11.10` | `295.61` | 168,314.72 USD | `+7.34%` | `3X Cross` |
| `995` | `0x3dc9...54b0` | `SHORT` | 2,220,800.00 USD | `200,000,000.00` | `7.56` | `11.10` | `93.77` | -709,641.58 USD | `-31.95%` | `10X Cross` |
| `1006` | `0x45d2...4029` | `SHORT` | 2,171,027.50 USD | `195,500,000.00` | `11.54` | `11.10` | `216.50` | 85,455.93 USD | `+3.94%` | `10X Cross` |
| `1190` | `0x6540...f7b7` | `LONG` | 1,859,023.64 USD | `167,404,200.00` | `12.40` | `11.10` | `6.70` | -216,782.47 USD | `-11.66%` | `5X Isolated` |
| `1255` | `0xeadc...9d55` | `LONG` | 1,751,007.53 USD | `157,691,600.00` | `9.43` | `11.10` | `0.000000` | 264,352.62 USD | `+15.10%` | `10X Cross` |
| `1471` | `0x5b5d...c060` | `SHORT` | 1,462,971.60 USD | `131,775,500.00` | `13.61` | `11.10` | `1089.87` | 330,286.37 USD | `+22.58%` | `3X Cross` |
| `1654` | `0xf6f3...47f8` | `SHORT` | 1,277,233.16 USD | `115,024,600.00` | `11.42` | `11.10` | `18.30` | 36,097.03 USD | `+2.83%` | `5X Cross` |
| `1836` | `0xfe7e...11b4` | `LONG` | 1,123,283.05 USD | `101,142,000.00` | `14.47` | `11.10` | `5.33` | -339,830.10 USD | `-30.25%` | `5X Isolated` |
| `1878` | `0x8af7...fa05` | `SHORT` | 1,095,632.63 USD | `98,661,200.00` | `14.08` | `11.10` | `201.16` | 293,549.91 USD | `+26.79%` | `10X Cross` |

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
| `7D` | `Long Liquidation` | `9.32` | 13,830,000.00 USD | 13,830,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 13,750,000.00 USD | 13,750,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 13,710,000.00 USD | 13,710,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 13,700,000.00 USD | 13,700,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 13,670,000.00 USD | 13,670,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 13,640,000.00 USD | 13,640,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 13,590,000.00 USD | 13,590,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 127,760.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 13,540,000.00 USD | 13,540,000.00 USD | 94,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 13,440,000.00 USD | 13,440,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 13,440,000.00 USD | 13,440,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 13,370,000.00 USD | 13,370,000.00 USD | 136.92 USD | 12,570.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 102,930.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 13,360,000.00 USD | 13,360,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 13,270,000.00 USD | 13,270,000.00 USD | 38,760.00 USD | 722.15 USD | 20.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 13,230,000.00 USD | 13,230,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 659.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 13,030,000.00 USD | 13,030,000.00 USD | 8,500.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 193,100.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 13,020,000.00 USD | 13,020,000.00 USD | 7,370.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 12,990,000.00 USD | 12,990,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 12,950,000.00 USD | 12,950,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 94,920.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 12,950,000.00 USD | 12,950,000.00 USD | 50,080.00 USD | 0.00 USD | 27,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 12,870,000.00 USD | 12,870,000.00 USD | 47,490.00 USD | 14,120.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 12,780,000.00 USD | 12,780,000.00 USD | 84,900.00 USD | 10,390.00 USD | 863.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 12,680,000.00 USD | 12,680,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 29,740.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 9,360,000.00 USD | 9,360,000.00 USD | 29,590.00 USD | 11,120.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.86` | 12,620,000.00 USD | 12,620,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 9,310,000.00 USD | 9,310,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 12,600,000.00 USD | 12,600,000.00 USD | 10,280.00 USD | 15,600.00 USD | 154.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 9,280,000.00 USD | 9,280,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 12,570,000.00 USD | 12,570,000.00 USD | 48,670.00 USD | 0.00 USD | 118.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 9,190,000.00 USD | 9,190,000.00 USD | 23,540.00 USD | 20,070.00 USD | 191.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 9,150,000.00 USD | 9,150,000.00 USD | 1,960.00 USD | 5,150.00 USD | 451.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 12,510,000.00 USD | 12,510,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 433,320.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 9,140,000.00 USD | 9,140,000.00 USD | 75,160.00 USD | 15,490.00 USD | 25,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.96` | 12,410,000.00 USD | 12,410,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 9,030,000.00 USD | 9,030,000.00 USD | 37,260.00 USD | 6,830.00 USD | 71,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 12,370,000.00 USD | 12,370,000.00 USD | 4,830.00 USD | 6,160.00 USD | 59,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,910,000.00 USD | 8,910,000.00 USD | 5,670.00 USD | 4,500.00 USD | 64,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 12,300,000.00 USD | 12,300,000.00 USD | 641.95 USD | 7,630.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,840,000.00 USD | 8,840,000.00 USD | 17,880.00 USD | 19,650.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 12,280,000.00 USD | 12,280,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,780,000.00 USD | 8,780,000.00 USD | 18,000.00 USD | 4,820.00 USD | 179.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 12,270,000.00 USD | 12,270,000.00 USD | 7,200.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 774,770.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,760,000.00 USD | 8,760,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.06` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 83,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 8,680,000.00 USD | 8,680,000.00 USD | 167,250.00 USD | 701.42 USD | 76,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 12,180,000.00 USD | 12,180,000.00 USD | 218,980.00 USD | 351.10 USD | 110,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 8,440,000.00 USD | 8,440,000.00 USD | 7,570.00 USD | 42,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 11,850,000.00 USD | 11,850,000.00 USD | 6,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 8,390,000.00 USD | 8,390,000.00 USD | 1,150.00 USD | 20,910.00 USD | 260.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 11,840,000.00 USD | 11,840,000.00 USD | 10,140.00 USD | 559.40 USD | 55,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 8,360,000.00 USD | 8,360,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 11,770,000.00 USD | 11,770,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 71,300.00 USD | 258,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 8,300,000.00 USD | 8,300,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.16` | 11,450,000.00 USD | 11,450,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 8,180,000.00 USD | 8,180,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 11,410,000.00 USD | 11,410,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,910,000.00 USD | 7,910,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 11,270,000.00 USD | 11,270,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 7,430,000.00 USD | 7,430,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 10,750,000.00 USD | 10,750,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 7,030,000.00 USD | 7,030,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 10,210,000.00 USD | 10,210,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 34,240.00 USD | 187,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,840,000.00 USD | 6,840,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 9,770,000.00 USD | 9,770,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 6,670,000.00 USD | 6,670,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 9,380,000.00 USD | 9,380,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 6,320,000.00 USD | 6,320,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 9,050,000.00 USD | 9,050,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 6,090,000.00 USD | 6,090,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 8,590,000.00 USD | 8,590,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 6,010,000.00 USD | 6,010,000.00 USD | 66,410.00 USD | 9,100.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 8,450,000.00 USD | 8,450,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 138,450.00 USD | 152,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,850,000.00 USD | 5,850,000.00 USD | 6,270.00 USD | 3,580.00 USD | 173.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 8,390,000.00 USD | 8,390,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,840,000.00 USD | 5,840,000.00 USD | 42,350.00 USD | 45,170.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 7,990,000.00 USD | 7,990,000.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,740,000.00 USD | 5,740,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 7,980,000.00 USD | 7,980,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 5,560,000.00 USD | 5,560,000.00 USD | 244,890.00 USD | 0.00 USD | 150.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 7,630,000.00 USD | 7,630,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 5,310,000.00 USD | 5,310,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 7,300,000.00 USD | 7,300,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 10,350.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,780,000.00 USD | 4,780,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 6,520,000.00 USD | 6,520,000.00 USD | 323,570.00 USD | 103,810.00 USD | 236.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 4,450,000.00 USD | 4,450,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 6,090,000.00 USD | 6,090,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 4,340,000.00 USD | 4,340,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 5,880,000.00 USD | 5,880,000.00 USD | 4,770.00 USD | 52,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 4,270,000.00 USD | 4,270,000.00 USD | 1,200.00 USD | 12,710.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 5,820,000.00 USD | 5,820,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 4,210,000.00 USD | 4,210,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 4,100.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,970,000.00 USD | 3,970,000.00 USD | 110,630.00 USD | 38,520.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 5,730,000.00 USD | 5,730,000.00 USD | 122,960.00 USD | 81,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,790,000.00 USD | 3,790,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 5,530,000.00 USD | 5,530,000.00 USD | 23,530.00 USD | 0.00 USD | 224.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,680,000.00 USD | 3,680,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 24,130.00 USD | 122.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 3,640,000.00 USD | 3,640,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 5,480,000.00 USD | 5,480,000.00 USD | 99,990.00 USD | 0.00 USD | 316.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 3,450,000.00 USD | 3,450,000.00 USD | 109,830.00 USD | 9,030.00 USD | 68,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 5,380,000.00 USD | 5,380,000.00 USD | 11,150.00 USD | 0.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 3,260,000.00 USD | 3,260,000.00 USD | 59,930.00 USD | 10,380.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 5,340,000.00 USD | 5,340,000.00 USD | 9,470.00 USD | 19,620.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 3,150,000.00 USD | 3,150,000.00 USD | 67,250.00 USD | 37,570.00 USD | 70,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 5,290,000.00 USD | 5,290,000.00 USD | 16,330.00 USD | 27,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,980,000.00 USD | 2,980,000.00 USD | 12,670.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 15,010.00 USD | 170.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,940,000.00 USD | 2,940,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 5,230,000.00 USD | 5,230,000.00 USD | 433,250.00 USD | 73,710.00 USD | 200.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,730,000.00 USD | 2,730,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 877.75 USD | 100,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,620,000.00 USD | 2,620,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 4,630,000.00 USD | 4,630,000.00 USD | 16,310.00 USD | 120,930.00 USD | 73.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 2,440,000.00 USD | 2,440,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 4,490,000.00 USD | 4,490,000.00 USD | 535,020.00 USD | 46,010.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,990,000.00 USD | 1,990,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 3,800,000.00 USD | 3,800,000.00 USD | 69,540.00 USD | 70,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,880,000.00 USD | 1,880,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 104,870.00 USD | 207,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,720,000.00 USD | 1,720,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 3,350,000.00 USD | 3,350,000.00 USD | 377,580.00 USD | 80,420.00 USD | 195,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.86` | 1,270,000.00 USD | 1,270,000.00 USD | 203,140.00 USD | 34,420.00 USD | 238,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 2,700,000.00 USD | 2,700,000.00 USD | 323,850.00 USD | 3,610.00 USD | 391,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 790,700.00 USD | 790,700.00 USD | 61,520.00 USD | 15,230.00 USD | 67,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 1,980,000.00 USD | 1,980,000.00 USD | 111,430.00 USD | 78,360.00 USD | 384,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 646,940.00 USD | 646,940.00 USD | 114,210.00 USD | 53,630.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 1,410,000.00 USD | 1,410,000.00 USD | 32,650.00 USD | 49,530.00 USD | 220,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 411,350.00 USD | 411,350.00 USD | 138,180.00 USD | 33,800.00 USD | 45.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 1,100,000.00 USD | 1,100,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 239,320.00 USD | 239,320.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 765,160.00 USD | 765,160.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.96` | 233,400.00 USD | 233,400.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 762,690.00 USD | 762,690.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 701,680.00 USD | 701,680.00 USD | 17,930.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 145,640.00 USD | 145,640.00 USD | 0.00 USD | 0.00 USD | 128.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 474,460.00 USD | 474,460.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 463,630.00 USD | 463,630.00 USD | 0.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 145,510.00 USD | 145,510.00 USD | 0.00 USD | 2,200.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 320,590.00 USD | 320,590.00 USD | 0.00 USD | 0.00 USD | 178,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 142,310.00 USD | 142,310.00 USD | 0.00 USD | 0.00 USD | 133,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 143,210.00 USD | 143,210.00 USD | 0.00 USD | 0.00 USD | 160.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 9,240.00 USD | 9,240.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 143,050.00 USD | 143,050.00 USD | 4,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 6,920.00 USD | 6,920.00 USD | 0.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 138,530.00 USD | 138,530.00 USD | 0.00 USD | 2,260.00 USD | 136,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.12` | 113,660.00 USD | 113,660.00 USD | 0.00 USD | 5,170.00 USD | 108,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.12` | 227,320.00 USD | 227,320.00 USD | 0.00 USD | 5,170.00 USD | 108,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 68,100.00 USD | 68,100.00 USD | 0.00 USD | 0.00 USD | 68,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 237,790.00 USD | 237,790.00 USD | 0.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 247,690.00 USD | 247,690.00 USD | 127,020.00 USD | 2,100.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.16` | 376,820.00 USD | 376,820.00 USD | 838.30 USD | 72,860.00 USD | 65,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 420,180.00 USD | 420,180.00 USD | 71,610.00 USD | 14,380.00 USD | 86,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 394,320.00 USD | 394,320.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 673,930.00 USD | 673,930.00 USD | 76,580.00 USD | 85,800.00 USD | 91,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 734,670.00 USD | 734,670.00 USD | 171,840.00 USD | 89,800.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,240,000.00 USD | 1,240,000.00 USD | 344,290.00 USD | 76,600.00 USD | 142,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 1,260,000.00 USD | 1,260,000.00 USD | 482,460.00 USD | 42,050.00 USD | 603.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 1,610,000.00 USD | 1,610,000.00 USD | 163,340.00 USD | 58,590.00 USD | 155,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 1,620,000.00 USD | 1,620,000.00 USD | 231,960.00 USD | 59,950.00 USD | 72,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 1,890,000.00 USD | 1,890,000.00 USD | 154,720.00 USD | 54,310.00 USD | 71,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.26` | 2,490,000.00 USD | 2,490,000.00 USD | 520,990.00 USD | 48,250.00 USD | 295,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 2,610,000.00 USD | 2,610,000.00 USD | 388,220.00 USD | 67,290.00 USD | 263,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 3,120,000.00 USD | 3,120,000.00 USD | 429,350.00 USD | 57,050.00 USD | 147,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,130,000.00 USD | 3,130,000.00 USD | 261,740.00 USD | 81,010.00 USD | 178,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 3,260,000.00 USD | 3,260,000.00 USD | 24,980.00 USD | 32,240.00 USD | 77,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 3,540,000.00 USD | 3,540,000.00 USD | 181,160.00 USD | 73,150.00 USD | 150,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 3,830,000.00 USD | 3,830,000.00 USD | 194,150.00 USD | 62,240.00 USD | 317,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,170,000.00 USD | 4,170,000.00 USD | 376,310.00 USD | 128,380.00 USD | 125,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 4,220,000.00 USD | 4,220,000.00 USD | 159,840.00 USD | 127,800.00 USD | 101,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,490,000.00 USD | 4,490,000.00 USD | 173,620.00 USD | 87,180.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.36` | 4,480,000.00 USD | 4,480,000.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 4,690,000.00 USD | 4,690,000.00 USD | 118,230.00 USD | 63,980.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 4,720,000.00 USD | 4,720,000.00 USD | 70,120.00 USD | 91,810.00 USD | 75,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 4,870,000.00 USD | 4,870,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 14,250.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,200,000.00 USD | 5,200,000.00 USD | 126,960.00 USD | 83,740.00 USD | 113,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 4,990,000.00 USD | 4,990,000.00 USD | 66,800.00 USD | 46,660.00 USD | 115,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,460,000.00 USD | 5,460,000.00 USD | 96,590.00 USD | 54,990.00 USD | 109,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 5,430,000.00 USD | 5,430,000.00 USD | 303,190.00 USD | 101,940.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 5,670,000.00 USD | 5,670,000.00 USD | 86,190.00 USD | 77,320.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.46` | 5,610,000.00 USD | 5,610,000.00 USD | 122,890.00 USD | 55,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 5,740,000.00 USD | 5,740,000.00 USD | 26,740.00 USD | 35,780.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 5,840,000.00 USD | 5,840,000.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 5,920,000.00 USD | 5,920,000.00 USD | 78,340.00 USD | 38,760.00 USD | 64,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 6,010,000.00 USD | 6,010,000.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,130,000.00 USD | 6,130,000.00 USD | 127,920.00 USD | 22,260.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 5,760.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,350,000.00 USD | 6,350,000.00 USD | 92,850.00 USD | 23,130.00 USD | 104,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 6,280,000.00 USD | 6,280,000.00 USD | 53,520.00 USD | 19,620.00 USD | 127,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 12,700.00 USD | 12,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,570,000.00 USD | 6,570,000.00 USD | 128,820.00 USD | 29,910.00 USD | 57,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 6,410,000.00 USD | 6,410,000.00 USD | 102,980.00 USD | 25,560.00 USD | 236.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,670,000.00 USD | 6,670,000.00 USD | 76,330.00 USD | 2,950.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 6,820,000.00 USD | 6,820,000.00 USD | 59,780.00 USD | 21,610.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 6,520,000.00 USD | 6,520,000.00 USD | 46,010.00 USD | 10,510.00 USD | 23,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 6,910,000.00 USD | 6,910,000.00 USD | 45,260.00 USD | 512.95 USD | 48,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 6,580,000.00 USD | 6,580,000.00 USD | 65,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 6,950,000.00 USD | 6,950,000.00 USD | 5,660.00 USD | 7,410.00 USD | 31,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 6,620,000.00 USD | 6,620,000.00 USD | 39,380.00 USD | 1,790.00 USD | 321.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 6,220.00 USD | 19,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.66` | 6,990,000.00 USD | 6,990,000.00 USD | 1,070.00 USD | 12,290.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,190,000.00 USD | 7,190,000.00 USD | 127,580.00 USD | 35,770.00 USD | 31,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 6,820,000.00 USD | 6,820,000.00 USD | 1,280.00 USD | 20,730.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,210,000.00 USD | 7,210,000.00 USD | 239.66 USD | 4,760.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 6,860,000.00 USD | 6,860,000.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,420,000.00 USD | 7,420,000.00 USD | 91,840.00 USD | 17,160.00 USD | 98,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 7,190,000.00 USD | 7,190,000.00 USD | 209,440.00 USD | 0.00 USD | 116,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,600,000.00 USD | 7,600,000.00 USD | 76,690.00 USD | 30,280.00 USD | 73,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 1,030.00 USD | 90,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,660,000.00 USD | 7,660,000.00 USD | 26,330.00 USD | 14,880.00 USD | 25,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 7,380,000.00 USD | 7,380,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 7,730,000.00 USD | 7,730,000.00 USD | 11,750.00 USD | 20,510.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 7,440,000.00 USD | 7,440,000.00 USD | 9,130.00 USD | 0.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 7,750,000.00 USD | 7,750,000.00 USD | 1,350.00 USD | 17,720.00 USD | 529.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 7,580,000.00 USD | 7,580,000.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 7,800,000.00 USD | 7,800,000.00 USD | 12,610.00 USD | 53.10 USD | 36,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 7,810,000.00 USD | 7,810,000.00 USD | 182,750.00 USD | 41,910.00 USD | 374.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 7,900,000.00 USD | 7,900,000.00 USD | 44,510.00 USD | 11,870.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 8,060,000.00 USD | 8,060,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 169.46 USD | 19,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 7,980,000.00 USD | 7,980,000.00 USD | 11,490.00 USD | 12,970.00 USD | 51,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 8,070,000.00 USD | 8,070,000.00 USD | 962.44 USD | 6,180.00 USD | 42.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,090,000.00 USD | 8,090,000.00 USD | 21,500.00 USD | 28,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 8,130,000.00 USD | 8,130,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,170,000.00 USD | 8,170,000.00 USD | 43,700.00 USD | 8,690.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 8,190,000.00 USD | 8,190,000.00 USD | 40,470.00 USD | 14,650.00 USD | 145.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,440,000.00 USD | 8,440,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 8,400,000.00 USD | 8,400,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,550,000.00 USD | 8,550,000.00 USD | 48,030.00 USD | 15,260.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 8,590,000.00 USD | 8,590,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 19,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,700,000.00 USD | 8,700,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 8,760,000.00 USD | 8,760,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 8,860,000.00 USD | 8,860,000.00 USD | 59,940.00 USD | 29,050.00 USD | 68,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 9,420,000.00 USD | 9,420,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,020,000.00 USD | 9,020,000.00 USD | 102,680.00 USD | 23,880.00 USD | 36,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 10,060,000.00 USD | 10,060,000.00 USD | 379,630.00 USD | 31,630.00 USD | 222,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,070,000.00 USD | 9,070,000.00 USD | 13,680.00 USD | 7,110.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 10,630,000.00 USD | 10,630,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,230,000.00 USD | 9,230,000.00 USD | 77,630.00 USD | 36,810.00 USD | 46,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 11,250,000.00 USD | 11,250,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,390,000.00 USD | 9,390,000.00 USD | 76,750.00 USD | 28,460.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 11,760,000.00 USD | 11,760,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,520,000.00 USD | 9,520,000.00 USD | 43,090.00 USD | 35,930.00 USD | 50,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 12,420,000.00 USD | 12,420,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 9,630,000.00 USD | 9,630,000.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 12,600,000.00 USD | 12,600,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 9,850,000.00 USD | 9,850,000.00 USD | 116,870.00 USD | 54,580.00 USD | 50,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 12,990,000.00 USD | 12,990,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,020,000.00 USD | 10,020,000.00 USD | 75,170.00 USD | 37,540.00 USD | 55,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 13,360,000.00 USD | 13,360,000.00 USD | 148,090.00 USD | 102,170.00 USD | 118,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,250,000.00 USD | 10,250,000.00 USD | 131,220.00 USD | 34,710.00 USD | 67,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 13,680,000.00 USD | 13,680,000.00 USD | 182,020.00 USD | 69,310.00 USD | 75,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,470,000.00 USD | 10,470,000.00 USD | 112,670.00 USD | 48,310.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 13,860,000.00 USD | 13,860,000.00 USD | 74,850.00 USD | 54,220.00 USD | 43,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,630,000.00 USD | 10,630,000.00 USD | 77,250.00 USD | 43,870.00 USD | 45,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 14,180,000.00 USD | 14,180,000.00 USD | 194,760.00 USD | 57,500.00 USD | 75,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 10,700,000.00 USD | 10,700,000.00 USD | 10,510.00 USD | 21,000.00 USD | 36,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 14,570,000.00 USD | 14,570,000.00 USD | 262,140.00 USD | 63,820.00 USD | 64,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 10,740,000.00 USD | 10,740,000.00 USD | 14,540.00 USD | 15,320.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 14,680,000.00 USD | 14,680,000.00 USD | 50,300.00 USD | 45,440.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 5,060.00 USD | 24,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 10,780,000.00 USD | 10,780,000.00 USD | 12,590.00 USD | 12,870.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 14,860,000.00 USD | 14,860,000.00 USD | 73,660.00 USD | 54,120.00 USD | 50,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 10,840,000.00 USD | 10,840,000.00 USD | 49,100.00 USD | 7,490.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 15,130,000.00 USD | 15,130,000.00 USD | 156,680.00 USD | 27,340.00 USD | 90,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 15,250,000.00 USD | 15,250,000.00 USD | 70,240.00 USD | 24,020.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 15,320,000.00 USD | 15,320,000.00 USD | 22,620.00 USD | 25,760.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 15,380,000.00 USD | 15,380,000.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 25,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 15,450,000.00 USD | 15,450,000.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 15,460,000.00 USD | 15,460,000.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `9.32` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,650.00 USD |
| `7D` | `9.34` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,820.00 USD |
| `7D` | `9.36` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,360.00 USD |
| `7D` | `9.40` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,040.00 USD |
| `7D` | `9.42` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,840.00 USD |
| `7D` | `9.44` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,160.00 USD |
| `7D` | `9.46` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 94,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.48` | 13,440,000.00 USD | 0.00 USD | 13,440,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 13,440,000.00 USD | 0.00 USD | 13,440,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD |
| `7D` | `9.52` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD |
| `7D` | `9.54` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 136.92 USD | 12,570.00 USD | 10.22 USD |
| `7D` | `9.56` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD |
| `7D` | `9.58` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 38,760.00 USD | 722.15 USD | 20.74 USD |
| `7D` | `9.60` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD |
| `7D` | `9.62` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 659.88 USD |
| `7D` | `9.64` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 8,500.00 USD | 0.00 USD | 186.31 USD |
| `7D` | `9.66` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 7,370.00 USD | 0.00 USD | 413.42 USD |
| `7D` | `9.68` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.70` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 12,980,000.00 USD | 0.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD |
| `7D` | `9.74` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD |
| `7D` | `9.76` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 50,080.00 USD | 0.00 USD | 27,020.00 USD |
| `7D` | `9.78` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.80` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 47,490.00 USD | 14,120.00 USD | 25,670.00 USD |
| `7D` | `9.82` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 84,900.00 USD | 10,390.00 USD | 863.01 USD |
| `7D` | `9.84` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD |
| `1D` | `9.86` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 29,590.00 USD | 11,120.00 USD | 10,600.00 USD |
| `7D` | `9.86` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD |
| `1D` | `9.88` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,150.00 USD |
| `7D` | `9.88` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 10,280.00 USD | 15,600.00 USD | 154.66 USD |
| `1D` | `9.90` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,510.00 USD |
| `7D` | `9.90` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 48,670.00 USD | 0.00 USD | 118.03 USD |
| `1D` | `9.92` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 23,540.00 USD | 20,070.00 USD | 191.80 USD |
| `7D` | `9.92` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD |
| `1D` | `9.94` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 1,960.00 USD | 5,150.00 USD | 451.73 USD |
| `7D` | `9.94` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,490.00 USD |
| `1D` | `9.96` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 75,160.00 USD | 15,490.00 USD | 25,940.00 USD |
| `7D` | `9.96` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,480.00 USD |
| `1D` | `9.98` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 37,260.00 USD | 6,830.00 USD | 71,890.00 USD |
| `7D` | `9.98` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 4,830.00 USD | 6,160.00 USD | 59,600.00 USD |
| `1D` | `10.00` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 5,670.00 USD | 4,500.00 USD | 64,350.00 USD |
| `7D` | `10.00` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 641.95 USD | 7,630.00 USD | 13,000.00 USD |
| `1D` | `10.02` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 17,880.00 USD | 19,650.00 USD | 18,770.00 USD |
| `7D` | `10.02` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD |
| `1D` | `10.04` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 18,000.00 USD | 4,820.00 USD | 179.68 USD |
| `7D` | `10.04` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 7,200.00 USD | 1,210.00 USD | 0.00 USD |
| `1D` | `10.06` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,230.00 USD |
| `7D` | `10.06` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 83,170.00 USD |
| `1D` | `10.08` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 167,250.00 USD | 701.42 USD | 76,090.00 USD |
| `7D` | `10.08` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 218,980.00 USD | 351.10 USD | 110,850.00 USD |
| `1D` | `10.10` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 7,570.00 USD | 42,810.00 USD | 0.00 USD |
| `7D` | `10.10` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 6,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.12` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 1,150.00 USD | 20,910.00 USD | 260.68 USD |
| `7D` | `10.12` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 10,140.00 USD | 559.40 USD | 55,920.00 USD |
| `1D` | `10.14` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,630.00 USD |
| `7D` | `10.14` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,470.00 USD |
| `1D` | `10.16` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,420.00 USD |
| `7D` | `10.16` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,740.00 USD |
| `1D` | `10.18` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,030.00 USD |
| `7D` | `10.18` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,410.00 USD |
| `1D` | `10.20` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,250.00 USD |
| `7D` | `10.20` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD |
| `1D` | `10.22` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,860.00 USD |
| `7D` | `10.22` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,030.00 USD |
| `1D` | `10.24` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,420.00 USD |
| `7D` | `10.24` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,040.00 USD |
| `1D` | `10.26` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,840.00 USD |
| `7D` | `10.26` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,590.00 USD |
| `1D` | `10.28` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,230.00 USD |
| `7D` | `10.28` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.30` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,820.00 USD |
| `7D` | `10.30` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,670.00 USD |
| `7D` | `10.32` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 66,410.00 USD | 9,100.00 USD | 85,980.00 USD |
| `7D` | `10.34` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.36` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 6,270.00 USD | 3,580.00 USD | 173.73 USD |
| `7D` | `10.36` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.38` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 42,350.00 USD | 45,170.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,800.00 USD |
| `7D` | `10.40` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 244,890.00 USD | 0.00 USD | 150.73 USD |
| `7D` | `10.42` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD |
| `1D` | `10.44` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,420.00 USD |
| `7D` | `10.44` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,140.00 USD |
| `7D` | `10.46` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 323,570.00 USD | 103,810.00 USD | 236.06 USD |
| `1D` | `10.48` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,370.00 USD |
| `7D` | `10.48` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,160.00 USD |
| `7D` | `10.50` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 4,770.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.52` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 1,200.00 USD | 12,710.00 USD | 38,170.00 USD |
| `7D` | `10.52` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,350.00 USD |
| `7D` | `10.54` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 110,630.00 USD | 38,520.00 USD | 37,770.00 USD |
| `7D` | `10.56` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 122,960.00 USD | 81,670.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,040.00 USD |
| `7D` | `10.58` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 23,530.00 USD | 0.00 USD | 224.70 USD |
| `1D` | `10.60` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,900.00 USD |
| `7D` | `10.60` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 0.00 USD | 24,130.00 USD | 122.40 USD |
| `1D` | `10.62` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,080.00 USD |
| `7D` | `10.62` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 99,990.00 USD | 0.00 USD | 316.83 USD |
| `1D` | `10.64` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 109,830.00 USD | 9,030.00 USD | 68,860.00 USD |
| `7D` | `10.64` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 11,150.00 USD | 0.00 USD | 28,990.00 USD |
| `1D` | `10.66` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 59,930.00 USD | 10,380.00 USD | 33,460.00 USD |
| `7D` | `10.66` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 9,470.00 USD | 19,620.00 USD | 18,990.00 USD |
| `1D` | `10.68` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 67,250.00 USD | 37,570.00 USD | 70,090.00 USD |
| `7D` | `10.68` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 16,330.00 USD | 27,190.00 USD | 0.00 USD |
| `1D` | `10.70` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 12,670.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `10.70` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 0.00 USD | 15,010.00 USD | 170.38 USD |
| `1D` | `10.72` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.72` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 433,250.00 USD | 73,710.00 USD | 200.04 USD |
| `1D` | `10.74` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.74` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 877.75 USD | 100,160.00 USD |
| `1D` | `10.76` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD |
| `7D` | `10.76` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 16,310.00 USD | 120,930.00 USD | 73.58 USD |
| `1D` | `10.78` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,570.00 USD |
| `7D` | `10.78` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 535,020.00 USD | 46,010.00 USD | 103,760.00 USD |
| `1D` | `10.80` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,970.00 USD |
| `7D` | `10.80` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 69,540.00 USD | 70,260.00 USD | 0.00 USD |
| `1D` | `10.82` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD |
| `7D` | `10.82` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 104,870.00 USD | 207,000.00 USD |
| `1D` | `10.84` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,650.00 USD |
| `7D` | `10.84` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 377,580.00 USD | 80,420.00 USD | 195,630.00 USD |
| `1D` | `10.86` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 203,140.00 USD | 34,420.00 USD | 238,460.00 USD |
| `7D` | `10.86` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 323,850.00 USD | 3,610.00 USD | 391,430.00 USD |
| `1D` | `10.88` | 790,700.00 USD | 0.00 USD | 790,700.00 USD | 61,520.00 USD | 15,230.00 USD | 67,010.00 USD |
| `7D` | `10.88` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 111,430.00 USD | 78,360.00 USD | 384,460.00 USD |
| `1D` | `10.90` | 646,940.00 USD | 0.00 USD | 646,940.00 USD | 114,210.00 USD | 53,630.00 USD | 67,740.00 USD |
| `7D` | `10.90` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 32,650.00 USD | 49,530.00 USD | 220,890.00 USD |
| `1D` | `10.92` | 411,350.00 USD | 0.00 USD | 411,350.00 USD | 138,180.00 USD | 33,800.00 USD | 45.61 USD |
| `7D` | `10.92` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD |
| `1D` | `10.94` | 239,320.00 USD | 0.00 USD | 239,320.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.94` | 765,160.00 USD | 0.00 USD | 765,160.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 233,400.00 USD | 0.00 USD | 233,400.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `10.96` | 762,690.00 USD | 0.00 USD | 762,690.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD |
| `7D` | `10.98` | 701,680.00 USD | 0.00 USD | 701,680.00 USD | 17,930.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 145,640.00 USD | 0.00 USD | 145,640.00 USD | 0.00 USD | 0.00 USD | 128.20 USD |
| `7D` | `11.00` | 474,460.00 USD | 0.00 USD | 474,460.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.02` | 463,630.00 USD | 0.00 USD | 463,630.00 USD | 0.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.04` | 145,510.00 USD | 0.00 USD | 145,510.00 USD | 0.00 USD | 2,200.00 USD | 103.72 USD |
| `7D` | `11.04` | 320,590.00 USD | 0.00 USD | 320,590.00 USD | 0.00 USD | 0.00 USD | 178,290.00 USD |
| `7D` | `11.06` | 142,310.00 USD | 0.00 USD | 142,310.00 USD | 0.00 USD | 0.00 USD | 133,070.00 USD |
| `1D` | `11.08` | 143,210.00 USD | 0.00 USD | 143,210.00 USD | 0.00 USD | 0.00 USD | 160.30 USD |
| `7D` | `11.08` | 9,240.00 USD | 0.00 USD | 9,240.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.10` | 143,050.00 USD | 0.00 USD | 143,050.00 USD | 4,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.10` | 6,920.00 USD | 0.00 USD | 6,920.00 USD | 0.00 USD | 6,920.00 USD | 0.00 USD |
| `1D` | `11.12` | 138,530.00 USD | 0.00 USD | 138,530.00 USD | 0.00 USD | 2,260.00 USD | 136,280.00 USD |
| `7D` | `11.12` | 113,660.00 USD | 113,660.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | 108,490.00 USD |
| `7D` | `11.12` | 227,320.00 USD | 227,320.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | 108,490.00 USD |
| `1D` | `11.13` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.14` | 68,100.00 USD | 68,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 68,100.00 USD |
| `7D` | `11.14` | 237,790.00 USD | 237,790.00 USD | 0.00 USD | 0.00 USD | 9,980.00 USD | 487.81 USD |
| `1D` | `11.16` | 247,690.00 USD | 247,690.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,490.00 USD |
| `7D` | `11.16` | 376,820.00 USD | 376,820.00 USD | 0.00 USD | 838.30 USD | 72,860.00 USD | 65,340.00 USD |
| `1D` | `11.18` | 420,180.00 USD | 420,180.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,500.00 USD |
| `7D` | `11.18` | 394,320.00 USD | 394,320.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD |
| `1D` | `11.20` | 673,930.00 USD | 673,930.00 USD | 0.00 USD | 76,580.00 USD | 85,800.00 USD | 91,370.00 USD |
| `7D` | `11.20` | 734,670.00 USD | 734,670.00 USD | 0.00 USD | 171,840.00 USD | 89,800.00 USD | 78,710.00 USD |
| `1D` | `11.22` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 344,290.00 USD | 76,600.00 USD | 142,250.00 USD |
| `7D` | `11.22` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 482,460.00 USD | 42,050.00 USD | 603.14 USD |
| `1D` | `11.24` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 163,340.00 USD | 58,590.00 USD | 155,220.00 USD |
| `7D` | `11.24` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 231,960.00 USD | 59,950.00 USD | 72,200.00 USD |
| `1D` | `11.26` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 154,720.00 USD | 54,310.00 USD | 71,610.00 USD |
| `7D` | `11.26` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 520,990.00 USD | 48,250.00 USD | 295,640.00 USD |
| `1D` | `11.28` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 388,220.00 USD | 67,290.00 USD | 263,100.00 USD |
| `7D` | `11.28` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 429,350.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.30` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 261,740.00 USD | 81,010.00 USD | 178,650.00 USD |
| `7D` | `11.30` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 77,260.00 USD |
| `1D` | `11.32` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 181,160.00 USD | 73,150.00 USD | 150,130.00 USD |
| `7D` | `11.32` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 194,150.00 USD | 62,240.00 USD | 317,340.00 USD |
| `1D` | `11.34` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 376,310.00 USD | 128,380.00 USD | 125,830.00 USD |
| `7D` | `11.34` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 159,840.00 USD | 127,800.00 USD | 101,680.00 USD |
| `1D` | `11.36` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 173,620.00 USD | 87,180.00 USD | 56,350.00 USD |
| `7D` | `11.36` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 118,230.00 USD | 63,980.00 USD | 25,400.00 USD |
| `7D` | `11.38` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,020.00 USD |
| `1D` | `11.40` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD |
| `7D` | `11.40` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 29,200.00 USD |
| `1D` | `11.42` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 126,960.00 USD | 83,740.00 USD | 113,310.00 USD |
| `7D` | `11.42` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 66,800.00 USD | 46,660.00 USD | 115,280.00 USD |
| `1D` | `11.44` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 96,590.00 USD | 54,990.00 USD | 109,240.00 USD |
| `7D` | `11.44` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 303,190.00 USD | 101,940.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 86,190.00 USD | 77,320.00 USD | 50,810.00 USD |
| `7D` | `11.46` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 122,890.00 USD | 55,470.00 USD | 0.00 USD |
| `1D` | `11.48` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 26,740.00 USD | 35,780.00 USD | 2,090.00 USD |
| `7D` | `11.48` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD |
| `1D` | `11.50` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 78,340.00 USD | 38,760.00 USD | 64,020.00 USD |
| `7D` | `11.50` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 127,920.00 USD | 22,260.00 USD | 64,320.00 USD |
| `7D` | `11.52` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 62,500.00 USD |
| `1D` | `11.54` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 92,850.00 USD | 23,130.00 USD | 104,540.00 USD |
| `7D` | `11.54` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 53,520.00 USD | 19,620.00 USD | 127,210.00 USD |
| `1D` | `11.56` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 128,820.00 USD | 29,910.00 USD | 57,180.00 USD |
| `7D` | `11.56` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 102,980.00 USD | 25,560.00 USD | 236.06 USD |
| `1D` | `11.58` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 76,330.00 USD | 2,950.00 USD | 17,870.00 USD |
| `7D` | `11.58` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 59,780.00 USD | 21,610.00 USD | 67,860.00 USD |
| `7D` | `11.60` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 46,010.00 USD | 10,510.00 USD | 23,230.00 USD |
| `1D` | `11.62` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 45,260.00 USD | 512.95 USD | 48,010.00 USD |
| `7D` | `11.62` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.64` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 5,660.00 USD | 7,410.00 USD | 31,250.00 USD |
| `7D` | `11.64` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 321.06 USD |
| `1D` | `11.66` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 1,070.00 USD | 12,290.00 USD | 25,650.00 USD |
| `7D` | `11.66` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.68` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 127,580.00 USD | 35,770.00 USD | 31,850.00 USD |
| `7D` | `11.68` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 1,280.00 USD | 20,730.00 USD | 71,150.00 USD |
| `1D` | `11.70` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,440.00 USD |
| `7D` | `11.70` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD |
| `1D` | `11.72` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 91,840.00 USD | 17,160.00 USD | 98,100.00 USD |
| `7D` | `11.72` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,320.00 USD |
| `1D` | `11.74` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 76,690.00 USD | 30,280.00 USD | 73,120.00 USD |
| `7D` | `11.74` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,190.00 USD |
| `1D` | `11.76` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 26,330.00 USD | 14,880.00 USD | 25,150.00 USD |
| `7D` | `11.76` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,810.00 USD |
| `1D` | `11.78` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 11,750.00 USD | 20,510.00 USD | 40,130.00 USD |
| `7D` | `11.78` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 9,130.00 USD | 0.00 USD | 56,750.00 USD |
| `1D` | `11.80` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 1,350.00 USD | 17,720.00 USD | 529.56 USD |
| `7D` | `11.80` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 12,610.00 USD | 53.10 USD | 36,160.00 USD |
| `7D` | `11.82` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 182,750.00 USD | 41,910.00 USD | 374.05 USD |
| `1D` | `11.84` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 44,510.00 USD | 11,870.00 USD | 41,170.00 USD |
| `7D` | `11.84` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,490.00 USD |
| `1D` | `11.86` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 11,490.00 USD | 12,970.00 USD | 51,050.00 USD |
| `7D` | `11.86` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 962.44 USD | 6,180.00 USD | 42.92 USD |
| `1D` | `11.88` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 21,500.00 USD | 28,990.00 USD | 60,210.00 USD |
| `7D` | `11.88` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,960.00 USD |
| `1D` | `11.90` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 27,960.00 USD |
| `7D` | `11.90` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 145.40 USD |
| `1D` | `11.92` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,040.00 USD |
| `7D` | `11.92` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,470.00 USD |
| `1D` | `11.94` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 48,030.00 USD | 15,260.00 USD | 40,150.00 USD |
| `7D` | `11.94` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,450.00 USD |
| `1D` | `11.96` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,360.00 USD |
| `7D` | `11.96` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,230.00 USD |
| `1D` | `11.98` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 59,940.00 USD | 29,050.00 USD | 68,160.00 USD |
| `7D` | `11.98` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,700.00 USD |
| `1D` | `12.00` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 102,680.00 USD | 23,880.00 USD | 36,240.00 USD |
| `7D` | `12.00` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,030.00 USD |
| `1D` | `12.02` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 13,680.00 USD | 7,110.00 USD | 31,500.00 USD |
| `7D` | `12.02` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,760.00 USD |
| `1D` | `12.04` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 77,630.00 USD | 36,810.00 USD | 46,050.00 USD |
| `7D` | `12.04` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,710.00 USD |
| `1D` | `12.06` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 76,750.00 USD | 28,460.00 USD | 52,300.00 USD |
| `7D` | `12.06` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,610.00 USD |
| `1D` | `12.08` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 43,090.00 USD | 35,930.00 USD | 50,030.00 USD |
| `7D` | `12.08` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,370.00 USD |
| `1D` | `12.10` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD |
| `7D` | `12.10` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,280.00 USD |
| `1D` | `12.12` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 116,870.00 USD | 54,580.00 USD | 50,430.00 USD |
| `7D` | `12.12` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,930.00 USD |
| `1D` | `12.14` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 75,170.00 USD | 37,540.00 USD | 55,760.00 USD |
| `7D` | `12.14` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 148,090.00 USD | 102,170.00 USD | 118,890.00 USD |
| `1D` | `12.16` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 131,220.00 USD | 34,710.00 USD | 67,880.00 USD |
| `7D` | `12.16` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 182,020.00 USD | 69,310.00 USD | 75,270.00 USD |
| `1D` | `12.18` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 112,670.00 USD | 48,310.00 USD | 50,560.00 USD |
| `7D` | `12.18` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 74,850.00 USD | 54,220.00 USD | 43,350.00 USD |
| `1D` | `12.20` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 77,250.00 USD | 43,870.00 USD | 45,690.00 USD |
| `7D` | `12.20` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 194,760.00 USD | 57,500.00 USD | 75,350.00 USD |
| `1D` | `12.22` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 10,510.00 USD | 21,000.00 USD | 36,050.00 USD |
| `7D` | `12.22` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 262,140.00 USD | 63,820.00 USD | 64,700.00 USD |
| `1D` | `12.24` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 14,540.00 USD | 15,320.00 USD | 7,630.00 USD |
| `7D` | `12.24` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 50,300.00 USD | 45,440.00 USD | 10,250.00 USD |
| `1D` | `12.26` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 12,590.00 USD | 12,870.00 USD | 12,140.00 USD |
| `7D` | `12.26` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 73,660.00 USD | 54,120.00 USD | 50,860.00 USD |
| `1D` | `12.28` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 49,100.00 USD | 7,490.00 USD | 12,080.00 USD |
| `7D` | `12.28` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 156,680.00 USD | 27,340.00 USD | 90,300.00 USD |
| `1D` | `12.29` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD |
| `7D` | `12.30` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 70,240.00 USD | 24,020.00 USD | 23,300.00 USD |
| `7D` | `12.32` | 15,320,000.00 USD | 15,320,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 17,980.00 USD |
| `7D` | `12.34` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD |
| `7D` | `12.36` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD |
| `7D` | `12.38` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `511.20M` | Total OI Tokens: `46,049,801.7 LINK`
  * 1h OI Change: `+0.54%` | 4h OI Change: `-1.53%` | 24h OI Change: `-7.33%`
  * Exchange Breakdown: Binance=`100.52M` | Bybit=`69.06M` | OKX=`27.06M` | Hyperliquid=`55.95M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.02K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0084%` |
| **USDT Bybit** | `-0.0008%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0021%` | **USDT Bitget** | `0.0053%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `51.66%` | `48.34%` | `1.07` | 7,680,000.00 USD |
| `15M` | `Binance` | `58.14%` | `41.86%` | `1.39` | 2,340,000.00 USD |
| `15M` | `OKX` | `46.04%` | `53.96%` | `0.85` | 838,580.00 USD |
| `15M` | `Bybit` | `49.28%` | `50.72%` | `0.97` | 1,230,000.00 USD |
| `15M` | `KuCoin` | `44.16%` | `55.84%` | `0.79` | 218,910.00 USD |
| `15M` | `Gate` | `57.23%` | `42.77%` | `1.34` | 155,030.00 USD |
| `15M` | `Bitget` | `68.43%` | `31.57%` | `2.17` | 254,130.00 USD |
| `15M` | `BingX` | `12.56%` | `87.44%` | `0.14` | 101,480.00 USD |
| `15M` | `MEXC` | `26.13%` | `73.87%` | `0.35` | 95,800.00 USD |
| `15M` | `Bitunix` | `48.29%` | `51.71%` | `0.93` | 139,930.00 USD |
| `15M` | `Hyperliquid` | `29.52%` | `70.48%` | `0.42` | 152,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.78%` | `50.22%` | `0.99` | 85,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `50.86%` | `49.14%` | `1.04` | 1,960,000.00 USD |
| `15M` | `HTX` | `52.82%` | `47.18%` | `1.12` | 16,810.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `86.36%` | `13.64%` | `6.33` | 21,900.00 USD |
| `15M` | `Aster` | `46.99%` | `53.01%` | `0.89` | 19,690.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.49%` | `43.51%` | `1.30` | 52,750.00 USD |
| `15M` | `Whale Positions` | `58.14%` | `41.86%` | `1.39` | 2,340,000.00 USD |
| `15M` | `Global Accounts` | `51.66%` | `48.34%` | `1.07` | 7,680,000.00 USD |
| `1H` | `LINK` | `49.12%` | `50.88%` | `0.97` | 25,000,000.00 USD |
| `1H` | `Binance` | `52.57%` | `47.43%` | `1.11` | 7,520,000.00 USD |
| `1H` | `OKX` | `63.29%` | `36.71%` | `1.72` | 2,480,000.00 USD |
| `1H` | `Bybit` | `53.32%` | `46.68%` | `1.14` | 2,770,000.00 USD |
| `1H` | `KuCoin` | `39.43%` | `60.57%` | `0.65` | 704,830.00 USD |
| `1H` | `Gate` | `63.28%` | `36.72%` | `1.72` | 1,000,000.00 USD |
| `1H` | `Bitget` | `54.83%` | `45.17%` | `1.21` | 588,420.00 USD |
| `1H` | `BingX` | `18.79%` | `81.21%` | `0.23` | 1,370,000.00 USD |
| `1H` | `MEXC` | `52.93%` | `47.07%` | `1.12` | 2,640,000.00 USD |
| `1H` | `Bitunix` | `64.05%` | `35.95%` | `1.78` | 546,760.00 USD |
| `1H` | `Hyperliquid` | `51.73%` | `48.27%` | `1.07` | 136,840.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.44%` | `52.56%` | `0.90` | 3,730,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,200,000.00 USD |
| `1H` | `HTX` | `44.97%` | `55.03%` | `0.82` | 52,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `71.08%` | `28.92%` | `2.46` | 237,990.00 USD |
| `1H` | `Aster` | `21.38%` | `78.62%` | `0.27` | 11,400.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.29%` | `53.71%` | `0.86` | 9,730.00 USD |
| `1H` | `Whale Positions` | `52.57%` | `47.43%` | `1.11` | 7,520,000.00 USD |
| `1H` | `Global Accounts` | `49.12%` | `50.88%` | `0.97` | 25,000,000.00 USD |
| `4H` | `LINK` | `47.41%` | `52.59%` | `0.90` | 77,470,000.00 USD |
| `4H` | `Binance` | `51.23%` | `48.77%` | `1.05` | 24,340,000.00 USD |
| `4H` | `OKX` | `55.3%` | `44.7%` | `1.24` | 6,460,000.00 USD |
| `4H` | `Bybit` | `52.63%` | `47.37%` | `1.11` | 6,980,000.00 USD |
| `4H` | `KuCoin` | `44.77%` | `55.23%` | `0.81` | 1,300,000.00 USD |
| `4H` | `Gate` | `59.94%` | `40.06%` | `1.50` | 2,850,000.00 USD |
| `4H` | `Bitget` | `49.45%` | `50.55%` | `0.98` | 1,900,000.00 USD |
| `4H` | `BingX` | `34.99%` | `65.01%` | `0.54` | 5,860,000.00 USD |
| `4H` | `MEXC` | `45.41%` | `54.59%` | `0.83` | 7,940,000.00 USD |
| `4H` | `Bitunix` | `52.05%` | `47.95%` | `1.09` | 1,730,000.00 USD |
| `4H` | `Hyperliquid` | `42.84%` | `57.16%` | `0.75` | 1,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.61%` | `50.39%` | `0.98` | 12,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `3.06%` | `96.94%` | `0.03` | 3,880,000.00 USD |
| `4H` | `HTX` | `53.22%` | `46.78%` | `1.14` | 282,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.62%` | `37.38%` | `1.68` | 745,860.00 USD |
| `4H` | `Aster` | `25.87%` | `74.13%` | `0.35` | 24,590.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `79.1%` | `20.9%` | `3.78` | 78,370.00 USD |
| `4H` | `Whale Positions` | `51.23%` | `48.77%` | `1.05` | 24,340,000.00 USD |
| `4H` | `Global Accounts` | `47.41%` | `52.59%` | `0.90` | 77,470,000.00 USD |


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
| `5m` | 129,650.00 USD | -84,100.00 USD | **`ACCUMULATION`** |
| `15m` | 126,380.00 USD | -134,120.00 USD | **`DISTRIBUTION`** |
| `30m` | 53,070.00 USD | 275,140.00 USD | **`ACCUMULATION`** |
| `1h` | 678,910.00 USD | 970,140.00 USD | **`ACCUMULATION`** |
| `2h` | 965,840.00 USD | 429,080.00 USD | **`ACCUMULATION`** |
| `4h` | 479,590.00 USD | -667,570.00 USD | **`DISTRIBUTION`** |
| `6h` | 544,620.00 USD | -935,550.00 USD | **`DISTRIBUTION`** |
| `8h` | -93,740.00 USD | -113,480.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,430,000.00 USD | -442,080.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,630,000.00 USD | -22,470,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -19,670,000.00 USD | -41,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,310,000.00 USD | -192,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+129.65K` | 15m=`+126.38K` | 1h=`+678.91K` | 24h=`-10.63M`
* Futures Capital Netflows: 5m=`-84.10K` | 15m=`-134.12K` | 1h=`+970.14K` | 24h=`-22.47M`
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
  * Spread-Padded Stop Loss: `9.24` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `13.88`
  * Mathematical Lot Sizing: **`7.54 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.45` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `7.81`
  * Mathematical Lot Sizing: **`7.54 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
