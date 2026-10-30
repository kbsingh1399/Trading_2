# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 10:19:39 IST` (`2026-10-30 04:49:39 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.95` | **Live Ask Quote**: `11.03` | **Mid Price**: `10.99`
- **Spread Points**: `85.00` | **Spread BPS**: `77.35 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.55` | VWAP Z-Score: `+2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1139` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `59.16` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.10` | Lower -3.00σ Band: `10.00`
  * Upper +2.51σ Band: `11.01` | Lower -2.51σ Band: `10.09`
  * Upper +2.01σ Band: `10.92` | Lower -2.01σ Band: `10.18`
  * Upper +2.00σ Band: `10.91` | Lower -2.00σ Band: `10.18`
  * Upper +1.28σ Band: `10.78` | Lower -1.28σ Band: `10.31`
  * Upper +1.00σ Band: `10.73` | Lower -1.00σ Band: `10.37`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.80` | EMA-20=`10.75` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.95` (Slope: `+0.0000`) | EMA-100=`11.17`
  * Institutional Anchors: EMA-144=`11.25` | EMA-200=`11.31` (Slope: `-0.6688`) | EMA-233=`11.34`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.88` (Distance: `+0.99%`)
  * Point of Control (POC) = `10.48` (Distance: `+4.86%`)
  * Value Area Low (VAL) = `10.35` (Distance: `+6.20%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.72` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.03` | Low=`10.94`
  * New York Session (13:00-21:00 UTC): High=`11.05` | Low=`10.92`
  * Initial Balance (First Hour): IB High=`11.02` | IB Low=`10.96`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.94` - `11.03`
  * Optimal Trade Entry (OTE 0.705): `11.01`
  * Structural Invalidation Anchor (0.786): `11.08`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.00` | `11.02` | `10.96` | `10.99` | `200,140` | 2,200,445.70 USD | -639,900.09 USD | `-29.08%` | -12,582,331.38 USD | `-3.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.99` | `11.01` | `10.99` | `11.01` | `127,077` | 1,398,249.60 USD | 749,956.81 USD | `+53.64%` | -11,832,374.57 USD | `+2.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `11.01` | `11.02` | `11.00` | `11.02` | `32,005` | 352,336.75 USD | 57,077.68 USD | `+16.20%` | -11,775,296.88 USD | `+0.06` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `10.96` | `10.99` | `10.90` | `10.99` | `236,732` | 2,589,400.57 USD | 48,743.44 USD | `+1.88%` | -11,838,476.89 USD | `-0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `10.99` | `11.02` | `10.96` | `11.00` | `173,533` | 1,907,525.28 USD | -103,954.39 USD | `-5.45%` | -11,942,431.29 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.00` | `11.02` | `10.96` | `11.02` | `360,146` | 3,961,213.32 USD | 156,953.13 USD | `+3.96%` | -11,785,478.16 USD | `+0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `10.52` | `10.74` | `10.47` | `10.72` | `1,548,991` | 16,462,599.15 USD | 1,237,330.15 USD | `+7.52%` | -12,901,161.72 USD | `+0.86` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.72` | `10.98` | `10.71` | `10.96` | `806,147` | 8,746,362.36 USD | 866,493.31 USD | `+9.91%` | -12,034,668.41 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.96` | `11.02` | `10.90` | `11.02` | `770,412` | 8,458,139.17 USD | 101,742.17 USD | `+1.20%` | -11,932,926.24 USD | `+0.32` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.02` | `10.90` | `11.02` | `769,484` | 8,447,920.89 USD | 111,960.46 USD | `+1.33%` | -12,116,867.61 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,625,285.45 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 595,900.27 USD | `-1.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.02` | `10.90` | `11.02` | `769,484` | 8,447,920.89 USD | 111,960.46 USD | `+1.33%` | -12,116,867.61 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`10.99`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `421` | `0xecb6...2b00` | `SHORT` | 5,244,910.02 USD | `475,728,800.00` | `10.66` | `11.03` | `66.48` | -174,282.14 USD | `-3.32%` | `10X Cross` |
| `509` | `0x73ce...8ce9` | `LONG` | 4,405,727.76 USD | `400,011,600.00` | `12.05` | `11.03` | `7.82` | -414,025.94 USD | `-9.40%` | `5X Cross` |
| `858` | `0xb83d...6e36` | `SHORT` | 2,665,531.18 USD | `242,013,000.00` | `12.93` | `11.03` | `536.73` | 464,363.01 USD | `+17.42%` | `3X Cross` |
| `907` | `0x458d...ab3b` | `LONG` | 2,502,131.05 USD | `227,156,700.00` | `13.13` | `11.03` | `9.34` | -480,099.35 USD | `-19.19%` | `3X Isolated` |
| `978` | `0xdd53...2b13` | `SHORT` | 2,273,706.00 USD | `206,475,300.00` | `11.92` | `11.03` | `299.50` | 187,516.92 USD | `+8.25%` | `3X Cross` |
| `1006` | `0x3dc9...54b0` | `SHORT` | 2,203,000.00 USD | `200,000,000.00` | `7.56` | `11.03` | `94.57` | -691,841.58 USD | `-31.40%` | `10X Cross` |
| `1019` | `0x45d2...4029` | `SHORT` | 2,151,868.50 USD | `195,500,000.00` | `11.54` | `11.03` | `217.39` | 104,614.93 USD | `+4.86%` | `10X Cross` |
| `1186` | `0x6540...f7b7` | `LONG` | 1,859,360.34 USD | `168,924,800.00` | `12.40` | `11.03` | `6.69` | -235,859.95 USD | `-12.69%` | `5X Isolated` |
| `1273` | `0xeadc...9d55` | `LONG` | 1,736,499.90 USD | `157,691,600.00` | `9.43` | `11.03` | `0.000000` | 249,845.00 USD | `+14.39%` | `10X Cross` |
| `1500` | `0x5b5d...c060` | `SHORT` | 1,451,111.81 USD | `131,775,500.00` | `13.61` | `11.03` | `1185.91` | 342,146.16 USD | `+23.58%` | `3X Cross` |
| `1669` | `0xf6f3...47f8` | `SHORT` | 1,266,305.82 USD | `115,024,600.00` | `11.42` | `11.03` | `19.18` | 47,024.36 USD | `+3.71%` | `5X Cross` |
| `1824` | `0x9df2...c665` | `SHORT` | 1,142,972.92 USD | `103,793,400.00` | `11.48` | `11.03` | `301.30` | 48,679.85 USD | `+4.26%` | `10X Cross` |
| `1861` | `0xfe7e...11b4` | `LONG` | 1,113,775.70 USD | `101,142,000.00` | `14.47` | `11.03` | `5.32` | -349,337.45 USD | `-31.37%` | `5X Isolated` |
| `1889` | `0x8af7...fa05` | `SHORT` | 1,086,358.47 USD | `98,661,200.00` | `14.08` | `11.03` | `203.28` | 302,824.07 USD | `+27.88%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `12.75` | 164.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.16K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 4,018.81 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 4.02K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 14,599.27 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 14.60K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 166.97 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.17K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 1,874.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 1.87K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `11.42` | 4,438.93 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 4.44K USD at 11.4170 USD [API] | `2026-10-29 02:00:09` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+1.30%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.02%`)
  * 48H Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+1.29%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.03%`)
  * 3D Horizon: Short MP=`11.11` (Vol: 502,200.00 USD, Dist: `+1.29%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.03%`)
  * 7D Horizon: Short MP=`11.05` (Vol: 597,700.00 USD, Dist: `+0.80%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.03%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 2,960.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 2,350.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,110.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 1,550.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,550.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 260.15 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,300.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 1,450.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 19,960.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 4,770.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 250.25 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,480.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 45,660.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 595.08 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 7,300.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 48,700.00 USD | 11,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 233,170.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 6,530.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 2,060.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 4,620.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 89,580.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 3,730.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 545,540.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 41,970.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,770.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 276.57 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 1,700.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 5,380.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 21,070.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 6,990.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 40,180.00 USD | 10,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 56,480.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 15,730.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,140,000.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 12,630.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 29,030.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 61,990.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 689,480.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 34,590.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 57,480.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 18,570.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 8,530.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 25,580.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 155,020.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 631.62 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 16,960.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 118,610.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 39,090.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 34,340.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 28,950.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 12,500.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,820.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 356,160.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 28,630.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 61,500.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 460,150.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 87,450.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,690.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.45` | 4,750,000.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 46,880.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.47` | 4,730,000.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.53` | 4,730,000.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.55` | 4,720,000.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 54,080.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.65` | 202,600.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.75` | 73,650.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.85` | 81,980.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 4,160,000.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 4,140,000.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 4,110,000.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 4,090,000.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 440,220.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 4,060,000.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 4,030,000.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 4,030,000.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 4,030,000.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 788,850.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 4,020,000.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 4,010,000.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 4,000,000.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 69,150.00 USD | 248,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `10.25` | 41,320.00 USD | 179,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `10.35` | 138,320.00 USD | 138,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `11.05` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.15` | 2,970.00 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 6,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.55` | 4,800.00 USD | 11,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.65` | 23,770.00 USD | 35,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.95` | 205.54 USD | 35,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.15` | 1,270.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 38,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 39,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.45` | 519.16 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.47` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 12,000.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,310.00 USD | 41,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 41,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Short Liquidation` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 158.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 46,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 139,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 140,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 140,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 166,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 166,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 166,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 167,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 167,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 168,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 230.30 USD | 168,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 31,700.00 USD | 200,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 91,200.00 USD | 291,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 15,760.00 USD | 307,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 387,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 388,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,700.00 USD | 415,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 5,480.00 USD | 420,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 421,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,200.00 USD | 672,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 2,690.00 USD | 674,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 702,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 706,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 699,710.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 75,870.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 2,230,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 289.81 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 637.59 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.65` | 185.85 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.25` | 3,670.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 119.62 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,100,000.00 USD | 0.00 USD | 2,960.00 USD | `-79.40%` | `1,313,700.00` |
| `Live` | `Long` | `2.35` | 12,090,000.00 USD | 0.00 USD | 2,350.00 USD | `-78.49%` | `1,000,000.00` |
| `Live` | `Long` | `2.45` | 12,090,000.00 USD | 0.00 USD | 1,110.00 USD | `-77.57%` | `452,300.00` |
| `Live` | `Long` | `2.55` | 12,090,000.00 USD | 0.00 USD | 1,550.00 USD | `-76.65%` | `606,600.00` |
| `Live` | `Long` | `2.65` | 12,090,000.00 USD | 0.00 USD | 2,550.00 USD | `-75.74%` | `961,300.00` |
| `Live` | `Long` | `2.75` | 12,090,000.00 USD | 0.00 USD | 260.15 USD | `-74.82%` | `94,600.00` |
| `Live` | `Long` | `3.05` | 12,090,000.00 USD | 0.00 USD | 7,300.00 USD | `-72.08%` | `2,394,200.00` |
| `Live` | `Long` | `3.15` | 12,080,000.00 USD | 0.00 USD | 297.99 USD | `-71.16%` | `94,600.00` |
| `Live` | `Long` | `3.35` | 12,080,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.33%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,080,000.00 USD | 0.00 USD | 1,450.00 USD | `-68.42%` | `421,000.00` |
| `Live` | `Long` | `3.55` | 12,080,000.00 USD | 0.00 USD | 19,960.00 USD | `-67.50%` | `5,622,000.00` |
| `Live` | `Long` | `3.65` | 12,060,000.00 USD | 0.00 USD | 4,770.00 USD | `-66.58%` | `1,307,000.00` |
| `Live` | `Long` | `3.85` | 12,050,000.00 USD | 0.00 USD | 250.25 USD | `-64.75%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,050,000.00 USD | 0.00 USD | 4,420.00 USD | `-63.84%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,050,000.00 USD | 0.00 USD | 6,480.00 USD | `-62.92%` | `1,601,100.00` |
| `Live` | `Long` | `4.15` | 12,040,000.00 USD | 0.00 USD | 45,660.00 USD | `-62.01%` | `11,003,200.00` |
| `Live` | `Long` | `4.25` | 11,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-61.09%` | `1,198,100.00` |
| `Live` | `Long` | `4.35` | 11,990,000.00 USD | 0.00 USD | 595.08 USD | `-60.18%` | `136,800.00` |
| `Live` | `Long` | `4.45` | 11,990,000.00 USD | 0.00 USD | 381.37 USD | `-59.26%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 11,990,000.00 USD | 0.00 USD | 7,300.00 USD | `-58.34%` | `1,604,500.00` |
| `Live` | `Long` | `4.65` | 11,980,000.00 USD | 0.00 USD | 48,700.00 USD | `-57.43%` | `10,473,800.00` |
| `Live` | `Long` | `4.75` | 11,930,000.00 USD | 0.00 USD | 233,170.00 USD | `-56.51%` | `49,088,200.00` |
| `Live` | `Long` | `4.85` | 11,700,000.00 USD | 0.00 USD | 6,530.00 USD | `-55.60%` | `1,346,600.00` |
| `Live` | `Long` | `4.95` | 11,690,000.00 USD | 0.00 USD | 2,060.00 USD | `-54.68%` | `416,200.00` |
| `Live` | `Long` | `5.05` | 11,690,000.00 USD | 0.00 USD | 4,620.00 USD | `-53.77%` | `914,400.00` |
| `Live` | `Long` | `5.15` | 11,690,000.00 USD | 0.00 USD | 89,580.00 USD | `-52.85%` | `17,393,500.00` |
| `Live` | `Long` | `5.25` | 11,600,000.00 USD | 0.00 USD | 3,730.00 USD | `-51.94%` | `711,000.00` |
| `Live` | `Long` | `5.35` | 11,590,000.00 USD | 0.00 USD | 545,540.00 USD | `-51.02%` | `101,970,200.00` |
| `Live` | `Long` | `5.45` | 11,050,000.00 USD | 0.00 USD | 138.97 USD | `-50.11%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 11,050,000.00 USD | 0.00 USD | 41,970.00 USD | `-49.19%` | `7,562,900.00` |
| `Live` | `Long` | `5.65` | 11,000,000.00 USD | 0.00 USD | 35,770.00 USD | `-48.27%` | `6,330,200.00` |
| `Live` | `Long` | `5.75` | 10,970,000.00 USD | 0.00 USD | 276.57 USD | `-47.36%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 10,970,000.00 USD | 0.00 USD | 1,700.00 USD | `-46.44%` | `290,500.00` |
| `Live` | `Long` | `5.95` | 10,970,000.00 USD | 0.00 USD | 5,380.00 USD | `-45.53%` | `903,400.00` |
| `Live` | `Long` | `6.05` | 10,960,000.00 USD | 0.00 USD | 21,070.00 USD | `-44.61%` | `3,482,800.00` |
| `Live` | `Long` | `6.15` | 10,940,000.00 USD | 0.00 USD | 6,990.00 USD | `-43.70%` | `1,136,400.00` |
| `Live` | `Long` | `6.25` | 10,930,000.00 USD | 0.00 USD | 40,180.00 USD | `-42.78%` | `6,429,000.00` |
| `Live` | `Long` | `6.35` | 10,890,000.00 USD | 0.00 USD | 56,480.00 USD | `-41.87%` | `8,895,000.00` |
| `Live` | `Long` | `6.45` | 10,840,000.00 USD | 0.00 USD | 15,730.00 USD | `-40.95%` | `2,439,300.00` |
| `Live` | `Long` | `6.55` | 10,820,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.03%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 10,820,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-39.12%` | `171,172,800.00` |
| `Live` | `Long` | `6.75` | 9,680,000.00 USD | 0.00 USD | 12,630.00 USD | `-38.20%` | `1,870,900.00` |
| `Live` | `Long` | `6.85` | 9,670,000.00 USD | 0.00 USD | 29,030.00 USD | `-37.29%` | `4,238,400.00` |
| `Live` | `Long` | `6.95` | 9,640,000.00 USD | 0.00 USD | 61,990.00 USD | `-36.37%` | `8,919,300.00` |
| `Live` | `Long` | `7.05` | 9,580,000.00 USD | 0.00 USD | 689,480.00 USD | `-35.46%` | `97,799,200.00` |
| `Live` | `Long` | `7.15` | 8,890,000.00 USD | 0.00 USD | 34,590.00 USD | `-34.54%` | `4,837,400.00` |
| `Live` | `Long` | `7.25` | 8,850,000.00 USD | 0.00 USD | 57,480.00 USD | `-33.63%` | `7,927,800.00` |
| `Live` | `Long` | `7.35` | 8,790,000.00 USD | 0.00 USD | 18,570.00 USD | `-32.71%` | `2,526,400.00` |
| `Live` | `Long` | `7.45` | 8,780,000.00 USD | 0.00 USD | 8,530.00 USD | `-31.80%` | `1,145,600.00` |
| `Live` | `Long` | `7.55` | 8,770,000.00 USD | 0.00 USD | 25,580.00 USD | `-30.88%` | `3,388,500.00` |
| `Live` | `Long` | `7.65` | 8,740,000.00 USD | 0.00 USD | 155,020.00 USD | `-29.96%` | `20,264,400.00` |
| `Live` | `Long` | `7.75` | 8,590,000.00 USD | 0.00 USD | 631.62 USD | `-29.05%` | `81,500.00` |
| `Live` | `Long` | `7.85` | 8,590,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.13%` | `400,939,100.00` |
| `Live` | `Long` | `7.95` | 5,440,000.00 USD | 0.00 USD | 16,960.00 USD | `-27.22%` | `2,133,900.00` |
| `Live` | `Long` | `8.05` | 5,420,000.00 USD | 0.00 USD | 118,610.00 USD | `-26.30%` | `14,733,800.00` |
| `Live` | `Long` | `8.15` | 5,300,000.00 USD | 0.00 USD | 39,090.00 USD | `-25.39%` | `4,795,900.00` |
| `Live` | `Long` | `8.25` | 5,260,000.00 USD | 0.00 USD | 34,340.00 USD | `-24.47%` | `4,162,900.00` |
| `Live` | `Long` | `8.35` | 5,230,000.00 USD | 0.00 USD | 28,950.00 USD | `-23.56%` | `3,466,900.00` |
| `Live` | `Long` | `8.45` | 5,200,000.00 USD | 0.00 USD | 12,500.00 USD | `-22.64%` | `1,478,800.00` |
| `Live` | `Long` | `8.55` | 5,190,000.00 USD | 0.00 USD | 15,820.00 USD | `-21.72%` | `1,849,800.00` |
| `Live` | `Long` | `8.65` | 5,170,000.00 USD | 0.00 USD | 356,160.00 USD | `-20.81%` | `41,174,900.00` |
| `Live` | `Long` | `8.75` | 4,820,000.00 USD | 0.00 USD | 28,630.00 USD | `-19.89%` | `3,271,900.00` |
| `Live` | `Long` | `8.85` | 4,790,000.00 USD | 0.00 USD | 61,500.00 USD | `-18.98%` | `6,949,200.00` |
| `Live` | `Long` | `8.95` | 4,730,000.00 USD | 0.00 USD | 460,150.00 USD | `-18.06%` | `51,413,900.00` |
| `Live` | `Long` | `9.05` | 4,270,000.00 USD | 0.00 USD | 87,450.00 USD | `-17.15%` | `9,662,700.00` |
| `Live` | `Long` | `9.15` | 4,180,000.00 USD | 0.00 USD | 76,340.00 USD | `-16.23%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,100,000.00 USD | 0.00 USD | 17,690.00 USD | `-15.32%` | `1,912,100.00` |
| `Live` | `Long` | `9.35` | 4,080,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-14.40%` | `229,680,600.00` |
| `Live` | `Long` | `9.45` | 1,940,000.00 USD | 0.00 USD | 46,880.00 USD | `-13.49%` | `4,961,100.00` |
| `Live` | `Long` | `9.55` | 1,890,000.00 USD | 0.00 USD | 54,080.00 USD | `-12.57%` | `5,663,000.00` |
| `Live` | `Long` | `9.65` | 1,840,000.00 USD | 0.00 USD | 202,600.00 USD | `-11.65%` | `20,995,300.00` |
| `Live` | `Long` | `9.75` | 1,630,000.00 USD | 0.00 USD | 73,650.00 USD | `-10.74%` | `7,553,700.00` |
| `Live` | `Long` | `9.85` | 1,560,000.00 USD | 0.00 USD | 81,980.00 USD | `-9.82%` | `8,322,900.00` |
| `Live` | `Long` | `9.95` | 1,480,000.00 USD | 0.00 USD | 440,220.00 USD | `-8.91%` | `44,243,500.00` |
| `Live` | `Long` | `10.05` | 1,040,000.00 USD | 0.00 USD | 788,850.00 USD | `-7.99%` | `78,492,700.00` |
| `Live` | `Long` | `10.15` | 248,800.00 USD | 0.00 USD | 69,150.00 USD | `-7.08%` | `6,813,000.00` |
| `Live` | `Long` | `10.25` | 179,650.00 USD | 0.00 USD | 41,320.00 USD | `-6.16%` | `4,031,700.00` |
| `Live` | `Long` | `10.35` | 138,320.00 USD | 0.00 USD | 138,320.00 USD | `-5.25%` | `13,364,500.00` |
| `Live` | `Short` | `11.05` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | `+1.16%` | `339,500.00` |
| `Live` | `Short` | `11.15` | 6,720.00 USD | 2,970.00 USD | 0.00 USD | `+2.08%` | `266,300.00` |
| `Live` | `Short` | `11.45` | 6,970.00 USD | 249.61 USD | 0.00 USD | `+4.82%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 11,770.00 USD | 4,800.00 USD | 0.00 USD | `+5.74%` | `415,600.00` |
| `Live` | `Short` | `11.65` | 35,540.00 USD | 23,770.00 USD | 0.00 USD | `+6.66%` | `2,040,400.00` |
| `Live` | `Short` | `11.95` | 35,750.00 USD | 205.54 USD | 0.00 USD | `+9.40%` | `17,200.00` |
| `Live` | `Short` | `12.15` | 37,020.00 USD | 1,270.00 USD | 0.00 USD | `+11.23%` | `104,700.00` |
| `Live` | `Short` | `12.25` | 38,450.00 USD | 1,430.00 USD | 0.00 USD | `+12.15%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 39,190.00 USD | 736.06 USD | 0.00 USD | `+13.06%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 39,700.00 USD | 519.16 USD | 0.00 USD | `+13.98%` | `41,700.00` |
| `Live` | `Short` | `12.55` | 41,020.00 USD | 1,310.00 USD | 0.00 USD | `+14.90%` | `104,500.00` |
| `Live` | `Short` | `12.65` | 41,450.00 USD | 435.16 USD | 0.00 USD | `+15.81%` | `34,400.00` |
| `Live` | `Short` | `13.45` | 46,880.00 USD | 5,430.00 USD | 0.00 USD | `+23.13%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 139,780.00 USD | 92,890.00 USD | 0.00 USD | `+24.05%` | `6,855,700.00` |
| `Live` | `Short` | `14.15` | 140,130.00 USD | 349.51 USD | 0.00 USD | `+29.54%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 140,670.00 USD | 544.35 USD | 0.00 USD | `+30.46%` | `38,200.00` |
| `Live` | `Short` | `14.95` | 166,000.00 USD | 25,330.00 USD | 0.00 USD | `+36.87%` | `1,694,600.00` |
| `Live` | `Short` | `15.25` | 166,160.00 USD | 155.55 USD | 0.00 USD | `+39.61%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 166,740.00 USD | 578.46 USD | 0.00 USD | `+42.36%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 167,010.00 USD | 271.04 USD | 0.00 USD | `+45.11%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 167,150.00 USD | 138.76 USD | 0.00 USD | `+46.02%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 168,540.00 USD | 1,390.00 USD | 0.00 USD | `+49.68%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 168,770.00 USD | 230.30 USD | 0.00 USD | `+50.60%` | `14,000.00` |
| `Live` | `Short` | `16.55` | 200,480.00 USD | 31,700.00 USD | 0.00 USD | `+51.52%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 291,680.00 USD | 91,200.00 USD | 0.00 USD | `+53.35%` | `5,445,000.00` |
| `Live` | `Short` | `16.85` | 307,440.00 USD | 15,760.00 USD | 0.00 USD | `+54.26%` | `935,400.00` |
| `Live` | `Short` | `16.95` | 387,210.00 USD | 79,770.00 USD | 0.00 USD | `+55.18%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 388,580.00 USD | 1,370.00 USD | 0.00 USD | `+57.01%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 415,280.00 USD | 26,700.00 USD | 0.00 USD | `+58.84%` | `1,539,000.00` |
| `Live` | `Short` | `17.75` | 420,770.00 USD | 5,480.00 USD | 0.00 USD | `+62.50%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 421,020.00 USD | 249.90 USD | 0.00 USD | `+63.42%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 672,210.00 USD | 251,200.00 USD | 0.00 USD | `+64.33%` | `13,994,200.00` |
| `Live` | `Short` | `18.05` | 674,900.00 USD | 2,690.00 USD | 0.00 USD | `+65.25%` | `149,000.00` |
| `Live` | `Short` | `18.25` | 702,700.00 USD | 27,790.00 USD | 0.00 USD | `+67.08%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 706,590.00 USD | 3,890.00 USD | 0.00 USD | `+68.91%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,410,000.00 USD | 699,710.00 USD | 0.00 USD | `+69.83%` | `37,720,000.00` |
| `Live` | `Short` | `18.65` | 1,410,000.00 USD | 186.50 USD | 0.00 USD | `+70.74%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 1,480,000.00 USD | 75,870.00 USD | 0.00 USD | `+72.57%` | `4,024,800.00` |
| `Live` | `Short` | `19.35` | 3,710,000.00 USD | 2,230,000.00 USD | 0.00 USD | `+77.15%` | `115,024,600.00` |
| `Live` | `Short` | `19.55` | 3,710,000.00 USD | 316.71 USD | 0.00 USD | `+78.98%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,750,000.00 USD | 38,790.00 USD | 0.00 USD | `+79.90%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,750,000.00 USD | 359.45 USD | 0.00 USD | `+80.81%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 3,750,000.00 USD | 289.81 USD | 0.00 USD | `+81.73%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,750,000.00 USD | 637.59 USD | 0.00 USD | `+83.56%` | `31,800.00` |
| `Live` | `Short` | `20.15` | 3,750,000.00 USD | 1,260.00 USD | 0.00 USD | `+84.47%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,750,000.00 USD | 1,770.00 USD | 0.00 USD | `+87.22%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,760,000.00 USD | 7,250.00 USD | 0.00 USD | `+88.14%` | `353,000.00` |
| `Live` | `Short` | `20.65` | 3,760,000.00 USD | 185.85 USD | 0.00 USD | `+89.05%` | `9,000.00` |
| `Live` | `Short` | `21.25` | 3,760,000.00 USD | 3,670.00 USD | 0.00 USD | `+94.54%` | `172,500.00` |
| `Live` | `Short` | `21.75` | 3,760,000.00 USD | 119.62 USD | 0.00 USD | `+99.12%` | `5,500.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 471,800.00 USD | 0.00 USD | 182.03 USD | `-77.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 471,610.00 USD | 0.00 USD | 234.23 USD | `-72.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 471,380.00 USD | 0.00 USD | 209.48 USD | `-71.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 471,170.00 USD | 0.00 USD | 680.89 USD | `-67.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 470,490.00 USD | 0.00 USD | 290.29 USD | `-58.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 470,200.00 USD | 0.00 USD | 120.22 USD | `-51.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 470,080.00 USD | 0.00 USD | 251.68 USD | `-44.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 469,830.00 USD | 0.00 USD | 749.30 USD | `-41.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 469,080.00 USD | 0.00 USD | 772.71 USD | `-40.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 468,300.00 USD | 0.00 USD | 3,760.00 USD | `-40.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 464,540.00 USD | 0.00 USD | 133.00 USD | `-39.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 464,410.00 USD | 0.00 USD | 1,320.00 USD | `-36.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 463,090.00 USD | 0.00 USD | 3,770.00 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 459,330.00 USD | 0.00 USD | 2,070.00 USD | `-33.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 457,250.00 USD | 0.00 USD | 3,740.00 USD | `-31.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 453,510.00 USD | 0.00 USD | 1,050.00 USD | `-30.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 452,460.00 USD | 0.00 USD | 120.90 USD | `-29.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 452,340.00 USD | 0.00 USD | 146.80 USD | `-28.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 452,190.00 USD | 0.00 USD | 124.02 USD | `-27.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 452,060.00 USD | 0.00 USD | 5,000.00 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 447,060.00 USD | 0.00 USD | 520.78 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 446,540.00 USD | 0.00 USD | 10,560.00 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 435,980.00 USD | 0.00 USD | 60,230.00 USD | `-23.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 375,750.00 USD | 0.00 USD | 1,480.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 374,270.00 USD | 0.00 USD | 52,990.00 USD | `-21.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 321,290.00 USD | 0.00 USD | 186.84 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 321,100.00 USD | 0.00 USD | 742.88 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 320,360.00 USD | 0.00 USD | 902.70 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 319,450.00 USD | 0.00 USD | 1,570.00 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 317,890.00 USD | 0.00 USD | 4,460.00 USD | `-17.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 313,430.00 USD | 0.00 USD | 194.90 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 313,230.00 USD | 0.00 USD | 232.18 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 313,000.00 USD | 0.00 USD | 7,060.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 305,950.00 USD | 0.00 USD | 518.80 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 305,430.00 USD | 0.00 USD | 19,460.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 285,970.00 USD | 0.00 USD | 686.12 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 285,280.00 USD | 0.00 USD | 2,370.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 282,910.00 USD | 0.00 USD | 24,850.00 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 258,060.00 USD | 0.00 USD | 13,710.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 244,340.00 USD | 0.00 USD | 42,800.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 201,550.00 USD | 0.00 USD | 51,460.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 150,090.00 USD | 0.00 USD | 107,370.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 42,720.00 USD | 0.00 USD | 731.75 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 41,990.00 USD | 0.00 USD | 2,220.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 39,770.00 USD | 0.00 USD | 12,710.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 27,050.00 USD | 0.00 USD | 19,870.00 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 7,190.00 USD | 0.00 USD | 1,760.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 5,430.00 USD | 0.00 USD | 5,430.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.95` | 188.34 USD | 188.34 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 78,140.00 USD | 77,950.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 102,370.00 USD | 24,230.00 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 116,920.00 USD | 14,550.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 138,560.00 USD | 21,640.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 138,950.00 USD | 396.17 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 177,020.00 USD | 38,070.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 179,810.00 USD | 2,790.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 181,250.00 USD | 1,440.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 181,360.00 USD | 110.21 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 185,190.00 USD | 3,820.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 213,160.00 USD | 27,980.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 214,980.00 USD | 1,820.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 308,380.00 USD | 93,390.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 308,970.00 USD | 597.74 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 313,870.00 USD | 4,890.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 370,640.00 USD | 56,780.00 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 376,820.00 USD | 6,180.00 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 377,500.00 USD | 679.57 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 397,870.00 USD | 20,360.00 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 398,320.00 USD | 451.95 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 414,950.00 USD | 16,630.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 415,870.00 USD | 919.19 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 417,190.00 USD | 1,320.00 USD | 0.00 USD | `+21.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 424,970.00 USD | 7,790.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 427,510.00 USD | 2,540.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 427,670.00 USD | 165.31 USD | 0.00 USD | `+24.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 428,630.00 USD | 954.14 USD | 0.00 USD | `+24.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 448,180.00 USD | 19,550.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 453,060.00 USD | 4,880.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 453,330.00 USD | 266.44 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 469,590.00 USD | 16,260.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 469,740.00 USD | 152.82 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 474,020.00 USD | 4,280.00 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 477,430.00 USD | 3,410.00 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 496,870.00 USD | 19,440.00 USD | 0.00 USD | `+32.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 497,090.00 USD | 218.25 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 499,610.00 USD | 2,520.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 506,870.00 USD | 7,270.00 USD | 0.00 USD | `+35.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 507,820.00 USD | 950.82 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 532,680.00 USD | 24,860.00 USD | 0.00 USD | `+37.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 535,130.00 USD | 2,450.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 768,170.00 USD | 233,040.00 USD | 0.00 USD | `+39.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 769,090.00 USD | 924.07 USD | 0.00 USD | `+40.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 769,990.00 USD | 893.01 USD | 0.00 USD | `+41.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 770,640.00 USD | 653.10 USD | 0.00 USD | `+42.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 771,110.00 USD | 472.63 USD | 0.00 USD | `+43.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 774,410.00 USD | 3,290.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 777,580.00 USD | 3,170.00 USD | 0.00 USD | `+45.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 782,710.00 USD | 5,130.00 USD | 0.00 USD | `+46.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 797,790.00 USD | 15,080.00 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 804,590.00 USD | 6,800.00 USD | 0.00 USD | `+47.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 811,090.00 USD | 6,500.00 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 817,630.00 USD | 6,540.00 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 824,210.00 USD | 6,580.00 USD | 0.00 USD | `+50.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 834,140.00 USD | 9,930.00 USD | 0.00 USD | `+51.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 938,120.00 USD | 103,980.00 USD | 0.00 USD | `+52.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 952,360.00 USD | 14,240.00 USD | 0.00 USD | `+53.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 1,040,000.00 USD | 84,360.00 USD | 0.00 USD | `+54.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 1,040,000.00 USD | 1,700.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 1,050,000.00 USD | 7,370.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 1,060,000.00 USD | 16,690.00 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 1,060,000.00 USD | 2,300.00 USD | 0.00 USD | `+57.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,070,000.00 USD | 1,740.00 USD | 0.00 USD | `+58.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,090,000.00 USD | 21,690.00 USD | 0.00 USD | `+59.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,090,000.00 USD | 4,390.00 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,100,000.00 USD | 4,410.00 USD | 0.00 USD | `+61.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,100,000.00 USD | 4,440.00 USD | 0.00 USD | `+62.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,110,000.00 USD | 4,460.00 USD | 0.00 USD | `+63.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,110,000.00 USD | 448.75 USD | 0.00 USD | `+64.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,140,000.00 USD | 30,960.00 USD | 0.00 USD | `+65.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,140,000.00 USD | 453.75 USD | 0.00 USD | `+66.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,140,000.00 USD | 456.25 USD | 0.00 USD | `+67.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,140,000.00 USD | 458.75 USD | 0.00 USD | `+67.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,140,000.00 USD | 461.25 USD | 0.00 USD | `+68.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,140,000.00 USD | 4,540.00 USD | 0.00 USD | `+69.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,140,000.00 USD | 466.25 USD | 0.00 USD | `+70.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,140,000.00 USD | 468.75 USD | 0.00 USD | `+71.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,150,000.00 USD | 471.25 USD | 0.00 USD | `+72.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,150,000.00 USD | 473.75 USD | 0.00 USD | `+73.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,210,000.00 USD | 67,000.00 USD | 0.00 USD | `+74.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,210,000.00 USD | 574.50 USD | 0.00 USD | `+75.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,210,000.00 USD | 577.50 USD | 0.00 USD | `+76.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,220,000.00 USD | 2,710.00 USD | 0.00 USD | `+77.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,220,000.00 USD | 972.50 USD | 0.00 USD | `+78.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,230,000.00 USD | 7,680.00 USD | 0.00 USD | `+78.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,230,000.00 USD | 786.00 USD | 0.00 USD | `+79.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,230,000.00 USD | 790.00 USD | 0.00 USD | `+80.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,230,000.00 USD | 992.50 USD | 0.00 USD | `+81.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,230,000.00 USD | 997.50 USD | 0.00 USD | `+82.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,830,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+83.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,830,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,830,000.00 USD | 1,010.00 USD | 0.00 USD | `+85.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,830,000.00 USD | 1,020.00 USD | 0.00 USD | `+86.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+87.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+88.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+89.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,840,000.00 USD | 1,040.00 USD | 0.00 USD | `+89.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,840,000.00 USD | 1,410.00 USD | 0.00 USD | `+90.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,840,000.00 USD | 1,050.00 USD | 0.00 USD | `+91.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,850,000.00 USD | 4,000.00 USD | 0.00 USD | `+92.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+94.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,890,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+95.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,900,000.00 USD | 1,070.00 USD | 0.00 USD | `+96.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+97.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+98.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,900,000.00 USD | 1,090.00 USD | 0.00 USD | `+99.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,900,000.00 USD | 3,280.00 USD | 0.00 USD | `+100.04%` | `TACTICAL (Retail Cluster)` |

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
| `1D` | `9.58` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 47,290.00 USD | 7,810.00 USD | 47,330.00 USD |
| `7D` | `9.58` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 38,760.00 USD | 722.15 USD | 4,200.00 USD |
| `1D` | `9.60` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 40,390.00 USD | 17,890.00 USD | 78,400.00 USD |
| `7D` | `9.60` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD |
| `1D` | `9.62` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 1,760.00 USD | 255.00 USD | 14,300.00 USD |
| `7D` | `9.62` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 5,420.00 USD | 0.00 USD | 11.28 USD |
| `1D` | `9.64` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 5,330.00 USD | 2,460.00 USD | 177.67 USD |
| `7D` | `9.64` | 12,170,000.00 USD | 0.00 USD | 12,170,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,460.00 USD |
| `1D` | `9.66` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 3,650.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `9.66` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.68` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 2,330.00 USD | 107.93 USD | 33,770.00 USD |
| `7D` | `9.68` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.70` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 10,930.00 USD | 118.50 USD | 15,990.00 USD |
| `7D` | `9.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 7,710.00 USD | 0.00 USD | 379.91 USD |
| `1D` | `9.72` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 3,050.00 USD | 3,290.00 USD | 14,340.00 USD |
| `7D` | `9.72` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.74` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 1,530.00 USD | 0.00 USD | 14,880.00 USD |
| `7D` | `9.74` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 2,070.00 USD | 0.00 USD | 413.42 USD |
| `1D` | `9.76` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 96,370.00 USD | 689.80 USD | 13,580.00 USD |
| `7D` | `9.76` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 50,080.00 USD | 0.00 USD | 26,530.00 USD |
| `1D` | `9.78` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 55,890.00 USD | 7,220.00 USD | 24,630.00 USD |
| `7D` | `9.78` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 0.00 USD | 671.70 USD | 1,420.00 USD |
| `1D` | `9.80` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 44,560.00 USD | 5,670.00 USD | 188.73 USD |
| `7D` | `9.80` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 47,490.00 USD | 14,120.00 USD | 25,050.00 USD |
| `1D` | `9.82` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 85,490.00 USD | 14,930.00 USD | 27,480.00 USD |
| `7D` | `9.82` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `9.84` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 17,970.00 USD | 7,030.00 USD | 0.00 USD |
| `7D` | `9.84` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 50,980.00 USD | 456.90 USD | 13,280.00 USD |
| `1D` | `9.86` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 23,360.00 USD | 3,910.00 USD | 10,270.00 USD |
| `7D` | `9.86` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD |
| `1D` | `9.88` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 2,240.00 USD | 8,620.00 USD | 5,510.00 USD |
| `7D` | `9.88` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 10,280.00 USD | 15,600.00 USD | 786.13 USD |
| `1D` | `9.90` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 37,440.00 USD | 27,290.00 USD | 5,210.00 USD |
| `7D` | `9.90` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 48,670.00 USD | 0.00 USD | 703.81 USD |
| `1D` | `9.92` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 14,940.00 USD | 17,480.00 USD | 229.89 USD |
| `7D` | `9.92` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 0.00 USD | 12,280.00 USD | 551.50 USD |
| `1D` | `9.94` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 1,820.00 USD | 792.40 USD | 849.54 USD |
| `7D` | `9.94` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,000.00 USD |
| `1D` | `9.96` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 62,740.00 USD | 13,640.00 USD | 16,330.00 USD |
| `7D` | `9.96` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 0.00 USD | 11,410.00 USD | 1,900.00 USD |
| `1D` | `9.98` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 5,450.00 USD | 6,740.00 USD | 58,110.00 USD |
| `7D` | `9.98` | 11,530,000.00 USD | 0.00 USD | 11,530,000.00 USD | 4,830.00 USD | 598.17 USD | 59,210.00 USD |
| `1D` | `10.00` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 1,940.00 USD | 254.10 USD | 51,530.00 USD |
| `7D` | `10.00` | 11,460,000.00 USD | 0.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 13,240.00 USD |
| `1D` | `10.02` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 5,440.00 USD | 13,120.00 USD | 18,560.00 USD |
| `7D` | `10.02` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 8,880.00 USD | 317.30 USD | 415.56 USD |
| `1D` | `10.04` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 18,000.00 USD | 305.90 USD | 337.58 USD |
| `7D` | `10.04` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 7,200.00 USD | 1,210.00 USD | 146.67 USD |
| `1D` | `10.06` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,510.00 USD |
| `7D` | `10.06` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 83,650.00 USD |
| `1D` | `10.08` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 167,250.00 USD | 701.42 USD | 75,830.00 USD |
| `7D` | `10.08` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 218,980.00 USD | 351.10 USD | 111,570.00 USD |
| `1D` | `10.10` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 7,570.00 USD | 42,810.00 USD | 353.44 USD |
| `7D` | `10.10` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 6,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.12` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 1,150.00 USD | 20,910.00 USD | 305.38 USD |
| `7D` | `10.12` | 11,010,000.00 USD | 0.00 USD | 11,010,000.00 USD | 10,140.00 USD | 559.40 USD | 55,860.00 USD |
| `1D` | `10.14` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,900.00 USD |
| `7D` | `10.14` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,210.00 USD |
| `1D` | `10.16` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,400.00 USD |
| `7D` | `10.16` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,210.00 USD |
| `1D` | `10.18` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 80,470.00 USD | 36,910.00 USD | 155,980.00 USD |
| `7D` | `10.18` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,940.00 USD |
| `1D` | `10.20` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,080.00 USD |
| `7D` | `10.20` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,660.00 USD |
| `1D` | `10.22` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 37,870.00 USD | 22,340.00 USD | 344,560.00 USD |
| `7D` | `10.22` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,080.00 USD |
| `1D` | `10.24` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 122,230.00 USD | 71,270.00 USD | 22,390.00 USD |
| `7D` | `10.24` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,090.00 USD |
| `1D` | `10.26` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 66,420.00 USD | 8,070.00 USD | 100,890.00 USD |
| `7D` | `10.26` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,490.00 USD |
| `1D` | `10.28` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 172,700.00 USD | 12,030.00 USD | 176,290.00 USD |
| `7D` | `10.28` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,580.00 USD |
| `1D` | `10.30` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 169,020.00 USD | 20,970.00 USD | 49,800.00 USD |
| `7D` | `10.30` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 457,980.00 USD | 0.00 USD | 267.66 USD |
| `1D` | `10.32` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 26,300.00 USD | 1,390.00 USD | 82,420.00 USD |
| `7D` | `10.32` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 43,210.00 USD | 0.00 USD | 99,860.00 USD |
| `1D` | `10.34` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 73,380.00 USD | 9,100.00 USD | 93,530.00 USD |
| `7D` | `10.34` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 56,680.00 USD | 0.00 USD | 146.32 USD |
| `1D` | `10.36` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 5,630.00 USD | 3,580.00 USD | 69.62 USD |
| `7D` | `10.36` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 294,520.00 USD | 0.00 USD | 103,880.00 USD |
| `1D` | `10.38` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 40,040.00 USD | 46,620.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,760.00 USD |
| `7D` | `10.40` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 255,660.00 USD | 0.00 USD | 313.96 USD |
| `7D` | `10.42` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD |
| `1D` | `10.44` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 214,390.00 USD | 27,590.00 USD | 305,400.00 USD |
| `7D` | `10.44` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,110.00 USD |
| `7D` | `10.46` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.48` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 50,100.00 USD | 2,200.00 USD | 55,170.00 USD |
| `7D` | `10.48` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,100.00 USD |
| `7D` | `10.50` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.52` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 71.67 USD | 10,910.00 USD | 38,150.00 USD |
| `7D` | `10.52` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 0.00 USD | 57,000.00 USD | 132,300.00 USD |
| `7D` | `10.54` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD |
| `1D` | `10.56` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 94,750.00 USD | 23,930.00 USD | 12,820.00 USD |
| `7D` | `10.56` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD |
| `1D` | `10.58` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 28,610.00 USD | 20,070.00 USD | 20,290.00 USD |
| `1D` | `10.60` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 4,790.00 USD | 79.66 USD |
| `1D` | `10.62` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 3,670.00 USD | 118,210.00 USD |
| `7D` | `10.62` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 8,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.64` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 11,820.00 USD | 660.00 USD | 23,920.00 USD |
| `7D` | `10.64` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 11,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.66` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 29,760.00 USD | 3,400.00 USD | 0.00 USD |
| `7D` | `10.66` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 9,470.00 USD | 0.00 USD | 57.50 USD |
| `1D` | `10.68` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 0.00 USD | 9,610.00 USD | 36,190.00 USD |
| `7D` | `10.68` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 2,430.00 USD | 253.63 USD |
| `1D` | `10.70` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 12,670.00 USD | 7,160.00 USD | 237.93 USD |
| `7D` | `10.70` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.72` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 83,030.00 USD | 23,680.00 USD | 14.66 USD |
| `7D` | `10.74` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 877.75 USD | 100,050.00 USD |
| `1D` | `10.76` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 6,560.00 USD | 47,140.00 USD | 25,950.00 USD |
| `7D` | `10.76` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 16,310.00 USD | 109,140.00 USD | 364.26 USD |
| `1D` | `10.78` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 190,290.00 USD | 134,860.00 USD | 25,630.00 USD |
| `7D` | `10.78` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 535,020.00 USD | 32,650.00 USD | 104,040.00 USD |
| `1D` | `10.80` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 13,650.00 USD | 3,750.00 USD | 9,950.00 USD |
| `7D` | `10.80` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 23,450.00 USD | 70,260.00 USD | 429.69 USD |
| `1D` | `10.82` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 88,080.00 USD | 2,860.00 USD | 0.00 USD |
| `7D` | `10.82` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 56,610.00 USD | 206,610.00 USD |
| `1D` | `10.84` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 308,110.00 USD | 2,970.00 USD | 20.88 USD |
| `7D` | `10.84` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 193,810.00 USD | 80,420.00 USD | 196,250.00 USD |
| `1D` | `10.86` | 939,550.00 USD | 0.00 USD | 939,550.00 USD | 7,110.00 USD | 17,680.00 USD | 148,530.00 USD |
| `7D` | `10.86` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 334,140.00 USD |
| `1D` | `10.88` | 766,230.00 USD | 0.00 USD | 766,230.00 USD | 0.00 USD | 1,270.00 USD | 12.95 USD |
| `7D` | `10.88` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 111,430.00 USD | 39,120.00 USD | 347,180.00 USD |
| `1D` | `10.90` | 764,950.00 USD | 0.00 USD | 764,950.00 USD | 37,360.00 USD | 2,950.00 USD | 46.37 USD |
| `7D` | `10.90` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 221,070.00 USD |
| `1D` | `10.92` | 724,600.00 USD | 0.00 USD | 724,600.00 USD | 80,530.00 USD | 0.00 USD | 258.27 USD |
| `7D` | `10.92` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 226,910.00 USD | 0.00 USD | 111,880.00 USD |
| `1D` | `10.94` | 643,810.00 USD | 0.00 USD | 643,810.00 USD | 4,370.00 USD | 1,550.00 USD | 19.56 USD |
| `7D` | `10.94` | 725,060.00 USD | 0.00 USD | 725,060.00 USD | 2,480.00 USD | 0.00 USD | 380.88 USD |
| `1D` | `10.96` | 637,860.00 USD | 0.00 USD | 637,860.00 USD | 1,090.00 USD | 784.50 USD | 87,770.00 USD |
| `7D` | `10.96` | 722,200.00 USD | 0.00 USD | 722,200.00 USD | 10,430.00 USD | 0.00 USD | 50,870.00 USD |
| `1D` | `10.98` | 548,220.00 USD | 0.00 USD | 548,220.00 USD | 0.00 USD | 0.00 USD | 694.26 USD |
| `7D` | `10.98` | 660,910.00 USD | 0.00 USD | 660,910.00 USD | 17,930.00 USD | 0.00 USD | 209,750.00 USD |
| `1D` | `11.00` | 547,530.00 USD | 0.00 USD | 547,530.00 USD | 0.00 USD | 2,520.00 USD | 105.88 USD |
| `7D` | `11.00` | 433,230.00 USD | 0.00 USD | 433,230.00 USD | 10,830.00 USD | 2,280.00 USD | 2,070.00 USD |
| `1D` | `11.02` | 544,900.00 USD | 0.00 USD | 544,900.00 USD | 5,330.00 USD | 27,810.00 USD | 151,280.00 USD |
| `7D` | `11.02` | 418,050.00 USD | 0.00 USD | 418,050.00 USD | 7,900.00 USD | 31,180.00 USD | 143,040.00 USD |
| `1D` | `11.04` | 360,480.00 USD | 0.00 USD | 360,480.00 USD | 163,320.00 USD | 18,120.00 USD | 179,040.00 USD |
| `7D` | `11.04` | 235,930.00 USD | 0.00 USD | 235,930.00 USD | 17,850.00 USD | 40,210.00 USD | 177,880.00 USD |
| `1D` | `11.05` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.05` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.06` | 659,110.00 USD | 659,110.00 USD | 0.00 USD | 518,210.00 USD | 33,960.00 USD | 106,950.00 USD |
| `7D` | `11.06` | 483,970.00 USD | 483,970.00 USD | 0.00 USD | 351,320.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.08` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 332,930.00 USD | 71,110.00 USD | 445,850.00 USD |
| `7D` | `11.08` | 825,050.00 USD | 825,050.00 USD | 0.00 USD | 171,900.00 USD | 1,810.00 USD | 167,370.00 USD |
| `1D` | `11.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 215,070.00 USD | 45,260.00 USD | 353.04 USD |
| `7D` | `11.10` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 301,790.00 USD | 23,300.00 USD | 173,740.00 USD |
| `1D` | `11.12` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 448,790.00 USD | 109,110.00 USD | 179,820.00 USD |
| `7D` | `11.12` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 262,770.00 USD | 115,910.00 USD | 234,130.00 USD |
| `1D` | `11.14` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 230,290.00 USD | 19,930.00 USD | 67,920.00 USD |
| `7D` | `11.14` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 1,350.00 USD |
| `1D` | `11.16` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 127,020.00 USD | 79,690.00 USD | 50,960.00 USD |
| `7D` | `11.16` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 64,850.00 USD |
| `1D` | `11.18` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 71,610.00 USD | 44,050.00 USD | 86,430.00 USD |
| `7D` | `11.18` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 1,420.00 USD |
| `1D` | `11.20` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 65,400.00 USD | 61,120.00 USD | 87,500.00 USD |
| `7D` | `11.20` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 171,840.00 USD | 78,020.00 USD | 78,710.00 USD |
| `1D` | `11.22` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 352,600.00 USD | 47,950.00 USD | 117,630.00 USD |
| `7D` | `11.22` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 482,460.00 USD | 28,690.00 USD | 0.00 USD |
| `1D` | `11.24` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 110,930.00 USD | 34,630.00 USD | 202,650.00 USD |
| `7D` | `11.24` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.26` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 130,470.00 USD | 13,530.00 USD | 105,580.00 USD |
| `7D` | `11.26` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 520,990.00 USD | 0.00 USD | 296,480.00 USD |
| `1D` | `11.28` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 293,730.00 USD | 56,750.00 USD | 243,800.00 USD |
| `7D` | `11.28` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 245,580.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.30` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 65,700.00 USD | 74,380.00 USD | 112,850.00 USD |
| `7D` | `11.30` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 20,580.00 USD |
| `1D` | `11.32` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 119,640.00 USD | 66,500.00 USD | 82,820.00 USD |
| `7D` | `11.32` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 280,300.00 USD |
| `1D` | `11.34` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 344,010.00 USD | 109,770.00 USD | 58,390.00 USD |
| `7D` | `11.34` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD |
| `1D` | `11.36` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 115,970.00 USD | 93,260.00 USD | 56,340.00 USD |
| `7D` | `11.36` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,340.00 USD |
| `7D` | `11.38` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 74,750.00 USD |
| `1D` | `11.40` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 39,080.00 USD | 32,990.00 USD | 104,540.00 USD |
| `7D` | `11.40` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 112,540.00 USD | 68,020.00 USD | 91,820.00 USD |
| `7D` | `11.42` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD |
| `1D` | `11.44` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 84,630.00 USD | 40,410.00 USD | 84,360.00 USD |
| `7D` | `11.44` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 303,190.00 USD | 95,260.00 USD | 38,840.00 USD |
| `1D` | `11.46` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 59,980.00 USD | 65,340.00 USD | 48,870.00 USD |
| `7D` | `11.46` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 99,360.00 USD | 55,470.00 USD | 0.00 USD |
| `1D` | `11.48` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 14,620.00 USD | 15,390.00 USD | 64.87 USD |
| `7D` | `11.48` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 54,660.00 USD | 84,840.00 USD | 64,880.00 USD |
| `1D` | `11.50` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 31,090.00 USD | 33,490.00 USD | 46,130.00 USD |
| `7D` | `11.50` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 40,840.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 29,590.00 USD | 13,890.00 USD | 19,390.00 USD |
| `7D` | `11.52` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 33,270.00 USD |
| `1D` | `11.54` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 60,850.00 USD | 16,150.00 USD | 71,230.00 USD |
| `7D` | `11.54` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,340.00 USD |
| `1D` | `11.56` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 90,400.00 USD | 4,570.00 USD | 23,110.00 USD |
| `7D` | `11.56` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 86,650.00 USD | 793.25 USD | 0.00 USD |
| `1D` | `11.58` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 46,550.00 USD | 335.85 USD | 17,550.00 USD |
| `7D` | `11.58` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `11.60` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 91,240.00 USD | 7,320.00 USD | 67,330.00 USD |
| `7D` | `11.60` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 44,670.00 USD | 10,510.00 USD | 22,780.00 USD |
| `1D` | `11.62` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 44,130.00 USD | 512.95 USD | 47,810.00 USD |
| `7D` | `11.62` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.64` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 4,510.00 USD | 7,410.00 USD | 31,500.00 USD |
| `7D` | `11.64` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 186.31 USD |
| `1D` | `11.66` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,610.00 USD |
| `7D` | `11.66` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,310.00 USD |
| `1D` | `11.68` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 124,510.00 USD | 35,770.00 USD | 31,880.00 USD |
| `7D` | `11.68` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,290.00 USD |
| `1D` | `11.70` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 4,760.00 USD | 15,560.00 USD |
| `7D` | `11.70` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD |
| `1D` | `11.72` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 187,700.00 USD | 18,090.00 USD | 98,210.00 USD |
| `7D` | `11.72` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,380.00 USD |
| `1D` | `11.74` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 75,970.00 USD | 30,440.00 USD | 73,470.00 USD |
| `7D` | `11.74` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,340.00 USD |
| `1D` | `11.76` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 26,090.00 USD | 15,090.00 USD | 24,570.00 USD |
| `7D` | `11.76` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,610.00 USD |
| `1D` | `11.78` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 27,290.00 USD | 21,040.00 USD | 40,030.00 USD |
| `7D` | `11.78` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 57,000.00 USD |
| `1D` | `11.80` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 1,190.00 USD | 18,420.00 USD | 0.00 USD |
| `7D` | `11.80` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 11,070.00 USD | 53.10 USD | 36,260.00 USD |
| `7D` | `11.82` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 71,130.00 USD | 11,870.00 USD | 60,860.00 USD |
| `7D` | `11.84` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,560.00 USD |
| `1D` | `11.86` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 10,930.00 USD | 14,080.00 USD | 51,000.00 USD |
| `7D` | `11.86` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 100.22 USD |
| `1D` | `11.88` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 19,750.00 USD | 29,160.00 USD | 60,280.00 USD |
| `7D` | `11.88` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,830.00 USD |
| `1D` | `11.90` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 43,700.00 USD | 8,750.00 USD | 28,050.00 USD |
| `7D` | `11.90` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 298.16 USD |
| `1D` | `11.92` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 230,070.00 USD | 23,160.00 USD | 25,320.00 USD |
| `7D` | `11.92` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,850.00 USD |
| `1D` | `11.94` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 48,250.00 USD | 15,310.00 USD | 40,190.00 USD |
| `7D` | `11.94` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,550.00 USD |
| `1D` | `11.96` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 64,140.00 USD | 40,240.00 USD | 48,070.00 USD |
| `7D` | `11.96` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,020.00 USD |
| `1D` | `11.98` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 78,260.00 USD | 29,060.00 USD | 81,750.00 USD |
| `7D` | `11.98` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,840.00 USD |
| `1D` | `12.00` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 120,680.00 USD | 24,160.00 USD | 51,070.00 USD |
| `7D` | `12.00` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 221,970.00 USD |
| `1D` | `12.02` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 30,340.00 USD | 16,500.00 USD | 31,440.00 USD |
| `7D` | `12.02` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,420.00 USD |
| `1D` | `12.04` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 113,250.00 USD | 48,840.00 USD | 62,850.00 USD |
| `7D` | `12.04` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,730.00 USD |
| `1D` | `12.06` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 113,790.00 USD | 49,180.00 USD | 72,690.00 USD |
| `7D` | `12.06` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,770.00 USD |
| `1D` | `12.08` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 38,930.00 USD | 35,220.00 USD | 48,320.00 USD |
| `7D` | `12.08` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,470.00 USD |
| `1D` | `12.10` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 48,930.00 USD | 20,220.00 USD | 27,560.00 USD |
| `7D` | `12.10` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,130.00 USD |
| `1D` | `12.12` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 108,350.00 USD | 51,990.00 USD | 50,400.00 USD |
| `7D` | `12.12` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,520.00 USD |
| `1D` | `12.14` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 76,660.00 USD | 33,190.00 USD | 55,690.00 USD |
| `7D` | `12.14` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 147,420.00 USD | 92,520.00 USD | 119,100.00 USD |
| `1D` | `12.16` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 125,380.00 USD | 34,710.00 USD | 67,530.00 USD |
| `7D` | `12.16` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,180.00 USD |
| `1D` | `12.18` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 106,900.00 USD | 46,460.00 USD | 41,160.00 USD |
| `7D` | `12.18` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 57,680.00 USD | 54,220.00 USD | 32,140.00 USD |
| `1D` | `12.20` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 43,510.00 USD | 17,410.00 USD | 4,530.00 USD |
| `7D` | `12.20` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 91,440.00 USD |
| `7D` | `12.22` | 15,910,000.00 USD | 15,910,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 106,040.00 USD |
| `7D` | `12.24` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 70,650.00 USD | 54,230.00 USD | 114,730.00 USD |
| `7D` | `12.26` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 192,800.00 USD | 55,780.00 USD | 50,780.00 USD |
| `7D` | `12.28` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 215,790.00 USD | 64,650.00 USD | 171,450.00 USD |
| `7D` | `12.30` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 97,010.00 USD |
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
  * Total Open Interest: `518.72M` | Total OI Tokens: `47,039,059.3 LINK`
  * 1h OI Change: `+0.45%` | 4h OI Change: `+0.52%` | 24h OI Change: `-5.87%`
  * Exchange Breakdown: Binance=`102.16M` | Bybit=`70.56M` | OKX=`27.08M` | Hyperliquid=`55.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-9.70K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0050%` | **USDT OKX** | `-0.0057%` |
| **USDT Bybit** | `-0.0201%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0050%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0085%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `47.74%` | `52.26%` | `0.91` | 3,160,000.00 USD |
| `15M` | `Binance` | `48.04%` | `51.96%` | `0.92` | 1,280,000.00 USD |
| `15M` | `OKX` | `57.27%` | `42.73%` | `1.34` | 251,270.00 USD |
| `15M` | `Bybit` | `38.47%` | `61.53%` | `0.63` | 373,100.00 USD |
| `15M` | `KuCoin` | `38.05%` | `61.95%` | `0.61` | 16,720.00 USD |
| `15M` | `Gate` | `77.09%` | `22.91%` | `3.36` | 132,090.00 USD |
| `15M` | `Bitget` | `46.6%` | `53.4%` | `0.87` | 76,110.00 USD |
| `15M` | `BingX` | `56.18%` | `43.82%` | `1.28` | 113,410.00 USD |
| `15M` | `MEXC` | `26.16%` | `73.84%` | `0.35` | 127,420.00 USD |
| `15M` | `Bitunix` | `43.15%` | `56.85%` | `0.76` | 62,540.00 USD |
| `15M` | `Hyperliquid` | `81.05%` | `18.95%` | `4.28` | 22,660.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.66%` | `50.34%` | `0.99` | 601,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 49,860.00 USD |
| `15M` | `HTX` | `49.94%` | `50.06%` | `1.00` | 13,560.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 53.99 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `34.08%` | `65.92%` | `0.52` | 31,130.00 USD |
| `15M` | `Whale Positions` | `48.04%` | `51.96%` | `0.92` | 1,280,000.00 USD |
| `15M` | `Global Accounts` | `47.74%` | `52.26%` | `0.91` | 3,160,000.00 USD |
| `1H` | `LINK` | `46.99%` | `53.01%` | `0.89` | 38,390,000.00 USD |
| `1H` | `Binance` | `48.12%` | `51.88%` | `0.93` | 17,730,000.00 USD |
| `1H` | `OKX` | `44.43%` | `55.57%` | `0.80` | 6,140,000.00 USD |
| `1H` | `Bybit` | `48.17%` | `51.83%` | `0.93` | 6,580,000.00 USD |
| `1H` | `KuCoin` | `49.66%` | `50.34%` | `0.99` | 773,310.00 USD |
| `1H` | `Gate` | `38.6%` | `61.4%` | `0.63` | 2,080,000.00 USD |
| `1H` | `Bitget` | `43.74%` | `56.26%` | `0.78` | 1,550,000.00 USD |
| `1H` | `BingX` | `47.06%` | `52.94%` | `0.89` | 192,200.00 USD |
| `1H` | `MEXC` | `52.78%` | `47.22%` | `1.12` | 602,140.00 USD |
| `1H` | `Bitunix` | `44.79%` | `55.21%` | `0.81` | 565,590.00 USD |
| `1H` | `Hyperliquid` | `44.82%` | `55.18%` | `0.81` | 1,220,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.24%` | `48.76%` | `1.05` | 470,290.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `76.14%` | `23.86%` | `3.19` | 176,970.00 USD |
| `1H` | `HTX` | `43.93%` | `56.07%` | `0.78` | 150,270.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `52.65%` | `47.35%` | `1.11` | 12,460.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.17%` | `39.83%` | `1.51` | 157,220.00 USD |
| `1H` | `Whale Positions` | `48.12%` | `51.88%` | `0.93` | 17,730,000.00 USD |
| `1H` | `Global Accounts` | `46.99%` | `53.01%` | `0.89` | 38,390,000.00 USD |
| `4H` | `LINK` | `49.15%` | `50.85%` | `0.97` | 172,750,000.00 USD |
| `4H` | `Binance` | `51.11%` | `48.89%` | `1.05` | 72,000,000.00 USD |
| `4H` | `OKX` | `48.95%` | `51.05%` | `0.96` | 22,960,000.00 USD |
| `4H` | `Bybit` | `50.87%` | `49.13%` | `1.04` | 32,940,000.00 USD |
| `4H` | `KuCoin` | `50.4%` | `49.6%` | `1.02` | 3,410,000.00 USD |
| `4H` | `Gate` | `42.48%` | `57.52%` | `0.74` | 11,370,000.00 USD |
| `4H` | `Bitget` | `48.96%` | `51.04%` | `0.96` | 6,660,000.00 USD |
| `4H` | `BingX` | `29.58%` | `70.42%` | `0.42` | 1,790,000.00 USD |
| `4H` | `MEXC` | `51.93%` | `48.07%` | `1.08` | 3,180,000.00 USD |
| `4H` | `Bitunix` | `49.27%` | `50.73%` | `0.97` | 2,600,000.00 USD |
| `4H` | `Hyperliquid` | `56.27%` | `43.73%` | `1.29` | 6,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.53%` | `51.47%` | `0.94` | 2,250,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `21.88%` | `78.12%` | `0.28` | 4,520,000.00 USD |
| `4H` | `HTX` | `48.06%` | `51.94%` | `0.93` | 682,160.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `33.23%` | `66.77%` | `0.50` | 1,140,000.00 USD |
| `4H` | `Aster` | `42.2%` | `57.8%` | `0.73` | 245,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `58.54%` | `41.46%` | `1.41` | 684,860.00 USD |
| `4H` | `Whale Positions` | `51.11%` | `48.89%` | `1.05` | 72,000,000.00 USD |
| `4H` | `Global Accounts` | `49.15%` | `50.85%` | `0.97` | 172,750,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `10.66` | `10.66` | `10.66` | `10.72` | `10.57` | 8,088,225.29 USD | 5,081,569.93 USD | 3,006,655.36 USD | 2,074,914.56 USD | `+25.65%` | `34B / 2S` |
| `0:00 UTC` | `10.72` | `10.71` | `10.72` | `10.74` | `10.66` | 2,303,326.18 USD | 1,025,885.42 USD | 1,277,440.76 USD | -251,555.33 USD | `-10.92%` | `6B / 12S` |
| `5:00 UTC` | `10.70` | `10.70` | `10.70` | `10.73` | `10.67` | 1,515,260.65 USD | 804,867.83 USD | 710,392.82 USD | 94,475.01 USD | `+6.23%` | `8B / 5S` |
| `0:00 UTC` | `10.77` | `10.75` | `10.77` | `10.78` | `10.71` | 1,791,807.07 USD | 1,021,807.03 USD | 770,000.04 USD | 251,806.99 USD | `+14.05%` | `17B / 3S` |
| `5:00 UTC` | `10.80` | `10.78` | `10.80` | `10.81` | `10.74` | 1,669,099.58 USD | 861,868.55 USD | 807,231.03 USD | 54,637.51 USD | `+3.27%` | `11B / 7S` |
| `0:00 UTC` | `10.91` | `10.88` | `10.91` | `10.95` | `10.78` | 3,369,524.30 USD | 1,989,204.80 USD | 1,380,319.50 USD | 608,885.30 USD | `+18.07%` | `47B / 26S` |
| `5:00 UTC` | `10.94` | `10.95` | `10.94` | `10.98` | `10.93` | 1,915,931.41 USD | 933,547.46 USD | 982,383.95 USD | -48,836.49 USD | `-2.55%` | `2B / 6S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `10.99` | `10.90` | 2,589,400.57 USD | 1,319,072.00 USD | 1,270,328.57 USD | 48,743.44 USD | `+1.88%` | `17B / 14S` |
| `5:00 UTC` | `10.99` | `10.99` | `10.99` | `11.02` | `10.96` | 1,907,525.28 USD | 901,785.44 USD | 1,005,739.84 USD | -103,954.39 USD | `-5.45%` | `12B / 13S` |
| `0:00 UTC` | `10.99` | `11.00` | `10.99` | `11.02` | `10.96` | 3,702,533.73 USD | 1,914,481.64 USD | 1,788,052.09 USD | 126,429.55 USD | `+3.41%` | `6B / 12S` |

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
| `5m` | -66,770.00 USD | -12,350.00 USD | **`DISTRIBUTION`** |
| `15m` | -500,460.00 USD | -929,880.00 USD | **`DISTRIBUTION`** |
| `30m` | -630,760.00 USD | -734,130.00 USD | **`DISTRIBUTION`** |
| `1h` | -677,300.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -327,130.00 USD | 485,880.00 USD | **`ACCUMULATION`** |
| `4h` | 246,930.00 USD | 2,770,000.00 USD | **`ACCUMULATION`** |
| `6h` | -4,810,000.00 USD | -2,440,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -9,080,000.00 USD | -20,900,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,270,000.00 USD | -23,030,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,480,000.00 USD | -20,730,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,470,000.00 USD | -45,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,050,000.00 USD | -198,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-66.77K` | 15m=`-500.46K` | 1h=`-677.30K` | 24h=`-10.48M`
* Futures Capital Netflows: 5m=`-12.35K` | 15m=`-929.88K` | 1h=`-1.43M` | 24h=`-20.73M`
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
  * `2026-10-30 09:50:55 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:55 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:10:55 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `10.09` (Risk Distance: `0.2642` pts)
  * +2.5R Take Profit: `11.01`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.88` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.15` (Risk Distance: `0.2642` pts)
  * +2.5R Take Profit: `10.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.08`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
