# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 15:09:00 IST` (`2026-10-30 09:39:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `278.66` | **Live Ask Quote**: `279.24` | **Mid Price**: `278.95`
- **Spread Points**: `580.00` | **Spread BPS**: `20.79 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `276.58` | VWAP Z-Score: `+0.39` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.09` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.04` | Lower -3.00σ Band: `258.12`
  * Upper +2.51σ Band: `292.03` | Lower -2.51σ Band: `261.13`
  * Upper +2.01σ Band: `288.95` | Lower -2.01σ Band: `264.21`
  * Upper +2.00σ Band: `288.89` | Lower -2.00σ Band: `264.27`
  * Upper +1.28σ Band: `284.46` | Lower -1.28σ Band: `268.70`
  * Upper +1.00σ Band: `282.73` | Lower -1.00σ Band: `270.43`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`280.43` | EMA-20=`280.88` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.26` (Slope: `+0.0000`) | EMA-100=`280.82`
  * Institutional Anchors: EMA-144=`281.70` | EMA-200=`283.30` (Slope: `-0.0870`) | EMA-233=`284.23`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `281.91` (Distance: `-1.05%`)
  * Point of Control (POC) = `276.23` (Distance: `+0.99%`)
  * Value Area Low (VAL) = `269.12` (Distance: `+3.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`280.62` | Low=`277.28`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `277.83` - `280.07`
  * Optimal Trade Entry (OTE 0.705): `279.51`
  * Structural Invalidation Anchor (0.786): `281.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `280.23` | `280.32` | `279.06` | `279.06` | `618` | 172,656.08 USD | -93,190.76 USD | `-53.97%` | -1,885,653.17 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `279.05` | `279.56` | `279.05` | `279.56` | `956` | 266,819.21 USD | 179,288.89 USD | `+67.19%` | -1,706,364.28 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `279.56` | `279.59` | `279.18` | `279.18` | `195` | 54,374.59 USD | -26,713.35 USD | `-49.13%` | -1,733,077.63 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `279.03` | `281.28` | `278.54` | `280.08` | `6,994` | 1,960,555.94 USD | -166,596.10 USD | `-8.50%` | -1,767,792.48 USD | `-0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `280.08` | `280.70` | `279.05` | `279.56` | `2,207` | 617,038.04 USD | 48,733.95 USD | `+7.90%` | -1,719,058.53 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `279.56` | `279.59` | `279.18` | `279.22` | `199` | 55,655.49 USD | -25,432.45 USD | `-45.70%` | -1,744,490.98 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `283.68` | `284.86` | `280.79` | `281.78` | `11,868` | 3,357,238.13 USD | -360,522.64 USD | `-10.74%` | -1,826,347.97 USD | `-0.33` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `278.73` | `279.02` | `16,468` | 4,630,594.81 USD | 275,996.65 USD | `+5.96%` | -1,550,351.32 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `279.03` | `281.28` | `278.54` | `279.18` | `9,396` | 2,631,947.63 USD | -144,596.43 USD | `-5.49%` | -1,694,947.75 USD | `-0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `279.18` | `25,863` | 7,262,542.44 USD | 131,400.22 USD | `+1.81%` | -1,608,510.43 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `279.18` | `25,863` | 7,262,542.44 USD | 131,400.22 USD | `+1.81%` | -1,608,510.43 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`278.95`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1983` | `0x12d2...f97f` | `LONG` | 1,012,606.55 USD | `3,627,243,000,000.00` | `303.26` | `278.89` | `0.000000` | -87,392.79 USD | `-8.63%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+3.39%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--4.99%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.36%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--4.97%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.36%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--4.97%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.36%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--4.97%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `65.50` | 2,690.00 USD | 211,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 556.06 USD | 208,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 1,120.00 USD | 208,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 349.65 USD | 206,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 206,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,400.00 USD | 205,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 199,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 107.50 USD | 195,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 195,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 194,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 194,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 194,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 1,930.00 USD | 193,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 130.50 USD | 192,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `132.50` | 3,310.00 USD | 191,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 188,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 187,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 186,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 184,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `161.50` | 1,550.00 USD | 183,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 182,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 8,660.00 USD | 181,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `168.50` | 1,280.00 USD | 173,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 171,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 171,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 171,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 170,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 170,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 169,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 169,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 168,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 167,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 166,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 210.65 USD | 165,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 165,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 165,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 164,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 164,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 41,790.00 USD | 164,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 122,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `211.50` | 634.50 USD | 122,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 121,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 117,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `222.50` | 7,010.00 USD | 117,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 31,290.00 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 5,830.00 USD | 79,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 73,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 72,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 72,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 114.75 USD | 71,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 1,190.00 USD | 71,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 70,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 637.61 USD | 69,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `234.80` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 10,380,000.00 USD | 10,380,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 10,360,000.00 USD | 10,360,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 10,350,000.00 USD | 10,350,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 69,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 10,310,000.00 USD | 10,310,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 10,310,000.00 USD | 10,310,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `238.50` | 10,840.00 USD | 45,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `238.80` | 10,290,000.00 USD | 10,290,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 10,260,000.00 USD | 10,260,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 34,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.30` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,240,000.00 USD | 10,240,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 10,240,000.00 USD | 10,240,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 33,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 10,230,000.00 USD | 10,230,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 10,210,000.00 USD | 10,210,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.80` | 10,130,000.00 USD | 10,130,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 3,380.00 USD | 33,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 10,110,000.00 USD | 10,110,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 29,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 10,060,000.00 USD | 10,060,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 10,030,000.00 USD | 10,030,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 10,000,000.00 USD | 10,000,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 10,000,000.00 USD | 10,000,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 9,950,000.00 USD | 9,950,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 9,940,000.00 USD | 9,940,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,900,000.00 USD | 9,900,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,890,000.00 USD | 9,890,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,880,000.00 USD | 9,880,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,770,000.00 USD | 9,770,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,700,000.00 USD | 9,700,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,580,000.00 USD | 9,580,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.50` | 4,980,000.00 USD | 4,980,000.00 USD | 13,910.00 USD | 7,600.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 23,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,490,000.00 USD | 9,490,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.90` | 4,940,000.00 USD | 4,940,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,900,000.00 USD | 4,900,000.00 USD | 26,350.00 USD | 24,910.00 USD | 23,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 9,350,000.00 USD | 9,350,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,830,000.00 USD | 4,830,000.00 USD | 30,050.00 USD | 53,570.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.80` | 9,200,000.00 USD | 9,200,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,730,000.00 USD | 4,730,000.00 USD | 20,730.00 USD | 8,350.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 8,990,000.00 USD | 8,990,000.00 USD | 69,530.00 USD | 39,900.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,690,000.00 USD | 4,690,000.00 USD | 10,950.00 USD | 1,620.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,870,000.00 USD | 8,870,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,670,000.00 USD | 4,670,000.00 USD | 3,030.00 USD | 6,970.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,660,000.00 USD | 4,660,000.00 USD | 12,480.00 USD | 8,710.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,780,000.00 USD | 8,780,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,620,000.00 USD | 4,620,000.00 USD | 21,830.00 USD | 15,190.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,680,000.00 USD | 8,680,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,570,000.00 USD | 4,570,000.00 USD | 1,590.00 USD | 7,170.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,590,000.00 USD | 8,590,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,560,000.00 USD | 4,560,000.00 USD | 8,310.00 USD | 10,840.00 USD | 35.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,470,000.00 USD | 8,470,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,540,000.00 USD | 4,540,000.00 USD | 9,050.00 USD | 10,890.00 USD | 24.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,520,000.00 USD | 4,520,000.00 USD | 9,910.00 USD | 15,540.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 8,300,000.00 USD | 8,300,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,460,000.00 USD | 4,460,000.00 USD | 14,640.00 USD | 23,250.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 8,220,000.00 USD | 8,220,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,410,000.00 USD | 4,410,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 8,160,000.00 USD | 8,160,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,370,000.00 USD | 4,370,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.80` | 8,060,000.00 USD | 8,060,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,320,000.00 USD | 4,320,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,300,000.00 USD | 4,300,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 7,950,000.00 USD | 7,950,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,280,000.00 USD | 4,280,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,920,000.00 USD | 7,920,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,270,000.00 USD | 4,270,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,850,000.00 USD | 7,850,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,200,000.00 USD | 4,200,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 645.99 USD | 17,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,630,000.00 USD | 7,630,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,140,000.00 USD | 4,140,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 4,070,000.00 USD | 4,070,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,450,000.00 USD | 7,450,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 4,030,000.00 USD | 4,030,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 7,390,000.00 USD | 7,390,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 3,940,000.00 USD | 3,940,000.00 USD | 39,530.00 USD | 8,640.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 7,240,000.00 USD | 7,240,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,880,000.00 USD | 3,880,000.00 USD | 19,010.00 USD | 1,900.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,340.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,020,000.00 USD | 7,020,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,830,000.00 USD | 3,830,000.00 USD | 8,950.00 USD | 50,950.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,760,000.00 USD | 3,760,000.00 USD | 8,220.00 USD | 29,340.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,890,000.00 USD | 6,890,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,690,000.00 USD | 3,690,000.00 USD | 15,340.00 USD | 60,640.00 USD | 51,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,730,000.00 USD | 6,730,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,560,000.00 USD | 3,560,000.00 USD | 13,620.00 USD | 27,450.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,530,000.00 USD | 6,530,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,500,000.00 USD | 3,500,000.00 USD | 21,110.00 USD | 4,750.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,360,000.00 USD | 6,360,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,460,000.00 USD | 3,460,000.00 USD | 629.76 USD | 12,630.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,430,000.00 USD | 3,430,000.00 USD | 9,930.00 USD | 4,350.00 USD | 61,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 6,200,000.00 USD | 6,200,000.00 USD | 33,590.00 USD | 13,710.00 USD | 169.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `263.50` | 464.81 USD | 13,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,350,000.00 USD | 3,350,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 6,150,000.00 USD | 6,150,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,240,000.00 USD | 3,240,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,640,000.00 USD | 5,640,000.00 USD | 48,230.00 USD | 1,170.00 USD | 128.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,160,000.00 USD | 3,160,000.00 USD | 1,200.00 USD | 19,920.00 USD | 4.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,590,000.00 USD | 5,590,000.00 USD | 33,470.00 USD | 21,870.00 USD | 198.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,140,000.00 USD | 3,140,000.00 USD | 33,390.00 USD | 2,170.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,050,000.00 USD | 3,050,000.00 USD | 64,840.00 USD | 2,650.00 USD | 9.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,540,000.00 USD | 5,540,000.00 USD | 256,440.00 USD | 2,330.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.70` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 629.76 USD | 6.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 5,240,000.00 USD | 5,240,000.00 USD | 69,380.00 USD | 0.00 USD | 106.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 2,980,000.00 USD | 2,980,000.00 USD | 16,330.00 USD | 13,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 5,170,000.00 USD | 5,170,000.00 USD | 216,090.00 USD | 645.20 USD | 17.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 2,950,000.00 USD | 2,950,000.00 USD | 14,430.00 USD | 8,470.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 4,960,000.00 USD | 4,960,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 2,920,000.00 USD | 2,920,000.00 USD | 18,330.00 USD | 22,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 2,880,000.00 USD | 2,880,000.00 USD | 33,460.00 USD | 68,530.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,760,000.00 USD | 4,760,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.70` | 2,770,000.00 USD | 2,770,000.00 USD | 10,330.00 USD | 36,260.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,570,000.00 USD | 4,570,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,690,000.00 USD | 2,690,000.00 USD | 18,930.00 USD | 28,480.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,280,000.00 USD | 4,280,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,590,000.00 USD | 2,590,000.00 USD | 18,310.00 USD | 18,920.00 USD | 67.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,840,000.00 USD | 3,840,000.00 USD | 23,340.00 USD | 17,480.00 USD | 105.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,550,000.00 USD | 2,550,000.00 USD | 21,330.00 USD | 11,500.00 USD | 182.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,520,000.00 USD | 2,520,000.00 USD | 7,610.00 USD | 1,120.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 3,490.00 USD | 148.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,500,000.00 USD | 2,500,000.00 USD | 6,500.00 USD | 17,350.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 1,920.00 USD | 240.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,460,000.00 USD | 2,460,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,430,000.00 USD | 2,430,000.00 USD | 42,710.00 USD | 118.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,790,000.00 USD | 3,790,000.00 USD | 33,050.00 USD | 0.00 USD | 120.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,390,000.00 USD | 2,390,000.00 USD | 505.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,370,000.00 USD | 2,370,000.00 USD | 12,710.00 USD | 1,780.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,350,000.00 USD | 2,350,000.00 USD | 8,650.00 USD | 34,920.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,740,000.00 USD | 3,740,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,300,000.00 USD | 2,300,000.00 USD | 21,980.00 USD | 21,380.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,230,000.00 USD | 2,230,000.00 USD | 6,060.00 USD | 38,280.00 USD | 41,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,600,000.00 USD | 3,600,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,150,000.00 USD | 2,150,000.00 USD | 59,390.00 USD | 5,420.00 USD | 71,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 2,010,000.00 USD | 2,010,000.00 USD | 28,730.00 USD | 121,350.00 USD | 40,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 1,820,000.00 USD | 1,820,000.00 USD | 69,050.00 USD | 67,190.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 3,100,000.00 USD | 3,100,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,610,000.00 USD | 1,610,000.00 USD | 165,910.00 USD | 37,550.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,830,000.00 USD | 2,830,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,400,000.00 USD | 1,400,000.00 USD | 186,780.00 USD | 21,440.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 2,170,000.00 USD | 2,170,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,140,000.00 USD | 1,140,000.00 USD | 47,590.00 USD | 19,960.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,060,000.00 USD | 1,060,000.00 USD | 11,720.00 USD | 0.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,640,000.00 USD | 1,640,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,040,000.00 USD | 1,040,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,560,000.00 USD | 1,560,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 917,560.00 USD | 917,560.00 USD | 161,250.00 USD | 3,340.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,450,000.00 USD | 1,450,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 745,880.00 USD | 745,880.00 USD | 11,920.00 USD | 5,230.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 1,130,000.00 USD | 1,130,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 719,920.00 USD | 719,920.00 USD | 37,290.00 USD | 25,410.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 633,750.00 USD | 633,750.00 USD | 17,610.00 USD | 18,260.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 1,110,000.00 USD | 1,110,000.00 USD | 152,190.00 USD | 77,800.00 USD | 140,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 587,280.00 USD | 587,280.00 USD | 13,750.00 USD | 10,950.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 743,120.00 USD | 743,120.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 542,280.00 USD | 542,280.00 USD | 12,120.00 USD | 97,470.00 USD | 83,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 525,530.00 USD | 525,530.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 349,030.00 USD | 349,030.00 USD | 78,720.00 USD | 56,870.00 USD | 47,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 308,370.00 USD | 308,370.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 165,580.00 USD | 165,580.00 USD | 19,260.00 USD | 10,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 135,480.00 USD | 135,480.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 238,000.00 USD | 238,000.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 94,400.00 USD | 94,400.00 USD | 0.00 USD | 0.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 70,080.00 USD | 70,080.00 USD | 0.00 USD | 0.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 38,750.00 USD | 38,750.00 USD | 0.00 USD | 38,740.00 USD | 12.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 235,340.00 USD | 235,340.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.90` | 17,460.00 USD | 17,460.00 USD | 0.00 USD | 17,450.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 219,800.00 USD | 219,800.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.80` | 122,390.00 USD | 122,390.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.10` | 29,870.00 USD | 29,870.00 USD | 8,260.00 USD | 0.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.30` | 24,220.00 USD | 24,220.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.30` | 31,160.00 USD | 31,160.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.30` | 27,670.00 USD | 27,670.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 29,670.00 USD | 29,670.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 31,230.00 USD | 31,230.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.50` | 69,360.00 USD | 69,360.00 USD | 10,630.00 USD | 0.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 86,620.00 USD | 86,620.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 105,720.00 USD | 105,720.00 USD | 28,720.00 USD | 7,620.00 USD | 9.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 200,330.00 USD | 200,330.00 USD | 36,620.00 USD | 16,320.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 508,580.00 USD | 508,580.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 249,340.00 USD | 249,340.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 742,130.00 USD | 742,130.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 312,620.00 USD | 312,620.00 USD | 26,810.00 USD | 719.80 USD | 35,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 786,350.00 USD | 786,350.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 359,680.00 USD | 359,680.00 USD | 15,270.00 USD | 1,650.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,030,000.00 USD | 1,030,000.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 514,540.00 USD | 514,540.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 690,070.00 USD | 690,070.00 USD | 97,970.00 USD | 43,890.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,230,000.00 USD | 1,230,000.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 785,290.00 USD | 785,290.00 USD | 22,860.00 USD | 22,500.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,630,000.00 USD | 1,630,000.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 867,210.00 USD | 867,210.00 USD | 21,420.00 USD | 26,660.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 974,760.00 USD | 974,760.00 USD | 52,260.00 USD | 26,060.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 1,930,000.00 USD | 1,930,000.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 1,040,000.00 USD | 1,040,000.00 USD | 44,740.00 USD | 24,620.00 USD | 17.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 1,160,000.00 USD | 1,160,000.00 USD | 17,220.00 USD | 47,120.00 USD | 51,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 1,370,000.00 USD | 1,370,000.00 USD | 52,150.00 USD | 67,790.00 USD | 92,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,330,000.00 USD | 2,330,000.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,600,000.00 USD | 1,600,000.00 USD | 65,110.00 USD | 51,750.00 USD | 114,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,390,000.00 USD | 2,390,000.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,800,000.00 USD | 1,800,000.00 USD | 28,010.00 USD | 120,130.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,510,000.00 USD | 2,510,000.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,940,000.00 USD | 1,940,000.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 2,010,000.00 USD | 2,010,000.00 USD | 27,020.00 USD | 12,070.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,570,000.00 USD | 2,570,000.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 2,070,000.00 USD | 2,070,000.00 USD | 9,470.00 USD | 23,560.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 2,770,000.00 USD | 2,770,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 2,120,000.00 USD | 2,120,000.00 USD | 6,710.00 USD | 37,580.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 2,840,000.00 USD | 2,840,000.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 2,160,000.00 USD | 2,160,000.00 USD | 29,880.00 USD | 3,650.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 6,050.00 USD | 7,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,940,000.00 USD | 2,940,000.00 USD | 887.27 USD | 101,280.00 USD | 138.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,260,000.00 USD | 2,260,000.00 USD | 62,580.00 USD | 30,990.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,330,000.00 USD | 2,330,000.00 USD | 22,320.00 USD | 18,040.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,110,000.00 USD | 3,110,000.00 USD | 33,580.00 USD | 132,770.00 USD | 91.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,510,000.00 USD | 2,510,000.00 USD | 76,520.00 USD | 47,640.00 USD | 64,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,170,000.00 USD | 3,170,000.00 USD | 38,790.00 USD | 1,860.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,610,000.00 USD | 2,610,000.00 USD | 21,480.00 USD | 23,760.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,580,000.00 USD | 3,580,000.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,870,000.00 USD | 2,870,000.00 USD | 96,690.00 USD | 76,870.00 USD | 85,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,840,000.00 USD | 3,840,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 2,970,000.00 USD | 2,970,000.00 USD | 33,360.00 USD | 16,240.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 3,140,000.00 USD | 3,140,000.00 USD | 15,750.00 USD | 60,930.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,310,000.00 USD | 4,310,000.00 USD | 46,330.00 USD | 82,780.00 USD | 345,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,370,000.00 USD | 3,370,000.00 USD | 98,960.00 USD | 6,830.00 USD | 128,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 4,760,000.00 USD | 4,760,000.00 USD | 165,320.00 USD | 82,100.00 USD | 197,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,590,000.00 USD | 3,590,000.00 USD | 52,840.00 USD | 126,740.00 USD | 35,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 5,090,000.00 USD | 5,090,000.00 USD | 43,710.00 USD | 167,940.00 USD | 120,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,690,000.00 USD | 3,690,000.00 USD | 33,300.00 USD | 22,420.00 USD | 41,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,430,000.00 USD | 5,430,000.00 USD | 133,820.00 USD | 3,570.00 USD | 201,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,820,000.00 USD | 3,820,000.00 USD | 24,280.00 USD | 21,780.00 USD | 90,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 3,920,000.00 USD | 3,920,000.00 USD | 61,380.00 USD | 1,000.00 USD | 31,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,560,000.00 USD | 5,560,000.00 USD | 78,980.00 USD | 54,960.00 USD | 72.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 3,960,000.00 USD | 3,960,000.00 USD | 15,840.00 USD | 11,340.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 5,800,000.00 USD | 5,800,000.00 USD | 47,530.00 USD | 99,810.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 4,060,000.00 USD | 4,060,000.00 USD | 51,840.00 USD | 10,000.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 5,950,000.00 USD | 5,950,000.00 USD | 32,650.00 USD | 45,150.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,120,000.00 USD | 4,120,000.00 USD | 5,730.00 USD | 1,480.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,030,000.00 USD | 6,030,000.00 USD | 69,820.00 USD | 12,530.00 USD | 112.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,250,000.00 USD | 4,250,000.00 USD | 28,240.00 USD | 5,580.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,310,000.00 USD | 4,310,000.00 USD | 34,110.00 USD | 10,760.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,150,000.00 USD | 6,150,000.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,360,000.00 USD | 4,360,000.00 USD | 8,250.00 USD | 10,790.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,200,000.00 USD | 6,200,000.00 USD | 22,060.00 USD | 9,100.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,480,000.00 USD | 4,480,000.00 USD | 19,900.00 USD | 36,560.00 USD | 64,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,230,000.00 USD | 6,230,000.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,520,000.00 USD | 4,520,000.00 USD | 23,270.00 USD | 1,560.00 USD | 17,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,380,000.00 USD | 6,380,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,550,000.00 USD | 4,550,000.00 USD | 269.05 USD | 1,020.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,590,000.00 USD | 4,590,000.00 USD | 597.00 USD | 15,110.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 6,660,000.00 USD | 6,660,000.00 USD | 73,320.00 USD | 58,690.00 USD | 150,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,630,000.00 USD | 4,630,000.00 USD | 19,840.00 USD | 8,470.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 6,910,000.00 USD | 6,910,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,700,000.00 USD | 4,700,000.00 USD | 25,190.00 USD | 30,660.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 7,090,000.00 USD | 7,090,000.00 USD | 1,560.00 USD | 181,550.00 USD | 35.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,760,000.00 USD | 4,760,000.00 USD | 13,820.00 USD | 13,290.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `302.50` | 3,640.00 USD | 10,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,320,000.00 USD | 7,320,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 4,780,000.00 USD | 4,780,000.00 USD | 1,370.00 USD | 2,260.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 4,810,000.00 USD | 4,810,000.00 USD | 21,200.00 USD | 2,760.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 1,950.00 USD | 183.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 391.16 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,380,000.00 USD | 7,380,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 4,880,000.00 USD | 4,880,000.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,400,000.00 USD | 7,400,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 4,930,000.00 USD | 4,930,000.00 USD | 9,670.00 USD | 2,100.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,460,000.00 USD | 7,460,000.00 USD | 35,470.00 USD | 11,790.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 4,950,000.00 USD | 4,950,000.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 4,950,000.00 USD | 4,950,000.00 USD | 83.23 USD | 172.52 USD | 7.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 7,880,000.00 USD | 7,880,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 4,970,000.00 USD | 4,970,000.00 USD | 6,340.00 USD | 3,500.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,030,000.00 USD | 8,030,000.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 4,990,000.00 USD | 4,990,000.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,190,000.00 USD | 8,190,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 5,000,000.00 USD | 5,000,000.00 USD | 4,330.00 USD | 6.13 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,430,000.00 USD | 8,430,000.00 USD | 94,690.00 USD | 74,510.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,070,000.00 USD | 5,070,000.00 USD | 19,810.00 USD | 35,610.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,140,000.00 USD | 5,140,000.00 USD | 11,250.00 USD | 40,340.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 8,740,000.00 USD | 8,740,000.00 USD | 27,410.00 USD | 136,370.00 USD | 147,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,200,000.00 USD | 5,200,000.00 USD | 27,000.00 USD | 25,340.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,040,000.00 USD | 9,040,000.00 USD | 127,080.00 USD | 113,210.00 USD | 60,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,240,000.00 USD | 5,240,000.00 USD | 19,140.00 USD | 7,600.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,390,000.00 USD | 9,390,000.00 USD | 169,010.00 USD | 66,670.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,250,000.00 USD | 5,250,000.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,560,000.00 USD | 9,560,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,260,000.00 USD | 5,260,000.00 USD | 7,450.00 USD | 5,890.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 5,270,000.00 USD | 5,270,000.00 USD | 3,240.00 USD | 1,580.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 9,660,000.00 USD | 9,660,000.00 USD | 34,260.00 USD | 36,030.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 5,290,000.00 USD | 5,290,000.00 USD | 10,040.00 USD | 7,670.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,010,000.00 USD | 10,010,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 5,320,000.00 USD | 5,320,000.00 USD | 14,750.00 USD | 3,980.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,260,000.00 USD | 10,260,000.00 USD | 62,230.00 USD | 108,410.00 USD | 80,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 5,330,000.00 USD | 5,330,000.00 USD | 112.30 USD | 5,020.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,390,000.00 USD | 10,390,000.00 USD | 60,910.00 USD | 51,380.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 5,340,000.00 USD | 5,340,000.00 USD | 5,080.00 USD | 73.70 USD | 13.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 5,340,000.00 USD | 5,340,000.00 USD | 257.90 USD | 2,350.00 USD | 29.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,630,000.00 USD | 10,630,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 5,360,000.00 USD | 5,360,000.00 USD | 7,980.00 USD | 9,070.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 10,690,000.00 USD | 10,690,000.00 USD | 19,570.00 USD | 11,240.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 5,380,000.00 USD | 5,380,000.00 USD | 299.35 USD | 10,320.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 10,770,000.00 USD | 10,770,000.00 USD | 43,780.00 USD | 11,410.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,420,000.00 USD | 5,420,000.00 USD | 14,640.00 USD | 8,480.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,830,000.00 USD | 10,830,000.00 USD | 21,990.00 USD | 14,880.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 5,440,000.00 USD | 5,440,000.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 5,460,000.00 USD | 5,460,000.00 USD | 3,580.00 USD | 18,130.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 10,900,000.00 USD | 10,900,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 5,470,000.00 USD | 5,470,000.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 10,980,000.00 USD | 10,980,000.00 USD | 32,780.00 USD | 1,570.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 11,070,000.00 USD | 11,070,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,100,000.00 USD | 11,100,000.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 11,110,000.00 USD | 11,110,000.00 USD | 500.10 USD | 547.95 USD | 9.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,190,000.00 USD | 11,190,000.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,290,000.00 USD | 11,290,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,350,000.00 USD | 11,350,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,360,000.00 USD | 11,360,000.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,390,000.00 USD | 11,390,000.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 11,460,000.00 USD | 11,460,000.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 11,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `324.50` | 2,220.00 USD | 14,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `338.50` | 1,350.00 USD | 40,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 41,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 42,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `373.50` | 41,090.00 USD | 83,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `406.50` | 10,640.00 USD | 94,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 140,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 141,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `535.50` | 348.61 USD | 141,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 142,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `65.50` | 211,350.00 USD | 0.00 USD | 2,690.00 USD | `-76.64%` | `41,012,000,000.00` |
| `Live` | `Long` | `77.50` | 208,670.00 USD | 0.00 USD | 556.06 USD | `-72.36%` | `7,175,000,000.00` |
| `Live` | `Long` | `85.50` | 208,110.00 USD | 0.00 USD | 1,120.00 USD | `-69.51%` | `13,105,000,000.00` |
| `Live` | `Long` | `92.50` | 206,990.00 USD | 0.00 USD | 349.65 USD | `-67.02%` | `3,780,000,000.00` |
| `Live` | `Long` | `95.50` | 206,640.00 USD | 0.00 USD | 920.05 USD | `-65.95%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 205,720.00 USD | 0.00 USD | 6,400.00 USD | `-63.81%` | `63,008,000,000.00` |
| `Live` | `Long` | `102.50` | 199,330.00 USD | 0.00 USD | 4,080.00 USD | `-63.45%` | `39,797,000,000.00` |
| `Live` | `Long` | `107.50` | 195,250.00 USD | 0.00 USD | 107.50 USD | `-61.67%` | `1,000,000,000.00` |
| `Live` | `Long` | `109.50` | 195,140.00 USD | 0.00 USD | 212.76 USD | `-60.95%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 194,930.00 USD | 0.00 USD | 212.35 USD | `-57.74%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 194,710.00 USD | 0.00 USD | 124.46 USD | `-56.32%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 194,590.00 USD | 0.00 USD | 658.18 USD | `-54.89%` | `5,203,000,000.00` |
| `Live` | `Long` | `128.50` | 193,930.00 USD | 0.00 USD | 1,930.00 USD | `-54.18%` | `15,000,000,000.00` |
| `Live` | `Long` | `130.50` | 192,000.00 USD | 0.00 USD | 130.50 USD | `-53.47%` | `1,000,000,000.00` |
| `Live` | `Long` | `132.50` | 191,870.00 USD | 0.00 USD | 3,310.00 USD | `-52.75%` | `25,000,000,000.00` |
| `Live` | `Long` | `147.50` | 188,560.00 USD | 0.00 USD | 895.47 USD | `-47.40%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 187,660.00 USD | 0.00 USD | 1,270.00 USD | `-47.05%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 186,400.00 USD | 0.00 USD | 2,370.00 USD | `-46.69%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 184,030.00 USD | 0.00 USD | 303.78 USD | `-45.62%` | `1,992,000,000.00` |
| `Live` | `Long` | `161.50` | 183,730.00 USD | 0.00 USD | 1,550.00 USD | `-42.41%` | `9,599,000,000.00` |
| `Live` | `Long` | `162.50` | 182,180.00 USD | 0.00 USD | 325.00 USD | `-42.06%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 181,850.00 USD | 0.00 USD | 8,660.00 USD | `-40.27%` | `51,706,000,000.00` |
| `Live` | `Long` | `168.50` | 173,190.00 USD | 0.00 USD | 1,280.00 USD | `-39.92%` | `7,572,000,000.00` |
| `Live` | `Long` | `170.50` | 171,920.00 USD | 0.00 USD | 426.25 USD | `-39.20%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 171,490.00 USD | 0.00 USD | 169.96 USD | `-37.78%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 171,320.00 USD | 0.00 USD | 516.67 USD | `-37.42%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 170,800.00 USD | 0.00 USD | 373.83 USD | `-37.06%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 170,430.00 USD | 0.00 USD | 808.66 USD | `-34.21%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 169,620.00 USD | 0.00 USD | 418.28 USD | `-32.78%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 169,200.00 USD | 0.00 USD | 694.75 USD | `-32.07%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 168,510.00 USD | 0.00 USD | 858.49 USD | `-31.71%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 167,650.00 USD | 0.00 USD | 1,490.00 USD | `-31.36%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 166,160.00 USD | 0.00 USD | 370.47 USD | `-30.29%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 165,790.00 USD | 0.00 USD | 210.65 USD | `-29.93%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 165,580.00 USD | 0.00 USD | 548.03 USD | `-28.86%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 165,040.00 USD | 0.00 USD | 293.13 USD | `-28.51%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 164,740.00 USD | 0.00 USD | 420.39 USD | `-27.79%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 164,320.00 USD | 0.00 USD | 191.53 USD | `-26.72%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 164,130.00 USD | 0.00 USD | 41,790.00 USD | `-26.37%` | `202,387,000,000.00` |
| `Live` | `Long` | `210.50` | 122,340.00 USD | 0.00 USD | 108.83 USD | `-24.94%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 122,230.00 USD | 0.00 USD | 634.50 USD | `-24.58%` | `3,000,000,000.00` |
| `Live` | `Long` | `213.50` | 121,590.00 USD | 0.00 USD | 3,800.00 USD | `-23.87%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 117,790.00 USD | 0.00 USD | 239.85 USD | `-23.16%` | `1,113,000,000.00` |
| `Live` | `Long` | `222.50` | 117,550.00 USD | 0.00 USD | 7,010.00 USD | `-20.66%` | `31,500,000,000.00` |
| `Live` | `Long` | `223.50` | 110,540.00 USD | 0.00 USD | 31,290.00 USD | `-20.30%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 79,250.00 USD | 0.00 USD | 5,830.00 USD | `-19.95%` | `25,951,000,000.00` |
| `Live` | `Long` | `226.50` | 73,430.00 USD | 0.00 USD | 1,240.00 USD | `-19.23%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 72,190.00 USD | 0.00 USD | 174.49 USD | `-18.88%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 72,020.00 USD | 0.00 USD | 642.77 USD | `-18.52%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 71,370.00 USD | 0.00 USD | 114.75 USD | `-18.16%` | `500,000,000.00` |
| `Live` | `Long` | `230.50` | 71,260.00 USD | 0.00 USD | 1,190.00 USD | `-17.81%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 70,070.00 USD | 0.00 USD | 295.86 USD | `-17.45%` | `1,278,000,000.00` |
| `Live` | `Long` | `234.50` | 69,770.00 USD | 0.00 USD | 637.61 USD | `-16.38%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 69,130.00 USD | 0.00 USD | 23,750.00 USD | `-15.31%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 45,380.00 USD | 0.00 USD | 10,840.00 USD | `-14.96%` | `45,467,000,000.00` |
| `Live` | `Long` | `239.50` | 34,540.00 USD | 0.00 USD | 1,030.00 USD | `-14.60%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 33,510.00 USD | 0.00 USD | 251.88 USD | `-13.89%` | `1,043,000,000.00` |
| `Live` | `Long` | `243.50` | 33,260.00 USD | 0.00 USD | 3,380.00 USD | `-13.17%` | `13,865,000,000.00` |
| `Live` | `Long` | `244.50` | 29,890.00 USD | 0.00 USD | 4,220.00 USD | `-12.82%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 25,660.00 USD | 0.00 USD | 1,030.00 USD | `-12.46%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,630.00 USD | 0.00 USD | 106.67 USD | `-11.75%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,530.00 USD | 0.00 USD | 595.16 USD | `-11.39%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 23,930.00 USD | 0.00 USD | 1,330.00 USD | `-10.68%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,610.00 USD | 0.00 USD | 268.35 USD | `-10.32%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 22,340.00 USD | 0.00 USD | 1,030.00 USD | `-9.96%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 21,310.00 USD | 0.00 USD | 548.45 USD | `-9.25%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 20,760.00 USD | 0.00 USD | 3,210.00 USD | `-8.54%` | `12,514,000,000.00` |
| `Live` | `Long` | `258.50` | 17,550.00 USD | 0.00 USD | 645.99 USD | `-7.82%` | `2,499,000,000.00` |
| `Live` | `Long` | `260.50` | 16,900.00 USD | 0.00 USD | 3,340.00 USD | `-7.11%` | `12,839,000,000.00` |
| `Live` | `Long` | `263.50` | 13,560.00 USD | 0.00 USD | 464.81 USD | `-6.04%` | `1,764,000,000.00` |
| `Live` | `Long` | `270.50` | 13,090.00 USD | 0.00 USD | 13,090.00 USD | `-3.54%` | `48,404,000,000.00` |
| `Live` | `Short` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | `+2.52%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 1,070.00 USD | 954.95 USD | 0.00 USD | `+3.94%` | `3,276,000,000.00` |
| `Live` | `Short` | `292.50` | 7,110.00 USD | 6,050.00 USD | 0.00 USD | `+4.30%` | `20,668,000,000.00` |
| `Live` | `Short` | `302.50` | 10,760.00 USD | 3,640.00 USD | 0.00 USD | `+7.87%` | `12,043,000,000.00` |
| `Live` | `Short` | `320.50` | 11,860.00 USD | 1,110.00 USD | 0.00 USD | `+14.28%` | `3,452,000,000.00` |
| `Live` | `Short` | `324.50` | 14,090.00 USD | 2,220.00 USD | 0.00 USD | `+15.71%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 39,610.00 USD | 25,530.00 USD | 0.00 USD | `+16.42%` | `78,189,000,000.00` |
| `Live` | `Short` | `338.50` | 40,970.00 USD | 1,350.00 USD | 0.00 USD | `+20.70%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 41,980.00 USD | 1,010.00 USD | 0.00 USD | `+27.83%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 42,420.00 USD | 445.52 USD | 0.00 USD | `+31.40%` | `1,209,000,000.00` |
| `Live` | `Short` | `373.50` | 83,510.00 USD | 41,090.00 USD | 0.00 USD | `+33.18%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 94,150.00 USD | 10,640.00 USD | 0.00 USD | `+44.95%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 140,400.00 USD | 46,250.00 USD | 0.00 USD | `+63.85%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 141,120.00 USD | 718.34 USD | 0.00 USD | `+77.76%` | `1,441,000,000.00` |
| `Live` | `Short` | `535.50` | 141,470.00 USD | 348.61 USD | 0.00 USD | `+90.95%` | `651,000,000.00` |
| `Live` | `Short` | `560.50` | 142,310.00 USD | 842.43 USD | 0.00 USD | `+99.86%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 458,730.00 USD | 0.00 USD | 210.94 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 458,520.00 USD | 0.00 USD | 2,070.00 USD | `-48.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 456,450.00 USD | 0.00 USD | 489.38 USD | `-40.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 455,960.00 USD | 0.00 USD | 2,530.00 USD | `-36.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 453,430.00 USD | 0.00 USD | 490.59 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 452,940.00 USD | 0.00 USD | 482.01 USD | `-29.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 452,460.00 USD | 0.00 USD | 189.07 USD | `-28.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 452,270.00 USD | 0.00 USD | 441.60 USD | `-25.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 451,830.00 USD | 0.00 USD | 299.96 USD | `-24.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 451,530.00 USD | 0.00 USD | 715.29 USD | `-24.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 450,810.00 USD | 0.00 USD | 638.36 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 450,180.00 USD | 0.00 USD | 740.85 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 449,440.00 USD | 0.00 USD | 478.48 USD | `-18.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 448,960.00 USD | 0.00 USD | 389.48 USD | `-16.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 448,570.00 USD | 0.00 USD | 812.38 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 447,760.00 USD | 0.00 USD | 220.64 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 447,530.00 USD | 0.00 USD | 429.30 USD | `-14.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 447,110.00 USD | 0.00 USD | 296.50 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 446,810.00 USD | 0.00 USD | 216.45 USD | `-14.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 446,590.00 USD | 0.00 USD | 387.76 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 446,200.00 USD | 0.00 USD | 18,080.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 428,120.00 USD | 0.00 USD | 1,630.00 USD | `-12.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 426,500.00 USD | 0.00 USD | 2,700.00 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 423,800.00 USD | 0.00 USD | 2,940.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 420,850.00 USD | 0.00 USD | 4,560.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 416,290.00 USD | 0.00 USD | 1,850.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 414,450.00 USD | 0.00 USD | 231.54 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 414,220.00 USD | 0.00 USD | 109.26 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 414,110.00 USD | 0.00 USD | 1,780.00 USD | `-8.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 412,330.00 USD | 0.00 USD | 51,300.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 361,030.00 USD | 0.00 USD | 250.81 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 360,780.00 USD | 0.00 USD | 2,370.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 358,410.00 USD | 0.00 USD | 269,800.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 88,610.00 USD | 0.00 USD | 3,600.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 85,010.00 USD | 0.00 USD | 199.17 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 84,810.00 USD | 0.00 USD | 2,180.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 82,640.00 USD | 0.00 USD | 241.98 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 82,390.00 USD | 0.00 USD | 219.35 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 82,170.00 USD | 0.00 USD | 107.40 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 82,070.00 USD | 0.00 USD | 29,530.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 52,540.00 USD | 0.00 USD | 3,340.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 49,200.00 USD | 0.00 USD | 620.38 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 48,580.00 USD | 0.00 USD | 13,500.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 35,080.00 USD | 0.00 USD | 136.20 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 34,940.00 USD | 0.00 USD | 667.86 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 34,280.00 USD | 0.00 USD | 275.50 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 34,000.00 USD | 0.00 USD | 6,640.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 27,360.00 USD | 0.00 USD | 326.34 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 27,030.00 USD | 0.00 USD | 5,040.00 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 21,990.00 USD | 0.00 USD | 21,990.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 139.69 USD | 139.69 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 3,240.00 USD | 3,100.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 6,180.00 USD | 2,940.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 14,220.00 USD | 8,040.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 14,360.00 USD | 137.98 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 15,410.00 USD | 1,050.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 15,690.00 USD | 280.77 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 22,600.00 USD | 6,910.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 22,860.00 USD | 261.96 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 23,390.00 USD | 530.36 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 23,600.00 USD | 212.36 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 48,880.00 USD | 25,280.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 49,050.00 USD | 167.89 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 50,040.00 USD | 992.62 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 52,060.00 USD | 2,020.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 56,790.00 USD | 4,730.00 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 56,900.00 USD | 110.37 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 57,290.00 USD | 388.95 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 57,440.00 USD | 153.94 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 68,220.00 USD | 10,780.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 73,320.00 USD | 5,110.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 84,050.00 USD | 10,730.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 86,700.00 USD | 2,650.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 86,980.00 USD | 282.89 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 101,480.00 USD | 14,500.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 102,110.00 USD | 634.04 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 103,150.00 USD | 1,030.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 108,800.00 USD | 5,650.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 109,330.00 USD | 534.59 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 109,650.00 USD | 321.50 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 176,370.00 USD | 66,720.00 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 177,460.00 USD | 1,090.00 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 189,450.00 USD | 12,000.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 190,000.00 USD | 547.52 USD | 0.00 USD | `+21.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 190,110.00 USD | 110.91 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 190,370.00 USD | 257.45 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 190,540.00 USD | 174.25 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 190,700.00 USD | 151.50 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 192,150.00 USD | 1,450.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 193,920.00 USD | 1,770.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 194,250.00 USD | 326.07 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 195,080.00 USD | 826.60 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 202,520.00 USD | 7,440.00 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 203,200.00 USD | 682.84 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 204,300.00 USD | 1,100.00 USD | 0.00 USD | `+36.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 204,990.00 USD | 683.96 USD | 0.00 USD | `+41.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 205,190.00 USD | 199.75 USD | 0.00 USD | `+42.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 206,680.00 USD | 1,490.00 USD | 0.00 USD | `+42.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 207,720.00 USD | 1,040.00 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 208,090.00 USD | 376.71 USD | 0.00 USD | `+44.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 208,250.00 USD | 158.86 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 214,150.00 USD | 5,900.00 USD | 0.00 USD | `+48.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 215,230.00 USD | 1,080.00 USD | 0.00 USD | `+51.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 216,930.00 USD | 1,700.00 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 218,490.00 USD | 1,550.00 USD | 0.00 USD | `+53.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 219,870.00 USD | 1,380.00 USD | 0.00 USD | `+55.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 220,490.00 USD | 621.14 USD | 0.00 USD | `+55.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 222,770.00 USD | 2,280.00 USD | 0.00 USD | `+57.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 222,990.00 USD | 222.75 USD | 0.00 USD | `+58.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 229,910.00 USD | 6,920.00 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 235,830.00 USD | 5,920.00 USD | 0.00 USD | `+61.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 236,960.00 USD | 1,130.00 USD | 0.00 USD | `+64.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 244,590.00 USD | 7,630.00 USD | 0.00 USD | `+72.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 245,570.00 USD | 975.00 USD | 0.00 USD | `+73.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 246,550.00 USD | 981.00 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 247,050.00 USD | 499.50 USD | 0.00 USD | `+78.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,130,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+78.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,130,000.00 USD | 1,000.00 USD | 0.00 USD | `+78.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,140,000.00 USD | 1,040.00 USD | 0.00 USD | `+84.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,140,000.00 USD | 340.67 USD | 0.00 USD | `+86.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,140,000.00 USD | 638.86 USD | 0.00 USD | `+98.44%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.80` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD |
| `7D` | `235.30` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `236.30` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `236.80` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD |
| `7D` | `237.30` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD |
| `7D` | `238.30` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD |
| `7D` | `238.80` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.30` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD |
| `7D` | `240.80` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.30` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD |
| `7D` | `243.30` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.30` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD |
| `7D` | `247.30` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.80` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD |
| `7D` | `248.30` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD |
| `7D` | `248.80` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD |
| `7D` | `249.30` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD |
| `7D` | `249.80` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD |
| `7D` | `250.30` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD |
| `1D` | `250.50` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 13,910.00 USD | 7,600.00 USD | 12,280.00 USD |
| `7D` | `250.80` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD |
| `1D` | `250.90` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD |
| `1D` | `251.30` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 26,350.00 USD | 24,910.00 USD | 23,590.00 USD |
| `7D` | `251.30` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,120.00 USD |
| `1D` | `251.70` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 30,050.00 USD | 53,570.00 USD | 14,600.00 USD |
| `7D` | `251.80` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,360.00 USD |
| `1D` | `252.10` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 20,730.00 USD | 8,350.00 USD | 12,960.00 USD |
| `7D` | `252.30` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 69,530.00 USD | 39,900.00 USD | 17,360.00 USD |
| `1D` | `252.50` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 10,950.00 USD | 1,620.00 USD | 6,000.00 USD |
| `7D` | `252.80` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD |
| `1D` | `252.90` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 3,030.00 USD | 6,970.00 USD | 2,170.00 USD |
| `1D` | `253.30` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 12,480.00 USD | 8,710.00 USD | 14,780.00 USD |
| `7D` | `253.30` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,250.00 USD |
| `1D` | `253.70` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 21,830.00 USD | 15,190.00 USD | 11,050.00 USD |
| `7D` | `253.80` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD |
| `1D` | `254.10` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 1,590.00 USD | 7,170.00 USD | 5,820.00 USD |
| `7D` | `254.30` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,090.00 USD |
| `1D` | `254.50` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 8,310.00 USD | 10,840.00 USD | 35.81 USD |
| `7D` | `254.80` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,360.00 USD |
| `1D` | `254.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 9,050.00 USD | 10,890.00 USD | 24.94 USD |
| `1D` | `255.30` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 9,910.00 USD | 15,540.00 USD | 28,000.00 USD |
| `7D` | `255.30` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,560.00 USD |
| `1D` | `255.70` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 14,640.00 USD | 23,250.00 USD | 11,800.00 USD |
| `7D` | `255.80` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD |
| `1D` | `256.10` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD |
| `7D` | `256.30` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,910.00 USD |
| `1D` | `256.50` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD |
| `7D` | `256.80` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,360.00 USD |
| `1D` | `256.90` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,300.00 USD |
| `1D` | `257.30` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD |
| `7D` | `257.30` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD |
| `1D` | `257.70` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD |
| `7D` | `257.80` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD |
| `7D` | `258.30` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD |
| `1D` | `258.50` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.80` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD |
| `1D` | `258.90` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,030.00 USD |
| `1D` | `259.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD |
| `1D` | `259.70` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,300.00 USD |
| `7D` | `259.80` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD |
| `1D` | `260.10` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 39,530.00 USD | 8,640.00 USD | 6,870.00 USD |
| `7D` | `260.30` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,930.00 USD |
| `1D` | `260.50` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 19,010.00 USD | 1,900.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,280.00 USD |
| `1D` | `260.90` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 8,950.00 USD | 50,950.00 USD | 13,940.00 USD |
| `1D` | `261.30` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 8,220.00 USD | 29,340.00 USD | 33,400.00 USD |
| `7D` | `261.30` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,540.00 USD |
| `1D` | `261.70` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 15,340.00 USD | 60,640.00 USD | 51,230.00 USD |
| `7D` | `261.80` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD |
| `1D` | `262.10` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 13,620.00 USD | 27,450.00 USD | 21,370.00 USD |
| `7D` | `262.30` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD |
| `1D` | `262.50` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 21,110.00 USD | 4,750.00 USD | 10,850.00 USD |
| `7D` | `262.80` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,760.00 USD |
| `1D` | `262.90` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 629.76 USD | 12,630.00 USD | 19,500.00 USD |
| `1D` | `263.30` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 9,930.00 USD | 4,350.00 USD | 61,500.00 USD |
| `7D` | `263.30` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 33,590.00 USD | 13,710.00 USD | 169.66 USD |
| `1D` | `263.70` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,370.00 USD |
| `7D` | `263.80` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,890.00 USD |
| `1D` | `264.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,270.00 USD |
| `7D` | `264.30` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 48,230.00 USD | 1,170.00 USD | 128.94 USD |
| `1D` | `264.50` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,200.00 USD | 19,920.00 USD | 4.35 USD |
| `7D` | `264.80` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 33,470.00 USD | 21,870.00 USD | 198.07 USD |
| `1D` | `264.90` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 33,390.00 USD | 2,170.00 USD | 53,310.00 USD |
| `1D` | `265.30` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 64,840.00 USD | 2,650.00 USD | 9.86 USD |
| `7D` | `265.30` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 256,440.00 USD | 2,330.00 USD | 34,040.00 USD |
| `1D` | `265.70` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 629.76 USD | 6.46 USD |
| `7D` | `265.80` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 69,380.00 USD | 0.00 USD | 106.95 USD |
| `1D` | `266.10` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 16,330.00 USD | 13,320.00 USD | 0.00 USD |
| `7D` | `266.30` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 216,090.00 USD | 645.20 USD | 17.82 USD |
| `1D` | `266.50` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 14,430.00 USD | 8,470.00 USD | 4,800.00 USD |
| `7D` | `266.80` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD |
| `1D` | `266.90` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 18,330.00 USD | 22,420.00 USD | 0.00 USD |
| `1D` | `267.30` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 33,460.00 USD | 68,530.00 USD | 12,550.00 USD |
| `7D` | `267.30` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD |
| `1D` | `267.70` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 10,330.00 USD | 36,260.00 USD | 28,720.00 USD |
| `7D` | `267.80` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,920.00 USD |
| `1D` | `268.10` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 18,930.00 USD | 28,480.00 USD | 60,070.00 USD |
| `7D` | `268.30` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,720.00 USD |
| `1D` | `268.50` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 18,310.00 USD | 18,920.00 USD | 67.34 USD |
| `7D` | `268.80` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 23,340.00 USD | 17,480.00 USD | 105.78 USD |
| `1D` | `268.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 21,330.00 USD | 11,500.00 USD | 182.87 USD |
| `1D` | `269.30` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 7,610.00 USD | 1,120.00 USD | 6,270.00 USD |
| `7D` | `269.30` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 3,490.00 USD | 148.23 USD |
| `1D` | `269.70` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 6,500.00 USD | 17,350.00 USD | 13,710.00 USD |
| `7D` | `269.80` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 0.00 USD | 1,920.00 USD | 240.42 USD |
| `1D` | `270.10` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD |
| `7D` | `270.30` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD |
| `1D` | `270.50` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 42,710.00 USD | 118.00 USD | 0.00 USD |
| `7D` | `270.80` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 33,050.00 USD | 0.00 USD | 120.25 USD |
| `1D` | `270.90` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 505.00 USD | 14,830.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 12,710.00 USD | 1,780.00 USD | 11,730.00 USD |
| `7D` | `271.30` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.70` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 8,650.00 USD | 34,920.00 USD | 5,300.00 USD |
| `7D` | `271.80` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD |
| `1D` | `272.10` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 21,980.00 USD | 21,380.00 USD | 19,770.00 USD |
| `7D` | `272.30` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 6,060.00 USD | 38,280.00 USD | 41,840.00 USD |
| `7D` | `272.80` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `272.90` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 59,390.00 USD | 5,420.00 USD | 71,640.00 USD |
| `1D` | `273.30` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 28,730.00 USD | 121,350.00 USD | 40,460.00 USD |
| `7D` | `273.30` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD |
| `1D` | `273.70` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 69,050.00 USD | 67,190.00 USD | 69,750.00 USD |
| `7D` | `273.80` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.10` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 165,910.00 USD | 37,550.00 USD | 12,160.00 USD |
| `7D` | `274.30` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 186,780.00 USD | 21,440.00 USD | 54,030.00 USD |
| `7D` | `274.80` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `274.90` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 47,590.00 USD | 19,960.00 USD | 12,550.00 USD |
| `1D` | `275.30` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 11,720.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `275.30` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.70` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD |
| `7D` | `275.80` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD |
| `1D` | `276.10` | 917,560.00 USD | 0.00 USD | 917,560.00 USD | 161,250.00 USD | 3,340.00 USD | 7,090.00 USD |
| `7D` | `276.30` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 745,880.00 USD | 0.00 USD | 745,880.00 USD | 11,920.00 USD | 5,230.00 USD | 8,810.00 USD |
| `7D` | `276.80` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 719,920.00 USD | 0.00 USD | 719,920.00 USD | 37,290.00 USD | 25,410.00 USD | 23,460.00 USD |
| `1D` | `277.30` | 633,750.00 USD | 0.00 USD | 633,750.00 USD | 17,610.00 USD | 18,260.00 USD | 10,600.00 USD |
| `7D` | `277.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 152,190.00 USD | 77,800.00 USD | 140,900.00 USD |
| `1D` | `277.70` | 587,280.00 USD | 0.00 USD | 587,280.00 USD | 13,750.00 USD | 10,950.00 USD | 20,300.00 USD |
| `7D` | `277.80` | 743,120.00 USD | 0.00 USD | 743,120.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD |
| `1D` | `278.10` | 542,280.00 USD | 0.00 USD | 542,280.00 USD | 12,120.00 USD | 97,470.00 USD | 83,650.00 USD |
| `7D` | `278.30` | 525,530.00 USD | 0.00 USD | 525,530.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD |
| `1D` | `278.50` | 349,030.00 USD | 0.00 USD | 349,030.00 USD | 78,720.00 USD | 56,870.00 USD | 47,870.00 USD |
| `7D` | `278.80` | 308,370.00 USD | 0.00 USD | 308,370.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `278.90` | 165,580.00 USD | 0.00 USD | 165,580.00 USD | 19,260.00 USD | 10,830.00 USD | 0.00 USD |
| `1D` | `279.30` | 135,480.00 USD | 0.00 USD | 135,480.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD |
| `7D` | `279.30` | 238,000.00 USD | 0.00 USD | 238,000.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 94,400.00 USD | 0.00 USD | 94,400.00 USD | 0.00 USD | 0.00 USD | 24,310.00 USD |
| `1D` | `280.10` | 70,080.00 USD | 0.00 USD | 70,080.00 USD | 0.00 USD | 0.00 USD | 31,340.00 USD |
| `1D` | `280.50` | 38,750.00 USD | 0.00 USD | 38,750.00 USD | 0.00 USD | 38,740.00 USD | 12.06 USD |
| `1D` | `280.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `280.80` | 235,340.00 USD | 0.00 USD | 235,340.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `280.90` | 17,460.00 USD | 17,460.00 USD | 0.00 USD | 0.00 USD | 17,450.00 USD | 12.68 USD |
| `7D` | `281.30` | 219,800.00 USD | 0.00 USD | 219,800.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `7D` | `281.80` | 122,390.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 29,870.00 USD | 29,870.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 4,140.00 USD |
| `7D` | `282.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.30` | 24,220.00 USD | 24,220.00 USD | 0.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `283.30` | 31,160.00 USD | 31,160.00 USD | 0.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD |
| `7D` | `283.30` | 27,670.00 USD | 27,670.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.80` | 29,670.00 USD | 29,670.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.30` | 31,230.00 USD | 31,230.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.50` | 69,360.00 USD | 69,360.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | 27,570.00 USD |
| `7D` | `284.80` | 86,620.00 USD | 86,620.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD |
| `1D` | `284.90` | 105,720.00 USD | 105,720.00 USD | 0.00 USD | 28,720.00 USD | 7,620.00 USD | 9.04 USD |
| `1D` | `285.30` | 200,330.00 USD | 200,330.00 USD | 0.00 USD | 36,620.00 USD | 16,320.00 USD | 41,680.00 USD |
| `7D` | `285.30` | 508,580.00 USD | 508,580.00 USD | 0.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD |
| `1D` | `285.70` | 249,340.00 USD | 249,340.00 USD | 0.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD |
| `7D` | `285.80` | 742,130.00 USD | 742,130.00 USD | 0.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD |
| `1D` | `286.10` | 312,620.00 USD | 312,620.00 USD | 0.00 USD | 26,810.00 USD | 719.80 USD | 35,760.00 USD |
| `7D` | `286.30` | 786,350.00 USD | 786,350.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD |
| `1D` | `286.50` | 359,680.00 USD | 359,680.00 USD | 0.00 USD | 15,270.00 USD | 1,650.00 USD | 30,140.00 USD |
| `7D` | `286.80` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 514,540.00 USD | 514,540.00 USD | 0.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD |
| `1D` | `287.30` | 690,070.00 USD | 690,070.00 USD | 0.00 USD | 97,970.00 USD | 43,890.00 USD | 33,670.00 USD |
| `7D` | `287.30` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD |
| `1D` | `287.70` | 785,290.00 USD | 785,290.00 USD | 0.00 USD | 22,860.00 USD | 22,500.00 USD | 49,860.00 USD |
| `7D` | `287.80` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.10` | 867,210.00 USD | 867,210.00 USD | 0.00 USD | 21,420.00 USD | 26,660.00 USD | 33,850.00 USD |
| `7D` | `288.30` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD |
| `1D` | `288.50` | 974,760.00 USD | 974,760.00 USD | 0.00 USD | 52,260.00 USD | 26,060.00 USD | 29,220.00 USD |
| `7D` | `288.80` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD |
| `1D` | `288.90` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 44,740.00 USD | 24,620.00 USD | 17.54 USD |
| `1D` | `289.30` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 17,220.00 USD | 47,120.00 USD | 51,210.00 USD |
| `7D` | `289.30` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.70` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 52,150.00 USD | 67,790.00 USD | 92,100.00 USD |
| `7D` | `289.80` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD |
| `1D` | `290.10` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 65,110.00 USD | 51,750.00 USD | 114,510.00 USD |
| `7D` | `290.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 28,010.00 USD | 120,130.00 USD | 46,650.00 USD |
| `7D` | `290.80` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD |
| `1D` | `290.90` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD |
| `1D` | `291.30` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 27,020.00 USD | 12,070.00 USD | 24,320.00 USD |
| `7D` | `291.30` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD |
| `1D` | `291.70` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 9,470.00 USD | 23,560.00 USD | 28,440.00 USD |
| `7D` | `291.80` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 6,710.00 USD | 37,580.00 USD | 11,510.00 USD |
| `7D` | `292.30` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD |
| `1D` | `292.50` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 29,880.00 USD | 3,650.00 USD | 2,240.00 USD |
| `7D` | `292.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 138.60 USD |
| `1D` | `292.90` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 62,580.00 USD | 30,990.00 USD | 3,560.00 USD |
| `1D` | `293.30` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 22,320.00 USD | 18,040.00 USD | 27,380.00 USD |
| `7D` | `293.30` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 33,580.00 USD | 132,770.00 USD | 91.25 USD |
| `1D` | `293.70` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 76,520.00 USD | 47,640.00 USD | 64,930.00 USD |
| `7D` | `293.80` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 20,950.00 USD |
| `1D` | `294.10` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 21,480.00 USD | 23,760.00 USD | 49,210.00 USD |
| `7D` | `294.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD |
| `1D` | `294.50` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 96,690.00 USD | 76,870.00 USD | 85,210.00 USD |
| `7D` | `294.80` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD |
| `1D` | `294.90` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 33,360.00 USD | 16,240.00 USD | 48,700.00 USD |
| `1D` | `295.30` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 15,750.00 USD | 60,930.00 USD | 96,730.00 USD |
| `7D` | `295.30` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 46,330.00 USD | 82,780.00 USD | 345,510.00 USD |
| `1D` | `295.70` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 98,960.00 USD | 6,830.00 USD | 128,460.00 USD |
| `7D` | `295.80` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 165,320.00 USD | 82,100.00 USD | 197,410.00 USD |
| `1D` | `296.10` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 52,840.00 USD | 126,740.00 USD | 35,670.00 USD |
| `7D` | `296.30` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 43,710.00 USD | 167,940.00 USD | 120,880.00 USD |
| `1D` | `296.50` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 33,300.00 USD | 22,420.00 USD | 41,260.00 USD |
| `7D` | `296.80` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 133,820.00 USD | 3,570.00 USD | 201,420.00 USD |
| `1D` | `296.90` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 24,280.00 USD | 21,780.00 USD | 90,450.00 USD |
| `1D` | `297.30` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 61,380.00 USD | 1,000.00 USD | 31,540.00 USD |
| `7D` | `297.30` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 78,980.00 USD | 54,960.00 USD | 72.03 USD |
| `1D` | `297.70` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 15,840.00 USD | 11,340.00 USD | 12,070.00 USD |
| `7D` | `297.80` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 47,530.00 USD | 99,810.00 USD | 89,650.00 USD |
| `1D` | `298.10` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 51,840.00 USD | 10,000.00 USD | 41,710.00 USD |
| `7D` | `298.30` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 32,650.00 USD | 45,150.00 USD | 68,810.00 USD |
| `1D` | `298.50` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 5,730.00 USD | 1,480.00 USD | 56,410.00 USD |
| `7D` | `298.80` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 112.32 USD |
| `1D` | `298.90` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 28,240.00 USD | 5,580.00 USD | 94,670.00 USD |
| `1D` | `299.30` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 34,110.00 USD | 10,760.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD |
| `1D` | `299.70` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 8,250.00 USD | 10,790.00 USD | 27,680.00 USD |
| `7D` | `299.80` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 22,060.00 USD | 9,100.00 USD | 19,830.00 USD |
| `1D` | `300.10` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 19,900.00 USD | 36,560.00 USD | 64,300.00 USD |
| `7D` | `300.30` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD |
| `1D` | `300.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 23,270.00 USD | 1,560.00 USD | 17,190.00 USD |
| `7D` | `300.80` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,380.00 USD |
| `1D` | `300.90` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 269.05 USD | 1,020.00 USD | 29,460.00 USD |
| `1D` | `301.30` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 597.00 USD | 15,110.00 USD | 20,950.00 USD |
| `7D` | `301.30` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 73,320.00 USD | 58,690.00 USD | 150,430.00 USD |
| `1D` | `301.70` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 19,840.00 USD | 8,470.00 USD | 15,530.00 USD |
| `7D` | `301.80` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,370.00 USD |
| `1D` | `302.10` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 25,190.00 USD | 30,660.00 USD | 10,400.00 USD |
| `7D` | `302.30` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 1,560.00 USD | 181,550.00 USD | 35.08 USD |
| `1D` | `302.50` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 13,820.00 USD | 13,290.00 USD | 38,380.00 USD |
| `7D` | `302.80` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD |
| `1D` | `302.90` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 1,370.00 USD | 2,260.00 USD | 14,080.00 USD |
| `1D` | `303.30` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 21,200.00 USD | 2,760.00 USD | 9,360.00 USD |
| `7D` | `303.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD | 183.84 USD |
| `1D` | `303.70` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 391.16 USD | 1.44 USD |
| `7D` | `303.80` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD |
| `1D` | `304.10` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD |
| `1D` | `304.50` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 9,670.00 USD | 2,100.00 USD | 44,520.00 USD |
| `7D` | `304.80` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 35,470.00 USD | 11,790.00 USD | 4,050.00 USD |
| `1D` | `304.90` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD |
| `1D` | `305.30` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 83.23 USD | 172.52 USD | 7.48 USD |
| `7D` | `305.30` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD |
| `1D` | `305.70` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 6,340.00 USD | 3,500.00 USD | 5,870.00 USD |
| `7D` | `305.80` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD |
| `1D` | `306.10` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD |
| `1D` | `306.50` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 4,330.00 USD | 6.13 USD | 5,660.00 USD |
| `7D` | `306.80` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 94,690.00 USD | 74,510.00 USD | 70,010.00 USD |
| `1D` | `306.90` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 19,810.00 USD | 35,610.00 USD | 18,580.00 USD |
| `1D` | `307.30` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 11,250.00 USD | 40,340.00 USD | 22,610.00 USD |
| `7D` | `307.30` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 27,410.00 USD | 136,370.00 USD | 147,550.00 USD |
| `1D` | `307.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 27,000.00 USD | 25,340.00 USD | 4,060.00 USD |
| `7D` | `307.80` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 127,080.00 USD | 113,210.00 USD | 60,720.00 USD |
| `1D` | `308.10` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 19,140.00 USD | 7,600.00 USD | 12,900.00 USD |
| `7D` | `308.30` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 169,010.00 USD | 66,670.00 USD | 114,230.00 USD |
| `1D` | `308.50` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD |
| `7D` | `308.80` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD |
| `1D` | `308.90` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 7,450.00 USD | 5,890.00 USD | 3,480.00 USD |
| `1D` | `309.30` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 3,240.00 USD | 1,580.00 USD | 2,150.00 USD |
| `7D` | `309.30` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 34,260.00 USD | 36,030.00 USD | 36,580.00 USD |
| `1D` | `309.70` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 10,040.00 USD | 7,670.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,820.00 USD |
| `1D` | `310.10` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 14,750.00 USD | 3,980.00 USD | 11,040.00 USD |
| `7D` | `310.30` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 62,230.00 USD | 108,410.00 USD | 80,780.00 USD |
| `1D` | `310.50` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 112.30 USD | 5,020.00 USD | 5,800.00 USD |
| `7D` | `310.80` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 12,180.00 USD |
| `1D` | `310.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 5,080.00 USD | 73.70 USD | 13.75 USD |
| `1D` | `311.30` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 257.90 USD | 2,350.00 USD | 29.00 USD |
| `7D` | `311.30` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,860.00 USD |
| `1D` | `311.70` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 7,980.00 USD | 9,070.00 USD | 4,060.00 USD |
| `7D` | `311.80` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 19,570.00 USD | 11,240.00 USD | 25,560.00 USD |
| `1D` | `312.10` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 299.35 USD | 10,320.00 USD | 15,040.00 USD |
| `7D` | `312.30` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 27,420.00 USD |
| `1D` | `312.50` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 14,640.00 USD | 8,480.00 USD | 11,780.00 USD |
| `7D` | `312.80` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 21,990.00 USD | 14,880.00 USD | 19,390.00 USD |
| `1D` | `312.90` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD |
| `1D` | `313.30` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 3,580.00 USD | 18,130.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD |
| `1D` | `313.50` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `313.80` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 32,780.00 USD | 1,570.00 USD | 44,160.00 USD |
| `7D` | `314.30` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `7D` | `314.80` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `315.30` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 500.10 USD | 547.95 USD | 9.16 USD |
| `7D` | `315.80` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD |
| `7D` | `316.30` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD |
| `7D` | `316.80` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD |
| `7D` | `317.30` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD |
| `7D` | `317.80` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD |
| `7D` | `318.30` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `301.86M` | Total OI Tokens: `1,081,595.4 BCH`
  * 1h OI Change: `-0.86%` | 4h OI Change: `-2.20%` | 24h OI Change: `-1.15%`
  * Exchange Breakdown: Binance=`87.80M` | Bybit=`37.63M` | OKX=`23.58M` | Hyperliquid=`7.13M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.42K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0086%` |
| **USDT Bybit** | `-0.0103%` | **USDT KuCoin** | `0.0095%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0054%` | **USDT Bitget** | `0.0074%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `42.57%` | `57.43%` | `0.74` | 2,160,000.00 USD |
| `15M` | `Binance` | `56.7%` | `43.3%` | `1.31` | 483,630.00 USD |
| `15M` | `OKX` | `44.47%` | `55.53%` | `0.80` | 379,050.00 USD |
| `15M` | `Bybit` | `52.07%` | `47.93%` | `1.09` | 58,780.00 USD |
| `15M` | `KuCoin` | `49.15%` | `50.85%` | `0.97` | 37,180.00 USD |
| `15M` | `Gate` | `62.79%` | `37.21%` | `1.69` | 170,830.00 USD |
| `15M` | `Bitget` | `63.45%` | `36.55%` | `1.74` | 22,890.00 USD |
| `15M` | `BingX` | `44.5%` | `55.5%` | `0.80` | 644,230.00 USD |
| `15M` | `MEXC` | `39.87%` | `60.13%` | `0.66` | 37,460.00 USD |
| `15M` | `Bitunix` | `53.02%` | `46.98%` | `1.13` | 79,820.00 USD |
| `15M` | `Hyperliquid` | `54.69%` | `45.31%` | `1.21` | 11,550.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.47%` | `53.53%` | `0.87` | 50,940.00 USD |
| `15M` | `Crypto.com` | `50%` | `50%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 164,190.00 USD |
| `15M` | `HTX` | `22.02%` | `77.98%` | `0.28` | 804.27 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `4.44%` | `95.56%` | `0.05` | 19,520.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 201.30 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `99.98%` | `0.02%` | `4999.00` | 1,160.00 USD |
| `15M` | `Whale Positions` | `56.7%` | `43.3%` | `1.31` | 483,630.00 USD |
| `15M` | `Global Accounts` | `42.57%` | `57.43%` | `0.74` | 2,160,000.00 USD |
| `1H` | `BCH` | `45.44%` | `54.56%` | `0.83` | 9,070,000.00 USD |
| `1H` | `Binance` | `43.01%` | `56.99%` | `0.75` | 1,970,000.00 USD |
| `1H` | `OKX` | `43.37%` | `56.63%` | `0.77` | 626,580.00 USD |
| `1H` | `Bybit` | `44.35%` | `55.65%` | `0.80` | 317,610.00 USD |
| `1H` | `KuCoin` | `49.23%` | `50.77%` | `0.97` | 372,070.00 USD |
| `1H` | `Gate` | `53.46%` | `46.54%` | `1.15` | 105,840.00 USD |
| `1H` | `Bitget` | `65.08%` | `34.92%` | `1.86` | 148,470.00 USD |
| `1H` | `BingX` | `14.72%` | `85.28%` | `0.17` | 1,160,000.00 USD |
| `1H` | `MEXC` | `35.98%` | `64.02%` | `0.56` | 297,110.00 USD |
| `1H` | `Bitunix` | `51.28%` | `48.72%` | `1.05` | 171,030.00 USD |
| `1H` | `Hyperliquid` | `15.95%` | `84.05%` | `0.19` | 114,980.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.82%` | `50.18%` | `0.99` | 2,870,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 675,350.00 USD |
| `1H` | `HTX` | `57.92%` | `42.08%` | `1.38` | 7,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `11.14%` | `88.86%` | `0.13` | 219,110.00 USD |
| `1H` | `Aster` | `32.94%` | `67.06%` | `0.49` | 1,640.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.12%` | `52.88%` | `0.89` | 9,360.00 USD |
| `1H` | `Whale Positions` | `43.01%` | `56.99%` | `0.75` | 1,970,000.00 USD |
| `1H` | `Global Accounts` | `45.44%` | `54.56%` | `0.83` | 9,070,000.00 USD |
| `4H` | `BCH` | `43.85%` | `56.15%` | `0.78` | 50,210,000.00 USD |
| `4H` | `Binance` | `47.49%` | `52.51%` | `0.90` | 16,470,000.00 USD |
| `4H` | `OKX` | `51.65%` | `48.35%` | `1.07` | 9,080,000.00 USD |
| `4H` | `Bybit` | `51.43%` | `48.57%` | `1.06` | 4,450,000.00 USD |
| `4H` | `KuCoin` | `49.38%` | `50.62%` | `0.98` | 2,310,000.00 USD |
| `4H` | `Gate` | `51.44%` | `48.56%` | `1.06` | 1,100,000.00 USD |
| `4H` | `Bitget` | `45.14%` | `54.86%` | `0.82` | 1,390,000.00 USD |
| `4H` | `BingX` | `9.05%` | `90.95%` | `0.10` | 3,440,000.00 USD |
| `4H` | `MEXC` | `40.49%` | `59.51%` | `0.68` | 844,100.00 USD |
| `4H` | `Bitunix` | `42.36%` | `57.64%` | `0.73` | 928,320.00 USD |
| `4H` | `Hyperliquid` | `51.56%` | `48.44%` | `1.06` | 406,870.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.27%` | `48.73%` | `1.05` | 6,870,000.00 USD |
| `4H` | `Crypto.com` | `3.55%` | `96.45%` | `0.04` | 3,660.00 USD |
| `4H` | `WhiteBIT` | `2.24%` | `97.76%` | `0.02` | 2,780,000.00 USD |
| `4H` | `HTX` | `44.47%` | `55.53%` | `0.80` | 32,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `17.54%` | `82.46%` | `0.21` | 46,260.00 USD |
| `4H` | `Aster` | `22.32%` | `77.68%` | `0.29` | 30,790.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.55%` | `49.45%` | `1.02` | 20,720.00 USD |
| `4H` | `Whale Positions` | `47.49%` | `52.51%` | `0.90` | 16,470,000.00 USD |
| `4H` | `Global Accounts` | `43.85%` | `56.15%` | `0.78` | 50,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `284.25` | `284.51` | `284.25` | `284.85` | `284.24` | 356,795.30 USD | 184,835.04 USD | 171,960.26 USD | 12,874.78 USD | `+3.61%` | `14B / 15S` |
| `0:00 UTC` | `282.15` | `283.00` | `282.15` | `284.87` | `281.41` | 1,285,912.66 USD | 419,903.43 USD | 866,009.23 USD | -446,105.80 USD | `-34.69%` | `7B / 53S` |
| `5:00 UTC` | `281.32` | `281.51` | `281.32` | `282.72` | `280.80` | 1,039,042.65 USD | 453,949.26 USD | 585,093.39 USD | -131,144.13 USD | `-12.62%` | `25B / 59S` |
| `0:00 UTC` | `281.50` | `282.15` | `281.50` | `283.26` | `281.24` | 1,246,277.92 USD | 838,584.24 USD | 407,693.68 USD | 430,890.56 USD | `+34.57%` | `32B / 6S` |
| `5:00 UTC` | `283.12` | `282.91` | `283.12` | `283.64` | `281.86` | 898,717.53 USD | 422,080.39 USD | 476,637.13 USD | -54,556.74 USD | `-6.07%` | `22B / 36S` |
| `0:00 UTC` | `280.81` | `281.09` | `280.81` | `281.94` | `280.02` | 959,751.07 USD | 348,775.30 USD | 610,975.78 USD | -262,200.48 USD | `-27.32%` | `10B / 71S` |
| `5:00 UTC` | `278.88` | `279.51` | `278.88` | `280.56` | `278.74` | 1,525,848.29 USD | 843,855.80 USD | 681,992.49 USD | 161,863.30 USD | `+10.61%` | `26B / 51S` |
| `0:00 UTC` | `281.21` | `280.32` | `281.21` | `281.29` | `278.55` | 1,960,555.94 USD | 896,979.92 USD | 1,063,576.02 USD | -166,596.10 USD | `-8.50%` | `26B / 22S` |
| `5:00 UTC` | `279.18` | `279.58` | `279.18` | `280.70` | `279.06` | 617,038.04 USD | 332,886.00 USD | 284,152.04 USD | 48,733.95 USD | `+7.90%` | `32B / 38S` |
| `0:00 UTC` | `279.30` | `281.05` | `279.30` | `282.30` | `278.88` | 1,623,489.16 USD | 750,676.11 USD | 872,813.05 USD | -122,136.94 USD | `-7.52%` | `40B / 30S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 1` | `Divergence` | **`BEARISH`** | Rally without taker buying | `294.56` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.50` | 3,900.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `295.29` | 0.00 USD | 0.00 USD |
| `10-28 16:40` | `Range 1` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `296.45` | 2,100.00 USD | 0.00 USD |
| `10-28 16:31` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.73` | 1,000.00 USD | 0.00 USD |
| `10-28 15:58` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `300.99` | 0.00 USD | 0.00 USD |
| `10-28 15:25` | `Volume 10K BCH` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `304.75` | 0.00 USD | 0.00 USD |
| `10-28 12:36` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.11` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Volume 10K BCH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,500.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `298.39` | 0.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,100.00 USD | 0.00 USD |
| `10-28 11:32` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `298.10` | 0.00 USD | 0.00 USD |
| `10-28 11:24` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.42` | 0.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.64` | 1,000.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `299.34` | 1,200.00 USD | 0.00 USD |
| `10-28 09:12` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.13` | 0.00 USD | 0.00 USD |
| `10-28 08:27` | `Range 1` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `297.20` | 0.00 USD | 0.00 USD |
| `10-28 07:51` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.25` | 2,500.00 USD | 0.00 USD |
| `10-28 07:41` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `295.18` | 0.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 10K BCH` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `293.94` | 2,400.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.42` | 0.00 USD | 0.00 USD |
| `10-28 06:21` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.97` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 5,490.00 USD | 109,590.00 USD | **`ACCUMULATION`** |
| `15m` | -450.35 USD | 15,620.00 USD | **`ACCUMULATION`** |
| `30m` | -4,290.00 USD | 5,790.00 USD | **`ACCUMULATION`** |
| `1h` | -212,580.00 USD | -560,950.00 USD | **`DISTRIBUTION`** |
| `2h` | -207,990.00 USD | -488,760.00 USD | **`DISTRIBUTION`** |
| `4h` | 55,550.00 USD | -289,650.00 USD | **`DISTRIBUTION`** |
| `6h` | 662,520.00 USD | 283,870.00 USD | **`ACCUMULATION`** |
| `8h` | 1,040,000.00 USD | 1,750,000.00 USD | **`ACCUMULATION`** |
| `12h` | 817,310.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 119,140.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -590,340.00 USD | -14,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,020,000.00 USD | -137,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.49K` | 15m=`-450.35` | 1h=`-212.58K` | 24h=`+119.14K`
* Futures Capital Netflows: 5m=`+109.59K` | 15m=`+15.62K` | 1h=`-560.95K` | 24h=`-2.48M`
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
  * Execution Entry: `269.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `265.75` (Risk Distance: `3.37` pts)
  * +2.5R Take Profit: `277.56`
  * Mathematical Lot Sizing: **`2.96 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `281.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `285.28` (Risk Distance: `3.37` pts)
  * +2.5R Take Profit: `273.47`
  * Mathematical Lot Sizing: **`2.96 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`281.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
