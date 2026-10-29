# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `134.66` | **Live Ask Quote**: `134.96` | **Mid Price**: `134.81`
- **Spread Points**: `30.00` | **Spread BPS**: `22.25 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `132.21` | VWAP Z-Score: `+1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.08` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.52` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `139.04` | Lower -3.00σ Band: `125.38`
  * Upper +2.51σ Band: `137.93` | Lower -2.51σ Band: `126.49`
  * Upper +2.01σ Band: `136.79` | Lower -2.01σ Band: `127.63`
  * Upper +2.00σ Band: `136.77` | Lower -2.00σ Band: `127.66`
  * Upper +1.28σ Band: `135.13` | Lower -1.28σ Band: `129.30`
  * Upper +1.00σ Band: `134.49` | Lower -1.00σ Band: `129.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`135.56` | EMA-20=`134.54` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`133.14` (Slope: `+0.0000`) | EMA-100=`132.75`
  * Institutional Anchors: EMA-144=`132.76` | EMA-200=`132.76` (Slope: `+0.2507`) | EMA-233=`132.76`
- **Range Boundaries**: 24H High=`138.47` | 24H Low=`128.25` | Weekly High=`138.47` | Weekly Low=`128.25`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `136.70` (Distance: `-1.26%`)
  * Point of Control (POC) = `132.93` (Distance: `+1.54%`)
  * Value Area Low (VAL) = `130.61` (Distance: `+3.34%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`135.85` | POC=`134.70` | VAL=`132.04`
  * Prior Day Extremes: PDH=`138.47` | PDL=`129.42` | PDC=`134.07`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.19` | Weekly POC=`134.76` | Weekly VAL=`131.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`135.37` | Low=`128.25`
  * London Session (08:00-16:00 UTC): High=`133.60` | Low=`129.16`
  * New York Session (13:00-21:00 UTC): High=`137.67` | Low=`130.09`
  * Initial Balance (First Hour): IB High=`131.85` | IB Low=`129.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `134.27` - `135.35`
  * Optimal Trade Entry (OTE 0.705): `135.08`
  * Structural Invalidation Anchor (0.786): `135.89`

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
| --- | **`134.81`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `413` | `0x3ee5...4fab` | `LONG` | 5,855,976.93 USD | `43,303.83` | `77.35` | `134.89` | `113.52` | 2,506,286.89 USD | `+42.80%` | `10X Cross` |
| `766` | `0x0514...bdfe` | `SHORT` | 3,110,750.00 USD | `23,000.00` | `87.41` | `134.89` | `182.07` | -1,100,270.78 USD | `-35.37%` | `10X Cross` |
| `810` | `0x08c1...1135` | `LONG` | 2,950,723.00 USD | `21,836.18` | `80.89` | `134.89` | `94.97` | 1,184,388.65 USD | `+40.14%` | `10X Cross` |
| `1010` | `0x0996...0ba6` | `SHORT` | 2,294,320.00 USD | `17,000.00` | `107.97` | `134.89` | `196.59` | -458,746.70 USD | `-19.99%` | `3X Cross` |
| `1073` | `0x45d2...4029` | `SHORT` | 2,122,976.42 USD | `15,721.00` | `118.40` | `134.89` | `2243.87` | -261,585.24 USD | `-12.32%` | `10X Cross` |
| `1086` | `0xbfc7...80b4` | `SHORT` | 2,102,822.79 USD | `15,561.48` | `115.30` | `134.89` | `397.53` | -308,523.47 USD | `-14.67%` | `10X Cross` |
| `1179` | `0x6540...f7b7` | `LONG` | 1,972,170.48 USD | `14,613.00` | `145.70` | `134.89` | `91.04` | -157,012.66 USD | `-7.96%` | `5X Isolated` |
| `1286` | `0x07fd...689d` | `LONG` | 1,820,644.14 USD | `13,490.25` | `150.69` | `134.89` | `0.000000` | -212,254.86 USD | `-11.66%` | `10X Cross` |
| `1435` | `0xcac1...26b3` | `SHORT` | 1,619,520.00 USD | `12,000.00` | `125.37` | `134.89` | `754.40` | -115,079.14 USD | `-7.11%` | `10X Cross` |
| `1449` | `0xeadc...9d55` | `LONG` | 1,600,958.77 USD | `11,823.92` | `89.93` | `134.89` | `0.000000` | 537,602.36 USD | `+33.58%` | `10X Cross` |
| `1597` | `0x9df2...c665` | `SHORT` | 1,421,193.40 USD | `10,532.82` | `133.81` | `134.89` | `2748.41` | -11,743.76 USD | `-0.83%` | `10X Cross` |
| `1646` | `0x3dc9...54b0` | `SHORT` | 1,357,000.00 USD | `10,000.00` | `128.60` | `134.89` | `1424.27` | -70,978.17 USD | `-5.23%` | `10X Cross` |
| `1764` | `0x8af7...fa05` | `SHORT` | 1,232,690.90 USD | `9,133.75` | `131.49` | `134.89` | `2200.89` | -31,710.15 USD | `-2.57%` | `10X Cross` |
| `1947` | `0x72db...8bb6` | `LONG` | 1,080,080.00 USD | `8,000.00` | `180.99` | `134.89` | `0.000000` | -367,877.43 USD | `-34.06%` | `10X Cross` |
| `2007` | `0x12d2...f97f` | `LONG` | 1,035,928.67 USD | `7,675.82` | `143.31` | `134.89` | `0.000000` | -64,064.06 USD | `-6.18%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 48H Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 3D Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 7D Horizon: Short MP=`139.76` (Vol: 320,000.00 USD, Dist: `+4.58%`) | Long MP=`127.18` (Vol: 326,000.00 USD, Dist: `--4.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `27.50` | 312.67 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 694.55 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 2,730.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 1,890.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 717.25 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 424.22 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 573.38 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 285.80 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 3,280.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 6,610.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 1,220.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,700.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 3,270.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 10,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 21,670.00 USD | 10,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 130,820.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 323.75 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 3,860.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 2,350.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 2,010.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,510.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 202.34 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 13,210.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,820.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,800.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,050.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 7,090.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 8,120.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 5,740.00 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 134.47 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 543.59 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 45,160.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 118,990.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,380.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 26,420.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 4,520.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 652.50 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 1,620,000.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 12,350.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 9,240.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,760.00 USD | 8,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 2,100,000.00 USD | 8,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,350.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 90,910.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 237,840.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 946.25 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 3,360.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 3,700.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,850.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 4,750.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 2,700.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 33,790.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 14,600.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 40,630.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 11,720.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 16,210.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 606,920.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 1,610.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 13,180.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 5,010,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 13,780.00 USD | 479,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 13,100.00 USD | 465,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 60,290.00 USD | 452,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 146,940.00 USD | 392,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 11,320.00 USD | 245,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 2,320.00 USD | 234,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 17,860.00 USD | 231,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 7,060.00 USD | 214,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 21,960.00 USD | 207,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 26,880.00 USD | 185,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 26,980.00 USD | 158,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 17,240.00 USD | 131,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 67,930.00 USD | 113,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `127.50` | 4,260.00 USD | 46,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 23,630.00 USD | 41,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `129.50` | 16,300.00 USD | 18,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 1,860.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 2,420.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,930.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 5,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 6,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 22,650.00 USD | 29,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 1,820.00 USD | 31,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 31,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 88,250.00 USD | 120,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 2,060.00 USD | 122,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 595,110.00 USD | 717,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 877.56 USD | 718,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 4,650.00 USD | 722,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 229.95 USD | 722,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,820.00 USD | 724,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 337.99 USD | 725,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 726,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 727,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 30,430.00 USD | 758,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 252.34 USD | 758,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 784.88 USD | 759,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 870.97 USD | 760,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 765,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 26,090.00 USD | 791,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 13,000.00 USD | 804,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 4,180,000.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 55,350.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 656,380.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 7,810.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 3,050.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 58,110.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 1,100.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 10,010.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 9,550.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 11,660.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 2,970.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 21,680.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 23,640.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 1,610.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `228.50` | 520.98 USD | 9,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 49,300.00 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 225.53 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 4,750.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 1,050.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 647.48 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `252.50` | 166.65 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `253.50` | 18,500.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `254.50` | 15,410.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `255.50` | 702.62 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `257.50` | 1,430.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `260.50` | 151,980.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `262.50` | 763.88 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `263.50` | 532.27 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `266.50` | 15,990.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `267.50` | 21,110.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `268.50` | 23,970.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `270.50` | 235.34 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `27.50` | 10,830,000.00 USD | 0.00 USD | 312.67 USD | `-79.75%` | `11.37` |
| `Live` | `Long` | `28.50` | 10,830,000.00 USD | 0.00 USD | 694.55 USD | `-79.01%` | `24.37` |
| `Live` | `Long` | `30.50` | 10,830,000.00 USD | 0.00 USD | 2,730.00 USD | `-77.54%` | `89.57` |
| `Live` | `Long` | `31.50` | 10,820,000.00 USD | 0.00 USD | 1,890.00 USD | `-76.80%` | `60.00` |
| `Live` | `Long` | `34.50` | 10,820,000.00 USD | 0.00 USD | 717.25 USD | `-74.59%` | `20.79` |
| `Live` | `Long` | `35.50` | 10,820,000.00 USD | 0.00 USD | 424.22 USD | `-73.86%` | `11.95` |
| `Live` | `Long` | `37.50` | 10,820,000.00 USD | 0.00 USD | 573.38 USD | `-72.38%` | `15.29` |
| `Live` | `Long` | `38.50` | 10,820,000.00 USD | 0.00 USD | 232.54 USD | `-71.65%` | `6.04` |
| `Live` | `Long` | `43.50` | 10,820,000.00 USD | 0.00 USD | 285.80 USD | `-67.97%` | `6.57` |
| `Live` | `Long` | `45.50` | 10,820,000.00 USD | 0.00 USD | 158.34 USD | `-66.49%` | `3.48` |
| `Live` | `Long` | `47.50` | 10,820,000.00 USD | 0.00 USD | 3,280.00 USD | `-65.02%` | `69.07` |
| `Live` | `Long` | `49.50` | 10,820,000.00 USD | 0.00 USD | 6,610.00 USD | `-63.55%` | `133.58` |
| `Live` | `Long` | `50.50` | 10,810,000.00 USD | 0.00 USD | 1,220.00 USD | `-62.81%` | `24.14` |
| `Live` | `Long` | `54.50` | 10,810,000.00 USD | 0.00 USD | 805.51 USD | `-59.87%` | `14.78` |
| `Live` | `Long` | `55.50` | 10,810,000.00 USD | 0.00 USD | 1,700.00 USD | `-59.13%` | `30.64` |
| `Live` | `Long` | `56.50` | 10,810,000.00 USD | 0.00 USD | 3,270.00 USD | `-58.39%` | `57.80` |
| `Live` | `Long` | `57.50` | 10,800,000.00 USD | 0.00 USD | 2,010.00 USD | `-57.66%` | `35.00` |
| `Live` | `Long` | `58.50` | 10,800,000.00 USD | 0.00 USD | 21,670.00 USD | `-56.92%` | `370.44` |
| `Live` | `Long` | `59.50` | 10,780,000.00 USD | 0.00 USD | 130,820.00 USD | `-56.18%` | `2,198.68` |
| `Live` | `Long` | `60.50` | 10,650,000.00 USD | 0.00 USD | 1,690.00 USD | `-55.45%` | `27.87` |
| `Live` | `Long` | `61.50` | 10,650,000.00 USD | 0.00 USD | 168.51 USD | `-54.71%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,650,000.00 USD | 0.00 USD | 323.75 USD | `-53.97%` | `5.18` |
| `Live` | `Long` | `63.50` | 10,650,000.00 USD | 0.00 USD | 3,860.00 USD | `-53.24%` | `60.85` |
| `Live` | `Long` | `66.50` | 10,640,000.00 USD | 0.00 USD | 2,350.00 USD | `-51.03%` | `35.29` |
| `Live` | `Long` | `67.50` | 10,640,000.00 USD | 0.00 USD | 24,320.00 USD | `-50.29%` | `360.30` |
| `Live` | `Long` | `68.50` | 10,620,000.00 USD | 0.00 USD | 2,010.00 USD | `-49.56%` | `29.33` |
| `Live` | `Long` | `69.50` | 10,610,000.00 USD | 0.00 USD | 18,510.00 USD | `-48.82%` | `266.40` |
| `Live` | `Long` | `70.50` | 10,600,000.00 USD | 0.00 USD | 202.34 USD | `-48.08%` | `2.87` |
| `Live` | `Long` | `71.50` | 10,600,000.00 USD | 0.00 USD | 13,210.00 USD | `-47.35%` | `184.76` |
| `Live` | `Long` | `73.50` | 10,580,000.00 USD | 0.00 USD | 11,820.00 USD | `-45.87%` | `160.80` |
| `Live` | `Long` | `74.50` | 10,570,000.00 USD | 0.00 USD | 1,800.00 USD | `-45.14%` | `24.13` |
| `Live` | `Long` | `75.50` | 10,570,000.00 USD | 0.00 USD | 1,050.00 USD | `-44.40%` | `13.87` |
| `Live` | `Long` | `77.50` | 10,570,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.93%` | `116.79` |
| `Live` | `Long` | `78.50` | 10,560,000.00 USD | 0.00 USD | 4,310.00 USD | `-42.19%` | `54.87` |
| `Live` | `Long` | `79.50` | 10,550,000.00 USD | 0.00 USD | 7,090.00 USD | `-41.45%` | `89.17` |
| `Live` | `Long` | `80.50` | 10,550,000.00 USD | 0.00 USD | 8,120.00 USD | `-40.72%` | `100.91` |
| `Live` | `Long` | `81.50` | 10,540,000.00 USD | 0.00 USD | 5,740.00 USD | `-39.98%` | `70.41` |
| `Live` | `Long` | `82.50` | 10,530,000.00 USD | 0.00 USD | 134.47 USD | `-39.25%` | `1.63` |
| `Live` | `Long` | `83.50` | 10,530,000.00 USD | 0.00 USD | 543.59 USD | `-38.51%` | `6.51` |
| `Live` | `Long` | `85.50` | 10,530,000.00 USD | 0.00 USD | 45,160.00 USD | `-37.04%` | `528.17` |
| `Live` | `Long` | `86.50` | 10,490,000.00 USD | 0.00 USD | 118,990.00 USD | `-36.30%` | `1,375.56` |
| `Live` | `Long` | `87.50` | 10,370,000.00 USD | 0.00 USD | 1,380.00 USD | `-35.56%` | `15.76` |
| `Live` | `Long` | `88.50` | 10,370,000.00 USD | 0.00 USD | 26,420.00 USD | `-34.83%` | `298.50` |
| `Live` | `Long` | `89.50` | 10,340,000.00 USD | 0.00 USD | 4,520.00 USD | `-34.09%` | `50.55` |
| `Live` | `Long` | `90.50` | 10,340,000.00 USD | 0.00 USD | 652.50 USD | `-33.35%` | `7.21` |
| `Live` | `Long` | `91.50` | 10,340,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-32.62%` | `17,708.50` |
| `Live` | `Long` | `92.50` | 8,720,000.00 USD | 0.00 USD | 12,350.00 USD | `-31.88%` | `133.49` |
| `Live` | `Long` | `93.50` | 8,700,000.00 USD | 0.00 USD | 9,240.00 USD | `-31.15%` | `98.84` |
| `Live` | `Long` | `94.50` | 8,690,000.00 USD | 0.00 USD | 2,760.00 USD | `-30.41%` | `29.16` |
| `Live` | `Long` | `95.50` | 8,690,000.00 USD | 0.00 USD | 2,100,000.00 USD | `-29.67%` | `21,991.58` |
| `Live` | `Long` | `96.50` | 6,590,000.00 USD | 0.00 USD | 9,350.00 USD | `-28.94%` | `96.84` |
| `Live` | `Long` | `97.50` | 6,580,000.00 USD | 0.00 USD | 90,910.00 USD | `-28.20%` | `932.39` |
| `Live` | `Long` | `98.50` | 6,490,000.00 USD | 0.00 USD | 237,840.00 USD | `-27.46%` | `2,414.66` |
| `Live` | `Long` | `99.50` | 6,250,000.00 USD | 0.00 USD | 946.25 USD | `-26.73%` | `9.51` |
| `Live` | `Long` | `100.50` | 6,250,000.00 USD | 0.00 USD | 3,360.00 USD | `-25.99%` | `33.39` |
| `Live` | `Long` | `101.50` | 6,250,000.00 USD | 0.00 USD | 3,700.00 USD | `-25.25%` | `36.42` |
| `Live` | `Long` | `102.50` | 6,240,000.00 USD | 0.00 USD | 11,850.00 USD | `-24.52%` | `115.59` |
| `Live` | `Long` | `103.50` | 6,230,000.00 USD | 0.00 USD | 4,750.00 USD | `-23.78%` | `45.85` |
| `Live` | `Long` | `104.50` | 6,230,000.00 USD | 0.00 USD | 2,700.00 USD | `-23.04%` | `25.83` |
| `Live` | `Long` | `105.50` | 6,230,000.00 USD | 0.00 USD | 33,790.00 USD | `-22.31%` | `320.26` |
| `Live` | `Long` | `106.50` | 6,190,000.00 USD | 0.00 USD | 14,600.00 USD | `-21.57%` | `137.12` |
| `Live` | `Long` | `107.50` | 6,180,000.00 USD | 0.00 USD | 40,630.00 USD | `-20.84%` | `377.94` |
| `Live` | `Long` | `108.50` | 6,140,000.00 USD | 0.00 USD | 11,720.00 USD | `-20.10%` | `108.02` |
| `Live` | `Long` | `109.50` | 6,120,000.00 USD | 0.00 USD | 16,210.00 USD | `-19.36%` | `148.06` |
| `Live` | `Long` | `110.50` | 6,110,000.00 USD | 0.00 USD | 606,920.00 USD | `-18.63%` | `5,492.51` |
| `Live` | `Long` | `111.50` | 5,500,000.00 USD | 0.00 USD | 1,610.00 USD | `-17.89%` | `14.46` |
| `Live` | `Long` | `112.50` | 5,500,000.00 USD | 0.00 USD | 13,180.00 USD | `-17.15%` | `117.18` |
| `Live` | `Long` | `113.50` | 5,490,000.00 USD | 0.00 USD | 5,010,000.00 USD | `-16.42%` | `44,112.21` |
| `Live` | `Long` | `114.50` | 479,680.00 USD | 0.00 USD | 13,780.00 USD | `-15.68%` | `120.31` |
| `Live` | `Long` | `115.50` | 465,910.00 USD | 0.00 USD | 13,100.00 USD | `-14.94%` | `113.39` |
| `Live` | `Long` | `116.50` | 452,810.00 USD | 0.00 USD | 60,290.00 USD | `-14.21%` | `517.51` |
| `Live` | `Long` | `117.50` | 392,520.00 USD | 0.00 USD | 146,940.00 USD | `-13.47%` | `1,250.53` |
| `Live` | `Long` | `118.50` | 245,580.00 USD | 0.00 USD | 11,320.00 USD | `-12.73%` | `95.51` |
| `Live` | `Long` | `119.50` | 234,270.00 USD | 0.00 USD | 2,320.00 USD | `-12.00%` | `19.38` |
| `Live` | `Long` | `120.50` | 231,950.00 USD | 0.00 USD | 17,860.00 USD | `-11.26%` | `148.18` |
| `Live` | `Long` | `121.50` | 214,090.00 USD | 0.00 USD | 7,060.00 USD | `-10.53%` | `58.13` |
| `Live` | `Long` | `122.50` | 207,030.00 USD | 0.00 USD | 21,960.00 USD | `-9.79%` | `179.23` |
| `Live` | `Long` | `123.50` | 185,080.00 USD | 0.00 USD | 26,880.00 USD | `-9.05%` | `217.63` |
| `Live` | `Long` | `124.50` | 158,200.00 USD | 0.00 USD | 26,980.00 USD | `-8.32%` | `216.72` |
| `Live` | `Long` | `125.50` | 131,220.00 USD | 0.00 USD | 17,240.00 USD | `-7.58%` | `137.40` |
| `Live` | `Long` | `126.50` | 113,970.00 USD | 0.00 USD | 67,930.00 USD | `-6.84%` | `536.97` |
| `Live` | `Long` | `127.50` | 46,050.00 USD | 0.00 USD | 4,260.00 USD | `-6.11%` | `33.43` |
| `Live` | `Long` | `128.50` | 41,780.00 USD | 0.00 USD | 23,630.00 USD | `-5.37%` | `183.90` |
| `Live` | `Long` | `129.50` | 18,150.00 USD | 0.00 USD | 16,300.00 USD | `-4.63%` | `125.85` |
| `Live` | `Long` | `130.50` | 1,860.00 USD | 0.00 USD | 1,860.00 USD | `-3.90%` | `14.22` |
| `Live` | `Short` | `133.50` | 2,420.00 USD | 2,420.00 USD | 0.00 USD | `-1.69%` | `18.12` |
| `Live` | `Short` | `138.50` | 5,350.00 USD | 2,930.00 USD | 0.00 USD | `+1.99%` | `21.17` |
| `Live` | `Short` | `139.50` | 5,450.00 USD | 100.44 USD | 0.00 USD | `+2.73%` | `0.72` |
| `Live` | `Short` | `140.50` | 6,600.00 USD | 1,150.00 USD | 0.00 USD | `+3.47%` | `8.19` |
| `Live` | `Short` | `143.50` | 29,250.00 USD | 22,650.00 USD | 0.00 USD | `+5.68%` | `157.82` |
| `Live` | `Short` | `144.50` | 31,070.00 USD | 1,820.00 USD | 0.00 USD | `+6.41%` | `12.58` |
| `Live` | `Short` | `145.50` | 31,800.00 USD | 731.87 USD | 0.00 USD | `+7.15%` | `5.03` |
| `Live` | `Short` | `150.50` | 120,040.00 USD | 88,250.00 USD | 0.00 USD | `+10.83%` | `586.35` |
| `Live` | `Short` | `151.50` | 122,110.00 USD | 2,060.00 USD | 0.00 USD | `+11.57%` | `13.60` |
| `Live` | `Short` | `152.50` | 717,210.00 USD | 595,110.00 USD | 0.00 USD | `+12.30%` | `3,902.35` |
| `Live` | `Short` | `154.50` | 718,090.00 USD | 877.56 USD | 0.00 USD | `+13.78%` | `5.68` |
| `Live` | `Short` | `155.50` | 722,740.00 USD | 4,650.00 USD | 0.00 USD | `+14.51%` | `29.89` |
| `Live` | `Short` | `157.50` | 722,970.00 USD | 229.95 USD | 0.00 USD | `+15.99%` | `1.46` |
| `Live` | `Short` | `158.50` | 724,790.00 USD | 1,820.00 USD | 0.00 USD | `+16.72%` | `11.47` |
| `Live` | `Short` | `166.50` | 725,120.00 USD | 337.99 USD | 0.00 USD | `+22.61%` | `2.03` |
| `Live` | `Short` | `167.50` | 726,700.00 USD | 1,580.00 USD | 0.00 USD | `+23.35%` | `9.42` |
| `Live` | `Short` | `168.50` | 727,700.00 USD | 995.84 USD | 0.00 USD | `+24.09%` | `5.91` |
| `Live` | `Short` | `169.50` | 758,130.00 USD | 30,430.00 USD | 0.00 USD | `+24.82%` | `179.52` |
| `Live` | `Short` | `170.50` | 758,380.00 USD | 252.34 USD | 0.00 USD | `+25.56%` | `1.48` |
| `Live` | `Short` | `172.50` | 759,160.00 USD | 784.88 USD | 0.00 USD | `+27.03%` | `4.55` |
| `Live` | `Short` | `173.50` | 760,040.00 USD | 870.97 USD | 0.00 USD | `+27.77%` | `5.02` |
| `Live` | `Short` | `175.50` | 765,660.00 USD | 5,620.00 USD | 0.00 USD | `+29.24%` | `32.04` |
| `Live` | `Short` | `177.50` | 791,750.00 USD | 26,090.00 USD | 0.00 USD | `+30.71%` | `147.00` |
| `Live` | `Short` | `180.50` | 804,750.00 USD | 13,000.00 USD | 0.00 USD | `+32.92%` | `72.00` |
| `Live` | `Short` | `181.50` | 4,980,000.00 USD | 4,180,000.00 USD | 0.00 USD | `+33.66%` | `23,011.93` |
| `Live` | `Short` | `184.50` | 5,040,000.00 USD | 55,350.00 USD | 0.00 USD | `+35.87%` | `300.00` |
| `Live` | `Short` | `186.50` | 5,690,000.00 USD | 656,380.00 USD | 0.00 USD | `+37.34%` | `3,519.45` |
| `Live` | `Short` | `187.50` | 5,700,000.00 USD | 4,230.00 USD | 0.00 USD | `+38.08%` | `22.56` |
| `Live` | `Short` | `189.50` | 5,700,000.00 USD | 867.91 USD | 0.00 USD | `+39.55%` | `4.58` |
| `Live` | `Short` | `190.50` | 5,710,000.00 USD | 7,810.00 USD | 0.00 USD | `+40.29%` | `41.00` |
| `Live` | `Short` | `191.50` | 5,710,000.00 USD | 3,050.00 USD | 0.00 USD | `+41.02%` | `15.95` |
| `Live` | `Short` | `192.50` | 5,770,000.00 USD | 58,110.00 USD | 0.00 USD | `+41.76%` | `301.86` |
| `Live` | `Short` | `193.50` | 5,770,000.00 USD | 1,100.00 USD | 0.00 USD | `+42.50%` | `5.68` |
| `Live` | `Short` | `194.50` | 5,780,000.00 USD | 10,010.00 USD | 0.00 USD | `+43.23%` | `51.47` |
| `Live` | `Short` | `196.50` | 9,120,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+44.71%` | `17,000.00` |
| `Live` | `Short` | `199.50` | 9,130,000.00 USD | 9,550.00 USD | 0.00 USD | `+46.92%` | `47.86` |
| `Live` | `Short` | `200.50` | 9,140,000.00 USD | 11,660.00 USD | 0.00 USD | `+47.65%` | `58.15` |
| `Live` | `Short` | `203.50` | 9,140,000.00 USD | 372.41 USD | 0.00 USD | `+49.86%` | `1.83` |
| `Live` | `Short` | `205.50` | 9,230,000.00 USD | 84,610.00 USD | 0.00 USD | `+51.33%` | `411.72` |
| `Live` | `Short` | `210.50` | 9,230,000.00 USD | 2,970.00 USD | 0.00 USD | `+55.02%` | `14.10` |
| `Live` | `Short` | `218.50` | 9,250,000.00 USD | 21,680.00 USD | 0.00 USD | `+60.91%` | `99.20` |
| `Live` | `Short` | `220.50` | 9,250,000.00 USD | 2,000.00 USD | 0.00 USD | `+62.38%` | `9.06` |
| `Live` | `Short` | `223.50` | 9,300,000.00 USD | 47,810.00 USD | 0.00 USD | `+64.59%` | `213.92` |
| `Live` | `Short` | `225.50` | 9,320,000.00 USD | 23,640.00 USD | 0.00 USD | `+66.06%` | `104.85` |
| `Live` | `Short` | `227.50` | 9,320,000.00 USD | 1,610.00 USD | 0.00 USD | `+67.53%` | `7.07` |
| `Live` | `Short` | `228.50` | 9,330,000.00 USD | 520.98 USD | 0.00 USD | `+68.27%` | `2.28` |
| `Live` | `Short` | `229.50` | 9,370,000.00 USD | 49,300.00 USD | 0.00 USD | `+69.01%` | `214.83` |
| `Live` | `Short` | `232.50` | 9,370,000.00 USD | 225.53 USD | 0.00 USD | `+71.22%` | `0.97` |
| `Live` | `Short` | `237.50` | 9,380,000.00 USD | 4,750.00 USD | 0.00 USD | `+74.90%` | `20.00` |
| `Live` | `Short` | `239.50` | 9,380,000.00 USD | 1,050.00 USD | 0.00 USD | `+76.37%` | `4.39` |
| `Live` | `Short` | `240.50` | 9,380,000.00 USD | 103.41 USD | 0.00 USD | `+77.11%` | `0.43` |
| `Live` | `Short` | `242.50` | 9,380,000.00 USD | 647.48 USD | 0.00 USD | `+78.58%` | `2.67` |
| `Live` | `Short` | `252.50` | 9,380,000.00 USD | 166.65 USD | 0.00 USD | `+85.95%` | `0.66` |
| `Live` | `Short` | `253.50` | 9,400,000.00 USD | 18,500.00 USD | 0.00 USD | `+86.68%` | `72.97` |
| `Live` | `Short` | `254.50` | 9,420,000.00 USD | 15,410.00 USD | 0.00 USD | `+87.42%` | `60.54` |
| `Live` | `Short` | `255.50` | 9,420,000.00 USD | 702.62 USD | 0.00 USD | `+88.15%` | `2.75` |
| `Live` | `Short` | `257.50` | 9,420,000.00 USD | 1,430.00 USD | 0.00 USD | `+89.63%` | `5.57` |
| `Live` | `Short` | `260.50` | 9,570,000.00 USD | 151,980.00 USD | 0.00 USD | `+91.84%` | `583.40` |
| `Live` | `Short` | `262.50` | 9,570,000.00 USD | 763.88 USD | 0.00 USD | `+93.31%` | `2.91` |
| `Live` | `Short` | `263.50` | 9,570,000.00 USD | 532.27 USD | 0.00 USD | `+94.05%` | `2.02` |
| `Live` | `Short` | `266.50` | 9,590,000.00 USD | 15,990.00 USD | 0.00 USD | `+96.26%` | `60.00` |
| `Live` | `Short` | `267.50` | 9,610,000.00 USD | 21,110.00 USD | 0.00 USD | `+96.99%` | `78.93` |
| `Live` | `Short` | `268.50` | 9,630,000.00 USD | 23,970.00 USD | 0.00 USD | `+97.73%` | `89.27` |
| `Live` | `Short` | `270.50` | 9,630,000.00 USD | 235.34 USD | 0.00 USD | `+99.20%` | `0.87` |

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
  * Current Rate: `9.10K` | Last 24h: `22.61K` | Last 3d: `65.36K` | Last 7d: `109.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0043%` | **USDT OKX** | `0.0076%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0042%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0099%` | **USDT Bitget** | `0.0033%` |
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
| `5:00 UTC` | `135.36` | `134.90` | `135.36` | `135.69` | `134.19` | 1,643,969.98 USD | 713,479.07 USD | 930,490.91 USD | -217,011.84 USD | `-13.20%` | `14B / 41S` |
| `0:00 UTC` | `135.81` | `135.11` | `135.81` | `135.97` | `134.12` | 1,651,999.36 USD | 836,590.75 USD | 815,408.61 USD | 21,182.13 USD | `+1.28%` | `41B / 22S` |
| `5:00 UTC` | `135.80` | `135.69` | `135.80` | `136.03` | `135.32` | 1,251,302.78 USD | 483,395.43 USD | 767,907.35 USD | -284,511.93 USD | `-22.74%` | `8B / 18S` |
| `0:00 UTC` | `136.50` | `136.45` | `136.50` | `136.91` | `135.53` | 2,672,463.66 USD | 1,636,609.16 USD | 1,035,854.51 USD | 600,754.65 USD | `+22.48%` | `41B / 16S` |
| `5:00 UTC` | `137.00` | `136.75` | `137.00` | `137.11` | `136.31` | 1,755,992.28 USD | 798,369.60 USD | 957,622.69 USD | -159,253.09 USD | `-9.07%` | `15B / 15S` |
| `0:00 UTC` | `136.91` | `137.14` | `136.91` | `137.94` | `136.38` | 2,268,812.62 USD | 1,173,914.80 USD | 1,094,897.82 USD | 79,016.99 USD | `+3.48%` | `32B / 27S` |
| `5:00 UTC` | `136.36` | `136.58` | `136.36` | `137.31` | `136.01` | 2,016,544.71 USD | 820,255.37 USD | 1,196,289.34 USD | -376,033.97 USD | `-18.65%` | `6B / 45S` |
| `0:00 UTC` | `136.31` | `135.82` | `136.31` | `136.41` | `135.25` | 1,856,319.84 USD | 851,137.54 USD | 1,005,182.30 USD | -154,044.76 USD | `-8.30%` | `11B / 26S` |
| `5:00 UTC` | `136.19` | `136.08` | `136.19` | `136.38` | `135.78` | 1,030,013.81 USD | 443,410.64 USD | 586,603.17 USD | -143,192.54 USD | `-13.90%` | `6B / 15S` |
| `0:00 UTC` | `135.20` | `135.19` | `135.20` | `135.91` | `134.72` | 2,147,077.59 USD | 1,184,718.32 USD | 962,359.27 USD | 222,359.04 USD | `+10.36%` | `11B / 33S` |

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
| `5m` | 0.00 USD | 145,580.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 149,470.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | -296,940.00 USD | **`DISTRIBUTION`** |
| `1h` | 0.00 USD | -1,670,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -1,260,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -798,690.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -1,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -113,200.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -595,200.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -1,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -37,210,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -98,540,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+145.58K` | 15m=`+149.47K` | 1h=`-1.67M` | 24h=`-1.57M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `130.61` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `128.87` (Risk Distance: `1.74` pts)
  * +2.5R Take Profit: `134.96`
  * Mathematical Lot Sizing: **`5.74 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `136.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `138.44` (Risk Distance: `1.74` pts)
  * +2.5R Take Profit: `132.35`
  * Mathematical Lot Sizing: **`5.74 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`135.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
