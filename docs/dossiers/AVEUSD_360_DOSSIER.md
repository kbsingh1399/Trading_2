# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:49:57 IST` (`2026-10-29 18:19:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `133.93` | **Live Ask Quote**: `134.22` | **Mid Price**: `134.07`
- **Spread Points**: `29.00` | **Spread BPS**: `21.63 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `132.35` | VWAP Z-Score: `+0.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `139.13` | Lower -3.00σ Band: `125.56`
  * Upper +2.51σ Band: `138.03` | Lower -2.51σ Band: `126.67`
  * Upper +2.01σ Band: `136.89` | Lower -2.01σ Band: `127.80`
  * Upper +2.00σ Band: `136.87` | Lower -2.00σ Band: `127.83`
  * Upper +1.28σ Band: `135.24` | Lower -1.28σ Band: `129.45`
  * Upper +1.00σ Band: `134.61` | Lower -1.00σ Band: `130.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`134.62` | EMA-20=`134.37` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`133.28` (Slope: `+0.0000`) | EMA-100=`132.85`
  * Institutional Anchors: EMA-144=`132.81` | EMA-200=`132.80` (Slope: `+0.2466`) | EMA-233=`132.77`
- **Range Boundaries**: 24H High=`138.47` | 24H Low=`128.25` | Weekly High=`138.47` | Weekly Low=`128.25`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `136.70` (Distance: `-1.83%`)
  * Point of Control (POC) = `132.93` (Distance: `+0.95%`)
  * Value Area Low (VAL) = `130.73` (Distance: `+2.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`135.85` | POC=`134.70` | VAL=`132.04`
  * Prior Day Extremes: PDH=`138.47` | PDL=`129.42` | PDC=`134.07`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.98` | Weekly POC=`134.76` | Weekly VAL=`131.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`135.37` | Low=`128.25`
  * London Session (08:00-16:00 UTC): High=`133.60` | Low=`129.16`
  * New York Session (13:00-21:00 UTC): High=`137.67` | Low=`130.09`
  * Initial Balance (First Hour): IB High=`131.85` | IB Low=`129.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `133.54` - `134.61`
  * Optimal Trade Entry (OTE 0.705): `134.34`
  * Structural Invalidation Anchor (0.786): `135.15`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| --- | **`134.07`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `405` | `0x3ee5...4fab` | `LONG` | 5,799,681.95 USD | `43,303.83` | `77.35` | `133.94` | `114.23` | 2,449,991.91 USD | `+42.24%` | `10X Cross` |
| `757` | `0x0514...bdfe` | `SHORT` | 3,080,160.00 USD | `23,000.00` | `87.41` | `133.94` | `183.20` | -1,069,680.78 USD | `-34.73%` | `10X Cross` |
| `799` | `0x08c1...1135` | `LONG` | 2,924,519.59 USD | `21,836.18` | `80.89` | `133.94` | `94.76` | 1,158,185.24 USD | `+39.60%` | `10X Cross` |
| `1000` | `0x0996...0ba6` | `SHORT` | 2,276,470.00 USD | `17,000.00` | `107.97` | `133.94` | `196.59` | -440,896.70 USD | `-19.37%` | `3X Cross` |
| `1061` | `0x45d2...4029` | `SHORT` | 2,108,343.31 USD | `15,721.00` | `118.40` | `133.94` | `2350.74` | -246,952.13 USD | `-11.71%` | `10X Cross` |
| `1077` | `0xbfc7...80b4` | `SHORT` | 2,083,682.17 USD | `15,561.48` | `115.30` | `133.94` | `409.62` | -289,382.85 USD | `-13.89%` | `10X Cross` |
| `1172` | `0x6540...f7b7` | `LONG` | 1,957,995.87 USD | `14,613.00` | `145.70` | `133.94` | `91.04` | -171,187.27 USD | `-8.74%` | `5X Isolated` |
| `1257` | `0x07fd...689d` | `LONG` | 1,822,026.83 USD | `13,600.26` | `150.55` | `133.94` | `0.000000` | -225,545.30 USD | `-12.38%` | `10X Cross` |
| `1417` | `0xcac1...26b3` | `SHORT` | 1,606,920.00 USD | `12,000.00` | `125.37` | `133.94` | `768.66` | -102,479.14 USD | `-6.38%` | `10X Cross` |
| `1436` | `0xeadc...9d55` | `LONG` | 1,583,341.13 USD | `11,823.92` | `89.93` | `133.94` | `0.000000` | 519,984.72 USD | `+32.84%` | `10X Cross` |
| `1578` | `0x9df2...c665` | `SHORT` | 1,410,239.27 USD | `10,532.82` | `133.81` | `133.94` | `2799.57` | -789.63 USD | `-0.06%` | `10X Cross` |
| `1636` | `0x3dc9...54b0` | `SHORT` | 1,338,699.00 USD | `10,000.00` | `128.60` | `133.94` | `1511.50` | -52,677.17 USD | `-3.93%` | `10X Cross` |
| `1751` | `0x8af7...fa05` | `SHORT` | 1,223,283.14 USD | `9,133.75` | `131.49` | `133.94` | `2205.22` | -22,302.39 USD | `-1.82%` | `10X Cross` |
| `1909` | `0x72db...8bb6` | `LONG` | 1,071,360.00 USD | `8,000.00` | `180.99` | `133.94` | `0.000000` | -376,597.43 USD | `-35.15%` | `10X Cross` |
| `1983` | `0x12d2...f97f` | `LONG` | 1,027,792.30 USD | `7,675.82` | `143.31` | `133.94` | `0.000000` | -72,200.42 USD | `-7.02%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`138.85` (Vol: 128,600.00 USD, Dist: `+3.81%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.77%`)
  * 48H Horizon: Short MP=`140.15` (Vol: 183,800.00 USD, Dist: `+4.79%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.77%`)
  * 3D Horizon: Short MP=`140.15` (Vol: 159,300.00 USD, Dist: `+4.79%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.77%`)
  * 7D Horizon: Short MP=`140.55` (Vol: 267,100.00 USD, Dist: `+5.08%`) | Long MP=`127.34` (Vol: 265,000.00 USD, Dist: `--4.79%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `29.50` | 718.92 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 1,890.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 380.89 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 3,560.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 3,540.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 483.97 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 862.78 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 665.12 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 3,970.00 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,700.00 USD | 10,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 136,760.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 5,700.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 323.75 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 4,590.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 246.94 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 2,350.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 22,710.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,510.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 336.99 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 13,210.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,820.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 2,080.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,050.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 134.47 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 855.88 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 8,530.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 51,060.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,610.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 14,280.00 USD | 10,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 65,710.00 USD | 10,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 7,290.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 55,690.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 1,610,000.00 USD | 10,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 12,350.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 9,020.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,070,000.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 13,290.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 8,520.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 91,600.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 40,740.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 946.25 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 7,780.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,850.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 4,750.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 10,710.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 258,120.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 14,600.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 40,630.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 15,190.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 15,810.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 606,920.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 2,020.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 12,520.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 40,620.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,970,000.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 80,430.00 USD | 504,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 60,290.00 USD | 423,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 147,040.00 USD | 363,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 11,320.00 USD | 216,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 781.53 USD | 205,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 14,670.00 USD | 204,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 7,060.00 USD | 189,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 27,360.00 USD | 182,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 16,050.00 USD | 155,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 26,980.00 USD | 139,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 17,870.00 USD | 112,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 67,290.00 USD | 94,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 12,820.00 USD | 12,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 23,770.00 USD | 27,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `129.50` | 1,500.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 1,860.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 2,080.00 USD | 14,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 15,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,350.00 USD | 16,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 2,360.00 USD | 18,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 869.25 USD | 19,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 22,650.00 USD | 42,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 394.49 USD | 42,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 43,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 88,250.00 USD | 131,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 2,060.00 USD | 133,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 595,110.00 USD | 728,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 877.56 USD | 729,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 2,200.00 USD | 731,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 229.95 USD | 732,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,820.00 USD | 733,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 337.99 USD | 734,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 735,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 736,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 138.99 USD | 736,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 356.34 USD | 737,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 31,610.00 USD | 768,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 870.97 USD | 769,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 775,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 777,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 4,930.00 USD | 782,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 4,300,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 13,360.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 656,380.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,510.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 3,560.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 17,700.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 59,550.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 837.90 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `204.50` | 9,790.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 193.58 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 21,680.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `219.50` | 2,940.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 947.10 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 1,370.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 46,600.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `228.50` | 221.64 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,310.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 192.29 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `235.50` | 24,770.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 4,750.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 546.06 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 647.48 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `245.50` | 284.78 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `252.50` | 558.02 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `253.50` | 1,780.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `254.50` | 6,970.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `255.50` | 424.13 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `256.50` | 813.11 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `257.50` | 1,430.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `262.50` | 763.88 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `263.50` | 16,340.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `264.50` | 10,480.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `267.50` | 21,110.00 USD | 9,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `29.50` | 10,880,000.00 USD | 0.00 USD | 718.92 USD | `-77.94%` | `24.37` |
| `Live` | `Long` | `31.50` | 10,870,000.00 USD | 0.00 USD | 1,890.00 USD | `-76.45%` | `60.00` |
| `Live` | `Long` | `33.50` | 10,870,000.00 USD | 0.00 USD | 380.89 USD | `-74.95%` | `11.37` |
| `Live` | `Long` | `34.50` | 10,870,000.00 USD | 0.00 USD | 3,560.00 USD | `-74.20%` | `103.05` |
| `Live` | `Long` | `38.50` | 10,870,000.00 USD | 0.00 USD | 232.54 USD | `-71.21%` | `6.04` |
| `Live` | `Long` | `39.50` | 10,870,000.00 USD | 0.00 USD | 3,540.00 USD | `-70.47%` | `89.57` |
| `Live` | `Long` | `40.50` | 10,860,000.00 USD | 0.00 USD | 483.97 USD | `-69.72%` | `11.95` |
| `Live` | `Long` | `41.50` | 10,860,000.00 USD | 0.00 USD | 862.78 USD | `-68.97%` | `20.79` |
| `Live` | `Long` | `43.50` | 10,860,000.00 USD | 0.00 USD | 665.12 USD | `-67.47%` | `15.29` |
| `Live` | `Long` | `45.50` | 10,860,000.00 USD | 0.00 USD | 158.34 USD | `-65.98%` | `3.48` |
| `Live` | `Long` | `52.50` | 10,860,000.00 USD | 0.00 USD | 3,970.00 USD | `-60.74%` | `75.64` |
| `Live` | `Long` | `54.50` | 10,860,000.00 USD | 0.00 USD | 805.51 USD | `-59.25%` | `14.78` |
| `Live` | `Long` | `55.50` | 10,860,000.00 USD | 0.00 USD | 1,410.00 USD | `-58.50%` | `25.36` |
| `Live` | `Long` | `56.50` | 10,860,000.00 USD | 0.00 USD | 1,700.00 USD | `-57.75%` | `30.06` |
| `Live` | `Long` | `57.50` | 10,850,000.00 USD | 0.00 USD | 2,010.00 USD | `-57.01%` | `35.00` |
| `Live` | `Long` | `58.50` | 10,850,000.00 USD | 0.00 USD | 1,610.00 USD | `-56.26%` | `27.49` |
| `Live` | `Long` | `59.50` | 10,850,000.00 USD | 0.00 USD | 136,760.00 USD | `-55.51%` | `2,298.53` |
| `Live` | `Long` | `60.50` | 10,710,000.00 USD | 0.00 USD | 5,700.00 USD | `-54.76%` | `94.25` |
| `Live` | `Long` | `61.50` | 10,710,000.00 USD | 0.00 USD | 168.51 USD | `-54.02%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,710,000.00 USD | 0.00 USD | 323.75 USD | `-53.27%` | `5.18` |
| `Live` | `Long` | `63.50` | 10,710,000.00 USD | 0.00 USD | 4,590.00 USD | `-52.52%` | `72.34` |
| `Live` | `Long` | `65.50` | 10,700,000.00 USD | 0.00 USD | 246.94 USD | `-51.02%` | `3.77` |
| `Live` | `Long` | `66.50` | 10,700,000.00 USD | 0.00 USD | 2,350.00 USD | `-50.28%` | `35.29` |
| `Live` | `Long` | `67.50` | 10,700,000.00 USD | 0.00 USD | 24,320.00 USD | `-49.53%` | `360.30` |
| `Live` | `Long` | `68.50` | 10,680,000.00 USD | 0.00 USD | 22,710.00 USD | `-48.78%` | `331.46` |
| `Live` | `Long` | `69.50` | 10,650,000.00 USD | 0.00 USD | 18,510.00 USD | `-48.03%` | `266.40` |
| `Live` | `Long` | `70.50` | 10,640,000.00 USD | 0.00 USD | 336.99 USD | `-47.29%` | `4.78` |
| `Live` | `Long` | `71.50` | 10,640,000.00 USD | 0.00 USD | 13,210.00 USD | `-46.54%` | `184.76` |
| `Live` | `Long` | `73.50` | 10,620,000.00 USD | 0.00 USD | 11,820.00 USD | `-45.04%` | `160.80` |
| `Live` | `Long` | `74.50` | 10,610,000.00 USD | 0.00 USD | 2,080.00 USD | `-44.29%` | `27.98` |
| `Live` | `Long` | `75.50` | 10,610,000.00 USD | 0.00 USD | 1,050.00 USD | `-43.55%` | `13.87` |
| `Live` | `Long` | `77.50` | 10,610,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.05%` | `116.79` |
| `Live` | `Long` | `78.50` | 10,600,000.00 USD | 0.00 USD | 4,310.00 USD | `-41.30%` | `54.87` |
| `Live` | `Long` | `79.50` | 10,590,000.00 USD | 0.00 USD | 6,790.00 USD | `-40.56%` | `85.43` |
| `Live` | `Long` | `82.50` | 10,590,000.00 USD | 0.00 USD | 134.47 USD | `-38.31%` | `1.63` |
| `Live` | `Long` | `83.50` | 10,590,000.00 USD | 0.00 USD | 855.88 USD | `-37.57%` | `10.25` |
| `Live` | `Long` | `84.50` | 10,590,000.00 USD | 0.00 USD | 8,530.00 USD | `-36.82%` | `100.91` |
| `Live` | `Long` | `85.50` | 10,580,000.00 USD | 0.00 USD | 51,060.00 USD | `-36.07%` | `597.23` |
| `Live` | `Long` | `86.50` | 10,530,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.32%` | `18.61` |
| `Live` | `Long` | `87.50` | 10,520,000.00 USD | 0.00 USD | 14,280.00 USD | `-34.57%` | `163.22` |
| `Live` | `Long` | `88.50` | 10,510,000.00 USD | 0.00 USD | 65,710.00 USD | `-33.83%` | `742.43` |
| `Live` | `Long` | `89.50` | 10,440,000.00 USD | 0.00 USD | 7,290.00 USD | `-33.08%` | `81.46` |
| `Live` | `Long` | `90.50` | 10,440,000.00 USD | 0.00 USD | 55,690.00 USD | `-32.33%` | `615.35` |
| `Live` | `Long` | `91.50` | 10,380,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-31.58%` | `17,641.69` |
| `Live` | `Long` | `92.50` | 8,770,000.00 USD | 0.00 USD | 12,350.00 USD | `-30.84%` | `133.49` |
| `Live` | `Long` | `93.50` | 8,760,000.00 USD | 0.00 USD | 9,020.00 USD | `-30.09%` | `96.51` |
| `Live` | `Long` | `94.50` | 8,750,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-29.34%` | `21,938.59` |
| `Live` | `Long` | `95.50` | 6,670,000.00 USD | 0.00 USD | 13,290.00 USD | `-28.59%` | `139.19` |
| `Live` | `Long` | `96.50` | 6,660,000.00 USD | 0.00 USD | 8,520.00 USD | `-27.85%` | `88.25` |
| `Live` | `Long` | `97.50` | 6,650,000.00 USD | 0.00 USD | 91,600.00 USD | `-27.10%` | `939.53` |
| `Live` | `Long` | `98.50` | 6,560,000.00 USD | 0.00 USD | 40,740.00 USD | `-26.35%` | `413.65` |
| `Live` | `Long` | `99.50` | 6,520,000.00 USD | 0.00 USD | 946.25 USD | `-25.60%` | `9.51` |
| `Live` | `Long` | `100.50` | 6,520,000.00 USD | 0.00 USD | 7,780.00 USD | `-24.85%` | `77.41` |
| `Live` | `Long` | `102.50` | 6,510,000.00 USD | 0.00 USD | 11,850.00 USD | `-23.36%` | `115.59` |
| `Live` | `Long` | `103.50` | 6,500,000.00 USD | 0.00 USD | 4,750.00 USD | `-22.61%` | `45.85` |
| `Live` | `Long` | `104.50` | 6,490,000.00 USD | 0.00 USD | 10,710.00 USD | `-21.86%` | `102.51` |
| `Live` | `Long` | `105.50` | 6,480,000.00 USD | 0.00 USD | 258,120.00 USD | `-21.12%` | `2,446.66` |
| `Live` | `Long` | `106.50` | 6,220,000.00 USD | 0.00 USD | 14,600.00 USD | `-20.37%` | `137.12` |
| `Live` | `Long` | `107.50` | 6,210,000.00 USD | 0.00 USD | 40,630.00 USD | `-19.62%` | `377.94` |
| `Live` | `Long` | `108.50` | 6,170,000.00 USD | 0.00 USD | 15,190.00 USD | `-18.87%` | `140.04` |
| `Live` | `Long` | `109.50` | 6,150,000.00 USD | 0.00 USD | 15,810.00 USD | `-18.12%` | `144.39` |
| `Live` | `Long` | `110.50` | 6,140,000.00 USD | 0.00 USD | 606,920.00 USD | `-17.38%` | `5,492.51` |
| `Live` | `Long` | `111.50` | 5,530,000.00 USD | 0.00 USD | 2,020.00 USD | `-16.63%` | `18.13` |
| `Live` | `Long` | `112.50` | 5,530,000.00 USD | 0.00 USD | 12,520.00 USD | `-15.88%` | `111.32` |
| `Live` | `Long` | `113.50` | 5,520,000.00 USD | 0.00 USD | 40,620.00 USD | `-15.13%` | `357.91` |
| `Live` | `Long` | `114.50` | 5,480,000.00 USD | 0.00 USD | 4,970,000.00 USD | `-14.39%` | `43,424.14` |
| `Live` | `Long` | `115.50` | 504,280.00 USD | 0.00 USD | 80,430.00 USD | `-13.64%` | `696.33` |
| `Live` | `Long` | `116.50` | 423,860.00 USD | 0.00 USD | 60,290.00 USD | `-12.89%` | `517.51` |
| `Live` | `Long` | `117.50` | 363,570.00 USD | 0.00 USD | 147,040.00 USD | `-12.14%` | `1,251.42` |
| `Live` | `Long` | `118.50` | 216,520.00 USD | 0.00 USD | 11,320.00 USD | `-11.40%` | `95.51` |
| `Live` | `Long` | `119.50` | 205,210.00 USD | 0.00 USD | 781.53 USD | `-10.65%` | `6.54` |
| `Live` | `Long` | `120.50` | 204,430.00 USD | 0.00 USD | 14,670.00 USD | `-9.90%` | `121.77` |
| `Live` | `Long` | `121.50` | 189,750.00 USD | 0.00 USD | 7,060.00 USD | `-9.15%` | `58.13` |
| `Live` | `Long` | `122.50` | 182,690.00 USD | 0.00 USD | 27,360.00 USD | `-8.40%` | `223.37` |
| `Live` | `Long` | `123.50` | 155,330.00 USD | 0.00 USD | 16,050.00 USD | `-7.66%` | `129.98` |
| `Live` | `Long` | `124.50` | 139,270.00 USD | 0.00 USD | 26,980.00 USD | `-6.91%` | `216.72` |
| `Live` | `Long` | `125.50` | 112,290.00 USD | 0.00 USD | 17,870.00 USD | `-6.16%` | `142.40` |
| `Live` | `Long` | `126.50` | 94,420.00 USD | 0.00 USD | 67,290.00 USD | `-5.41%` | `531.97` |
| `Live` | `Short` | `127.50` | 12,820.00 USD | 12,820.00 USD | 0.00 USD | `-4.67%` | `100.51` |
| `Live` | `Long` | `128.50` | 27,130.00 USD | 0.00 USD | 23,770.00 USD | `-3.92%` | `184.97` |
| `Live` | `Long` | `129.50` | 3,360.00 USD | 0.00 USD | 1,500.00 USD | `-3.17%` | `11.60` |
| `Live` | `Long` | `130.50` | 1,860.00 USD | 0.00 USD | 1,860.00 USD | `-2.42%` | `14.22` |
| `Live` | `Short` | `137.50` | 14,900.00 USD | 2,080.00 USD | 0.00 USD | `+2.81%` | `15.16` |
| `Live` | `Short` | `139.50` | 15,000.00 USD | 100.44 USD | 0.00 USD | `+4.31%` | `0.72` |
| `Live` | `Short` | `140.50` | 16,350.00 USD | 1,350.00 USD | 0.00 USD | `+5.05%` | `9.59` |
| `Live` | `Short` | `141.50` | 18,700.00 USD | 2,360.00 USD | 0.00 USD | `+5.80%` | `16.66` |
| `Live` | `Short` | `142.50` | 19,570.00 USD | 869.25 USD | 0.00 USD | `+6.55%` | `6.10` |
| `Live` | `Short` | `143.50` | 42,220.00 USD | 22,650.00 USD | 0.00 USD | `+7.30%` | `157.82` |
| `Live` | `Short` | `144.50` | 42,620.00 USD | 394.49 USD | 0.00 USD | `+8.05%` | `2.73` |
| `Live` | `Short` | `145.50` | 43,350.00 USD | 731.87 USD | 0.00 USD | `+8.79%` | `5.03` |
| `Live` | `Short` | `150.50` | 131,590.00 USD | 88,250.00 USD | 0.00 USD | `+12.53%` | `586.35` |
| `Live` | `Short` | `151.50` | 133,650.00 USD | 2,060.00 USD | 0.00 USD | `+13.28%` | `13.60` |
| `Live` | `Short` | `152.50` | 728,760.00 USD | 595,110.00 USD | 0.00 USD | `+14.03%` | `3,902.35` |
| `Live` | `Short` | `154.50` | 729,640.00 USD | 877.56 USD | 0.00 USD | `+15.52%` | `5.68` |
| `Live` | `Short` | `155.50` | 731,840.00 USD | 2,200.00 USD | 0.00 USD | `+16.27%` | `14.15` |
| `Live` | `Short` | `157.50` | 732,070.00 USD | 229.95 USD | 0.00 USD | `+17.77%` | `1.46` |
| `Live` | `Short` | `158.50` | 733,890.00 USD | 1,820.00 USD | 0.00 USD | `+18.51%` | `11.47` |
| `Live` | `Short` | `166.50` | 734,230.00 USD | 337.99 USD | 0.00 USD | `+24.50%` | `2.03` |
| `Live` | `Short` | `167.50` | 735,800.00 USD | 1,580.00 USD | 0.00 USD | `+25.24%` | `9.42` |
| `Live` | `Short` | `168.50` | 736,800.00 USD | 995.84 USD | 0.00 USD | `+25.99%` | `5.91` |
| `Live` | `Short` | `169.50` | 736,940.00 USD | 138.99 USD | 0.00 USD | `+26.74%` | `0.82` |
| `Live` | `Short` | `170.50` | 737,290.00 USD | 356.34 USD | 0.00 USD | `+27.49%` | `2.09` |
| `Live` | `Short` | `172.50` | 768,910.00 USD | 31,610.00 USD | 0.00 USD | `+28.98%` | `183.25` |
| `Live` | `Short` | `173.50` | 769,780.00 USD | 870.97 USD | 0.00 USD | `+29.73%` | `5.02` |
| `Live` | `Short` | `175.50` | 775,400.00 USD | 5,620.00 USD | 0.00 USD | `+31.22%` | `32.04` |
| `Live` | `Short` | `181.50` | 777,560.00 USD | 2,170.00 USD | 0.00 USD | `+35.71%` | `11.93` |
| `Live` | `Short` | `182.50` | 782,490.00 USD | 4,930.00 USD | 0.00 USD | `+36.46%` | `27.00` |
| `Live` | `Short` | `183.50` | 5,080,000.00 USD | 4,300,000.00 USD | 0.00 USD | `+37.21%` | `23,420.00` |
| `Live` | `Short` | `185.50` | 5,090,000.00 USD | 13,360.00 USD | 0.00 USD | `+38.70%` | `72.00` |
| `Live` | `Short` | `186.50` | 5,750,000.00 USD | 656,380.00 USD | 0.00 USD | `+39.45%` | `3,519.45` |
| `Live` | `Short` | `187.50` | 5,750,000.00 USD | 4,510.00 USD | 0.00 USD | `+40.20%` | `24.03` |
| `Live` | `Short` | `189.50` | 5,760,000.00 USD | 867.91 USD | 0.00 USD | `+41.69%` | `4.58` |
| `Live` | `Short` | `191.50` | 5,760,000.00 USD | 1,500.00 USD | 0.00 USD | `+43.19%` | `7.83` |
| `Live` | `Short` | `192.50` | 5,760,000.00 USD | 358.05 USD | 0.00 USD | `+43.94%` | `1.86` |
| `Live` | `Short` | `193.50` | 5,760,000.00 USD | 3,560.00 USD | 0.00 USD | `+44.68%` | `18.42` |
| `Live` | `Short` | `194.50` | 5,780,000.00 USD | 17,700.00 USD | 0.00 USD | `+45.43%` | `91.00` |
| `Live` | `Short` | `196.50` | 9,120,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+46.93%` | `17,000.00` |
| `Live` | `Short` | `198.50` | 9,180,000.00 USD | 59,550.00 USD | 0.00 USD | `+48.42%` | `300.00` |
| `Live` | `Short` | `199.50` | 9,180,000.00 USD | 837.90 USD | 0.00 USD | `+49.17%` | `4.20` |
| `Live` | `Short` | `200.50` | 9,190,000.00 USD | 9,850.00 USD | 0.00 USD | `+49.92%` | `49.15` |
| `Live` | `Short` | `203.50` | 9,190,000.00 USD | 372.41 USD | 0.00 USD | `+52.16%` | `1.83` |
| `Live` | `Short` | `204.50` | 9,200,000.00 USD | 9,790.00 USD | 0.00 USD | `+52.91%` | `47.86` |
| `Live` | `Short` | `205.50` | 9,280,000.00 USD | 84,610.00 USD | 0.00 USD | `+53.66%` | `411.72` |
| `Live` | `Short` | `210.50` | 9,280,000.00 USD | 151.56 USD | 0.00 USD | `+57.39%` | `0.72` |
| `Live` | `Short` | `217.50` | 9,280,000.00 USD | 193.58 USD | 0.00 USD | `+62.63%` | `0.89` |
| `Live` | `Short` | `218.50` | 9,310,000.00 USD | 21,680.00 USD | 0.00 USD | `+63.38%` | `99.20` |
| `Live` | `Short` | `219.50` | 9,310,000.00 USD | 2,940.00 USD | 0.00 USD | `+64.12%` | `13.38` |
| `Live` | `Short` | `220.50` | 9,310,000.00 USD | 2,000.00 USD | 0.00 USD | `+64.87%` | `9.06` |
| `Live` | `Short` | `223.50` | 9,360,000.00 USD | 47,810.00 USD | 0.00 USD | `+67.12%` | `213.92` |
| `Live` | `Short` | `225.50` | 9,360,000.00 USD | 947.10 USD | 0.00 USD | `+68.61%` | `4.20` |
| `Live` | `Short` | `226.50` | 9,360,000.00 USD | 1,370.00 USD | 0.00 USD | `+69.36%` | `6.05` |
| `Live` | `Short` | `227.50` | 9,410,000.00 USD | 46,600.00 USD | 0.00 USD | `+70.11%` | `204.83` |
| `Live` | `Short` | `228.50` | 9,410,000.00 USD | 221.64 USD | 0.00 USD | `+70.85%` | `0.97` |
| `Live` | `Short` | `230.50` | 9,410,000.00 USD | 2,310.00 USD | 0.00 USD | `+72.35%` | `10.00` |
| `Live` | `Short` | `234.50` | 9,410,000.00 USD | 192.29 USD | 0.00 USD | `+75.34%` | `0.82` |
| `Live` | `Short` | `235.50` | 9,430,000.00 USD | 24,770.00 USD | 0.00 USD | `+76.09%` | `105.18` |
| `Live` | `Short` | `237.50` | 9,440,000.00 USD | 4,750.00 USD | 0.00 USD | `+77.58%` | `20.00` |
| `Live` | `Short` | `239.50` | 9,440,000.00 USD | 546.06 USD | 0.00 USD | `+79.08%` | `2.28` |
| `Live` | `Short` | `240.50` | 9,440,000.00 USD | 103.41 USD | 0.00 USD | `+79.83%` | `0.43` |
| `Live` | `Short` | `242.50` | 9,440,000.00 USD | 647.48 USD | 0.00 USD | `+81.32%` | `2.67` |
| `Live` | `Short` | `245.50` | 9,440,000.00 USD | 284.78 USD | 0.00 USD | `+83.57%` | `1.16` |
| `Live` | `Short` | `252.50` | 9,440,000.00 USD | 558.02 USD | 0.00 USD | `+88.80%` | `2.21` |
| `Live` | `Short` | `253.50` | 9,440,000.00 USD | 1,780.00 USD | 0.00 USD | `+89.55%` | `7.01` |
| `Live` | `Short` | `254.50` | 9,450,000.00 USD | 6,970.00 USD | 0.00 USD | `+90.29%` | `27.37` |
| `Live` | `Short` | `255.50` | 9,450,000.00 USD | 424.13 USD | 0.00 USD | `+91.04%` | `1.66` |
| `Live` | `Short` | `256.50` | 9,450,000.00 USD | 813.11 USD | 0.00 USD | `+91.79%` | `3.17` |
| `Live` | `Short` | `257.50` | 9,450,000.00 USD | 1,430.00 USD | 0.00 USD | `+92.54%` | `5.57` |
| `Live` | `Short` | `262.50` | 9,450,000.00 USD | 763.88 USD | 0.00 USD | `+96.28%` | `2.91` |
| `Live` | `Short` | `263.50` | 9,470,000.00 USD | 16,340.00 USD | 0.00 USD | `+97.02%` | `62.02` |
| `Live` | `Short` | `264.50` | 9,480,000.00 USD | 10,480.00 USD | 0.00 USD | `+97.77%` | `39.63` |
| `Live` | `Short` | `267.50` | 9,500,000.00 USD | 21,110.00 USD | 0.00 USD | `+100.01%` | `78.93` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.69K` | Last 24h: `22.61K` | Last 3d: `65.36K` | Last 7d: `109.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0053%` | **USDT OKX** | `0.0055%` |
| **USDT Bybit** | `0.0042%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0053%` | **USDT BingX** | `0.0060%` |
| **USDT Gate** | `0.0053%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `137.00` | `136.75` | `137.00` | `137.11` | `136.31` | 1,755,992.28 USD | 798,369.60 USD | 957,622.69 USD | -159,253.09 USD | `-9.07%` | `15B / 15S` |
| `0:00 UTC` | `136.91` | `137.14` | `136.91` | `137.94` | `136.38` | 2,268,812.62 USD | 1,173,914.80 USD | 1,094,897.82 USD | 79,016.99 USD | `+3.48%` | `32B / 27S` |
| `5:00 UTC` | `136.36` | `136.58` | `136.36` | `137.31` | `136.01` | 2,016,544.71 USD | 820,255.37 USD | 1,196,289.34 USD | -376,033.97 USD | `-18.65%` | `6B / 45S` |
| `0:00 UTC` | `136.31` | `135.82` | `136.31` | `136.41` | `135.25` | 1,856,319.84 USD | 851,137.54 USD | 1,005,182.30 USD | -154,044.76 USD | `-8.30%` | `11B / 26S` |
| `5:00 UTC` | `136.19` | `136.08` | `136.19` | `136.38` | `135.78` | 1,030,013.81 USD | 443,410.64 USD | 586,603.17 USD | -143,192.54 USD | `-13.90%` | `6B / 15S` |
| `0:00 UTC` | `135.20` | `135.14` | `135.20` | `135.91` | `134.62` | 2,622,608.21 USD | 1,514,994.17 USD | 1,107,614.04 USD | 407,380.13 USD | `+15.53%` | `12B / 29S` |
| `5:00 UTC` | `134.62` | `134.76` | `134.62` | `135.20` | `134.44` | 878,992.69 USD | 464,259.89 USD | 414,732.80 USD | 49,527.10 USD | `+5.63%` | `10B / 8S` |
| `0:00 UTC` | `134.09` | `134.61` | `134.09` | `135.59` | `133.75` | 1,172,719.65 USD | 442,820.23 USD | 729,899.42 USD | -287,079.19 USD | `-24.48%` | `18B / 51S` |
| `5:00 UTC` | `133.19` | `133.34` | `133.19` | `134.06` | `132.89` | 1,323,282.70 USD | 549,454.30 USD | 773,828.40 USD | -224,374.10 USD | `-16.96%` | `12B / 26S` |
| `0:00 UTC` | `133.56` | `133.83` | `133.56` | `134.20` | `133.47` | 714,011.24 USD | 312,431.62 USD | 401,579.63 USD | -89,148.01 USD | `-12.49%` | `10B / 20S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:02` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `132.86` | 0.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.95` | 1,200.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 20K AAVE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `130.77` | 3,200.00 USD | 0.00 USD |
| `10-28 19:42` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `131.45` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.5` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `131.08` | 3,500.00 USD | 0.00 USD |
| `10-28 19:06` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.72` | 3,400.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `131.61` | 4,500.00 USD | 0.00 USD |
| `10-28 18:36` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.46` | 1,300.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.24` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `133.63` | 5,700.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `133.04` | 0.00 USD | 0.00 USD |
| `10-28 16:41` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `134.42` | 0.00 USD | 0.00 USD |
| `10-28 15:53` | `Range 0.5` | `Divergence` | **`BULLISH`** | Drop without taker selling | `135.39` | 0.00 USD | 0.00 USD |
| `10-28 13:58` | `Volume 20K AAVE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `136.84` | 0.00 USD | 0.00 USD |
| `10-28 13:36` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `135.33` | 3,200.00 USD | 0.00 USD |
| `10-28 11:03` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.16` | 3,800.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `134.87` | 0.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.37` | 1,400.00 USD | 0.00 USD |
| `10-28 09:16` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `136.00` | 1,200.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `136.00` | 3,700.00 USD | 0.00 USD |
| `10-28 08:34` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.67` | 3,800.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.22` | 0.00 USD | 0.00 USD |
| `10-28 08:15` | `Volume 20K AAVE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.66` | 0.00 USD | 0.00 USD |
| `10-28 08:09` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.15` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `135.87` | 3,900.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.5` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `135.17` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 10,190.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | -78,540.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | -436,500.00 USD | **`DISTRIBUTION`** |
| `1h` | 0.00 USD | -855,350.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -2,430,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -1,390,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -574,700.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -1,130,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -422,430.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -3,180,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -38,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -100,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+10.19K` | 15m=`-78.54K` | 1h=`-855.35K` | 24h=`-3.18M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `130.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `128.96` (Risk Distance: `1.77` pts)
  * +2.5R Take Profit: `135.16`
  * Mathematical Lot Sizing: **`5.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `136.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `138.47` (Risk Distance: `1.77` pts)
  * +2.5R Take Profit: `132.27`
  * Mathematical Lot Sizing: **`5.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`135.15`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
