# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `118.84` | **Live Ask Quote**: `119.15` | **Mid Price**: `119.00`
- **Spread Points**: `31.00` | **Spread BPS**: `26.05 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `130.07` | VWAP Z-Score: `-2.21` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `2.10` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `27.93` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `143.65` | Lower -3.00σ Band: `116.50`
  * Upper +2.51σ Band: `141.43` | Lower -2.51σ Band: `118.71`
  * Upper +2.01σ Band: `139.17` | Lower -2.01σ Band: `120.98`
  * Upper +2.00σ Band: `139.12` | Lower -2.00σ Band: `121.02`
  * Upper +1.28σ Band: `135.87` | Lower -1.28σ Band: `124.28`
  * Upper +1.00σ Band: `134.60` | Lower -1.00σ Band: `125.55`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`122.26` | EMA-20=`125.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`129.11` (Slope: `+0.0000`) | EMA-100=`130.68`
  * Institutional Anchors: EMA-144=`131.20` | EMA-200=`131.55` (Slope: `-0.8367`) | EMA-233=`131.81`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`118.05` | Weekly High=`138.47` | Weekly Low=`118.05`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `122.79` (Distance: `-3.12%`)
  * Point of Control (POC) = `119.02` (Distance: `-0.06%`)
  * Value Area Low (VAL) = `114.73` (Distance: `+3.68%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.94`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`119.47` | Low=`118.52`
  * New York Session (13:00-21:00 UTC): High=`119.71` | Low=`118.28`
  * Initial Balance (First Hour): IB High=`119.35` | IB Low=`118.64`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `118.52` - `119.47`
  * Optimal Trade Entry (OTE 0.705): `119.23`
  * Structural Invalidation Anchor (0.786): `119.95`

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
| --- | **`119.00`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `415` | `0x3ee5...4fab` | `LONG` | 5,169,178.19 USD | `43,303.83` | `77.35` | `120.07` | `100.13` | 1,819,488.15 USD | `+35.20%` | `10X Cross` |
| `753` | `0xecb6...2b00` | `SHORT` | 2,970,532.52 USD | `24,891.34` | `133.17` | `120.07` | `1282.66` | 344,311.67 USD | `+11.59%` | `10X Cross` |
| `812` | `0x0514...bdfe` | `SHORT` | 2,740,680.00 USD | `23,000.00` | `87.41` | `120.07` | `155.68` | -730,200.78 USD | `-26.64%` | `10X Cross` |
| `851` | `0x08c1...1135` | `LONG` | 2,607,676.62 USD | `21,836.18` | `80.89` | `120.07` | `83.55` | 841,342.26 USD | `+32.26%` | `10X Cross` |
| `1057` | `0x0996...0ba6` | `SHORT` | 2,025,210.00 USD | `17,000.00` | `107.97` | `120.07` | `196.58` | -189,636.70 USD | `-9.36%` | `3X Cross` |
| `1152` | `0x45d2...4029` | `SHORT` | 1,872,655.65 USD | `15,721.00` | `118.40` | `120.07` | `2958.40` | -11,264.47 USD | `-0.60%` | `10X Cross` |
| `1161` | `0xbfc7...80b4` | `SHORT` | 1,858,040.71 USD | `15,561.48` | `115.30` | `120.07` | `258.46` | -63,741.39 USD | `-3.43%` | `10X Cross` |
| `1171` | `0x6540...f7b7` | `LONG` | 1,839,248.38 USD | `15,439.21` | `144.40` | `120.07` | `76.38` | -390,112.17 USD | `-21.21%` | `5X Isolated` |
| `1230` | `0x07fd...689d` | `LONG` | 1,763,277.83 USD | `14,772.77` | `148.42` | `120.07` | `0.000000` | -429,315.75 USD | `-24.35%` | `10X Cross` |
| `1474` | `0xcac1...26b3` | `SHORT` | 1,431,480.00 USD | `12,000.00` | `125.37` | `120.07` | `870.85` | 72,960.86 USD | `+5.10%` | `10X Cross` |
| `1480` | `0x12d2...f97f` | `LONG` | 1,427,474.67 USD | `11,961.41` | `133.88` | `120.07` | `11.70` | -173,929.77 USD | `-12.18%` | `10X Cross` |
| `1494` | `0xeadc...9d55` | `LONG` | 1,412,012.53 USD | `11,823.92` | `89.93` | `120.07` | `0.000000` | 348,656.11 USD | `+24.69%` | `10X Cross` |
| `1652` | `0x9df2...c665` | `SHORT` | 1,238,769.49 USD | `10,380.17` | `133.78` | `120.07` | `3222.21` | 149,939.79 USD | `+12.10%` | `10X Cross` |
| `1699` | `0x3dc9...54b0` | `SHORT` | 1,194,200.00 USD | `10,000.00` | `128.60` | `120.07` | `1972.63` | 91,821.83 USD | `+7.69%` | `10X Cross` |
| `1821` | `0x8af7...fa05` | `SHORT` | 1,087,098.93 USD | `9,133.75` | `131.49` | `120.07` | `2215.20` | 113,881.82 USD | `+10.48%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`126.67` (Vol: 411,400.00 USD, Dist: `+5.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`126.73` (Vol: 504,200.00 USD, Dist: `+5.06%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`122.59` (Vol: 457,200.00 USD, Dist: `+1.63%`) | Long MP=`117.89` (Vol: 457,200.00 USD, Dist: `--2.27%`)
  * 7D Horizon: Short MP=`126.74` (Vol: 504,200.00 USD, Dist: `+5.07%`) | Long MP=`117.98` (Vol: 457,200.00 USD, Dist: `--2.19%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `24.50` | 10,840.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 5,220.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 1,340.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 28,240.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 283.86 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 2,170.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 15,250.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 639.13 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 901.48 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 1,560.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 723.13 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 24,590.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 307.80 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 611.71 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 528.96 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 5,800.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 1,220.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 181.90 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 62,440.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,830.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 7,860.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 323.75 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 797.56 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 4,790.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 314.40 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 1,380.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,530.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 1,010.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,620.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 836.84 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 20,690.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 471.25 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 13,560.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,330.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 156.06 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 10,890.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 7,710.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 48,060.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,810,000.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 2,920.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 16,900.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 45,290.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 4,860.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,370,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 3,750.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 4,470.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 12,350.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 12,070.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 77,160.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 66,790.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 93,240.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 4,320,000.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 2,640.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 77,440.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 2,180.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,220.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 22,970.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 1,380.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 28,420.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 5,440.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 113,190.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 5,570.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 14,330.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 653,580.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 15,530.00 USD | 630,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 2,560.00 USD | 614,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 40,710.00 USD | 612,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 20,180.00 USD | 571,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 27,900.00 USD | 551,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 61,640.00 USD | 523,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 414,710.00 USD | 461,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 19,120.00 USD | 47,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 27,960.00 USD | 27,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 12,490.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 190.75 USD | 12,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 2,610.00 USD | 15,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 5,330.00 USD | 20,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 2,770.00 USD | 23,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 6,490.00 USD | 29,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 7,130.00 USD | 37,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 185.04 USD | 37,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 62,340.00 USD | 99,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 92,320.00 USD | 191,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 43,880.00 USD | 235,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 4,140.00 USD | 239,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 31,160.00 USD | 271,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 26,350.00 USD | 297,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 613.82 USD | 298,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 1,180.00 USD | 299,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 998.59 USD | 300,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 300,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 60,070.00 USD | 360,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 19,640.00 USD | 379,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 142.50 USD | 380,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 380,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 84,040.00 USD | 464,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 2,540.00 USD | 467,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 467,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 373,730.00 USD | 841,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 594,420.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 41,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 6,920.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 1,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 674.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 256.51 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 54,150.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 242,130.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 964.60 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 4,340,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 34,580.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 11,800.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 16,810.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 407,370.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `204.50` | 41,890.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 1,070.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 5,840.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `213.50` | 57,590.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `215.50` | 15,520.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 26,220.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,250.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 9,200.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 1,130.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 820,600.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 70,540.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 4,770.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 261.06 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `24.50` | 9,260,000.00 USD | 0.00 USD | 24,500.00 USD | `-79.36%` | `1,000.00` |
| `Live` | `Long` | `25.50` | 9,240,000.00 USD | 0.00 USD | 23,650.00 USD | `-78.52%` | `927.45` |
| `Live` | `Long` | `26.50` | 9,210,000.00 USD | 0.00 USD | 360.40 USD | `-77.67%` | `13.60` |
| `Live` | `Long` | `28.50` | 9,210,000.00 USD | 0.00 USD | 15,090.00 USD | `-75.99%` | `529.38` |
| `Live` | `Long` | `29.50` | 9,200,000.00 USD | 0.00 USD | 293.82 USD | `-75.15%` | `9.96` |
| `Live` | `Long` | `30.50` | 9,200,000.00 USD | 0.00 USD | 3,970.00 USD | `-74.30%` | `130.23` |
| `Live` | `Long` | `31.50` | 9,200,000.00 USD | 0.00 USD | 6,860.00 USD | `-73.46%` | `217.76` |
| `Live` | `Long` | `35.50` | 9,190,000.00 USD | 0.00 USD | 58,390.00 USD | `-70.09%` | `1,644.72` |
| `Live` | `Long` | `37.50` | 9,130,000.00 USD | 0.00 USD | 495.00 USD | `-68.41%` | `13.20` |
| `Live` | `Long` | `38.50` | 9,130,000.00 USD | 0.00 USD | 1,450.00 USD | `-67.57%` | `37.73` |
| `Live` | `Long` | `40.50` | 9,130,000.00 USD | 0.00 USD | 405.00 USD | `-65.88%` | `10.00` |
| `Live` | `Long` | `43.50` | 9,130,000.00 USD | 0.00 USD | 667.73 USD | `-63.35%` | `15.35` |
| `Live` | `Long` | `45.50` | 9,130,000.00 USD | 0.00 USD | 37,130.00 USD | `-61.67%` | `816.08` |
| `Live` | `Long` | `46.50` | 9,090,000.00 USD | 0.00 USD | 4,450.00 USD | `-60.83%` | `95.76` |
| `Live` | `Long` | `49.50` | 9,090,000.00 USD | 0.00 USD | 158.40 USD | `-58.30%` | `3.20` |
| `Live` | `Long` | `50.50` | 9,090,000.00 USD | 0.00 USD | 168.67 USD | `-57.46%` | `3.34` |
| `Live` | `Long` | `51.50` | 9,080,000.00 USD | 0.00 USD | 835.85 USD | `-56.61%` | `16.23` |
| `Live` | `Long` | `52.50` | 9,080,000.00 USD | 0.00 USD | 7,570.00 USD | `-55.77%` | `144.17` |
| `Live` | `Long` | `53.50` | 9,080,000.00 USD | 0.00 USD | 1,110.00 USD | `-54.93%` | `20.71` |
| `Live` | `Long` | `54.50` | 9,080,000.00 USD | 0.00 USD | 1,610.00 USD | `-54.09%` | `29.52` |
| `Live` | `Long` | `56.50` | 9,070,000.00 USD | 0.00 USD | 1,510.00 USD | `-52.40%` | `26.66` |
| `Live` | `Long` | `58.50` | 9,070,000.00 USD | 0.00 USD | 2,950.00 USD | `-50.72%` | `50.50` |
| `Live` | `Long` | `60.50` | 9,070,000.00 USD | 0.00 USD | 1,690.00 USD | `-49.03%` | `27.87` |
| `Live` | `Long` | `61.50` | 9,070,000.00 USD | 0.00 USD | 273.68 USD | `-48.19%` | `4.45` |
| `Live` | `Long` | `62.50` | 9,070,000.00 USD | 0.00 USD | 918.75 USD | `-47.35%` | `14.70` |
| `Live` | `Long` | `63.50` | 9,070,000.00 USD | 0.00 USD | 3,560.00 USD | `-46.50%` | `56.00` |
| `Live` | `Long` | `64.50` | 9,060,000.00 USD | 0.00 USD | 219.30 USD | `-45.66%` | `3.40` |
| `Live` | `Long` | `65.50` | 9,060,000.00 USD | 0.00 USD | 434.27 USD | `-44.82%` | `6.63` |
| `Live` | `Long` | `66.50` | 9,060,000.00 USD | 0.00 USD | 137,950.00 USD | `-43.98%` | `2,074.45` |
| `Live` | `Long` | `67.50` | 8,920,000.00 USD | 0.00 USD | 24,570.00 USD | `-43.13%` | `364.07` |
| `Live` | `Long` | `68.50` | 8,900,000.00 USD | 0.00 USD | 2,230.00 USD | `-42.29%` | `32.58` |
| `Live` | `Long` | `69.50` | 8,900,000.00 USD | 0.00 USD | 24,960.00 USD | `-41.45%` | `359.12` |
| `Live` | `Long` | `70.50` | 8,870,000.00 USD | 0.00 USD | 836.84 USD | `-40.61%` | `11.87` |
| `Live` | `Long` | `71.50` | 8,870,000.00 USD | 0.00 USD | 9,340.00 USD | `-39.76%` | `130.60` |
| `Live` | `Long` | `72.50` | 8,860,000.00 USD | 0.00 USD | 694.55 USD | `-38.92%` | `9.58` |
| `Live` | `Long` | `73.50` | 8,860,000.00 USD | 0.00 USD | 19,340.00 USD | `-38.08%` | `263.13` |
| `Live` | `Long` | `74.50` | 8,840,000.00 USD | 0.00 USD | 10,370.00 USD | `-37.24%` | `139.20` |
| `Live` | `Long` | `76.50` | 8,830,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-35.55%` | `15,522.61` |
| `Live` | `Long` | `77.50` | 7,640,000.00 USD | 0.00 USD | 9,050.00 USD | `-34.71%` | `116.79` |
| `Live` | `Long` | `78.50` | 7,640,000.00 USD | 0.00 USD | 4,310.00 USD | `-33.87%` | `54.87` |
| `Live` | `Long` | `79.50` | 7,630,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-33.02%` | `22,032.59` |
| `Live` | `Long` | `80.50` | 5,880,000.00 USD | 0.00 USD | 8,340.00 USD | `-32.18%` | `103.62` |
| `Live` | `Long` | `81.50` | 5,870,000.00 USD | 0.00 USD | 3,900.00 USD | `-31.34%` | `47.91` |
| `Live` | `Long` | `83.50` | 5,870,000.00 USD | 0.00 USD | 3,390.00 USD | `-29.65%` | `40.59` |
| `Live` | `Long` | `85.50` | 5,860,000.00 USD | 0.00 USD | 44,800.00 USD | `-27.97%` | `524.00` |
| `Live` | `Long` | `86.50` | 5,820,000.00 USD | 0.00 USD | 3,210.00 USD | `-27.13%` | `37.14` |
| `Live` | `Long` | `87.50` | 5,820,000.00 USD | 0.00 USD | 24,480.00 USD | `-26.28%` | `279.76` |
| `Live` | `Long` | `88.50` | 5,790,000.00 USD | 0.00 USD | 2,050.00 USD | `-25.44%` | `23.18` |
| `Live` | `Long` | `89.50` | 5,790,000.00 USD | 0.00 USD | 15,140.00 USD | `-24.60%` | `169.16` |
| `Live` | `Long` | `90.50` | 5,770,000.00 USD | 0.00 USD | 6,910.00 USD | `-23.76%` | `76.33` |
| `Live` | `Long` | `91.50` | 5,770,000.00 USD | 0.00 USD | 286,910.00 USD | `-22.91%` | `3,135.68` |
| `Live` | `Long` | `92.50` | 5,480,000.00 USD | 0.00 USD | 15,320.00 USD | `-22.07%` | `165.65` |
| `Live` | `Long` | `93.50` | 5,460,000.00 USD | 0.00 USD | 17,450.00 USD | `-21.23%` | `186.59` |
| `Live` | `Long` | `94.50` | 5,450,000.00 USD | 0.00 USD | 14,320.00 USD | `-20.39%` | `151.54` |
| `Live` | `Long` | `95.50` | 5,430,000.00 USD | 0.00 USD | 11,900.00 USD | `-19.55%` | `124.56` |
| `Live` | `Long` | `96.50` | 5,420,000.00 USD | 0.00 USD | 7,770.00 USD | `-18.70%` | `80.47` |
| `Live` | `Long` | `97.50` | 5,410,000.00 USD | 0.00 USD | 155,100.00 USD | `-17.86%` | `1,590.82` |
| `Live` | `Long` | `98.50` | 5,260,000.00 USD | 0.00 USD | 41,330.00 USD | `-17.02%` | `419.64` |
| `Live` | `Long` | `99.50` | 5,220,000.00 USD | 0.00 USD | 946.25 USD | `-16.18%` | `9.51` |
| `Live` | `Long` | `100.50` | 5,220,000.00 USD | 0.00 USD | 4,360,000.00 USD | `-15.33%` | `43,347.05` |
| `Live` | `Long` | `101.50` | 859,790.00 USD | 0.00 USD | 32,170.00 USD | `-14.49%` | `316.97` |
| `Live` | `Long` | `102.50` | 827,620.00 USD | 0.00 USD | 17,370.00 USD | `-13.65%` | `169.44` |
| `Live` | `Long` | `103.50` | 810,250.00 USD | 0.00 USD | 8,860.00 USD | `-12.81%` | `85.59` |
| `Live` | `Long` | `104.50` | 801,390.00 USD | 0.00 USD | 11,110.00 USD | `-11.96%` | `106.30` |
| `Live` | `Long` | `105.50` | 790,280.00 USD | 0.00 USD | 66,450.00 USD | `-11.12%` | `629.90` |
| `Live` | `Long` | `106.50` | 723,830.00 USD | 0.00 USD | 4,430.00 USD | `-10.28%` | `41.56` |
| `Live` | `Long` | `107.50` | 719,400.00 USD | 0.00 USD | 109,980.00 USD | `-9.44%` | `1,023.06` |
| `Live` | `Long` | `108.50` | 609,420.00 USD | 0.00 USD | 87,280.00 USD | `-8.59%` | `804.38` |
| `Live` | `Long` | `109.50` | 522,150.00 USD | 0.00 USD | 2,400.00 USD | `-7.75%` | `21.88` |
| `Live` | `Long` | `110.50` | 519,750.00 USD | 0.00 USD | 433,780.00 USD | `-6.91%` | `3,925.60` |
| `Live` | `Long` | `111.50` | 85,980.00 USD | 0.00 USD | 17,790.00 USD | `-6.07%` | `159.59` |
| `Live` | `Long` | `112.50` | 68,180.00 USD | 0.00 USD | 2,310.00 USD | `-5.22%` | `20.49` |
| `Live` | `Long` | `113.50` | 65,880.00 USD | 0.00 USD | 51,620.00 USD | `-4.38%` | `454.78` |
| `Live` | `Long` | `114.50` | 14,260.00 USD | 0.00 USD | 11,160.00 USD | `-3.54%` | `97.43` |
| `Live` | `Long` | `115.50` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | `-2.70%` | `26.86` |
| `Live` | `Short` | `121.50` | 24,390.00 USD | 24,390.00 USD | 0.00 USD | `+2.36%` | `200.78` |
| `Live` | `Short` | `123.50` | 25,960.00 USD | 1,570.00 USD | 0.00 USD | `+4.04%` | `12.70` |
| `Live` | `Short` | `124.50` | 38,850.00 USD | 12,890.00 USD | 0.00 USD | `+4.89%` | `103.51` |
| `Live` | `Short` | `125.50` | 227,630.00 USD | 188,780.00 USD | 0.00 USD | `+5.73%` | `1,504.22` |
| `Live` | `Short` | `126.50` | 229,380.00 USD | 1,750.00 USD | 0.00 USD | `+6.57%` | `13.86` |
| `Live` | `Short` | `127.50` | 229,550.00 USD | 161.93 USD | 0.00 USD | `+7.41%` | `1.27` |
| `Live` | `Short` | `129.50` | 233,270.00 USD | 3,720.00 USD | 0.00 USD | `+9.10%` | `28.74` |
| `Live` | `Short` | `130.50` | 249,060.00 USD | 15,800.00 USD | 0.00 USD | `+9.94%` | `121.04` |
| `Live` | `Short` | `136.50` | 254,210.00 USD | 5,150.00 USD | 0.00 USD | `+15.00%` | `37.71` |
| `Live` | `Short` | `137.50` | 335,110.00 USD | 80,900.00 USD | 0.00 USD | `+15.84%` | `588.34` |
| `Live` | `Short` | `138.50` | 336,110.00 USD | 998.59 USD | 0.00 USD | `+16.68%` | `7.21` |
| `Live` | `Short` | `139.50` | 347,730.00 USD | 11,630.00 USD | 0.00 USD | `+17.52%` | `83.36` |
| `Live` | `Short` | `140.50` | 349,020.00 USD | 1,280.00 USD | 0.00 USD | `+18.37%` | `9.13` |
| `Live` | `Short` | `141.50` | 349,530.00 USD | 517.89 USD | 0.00 USD | `+19.21%` | `3.66` |
| `Live` | `Short` | `142.50` | 360,650.00 USD | 11,120.00 USD | 0.00 USD | `+20.05%` | `78.02` |
| `Live` | `Short` | `145.50` | 928,520.00 USD | 567,860.00 USD | 0.00 USD | `+22.58%` | `3,902.85` |
| `Live` | `Short` | `150.50` | 928,680.00 USD | 167.06 USD | 0.00 USD | `+26.79%` | `1.11` |
| `Live` | `Short` | `151.50` | 956,580.00 USD | 27,900.00 USD | 0.00 USD | `+27.63%` | `184.14` |
| `Live` | `Short` | `153.50` | 959,190.00 USD | 2,610.00 USD | 0.00 USD | `+29.32%` | `16.98` |
| `Live` | `Short` | `154.50` | 959,420.00 USD | 227.12 USD | 0.00 USD | `+30.16%` | `1.47` |
| `Live` | `Short` | `155.50` | 961,610.00 USD | 2,200.00 USD | 0.00 USD | `+31.00%` | `14.13` |
| `Live` | `Short` | `158.50` | 963,100.00 USD | 1,480.00 USD | 0.00 USD | `+33.53%` | `9.36` |
| `Live` | `Short` | `160.50` | 964,700.00 USD | 1,600.00 USD | 0.00 USD | `+35.21%` | `10.00` |
| `Live` | `Short` | `164.50` | 966,640.00 USD | 1,940.00 USD | 0.00 USD | `+38.58%` | `11.81` |
| `Live` | `Short` | `166.50` | 4,850,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+40.27%` | `23,300.00` |
| `Live` | `Short` | `169.50` | 5,140,000.00 USD | 296,280.00 USD | 0.00 USD | `+42.80%` | `1,747.94` |
| `Live` | `Short` | `170.50` | 5,140,000.00 USD | 168.79 USD | 0.00 USD | `+43.64%` | `0.99` |
| `Live` | `Short` | `174.50` | 5,140,000.00 USD | 1,570.00 USD | 0.00 USD | `+47.01%` | `9.00` |
| `Live` | `Short` | `175.50` | 5,150,000.00 USD | 5,620.00 USD | 0.00 USD | `+47.85%` | `32.04` |
| `Live` | `Short` | `177.50` | 5,190,000.00 USD | 36,360.00 USD | 0.00 USD | `+49.54%` | `204.83` |
| `Live` | `Short` | `178.50` | 5,310,000.00 USD | 121,140.00 USD | 0.00 USD | `+50.38%` | `678.65` |
| `Live` | `Short` | `179.50` | 5,310,000.00 USD | 1,110.00 USD | 0.00 USD | `+51.22%` | `6.20` |
| `Live` | `Short` | `181.50` | 5,310,000.00 USD | 2,380.00 USD | 0.00 USD | `+52.91%` | `13.10` |
| `Live` | `Short` | `183.50` | 5,310,000.00 USD | 141.30 USD | 0.00 USD | `+54.59%` | `0.77` |
| `Live` | `Short` | `187.50` | 5,320,000.00 USD | 4,230.00 USD | 0.00 USD | `+57.96%` | `22.56` |
| `Live` | `Short` | `189.50` | 5,320,000.00 USD | 295.62 USD | 0.00 USD | `+59.65%` | `1.56` |
| `Live` | `Short` | `190.50` | 6,190,000.00 USD | 874,760.00 USD | 0.00 USD | `+60.49%` | `4,591.90` |
| `Live` | `Short` | `192.50` | 6,190,000.00 USD | 358.05 USD | 0.00 USD | `+62.17%` | `1.86` |
| `Live` | `Short` | `194.50` | 6,230,000.00 USD | 34,760.00 USD | 0.00 USD | `+63.86%` | `178.70` |
| `Live` | `Short` | `196.50` | 9,570,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+65.54%` | `17,007.57` |
| `Live` | `Short` | `197.50` | 9,570,000.00 USD | 2,040.00 USD | 0.00 USD | `+66.39%` | `10.33` |
| `Live` | `Short` | `200.50` | 9,580,000.00 USD | 9,850.00 USD | 0.00 USD | `+68.91%` | `49.15` |
| `Live` | `Short` | `203.50` | 9,580,000.00 USD | 372.41 USD | 0.00 USD | `+71.44%` | `1.83` |
| `Live` | `Short` | `205.50` | 9,660,000.00 USD | 84,610.00 USD | 0.00 USD | `+73.13%` | `411.72` |
| `Live` | `Short` | `206.50` | 9,680,000.00 USD | 17,610.00 USD | 0.00 USD | `+73.97%` | `85.28` |
| `Live` | `Short` | `210.50` | 9,680,000.00 USD | 151.56 USD | 0.00 USD | `+77.34%` | `0.72` |
| `Live` | `Short` | `212.50` | 9,690,000.00 USD | 5,740.00 USD | 0.00 USD | `+79.02%` | `27.00` |
| `Live` | `Short` | `214.50` | 9,690,000.00 USD | 148.00 USD | 0.00 USD | `+80.71%` | `0.69` |
| `Live` | `Short` | `218.50` | 9,700,000.00 USD | 15,730.00 USD | 0.00 USD | `+84.08%` | `72.00` |
| `Live` | `Short` | `219.50` | 9,730,000.00 USD | 27,070.00 USD | 0.00 USD | `+84.92%` | `123.34` |
| `Live` | `Short` | `220.50` | 9,730,000.00 USD | 2,000.00 USD | 0.00 USD | `+85.76%` | `9.06` |
| `Live` | `Short` | `222.50` | 9,730,000.00 USD | 117.93 USD | 0.00 USD | `+87.45%` | `0.53` |
| `Live` | `Short` | `226.50` | 9,730,000.00 USD | 262.74 USD | 0.00 USD | `+90.82%` | `1.16` |
| `Live` | `Short` | `227.50` | 9,740,000.00 USD | 9,330.00 USD | 0.00 USD | `+91.66%` | `41.00` |
| `Live` | `Short` | `232.50` | 10,560,000.00 USD | 818,270.00 USD | 0.00 USD | `+95.87%` | `3,519.45` |
| `Live` | `Short` | `233.50` | 10,560,000.00 USD | 2,590.00 USD | 0.00 USD | `+96.71%` | `11.09` |
| `Live` | `Short` | `234.50` | 10,630,000.00 USD | 63,440.00 USD | 0.00 USD | `+97.56%` | `270.55` |

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
  * Current Rate: `-7.42K` | Last 24h: `15.98K` | Last 3d: `56.03K` | Last 7d: `119.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0091%` | **USDT OKX** | `0.0063%` |
| **USDT Bybit** | `-0.0279%` | **USDT KuCoin** | `0.0012%` |
| **USDT MEXC** | `0.0088%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0071%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0091%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `120.70` | `120.78` | `120.70` | `121.41` | `120.30` | 5,029,340.94 USD | 3,109,868.09 USD | 1,919,472.85 USD | 1,190,395.24 USD | `+23.67%` | `19B / 2S` |
| `5:00 UTC` | `120.00` | `120.01` | `120.00` | `120.94` | `119.12` | 4,156,390.88 USD | 1,952,531.59 USD | 2,203,859.29 USD | -251,327.70 USD | `-6.05%` | `15B / 40S` |
| `0:00 UTC` | `119.66` | `119.27` | `119.66` | `119.97` | `118.60` | 4,404,214.29 USD | 2,484,500.94 USD | 1,919,713.35 USD | 564,787.59 USD | `+12.82%` | `14B / 7S` |
| `5:00 UTC` | `117.22` | `116.97` | `117.22` | `120.02` | `115.02` | 9,861,640.78 USD | 3,876,505.89 USD | 5,985,134.89 USD | -2,108,629.00 USD | `-21.38%` | `2B / 29S` |
| `0:00 UTC` | `117.74` | `117.24` | `117.74` | `118.42` | `115.96` | 3,865,835.63 USD | 1,961,740.56 USD | 1,904,095.08 USD | 57,645.48 USD | `+1.49%` | `20B / 16S` |
| `5:00 UTC` | `118.95` | `118.77` | `118.95` | `119.34` | `118.05` | 3,208,757.12 USD | 1,414,154.79 USD | 1,794,602.33 USD | -380,447.54 USD | `-11.86%` | `12B / 34S` |
| `0:00 UTC` | `118.90` | `119.01` | `118.90` | `119.97` | `118.07` | 2,314,365.12 USD | 1,430,488.25 USD | 883,876.88 USD | 546,611.37 USD | `+23.62%` | `42B / 21S` |
| `5:00 UTC` | `118.70` | `118.80` | `118.70` | `119.53` | `118.31` | 2,154,963.00 USD | 1,005,187.45 USD | 1,149,775.55 USD | -144,588.09 USD | `-6.71%` | `17B / 19S` |
| `0:00 UTC` | `119.81` | `119.19` | `119.81` | `120.27` | `117.51` | 3,059,962.26 USD | 1,668,626.89 USD | 1,391,335.36 USD | 277,291.53 USD | `+9.06%` | `20B / 9S` |
| `5:00 UTC` | `118.97` | `119.17` | `118.97` | `119.84` | `118.78` | 664,334.86 USD | 294,321.29 USD | 370,013.57 USD | -75,692.28 USD | `-11.39%` | `13B / 21S` |

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
| `5m` | 15,270.00 USD | 315,060.00 USD | **`ACCUMULATION`** |
| `15m` | -234,580.00 USD | 240,020.00 USD | **`ACCUMULATION`** |
| `30m` | -654,000.00 USD | 795,310.00 USD | **`ACCUMULATION`** |
| `1h` | -972,710.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,330,000.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,860,000.00 USD | -7,090,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,780,000.00 USD | -12,510,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,600,000.00 USD | -12,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,710,000.00 USD | -13,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,590,000.00 USD | -12,770,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -29,710,000.00 USD | -52,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -117,020,000.00 USD | -102,680,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+15.27K` | 15m=`-234.58K` | 1h=`-972.71K` | 24h=`-7.59M`
* Futures Capital Netflows: 5m=`+315.06K` | 15m=`+240.02K` | 1h=`+1.47M` | 24h=`-12.77M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `114.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `111.74` (Risk Distance: `2.99` pts)
  * +2.5R Take Profit: `122.19`
  * Mathematical Lot Sizing: **`3.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `122.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `125.78` (Risk Distance: `2.99` pts)
  * +2.5R Take Profit: `115.33`
  * Mathematical Lot Sizing: **`3.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`119.95`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
