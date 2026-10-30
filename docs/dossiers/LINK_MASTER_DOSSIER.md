# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 15:12:01 IST` (`2026-10-30 09:42:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.94` | **Live Ask Quote**: `11.02` | **Mid Price**: `10.98`
- **Spread Points**: `86.00` | **Spread BPS**: `78.33 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.75` | VWAP Z-Score: `+0.70` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0828` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.93` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.55` | Lower -3.00σ Band: `9.95`
  * Upper +2.51σ Band: `11.42` | Lower -2.51σ Band: `10.08`
  * Upper +2.01σ Band: `11.29` | Lower -2.01σ Band: `10.21`
  * Upper +2.00σ Band: `11.28` | Lower -2.00σ Band: `10.21`
  * Upper +1.28σ Band: `11.09` | Lower -1.28σ Band: `10.41`
  * Upper +1.00σ Band: `11.02` | Lower -1.00σ Band: `10.48`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.96` | EMA-20=`10.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.98` (Slope: `+0.0000`) | EMA-100=`11.11`
  * Institutional Anchors: EMA-144=`11.20` | EMA-200=`11.26` (Slope: `-0.3120`) | EMA-233=`11.29`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-1.29%`)
  * Point of Control (POC) = `11.04` (Distance: `-0.61%`)
  * Value Area Low (VAL) = `10.55` (Distance: `+4.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.78` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.89`
  * New York Session (13:00-21:00 UTC): High=`11.04` | Low=`10.91`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.94` - `11.02`
  * Optimal Trade Entry (OTE 0.705): `11.00`
  * Structural Invalidation Anchor (0.786): `11.07`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.00` | `11.00` | `10.95` | `10.98` | `50,514` | 554,510.87 USD | -90,806.09 USD | `-16.38%` | -12,719,823.09 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.98` | `11.00` | `10.98` | `11.00` | `25,185` | 276,752.75 USD | 8,356.29 USD | `+3.02%` | -12,711,466.80 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `11.00` | `11.00` | `10.99` | `10.99` | `3,568` | 39,245.71 USD | 1,377.41 USD | `+3.51%` | -12,710,089.39 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.01` | `11.03` | `10.97` | `10.99` | `174,200` | 1,915,299.28 USD | -303,320.17 USD | `-15.84%` | -12,553,347.82 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `10.99` | `11.01` | `10.96` | `11.00` | `99,172` | 1,089,442.23 USD | -75,669.18 USD | `-6.95%` | -12,629,017.00 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.00` | `11.00` | `10.95` | `10.99` | `79,271` | 870,546.93 USD | -81,066.01 USD | `-9.31%` | -12,710,083.01 USD | `-0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.13` | `11.15` | `11.00` | `11.04` | `706,212` | 7,823,977.42 USD | -443,394.34 USD | `-5.67%` | -11,819,138.86 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.04` | `11.11` | `10.99` | `11.01` | `546,831` | 6,037,228.26 USD | -347,696.97 USD | `-5.76%` | -12,166,835.83 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.01` | `11.03` | `10.95` | `10.99` | `352,643` | 3,875,288.44 USD | -460,055.36 USD | `-11.87%` | -12,626,891.19 USD | `+0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.00` | `899,429` | 9,912,023.83 USD | -807,668.75 USD | `-8.15%` | -12,682,774.04 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.00` | `899,429` | 9,912,023.83 USD | -807,668.75 USD | `-8.15%` | -12,682,774.04 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.98`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:10:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `420` | `0xecb6...2b00` | `SHORT` | 5,202,818.91 USD | `473,931,400.00` | `10.66` | `10.96` | `74.40` | -151,348.89 USD | `-2.91%` | `10X Cross` |
| `507` | `0x73ce...8ce9` | `LONG` | 4,391,127.34 USD | `400,011,600.00` | `12.05` | `10.96` | `7.82` | -428,626.36 USD | `-9.76%` | `5X Cross` |
| `851` | `0xb83d...6e36` | `SHORT` | 2,656,334.69 USD | `242,013,000.00` | `12.93` | `10.96` | `477.73` | 473,559.50 USD | `+17.83%` | `3X Cross` |
| `889` | `0x458d...ab3b` | `LONG` | 2,493,953.41 USD | `227,156,700.00` | `13.13` | `10.96` | `9.34` | -488,276.99 USD | `-19.58%` | `3X Isolated` |
| `978` | `0xdd53...2b13` | `SHORT` | 2,265,859.94 USD | `206,475,300.00` | `11.92` | `10.96` | `301.56` | 195,362.98 USD | `+8.62%` | `3X Cross` |
| `1007` | `0x3dc9...54b0` | `SHORT` | 2,195,600.00 USD | `200,000,000.00` | `7.56` | `10.96` | `96.52` | -684,441.58 USD | `-31.17%` | `10X Cross` |
| `1024` | `0x45d2...4029` | `SHORT` | 2,146,003.50 USD | `195,500,000.00` | `11.54` | `10.96` | `223.87` | 110,479.93 USD | `+5.15%` | `10X Cross` |
| `1196` | `0x6540...f7b7` | `LONG` | 1,837,093.69 USD | `167,404,200.00` | `12.40` | `10.96` | `6.70` | -238,712.42 USD | `-12.99%` | `5X Isolated` |
| `1269` | `0xeadc...9d55` | `LONG` | 1,731,296.08 USD | `157,691,600.00` | `9.43` | `10.96` | `0.000000` | 244,641.17 USD | `+14.13%` | `10X Cross` |
| `1489` | `0x5b5d...c060` | `SHORT` | 1,446,367.89 USD | `131,775,500.00` | `13.61` | `10.96` | `1116.22` | 346,890.08 USD | `+23.98%` | `3X Cross` |
| `1673` | `0xf6f3...47f8` | `SHORT` | 1,260,784.64 USD | `115,024,600.00` | `11.42` | `10.96` | `18.55` | 52,545.55 USD | `+4.17%` | `5X Cross` |
| `1861` | `0xfe7e...11b4` | `LONG` | 1,110,033.45 USD | `101,142,000.00` | `14.47` | `10.96` | `5.33` | -353,079.70 USD | `-31.81%` | `5X Isolated` |
| `1889` | `0x8af7...fa05` | `SHORT` | 1,083,299.98 USD | `98,661,200.00` | `14.08` | `10.96` | `203.10` | 305,882.56 USD | `+28.24%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.46` | 6,666.32 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.4640 USD [API] | `2026-10-29 09:31:24` |
| `ANNOUNCEMENT` | `INFO` | `11.48` | 5,889.12 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.89K USD at 11.4820 USD [API] | `2026-10-29 09:50:11` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 8,316.00 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 8.32K USD at 11.5500 USD [API] | `2026-10-29 10:34:53` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 169.54 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.17K USD at 11.5330 USD [API] | `2026-10-24 09:35:07` |
| `ANNOUNCEMENT` | `INFO` | `11.59` | 7,508.89 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.51K USD at 11.5860 USD [API] | `2026-10-29 11:05:03` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+2.25%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.12%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+2.24%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.13%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+2.24%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.13%`)
  * 7D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+2.20%`) | Long MP=`10.30` (Vol: 866,700.00 USD, Dist: `--6.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 46,320.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 222.31 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 29,610.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 3,480.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,300.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,430.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,420.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 250.25 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,810.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 15,960.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 24,410.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 411.94 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 1,050.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 57,150.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 2,400.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 235,200.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 83,570.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 5,440.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 6,620.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 543,120.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 1,780.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 9,670.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 52,720.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 276.57 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 6,010.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,260.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 13,590.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 69,580.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 15,990.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 3,270.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 20,540.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 79,550.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 710,860.00 USD | 9,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 10,740.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 7,160.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 55,430.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 5,120.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 173,010.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 38,790.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 15,080.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,610.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 66,130.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 90,360.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 32,110.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 520,270.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 15,960.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 14,810.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 23,240.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 57,860.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 473,800.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 87,420.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.15` | 12,910,000.00 USD | 12,910,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.17` | 12,840,000.00 USD | 12,840,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.19` | 12,790,000.00 USD | 12,790,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.21` | 12,730,000.00 USD | 12,730,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.23` | 12,720,000.00 USD | 12,720,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.25` | 12,690,000.00 USD | 12,690,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 19,930.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.27` | 12,650,000.00 USD | 12,650,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.29` | 12,630,000.00 USD | 12,630,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.31` | 12,590,000.00 USD | 12,590,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.33` | 12,530,000.00 USD | 12,530,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.35` | 12,530,000.00 USD | 12,530,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.37` | 12,480,000.00 USD | 12,480,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.39` | 12,470,000.00 USD | 12,470,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.41` | 12,420,000.00 USD | 12,420,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.43` | 12,410,000.00 USD | 12,410,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.45` | 12,360,000.00 USD | 12,360,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 55,970.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.47` | 12,210,000.00 USD | 12,210,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.49` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.51` | 12,210,000.00 USD | 12,210,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 12,140,000.00 USD | 12,140,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 102,020.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.57` | 12,100,000.00 USD | 12,100,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 12,010,000.00 USD | 12,010,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 11,810,000.00 USD | 11,810,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 11,800,000.00 USD | 11,800,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 204,090.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.69` | 11,780,000.00 USD | 11,780,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 11,710,000.00 USD | 11,710,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 63,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 11,630,000.00 USD | 11,630,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 11,590,000.00 USD | 11,590,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 11,480,000.00 USD | 11,480,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 11,430,000.00 USD | 11,430,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 30,620.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 8,500,000.00 USD | 8,500,000.00 USD | 29,590.00 USD | 11,010.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.87` | 11,360,000.00 USD | 11,360,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 8,450,000.00 USD | 8,450,000.00 USD | 6,450.00 USD | 12,250.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 11,350,000.00 USD | 11,350,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 8,420,000.00 USD | 8,420,000.00 USD | 37,810.00 USD | 28,440.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 8,350,000.00 USD | 8,350,000.00 USD | 23,430.00 USD | 19,950.00 USD | 444.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 8,310,000.00 USD | 8,310,000.00 USD | 1,820.00 USD | 3,260.00 USD | 499.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 11,220,000.00 USD | 11,220,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 421,600.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 8,300,000.00 USD | 8,300,000.00 USD | 67,680.00 USD | 14,110.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 11,170,000.00 USD | 11,170,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 8,200,000.00 USD | 8,200,000.00 USD | 31,010.00 USD | 6,830.00 USD | 64,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 11,170,000.00 USD | 11,170,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,090,000.00 USD | 8,090,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,030,000.00 USD | 8,030,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.03` | 11,080,000.00 USD | 11,080,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 7,980,000.00 USD | 7,980,000.00 USD | 18,000.00 USD | 1,900.00 USD | 492.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 781,760.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 7,960,000.00 USD | 7,960,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 7,880,000.00 USD | 7,880,000.00 USD | 167,250.00 USD | 701.42 USD | 75,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 10,870,000.00 USD | 10,870,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 7,640,000.00 USD | 7,640,000.00 USD | 7,570.00 USD | 42,810.00 USD | 122.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 10,650,000.00 USD | 10,650,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 7,590,000.00 USD | 7,590,000.00 USD | 1,150.00 USD | 20,910.00 USD | 395.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 10,590,000.00 USD | 10,590,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 7,560,000.00 USD | 7,560,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 10,470,000.00 USD | 10,470,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 79,580.00 USD | 287,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 7,500,000.00 USD | 7,500,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 10,220,000.00 USD | 10,220,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 7,380,000.00 USD | 7,380,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 10,120,000.00 USD | 10,120,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,110,000.00 USD | 7,110,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 9,870,000.00 USD | 9,870,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 6,630,000.00 USD | 6,630,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 9,520,000.00 USD | 9,520,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 6,230,000.00 USD | 6,230,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 8,790,000.00 USD | 8,790,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 32,460.00 USD | 208,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,040,000.00 USD | 6,040,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 8,520,000.00 USD | 8,520,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 5,870,000.00 USD | 5,870,000.00 USD | 164,060.00 USD | 11,970.00 USD | 168,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 8,110,000.00 USD | 8,110,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 5,520,000.00 USD | 5,520,000.00 USD | 166,230.00 USD | 20,900.00 USD | 39,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 7,410,000.00 USD | 7,410,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 5,290,000.00 USD | 5,290,000.00 USD | 11,920.00 USD | 1,310.00 USD | 71,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 7,360,000.00 USD | 7,360,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 5,210,000.00 USD | 5,210,000.00 USD | 68,350.00 USD | 9,100.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 7,210,000.00 USD | 7,210,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,720.00 USD | 175,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,050,000.00 USD | 5,050,000.00 USD | 5,630.00 USD | 3,580.00 USD | 69.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 6,800,000.00 USD | 6,800,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,040,000.00 USD | 5,040,000.00 USD | 41,250.00 USD | 45,790.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 6,790,000.00 USD | 6,790,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 4,940,000.00 USD | 4,940,000.00 USD | 88,080.00 USD | 32,290.00 USD | 67,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 6,790,000.00 USD | 6,790,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 4,750,000.00 USD | 4,750,000.00 USD | 247,240.00 USD | 0.00 USD | 57.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 6,340,000.00 USD | 6,340,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 4,510,000.00 USD | 4,510,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 6,090,000.00 USD | 6,090,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 26,900.00 USD | 34,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 3,970,000.00 USD | 3,970,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 5,220,000.00 USD | 5,220,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 3,650,000.00 USD | 3,650,000.00 USD | 50,630.00 USD | 2,200.00 USD | 55,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 4,820,000.00 USD | 4,820,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 3,540,000.00 USD | 3,540,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 4,680,000.00 USD | 4,680,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 3,460,000.00 USD | 3,460,000.00 USD | 446.87 USD | 12,710.00 USD | 38,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 4,630,000.00 USD | 4,630,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 3,410,000.00 USD | 3,410,000.00 USD | 15,130.00 USD | 66,080.00 USD | 144,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 4,590,000.00 USD | 4,590,000.00 USD | 121,680.00 USD | 114,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 8,100.00 USD | 8,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,190,000.00 USD | 3,190,000.00 USD | 96,350.00 USD | 26,820.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 4,350,000.00 USD | 4,350,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,040,000.00 USD | 3,040,000.00 USD | 54,810.00 USD | 29,840.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 2,930,000.00 USD | 2,930,000.00 USD | 9,410.00 USD | 18,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 4,330,000.00 USD | 4,330,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 2,910,000.00 USD | 2,910,000.00 USD | 21,530.00 USD | 4,920.00 USD | 126,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 4,320,000.00 USD | 4,320,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 2,750,000.00 USD | 2,750,000.00 USD | 85,770.00 USD | 3,750.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 4,260,000.00 USD | 4,260,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 2,620,000.00 USD | 2,620,000.00 USD | 53,760.00 USD | 7,540.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,530,000.00 USD | 2,530,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,390,000.00 USD | 2,390,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 4,220,000.00 USD | 4,220,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,360,000.00 USD | 2,360,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,150,000.00 USD | 2,150,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 3,700,000.00 USD | 3,700,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,040,000.00 USD | 2,040,000.00 USD | 35,390.00 USD | 65,300.00 USD | 51,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 3,570,000.00 USD | 3,570,000.00 USD | 537,300.00 USD | 111,300.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 1,890,000.00 USD | 1,890,000.00 USD | 190,170.00 USD | 140,640.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 2,820,000.00 USD | 2,820,000.00 USD | 79,540.00 USD | 64,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,510,000.00 USD | 1,510,000.00 USD | 66,060.00 USD | 23,280.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,410,000.00 USD | 1,410,000.00 USD | 106,890.00 USD | 31,060.00 USD | 12.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,270,000.00 USD | 1,270,000.00 USD | 351,160.00 USD | 5,480.00 USD | 16,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 2,120,000.00 USD | 2,120,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.86` | 901,310.00 USD | 901,310.00 USD | 155,010.00 USD | 23,860.00 USD | 189,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 1,820,000.00 USD | 1,820,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 533,390.00 USD | 533,390.00 USD | 49,200.00 USD | 9,550.00 USD | 59,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 959,600.00 USD | 959,600.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 414,970.00 USD | 414,970.00 USD | 114,210.00 USD | 35,090.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 545,160.00 USD | 545,160.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 216,630.00 USD | 216,630.00 USD | 103,270.00 USD | 19,240.00 USD | 74.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 286,690.00 USD | 286,690.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 94,050.00 USD | 94,050.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 70,060.00 USD | 70,060.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.96` | 88,120.00 USD | 88,120.00 USD | 0.00 USD | 0.00 USD | 88,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 12,320.00 USD | 12,320.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.98` | 175.98 USD | 175.98 USD | 0.00 USD | 0.00 USD | 175.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.98` | 351.96 USD | 351.96 USD | 0.00 USD | 0.00 USD | 175.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 224,900.00 USD | 224,900.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 449,800.00 USD | 449,800.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.00` | 818.96 USD | 818.96 USD | 0.00 USD | 467.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 461,480.00 USD | 461,480.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.02` | 151,730.00 USD | 151,730.00 USD | 0.00 USD | 0.00 USD | 150,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 729,460.00 USD | 729,460.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.04` | 307,900.00 USD | 307,900.00 USD | 0.00 USD | 2,200.00 USD | 153,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 1,010,000.00 USD | 1,010,000.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.06` | 334,880.00 USD | 334,880.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.08` | 637,270.00 USD | 637,270.00 USD | 0.00 USD | 0.00 USD | 302,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 645,250.00 USD | 645,250.00 USD | 7,750.00 USD | 0.00 USD | 232.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,770,000.00 USD | 1,770,000.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 790,460.00 USD | 790,460.00 USD | 6,320.00 USD | 2,260.00 USD | 136,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 2,260,000.00 USD | 2,260,000.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 863,440.00 USD | 863,440.00 USD | 4,910.00 USD | 0.00 USD | 68,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,550,000.00 USD | 2,550,000.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 1,040,000.00 USD | 1,040,000.00 USD | 127,020.00 USD | 2,100.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,640,000.00 USD | 2,640,000.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 1,220,000.00 USD | 1,220,000.00 USD | 71,610.00 USD | 14,380.00 USD | 86,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 1,440,000.00 USD | 1,440,000.00 USD | 76,580.00 USD | 72,530.00 USD | 74,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 3,380,000.00 USD | 3,380,000.00 USD | 554,520.00 USD | 106,700.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,930,000.00 USD | 1,930,000.00 USD | 320,360.00 USD | 53,200.00 USD | 112,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 3,800,000.00 USD | 3,800,000.00 USD | 288,220.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 2,290,000.00 USD | 2,290,000.00 USD | 163,340.00 USD | 54,170.00 USD | 151,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 4,270,000.00 USD | 4,270,000.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 2,550,000.00 USD | 2,550,000.00 USD | 149,280.00 USD | 41,730.00 USD | 67,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,930,000.00 USD | 4,930,000.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 3,210,000.00 USD | 3,210,000.00 USD | 336,790.00 USD | 59,260.00 USD | 259,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 5,250,000.00 USD | 5,250,000.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,630,000.00 USD | 3,630,000.00 USD | 213,610.00 USD | 75,000.00 USD | 129,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 5,560,000.00 USD | 5,560,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 4,010,000.00 USD | 4,010,000.00 USD | 168,840.00 USD | 74,250.00 USD | 142,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 5,950,000.00 USD | 5,950,000.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,630,000.00 USD | 4,630,000.00 USD | 390,100.00 USD | 118,470.00 USD | 107,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 6,240,000.00 USD | 6,240,000.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,920,000.00 USD | 4,920,000.00 USD | 138,710.00 USD | 95,240.00 USD | 56,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 6,580,000.00 USD | 6,580,000.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 5,150,000.00 USD | 5,150,000.00 USD | 118,230.00 USD | 85,980.00 USD | 25,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 5,330,000.00 USD | 5,330,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,640,000.00 USD | 5,640,000.00 USD | 126,960.00 USD | 77,100.00 USD | 104,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 7,170,000.00 USD | 7,170,000.00 USD | 265,450.00 USD | 105,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,860,000.00 USD | 5,860,000.00 USD | 84,630.00 USD | 43,290.00 USD | 94,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 7,500,000.00 USD | 7,500,000.00 USD | 227,420.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 6,070,000.00 USD | 6,070,000.00 USD | 86,190.00 USD | 75,110.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 7,590,000.00 USD | 7,590,000.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 6,120,000.00 USD | 6,120,000.00 USD | 24,020.00 USD | 29,490.00 USD | 452.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 7,730,000.00 USD | 7,730,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,260,000.00 USD | 6,260,000.00 USD | 52,620.00 USD | 34,750.00 USD | 53,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 7,850,000.00 USD | 7,850,000.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,420,000.00 USD | 6,420,000.00 USD | 103,860.00 USD | 16,980.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 7,970,000.00 USD | 7,970,000.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,630,000.00 USD | 6,630,000.00 USD | 86,680.00 USD | 20,290.00 USD | 100,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 8,160,000.00 USD | 8,160,000.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,830,000.00 USD | 6,830,000.00 USD | 128,820.00 USD | 20,640.00 USD | 47,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,910,000.00 USD | 6,910,000.00 USD | 58,440.00 USD | 2,950.00 USD | 17,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 7,050,000.00 USD | 7,050,000.00 USD | 59,560.00 USD | 14,330.00 USD | 67,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 8,270,000.00 USD | 8,270,000.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 7,140,000.00 USD | 7,140,000.00 USD | 44,510.00 USD | 512.95 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 8,380,000.00 USD | 8,380,000.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 7,190,000.00 USD | 7,190,000.00 USD | 5,220.00 USD | 7,410.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,220,000.00 USD | 7,220,000.00 USD | 228.94 USD | 12,290.00 USD | 25,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,420,000.00 USD | 7,420,000.00 USD | 126,110.00 USD | 35,770.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 8,610,000.00 USD | 8,610,000.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,440,000.00 USD | 7,440,000.00 USD | 239.66 USD | 4,760.00 USD | 15,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 8,810,000.00 USD | 8,810,000.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,680,000.00 USD | 7,680,000.00 USD | 121,720.00 USD | 18,090.00 USD | 98,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 8,990,000.00 USD | 8,990,000.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,860,000.00 USD | 7,860,000.00 USD | 76,690.00 USD | 30,300.00 USD | 73,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 9,050,000.00 USD | 9,050,000.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,920,000.00 USD | 7,920,000.00 USD | 26,090.00 USD | 14,880.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 9,200,000.00 USD | 9,200,000.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 8,010,000.00 USD | 8,010,000.00 USD | 27,690.00 USD | 20,510.00 USD | 40,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 9,270,000.00 USD | 9,270,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 8,030,000.00 USD | 8,030,000.00 USD | 1,190.00 USD | 18,000.00 USD | 150.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 9,440,000.00 USD | 9,440,000.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 8,080,000.00 USD | 8,080,000.00 USD | 11,880.00 USD | 53.10 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 9,560,000.00 USD | 9,560,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 8,180,000.00 USD | 8,180,000.00 USD | 43,880.00 USD | 11,870.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 9,810,000.00 USD | 9,810,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 1,420.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,260,000.00 USD | 8,260,000.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 9,840,000.00 USD | 9,840,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,370,000.00 USD | 8,370,000.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 9,930,000.00 USD | 9,930,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,450,000.00 USD | 8,450,000.00 USD | 43,700.00 USD | 8,690.00 USD | 28,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 10,090,000.00 USD | 10,090,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,720,000.00 USD | 8,720,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 10,160,000.00 USD | 10,160,000.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,830,000.00 USD | 8,830,000.00 USD | 48,030.00 USD | 15,270.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 10,400,000.00 USD | 10,400,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 5,650.00 USD | 7,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,980,000.00 USD | 8,980,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 11,040,000.00 USD | 11,040,000.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 9,150,000.00 USD | 9,150,000.00 USD | 64,190.00 USD | 29,060.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 11,510,000.00 USD | 11,510,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,340,000.00 USD | 9,340,000.00 USD | 119,890.00 USD | 23,880.00 USD | 44,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 11,970,000.00 USD | 11,970,000.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,390,000.00 USD | 9,390,000.00 USD | 13,680.00 USD | 11,370.00 USD | 31,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 12,680,000.00 USD | 12,680,000.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,580,000.00 USD | 9,580,000.00 USD | 90,660.00 USD | 39,490.00 USD | 56,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 13,330,000.00 USD | 13,330,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,770,000.00 USD | 9,770,000.00 USD | 76,750.00 USD | 43,270.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 13,900,000.00 USD | 13,900,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,900,000.00 USD | 9,900,000.00 USD | 43,090.00 USD | 38,850.00 USD | 50,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 14,260,000.00 USD | 14,260,000.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 10,000,000.00 USD | 10,000,000.00 USD | 49,200.00 USD | 21,380.00 USD | 29,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 14,540,000.00 USD | 14,540,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 10,220,000.00 USD | 10,220,000.00 USD | 116,760.00 USD | 54,460.00 USD | 50,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 14,810,000.00 USD | 14,810,000.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,390,000.00 USD | 10,390,000.00 USD | 75,780.00 USD | 35,660.00 USD | 55,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 15,330,000.00 USD | 15,330,000.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,620,000.00 USD | 10,620,000.00 USD | 124,550.00 USD | 34,710.00 USD | 67,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 15,480,000.00 USD | 15,480,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,830,000.00 USD | 10,830,000.00 USD | 112,670.00 USD | 46,930.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 15,800,000.00 USD | 15,800,000.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,980,000.00 USD | 10,980,000.00 USD | 71,000.00 USD | 43,870.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 16,170,000.00 USD | 16,170,000.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 11,040,000.00 USD | 11,040,000.00 USD | 10,400.00 USD | 18,360.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 16,340,000.00 USD | 16,340,000.00 USD | 140,270.00 USD | 27,350.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 11,060,000.00 USD | 11,060,000.00 USD | 4,800.00 USD | 15,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 16,540,000.00 USD | 16,540,000.00 USD | 101,460.00 USD | 47,320.00 USD | 46,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.27` | 16,710,000.00 USD | 16,710,000.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 17,020,000.00 USD | 17,020,000.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 17,160,000.00 USD | 17,160,000.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 17,200,000.00 USD | 17,200,000.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 17,250,000.00 USD | 17,250,000.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 1,940.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.37` | 17,320,000.00 USD | 17,320,000.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 17,480,000.00 USD | 17,480,000.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 17,500,000.00 USD | 17,500,000.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 12,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,070.00 USD | 13,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 779.24 USD | 14,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.85` | 535.85 USD | 15,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.25` | 1,060.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 21,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 866.89 USD | 115,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 115,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 3,860.00 USD | 119,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 4,280.00 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 149,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 149,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 150,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 150,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 150,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 323.00 USD | 150,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 152,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 230.30 USD | 152,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 31,700.00 USD | 184,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 286,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 365,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 367,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,700.00 USD | 393,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 101.79 USD | 393,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,450.00 USD | 399,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 649,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 649,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 651,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,920.00 USD | 679,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 2,130,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 63,600.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 707,060.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 75,870.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 619.67 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 39,570.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 202.08 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 222.87 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,270,000.00 USD | 0.00 USD | 46,320.00 USD | `-79.51%` | `20,585,500.00` |
