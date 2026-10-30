# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 16:18:37 IST` (`2026-10-30 10:48:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.02` | **Live Ask Quote**: `11.10` | **Mid Price**: `11.06`
- **Spread Points**: `86.00` | **Spread BPS**: `77.76 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.76` | VWAP Z-Score: `+0.73` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0786` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.71` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.55` | Lower -3.00σ Band: `9.97`
  * Upper +2.51σ Band: `11.42` | Lower -2.51σ Band: `10.10`
  * Upper +2.01σ Band: `11.29` | Lower -2.01σ Band: `10.23`
  * Upper +2.00σ Band: `11.29` | Lower -2.00σ Band: `10.24`
  * Upper +1.28σ Band: `11.10` | Lower -1.28σ Band: `10.43`
  * Upper +1.00σ Band: `11.03` | Lower -1.00σ Band: `10.50`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.96` | EMA-20=`10.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.98` (Slope: `+0.0000`) | EMA-100=`11.10`
  * Institutional Anchors: EMA-144=`11.18` | EMA-200=`11.26` (Slope: `-0.3344`) | EMA-233=`11.27`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-0.53%`)
  * Point of Control (POC) = `10.96` (Distance: `+0.92%`)
  * Value Area Low (VAL) = `10.56` (Distance: `+4.76%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.79` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.89`
  * New York Session (13:00-21:00 UTC): High=`11.04` | Low=`10.93`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.02` - `11.10`
  * Optimal Trade Entry (OTE 0.705): `11.08`
  * Structural Invalidation Anchor (0.786): `11.15`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.02` | `11.10` | `11.01` | `11.07` | `107,137` | 1,185,675.63 USD | 167,976.38 USD | `+14.17%` | -12,617,425.71 USD | `+2.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.07` | `11.08` | `11.03` | `11.06` | `123,092` | 1,360,353.47 USD | 137,130.38 USD | `+10.08%` | -12,480,295.33 USD | `+1.74` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.06` | `11.08` | `11.06` | `11.08` | `57,080` | 631,900.94 USD | 253,355.27 USD | `+40.09%` | -12,226,940.05 USD | `+2.43` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.04` | `11.04` | `10.99` | `10.99` | `95,885` | 1,056,195.55 USD | -27,195.58 USD | `-2.57%` | -12,733,671.75 USD | `+0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `10.99` | `11.06` | `10.98` | `11.02` | `87,422` | 963,211.20 USD | -51,730.34 USD | `-5.37%` | -12,785,402.09 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.02` | `11.10` | `11.01` | `11.08` | `287,308` | 3,177,930.04 USD | 558,462.03 USD | `+17.57%` | -12,226,940.05 USD | `+2.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `11.04` | `11.11` | `10.99` | `11.01` | `546,831` | 6,037,228.26 USD | -347,696.97 USD | `-5.76%` | -12,182,060.85 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.01` | `11.05` | `10.95` | `11.04` | `483,549` | 5,317,760.14 USD | -566,832.14 USD | `-10.66%` | -12,748,892.99 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.10` | `10.98` | `11.08` | `471,001` | 5,201,610.01 USD | 482,408.48 USD | `+9.27%` | -12,266,484.51 USD | `+0.53` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.08` | `1,501,320` | 16,555,922.92 USD | -431,445.13 USD | `-2.61%` | -12,306,550.42 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.08` | `1,501,320` | 16,555,922.92 USD | -431,445.13 USD | `-2.61%` | -12,306,550.42 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`11.06`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `422` | `0xecb6...2b00` | `SHORT` | 5,249,955.65 USD | `473,737,200.00` | `10.66` | `11.08` | `75.93` | -200,555.54 USD | `-3.82%` | `10X Cross` |
| `506` | `0x73ce...8ce9` | `LONG` | 4,430,328.48 USD | `400,011,600.00` | `12.05` | `11.08` | `7.82` | -389,425.23 USD | `-8.79%` | `5X Cross` |
| `838` | `0xb83d...6e36` | `SHORT` | 2,684,650.21 USD | `242,013,000.00` | `12.93` | `11.08` | `426.13` | 445,243.98 USD | `+16.58%` | `3X Cross` |
| `884` | `0x458d...ab3b` | `LONG` | 2,515,987.61 USD | `227,156,700.00` | `13.13` | `11.08` | `9.34` | -466,242.79 USD | `-18.53%` | `3X Isolated` |
| `967` | `0xdd53...2b13` | `SHORT` | 2,288,365.75 USD | `206,475,300.00` | `11.92` | `11.08` | `295.90` | 172,857.18 USD | `+7.55%` | `3X Cross` |
| `990` | `0x3dc9...54b0` | `SHORT` | 2,217,400.00 USD | `200,000,000.00` | `7.56` | `11.08` | `93.18` | -706,241.58 USD | `-31.85%` | `10X Cross` |
| `1003` | `0x45d2...4029` | `SHORT` | 2,166,531.00 USD | `195,500,000.00` | `11.54` | `11.08` | `216.66` | 89,952.43 USD | `+4.15%` | `10X Cross` |
| `1190` | `0x6540...f7b7` | `LONG` | 1,855,340.75 USD | `167,404,200.00` | `12.40` | `11.08` | `6.70` | -220,465.36 USD | `-11.88%` | `5X Isolated` |
| `1260` | `0xeadc...9d55` | `LONG` | 1,742,019.11 USD | `157,691,600.00` | `9.43` | `11.08` | `0.000000` | 255,364.20 USD | `+14.66%` | `10X Cross` |
| `1463` | `0x5b5d...c060` | `SHORT` | 1,459,281.89 USD | `131,775,500.00` | `13.61` | `11.08` | `1085.41` | 333,976.08 USD | `+22.89%` | `3X Cross` |
| `1645` | `0xf6f3...47f8` | `SHORT` | 1,275,277.74 USD | `115,024,600.00` | `11.42` | `11.08` | `18.21` | 38,052.45 USD | `+2.98%` | `5X Cross` |
| `1839` | `0xfe7e...11b4` | `LONG` | 1,120,956.79 USD | `101,142,000.00` | `14.47` | `11.08` | `5.33` | -342,156.36 USD | `-30.52%` | `5X Isolated` |
| `1871` | `0x8af7...fa05` | `SHORT` | 1,093,462.08 USD | `98,661,200.00` | `14.08` | `11.08` | `201.37` | 295,720.46 USD | `+27.04%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.63` | 5,465.85 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.6270 USD [API] | `2026-10-29 11:53:04` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.6000 USD [API] | `2026-10-29 12:19:39` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,643.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.64K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.72 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.68` | 6,290.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.29K USD at 11.6780 USD [API] | `2026-10-29 13:02:36` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,599.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:46` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,597.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:45` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.27` | 23.67 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.02K USD at 11.2730 USD [API] | `2026-09-13 09:25:11` |
| `ANNOUNCEMENT` | `INFO` | `11.63` | 227.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.23K USD at 11.6300 USD [API] | `2026-09-09 22:09:04` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 63.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 12.02 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.01K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `11.83` | 5,469.27 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8280 USD [API] | `2026-10-29 17:21:54` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 6,883.73 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.88K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 8,500.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.50K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 10,014.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 10.01K USD at 11.6670 USD [API] | `2026-10-29 19:26:32` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 6,067.82 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.07K USD at 11.7230 USD [API] | `2026-10-29 19:32:49` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 5,463.85 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.7250 USD [API] | `2026-10-29 19:36:14` |


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
| `Live` | `Long Liquidation` | `2.25` | 1,720.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 50,730.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 1,030.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 6,130.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 28,270.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,490.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,430.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 445.25 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 250.25 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 412.51 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 20,850.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 5,600.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 1,050.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 7,280.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 17,600.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 366,620.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 2,070.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 6,080.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 262.13 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,020.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 543,950.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 2,600.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 9,670.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,770.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 18,750.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 6,010.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,260.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 13,590.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 29,010.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 54,590.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,910.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 24,870.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 79,160.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 690,270.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 32,340.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 7,160.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 20,090.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 40,720.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 173,010.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,830.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 19,300.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 17,480.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 99,930.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 45,950.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 32,110.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 520,270.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 58,710.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,270.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 17,890.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 60,320.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 458,450.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 105,400.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,640.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.17` | 13,410,000.00 USD | 13,410,000.00 USD | 17,890.00 USD | 14,330.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.19` | 13,340,000.00 USD | 13,340,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.21` | 13,280,000.00 USD | 13,280,000.00 USD | 9,420.00 USD | 218.83 USD | 53.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.23` | 13,270,000.00 USD | 13,270,000.00 USD | 568.40 USD | 6,490.00 USD | 24,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.25` | 13,240,000.00 USD | 13,240,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 19,930.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.27` | 13,200,000.00 USD | 13,200,000.00 USD | 11,080.00 USD | 8,280.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.29` | 13,170,000.00 USD | 13,170,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.31` | 13,140,000.00 USD | 13,140,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.33` | 13,080,000.00 USD | 13,080,000.00 USD | 7,290.00 USD | 91.61 USD | 320.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.35` | 13,070,000.00 USD | 13,070,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.37` | 13,020,000.00 USD | 13,020,000.00 USD | 374.00 USD | 36.40 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.39` | 13,020,000.00 USD | 13,020,000.00 USD | 25,080.00 USD | 13,650.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.41` | 12,970,000.00 USD | 12,970,000.00 USD | 13,950.00 USD | 480.65 USD | 575.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.43` | 12,960,000.00 USD | 12,960,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.45` | 12,910,000.00 USD | 12,910,000.00 USD | 100,060.00 USD | 0.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 55,700.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.47` | 12,760,000.00 USD | 12,760,000.00 USD | 360.58 USD | 1,630.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.49` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.51` | 12,750,000.00 USD | 12,750,000.00 USD | 58,490.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 12,690,000.00 USD | 12,690,000.00 USD | 297.65 USD | 11,000.00 USD | 32,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 103,520.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.57` | 12,650,000.00 USD | 12,650,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 12,550,000.00 USD | 12,550,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 504.13 USD | 35,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 12,350,000.00 USD | 12,350,000.00 USD | 8,880.00 USD | 0.00 USD | 535.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 12,340,000.00 USD | 12,340,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 202,670.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.67` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 12,330,000.00 USD | 12,330,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 458.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 12,260,000.00 USD | 12,260,000.00 USD | 52,150.00 USD | 0.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 85,410.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 964.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 12,180,000.00 USD | 12,180,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 12,130,000.00 USD | 12,130,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 12,030,000.00 USD | 12,030,000.00 USD | 50,280.00 USD | 2,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 11,980,000.00 USD | 11,980,000.00 USD | 38,130.00 USD | 14,570.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 30,620.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 8,750,000.00 USD | 8,750,000.00 USD | 29,590.00 USD | 11,010.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.87` | 11,910,000.00 USD | 11,910,000.00 USD | 10,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 8,700,000.00 USD | 8,700,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 11,900,000.00 USD | 11,900,000.00 USD | 48,670.00 USD | 15,600.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 8,670,000.00 USD | 8,670,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 11,990.00 USD | 118.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 8,580,000.00 USD | 8,580,000.00 USD | 23,540.00 USD | 20,070.00 USD | 191.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 41,640.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 8,540,000.00 USD | 8,540,000.00 USD | 1,850.00 USD | 5,150.00 USD | 451.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 11,770,000.00 USD | 11,770,000.00 USD | 14,920.00 USD | 22,060.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 433,320.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 8,530,000.00 USD | 8,530,000.00 USD | 67,680.00 USD | 15,490.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 11,720,000.00 USD | 11,720,000.00 USD | 789.70 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 8,430,000.00 USD | 8,430,000.00 USD | 31,100.00 USD | 6,830.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 11,710,000.00 USD | 11,710,000.00 USD | 4,830.00 USD | 0.00 USD | 72,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,320,000.00 USD | 8,320,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 7,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,250,000.00 USD | 8,250,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.03` | 11,630,000.00 USD | 11,630,000.00 USD | 16,070.00 USD | 0.00 USD | 650.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,210,000.00 USD | 8,210,000.00 USD | 18,000.00 USD | 1,900.00 USD | 179.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 1,210.00 USD | 83,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 774,770.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,190,000.00 USD | 8,190,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 351.10 USD | 110,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 8,110,000.00 USD | 8,110,000.00 USD | 167,250.00 USD | 701.42 USD | 76,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 11,420,000.00 USD | 11,420,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 7,870,000.00 USD | 7,870,000.00 USD | 7,570.00 USD | 42,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 11,200,000.00 USD | 11,200,000.00 USD | 4,940.00 USD | 0.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 7,820,000.00 USD | 7,820,000.00 USD | 1,150.00 USD | 20,910.00 USD | 260.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 11,140,000.00 USD | 11,140,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 7,790,000.00 USD | 7,790,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 11,020,000.00 USD | 11,020,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 69,470.00 USD | 251,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 7,730,000.00 USD | 7,730,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 10,770,000.00 USD | 10,770,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 7,610,000.00 USD | 7,610,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 10,670,000.00 USD | 10,670,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,340,000.00 USD | 7,340,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 10,410,000.00 USD | 10,410,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 6,860,000.00 USD | 6,860,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 10,070,000.00 USD | 10,070,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 6,460,000.00 USD | 6,460,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 9,340,000.00 USD | 9,340,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 32,460.00 USD | 182,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,270,000.00 USD | 6,270,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 9,070,000.00 USD | 9,070,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 6,090,000.00 USD | 6,090,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 8,650,000.00 USD | 8,650,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 5,750,000.00 USD | 5,750,000.00 USD | 166,320.00 USD | 20,900.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 7,950,000.00 USD | 7,950,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 5,520,000.00 USD | 5,520,000.00 USD | 11,920.00 USD | 1,310.00 USD | 71,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 7,910,000.00 USD | 7,910,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 5,440,000.00 USD | 5,440,000.00 USD | 65,830.00 USD | 9,100.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 7,750,000.00 USD | 7,750,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,250.00 USD | 149,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,280,000.00 USD | 5,280,000.00 USD | 5,630.00 USD | 3,580.00 USD | 173.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 7,340,000.00 USD | 7,340,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,270,000.00 USD | 5,270,000.00 USD | 41,250.00 USD | 45,170.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 7,340,000.00 USD | 7,340,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,170,000.00 USD | 5,170,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 7,340,000.00 USD | 7,340,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 4,990,000.00 USD | 4,990,000.00 USD | 247,240.00 USD | 0.00 USD | 150.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 6,890,000.00 USD | 6,890,000.00 USD | 225,570.00 USD | 22,080.00 USD | 309.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 4,740,000.00 USD | 4,740,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 6,640,000.00 USD | 6,640,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 5,590.00 USD | 9,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,210,000.00 USD | 4,210,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 5,760,000.00 USD | 5,760,000.00 USD | 350,820.00 USD | 45,390.00 USD | 236.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 3,880,000.00 USD | 3,880,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 5,370,000.00 USD | 5,370,000.00 USD | 2,260.00 USD | 0.00 USD | 138,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 3,770,000.00 USD | 3,770,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 5,230,000.00 USD | 5,230,000.00 USD | 1,560.00 USD | 54,560.00 USD | 157.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 3,690,000.00 USD | 3,690,000.00 USD | 446.87 USD | 12,710.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 5,170,000.00 USD | 5,170,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 3,640,000.00 USD | 3,640,000.00 USD | 15,320.00 USD | 72,720.00 USD | 153,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 5,130,000.00 USD | 5,130,000.00 USD | 121,680.00 USD | 126,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,400,000.00 USD | 3,400,000.00 USD | 108,320.00 USD | 38,520.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 4,890,000.00 USD | 4,890,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,220,000.00 USD | 3,220,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,110,000.00 USD | 3,110,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 4,860,000.00 USD | 4,860,000.00 USD | 4,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 3,070,000.00 USD | 3,070,000.00 USD | 21,530.00 USD | 7,040.00 USD | 128,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 4,860,000.00 USD | 4,860,000.00 USD | 58,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 2,910,000.00 USD | 2,910,000.00 USD | 85,770.00 USD | 7,000.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 4,800,000.00 USD | 4,800,000.00 USD | 16,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 2,770,000.00 USD | 2,770,000.00 USD | 53,760.00 USD | 7,540.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,680,000.00 USD | 2,680,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 4,830.00 USD | 138.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,540,000.00 USD | 2,540,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 4,750,000.00 USD | 4,750,000.00 USD | 433,250.00 USD | 10,190.00 USD | 536.35 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,520,000.00 USD | 2,520,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 73,710.00 USD | 365.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,310,000.00 USD | 2,310,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 4,240,000.00 USD | 4,240,000.00 USD | 4,030.00 USD | 31,380.00 USD | 100,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,200,000.00 USD | 2,200,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 4,100,000.00 USD | 4,100,000.00 USD | 537,300.00 USD | 136,440.00 USD | 103,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 2,010,000.00 USD | 2,010,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 3,320,000.00 USD | 3,320,000.00 USD | 79,540.00 USD | 64,510.00 USD | 598.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,560,000.00 USD | 1,560,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 67,590.00 USD | 257.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,450,000.00 USD | 1,450,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 80,420.00 USD | 402,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,290,000.00 USD | 1,290,000.00 USD | 351,160.00 USD | 9,710.00 USD | 21,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 2,630,000.00 USD | 2,630,000.00 USD | 295,700.00 USD | 3,610.00 USD | 692.60 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.85` | 1,380.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 909,740.00 USD | 909,740.00 USD | 155,010.00 USD | 30,360.00 USD | 189,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 2,330,000.00 USD | 2,330,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 535,140.00 USD | 535,140.00 USD | 49,200.00 USD | 9,550.00 USD | 59,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 1,460,000.00 USD | 1,460,000.00 USD | 111,430.00 USD | 41,880.00 USD | 261,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 416,960.00 USD | 416,960.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 1,050,000.00 USD | 1,050,000.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 218,660.00 USD | 218,660.00 USD | 103,270.00 USD | 19,240.00 USD | 45.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 791,400.00 USD | 791,400.00 USD | 216,630.00 USD | 0.00 USD | 612.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 96,110.00 USD | 96,110.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 574,160.00 USD | 574,160.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 2,180.00 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 90,190.00 USD | 90,190.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 516,420.00 USD | 516,420.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 504,100.00 USD | 504,100.00 USD | 15,610.00 USD | 0.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 2,430.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 128.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 277,910.00 USD | 277,910.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.03` | 267,330.00 USD | 267,330.00 USD | 16,740.00 USD | 27,490.00 USD | 223,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 2,310.00 USD | 2,310.00 USD | 0.00 USD | 2,200.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 277,630.00 USD | 277,630.00 USD | 6,540.00 USD | 40,210.00 USD | 230,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 555,250.00 USD | 555,250.00 USD | 6,540.00 USD | 40,210.00 USD | 230,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 557,060.00 USD | 557,060.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.08` | 302,300.00 USD | 302,300.00 USD | 0.00 USD | 0.00 USD | 302,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 813,720.00 USD | 813,720.00 USD | 0.00 USD | 4,680.00 USD | 251,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 310,040.00 USD | 310,040.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,320,000.00 USD | 1,320,000.00 USD | 283,610.00 USD | 3,950.00 USD | 214,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 454,900.00 USD | 454,900.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,810,000.00 USD | 1,810,000.00 USD | 371,200.00 USD | 11,160.00 USD | 109,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 527,900.00 USD | 527,900.00 USD | 4,910.00 USD | 0.00 USD | 68,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,100,000.00 USD | 2,100,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 707,500.00 USD | 707,500.00 USD | 127,020.00 USD | 2,100.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,190,000.00 USD | 2,190,000.00 USD | 3,970.00 USD | 86,750.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 879,990.00 USD | 879,990.00 USD | 71,610.00 USD | 14,380.00 USD | 86,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 79,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 1,130,000.00 USD | 1,130,000.00 USD | 76,580.00 USD | 85,800.00 USD | 91,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,960,000.00 USD | 2,960,000.00 USD | 554,520.00 USD | 131,850.00 USD | 49.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,700,000.00 USD | 1,700,000.00 USD | 344,290.00 USD | 76,600.00 USD | 142,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 3,380,000.00 USD | 3,380,000.00 USD | 288,220.00 USD | 59,950.00 USD | 71,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 2,070,000.00 USD | 2,070,000.00 USD | 163,340.00 USD | 58,590.00 USD | 155,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,850,000.00 USD | 3,850,000.00 USD | 336,740.00 USD | 5,230.00 USD | 129,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 1,850.00 USD | 5,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.26` | 2,350,000.00 USD | 2,350,000.00 USD | 154,720.00 USD | 54,310.00 USD | 71,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,500,000.00 USD | 4,500,000.00 USD | 393,370.00 USD | 0.00 USD | 258,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 3,000,000.00 USD | 3,000,000.00 USD | 336,790.00 USD | 63,490.00 USD | 248,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,820,000.00 USD | 4,820,000.00 USD | 206,860.00 USD | 57,050.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,420,000.00 USD | 3,420,000.00 USD | 213,610.00 USD | 78,380.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 5,130,000.00 USD | 5,130,000.00 USD | 28,170.00 USD | 45,840.00 USD | 237,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 3,810,000.00 USD | 3,810,000.00 USD | 168,840.00 USD | 74,250.00 USD | 142,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 5,520,000.00 USD | 5,520,000.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,430,000.00 USD | 4,430,000.00 USD | 390,100.00 USD | 118,470.00 USD | 107,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,810,000.00 USD | 5,810,000.00 USD | 182,690.00 USD | 86,770.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,720,000.00 USD | 4,720,000.00 USD | 138,710.00 USD | 95,240.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 6,150,000.00 USD | 6,150,000.00 USD | 121,950.00 USD | 84,950.00 USD | 131,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 4,950,000.00 USD | 4,950,000.00 USD | 118,230.00 USD | 85,980.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 5,120,000.00 USD | 5,120,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 16,010.00 USD | 34,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,450,000.00 USD | 5,450,000.00 USD | 126,960.00 USD | 83,740.00 USD | 113,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 6,750,000.00 USD | 6,750,000.00 USD | 265,450.00 USD | 117,900.00 USD | 92,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,710,000.00 USD | 5,710,000.00 USD | 96,590.00 USD | 54,990.00 USD | 109,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 7,090,000.00 USD | 7,090,000.00 USD | 227,420.00 USD | 68,950.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 5,920,000.00 USD | 5,920,000.00 USD | 86,190.00 USD | 77,320.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 7,180,000.00 USD | 7,180,000.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 5,990,000.00 USD | 5,990,000.00 USD | 26,740.00 USD | 35,780.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 7,320,000.00 USD | 7,320,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,130,000.00 USD | 6,130,000.00 USD | 52,620.00 USD | 36,860.00 USD | 56,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 7,440,000.00 USD | 7,440,000.00 USD | 91,790.00 USD | 28,520.00 USD | 534.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,300,000.00 USD | 6,300,000.00 USD | 103,860.00 USD | 20,230.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 7,560,000.00 USD | 7,560,000.00 USD | 48,860.00 USD | 5,760.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,510,000.00 USD | 6,510,000.00 USD | 86,680.00 USD | 20,290.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 7,750,000.00 USD | 7,750,000.00 USD | 91,310.00 USD | 19,070.00 USD | 75,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 3,800.00 USD | 9,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,700,000.00 USD | 6,700,000.00 USD | 128,820.00 USD | 20,640.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 793.25 USD | 31,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,780,000.00 USD | 6,780,000.00 USD | 58,870.00 USD | 2,950.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 325.90 USD | 23,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 6,920,000.00 USD | 6,920,000.00 USD | 59,560.00 USD | 14,330.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 7,860,000.00 USD | 7,860,000.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 7,020,000.00 USD | 7,020,000.00 USD | 44,510.00 USD | 512.95 USD | 48,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 7,960,000.00 USD | 7,960,000.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 7,060,000.00 USD | 7,060,000.00 USD | 5,420.00 USD | 7,410.00 USD | 31,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 2,940.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 5,230.00 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,100,000.00 USD | 7,100,000.00 USD | 228.94 USD | 12,290.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,290,000.00 USD | 7,290,000.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 8,200,000.00 USD | 8,200,000.00 USD | 38,760.00 USD | 16,460.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,310,000.00 USD | 7,310,000.00 USD | 239.66 USD | 4,760.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 8,400,000.00 USD | 8,400,000.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,520,000.00 USD | 7,520,000.00 USD | 91,840.00 USD | 17,160.00 USD | 98,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 8,580,000.00 USD | 8,580,000.00 USD | 62,800.00 USD | 528.30 USD | 121,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,700,000.00 USD | 7,700,000.00 USD | 76,690.00 USD | 30,300.00 USD | 73,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 8,640,000.00 USD | 8,640,000.00 USD | 17,390.00 USD | 504.13 USD | 35,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,770,000.00 USD | 7,770,000.00 USD | 26,330.00 USD | 14,880.00 USD | 25,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 8,780,000.00 USD | 8,780,000.00 USD | 43,650.00 USD | 27,570.00 USD | 77,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 7,860,000.00 USD | 7,860,000.00 USD | 27,770.00 USD | 20,510.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 8,860,000.00 USD | 8,860,000.00 USD | 75,400.00 USD | 0.00 USD | 240.67 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 7,880,000.00 USD | 7,880,000.00 USD | 1,190.00 USD | 18,000.00 USD | 529.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 9,030,000.00 USD | 9,030,000.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 7,920,000.00 USD | 7,920,000.00 USD | 12,030.00 USD | 53.10 USD | 36,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 9,150,000.00 USD | 9,150,000.00 USD | 81,180.00 USD | 45,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 8,030,000.00 USD | 8,030,000.00 USD | 43,880.00 USD | 11,870.00 USD | 45,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 9,400,000.00 USD | 9,400,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 169.46 USD | 14,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,100,000.00 USD | 8,100,000.00 USD | 10,930.00 USD | 12,970.00 USD | 51,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 9,430,000.00 USD | 9,430,000.00 USD | 438.10 USD | 4,980.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,210,000.00 USD | 8,210,000.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 9,510,000.00 USD | 9,510,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,290,000.00 USD | 8,290,000.00 USD | 43,700.00 USD | 8,690.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 9,680,000.00 USD | 9,680,000.00 USD | 134,180.00 USD | 0.00 USD | 26,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,570,000.00 USD | 8,570,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 9,750,000.00 USD | 9,750,000.00 USD | 18,580.00 USD | 14,930.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,670,000.00 USD | 8,670,000.00 USD | 48,030.00 USD | 15,260.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 9,990,000.00 USD | 9,990,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 15,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,830,000.00 USD | 8,830,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 10,630,000.00 USD | 10,630,000.00 USD | 379,270.00 USD | 35,810.00 USD | 223,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 8,980,000.00 USD | 8,980,000.00 USD | 59,940.00 USD | 29,060.00 USD | 68,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 11,100,000.00 USD | 11,100,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,160,000.00 USD | 9,160,000.00 USD | 113,430.00 USD | 23,880.00 USD | 44,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 11,560,000.00 USD | 11,560,000.00 USD | 204,590.00 USD | 7,350.00 USD | 247,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,220,000.00 USD | 9,220,000.00 USD | 13,680.00 USD | 11,370.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 12,270,000.00 USD | 12,270,000.00 USD | 347,250.00 USD | 155,110.00 USD | 205,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,410,000.00 USD | 9,410,000.00 USD | 90,410.00 USD | 39,490.00 USD | 56,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 12,920,000.00 USD | 12,920,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,600,000.00 USD | 9,600,000.00 USD | 76,750.00 USD | 43,270.00 USD | 69,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 13,490,000.00 USD | 13,490,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,730,000.00 USD | 9,730,000.00 USD | 43,090.00 USD | 40,800.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 13,850,000.00 USD | 13,850,000.00 USD | 215,750.00 USD | 90,820.00 USD | 50,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 9,840,000.00 USD | 9,840,000.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 14,130,000.00 USD | 14,130,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 10,070,000.00 USD | 10,070,000.00 USD | 116,870.00 USD | 54,580.00 USD | 50,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 14,400,000.00 USD | 14,400,000.00 USD | 148,530.00 USD | 74,170.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,230,000.00 USD | 10,230,000.00 USD | 75,820.00 USD | 37,540.00 USD | 55,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 14,920,000.00 USD | 14,920,000.00 USD | 287,440.00 USD | 100,800.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,460,000.00 USD | 10,460,000.00 USD | 124,550.00 USD | 34,710.00 USD | 67,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 15,070,000.00 USD | 15,070,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,670,000.00 USD | 10,670,000.00 USD | 112,670.00 USD | 48,310.00 USD | 47,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 15,390,000.00 USD | 15,390,000.00 USD | 196,990.00 USD | 58,810.00 USD | 63,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,820,000.00 USD | 10,820,000.00 USD | 71,090.00 USD | 43,870.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 15,750,000.00 USD | 15,750,000.00 USD | 200,760.00 USD | 62,900.00 USD | 99,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 10,880,000.00 USD | 10,880,000.00 USD | 10,400.00 USD | 17,890.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 15,930,000.00 USD | 15,930,000.00 USD | 140,270.00 USD | 27,350.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 16,070,000.00 USD | 16,070,000.00 USD | 47,780.00 USD | 46,250.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.27` | 16,240,000.00 USD | 16,240,000.00 USD | 68,520.00 USD | 40,890.00 USD | 64,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 16,560,000.00 USD | 16,560,000.00 USD | 157,390.00 USD | 60,790.00 USD | 95,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 16,690,000.00 USD | 16,690,000.00 USD | 66,830.00 USD | 28,200.00 USD | 36,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,730,000.00 USD | 16,730,000.00 USD | 17,200.00 USD | 18,480.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,780,000.00 USD | 16,780,000.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 17,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,850,000.00 USD | 16,850,000.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 17,010,000.00 USD | 17,010,000.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 17,030,000.00 USD | 17,030,000.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 19,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 7,190.00 USD | 26,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 26,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.95` | 540.01 USD | 27,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 32,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 125,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 758.88 USD | 126,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 601.34 USD | 127,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 127,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 3,860.00 USD | 131,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 4,340.00 USD | 135,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 161,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 161,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 162,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 162,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 323.00 USD | 162,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 227.50 USD | 162,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 164,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 31,700.00 USD | 195,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 297,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 377,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 378,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,700.00 USD | 405,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,560.00 USD | 411,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 411,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,080.00 USD | 662,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 664,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 692,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 2,130,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 850,790.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 1,090.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 202.08 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.35` | 217.77 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,270,000.00 USD | 0.00 USD | 1,720.00 USD | `-79.56%` | `766,500.00` |
| `Live` | `Long` | `2.35` | 12,270,000.00 USD | 0.00 USD | 50,730.00 USD | `-78.65%` | `21,585,500.00` |
| `Live` | `Long` | `2.55` | 12,220,000.00 USD | 0.00 USD | 1,030.00 USD | `-76.83%` | `402,300.00` |
| `Live` | `Long` | `2.65` | 12,220,000.00 USD | 0.00 USD | 6,130.00 USD | `-75.92%` | `2,314,300.00` |
| `Live` | `Long` | `2.75` | 12,210,000.00 USD | 0.00 USD | 28,270.00 USD | `-75.01%` | `10,281,800.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 7,490.00 USD | `-72.29%` | `2,454,900.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 1,430.00 USD | `-71.38%` | `454,900.00` |
| `Live` | `Long` | `3.25` | 12,180,000.00 USD | 0.00 USD | 445.25 USD | `-70.47%` | `137,000.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.56%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,170,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.65%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 126.73 USD | `-67.74%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.84%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,160,000.00 USD | 0.00 USD | 250.25 USD | `-65.02%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,160,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.11%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,160,000.00 USD | 0.00 USD | 950.54 USD | `-63.20%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,160,000.00 USD | 0.00 USD | 412.51 USD | `-62.29%` | `99,400.00` |
| `Live` | `Long` | `4.25` | 12,160,000.00 USD | 0.00 USD | 20,850.00 USD | `-61.38%` | `4,905,100.00` |
| `Live` | `Long` | `4.35` | 12,140,000.00 USD | 0.00 USD | 5,600.00 USD | `-60.48%` | `1,287,000.00` |
| `Live` | `Long` | `4.45` | 12,130,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.57%` | `235,700.00` |
| `Live` | `Long` | `4.55` | 12,130,000.00 USD | 0.00 USD | 7,280.00 USD | `-58.66%` | `1,599,800.00` |
| `Live` | `Long` | `4.65` | 12,120,000.00 USD | 0.00 USD | 17,600.00 USD | `-57.75%` | `3,784,500.00` |
| `Live` | `Long` | `4.75` | 12,110,000.00 USD | 0.00 USD | 366,620.00 USD | `-56.84%` | `77,183,100.00` |
| `Live` | `Long` | `4.85` | 11,740,000.00 USD | 0.00 USD | 2,070.00 USD | `-55.93%` | `426,800.00` |
| `Live` | `Long` | `4.95` | 11,740,000.00 USD | 0.00 USD | 6,080.00 USD | `-55.02%` | `1,228,100.00` |
| `Live` | `Long` | `5.05` | 11,730,000.00 USD | 0.00 USD | 217.66 USD | `-54.12%` | `43,100.00` |
| `Live` | `Long` | `5.15` | 11,730,000.00 USD | 0.00 USD | 262.13 USD | `-53.21%` | `50,900.00` |
| `Live` | `Long` | `5.25` | 11,730,000.00 USD | 0.00 USD | 5,020.00 USD | `-52.30%` | `956,800.00` |
| `Live` | `Long` | `5.35` | 11,720,000.00 USD | 0.00 USD | 543,950.00 USD | `-51.39%` | `101,672,700.00` |
| `Live` | `Long` | `5.45` | 11,180,000.00 USD | 0.00 USD | 2,600.00 USD | `-50.48%` | `477,300.00` |
| `Live` | `Long` | `5.55` | 11,180,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.57%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 35,770.00 USD | `-48.66%` | `6,330,200.00` |
| `Live` | `Long` | `5.75` | 11,130,000.00 USD | 0.00 USD | 18,750.00 USD | `-47.76%` | `3,260,900.00` |
| `Live` | `Long` | `5.85` | 11,110,000.00 USD | 0.00 USD | 6,010.00 USD | `-46.85%` | `1,026,700.00` |
| `Live` | `Long` | `5.95` | 11,110,000.00 USD | 0.00 USD | 10,260.00 USD | `-45.94%` | `1,724,100.00` |
| `Live` | `Long` | `6.05` | 11,100,000.00 USD | 0.00 USD | 13,590.00 USD | `-45.03%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 11,080,000.00 USD | 0.00 USD | 489.54 USD | `-44.12%` | `79,600.00` |
| `Live` | `Long` | `6.25` | 11,080,000.00 USD | 0.00 USD | 29,010.00 USD | `-43.21%` | `4,642,000.00` |
| `Live` | `Long` | `6.35` | 11,050,000.00 USD | 0.00 USD | 54,590.00 USD | `-42.30%` | `8,596,600.00` |
| `Live` | `Long` | `6.45` | 11,000,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.40%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 10,990,000.00 USD | 0.00 USD | 2,910.00 USD | `-40.49%` | `444,300.00` |
| `Live` | `Long` | `6.65` | 10,990,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.58%` | `169,295,200.00` |
| `Live` | `Long` | `6.75` | 9,860,000.00 USD | 0.00 USD | 24,870.00 USD | `-38.67%` | `3,684,700.00` |
| `Live` | `Long` | `6.85` | 9,840,000.00 USD | 0.00 USD | 5,060.00 USD | `-37.76%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,830,000.00 USD | 0.00 USD | 79,160.00 USD | `-36.85%` | `11,389,500.00` |
| `Live` | `Long` | `7.05` | 9,750,000.00 USD | 0.00 USD | 690,270.00 USD | `-35.94%` | `97,910,200.00` |
| `Live` | `Long` | `7.15` | 9,060,000.00 USD | 0.00 USD | 32,340.00 USD | `-35.04%` | `4,522,900.00` |
| `Live` | `Long` | `7.25` | 9,030,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.13%` | `986,900.00` |
| `Live` | `Long` | `7.35` | 9,020,000.00 USD | 0.00 USD | 20,090.00 USD | `-33.22%` | `2,734,000.00` |
| `Live` | `Long` | `7.45` | 9,000,000.00 USD | 0.00 USD | 40,720.00 USD | `-32.31%` | `5,465,700.00` |
| `Live` | `Long` | `7.55` | 8,960,000.00 USD | 0.00 USD | 173,010.00 USD | `-31.40%` | `22,914,800.00` |
| `Live` | `Long` | `7.65` | 8,790,000.00 USD | 0.00 USD | 1,830.00 USD | `-30.49%` | `239,400.00` |
| `Live` | `Long` | `7.75` | 8,790,000.00 USD | 0.00 USD | 19,300.00 USD | `-29.58%` | `2,490,300.00` |
| `Live` | `Long` | `7.85` | 8,770,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.68%` | `400,988,000.00` |
| `Live` | `Long` | `7.95` | 5,620,000.00 USD | 0.00 USD | 17,480.00 USD | `-27.77%` | `2,198,500.00` |
| `Live` | `Long` | `8.05` | 5,600,000.00 USD | 0.00 USD | 99,930.00 USD | `-26.86%` | `12,413,400.00` |
| `Live` | `Long` | `8.15` | 5,500,000.00 USD | 0.00 USD | 45,950.00 USD | `-25.95%` | `5,638,000.00` |
| `Live` | `Long` | `8.25` | 5,460,000.00 USD | 0.00 USD | 32,110.00 USD | `-25.04%` | `3,892,000.00` |
| `Live` | `Long` | `8.35` | 5,430,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.13%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,420,000.00 USD | 0.00 USD | 520,270.00 USD | `-23.22%` | `61,570,800.00` |
| `Live` | `Long` | `8.55` | 4,900,000.00 USD | 0.00 USD | 58,710.00 USD | `-22.32%` | `6,866,700.00` |
| `Live` | `Long` | `8.65` | 4,840,000.00 USD | 0.00 USD | 15,270.00 USD | `-21.41%` | `1,765,700.00` |
| `Live` | `Long` | `8.75` | 4,820,000.00 USD | 0.00 USD | 17,890.00 USD | `-20.50%` | `2,044,100.00` |
| `Live` | `Long` | `8.85` | 4,810,000.00 USD | 0.00 USD | 60,320.00 USD | `-19.59%` | `6,816,200.00` |
| `Live` | `Long` | `8.95` | 4,750,000.00 USD | 0.00 USD | 458,450.00 USD | `-18.68%` | `51,223,800.00` |
| `Live` | `Long` | `9.05` | 4,290,000.00 USD | 0.00 USD | 105,400.00 USD | `-17.77%` | `11,646,400.00` |
| `Live` | `Long` | `9.15` | 4,180,000.00 USD | 0.00 USD | 76,640.00 USD | `-16.86%` | `8,376,000.00` |
| `Live` | `Long` | `9.25` | 4,110,000.00 USD | 0.00 USD | 19,930.00 USD | `-15.95%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,090,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.05%` | `229,774,900.00` |
| `Live` | `Long` | `9.45` | 1,940,000.00 USD | 0.00 USD | 55,700.00 USD | `-14.14%` | `5,894,700.00` |
| `Live` | `Long` | `9.55` | 1,880,000.00 USD | 0.00 USD | 103,520.00 USD | `-13.23%` | `10,839,700.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 202,670.00 USD | `-12.32%` | `21,001,700.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 85,410.00 USD | `-11.41%` | `8,760,500.00` |
| `Live` | `Long` | `9.85` | 1,490,000.00 USD | 0.00 USD | 30,620.00 USD | `-10.50%` | `3,108,900.00` |
| `Live` | `Long` | `9.95` | 1,460,000.00 USD | 0.00 USD | 433,320.00 USD | `-9.59%` | `43,549,800.00` |
| `Live` | `Long` | `10.05` | 1,030,000.00 USD | 0.00 USD | 774,770.00 USD | `-8.69%` | `77,091,800.00` |
| `Live` | `Long` | `10.15` | 251,760.00 USD | 0.00 USD | 69,470.00 USD | `-7.78%` | `6,844,000.00` |
| `Live` | `Long` | `10.25` | 182,290.00 USD | 0.00 USD | 32,460.00 USD | `-6.87%` | `3,166,900.00` |
| `Live` | `Long` | `10.35` | 149,830.00 USD | 0.00 USD | 140,250.00 USD | `-5.96%` | `13,550,500.00` |
| `Live` | `Long` | `10.45` | 9,580.00 USD | 0.00 USD | 5,590.00 USD | `-5.05%` | `534,800.00` |
| `Live` | `Long` | `10.55` | 3,990.00 USD | 0.00 USD | 3,990.00 USD | `-4.14%` | `378,500.00` |
| `Live` | `Short` | `10.85` | 1,380.00 USD | 1,380.00 USD | 0.00 USD | `-1.42%` | `127,500.00` |
| `Live` | `Short` | `10.95` | 3,560.00 USD | 2,180.00 USD | 0.00 USD | `-0.51%` | `199,100.00` |
| `Live` | `Short` | `11.25` | 5,410.00 USD | 1,850.00 USD | 0.00 USD | `+2.22%` | `164,100.00` |
| `Live` | `Short` | `11.45` | 5,660.00 USD | 249.61 USD | 0.00 USD | `+4.03%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 9,450.00 USD | 3,800.00 USD | 0.00 USD | `+4.94%` | `328,600.00` |
| `Live` | `Short` | `11.65` | 14,680.00 USD | 5,230.00 USD | 0.00 USD | `+5.85%` | `448,800.00` |
| `Live` | `Short` | `11.85` | 14,850.00 USD | 169.46 USD | 0.00 USD | `+7.67%` | `14,300.00` |
| `Live` | `Short` | `11.95` | 15,140.00 USD | 283.21 USD | 0.00 USD | `+8.58%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 16,570.00 USD | 1,430.00 USD | 0.00 USD | `+11.30%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 17,300.00 USD | 736.06 USD | 0.00 USD | `+12.21%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 19,280.00 USD | 1,980.00 USD | 0.00 USD | `+13.12%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 26,470.00 USD | 7,190.00 USD | 0.00 USD | `+14.03%` | `572,900.00` |
| `Live` | `Short` | `12.65` | 26,900.00 USD | 435.16 USD | 0.00 USD | `+14.94%` | `34,400.00` |
| `Live` | `Short` | `12.95` | 27,440.00 USD | 540.01 USD | 0.00 USD | `+17.66%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 32,870.00 USD | 5,430.00 USD | 0.00 USD | `+22.21%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 125,770.00 USD | 92,890.00 USD | 0.00 USD | `+23.11%` | `6,855,700.00` |
| `Live` | `Short` | `13.95` | 126,530.00 USD | 758.88 USD | 0.00 USD | `+26.75%` | `54,400.00` |
| `Live` | `Short` | `14.05` | 127,130.00 USD | 601.34 USD | 0.00 USD | `+27.66%` | `42,800.00` |
| `Live` | `Short` | `14.25` | 127,670.00 USD | 544.35 USD | 0.00 USD | `+29.47%` | `38,200.00` |
| `Live` | `Short` | `14.35` | 131,540.00 USD | 3,860.00 USD | 0.00 USD | `+30.38%` | `269,100.00` |
| `Live` | `Short` | `14.65` | 135,880.00 USD | 4,340.00 USD | 0.00 USD | `+33.11%` | `296,400.00` |
| `Live` | `Short` | `14.95` | 161,210.00 USD | 25,330.00 USD | 0.00 USD | `+35.83%` | `1,694,600.00` |
| `Live` | `Short` | `15.55` | 161,790.00 USD | 578.46 USD | 0.00 USD | `+41.29%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 162,060.00 USD | 271.04 USD | 0.00 USD | `+44.01%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 162,200.00 USD | 138.76 USD | 0.00 USD | `+44.92%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 162,520.00 USD | 323.00 USD | 0.00 USD | `+46.74%` | `20,000.00` |
| `Live` | `Short` | `16.25` | 162,750.00 USD | 227.50 USD | 0.00 USD | `+47.65%` | `14,000.00` |
| `Live` | `Short` | `16.35` | 164,150.00 USD | 1,390.00 USD | 0.00 USD | `+48.56%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 195,850.00 USD | 31,700.00 USD | 0.00 USD | `+50.37%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 297,760.00 USD | 101,910.00 USD | 0.00 USD | `+52.19%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 377,530.00 USD | 79,770.00 USD | 0.00 USD | `+54.01%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 378,900.00 USD | 1,370.00 USD | 0.00 USD | `+55.82%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 405,600.00 USD | 26,700.00 USD | 0.00 USD | `+57.64%` | `1,539,000.00` |
| `Live` | `Short` | `17.65` | 411,150.00 USD | 5,560.00 USD | 0.00 USD | `+60.37%` | `314,800.00` |
| `Live` | `Short` | `17.85` | 411,400.00 USD | 249.90 USD | 0.00 USD | `+62.18%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 662,480.00 USD | 251,080.00 USD | 0.00 USD | `+63.09%` | `13,987,600.00` |
| `Live` | `Short` | `18.05` | 664,450.00 USD | 1,970.00 USD | 0.00 USD | `+64.00%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 692,250.00 USD | 27,790.00 USD | 0.00 USD | `+65.82%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 2,820,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+67.64%` | `115,242,000.00` |
| `Live` | `Short` | `18.55` | 2,820,000.00 USD | 185.50 USD | 0.00 USD | `+68.54%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,820,000.00 USD | 186.50 USD | 0.00 USD | `+69.45%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 3,670,000.00 USD | 850,790.00 USD | 0.00 USD | `+71.27%` | `45,134,800.00` |
| `Live` | `Short` | `19.55` | 3,670,000.00 USD | 1,090.00 USD | 0.00 USD | `+77.63%` | `55,900.00` |
| `Live` | `Short` | `19.65` | 3,710,000.00 USD | 38,790.00 USD | 0.00 USD | `+78.54%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,710,000.00 USD | 359.45 USD | 0.00 USD | `+79.45%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,710,000.00 USD | 291.27 USD | 0.00 USD | `+81.26%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,710,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.08%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,710,000.00 USD | 1,770.00 USD | 0.00 USD | `+85.81%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+86.72%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,720,000.00 USD | 114.68 USD | 0.00 USD | `+89.44%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,720,000.00 USD | 202.08 USD | 0.00 USD | `+91.26%` | `9,600.00` |
| `Live` | `Short` | `21.35` | 3,720,000.00 USD | 217.77 USD | 0.00 USD | `+93.99%` | `10,200.00` |
| `Live` | `Short` | `21.75` | 3,790,000.00 USD | 65,060.00 USD | 0.00 USD | `+97.62%` | `2,991,400.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 401,190.00 USD | 0.00 USD | 182.03 USD | `-77.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 401,010.00 USD | 0.00 USD | 221.45 USD | `-74.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 400,790.00 USD | 0.00 USD | 234.23 USD | `-73.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 400,560.00 USD | 0.00 USD | 209.48 USD | `-71.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 400,350.00 USD | 0.00 USD | 236.33 USD | `-68.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 400,110.00 USD | 0.00 USD | 431.68 USD | `-67.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 399,680.00 USD | 0.00 USD | 290.29 USD | `-58.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 399,390.00 USD | 0.00 USD | 120.22 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 399,270.00 USD | 0.00 USD | 3,790.00 USD | `-48.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 395,470.00 USD | 0.00 USD | 251.68 USD | `-45.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 395,220.00 USD | 0.00 USD | 749.94 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 394,470.00 USD | 0.00 USD | 772.71 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 393,700.00 USD | 0.00 USD | 3,760.00 USD | `-40.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 389,940.00 USD | 0.00 USD | 133.00 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 389,800.00 USD | 0.00 USD | 1,320.00 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 388,490.00 USD | 0.00 USD | 3,770.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 384,720.00 USD | 0.00 USD | 2,070.00 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 382,650.00 USD | 0.00 USD | 3,740.00 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 378,900.00 USD | 0.00 USD | 1,050.00 USD | `-31.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 377,850.00 USD | 0.00 USD | 120.90 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 377,730.00 USD | 0.00 USD | 146.80 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 377,580.00 USD | 0.00 USD | 124.02 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 377,460.00 USD | 0.00 USD | 5,000.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 372,460.00 USD | 0.00 USD | 393.64 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 372,060.00 USD | 0.00 USD | 10,560.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 361,500.00 USD | 0.00 USD | 57,330.00 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 304,170.00 USD | 0.00 USD | 1,480.00 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 302,690.00 USD | 0.00 USD | 52,990.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 249,700.00 USD | 0.00 USD | 186.84 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 249,520.00 USD | 0.00 USD | 742.88 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 248,780.00 USD | 0.00 USD | 902.70 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 247,870.00 USD | 0.00 USD | 1,570.00 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 246,300.00 USD | 0.00 USD | 3,440.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 242,860.00 USD | 0.00 USD | 194.90 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 242,660.00 USD | 0.00 USD | 1,360.00 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 241,310.00 USD | 0.00 USD | 9,010.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 232,300.00 USD | 0.00 USD | 518.80 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 231,780.00 USD | 0.00 USD | 19,590.00 USD | `-13.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 212,190.00 USD | 0.00 USD | 504.70 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 211,680.00 USD | 0.00 USD | 3,070.00 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 208,610.00 USD | 0.00 USD | 24,100.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 184,510.00 USD | 0.00 USD | 3,450.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 181,070.00 USD | 0.00 USD | 47,890.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 133,180.00 USD | 0.00 USD | 5,650.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 127,520.00 USD | 0.00 USD | 30,030.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 97,490.00 USD | 0.00 USD | 3,480.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 94,010.00 USD | 0.00 USD | 18,670.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 75,340.00 USD | 0.00 USD | 23,690.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 51,660.00 USD | 0.00 USD | 5,170.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 46,490.00 USD | 0.00 USD | 28,310.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 18,180.00 USD | 0.00 USD | 15,000.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 3,180.00 USD | 0.00 USD | 3,180.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 5,030.00 USD | 5,030.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 10,580.00 USD | 5,550.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 37,630.00 USD | 27,050.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 54,340.00 USD | 16,710.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 58,540.00 USD | 4,190.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 84,410.00 USD | 25,870.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 87,250.00 USD | 2,840.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 88,880.00 USD | 1,630.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 96,010.00 USD | 7,130.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 100,300.00 USD | 4,300.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 130,580.00 USD | 30,280.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 132,510.00 USD | 1,930.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 225,800.00 USD | 93,280.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 226,390.00 USD | 597.74 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 231,050.00 USD | 4,650.00 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 233,540.00 USD | 2,500.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 239,720.00 USD | 6,180.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 240,400.00 USD | 679.57 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 260,770.00 USD | 20,360.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 261,220.00 USD | 451.95 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 279,420.00 USD | 18,200.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 280,340.00 USD | 919.19 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 281,660.00 USD | 1,320.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 289,440.00 USD | 7,790.00 USD | 0.00 USD | `+21.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 291,980.00 USD | 2,540.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 293,450.00 USD | 1,470.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 294,400.00 USD | 954.14 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 313,950.00 USD | 19,550.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 319,590.00 USD | 5,640.00 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 319,860.00 USD | 266.44 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 336,120.00 USD | 16,260.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 336,280.00 USD | 152.82 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 340,550.00 USD | 4,280.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 343,960.00 USD | 3,410.00 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 357,630.00 USD | 13,670.00 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 357,840.00 USD | 218.25 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 359,700.00 USD | 1,850.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 366,960.00 USD | 7,270.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 367,910.00 USD | 950.82 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 393,610.00 USD | 25,700.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 396,060.00 USD | 2,450.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 633,370.00 USD | 237,310.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 634,290.00 USD | 924.07 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 635,190.00 USD | 893.01 USD | 0.00 USD | `+40.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 659,930.00 USD | 24,740.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 660,170.00 USD | 237.88 USD | 0.00 USD | `+42.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 663,460.00 USD | 3,290.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 666,630.00 USD | 3,170.00 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 671,760.00 USD | 5,130.00 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 687,200.00 USD | 15,440.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 694,010.00 USD | 6,800.00 USD | 0.00 USD | `+46.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 700,510.00 USD | 6,500.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 707,050.00 USD | 6,540.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 713,630.00 USD | 6,580.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 723,560.00 USD | 9,930.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 827,540.00 USD | 103,980.00 USD | 0.00 USD | `+51.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 841,770.00 USD | 14,240.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 926,130.00 USD | 84,360.00 USD | 0.00 USD | `+53.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 927,820.00 USD | 1,700.00 USD | 0.00 USD | `+54.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 935,190.00 USD | 7,370.00 USD | 0.00 USD | `+54.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 936,900.00 USD | 1,710.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 939,210.00 USD | 2,300.00 USD | 0.00 USD | `+56.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 940,940.00 USD | 1,740.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 963,510.00 USD | 22,560.00 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 967,890.00 USD | 4,390.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 972,310.00 USD | 4,410.00 USD | 0.00 USD | `+60.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 976,740.00 USD | 4,440.00 USD | 0.00 USD | `+61.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 981,210.00 USD | 4,460.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 981,650.00 USD | 448.75 USD | 0.00 USD | `+63.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,010,000.00 USD | 30,960.00 USD | 0.00 USD | `+64.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,010,000.00 USD | 453.75 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,010,000.00 USD | 456.25 USD | 0.00 USD | `+65.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,010,000.00 USD | 458.75 USD | 0.00 USD | `+66.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,010,000.00 USD | 461.25 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,020,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,020,000.00 USD | 466.25 USD | 0.00 USD | `+69.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,020,000.00 USD | 468.75 USD | 0.00 USD | `+70.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,020,000.00 USD | 471.25 USD | 0.00 USD | `+71.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,020,000.00 USD | 473.75 USD | 0.00 USD | `+72.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,090,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,090,000.00 USD | 574.50 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,090,000.00 USD | 577.50 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,090,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,090,000.00 USD | 972.50 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,100,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,100,000.00 USD | 786.00 USD | 0.00 USD | `+78.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,100,000.00 USD | 790.00 USD | 0.00 USD | `+79.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,100,000.00 USD | 992.50 USD | 0.00 USD | `+80.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,100,000.00 USD | 997.50 USD | 0.00 USD | `+81.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,710,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+82.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,710,000.00 USD | 1,040.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,720,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,720,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,720,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,770,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,770,000.00 USD | 1,070.00 USD | 0.00 USD | `+94.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,770,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,780,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+100.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.32` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,440.00 USD |
| `7D` | `9.34` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD |
| `7D` | `9.36` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD |
| `7D` | `9.40` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD |
| `7D` | `9.42` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD |
| `7D` | `9.44` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD |
| `7D` | `9.46` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD |
| `7D` | `9.48` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD |
| `7D` | `9.52` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD |
| `7D` | `9.54` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 136.92 USD | 12,570.00 USD | 10.22 USD |
| `7D` | `9.56` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD |
| `7D` | `9.58` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 38,760.00 USD | 722.15 USD | 20.74 USD |
| `7D` | `9.60` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD |
| `7D` | `9.62` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 212.33 USD |
| `7D` | `9.64` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 8,500.00 USD | 2,560.00 USD | 6,100.00 USD |
| `7D` | `9.66` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.68` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.70` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.74` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD |
| `7D` | `9.76` | 12,610,000.00 USD | 0.00 USD | 12,610,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD |
| `7D` | `9.78` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.80` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD |
| `7D` | `9.82` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `7D` | `9.84` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD |
| `1D` | `9.86` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 29,590.00 USD | 11,010.00 USD | 11,110.00 USD |
| `7D` | `9.86` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 5,390.00 USD | 14,570.00 USD | 118.03 USD |
| `1D` | `9.88` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,220.00 USD |
| `7D` | `9.88` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD |
| `1D` | `9.90` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,610.00 USD |
| `7D` | `9.90` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.92` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 23,540.00 USD | 20,070.00 USD | 118.68 USD |
| `7D` | `9.92` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD |
| `1D` | `9.94` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 1,960.00 USD | 5,150.00 USD | 101.06 USD |
| `7D` | `9.94` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,390.00 USD |
| `1D` | `9.96` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 75,160.00 USD | 15,490.00 USD | 26,050.00 USD |
| `7D` | `9.96` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,480.00 USD |
| `1D` | `9.98` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 37,260.00 USD | 6,830.00 USD | 68,220.00 USD |
| `7D` | `9.98` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD |
| `1D` | `10.00` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD |
| `7D` | `10.00` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 0.00 USD | 7,630.00 USD | 12,870.00 USD |
| `1D` | `10.02` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,520.00 USD |
| `7D` | `10.02` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD |
| `1D` | `10.04` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 18,000.00 USD | 1,900.00 USD | 264.22 USD |
| `7D` | `10.04` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD |
| `1D` | `10.06` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,130.00 USD |
| `7D` | `10.06` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD |
| `1D` | `10.08` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 167,250.00 USD | 701.42 USD | 76,080.00 USD |
| `7D` | `10.08` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.10` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 7,570.00 USD | 42,810.00 USD | 288.89 USD |
| `7D` | `10.10` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD |
| `1D` | `10.12` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 1,150.00 USD | 20,910.00 USD | 0.00 USD |
| `7D` | `10.12` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD |
| `1D` | `10.14` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,520.00 USD |
| `7D` | `10.14` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD |
| `1D` | `10.16` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,610.00 USD |
| `7D` | `10.16` | 11,130,000.00 USD | 0.00 USD | 11,130,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD |
| `1D` | `10.18` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,200.00 USD |
| `7D` | `10.18` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD |
| `1D` | `10.20` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,090.00 USD |
| `7D` | `10.20` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD |
| `1D` | `10.22` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,790.00 USD |
| `7D` | `10.22` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD |
| `1D` | `10.24` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,590.00 USD |
| `7D` | `10.24` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,540.00 USD |
| `1D` | `10.26` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,930.00 USD |
| `7D` | `10.26` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD |
| `1D` | `10.28` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,690.00 USD |
| `7D` | `10.28` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.30` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,850.00 USD |
| `7D` | `10.30` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,710.00 USD |
| `7D` | `10.32` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 66,010.00 USD | 9,100.00 USD | 86,060.00 USD |
| `7D` | `10.34` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.36` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 5,630.00 USD | 3,580.00 USD | 39.63 USD |
| `7D` | `10.36` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.38` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 41,250.00 USD | 45,170.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,800.00 USD |
| `7D` | `10.40` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 247,240.00 USD | 0.00 USD | 136.88 USD |
| `7D` | `10.42` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 229,660.00 USD | 97,940.00 USD | 236.06 USD |
| `1D` | `10.44` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,440.00 USD |
| `7D` | `10.44` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,120.00 USD |
| `7D` | `10.46` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.48` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,100.00 USD |
| `7D` | `10.48` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,170.00 USD |
| `7D` | `10.50` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 4,770.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.52` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 668.27 USD | 12,710.00 USD | 38,150.00 USD |
| `7D` | `10.52` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,390.00 USD |
| `7D` | `10.54` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 108,320.00 USD | 38,520.00 USD | 37,770.00 USD |
| `7D` | `10.56` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 121,680.00 USD | 81,670.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,000.00 USD |
| `7D` | `10.58` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.60` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,950.00 USD |
| `7D` | `10.60` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 0.00 USD | 24,130.00 USD | 458.05 USD |
| `1D` | `10.62` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,030.00 USD |
| `7D` | `10.62` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 99,990.00 USD | 0.00 USD | 180.54 USD |
| `1D` | `10.64` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 109,830.00 USD | 9,030.00 USD | 56,100.00 USD |
| `7D` | `10.64` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 11,150.00 USD | 0.00 USD | 28,630.00 USD |
| `1D` | `10.66` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 59,930.00 USD | 7,540.00 USD | 29,670.00 USD |
| `7D` | `10.66` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD |
| `1D` | `10.68` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD |
| `7D` | `10.68` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD |
| `1D` | `10.70` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD |
| `7D` | `10.70` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.72` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.74` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD |
| `1D` | `10.76` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD |
| `7D` | `10.76` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 16,310.00 USD | 120,930.00 USD | 0.00 USD |
| `1D` | `10.78` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,550.00 USD |
| `7D` | `10.78` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 535,020.00 USD | 46,010.00 USD | 103,760.00 USD |
| `1D` | `10.80` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,640.00 USD |
| `7D` | `10.80` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 69,540.00 USD | 70,260.00 USD | 0.00 USD |
| `1D` | `10.82` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD |
| `7D` | `10.82` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 104,870.00 USD | 206,380.00 USD |
| `1D` | `10.84` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,630.00 USD |
| `7D` | `10.84` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 377,580.00 USD | 80,420.00 USD | 196,240.00 USD |
| `1D` | `10.86` | 998,620.00 USD | 0.00 USD | 998,620.00 USD | 203,140.00 USD | 34,420.00 USD | 213,120.00 USD |
| `7D` | `10.86` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 390,880.00 USD |
| `1D` | `10.88` | 547,940.00 USD | 0.00 USD | 547,940.00 USD | 61,520.00 USD | 9,550.00 USD | 59,460.00 USD |
| `7D` | `10.88` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD |
| `1D` | `10.90` | 417,410.00 USD | 0.00 USD | 417,410.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD |
| `7D` | `10.90` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 38,140.00 USD | 220,890.00 USD |
| `1D` | `10.92` | 219,110.00 USD | 0.00 USD | 219,110.00 USD | 103,270.00 USD | 19,240.00 USD | 86.22 USD |
| `7D` | `10.92` | 960,920.00 USD | 0.00 USD | 960,920.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD |
| `1D` | `10.94` | 96,520.00 USD | 0.00 USD | 96,520.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.94` | 623,540.00 USD | 0.00 USD | 623,540.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 90,600.00 USD | 0.00 USD | 90,600.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `10.96` | 621,060.00 USD | 0.00 USD | 621,060.00 USD | 10,430.00 USD | 0.00 USD | 49,920.00 USD |
| `7D` | `10.98` | 560,710.00 USD | 0.00 USD | 560,710.00 USD | 17,930.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 2,840.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 103.72 USD |
| `7D` | `11.00` | 333,490.00 USD | 0.00 USD | 333,490.00 USD | 10,830.00 USD | 0.00 USD | 634.90 USD |
| `7D` | `11.02` | 322,020.00 USD | 0.00 USD | 322,020.00 USD | 0.00 USD | 0.00 USD | 143,500.00 USD |
| `1D` | `11.04` | 2,740.00 USD | 0.00 USD | 2,740.00 USD | 0.00 USD | 2,200.00 USD | 402.88 USD |
| `7D` | `11.04` | 178,530.00 USD | 0.00 USD | 178,530.00 USD | 0.00 USD | 0.00 USD | 178,530.00 USD |
| `1D` | `11.06` | 135.97 USD | 0.00 USD | 135.97 USD | 0.00 USD | 0.00 USD | 135.97 USD |
| `7D` | `11.06` | 132,650.00 USD | 132,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD |
| `7D` | `11.06` | 265,310.00 USD | 265,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.08` | 267,620.00 USD | 267,620.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.10` | 7,750.00 USD | 7,750.00 USD | 0.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.10` | 645,570.00 USD | 645,570.00 USD | 0.00 USD | 282,040.00 USD | 6,920.00 USD | 88,980.00 USD |
| `1D` | `11.12` | 152,600.00 USD | 152,600.00 USD | 0.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD |
| `7D` | `11.12` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 261,760.00 USD | 5,170.00 USD | 234,170.00 USD |
| `1D` | `11.14` | 225,650.00 USD | 225,650.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD | 68,140.00 USD |
| `7D` | `11.14` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `1D` | `11.16` | 405,030.00 USD | 405,030.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,270.00 USD |
| `7D` | `11.16` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD |
| `1D` | `11.18` | 577,410.00 USD | 577,410.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,390.00 USD |
| `7D` | `11.18` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD |
| `1D` | `11.20` | 830,900.00 USD | 830,900.00 USD | 0.00 USD | 76,580.00 USD | 85,800.00 USD | 91,110.00 USD |
| `7D` | `11.20` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 171,840.00 USD | 89,800.00 USD | 79,190.00 USD |
| `1D` | `11.22` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 344,290.00 USD | 76,600.00 USD | 142,440.00 USD |
| `7D` | `11.22` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 482,460.00 USD | 42,050.00 USD | 603.14 USD |
| `1D` | `11.24` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 163,340.00 USD | 58,590.00 USD | 155,350.00 USD |
| `7D` | `11.24` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 231,960.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.26` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 154,720.00 USD | 54,310.00 USD | 71,490.00 USD |
| `7D` | `11.26` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 520,990.00 USD | 48,250.00 USD | 296,010.00 USD |
| `1D` | `11.28` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 388,220.00 USD | 67,290.00 USD | 263,100.00 USD |
| `7D` | `11.28` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 429,350.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.30` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 261,740.00 USD | 81,010.00 USD | 153,180.00 USD |
| `7D` | `11.30` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 77,570.00 USD |
| `1D` | `11.32` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 181,160.00 USD | 67,470.00 USD | 142,340.00 USD |
| `7D` | `11.32` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD |
| `1D` | `11.34` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 390,100.00 USD | 114,410.00 USD | 107,170.00 USD |
| `7D` | `11.34` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 127,190.00 USD | 116,400.00 USD | 101,390.00 USD |
| `1D` | `11.36` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 138,710.00 USD | 95,240.00 USD | 56,330.00 USD |
| `7D` | `11.36` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,380.00 USD |
| `7D` | `11.38` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD |
| `1D` | `11.40` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD |
| `7D` | `11.40` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD |
| `1D` | `11.42` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 126,960.00 USD | 83,740.00 USD | 113,690.00 USD |
| `7D` | `11.42` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 66,800.00 USD | 46,660.00 USD | 115,000.00 USD |
| `1D` | `11.44` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 96,590.00 USD | 54,990.00 USD | 109,190.00 USD |
| `7D` | `11.44` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 303,190.00 USD | 101,940.00 USD | 38,210.00 USD |
| `1D` | `11.46` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 86,190.00 USD | 77,320.00 USD | 50,780.00 USD |
| `7D` | `11.46` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 122,890.00 USD | 55,470.00 USD | 269.04 USD |
| `1D` | `11.48` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 26,740.00 USD | 35,780.00 USD | 1,910.00 USD |
| `7D` | `11.48` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD |
| `1D` | `11.50` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 78,340.00 USD | 38,760.00 USD | 63,740.00 USD |
| `7D` | `11.50` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 127,920.00 USD | 22,260.00 USD | 52,220.00 USD |
| `7D` | `11.52` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 62,260.00 USD |
| `1D` | `11.54` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 92,850.00 USD | 20,290.00 USD | 101,050.00 USD |
| `7D` | `11.54` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD |
| `1D` | `11.56` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 128,820.00 USD | 20,640.00 USD | 47,760.00 USD |
| `7D` | `11.56` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 86,650.00 USD | 19,860.00 USD | 432.76 USD |
| `1D` | `11.58` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 58,870.00 USD | 2,950.00 USD | 17,790.00 USD |
| `7D` | `11.58` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 59,780.00 USD | 14,330.00 USD | 67,580.00 USD |
| `7D` | `11.60` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 46,010.00 USD | 10,510.00 USD | 23,030.00 USD |
| `1D` | `11.62` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 44,730.00 USD | 512.95 USD | 48,190.00 USD |
| `7D` | `11.62` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.64` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 5,660.00 USD | 7,410.00 USD | 31,250.00 USD |
| `7D` | `11.64` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD |
| `1D` | `11.66` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,690.00 USD |
| `7D` | `11.66` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.68` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD |
| `7D` | `11.68` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD |
| `1D` | `11.70` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,790.00 USD |
| `7D` | `11.70` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 176.96 USD |
| `1D` | `11.72` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 91,840.00 USD | 17,160.00 USD | 98,120.00 USD |
| `7D` | `11.72` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD |
| `1D` | `11.74` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 76,690.00 USD | 30,280.00 USD | 73,130.00 USD |
| `7D` | `11.74` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD |
| `1D` | `11.76` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 26,330.00 USD | 14,880.00 USD | 24,830.00 USD |
| `7D` | `11.76` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD |
| `1D` | `11.78` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 11,750.00 USD | 20,510.00 USD | 40,030.00 USD |
| `7D` | `11.78` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 9,130.00 USD | 0.00 USD | 56,750.00 USD |
| `1D` | `11.80` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 1,350.00 USD | 18,000.00 USD | 531.07 USD |
| `7D` | `11.80` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 12,210.00 USD | 53.10 USD | 36,070.00 USD |
| `7D` | `11.82` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 182,750.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 43,880.00 USD | 11,870.00 USD | 45,600.00 USD |
| `7D` | `11.84` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD |
| `1D` | `11.86` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD |
| `7D` | `11.86` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD |
| `1D` | `11.88` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD |
| `7D` | `11.88` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD |
| `1D` | `11.90` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 28,000.00 USD |
| `7D` | `11.90` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.92` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,120.00 USD |
| `7D` | `11.92` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD |
| `1D` | `11.94` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 48,030.00 USD | 15,260.00 USD | 40,220.00 USD |
| `7D` | `11.94` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD |
| `7D` | `11.96` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD |
| `1D` | `11.98` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 59,940.00 USD | 29,050.00 USD | 68,170.00 USD |
| `7D` | `11.98` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD |
| `1D` | `12.00` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 102,680.00 USD | 23,880.00 USD | 36,270.00 USD |
| `7D` | `12.00` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD |
| `1D` | `12.02` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 13,680.00 USD | 9,340.00 USD | 31,440.00 USD |
| `7D` | `12.02` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD |
| `1D` | `12.04` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 90,410.00 USD | 39,490.00 USD | 56,310.00 USD |
| `7D` | `12.04` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD |
| `1D` | `12.06` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 76,750.00 USD | 43,270.00 USD | 69,920.00 USD |
| `7D` | `12.06` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,810.00 USD |
| `1D` | `12.08` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 43,090.00 USD | 40,800.00 USD | 52,270.00 USD |
| `7D` | `12.08` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD |
| `1D` | `12.10` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD |
| `7D` | `12.10` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 116,870.00 USD | 54,580.00 USD | 50,650.00 USD |
| `7D` | `12.12` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD |
| `1D` | `12.14` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 75,920.00 USD | 37,540.00 USD | 55,700.00 USD |
| `7D` | `12.14` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 148,090.00 USD | 102,170.00 USD | 119,290.00 USD |
| `1D` | `12.16` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 132,030.00 USD | 34,710.00 USD | 67,620.00 USD |
| `7D` | `12.16` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 182,020.00 USD | 69,310.00 USD | 75,200.00 USD |
| `1D` | `12.18` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 112,670.00 USD | 48,310.00 USD | 50,430.00 USD |
| `7D` | `12.18` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 74,850.00 USD | 54,220.00 USD | 43,550.00 USD |
| `1D` | `12.20` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 77,250.00 USD | 43,870.00 USD | 41,740.00 USD |
| `7D` | `12.20` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 75,220.00 USD |
| `1D` | `12.22` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 10,400.00 USD | 17,890.00 USD | 32,260.00 USD |
| `7D` | `12.22` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 261,490.00 USD | 63,820.00 USD | 64,370.00 USD |
| `7D` | `12.24` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 50,300.00 USD | 45,440.00 USD | 10,760.00 USD |
| `7D` | `12.26` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 73,660.00 USD | 54,120.00 USD | 50,600.00 USD |
| `7D` | `12.28` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 156,680.00 USD | 27,340.00 USD | 90,380.00 USD |
| `7D` | `12.30` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 70,240.00 USD | 49,630.00 USD | 77,910.00 USD |
| `7D` | `12.32` | 16,460,000.00 USD | 16,460,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 17,810.00 USD |
| `7D` | `12.34` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD |
| `7D` | `12.36` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD |
| `7D` | `12.38` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `511.11M` | Total OI Tokens: `46,116,928.6 LINK`
  * 1h OI Change: `+0.63%` | 4h OI Change: `-1.57%` | 24h OI Change: `-7.06%`
  * Exchange Breakdown: Binance=`100.55M` | Bybit=`68.94M` | OKX=`26.83M` | Hyperliquid=`55.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.52K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0069%` |
| **USDT Bybit** | `0.0020%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0051%` | **USDT Bitget** | `0.0087%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `39.39%` | `60.61%` | `0.65` | 16,960,000.00 USD |
| `15M` | `Binance` | `39.73%` | `60.27%` | `0.66` | 6,820,000.00 USD |
| `15M` | `OKX` | `49.65%` | `50.35%` | `0.99` | 1,270,000.00 USD |
| `15M` | `Bybit` | `53.72%` | `46.28%` | `1.16` | 3,330,000.00 USD |
| `15M` | `KuCoin` | `48.89%` | `51.11%` | `0.96` | 198,970.00 USD |
| `15M` | `Gate` | `46.53%` | `53.47%` | `0.87` | 671,350.00 USD |
| `15M` | `Bitget` | `58.41%` | `41.59%` | `1.40` | 615,710.00 USD |
| `15M` | `BingX` | `44.04%` | `55.96%` | `0.79` | 161,750.00 USD |
| `15M` | `MEXC` | `58.27%` | `41.73%` | `1.40` | 163,780.00 USD |
| `15M` | `Bitunix` | `37.34%` | `62.66%` | `0.60` | 207,910.00 USD |
| `15M` | `Hyperliquid` | `45.12%` | `54.88%` | `0.82` | 361,040.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.48%` | `52.52%` | `0.90` | 97,830.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `7.06%` | `92.94%` | `0.08` | 2,850,000.00 USD |
| `15M` | `HTX` | `57.9%` | `42.1%` | `1.38` | 33,960.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.85%` | `22.15%` | `3.51` | 101,670.00 USD |
| `15M` | `Aster` | `15.19%` | `84.81%` | `0.18` | 44,060.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `85.96%` | `14.04%` | `6.12` | 24,820.00 USD |
| `15M` | `Whale Positions` | `39.73%` | `60.27%` | `0.66` | 6,820,000.00 USD |
| `15M` | `Global Accounts` | `39.39%` | `60.61%` | `0.65` | 16,960,000.00 USD |
| `1H` | `LINK` | `45.09%` | `54.91%` | `0.82` | 43,550,000.00 USD |
| `1H` | `Binance` | `44.22%` | `55.78%` | `0.79` | 14,050,000.00 USD |
| `1H` | `OKX` | `45.43%` | `54.57%` | `0.83` | 4,890,000.00 USD |
| `1H` | `Bybit` | `55.8%` | `44.2%` | `1.26` | 9,750,000.00 USD |
| `1H` | `KuCoin` | `45.51%` | `54.49%` | `0.84` | 795,690.00 USD |
| `1H` | `Gate` | `49.59%` | `50.41%` | `0.98` | 2,200,000.00 USD |
| `1H` | `Bitget` | `58.25%` | `41.75%` | `1.40` | 2,210,000.00 USD |
| `1H` | `BingX` | `30.75%` | `69.25%` | `0.44` | 736,090.00 USD |
| `1H` | `MEXC` | `57.34%` | `42.66%` | `1.34` | 368,310.00 USD |
| `1H` | `Bitunix` | `43.23%` | `56.77%` | `0.76` | 568,800.00 USD |
| `1H` | `Hyperliquid` | `56.69%` | `43.31%` | `1.31` | 2,060,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.55%` | `50.45%` | `0.98` | 368,560.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.01%` | `88.99%` | `0.12` | 4,870,000.00 USD |
| `1H` | `HTX` | `51.88%` | `48.12%` | `1.08` | 77,890.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `83.92%` | `16.08%` | `5.22` | 402,120.00 USD |
| `1H` | `Aster` | `26.32%` | `73.68%` | `0.36` | 85,410.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.8%` | `57.2%` | `0.75` | 119,920.00 USD |
| `1H` | `Whale Positions` | `44.22%` | `55.78%` | `0.79` | 14,050,000.00 USD |
| `1H` | `Global Accounts` | `45.09%` | `54.91%` | `0.82` | 43,550,000.00 USD |
| `4H` | `LINK` | `49.67%` | `50.33%` | `0.99` | 160,830,000.00 USD |
| `4H` | `Binance` | `49.61%` | `50.39%` | `0.98` | 66,540,000.00 USD |
| `4H` | `OKX` | `47.15%` | `52.85%` | `0.89` | 19,640,000.00 USD |
| `4H` | `Bybit` | `57.18%` | `42.82%` | `1.34` | 26,140,000.00 USD |
| `4H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 3,180,000.00 USD |
| `4H` | `Gate` | `44.43%` | `55.57%` | `0.80` | 6,590,000.00 USD |
| `4H` | `Bitget` | `56.89%` | `43.11%` | `1.32` | 6,050,000.00 USD |
| `4H` | `BingX` | `27.58%` | `72.42%` | `0.38` | 2,910,000.00 USD |
| `4H` | `MEXC` | `55.14%` | `44.86%` | `1.23` | 1,450,000.00 USD |
| `4H` | `Bitunix` | `51.32%` | `48.68%` | `1.05` | 2,280,000.00 USD |
| `4H` | `Hyperliquid` | `54.53%` | `45.47%` | `1.20` | 14,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.22%` | `49.78%` | `1.01` | 2,050,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `16.49%` | `83.51%` | `0.20` | 5,810,000.00 USD |
| `4H` | `HTX` | `50.14%` | `49.86%` | `1.01` | 396,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `78.07%` | `21.93%` | `3.56` | 895,790.00 USD |
| `4H` | `Aster` | `37.86%` | `62.14%` | `0.61` | 1,010,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.27%` | `43.73%` | `1.29` | 975,010.00 USD |
| `4H` | `Whale Positions` | `49.61%` | `50.39%` | `0.98` | 66,540,000.00 USD |
| `4H` | `Global Accounts` | `49.67%` | `50.33%` | `0.99` | 160,830,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.07` | `11.08` | `11.07` | `11.11` | `11.04` | 1,641,738.88 USD | 696,135.31 USD | 945,603.58 USD | -249,468.27 USD | `-15.20%` | `10B / 19S` |
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.07` | `11.00` | 1,477,587.17 USD | 739,486.08 USD | 738,101.09 USD | 1,384.99 USD | `+0.09%` | `8B / 13S` |
| `5:00 UTC` | `11.00` | `11.01` | `11.00` | `11.05` | `10.99` | 1,128,540.66 USD | 513,281.75 USD | 615,258.92 USD | -101,977.17 USD | `-9.04%` | `14B / 18S` |
| `0:00 UTC` | `11.01` | `11.00` | `11.01` | `11.03` | `10.97` | 1,915,299.28 USD | 805,989.55 USD | 1,109,309.72 USD | -303,320.17 USD | `-15.84%` | `3B / 10S` |
| `5:00 UTC` | `10.97` | `10.99` | `10.97` | `11.01` | `10.96` | 1,089,442.23 USD | 506,886.53 USD | 582,555.71 USD | -75,669.18 USD | `-6.95%` | `5B / 8S` |
| `0:00 UTC` | `10.98` | `10.99` | `10.98` | `11.03` | `10.95` | 1,226,717.62 USD | 576,497.16 USD | 650,220.46 USD | -73,723.30 USD | `-6.01%` | `21B / 13S` |
| `5:00 UTC` | `11.03` | `11.02` | `11.03` | `11.05` | `10.99` | 1,086,301.02 USD | 486,090.76 USD | 600,210.26 USD | -114,119.49 USD | `-10.51%` | `11B / 6S` |
| `0:00 UTC` | `11.02` | `11.02` | `11.02` | `11.04` | `10.99` | 1,056,195.55 USD | 514,499.98 USD | 541,695.57 USD | -27,195.58 USD | `-2.57%` | `3B / 5S` |
| `5:00 UTC` | `11.00` | `11.02` | `11.00` | `11.06` | `10.99` | 963,211.20 USD | 455,740.43 USD | 507,470.77 USD | -51,730.34 USD | `-5.37%` | `9B / 12S` |
| `0:00 UTC` | `11.05` | `11.06` | `11.05` | `11.10` | `11.01` | 1,843,714.97 USD | 960,530.89 USD | 883,184.09 USD | 77,346.80 USD | `+4.20%` | `17B / 12S` |

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
| `5m` | 227,190.00 USD | -16,580.00 USD | **`ACCUMULATION`** |
| `15m` | 273,760.00 USD | 104,810.00 USD | **`ACCUMULATION`** |
| `30m` | 485,500.00 USD | -159,410.00 USD | **`ACCUMULATION`** |
| `1h` | 680,820.00 USD | -194,430.00 USD | **`ACCUMULATION`** |
| `2h` | 396,660.00 USD | -899,150.00 USD | **`DISTRIBUTION`** |
| `4h` | 107,930.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -66,830.00 USD | -1,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -329,980.00 USD | -41,090.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,860,000.00 USD | -6,480,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,720,000.00 USD | -23,150,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,020,000.00 USD | -42,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,020,000.00 USD | -194,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+227.19K` | 15m=`+273.76K` | 1h=`+680.82K` | 24h=`-10.72M`
* Futures Capital Netflows: 5m=`-16.58K` | 15m=`+104.81K` | 1h=`-194.43K` | 24h=`-23.15M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.56` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.34` (Risk Distance: `0.2233` pts)
  * +2.5R Take Profit: `11.12`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.34` (Risk Distance: `0.2233` pts)
  * +2.5R Take Profit: `10.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.15`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