| `Live` | `Long` | `2.35` | 12,220,000.00 USD | 0.00 USD | 222.31 USD | `-78.60%` | `94,600.00` |
| `Live` | `Long` | `2.55` | 12,220,000.00 USD | 0.00 USD | 29,610.00 USD | `-76.78%` | `11,610,100.00` |
| `Live` | `Long` | `2.65` | 12,190,000.00 USD | 0.00 USD | 3,480.00 USD | `-75.87%` | `1,314,000.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 7,300.00 USD | `-72.23%` | `2,394,200.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 1,430.00 USD | `-71.32%` | `454,900.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 2,420.00 USD | `-69.50%` | `723,600.00` |
| `Live` | `Long` | `3.45` | 12,180,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.59%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 126.73 USD | `-67.68%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.77%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,170,000.00 USD | 0.00 USD | 250.25 USD | `-64.95%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,170,000.00 USD | 0.00 USD | 4,810.00 USD | `-64.04%` | `1,217,900.00` |
| `Live` | `Long` | `4.05` | 12,160,000.00 USD | 0.00 USD | 15,960.00 USD | `-63.12%` | `3,941,700.00` |
| `Live` | `Long` | `4.25` | 12,150,000.00 USD | 0.00 USD | 24,410.00 USD | `-61.30%` | `5,744,100.00` |
| `Live` | `Long` | `4.35` | 12,120,000.00 USD | 0.00 USD | 411.94 USD | `-60.39%` | `94,700.00` |
| `Live` | `Long` | `4.45` | 12,120,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.48%` | `235,700.00` |
| `Live` | `Long` | `4.55` | 12,120,000.00 USD | 0.00 USD | 57,150.00 USD | `-58.57%` | `12,560,000.00` |
| `Live` | `Long` | `4.65` | 12,060,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.66%` | `515,900.00` |
| `Live` | `Long` | `4.75` | 12,060,000.00 USD | 0.00 USD | 235,200.00 USD | `-56.75%` | `49,515,000.00` |
| `Live` | `Long` | `4.85` | 11,820,000.00 USD | 0.00 USD | 83,570.00 USD | `-55.84%` | `17,230,400.00` |
| `Live` | `Long` | `4.95` | 11,740,000.00 USD | 0.00 USD | 5,440.00 USD | `-54.93%` | `1,098,200.00` |
| `Live` | `Long` | `5.05` | 11,740,000.00 USD | 0.00 USD | 217.66 USD | `-54.02%` | `43,100.00` |
| `Live` | `Long` | `5.25` | 11,740,000.00 USD | 0.00 USD | 6,620.00 USD | `-52.20%` | `1,261,800.00` |
| `Live` | `Long` | `5.35` | 11,730,000.00 USD | 0.00 USD | 543,120.00 USD | `-51.29%` | `101,517,700.00` |
| `Live` | `Long` | `5.45` | 11,190,000.00 USD | 0.00 USD | 1,780.00 USD | `-50.38%` | `327,300.00` |
| `Live` | `Long` | `5.55` | 11,180,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.47%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 52,720.00 USD | `-48.56%` | `9,330,200.00` |
| `Live` | `Long` | `5.75` | 11,120,000.00 USD | 0.00 USD | 276.57 USD | `-47.65%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 11,120,000.00 USD | 0.00 USD | 6,010.00 USD | `-46.74%` | `1,026,700.00` |
| `Live` | `Long` | `5.95` | 11,120,000.00 USD | 0.00 USD | 10,260.00 USD | `-45.83%` | `1,724,100.00` |
| `Live` | `Long` | `6.05` | 11,110,000.00 USD | 0.00 USD | 13,590.00 USD | `-44.91%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 11,090,000.00 USD | 0.00 USD | 489.54 USD | `-44.00%` | `79,600.00` |
| `Live` | `Long` | `6.25` | 11,090,000.00 USD | 0.00 USD | 69,580.00 USD | `-43.09%` | `11,133,300.00` |
| `Live` | `Long` | `6.35` | 11,020,000.00 USD | 0.00 USD | 15,990.00 USD | `-42.18%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 11,010,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.27%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 11,000,000.00 USD | 0.00 USD | 3,270.00 USD | `-40.36%` | `499,500.00` |
| `Live` | `Long` | `6.65` | 10,990,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.45%` | `169,517,500.00` |
| `Live` | `Long` | `6.75` | 9,870,000.00 USD | 0.00 USD | 20,540.00 USD | `-38.54%` | `3,042,300.00` |
| `Live` | `Long` | `6.85` | 9,850,000.00 USD | 0.00 USD | 5,060.00 USD | `-37.63%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,840,000.00 USD | 0.00 USD | 79,550.00 USD | `-36.72%` | `11,445,400.00` |
| `Live` | `Long` | `7.05` | 9,760,000.00 USD | 0.00 USD | 710,860.00 USD | `-35.81%` | `100,830,900.00` |
| `Live` | `Long` | `7.15` | 9,050,000.00 USD | 0.00 USD | 10,740.00 USD | `-34.90%` | `1,501,900.00` |
| `Live` | `Long` | `7.25` | 9,040,000.00 USD | 0.00 USD | 7,160.00 USD | `-33.99%` | `986,900.00` |
| `Live` | `Long` | `7.35` | 9,030,000.00 USD | 0.00 USD | 55,430.00 USD | `-33.08%` | `7,541,100.00` |
| `Live` | `Long` | `7.45` | 8,980,000.00 USD | 0.00 USD | 5,120.00 USD | `-32.17%` | `686,600.00` |
| `Live` | `Long` | `7.55` | 8,970,000.00 USD | 0.00 USD | 173,010.00 USD | `-31.26%` | `22,914,800.00` |
| `Live` | `Long` | `7.65` | 8,800,000.00 USD | 0.00 USD | 38,790.00 USD | `-30.35%` | `5,070,100.00` |
| `Live` | `Long` | `7.75` | 8,760,000.00 USD | 0.00 USD | 15,080.00 USD | `-29.44%` | `1,945,700.00` |
| `Live` | `Long` | `7.85` | 8,740,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.53%` | `401,116,200.00` |
| `Live` | `Long` | `7.95` | 5,600,000.00 USD | 0.00 USD | 15,610.00 USD | `-27.62%` | `1,963,900.00` |
| `Live` | `Long` | `8.05` | 5,580,000.00 USD | 0.00 USD | 66,130.00 USD | `-26.70%` | `8,214,600.00` |
| `Live` | `Long` | `8.15` | 5,510,000.00 USD | 0.00 USD | 90,360.00 USD | `-25.79%` | `11,087,300.00` |
| `Live` | `Long` | `8.25` | 5,420,000.00 USD | 0.00 USD | 32,110.00 USD | `-24.88%` | `3,892,000.00` |
| `Live` | `Long` | `8.35` | 5,390,000.00 USD | 0.00 USD | 6,370.00 USD | `-23.97%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,390,000.00 USD | 0.00 USD | 520,270.00 USD | `-23.06%` | `61,570,800.00` |
| `Live` | `Long` | `8.55` | 4,860,000.00 USD | 0.00 USD | 15,960.00 USD | `-22.15%` | `1,866,700.00` |
| `Live` | `Long` | `8.65` | 4,850,000.00 USD | 0.00 USD | 14,810.00 USD | `-21.24%` | `1,712,600.00` |
| `Live` | `Long` | `8.75` | 4,830,000.00 USD | 0.00 USD | 23,240.00 USD | `-20.33%` | `2,655,700.00` |
| `Live` | `Long` | `8.85` | 4,810,000.00 USD | 0.00 USD | 57,860.00 USD | `-19.42%` | `6,537,900.00` |
| `Live` | `Long` | `8.95` | 4,750,000.00 USD | 0.00 USD | 473,800.00 USD | `-18.51%` | `52,938,100.00` |
| `Live` | `Long` | `9.05` | 4,280,000.00 USD | 0.00 USD | 87,420.00 USD | `-17.60%` | `9,660,200.00` |
| `Live` | `Long` | `9.15` | 4,190,000.00 USD | 0.00 USD | 76,340.00 USD | `-16.69%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,120,000.00 USD | 0.00 USD | 19,930.00 USD | `-15.78%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,100,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-14.87%` | `229,774,900.00` |
| `Live` | `Long` | `9.45` | 1,950,000.00 USD | 0.00 USD | 55,970.00 USD | `-13.96%` | `5,922,500.00` |
| `Live` | `Long` | `9.55` | 1,890,000.00 USD | 0.00 USD | 102,020.00 USD | `-13.05%` | `10,682,700.00` |
| `Live` | `Long` | `9.65` | 1,790,000.00 USD | 0.00 USD | 204,090.00 USD | `-12.14%` | `21,148,900.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 63,190.00 USD | `-11.23%` | `6,481,300.00` |
| `Live` | `Long` | `9.85` | 1,520,000.00 USD | 0.00 USD | 30,620.00 USD | `-10.32%` | `3,108,900.00` |
| `Live` | `Long` | `9.95` | 1,490,000.00 USD | 0.00 USD | 421,600.00 USD | `-9.41%` | `42,372,100.00` |
| `Live` | `Long` | `10.05` | 1,070,000.00 USD | 0.00 USD | 781,760.00 USD | `-8.49%` | `77,786,700.00` |
| `Live` | `Long` | `10.15` | 287,760.00 USD | 0.00 USD | 79,580.00 USD | `-7.58%` | `7,840,300.00` |
| `Live` | `Long` | `10.25` | 208,180.00 USD | 0.00 USD | 32,460.00 USD | `-6.67%` | `3,166,900.00` |
| `Live` | `Long` | `10.35` | 175,720.00 USD | 0.00 USD | 140,720.00 USD | `-5.76%` | `13,596,500.00` |
| `Live` | `Long` | `10.45` | 34,990.00 USD | 0.00 USD | 26,900.00 USD | `-4.85%` | `2,574,100.00` |
| `Live` | `Long` | `10.55` | 8,100.00 USD | 0.00 USD | 8,100.00 USD | `-3.94%` | `767,300.00` |
| `Live` | `Short` | `11.45` | 249.61 USD | 249.61 USD | 0.00 USD | `+4.25%` | `21,800.00` |
| `Live` | `Short` | `11.85` | 1,670.00 USD | 1,420.00 USD | 0.00 USD | `+7.89%` | `119,600.00` |
| `Live` | `Short` | `11.95` | 7,310.00 USD | 5,650.00 USD | 0.00 USD | `+8.80%` | `472,500.00` |
| `Live` | `Short` | `12.25` | 8,740.00 USD | 1,430.00 USD | 0.00 USD | `+11.54%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 10,680.00 USD | 1,940.00 USD | 0.00 USD | `+12.45%` | `157,000.00` |
| `Live` | `Short` | `12.45` | 12,660.00 USD | 1,980.00 USD | 0.00 USD | `+13.36%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 13,730.00 USD | 1,070.00 USD | 0.00 USD | `+14.27%` | `85,200.00` |
| `Live` | `Short` | `12.65` | 14,510.00 USD | 779.24 USD | 0.00 USD | `+15.18%` | `61,600.00` |
| `Live` | `Short` | `12.85` | 15,040.00 USD | 535.85 USD | 0.00 USD | `+17.00%` | `41,700.00` |
| `Live` | `Short` | `13.25` | 16,100.00 USD | 1,060.00 USD | 0.00 USD | `+20.64%` | `79,900.00` |
| `Live` | `Short` | `13.45` | 21,530.00 USD | 5,430.00 USD | 0.00 USD | `+22.46%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 114,430.00 USD | 92,890.00 USD | 0.00 USD | `+23.37%` | `6,855,700.00` |
| `Live` | `Short` | `14.05` | 115,290.00 USD | 866.89 USD | 0.00 USD | `+27.92%` | `61,700.00` |
| `Live` | `Short` | `14.25` | 115,840.00 USD | 544.35 USD | 0.00 USD | `+29.75%` | `38,200.00` |
| `Live` | `Short` | `14.35` | 119,700.00 USD | 3,860.00 USD | 0.00 USD | `+30.66%` | `269,100.00` |
| `Live` | `Short` | `14.45` | 123,980.00 USD | 4,280.00 USD | 0.00 USD | `+31.57%` | `296,400.00` |
| `Live` | `Short` | `14.95` | 149,320.00 USD | 25,330.00 USD | 0.00 USD | `+36.12%` | `1,694,600.00` |
| `Live` | `Short` | `15.25` | 149,470.00 USD | 155.55 USD | 0.00 USD | `+38.85%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 150,050.00 USD | 578.46 USD | 0.00 USD | `+41.58%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 150,320.00 USD | 271.04 USD | 0.00 USD | `+44.31%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 150,460.00 USD | 138.76 USD | 0.00 USD | `+45.22%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 150,780.00 USD | 323.00 USD | 0.00 USD | `+47.05%` | `20,000.00` |
| `Live` | `Short` | `16.35` | 152,180.00 USD | 1,390.00 USD | 0.00 USD | `+48.87%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 152,410.00 USD | 230.30 USD | 0.00 USD | `+49.78%` | `14,000.00` |
| `Live` | `Short` | `16.55` | 184,110.00 USD | 31,700.00 USD | 0.00 USD | `+50.69%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 286,020.00 USD | 101,910.00 USD | 0.00 USD | `+52.51%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 365,790.00 USD | 79,770.00 USD | 0.00 USD | `+54.33%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 367,160.00 USD | 1,370.00 USD | 0.00 USD | `+56.15%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 393,860.00 USD | 26,700.00 USD | 0.00 USD | `+57.97%` | `1,539,000.00` |
| `Live` | `Short` | `17.55` | 393,960.00 USD | 101.79 USD | 0.00 USD | `+59.79%` | `5,800.00` |
| `Live` | `Short` | `17.65` | 399,420.00 USD | 5,450.00 USD | 0.00 USD | `+60.70%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 649,000.00 USD | 249,580.00 USD | 0.00 USD | `+62.52%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 649,350.00 USD | 351.82 USD | 0.00 USD | `+63.43%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 651,320.00 USD | 1,970.00 USD | 0.00 USD | `+64.34%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 679,240.00 USD | 27,920.00 USD | 0.00 USD | `+66.17%` | `1,529,600.00` |
| `Live` | `Short` | `18.45` | 2,810,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+67.99%` | `115,235,400.00` |
| `Live` | `Short` | `18.55` | 2,810,000.00 USD | 185.50 USD | 0.00 USD | `+68.90%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,870,000.00 USD | 63,600.00 USD | 0.00 USD | `+69.81%` | `3,410,000.00` |
| `Live` | `Short` | `18.75` | 3,580,000.00 USD | 707,060.00 USD | 0.00 USD | `+70.72%` | `37,710,000.00` |
| `Live` | `Short` | `18.85` | 3,650,000.00 USD | 75,870.00 USD | 0.00 USD | `+71.63%` | `4,024,800.00` |
| `Live` | `Short` | `18.95` | 3,650,000.00 USD | 619.67 USD | 0.00 USD | `+72.54%` | `32,700.00` |
| `Live` | `Short` | `19.55` | 3,650,000.00 USD | 316.71 USD | 0.00 USD | `+78.00%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,690,000.00 USD | 39,570.00 USD | 0.00 USD | `+78.91%` | `2,013,700.00` |
| `Live` | `Short` | `19.75` | 3,690,000.00 USD | 359.45 USD | 0.00 USD | `+79.82%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,690,000.00 USD | 291.27 USD | 0.00 USD | `+81.64%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,690,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.47%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,700,000.00 USD | 1,770.00 USD | 0.00 USD | `+86.20%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,700,000.00 USD | 7,250.00 USD | 0.00 USD | `+87.11%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,700,000.00 USD | 114.68 USD | 0.00 USD | `+89.84%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,700,000.00 USD | 202.08 USD | 0.00 USD | `+91.66%` | `9,600.00` |
| `Live` | `Short` | `21.75` | 3,770,000.00 USD | 65,060.00 USD | 0.00 USD | `+98.03%` | `2,991,400.00` |
| `Live` | `Short` | `21.85` | 3,770,000.00 USD | 222.87 USD | 0.00 USD | `+98.94%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 397,720.00 USD | 0.00 USD | 182.03 USD | `-77.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 397,540.00 USD | 0.00 USD | 221.45 USD | `-74.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 397,320.00 USD | 0.00 USD | 234.23 USD | `-73.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 397,090.00 USD | 0.00 USD | 209.48 USD | `-71.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 396,880.00 USD | 0.00 USD | 236.33 USD | `-68.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 396,640.00 USD | 0.00 USD | 431.68 USD | `-67.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 396,210.00 USD | 0.00 USD | 290.29 USD | `-58.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 395,920.00 USD | 0.00 USD | 120.22 USD | `-52.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 395,800.00 USD | 0.00 USD | 3,790.00 USD | `-48.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 392,010.00 USD | 0.00 USD | 251.68 USD | `-44.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 391,750.00 USD | 0.00 USD | 749.94 USD | `-42.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 391,000.00 USD | 0.00 USD | 772.71 USD | `-41.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 390,230.00 USD | 0.00 USD | 3,760.00 USD | `-40.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 386,470.00 USD | 0.00 USD | 133.00 USD | `-39.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 386,330.00 USD | 0.00 USD | 1,320.00 USD | `-36.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 385,020.00 USD | 0.00 USD | 3,770.00 USD | `-35.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 381,250.00 USD | 0.00 USD | 2,070.00 USD | `-33.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 379,180.00 USD | 0.00 USD | 3,740.00 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 375,430.00 USD | 0.00 USD | 1,050.00 USD | `-31.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 374,380.00 USD | 0.00 USD | 120.90 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 374,260.00 USD | 0.00 USD | 146.80 USD | `-28.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 374,120.00 USD | 0.00 USD | 124.02 USD | `-27.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 373,990.00 USD | 0.00 USD | 5,000.00 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 368,990.00 USD | 0.00 USD | 393.64 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 368,600.00 USD | 0.00 USD | 10,560.00 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 358,030.00 USD | 0.00 USD | 57,330.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 300,700.00 USD | 0.00 USD | 1,480.00 USD | `-23.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 299,220.00 USD | 0.00 USD | 52,990.00 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 246,240.00 USD | 0.00 USD | 186.84 USD | `-21.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 246,050.00 USD | 0.00 USD | 742.88 USD | `-20.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 245,310.00 USD | 0.00 USD | 902.70 USD | `-19.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 244,400.00 USD | 0.00 USD | 1,570.00 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 242,830.00 USD | 0.00 USD | 3,440.00 USD | `-17.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 239,390.00 USD | 0.00 USD | 194.90 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 239,200.00 USD | 0.00 USD | 232.18 USD | `-15.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 238,960.00 USD | 0.00 USD | 9,010.00 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 229,960.00 USD | 0.00 USD | 518.80 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 229,440.00 USD | 0.00 USD | 19,590.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 209,840.00 USD | 0.00 USD | 504.70 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 209,340.00 USD | 0.00 USD | 3,060.00 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 206,280.00 USD | 0.00 USD | 24,100.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 182,180.00 USD | 0.00 USD | 3,450.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 178,730.00 USD | 0.00 USD | 47,890.00 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 130,840.00 USD | 0.00 USD | 5,650.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 125,190.00 USD | 0.00 USD | 30,030.00 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 95,160.00 USD | 0.00 USD | 4,870.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 90,280.00 USD | 0.00 USD | 11,220.00 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 79,060.00 USD | 0.00 USD | 23,980.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 55,080.00 USD | 0.00 USD | 6,120.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 48,960.00 USD | 0.00 USD | 29,030.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 19,930.00 USD | 0.00 USD | 9,140.00 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 10,790.00 USD | 0.00 USD | 10,790.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 7,550.00 USD | 7,550.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 11,460.00 USD | 3,910.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 24,530.00 USD | 13,060.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 41,190.00 USD | 16,660.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 45,390.00 USD | 4,190.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 71,260.00 USD | 25,870.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 74,410.00 USD | 3,160.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 76,050.00 USD | 1,630.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 83,170.00 USD | 7,130.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 87,460.00 USD | 4,280.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 115,170.00 USD | 27,710.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 117,100.00 USD | 1,930.00 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 210,390.00 USD | 93,280.00 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 210,980.00 USD | 597.74 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 215,640.00 USD | 4,650.00 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 218,130.00 USD | 2,500.00 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 224,310.00 USD | 6,180.00 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 224,990.00 USD | 679.57 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 245,360.00 USD | 20,360.00 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 245,810.00 USD | 451.95 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 264,010.00 USD | 18,200.00 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 264,930.00 USD | 919.19 USD | 0.00 USD | `+19.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 266,250.00 USD | 1,320.00 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 274,030.00 USD | 7,790.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 276,570.00 USD | 2,540.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 278,040.00 USD | 1,470.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 278,990.00 USD | 954.14 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 298,540.00 USD | 19,550.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 304,180.00 USD | 5,640.00 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 304,450.00 USD | 266.44 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 320,710.00 USD | 16,260.00 USD | 0.00 USD | `+27.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 320,860.00 USD | 152.82 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 325,140.00 USD | 4,280.00 USD | 0.00 USD | `+29.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 328,550.00 USD | 3,410.00 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 342,220.00 USD | 13,670.00 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 342,430.00 USD | 218.25 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 344,290.00 USD | 1,850.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 351,550.00 USD | 7,270.00 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 352,500.00 USD | 950.82 USD | 0.00 USD | `+36.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 378,200.00 USD | 25,700.00 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 380,650.00 USD | 2,450.00 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 617,960.00 USD | 237,310.00 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 618,880.00 USD | 924.07 USD | 0.00 USD | `+39.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 619,780.00 USD | 893.01 USD | 0.00 USD | `+40.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 644,520.00 USD | 24,740.00 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 644,760.00 USD | 237.88 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 648,050.00 USD | 3,290.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 651,220.00 USD | 3,170.00 USD | 0.00 USD | `+44.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 656,350.00 USD | 5,130.00 USD | 0.00 USD | `+45.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 671,790.00 USD | 15,440.00 USD | 0.00 USD | `+46.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 678,600.00 USD | 6,800.00 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 685,100.00 USD | 6,500.00 USD | 0.00 USD | `+47.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 691,640.00 USD | 6,540.00 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 698,220.00 USD | 6,580.00 USD | 0.00 USD | `+49.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 708,150.00 USD | 9,930.00 USD | 0.00 USD | `+50.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 812,120.00 USD | 103,980.00 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 826,360.00 USD | 14,240.00 USD | 0.00 USD | `+52.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 910,720.00 USD | 84,360.00 USD | 0.00 USD | `+53.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 912,410.00 USD | 1,700.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 919,780.00 USD | 7,370.00 USD | 0.00 USD | `+55.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 921,490.00 USD | 1,710.00 USD | 0.00 USD | `+56.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 923,800.00 USD | 2,300.00 USD | 0.00 USD | `+57.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 925,530.00 USD | 1,740.00 USD | 0.00 USD | `+57.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 948,090.00 USD | 22,560.00 USD | 0.00 USD | `+58.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 952,480.00 USD | 4,390.00 USD | 0.00 USD | `+59.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 956,890.00 USD | 4,410.00 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 961,330.00 USD | 4,440.00 USD | 0.00 USD | `+61.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 965,790.00 USD | 4,460.00 USD | 0.00 USD | `+62.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 966,240.00 USD | 448.75 USD | 0.00 USD | `+63.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 997,210.00 USD | 30,960.00 USD | 0.00 USD | `+64.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 997,660.00 USD | 453.75 USD | 0.00 USD | `+65.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 998,120.00 USD | 456.25 USD | 0.00 USD | `+66.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 998,580.00 USD | 458.75 USD | 0.00 USD | `+67.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 999,040.00 USD | 461.25 USD | 0.00 USD | `+67.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,000,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,000,000.00 USD | 466.25 USD | 0.00 USD | `+69.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,000,000.00 USD | 468.75 USD | 0.00 USD | `+70.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,000,000.00 USD | 471.25 USD | 0.00 USD | `+71.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,010,000.00 USD | 473.75 USD | 0.00 USD | `+72.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,070,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,070,000.00 USD | 574.50 USD | 0.00 USD | `+74.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,070,000.00 USD | 577.50 USD | 0.00 USD | `+75.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,080,000.00 USD | 2,710.00 USD | 0.00 USD | `+76.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,080,000.00 USD | 972.50 USD | 0.00 USD | `+77.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,080,000.00 USD | 7,680.00 USD | 0.00 USD | `+78.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,090,000.00 USD | 786.00 USD | 0.00 USD | `+78.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,090,000.00 USD | 790.00 USD | 0.00 USD | `+79.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,090,000.00 USD | 992.50 USD | 0.00 USD | `+80.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,090,000.00 USD | 997.50 USD | 0.00 USD | `+81.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,690,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+82.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,700,000.00 USD | 1,020.00 USD | 0.00 USD | `+86.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,700,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,700,000.00 USD | 1,030.00 USD | 0.00 USD | `+88.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,700,000.00 USD | 1,040.00 USD | 0.00 USD | `+88.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,700,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,700,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,710,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,710,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,710,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,750,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,760,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,760,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,760,000.00 USD | 1,080.00 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,760,000.00 USD | 1,090.00 USD | 0.00 USD | `+98.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,760,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.15` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 28,870.00 USD | 20,730.00 USD | 18,210.00 USD |
| `7D` | `9.17` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 16,460.00 USD | 9,000.00 USD | 25,470.00 USD |
| `7D` | `9.19` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 32,450.00 USD | 21,470.00 USD | 4,040.00 USD |
| `7D` | `9.21` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 9,420.00 USD | 218.83 USD | 12.05 USD |
| `7D` | `9.23` | 12,720,000.00 USD | 0.00 USD | 12,720,000.00 USD | 568.40 USD | 6,490.00 USD | 24,420.00 USD |
| `7D` | `9.25` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 13,760.00 USD | 8,650.00 USD | 15,730.00 USD |
| `7D` | `9.27` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 11,080.00 USD | 8,280.00 USD | 6,070.00 USD |
| `7D` | `9.29` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 13,210.00 USD | 1,630.00 USD | 21,080.00 USD |
| `7D` | `9.31` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 28,020.00 USD | 21,860.00 USD | 8,940.00 USD |
| `7D` | `9.33` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 7,290.00 USD | 91.61 USD | 0.00 USD |
| `7D` | `9.35` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 27,860.00 USD | 9,940.00 USD | 11,140.00 USD |
| `7D` | `9.37` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 374.00 USD | 36.40 USD | 6,380.00 USD |
| `7D` | `9.39` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 25,080.00 USD | 13,650.00 USD | 7,010.00 USD |
| `7D` | `9.41` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 13,950.00 USD | 480.65 USD | 310.62 USD |
| `7D` | `9.43` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,120.00 USD | 5,950.00 USD | 33,670.00 USD |
| `7D` | `9.45` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 100,060.00 USD | 0.00 USD | 48,300.00 USD |
| `7D` | `9.47` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 360.58 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.49` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 0.00 USD | 1,680.00 USD | 253.40 USD |
| `7D` | `9.51` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 58,490.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `9.53` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD |
| `7D` | `9.55` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 297.65 USD | 11,000.00 USD | 32,030.00 USD |
| `7D` | `9.57` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 38,760.00 USD | 16,080.00 USD | 39,150.00 USD |
| `7D` | `9.59` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 62,800.00 USD | 1,250.00 USD | 100,540.00 USD |
| `7D` | `9.61` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 0.00 USD | 504.13 USD | 35,790.00 USD |
| `7D` | `9.63` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 8,880.00 USD | 0.00 USD | 470.11 USD |
| `7D` | `9.65` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,370.00 USD | 2,560.00 USD | 5,640.00 USD |
| `7D` | `9.69` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 7,710.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.73` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.75` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 52,150.00 USD | 0.00 USD | 27,160.00 USD |
| `7D` | `9.77` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 413.42 USD |
| `7D` | `9.79` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 44,630.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.81` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 55,730.00 USD | 22,970.00 USD | 26,150.00 USD |
| `7D` | `9.83` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 50,280.00 USD | 2,000.00 USD | 379.91 USD |
| `7D` | `9.85` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 38,130.00 USD | 14,570.00 USD | 12,970.00 USD |
| `1D` | `9.86` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 29,590.00 USD | 11,010.00 USD | 10,860.00 USD |
| `7D` | `9.87` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 10,280.00 USD | 0.00 USD | 429.54 USD |
| `1D` | `9.88` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 6,450.00 USD | 12,250.00 USD | 7,720.00 USD |
| `7D` | `9.89` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 48,670.00 USD | 15,600.00 USD | 107.02 USD |
| `1D` | `9.90` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 37,810.00 USD | 28,440.00 USD | 7,510.00 USD |
| `7D` | `9.91` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.92` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 23,430.00 USD | 19,950.00 USD | 444.67 USD |
| `7D` | `9.93` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 0.00 USD | 41,640.00 USD | 12,710.00 USD |
| `1D` | `9.94` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 1,820.00 USD | 3,260.00 USD | 499.43 USD |
| `7D` | `9.95` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 14,920.00 USD | 22,060.00 USD | 14,330.00 USD |
| `1D` | `9.96` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 67,680.00 USD | 14,110.00 USD | 22,820.00 USD |
| `7D` | `9.97` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 789.70 USD | 598.17 USD | 1,090.00 USD |
| `1D` | `9.98` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 31,010.00 USD | 6,830.00 USD | 64,750.00 USD |
| `7D` | `9.99` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 4,830.00 USD | 0.00 USD | 72,880.00 USD |
| `1D` | `10.00` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,510.00 USD |
| `7D` | `10.01` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 0.00 USD | 7,950.00 USD | 506.80 USD |
| `1D` | `10.02` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,770.00 USD |
| `7D` | `10.03` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.04` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 18,000.00 USD | 1,900.00 USD | 492.55 USD |
| `7D` | `10.05` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 0.00 USD | 1,210.00 USD | 83,740.00 USD |
| `1D` | `10.06` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,300.00 USD |
| `7D` | `10.07` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 0.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.08` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 167,250.00 USD | 701.42 USD | 75,660.00 USD |
| `7D` | `10.09` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 220,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.10` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 7,570.00 USD | 42,810.00 USD | 122.26 USD |
| `7D` | `10.11` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 4,940.00 USD | 0.00 USD | 56,110.00 USD |
| `1D` | `10.12` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 1,150.00 USD | 20,910.00 USD | 395.62 USD |
| `7D` | `10.13` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 27,980.00 USD | 71,860.00 USD | 18,110.00 USD |
| `1D` | `10.14` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,690.00 USD |
| `7D` | `10.15` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 171,760.00 USD | 8,310.00 USD | 66,940.00 USD |
| `1D` | `10.16` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,510.00 USD |
| `7D` | `10.17` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 72,100.00 USD | 8,390.00 USD | 22,180.00 USD |
| `1D` | `10.18` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,010.00 USD |
| `7D` | `10.19` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 10,880.00 USD | 37,330.00 USD | 207,300.00 USD |
| `1D` | `10.20` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,260.00 USD |
| `7D` | `10.21` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 139,440.00 USD | 57,960.00 USD | 149,220.00 USD |
| `1D` | `10.22` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,760.00 USD |
| `7D` | `10.23` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 307,290.00 USD | 52,960.00 USD | 369,720.00 USD |
| `1D` | `10.24` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,260.00 USD |
| `7D` | `10.25` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 108,200.00 USD | 18,890.00 USD | 138,800.00 USD |
| `1D` | `10.26` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,920.00 USD |
| `7D` | `10.27` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 77,310.00 USD | 32,240.00 USD | 307,680.00 USD |
| `1D` | `10.28` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 164,060.00 USD | 11,970.00 USD | 168,230.00 USD |
| `7D` | `10.29` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 480,110.00 USD | 0.00 USD | 220,960.00 USD |
| `1D` | `10.30` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 166,230.00 USD | 20,900.00 USD | 39,770.00 USD |
| `7D` | `10.31` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 11,920.00 USD | 1,310.00 USD | 71,260.00 USD |
| `7D` | `10.33` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 56,120.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 68,350.00 USD | 9,100.00 USD | 86,210.00 USD |
| `7D` | `10.35` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 306,500.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.36` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,630.00 USD | 3,580.00 USD | 69.62 USD |
| `7D` | `10.37` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.38` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 41,250.00 USD | 45,790.00 USD | 7,690.00 USD |
| `7D` | `10.39` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 88,080.00 USD | 32,290.00 USD | 67,090.00 USD |
| `7D` | `10.41` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 181,080.00 USD | 107,700.00 USD | 160,350.00 USD |
| `1D` | `10.42` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 247,240.00 USD | 0.00 USD | 57.36 USD |
| `7D` | `10.43` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 225,570.00 USD | 22,080.00 USD | 0.00 USD |
| `1D` | `10.44` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,450.00 USD |
| `7D` | `10.45` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 463,680.00 USD | 77,400.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,260.00 USD |
| `7D` | `10.47` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 350,820.00 USD | 45,390.00 USD | 0.00 USD |
| `1D` | `10.48` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 50,630.00 USD | 2,200.00 USD | 55,120.00 USD |
| `7D` | `10.49` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 2,260.00 USD | 0.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,180.00 USD |
| `7D` | `10.51` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 1,560.00 USD | 54,560.00 USD | 0.00 USD |
| `1D` | `10.52` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 446.87 USD | 12,710.00 USD | 38,520.00 USD |
| `7D` | `10.53` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 2,370.00 USD | 34,340.00 USD | 0.00 USD |
| `1D` | `10.54` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 15,130.00 USD | 66,080.00 USD | 144,770.00 USD |
| `7D` | `10.55` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 121,680.00 USD | 114,000.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 96,350.00 USD | 26,820.00 USD | 23,050.00 USD |
| `7D` | `10.57` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 54,810.00 USD | 29,840.00 USD | 20,150.00 USD |
| `7D` | `10.59` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 0.00 USD | 2,610.00 USD | 0.00 USD |
| `1D` | `10.60` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 9,410.00 USD | 18,890.00 USD | 0.00 USD |
| `7D` | `10.61` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 4,720.00 USD | 0.00 USD | 503.21 USD |
| `1D` | `10.62` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 21,530.00 USD | 4,920.00 USD | 126,220.00 USD |
| `7D` | `10.63` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 58,950.00 USD | 0.00 USD | 264.13 USD |
| `1D` | `10.64` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 85,770.00 USD | 3,750.00 USD | 44,240.00 USD |
| `7D` | `10.65` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 16,010.00 USD | 0.00 USD | 168.26 USD |
| `1D` | `10.66` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 53,760.00 USD | 7,540.00 USD | 29,670.00 USD |
| `7D` | `10.67` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD |
| `1D` | `10.68` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD |
| `7D` | `10.69` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD |
| `1D` | `10.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD |
| `7D` | `10.71` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 433,250.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,300.00 USD |
| `7D` | `10.73` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 0.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.75` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 4,030.00 USD | 31,380.00 USD | 99,850.00 USD |
| `1D` | `10.76` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 35,390.00 USD | 65,300.00 USD | 51,640.00 USD |
| `7D` | `10.77` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 537,300.00 USD | 111,300.00 USD | 103,760.00 USD |
| `1D` | `10.78` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 190,170.00 USD | 140,640.00 USD | 46,300.00 USD |
| `7D` | `10.79` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 79,540.00 USD | 64,510.00 USD | 0.00 USD |
| `1D` | `10.80` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 66,060.00 USD | 23,280.00 USD | 9,990.00 USD |
| `7D` | `10.81` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD |
| `1D` | `10.82` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 106,890.00 USD | 31,060.00 USD | 12.95 USD |
| `7D` | `10.83` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 80,420.00 USD | 402,020.00 USD |
| `1D` | `10.84` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 351,160.00 USD | 5,480.00 USD | 16,050.00 USD |
| `7D` | `10.85` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 295,700.00 USD | 3,610.00 USD | 612.08 USD |
| `1D` | `10.86` | 901,310.00 USD | 0.00 USD | 901,310.00 USD | 155,010.00 USD | 23,860.00 USD | 189,040.00 USD |
| `7D` | `10.87` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 323,850.00 USD | 35,390.00 USD | 502,670.00 USD |
| `1D` | `10.88` | 533,390.00 USD | 0.00 USD | 533,390.00 USD | 49,200.00 USD | 9,550.00 USD | 59,670.00 USD |
| `7D` | `10.89` | 959,600.00 USD | 0.00 USD | 959,600.00 USD | 111,430.00 USD | 41,880.00 USD | 261,140.00 USD |
| `1D` | `10.90` | 414,970.00 USD | 0.00 USD | 414,970.00 USD | 114,210.00 USD | 35,090.00 USD | 49,030.00 USD |
| `7D` | `10.91` | 545,160.00 USD | 0.00 USD | 545,160.00 USD | 10,280.00 USD | 0.00 USD | 248,200.00 USD |
| `1D` | `10.92` | 216,630.00 USD | 0.00 USD | 216,630.00 USD | 103,270.00 USD | 19,240.00 USD | 74.31 USD |
| `7D` | `10.93` | 286,690.00 USD | 0.00 USD | 286,690.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.94` | 94,050.00 USD | 0.00 USD | 94,050.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.95` | 70,060.00 USD | 0.00 USD | 70,060.00 USD | 7,820.00 USD | 0.00 USD | 49,920.00 USD |
| `1D` | `10.96` | 88,120.00 USD | 0.00 USD | 88,120.00 USD | 0.00 USD | 0.00 USD | 88,120.00 USD |
| `7D` | `10.97` | 12,320.00 USD | 0.00 USD | 12,320.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.98` | 175.98 USD | 175.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | 175.98 USD |
| `1D` | `10.98` | 351.96 USD | 351.96 USD | 0.00 USD | 0.00 USD | 0.00 USD | 175.98 USD |
| `7D` | `10.99` | 224,900.00 USD | 224,900.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD |
| `7D` | `10.99` | 449,800.00 USD | 449,800.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 818.96 USD | 818.96 USD | 0.00 USD | 0.00 USD | 467.00 USD | 0.00 USD |
| `7D` | `11.01` | 461,480.00 USD | 461,480.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 1,090.00 USD |
| `1D` | `11.02` | 151,730.00 USD | 151,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 150,910.00 USD |
| `7D` | `11.03` | 729,460.00 USD | 729,460.00 USD | 0.00 USD | 16,740.00 USD | 27,490.00 USD | 223,750.00 USD |
| `1D` | `11.04` | 307,900.00 USD | 307,900.00 USD | 0.00 USD | 0.00 USD | 2,200.00 USD | 153,970.00 USD |
| `7D` | `11.05` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 6,540.00 USD | 40,210.00 USD | 230,470.00 USD |
| `1D` | `11.06` | 334,880.00 USD | 334,880.00 USD | 0.00 USD | 0.00 USD | 26,840.00 USD | 135.97 USD |
| `7D` | `11.07` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.08` | 637,270.00 USD | 637,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302,390.00 USD |
| `7D` | `11.09` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 4,680.00 USD | 251,330.00 USD |
| `1D` | `11.10` | 645,250.00 USD | 645,250.00 USD | 0.00 USD | 7,750.00 USD | 0.00 USD | 232.88 USD |
| `7D` | `11.11` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 283,610.00 USD | 3,950.00 USD | 214,670.00 USD |
| `1D` | `11.12` | 790,460.00 USD | 790,460.00 USD | 0.00 USD | 6,320.00 USD | 2,260.00 USD | 136,640.00 USD |
| `7D` | `11.13` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 371,200.00 USD | 11,160.00 USD | 108,490.00 USD |
| `1D` | `11.14` | 863,440.00 USD | 863,440.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD | 68,070.00 USD |
| `7D` | `11.15` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 65,340.00 USD |
| `1D` | `11.16` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,470.00 USD |
| `7D` | `11.17` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,970.00 USD | 86,750.00 USD | 413.42 USD |
| `1D` | `11.18` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,520.00 USD |
| `7D` | `11.19` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79,180.00 USD |
| `1D` | `11.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 76,580.00 USD | 72,530.00 USD | 74,170.00 USD |
| `7D` | `11.21` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 554,520.00 USD | 106,700.00 USD | 1,090.00 USD |
| `1D` | `11.22` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 320,360.00 USD | 53,200.00 USD | 112,830.00 USD |
| `7D` | `11.23` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 288,220.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.24` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 163,340.00 USD | 54,170.00 USD | 151,640.00 USD |
| `7D` | `11.25` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 336,740.00 USD | 5,230.00 USD | 130,190.00 USD |
| `1D` | `11.26` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 149,280.00 USD | 41,730.00 USD | 67,760.00 USD |
| `7D` | `11.27` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 393,370.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.28` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 336,790.00 USD | 59,260.00 USD | 259,740.00 USD |
| `7D` | `11.29` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 206,860.00 USD | 57,050.00 USD | 56,290.00 USD |
| `1D` | `11.30` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 213,610.00 USD | 75,000.00 USD | 129,740.00 USD |
| `7D` | `11.31` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.32` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 168,840.00 USD | 74,250.00 USD | 142,080.00 USD |
| `7D` | `11.33` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 165,980.00 USD | 82,860.00 USD | 144,500.00 USD |
| `1D` | `11.34` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 390,100.00 USD | 118,470.00 USD | 107,170.00 USD |
| `7D` | `11.35` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 182,690.00 USD | 86,770.00 USD | 19,810.00 USD |
| `1D` | `11.36` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 138,710.00 USD | 95,240.00 USD | 56,340.00 USD |
| `7D` | `11.37` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 121,950.00 USD | 84,950.00 USD | 131,810.00 USD |
| `1D` | `11.38` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,330.00 USD |
| `7D` | `11.39` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 56,830.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,530.00 USD |
| `7D` | `11.41` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 35,150.00 USD |
| `1D` | `11.42` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 126,960.00 USD | 77,100.00 USD | 104,890.00 USD |
| `7D` | `11.43` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 265,450.00 USD | 105,330.00 USD | 92,240.00 USD |
| `1D` | `11.44` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 84,630.00 USD | 43,290.00 USD | 94,390.00 USD |
| `7D` | `11.45` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 227,420.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.46` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 86,190.00 USD | 75,110.00 USD | 48,870.00 USD |
| `7D` | `11.47` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 17,370.00 USD | 42,570.00 USD | 30,160.00 USD |
| `1D` | `11.48` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 24,020.00 USD | 29,490.00 USD | 452.42 USD |
| `7D` | `11.49` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.50` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 52,620.00 USD | 34,750.00 USD | 53,880.00 USD |
| `7D` | `11.51` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 91,790.00 USD | 28,520.00 USD | 511.81 USD |
| `1D` | `11.52` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 103,860.00 USD | 16,980.00 USD | 39,790.00 USD |
| `7D` | `11.53` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 66,280.00 USD |
| `1D` | `11.54` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 86,680.00 USD | 20,290.00 USD | 100,860.00 USD |
| `7D` | `11.55` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 91,310.00 USD | 19,070.00 USD | 75,870.00 USD |
| `1D` | `11.56` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 128,820.00 USD | 20,640.00 USD | 47,700.00 USD |
| `7D` | `11.57` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.58` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 58,440.00 USD | 2,950.00 USD | 17,570.00 USD |
| `7D` | `11.59` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 23,030.00 USD |
| `1D` | `11.60` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 59,560.00 USD | 14,330.00 USD | 67,440.00 USD |
| `7D` | `11.61` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 47,630.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.62` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 44,510.00 USD | 512.95 USD | 48,080.00 USD |
| `7D` | `11.63` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 101,580.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.64` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 5,220.00 USD | 7,410.00 USD | 31,580.00 USD |
| `7D` | `11.65` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | 18,430.00 USD |
| `1D` | `11.66` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,790.00 USD |
| `7D` | `11.67` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 93,990.00 USD |
| `1D` | `11.68` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 126,110.00 USD | 35,770.00 USD | 31,840.00 USD |
| `7D` | `11.69` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 38,760.00 USD | 16,460.00 USD | 39,300.00 USD |
| `1D` | `11.70` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,540.00 USD |
| `7D` | `11.71` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 146,640.00 USD | 722.15 USD | 49,310.00 USD |
| `1D` | `11.72` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 121,720.00 USD | 18,090.00 USD | 98,520.00 USD |
| `7D` | `11.73` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 62,800.00 USD | 528.30 USD | 121,760.00 USD |
| `1D` | `11.74` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 76,690.00 USD | 30,300.00 USD | 73,280.00 USD |
| `7D` | `11.75` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 17,390.00 USD | 504.13 USD | 35,790.00 USD |
| `1D` | `11.76` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 26,090.00 USD | 14,880.00 USD | 24,570.00 USD |
| `7D` | `11.77` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 43,650.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.78` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 27,690.00 USD | 20,510.00 USD | 40,050.00 USD |
| `7D` | `11.79` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.80` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 1,190.00 USD | 18,000.00 USD | 150.81 USD |
| `7D` | `11.81` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 166,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 11,880.00 USD | 53.10 USD | 36,200.00 USD |
| `7D` | `11.83` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.84` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 43,880.00 USD | 11,870.00 USD | 45,920.00 USD |
| `7D` | `11.85` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.86` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD |
| `7D` | `11.87` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.88` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD |
| `7D` | `11.89` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.90` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 28,290.00 USD |
| `7D` | `11.91` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.92` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,010.00 USD |
| `7D` | `11.93` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 18,580.00 USD | 14,930.00 USD | 38,820.00 USD |
| `1D` | `11.94` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 48,030.00 USD | 15,270.00 USD | 40,150.00 USD |
| `7D` | `11.95` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD |
| `7D` | `11.97` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 379,270.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.98` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 64,190.00 USD | 29,060.00 USD | 76,320.00 USD |
| `7D` | `11.99` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.00` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 119,890.00 USD | 23,880.00 USD | 44,340.00 USD |
| `7D` | `12.01` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 204,590.00 USD | 7,350.00 USD | 247,680.00 USD |
| `1D` | `12.02` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 13,680.00 USD | 11,370.00 USD | 31,520.00 USD |
| `7D` | `12.03` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 347,250.00 USD | 155,110.00 USD | 205,570.00 USD |
| `1D` | `12.04` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 90,660.00 USD | 39,490.00 USD | 56,280.00 USD |
| `7D` | `12.05` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.06` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 76,750.00 USD | 43,270.00 USD | 69,750.00 USD |
| `7D` | `12.07` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,400.00 USD |
| `1D` | `12.08` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 43,090.00 USD | 38,850.00 USD | 50,700.00 USD |
| `7D` | `12.09` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 215,750.00 USD | 90,820.00 USD | 50,380.00 USD |
| `1D` | `12.10` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 49,200.00 USD | 21,380.00 USD | 29,920.00 USD |
| `7D` | `12.11` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.12` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 116,760.00 USD | 54,460.00 USD | 50,350.00 USD |
| `7D` | `12.13` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 148,530.00 USD | 74,170.00 USD | 48,150.00 USD |
| `1D` | `12.14` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 75,780.00 USD | 35,660.00 USD | 55,750.00 USD |
| `7D` | `12.15` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 287,440.00 USD | 100,800.00 USD | 129,160.00 USD |
| `1D` | `12.16` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 124,550.00 USD | 34,710.00 USD | 67,580.00 USD |
| `7D` | `12.17` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.18` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 112,670.00 USD | 46,930.00 USD | 47,720.00 USD |
| `7D` | `12.19` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 196,990.00 USD | 58,810.00 USD | 63,360.00 USD |
| `1D` | `12.20` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 71,000.00 USD | 43,870.00 USD | 38,790.00 USD |
| `7D` | `12.21` | 16,170,000.00 USD | 16,170,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 99,390.00 USD |
| `1D` | `12.22` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 10,400.00 USD | 18,360.00 USD | 32,260.00 USD |
| `7D` | `12.23` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 140,270.00 USD | 27,350.00 USD | 9,170.00 USD |
| `1D` | `12.24` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 4,800.00 USD | 15,280.00 USD | 0.00 USD |
| `7D` | `12.25` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 101,460.00 USD | 47,320.00 USD | 46,950.00 USD |
| `7D` | `12.27` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 68,520.00 USD | 40,890.00 USD | 64,060.00 USD |
| `7D` | `12.29` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 157,390.00 USD | 60,790.00 USD | 94,930.00 USD |
| `7D` | `12.31` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 66,830.00 USD | 28,200.00 USD | 36,230.00 USD |
| `7D` | `12.33` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 17,200.00 USD | 18,480.00 USD | 5,470.00 USD |
| `7D` | `12.35` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 24,330.00 USD | 9,820.00 USD | 19,060.00 USD |
| `7D` | `12.37` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 11,660.00 USD |
| `7D` | `12.39` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 76,330.00 USD | 27,290.00 USD | 54,860.00 USD |
| `7D` | `12.40` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 15,620.00 USD | 6,100.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `505.30M` | Total OI Tokens: `46,081,609.7 LINK`
  * 1h OI Change: `-1.90%` | 4h OI Change: `-3.07%` | 24h OI Change: `-7.59%`
  * Exchange Breakdown: Binance=`99.56M` | Bybit=`68.22M` | OKX=`26.49M` | Hyperliquid=`55.20M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.33K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0012%` |
| **USDT Bybit** | `-0.0028%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0018%` | **USDT Bitget** | `0.0086%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `47.09%` | `52.91%` | `0.89` | 14,460,000.00 USD |
| `15M` | `Binance` | `47.18%` | `52.82%` | `0.89` | 9,810,000.00 USD |
| `15M` | `OKX` | `62.04%` | `37.96%` | `1.63` | 820,690.00 USD |
| `15M` | `Bybit` | `35.05%` | `64.95%` | `0.54` | 920,860.00 USD |
| `15M` | `KuCoin` | `58.08%` | `41.92%` | `1.39` | 229,050.00 USD |
| `15M` | `Gate` | `49.02%` | `50.98%` | `0.96` | 659,180.00 USD |
| `15M` | `Bitget` | `37.35%` | `62.65%` | `0.60` | 181,600.00 USD |
| `15M` | `BingX` | `41.16%` | `58.84%` | `0.70` | 255,100.00 USD |
| `15M` | `MEXC` | `71.88%` | `28.12%` | `2.56` | 100,980.00 USD |
| `15M` | `Bitunix` | `54.56%` | `45.44%` | `1.20` | 340,360.00 USD |
| `15M` | `Hyperliquid` | `60.49%` | `39.51%` | `1.53` | 134,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `42.19%` | `57.81%` | `0.73` | 146,250.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `2.89%` | `97.11%` | `0.03` | 272,390.00 USD |
| `15M` | `HTX` | `62.17%` | `37.83%` | `1.64` | 112,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `31.54%` | `68.46%` | `0.46` | 93,250.00 USD |
| `15M` | `Aster` | `54.66%` | `45.34%` | `1.21` | 304,510.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.96%` | `44.04%` | `1.27` | 92,190.00 USD |
| `15M` | `Whale Positions` | `47.18%` | `52.82%` | `0.89` | 9,810,000.00 USD |
| `15M` | `Global Accounts` | `47.09%` | `52.91%` | `0.89` | 14,460,000.00 USD |
| `1H` | `LINK` | `50.79%` | `49.21%` | `1.03` | 30,120,000.00 USD |
| `1H` | `Binance` | `50.73%` | `49.27%` | `1.03` | 11,250,000.00 USD |
| `1H` | `OKX` | `46.32%` | `53.68%` | `0.86` | 4,570,000.00 USD |
| `1H` | `Bybit` | `67.23%` | `32.77%` | `2.05` | 4,970,000.00 USD |
| `1H` | `KuCoin` | `52.11%` | `47.89%` | `1.09` | 745,370.00 USD |
| `1H` | `Gate` | `38.83%` | `61.17%` | `0.63` | 1,540,000.00 USD |
| `1H` | `Bitget` | `61.33%` | `38.67%` | `1.59` | 826,880.00 USD |
| `1H` | `BingX` | `14.31%` | `85.69%` | `0.17` | 1,470,000.00 USD |
| `1H` | `MEXC` | `47.58%` | `52.42%` | `0.91` | 181,610.00 USD |
| `1H` | `Bitunix` | `54.17%` | `45.83%` | `1.18` | 421,490.00 USD |
| `1H` | `Hyperliquid` | `43.8%` | `56.2%` | `0.78` | 2,970,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.46%` | `49.54%` | `1.02` | 357,340.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.8%` | `0.2%` | `499.00` | 124,950.00 USD |
| `1H` | `HTX` | `58.47%` | `41.53%` | `1.41` | 123,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `76.88%` | `23.12%` | `3.33` | 331,300.00 USD |
| `1H` | `Aster` | `65.48%` | `34.52%` | `1.90` | 42,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `79.26%` | `20.74%` | `3.82` | 196,230.00 USD |
| `1H` | `Whale Positions` | `50.73%` | `49.27%` | `1.03` | 11,250,000.00 USD |
| `1H` | `Global Accounts` | `50.79%` | `49.21%` | `1.03` | 30,120,000.00 USD |
| `4H` | `LINK` | `48.48%` | `51.52%` | `0.94` | 170,740,000.00 USD |
| `4H` | `Binance` | `46.85%` | `53.15%` | `0.88` | 82,440,000.00 USD |
| `4H` | `OKX` | `46.87%` | `53.13%` | `0.88` | 21,500,000.00 USD |
| `4H` | `Bybit` | `53.58%` | `46.42%` | `1.15` | 23,710,000.00 USD |
| `4H` | `KuCoin` | `50.03%` | `49.97%` | `1.00` | 3,050,000.00 USD |
| `4H` | `Gate` | `43.44%` | `56.56%` | `0.77` | 5,340,000.00 USD |
| `4H` | `Bitget` | `52.24%` | `47.76%` | `1.09` | 5,220,000.00 USD |
| `4H` | `BingX` | `25.26%` | `74.74%` | `0.34` | 2,940,000.00 USD |
| `4H` | `MEXC` | `51.28%` | `48.72%` | `1.05` | 1,970,000.00 USD |
| `4H` | `Bitunix` | `49.26%` | `50.74%` | `0.97` | 3,330,000.00 USD |
| `4H` | `Hyperliquid` | `54.47%` | `45.53%` | `1.20` | 14,120,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 2,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `59.54%` | `40.46%` | `1.47` | 801,480.00 USD |
| `4H` | `HTX` | `43.31%` | `56.69%` | `0.76` | 727,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `72.36%` | `27.64%` | `2.62` | 453,670.00 USD |
| `4H` | `Aster` | `41.12%` | `58.88%` | `0.70` | 1,100,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `60.61%` | `39.39%` | `1.54` | 1,060,000.00 USD |
| `4H` | `Whale Positions` | `46.85%` | `53.15%` | `0.88` | 82,440,000.00 USD |
| `4H` | `Global Accounts` | `48.48%` | `51.52%` | `0.94` | 170,740,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.11` | `11.11` | `11.11` | `11.13` | `11.07` | 1,646,720.35 USD | 860,860.38 USD | 785,859.96 USD | 75,000.42 USD | `+4.55%` | `16B / 7S` |
| `0:00 UTC` | `11.14` | `11.07` | `11.14` | `11.15` | `11.01` | 2,445,438.23 USD | 1,141,920.05 USD | 1,303,518.19 USD | -161,598.14 USD | `-6.61%` | `15B / 43S` |
| `5:00 UTC` | `11.07` | `11.04` | `11.07` | `11.07` | `11.00` | 2,041,123.66 USD | 896,885.50 USD | 1,144,238.16 USD | -247,352.65 USD | `-12.12%` | `4B / 9S` |
| `0:00 UTC` | `11.04` | `11.03` | `11.04` | `11.08` | `10.99` | 1,789,361.54 USD | 895,862.51 USD | 893,499.03 USD | 2,363.48 USD | `+0.13%` | `15B / 15S` |
| `5:00 UTC` | `11.07` | `11.08` | `11.07` | `11.11` | `11.04` | 1,641,738.88 USD | 696,135.31 USD | 945,603.58 USD | -249,468.27 USD | `-15.20%` | `10B / 19S` |
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.07` | `11.00` | 1,477,587.17 USD | 739,486.08 USD | 738,101.09 USD | 1,384.99 USD | `+0.09%` | `8B / 13S` |
| `5:00 UTC` | `11.00` | `11.01` | `11.00` | `11.05` | `10.99` | 1,128,540.66 USD | 513,281.75 USD | 615,258.92 USD | -101,977.17 USD | `-9.04%` | `14B / 18S` |
| `0:00 UTC` | `11.01` | `11.00` | `11.01` | `11.03` | `10.97` | 1,915,299.28 USD | 805,989.55 USD | 1,109,309.72 USD | -303,320.17 USD | `-15.84%` | `3B / 10S` |
| `5:00 UTC` | `10.97` | `10.99` | `10.97` | `11.01` | `10.96` | 1,089,442.23 USD | 506,886.53 USD | 582,555.71 USD | -75,669.18 USD | `-6.95%` | `5B / 8S` |
| `0:00 UTC` | `10.98` | `10.98` | `10.98` | `11.00` | `10.95` | 668,580.08 USD | 284,176.04 USD | 384,404.04 USD | -100,227.99 USD | `-14.99%` | `15B / 12S` |

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
| `5m` | 16,110.00 USD | 36,160.00 USD | **`ACCUMULATION`** |
| `15m` | -13,650.00 USD | -62,860.00 USD | **`DISTRIBUTION`** |
| `30m` | -35,430.00 USD | -176,270.00 USD | **`DISTRIBUTION`** |
| `1h` | -301,410.00 USD | -743,220.00 USD | **`DISTRIBUTION`** |
| `2h` | -570,750.00 USD | -1,750,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -282,490.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,360,000.00 USD | -2,430,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,690,000.00 USD | 2,320,000.00 USD | **`ACCUMULATION`** |
| `12h` | -6,290,000.00 USD | -12,890,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,540,000.00 USD | -22,980,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,910,000.00 USD | -42,760,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,190,000.00 USD | -193,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.11K` | 15m=`-13.65K` | 1h=`-301.41K` | 24h=`-11.54M`
* Futures Capital Netflows: 5m=`+36.16K` | 15m=`-62.86K` | 1h=`-743.22K` | 24h=`-22.98M`
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
  * `2026-10-30 14:41:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:27 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.32` (Risk Distance: `0.2284` pts)
  * +2.5R Take Profit: `11.12`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.35` (Risk Distance: `0.2284` pts)
  * +2.5R Take Profit: `10.55`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.07`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
