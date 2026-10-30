# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `283.66` | **Live Ask Quote**: `284.24` | **Mid Price**: `283.95`
- **Spread Points**: `580.00` | **Spread BPS**: `20.43 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `283.95` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `285.94` | Lower -3.00σ Band: `281.96`
  * Upper +2.51σ Band: `285.51` | Lower -2.51σ Band: `282.39`
  * Upper +2.01σ Band: `285.14` | Lower -2.01σ Band: `282.76`
  * Upper +2.00σ Band: `285.09` | Lower -2.00σ Band: `282.81`
  * Upper +1.28σ Band: `284.75` | Lower -1.28σ Band: `283.15`
  * Upper +1.00σ Band: `284.52` | Lower -1.00σ Band: `283.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`283.95` | EMA-20=`283.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.95` (Slope: `+0.0000`) | EMA-100=`283.95`
  * Institutional Anchors: EMA-144=`283.95` | EMA-200=`283.95` (Slope: `+0.0000`) | EMA-233=`283.95`
- **Range Boundaries**: 24H High=`286.79` | 24H Low=`281.11` | Weekly High=`289.63` | Weekly Low=`278.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `284.44` (Distance: `-0.10%`)
  * Point of Control (POC) = `283.81` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `273.07` (Distance: `+4.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`284.06` | Low=`279.46`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `282.81` - `285.09`
  * Optimal Trade Entry (OTE 0.705): `284.52`
  * Structural Invalidation Anchor (0.786): `286.22`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `281.72` | `284.61` | `281.56` | `283.96` | `3,015` | 854,014.45 USD | 134,127.46 USD | `+15.71%` | -1,564,408.64 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `283.95` | `284.57` | `283.36` | `284.30` | `1,111` | 315,411.77 USD | -20,238.70 USD | `-6.42%` | -1,584,647.34 USD | `-0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `284.29` | `284.37` | `284.04` | `284.25` | `147` | 41,871.67 USD | 6,614.57 USD | `+15.80%` | -1,578,032.76 USD | `+0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `281.14` | `281.14` | `280.02` | `280.48` | `1,714` | 480,699.25 USD | 45,070.56 USD | `+9.38%` | -1,869,072.34 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `280.48` | `282.20` | `280.15` | `281.70` | `2,342` | 658,245.44 USD | 170,536.24 USD | `+25.91%` | -1,698,536.10 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `281.72` | `284.61` | `281.56` | `284.31` | `4,275` | 1,211,872.47 USD | 121,032.42 USD | `+9.99%` | -1,577,503.68 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `278.73` | `279.02` | `16,468` | 4,630,594.81 USD | 275,996.65 USD | `+5.96%` | -1,529,264.29 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `279.03` | `282.29` | `278.54` | `281.15` | `18,009` | 5,054,095.53 USD | -226,117.37 USD | `-4.47%` | -1,755,381.65 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `281.14` | `284.61` | `280.02` | `284.35` | `8,332` | 2,351,258.15 USD | 336,948.29 USD | `+14.33%` | -1,418,433.37 USD | `+0.60` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `284.61` | `278.54` | `284.25` | `42,805` | 12,034,932.92 USD | 385,989.41 USD | `+3.21%` | -1,353,921.23 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `284.61` | `278.54` | `284.25` | `42,805` | 12,034,932.92 USD | 385,989.41 USD | `+3.21%` | -1,353,921.23 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`283.95`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1945` | `0x12d2...f97f` | `LONG` | 1,026,981.31 USD | `3,627,243,000,000.00` | `303.26` | `283.66` | `0.000000` | -73,018.03 USD | `-7.11%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+1.75%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.50%`)
  * 48H Horizon: Short MP=`296.90` (Vol: 281,700.00 USD, Dist: `+4.58%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.50%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.72%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.47%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.72%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.47%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `70.50` | 2,890.00 USD | 212,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 556.06 USD | 209,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,170.00 USD | 208,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 207,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 206,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 200,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 398.79 USD | 196,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 108.50 USD | 195,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 195,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 174.94 USD | 195,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 195,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 195,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 195,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 2,060.00 USD | 194,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `138.50` | 3,460.00 USD | 192,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 188,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 188,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 186,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 184,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 1,880.00 USD | 184,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 182,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `168.50` | 8,430.00 USD | 181,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `169.50` | 1,280.00 USD | 173,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 172,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 171,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 171,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 171,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 170,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 169,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 169,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 168,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 166,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 210.65 USD | 166,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 165,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 165,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 165,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 164,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 41,790.00 USD | 164,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 122,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 122,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `214.50` | 643.50 USD | 118,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 118,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 31,290.00 USD | 117,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 12,900.00 USD | 86,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 73,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 72,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 72,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 114.75 USD | 71,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 1,190.00 USD | 71,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 70,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 637.61 USD | 69,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 69,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 10,390,000.00 USD | 10,390,000.00 USD | 5,120.00 USD | 146.67 USD | 13.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 10,380,000.00 USD | 10,380,000.00 USD | 178.62 USD | 6,570.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `238.50` | 3,790.00 USD | 45,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `238.80` | 10,370,000.00 USD | 10,370,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 10,340,000.00 USD | 10,340,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 41,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,320,000.00 USD | 10,320,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 10,310,000.00 USD | 10,310,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 40,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 10,300,000.00 USD | 10,300,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 10,290,000.00 USD | 10,290,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 7,180.00 USD | 40,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 10,210,000.00 USD | 10,210,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 33,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 10,190,000.00 USD | 10,190,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 5,760.00 USD | 31,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 10,130,000.00 USD | 10,130,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 10,110,000.00 USD | 10,110,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 10,080,000.00 USD | 10,080,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 10,070,000.00 USD | 10,070,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 10,020,000.00 USD | 10,020,000.00 USD | 4,590.00 USD | 472.85 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 10,020,000.00 USD | 10,020,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,980,000.00 USD | 9,980,000.00 USD | 3,560.00 USD | 4,920.00 USD | 8.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,970,000.00 USD | 9,970,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,950,000.00 USD | 9,950,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,850,000.00 USD | 9,850,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,770,000.00 USD | 9,770,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,660,000.00 USD | 9,660,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.50` | 5,050,000.00 USD | 5,050,000.00 USD | 13,910.00 USD | 7,600.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 24,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,560,000.00 USD | 9,560,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.90` | 5,020,000.00 USD | 5,020,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,980,000.00 USD | 4,980,000.00 USD | 26,340.00 USD | 22,320.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 9,430,000.00 USD | 9,430,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,900,000.00 USD | 4,900,000.00 USD | 27,330.00 USD | 43,370.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.80` | 9,280,000.00 USD | 9,280,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,820,000.00 USD | 4,820,000.00 USD | 16,350.00 USD | 5,490.00 USD | 12,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 9,070,000.00 USD | 9,070,000.00 USD | 69,530.00 USD | 40,300.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,780,000.00 USD | 4,780,000.00 USD | 11,020.00 USD | 1,620.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,940,000.00 USD | 8,940,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,770,000.00 USD | 4,770,000.00 USD | 3,030.00 USD | 8,080.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,750,000.00 USD | 4,750,000.00 USD | 12,560.00 USD | 9,060.00 USD | 14,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,860,000.00 USD | 8,860,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,720,000.00 USD | 4,720,000.00 USD | 21,830.00 USD | 17,470.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,750,000.00 USD | 8,750,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,660,000.00 USD | 4,660,000.00 USD | 1,650.00 USD | 7,170.00 USD | 5,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,670,000.00 USD | 8,670,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,650,000.00 USD | 4,650,000.00 USD | 8,310.00 USD | 11,590.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,550,000.00 USD | 8,550,000.00 USD | 50,920.00 USD | 38,370.00 USD | 85,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,630,000.00 USD | 4,630,000.00 USD | 9,050.00 USD | 12,090.00 USD | 32.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,600,000.00 USD | 4,600,000.00 USD | 9,910.00 USD | 15,640.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 8,370,000.00 USD | 8,370,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,550,000.00 USD | 4,550,000.00 USD | 17,660.00 USD | 23,250.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 8,290,000.00 USD | 8,290,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,500,000.00 USD | 4,500,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 8,230,000.00 USD | 8,230,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,450,000.00 USD | 4,450,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.80` | 8,130,000.00 USD | 8,130,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,410,000.00 USD | 4,410,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,380,000.00 USD | 4,380,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 8,020,000.00 USD | 8,020,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,360,000.00 USD | 4,360,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,990,000.00 USD | 7,990,000.00 USD | 34,690.00 USD | 7,360.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,350,000.00 USD | 4,350,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,930,000.00 USD | 7,930,000.00 USD | 98,560.00 USD | 37,040.00 USD | 71,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,280,000.00 USD | 4,280,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 645.99 USD | 17,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,720,000.00 USD | 7,720,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,220,000.00 USD | 4,220,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 4,150,000.00 USD | 4,150,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,550,000.00 USD | 7,550,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 4,110,000.00 USD | 4,110,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 7,490,000.00 USD | 7,490,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 4,020,000.00 USD | 4,020,000.00 USD | 39,470.00 USD | 8,640.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 7,330,000.00 USD | 7,330,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,960,000.00 USD | 3,960,000.00 USD | 19,000.00 USD | 1,900.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 16,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,110,000.00 USD | 7,110,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,910,000.00 USD | 3,910,000.00 USD | 9,090.00 USD | 50,950.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,840,000.00 USD | 3,840,000.00 USD | 8,200.00 USD | 29,340.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,980,000.00 USD | 6,980,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,770,000.00 USD | 3,770,000.00 USD | 15,340.00 USD | 60,900.00 USD | 51,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,820,000.00 USD | 6,820,000.00 USD | 68,120.00 USD | 83,380.00 USD | 45,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,640,000.00 USD | 3,640,000.00 USD | 13,720.00 USD | 28,450.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,620,000.00 USD | 6,620,000.00 USD | 43,780.00 USD | 83,970.00 USD | 48,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,580,000.00 USD | 3,580,000.00 USD | 21,220.00 USD | 5,740.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,310.00 USD | 14,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,450,000.00 USD | 6,450,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,540,000.00 USD | 3,540,000.00 USD | 629.76 USD | 12,770.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,510,000.00 USD | 3,510,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 6,290,000.00 USD | 6,290,000.00 USD | 33,590.00 USD | 13,710.00 USD | 221.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,430,000.00 USD | 3,430,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 6,240,000.00 USD | 6,240,000.00 USD | 391,670.00 USD | 2,510.00 USD | 117,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,320,000.00 USD | 3,320,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,730,000.00 USD | 5,730,000.00 USD | 48,230.00 USD | 1,170.00 USD | 89.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,240,000.00 USD | 3,240,000.00 USD | 1,300.00 USD | 19,920.00 USD | 106.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,680,000.00 USD | 5,680,000.00 USD | 33,470.00 USD | 21,870.00 USD | 151.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,220,000.00 USD | 3,220,000.00 USD | 33,320.00 USD | 2,320.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,130,000.00 USD | 3,130,000.00 USD | 64,840.00 USD | 2,650.00 USD | 6.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,630,000.00 USD | 5,630,000.00 USD | 256,440.00 USD | 2,330.00 USD | 33,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 531.00 USD | 13,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 3,060,000.00 USD | 3,060,000.00 USD | 187.80 USD | 629.76 USD | 5.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 5,330,000.00 USD | 5,330,000.00 USD | 69,380.00 USD | 0.00 USD | 91.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 3,060,000.00 USD | 3,060,000.00 USD | 16,330.00 USD | 13,320.00 USD | 5.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 5,260,000.00 USD | 5,260,000.00 USD | 216,090.00 USD | 1,450.00 USD | 51.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 3,030,000.00 USD | 3,030,000.00 USD | 14,430.00 USD | 8,820.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 5,050,000.00 USD | 5,050,000.00 USD | 136,640.00 USD | 63,260.00 USD | 51.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 3,000,000.00 USD | 3,000,000.00 USD | 18,470.00 USD | 23,750.00 USD | 1.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 2,960,000.00 USD | 2,960,000.00 USD | 33,620.00 USD | 69,850.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,850,000.00 USD | 4,850,000.00 USD | 131,280.00 USD | 53,030.00 USD | 93.84 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `267.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 2,840,000.00 USD | 2,840,000.00 USD | 10,330.00 USD | 36,440.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,660,000.00 USD | 4,660,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,770,000.00 USD | 2,770,000.00 USD | 19,060.00 USD | 28,480.00 USD | 59,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,370,000.00 USD | 4,370,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,660,000.00 USD | 2,660,000.00 USD | 18,310.00 USD | 18,920.00 USD | 248.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,920,000.00 USD | 3,920,000.00 USD | 23,340.00 USD | 18,320.00 USD | 83.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,620,000.00 USD | 2,620,000.00 USD | 21,330.00 USD | 11,500.00 USD | 156.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,590,000.00 USD | 2,590,000.00 USD | 11,120.00 USD | 2,390.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 3,490.00 USD | 44.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,570,000.00 USD | 2,570,000.00 USD | 6,500.00 USD | 19,440.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,530,000.00 USD | 2,530,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,500,000.00 USD | 2,500,000.00 USD | 48,370.00 USD | 2,840.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,880,000.00 USD | 3,880,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,440,000.00 USD | 2,440,000.00 USD | 505.00 USD | 17,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,420,000.00 USD | 2,420,000.00 USD | 12,710.00 USD | 1,780.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,390,000.00 USD | 2,390,000.00 USD | 8,650.00 USD | 36,810.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,820,000.00 USD | 3,820,000.00 USD | 61,810.00 USD | 7,250.00 USD | 61,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,340,000.00 USD | 2,340,000.00 USD | 21,980.00 USD | 24,370.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,270,000.00 USD | 2,270,000.00 USD | 6,060.00 USD | 38,280.00 USD | 47,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `272.50` | 214.19 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,660,000.00 USD | 3,660,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,180,000.00 USD | 2,180,000.00 USD | 66,940.00 USD | 5,420.00 USD | 71,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 2,030,000.00 USD | 2,030,000.00 USD | 28,730.00 USD | 121,350.00 USD | 40,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 1,840,000.00 USD | 1,840,000.00 USD | 60,550.00 USD | 67,190.00 USD | 69,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 3,170,000.00 USD | 3,170,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,650,000.00 USD | 1,650,000.00 USD | 152,290.00 USD | 37,550.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,890,000.00 USD | 2,890,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,440,000.00 USD | 1,440,000.00 USD | 157,790.00 USD | 21,440.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 2,240,000.00 USD | 2,240,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,210,000.00 USD | 1,210,000.00 USD | 54,360.00 USD | 22,510.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,120,000.00 USD | 1,120,000.00 USD | 11,720.00 USD | 3,760.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,710,000.00 USD | 1,710,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,090,000.00 USD | 1,090,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,630,000.00 USD | 1,630,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 974,590.00 USD | 974,590.00 USD | 172,570.00 USD | 3,340.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,520,000.00 USD | 1,520,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 791,600.00 USD | 791,600.00 USD | 11,920.00 USD | 16,150.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 1,200,000.00 USD | 1,200,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 744,860.00 USD | 744,860.00 USD | 37,290.00 USD | 25,410.00 USD | 33,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 648,240.00 USD | 648,240.00 USD | 17,610.00 USD | 22,050.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 1,180,000.00 USD | 1,180,000.00 USD | 152,190.00 USD | 77,800.00 USD | 182,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 590,780.00 USD | 590,780.00 USD | 13,750.00 USD | 16,920.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 769,370.00 USD | 769,370.00 USD | 0.00 USD | 157,740.00 USD | 59,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 539,790.00 USD | 539,790.00 USD | 12,120.00 USD | 97,470.00 USD | 95,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 551,660.00 USD | 551,660.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 335,020.00 USD | 335,020.00 USD | 93,830.00 USD | 56,870.00 USD | 47,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 334,510.00 USD | 334,510.00 USD | 51,310.00 USD | 19,060.00 USD | 49.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 136,450.00 USD | 136,450.00 USD | 19,260.00 USD | 10,830.00 USD | 43.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 106,310.00 USD | 106,310.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 264,080.00 USD | 264,080.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 65,220.00 USD | 65,220.00 USD | 0.00 USD | 0.00 USD | 24,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 40,880.00 USD | 40,880.00 USD | 0.00 USD | 0.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 261,420.00 USD | 261,420.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 245,880.00 USD | 245,880.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.80` | 152,050.00 USD | 152,050.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 9,540.00 USD | 9,540.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 29,670.00 USD | 29,670.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 1,280.00 USD | 1,280.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 5,440.00 USD | 5,440.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `283.50` | 306.46 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `283.80` | 2,000.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.10` | 15.61 USD | 15.61 USD | 0.00 USD | 0.00 USD | 15.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 1,570.00 USD | 1,570.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.50` | 11,420.00 USD | 11,420.00 USD | 0.00 USD | 0.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 56,960.00 USD | 56,960.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 47,770.00 USD | 47,770.00 USD | 28,720.00 USD | 7,620.00 USD | 5.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 142,400.00 USD | 142,400.00 USD | 36,620.00 USD | 16,320.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 478,930.00 USD | 478,930.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 191,400.00 USD | 191,400.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 712,480.00 USD | 712,480.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 268,000.00 USD | 268,000.00 USD | 33,580.00 USD | 3,270.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 756,690.00 USD | 756,690.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 318,830.00 USD | 318,830.00 USD | 15,270.00 USD | 5,410.00 USD | 30,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,000,000.00 USD | 1,000,000.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 473,690.00 USD | 473,690.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 660,500.00 USD | 660,500.00 USD | 109,280.00 USD | 43,890.00 USD | 33,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,200,000.00 USD | 1,200,000.00 USD | 82,910.00 USD | 116,440.00 USD | 11.42 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 776,500.00 USD | 776,500.00 USD | 22,860.00 USD | 33,420.00 USD | 59,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,600,000.00 USD | 1,600,000.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 868,880.00 USD | 868,880.00 USD | 21,420.00 USD | 26,660.00 USD | 44,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 987,410.00 USD | 987,410.00 USD | 52,260.00 USD | 29,840.00 USD | 36,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 1,940,000.00 USD | 1,940,000.00 USD | 124,780.00 USD | 15,650.00 USD | 122,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 1,060,000.00 USD | 1,060,000.00 USD | 44,740.00 USD | 30,590.00 USD | 9.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 1,180,000.00 USD | 1,180,000.00 USD | 17,220.00 USD | 47,120.00 USD | 51,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 1,420,000.00 USD | 1,420,000.00 USD | 67,250.00 USD | 67,790.00 USD | 103,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,350,000.00 USD | 2,350,000.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,650,000.00 USD | 1,650,000.00 USD | 65,110.00 USD | 51,750.00 USD | 114,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,400,000.00 USD | 2,400,000.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,840,000.00 USD | 1,840,000.00 USD | 28,010.00 USD | 120,130.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,520,000.00 USD | 2,520,000.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,990,000.00 USD | 1,990,000.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 2,050,000.00 USD | 2,050,000.00 USD | 27,020.00 USD | 12,070.00 USD | 24,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,580,000.00 USD | 2,580,000.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 2,120,000.00 USD | 2,120,000.00 USD | 12,850.00 USD | 24,830.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 2,780,000.00 USD | 2,780,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 2,180,000.00 USD | 2,180,000.00 USD | 6,710.00 USD | 39,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 2,850,000.00 USD | 2,850,000.00 USD | 1,240.00 USD | 73,530.00 USD | 49.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 2,210,000.00 USD | 2,210,000.00 USD | 29,880.00 USD | 3,650.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 6,050.00 USD | 10,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,960,000.00 USD | 2,960,000.00 USD | 887.27 USD | 101,280.00 USD | 126.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,310,000.00 USD | 2,310,000.00 USD | 62,510.00 USD | 30,990.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,400,000.00 USD | 2,400,000.00 USD | 27,950.00 USD | 23,500.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,120,000.00 USD | 3,120,000.00 USD | 33,580.00 USD | 132,770.00 USD | 100.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,590,000.00 USD | 2,590,000.00 USD | 76,710.00 USD | 47,640.00 USD | 70,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,180,000.00 USD | 3,180,000.00 USD | 38,790.00 USD | 1,860.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,690,000.00 USD | 2,690,000.00 USD | 21,460.00 USD | 25,650.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,610,000.00 USD | 3,610,000.00 USD | 217,140.00 USD | 42,290.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,950,000.00 USD | 2,950,000.00 USD | 96,690.00 USD | 80,200.00 USD | 85,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,870,000.00 USD | 3,870,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 3,050,000.00 USD | 3,050,000.00 USD | 33,490.00 USD | 17,570.00 USD | 48,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 3,230,000.00 USD | 3,230,000.00 USD | 15,750.00 USD | 62,250.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,350,000.00 USD | 4,350,000.00 USD | 46,330.00 USD | 83,600.00 USD | 345,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,470,000.00 USD | 3,470,000.00 USD | 106,670.00 USD | 7,020.00 USD | 128,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 4,790,000.00 USD | 4,790,000.00 USD | 165,320.00 USD | 82,100.00 USD | 197,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,690,000.00 USD | 3,690,000.00 USD | 52,840.00 USD | 126,740.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 5,120,000.00 USD | 5,120,000.00 USD | 43,710.00 USD | 167,940.00 USD | 121,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,790,000.00 USD | 3,790,000.00 USD | 33,430.00 USD | 22,420.00 USD | 41,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,460,000.00 USD | 5,460,000.00 USD | 133,820.00 USD | 4,410.00 USD | 201,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,920,000.00 USD | 3,920,000.00 USD | 24,280.00 USD | 21,780.00 USD | 90,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 4,020,000.00 USD | 4,020,000.00 USD | 61,380.00 USD | 1,000.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,600,000.00 USD | 5,600,000.00 USD | 78,980.00 USD | 54,960.00 USD | 5.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 4,060,000.00 USD | 4,060,000.00 USD | 15,920.00 USD | 11,340.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 5,840,000.00 USD | 5,840,000.00 USD | 47,530.00 USD | 99,810.00 USD | 89,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 4,160,000.00 USD | 4,160,000.00 USD | 51,960.00 USD | 10,200.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 5,980,000.00 USD | 5,980,000.00 USD | 32,650.00 USD | 45,150.00 USD | 68,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,220,000.00 USD | 4,220,000.00 USD | 5,730.00 USD | 1,480.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,060,000.00 USD | 6,060,000.00 USD | 69,820.00 USD | 12,530.00 USD | 106.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,350,000.00 USD | 4,350,000.00 USD | 28,220.00 USD | 5,580.00 USD | 94,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,410,000.00 USD | 4,410,000.00 USD | 34,110.00 USD | 11,020.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,180,000.00 USD | 6,180,000.00 USD | 3,550.00 USD | 27,070.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,460,000.00 USD | 4,460,000.00 USD | 8,350.00 USD | 11,780.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,230,000.00 USD | 6,230,000.00 USD | 22,060.00 USD | 9,100.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,580,000.00 USD | 4,580,000.00 USD | 20,020.00 USD | 37,550.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,270,000.00 USD | 6,270,000.00 USD | 35,320.00 USD | 3,530.00 USD | 101.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,620,000.00 USD | 4,620,000.00 USD | 23,270.00 USD | 1,700.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 991.05 USD | 11,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,420,000.00 USD | 6,420,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,650,000.00 USD | 4,650,000.00 USD | 269.05 USD | 1,020.00 USD | 29,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,690,000.00 USD | 4,690,000.00 USD | 693.10 USD | 15,110.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 6,700,000.00 USD | 6,700,000.00 USD | 73,320.00 USD | 58,690.00 USD | 150,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,730,000.00 USD | 4,730,000.00 USD | 19,840.00 USD | 8,470.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 6,950,000.00 USD | 6,950,000.00 USD | 89,300.00 USD | 131,150.00 USD | 26,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,800,000.00 USD | 4,800,000.00 USD | 25,190.00 USD | 30,660.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 7,130,000.00 USD | 7,130,000.00 USD | 1,560.00 USD | 181,550.00 USD | 12.67 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,860,000.00 USD | 4,860,000.00 USD | 13,920.00 USD | 13,290.00 USD | 38,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,350,000.00 USD | 7,350,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 4,880,000.00 USD | 4,880,000.00 USD | 1,370.00 USD | 2,410.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 4,920,000.00 USD | 4,920,000.00 USD | 21,200.00 USD | 2,760.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 1,950.00 USD | 96.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 391.16 USD | 8.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,410,000.00 USD | 7,410,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 4,980,000.00 USD | 4,980,000.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,440,000.00 USD | 7,440,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 5,040,000.00 USD | 5,040,000.00 USD | 9,670.00 USD | 2,100.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,490,000.00 USD | 7,490,000.00 USD | 35,470.00 USD | 11,790.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 5,060,000.00 USD | 5,060,000.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 5,060,000.00 USD | 5,060,000.00 USD | 83.23 USD | 172.52 USD | 2.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 7,920,000.00 USD | 7,920,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 5,070,000.00 USD | 5,070,000.00 USD | 6,340.00 USD | 3,500.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,070,000.00 USD | 8,070,000.00 USD | 80,680.00 USD | 52,160.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 5,090,000.00 USD | 5,090,000.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,220,000.00 USD | 8,220,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 5,100,000.00 USD | 5,100,000.00 USD | 4,330.00 USD | 6.13 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,460,000.00 USD | 8,460,000.00 USD | 94,690.00 USD | 74,510.00 USD | 69,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,170,000.00 USD | 5,170,000.00 USD | 19,810.00 USD | 35,610.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,240,000.00 USD | 5,240,000.00 USD | 11,240.00 USD | 32,670.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 8,780,000.00 USD | 8,780,000.00 USD | 27,410.00 USD | 136,370.00 USD | 147,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,290,000.00 USD | 5,290,000.00 USD | 24,280.00 USD | 20,210.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,080,000.00 USD | 9,080,000.00 USD | 127,080.00 USD | 113,210.00 USD | 60,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,320,000.00 USD | 5,320,000.00 USD | 14,750.00 USD | 4,740.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,430,000.00 USD | 9,430,000.00 USD | 169,010.00 USD | 67,070.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,330,000.00 USD | 5,330,000.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,590,000.00 USD | 9,590,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,340,000.00 USD | 5,340,000.00 USD | 7,510.00 USD | 6,640.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 5,350,000.00 USD | 5,350,000.00 USD | 3,240.00 USD | 2,300.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 9,700,000.00 USD | 9,700,000.00 USD | 34,260.00 USD | 36,030.00 USD | 36,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 5,370,000.00 USD | 5,370,000.00 USD | 10,120.00 USD | 7,760.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,050,000.00 USD | 10,050,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 5,410,000.00 USD | 5,410,000.00 USD | 14,750.00 USD | 6,170.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,300,000.00 USD | 10,300,000.00 USD | 62,230.00 USD | 108,410.00 USD | 80,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 5,420,000.00 USD | 5,420,000.00 USD | 176.40 USD | 5,020.00 USD | 5,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,420,000.00 USD | 10,420,000.00 USD | 60,910.00 USD | 51,380.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 5,420,000.00 USD | 5,420,000.00 USD | 5,080.00 USD | 73.70 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 5,430,000.00 USD | 5,430,000.00 USD | 257.90 USD | 3,110.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,680,000.00 USD | 10,680,000.00 USD | 114,310.00 USD | 65,480.00 USD | 72,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 5,450,000.00 USD | 5,450,000.00 USD | 7,980.00 USD | 10,260.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 10,730,000.00 USD | 10,730,000.00 USD | 19,570.00 USD | 11,240.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 5,480,000.00 USD | 5,480,000.00 USD | 299.35 USD | 10,430.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 10,820,000.00 USD | 10,820,000.00 USD | 43,780.00 USD | 11,410.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,520,000.00 USD | 5,520,000.00 USD | 17,660.00 USD | 8,480.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,870,000.00 USD | 10,870,000.00 USD | 21,990.00 USD | 14,880.00 USD | 19,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 5,530,000.00 USD | 5,530,000.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 5,560,000.00 USD | 5,560,000.00 USD | 3,580.00 USD | 18,130.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 10,950,000.00 USD | 10,950,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 5,570,000.00 USD | 5,570,000.00 USD | 4,550.00 USD | 0.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 11,030,000.00 USD | 11,030,000.00 USD | 32,780.00 USD | 1,570.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 11,110,000.00 USD | 11,110,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,140,000.00 USD | 11,140,000.00 USD | 17,720.00 USD | 0.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 547.95 USD | 52.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,210,000.00 USD | 11,210,000.00 USD | 1,670.00 USD | 33,700.00 USD | 29,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,310,000.00 USD | 11,310,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,370,000.00 USD | 11,370,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,380,000.00 USD | 11,380,000.00 USD | 15,590.00 USD | 748.91 USD | 173.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,410,000.00 USD | 11,410,000.00 USD | 21,110.00 USD | 8,380.00 USD | 5.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `324.50` | 2,220.00 USD | 14,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 40,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `342.50` | 1,370.00 USD | 41,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 43,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `373.50` | 41,090.00 USD | 84,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `406.50` | 10,640.00 USD | 94,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 141,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 141,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `552.50` | 195.03 USD | 142,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 142,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `70.50` | 212,160.00 USD | 0.00 USD | 2,890.00 USD | `-74.82%` | `41,012,000,000.00` |
| `Live` | `Long` | `77.50` | 209,270.00 USD | 0.00 USD | 556.06 USD | `-72.32%` | `7,175,000,000.00` |
| `Live` | `Long` | `89.50` | 208,720.00 USD | 0.00 USD | 1,170.00 USD | `-68.04%` | `13,105,000,000.00` |
| `Live` | `Long` | `95.50` | 207,540.00 USD | 0.00 USD | 920.05 USD | `-65.90%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 206,620.00 USD | 0.00 USD | 6,240.00 USD | `-63.75%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 200,390.00 USD | 0.00 USD | 4,080.00 USD | `-63.40%` | `39,797,000,000.00` |
| `Live` | `Long` | `105.50` | 196,310.00 USD | 0.00 USD | 398.79 USD | `-62.33%` | `3,780,000,000.00` |
| `Live` | `Long` | `108.50` | 195,910.00 USD | 0.00 USD | 108.50 USD | `-61.25%` | `1,000,000,000.00` |
| `Live` | `Long` | `109.50` | 195,800.00 USD | 0.00 USD | 212.76 USD | `-60.90%` | `1,943,000,000.00` |
| `Live` | `Long` | `111.50` | 195,590.00 USD | 0.00 USD | 174.94 USD | `-60.18%` | `1,569,000,000.00` |
| `Live` | `Long` | `118.50` | 195,410.00 USD | 0.00 USD | 212.35 USD | `-57.68%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 195,200.00 USD | 0.00 USD | 124.46 USD | `-56.25%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 195,080.00 USD | 0.00 USD | 658.18 USD | `-54.83%` | `5,203,000,000.00` |
| `Live` | `Long` | `128.50` | 194,420.00 USD | 0.00 USD | 2,060.00 USD | `-54.11%` | `16,000,000,000.00` |
| `Live` | `Long` | `138.50` | 192,360.00 USD | 0.00 USD | 3,460.00 USD | `-50.54%` | `25,000,000,000.00` |
| `Live` | `Long` | `147.50` | 188,900.00 USD | 0.00 USD | 895.47 USD | `-47.33%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 188,000.00 USD | 0.00 USD | 1,270.00 USD | `-46.97%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 186,740.00 USD | 0.00 USD | 2,370.00 USD | `-46.61%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 184,370.00 USD | 0.00 USD | 303.78 USD | `-45.54%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 184,070.00 USD | 0.00 USD | 1,880.00 USD | `-41.97%` | `11,599,000,000.00` |
| `Live` | `Long` | `167.50` | 182,180.00 USD | 0.00 USD | 285.75 USD | `-40.18%` | `1,706,000,000.00` |
| `Live` | `Long` | `168.50` | 181,900.00 USD | 0.00 USD | 8,430.00 USD | `-39.83%` | `50,000,000,000.00` |
| `Live` | `Long` | `169.50` | 173,470.00 USD | 0.00 USD | 1,280.00 USD | `-39.47%` | `7,572,000,000.00` |
| `Live` | `Long` | `170.50` | 172,190.00 USD | 0.00 USD | 426.25 USD | `-39.11%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 171,760.00 USD | 0.00 USD | 169.96 USD | `-37.69%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 171,590.00 USD | 0.00 USD | 516.67 USD | `-37.33%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 171,080.00 USD | 0.00 USD | 373.83 USD | `-36.97%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 170,700.00 USD | 0.00 USD | 808.66 USD | `-34.11%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 169,890.00 USD | 0.00 USD | 418.28 USD | `-32.69%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 169,480.00 USD | 0.00 USD | 694.75 USD | `-31.97%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 168,780.00 USD | 0.00 USD | 858.49 USD | `-31.61%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 167,920.00 USD | 0.00 USD | 1,490.00 USD | `-31.26%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 166,440.00 USD | 0.00 USD | 370.47 USD | `-30.19%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 166,070.00 USD | 0.00 USD | 210.65 USD | `-29.83%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 165,860.00 USD | 0.00 USD | 548.03 USD | `-28.76%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 165,310.00 USD | 0.00 USD | 293.13 USD | `-28.40%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 165,020.00 USD | 0.00 USD | 420.39 USD | `-27.69%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 164,600.00 USD | 0.00 USD | 191.53 USD | `-26.62%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 164,400.00 USD | 0.00 USD | 41,790.00 USD | `-26.26%` | `202,387,000,000.00` |
| `Live` | `Long` | `210.50` | 122,610.00 USD | 0.00 USD | 108.83 USD | `-24.83%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 122,500.00 USD | 0.00 USD | 3,800.00 USD | `-23.76%` | `17,817,000,000.00` |
| `Live` | `Long` | `214.50` | 118,700.00 USD | 0.00 USD | 643.50 USD | `-23.40%` | `3,000,000,000.00` |
| `Live` | `Long` | `215.50` | 118,050.00 USD | 0.00 USD | 239.85 USD | `-23.04%` | `1,113,000,000.00` |
| `Live` | `Long` | `223.50` | 117,810.00 USD | 0.00 USD | 31,290.00 USD | `-20.19%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 86,520.00 USD | 0.00 USD | 12,900.00 USD | `-19.83%` | `57,451,000,000.00` |
| `Live` | `Long` | `226.50` | 73,630.00 USD | 0.00 USD | 1,240.00 USD | `-19.12%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 72,390.00 USD | 0.00 USD | 174.49 USD | `-18.76%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 72,220.00 USD | 0.00 USD | 642.77 USD | `-18.40%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 71,570.00 USD | 0.00 USD | 114.75 USD | `-18.04%` | `500,000,000.00` |
| `Live` | `Long` | `230.50` | 71,460.00 USD | 0.00 USD | 1,190.00 USD | `-17.69%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 70,270.00 USD | 0.00 USD | 295.86 USD | `-17.33%` | `1,278,000,000.00` |
| `Live` | `Long` | `234.50` | 69,970.00 USD | 0.00 USD | 637.61 USD | `-16.26%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 69,330.00 USD | 0.00 USD | 23,750.00 USD | `-15.19%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 45,580.00 USD | 0.00 USD | 3,790.00 USD | `-14.83%` | `15,877,000,000.00` |
| `Live` | `Long` | `239.50` | 41,800.00 USD | 0.00 USD | 1,030.00 USD | `-14.47%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 40,770.00 USD | 0.00 USD | 251.88 USD | `-13.76%` | `1,043,000,000.00` |
| `Live` | `Long` | `242.50` | 40,520.00 USD | 0.00 USD | 7,180.00 USD | `-13.40%` | `29,590,000,000.00` |
| `Live` | `Long` | `243.50` | 33,340.00 USD | 0.00 USD | 1,850.00 USD | `-13.05%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 31,500.00 USD | 0.00 USD | 5,760.00 USD | `-12.69%` | `23,551,000,000.00` |
| `Live` | `Long` | `245.50` | 25,740.00 USD | 0.00 USD | 1,030.00 USD | `-12.33%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,710.00 USD | 0.00 USD | 106.67 USD | `-11.62%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,600.00 USD | 0.00 USD | 595.16 USD | `-11.26%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 24,010.00 USD | 0.00 USD | 1,330.00 USD | `-10.55%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,680.00 USD | 0.00 USD | 268.35 USD | `-10.19%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 22,420.00 USD | 0.00 USD | 1,030.00 USD | `-9.83%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 21,380.00 USD | 0.00 USD | 548.45 USD | `-9.12%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 20,830.00 USD | 0.00 USD | 3,210.00 USD | `-8.40%` | `12,514,000,000.00` |
| `Live` | `Long` | `258.50` | 17,620.00 USD | 0.00 USD | 645.99 USD | `-7.69%` | `2,499,000,000.00` |
| `Live` | `Long` | `260.50` | 16,980.00 USD | 0.00 USD | 2,040.00 USD | `-6.97%` | `7,839,000,000.00` |
| `Live` | `Long` | `262.50` | 14,940.00 USD | 0.00 USD | 1,310.00 USD | `-6.26%` | `5,000,000,000.00` |
| `Live` | `Long` | `265.50` | 13,620.00 USD | 0.00 USD | 531.00 USD | `-5.19%` | `2,000,000,000.00` |
| `Live` | `Short` | `267.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | `-4.47%` | `10,931,000,000.00` |
| `Live` | `Long` | `270.50` | 13,090.00 USD | 0.00 USD | 13,090.00 USD | `-3.40%` | `48,404,000,000.00` |
| `Live` | `Short` | `272.50` | 3,140.00 USD | 214.19 USD | 0.00 USD | `-2.69%` | `786,000,000.00` |
| `Live` | `Short` | `283.50` | 3,440.00 USD | 306.46 USD | 0.00 USD | `+1.24%` | `1,081,000,000.00` |
| `Live` | `Short` | `287.50` | 3,560.00 USD | 112.12 USD | 0.00 USD | `+2.67%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 4,510.00 USD | 954.95 USD | 0.00 USD | `+4.10%` | `3,276,000,000.00` |
| `Live` | `Short` | `292.50` | 10,560.00 USD | 6,050.00 USD | 0.00 USD | `+4.45%` | `20,668,000,000.00` |
| `Live` | `Short` | `300.50` | 11,550.00 USD | 991.05 USD | 0.00 USD | `+7.31%` | `3,298,000,000.00` |
| `Live` | `Short` | `320.50` | 12,650.00 USD | 1,110.00 USD | 0.00 USD | `+14.45%` | `3,452,000,000.00` |
| `Live` | `Short` | `324.50` | 14,880.00 USD | 2,220.00 USD | 0.00 USD | `+15.88%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 40,410.00 USD | 25,530.00 USD | 0.00 USD | `+16.59%` | `78,189,000,000.00` |
| `Live` | `Short` | `342.50` | 41,780.00 USD | 1,370.00 USD | 0.00 USD | `+22.31%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 42,790.00 USD | 1,010.00 USD | 0.00 USD | `+28.02%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 43,230.00 USD | 445.52 USD | 0.00 USD | `+31.59%` | `1,209,000,000.00` |
| `Live` | `Short` | `373.50` | 84,320.00 USD | 41,090.00 USD | 0.00 USD | `+33.38%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 94,960.00 USD | 10,640.00 USD | 0.00 USD | `+45.16%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 141,210.00 USD | 46,250.00 USD | 0.00 USD | `+64.09%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 141,930.00 USD | 718.34 USD | 0.00 USD | `+78.02%` | `1,441,000,000.00` |
| `Live` | `Short` | `552.50` | 142,120.00 USD | 195.03 USD | 0.00 USD | `+97.30%` | `353,000,000.00` |
| `Live` | `Short` | `560.50` | 142,970.00 USD | 842.43 USD | 0.00 USD | `+100.16%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 452,640.00 USD | 0.00 USD | 210.94 USD | `-48.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 452,430.00 USD | 0.00 USD | 2,070.00 USD | `-48.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 450,360.00 USD | 0.00 USD | 489.38 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 449,870.00 USD | 0.00 USD | 2,530.00 USD | `-36.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 447,350.00 USD | 0.00 USD | 490.59 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 446,850.00 USD | 0.00 USD | 482.01 USD | `-29.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 446,370.00 USD | 0.00 USD | 189.07 USD | `-28.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 446,180.00 USD | 0.00 USD | 441.60 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 445,740.00 USD | 0.00 USD | 299.96 USD | `-24.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 445,440.00 USD | 0.00 USD | 715.29 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 444,730.00 USD | 0.00 USD | 638.36 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 444,090.00 USD | 0.00 USD | 740.85 USD | `-19.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 443,350.00 USD | 0.00 USD | 478.48 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 442,870.00 USD | 0.00 USD | 389.48 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 442,480.00 USD | 0.00 USD | 812.38 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 441,670.00 USD | 0.00 USD | 220.64 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 441,450.00 USD | 0.00 USD | 429.30 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 441,020.00 USD | 0.00 USD | 296.50 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 440,720.00 USD | 0.00 USD | 216.45 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 440,500.00 USD | 0.00 USD | 387.76 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 440,120.00 USD | 0.00 USD | 18,080.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 422,030.00 USD | 0.00 USD | 1,630.00 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 420,410.00 USD | 0.00 USD | 2,700.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 417,710.00 USD | 0.00 USD | 2,940.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 414,760.00 USD | 0.00 USD | 4,560.00 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 410,210.00 USD | 0.00 USD | 1,850.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 408,360.00 USD | 0.00 USD | 231.54 USD | `-9.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 408,130.00 USD | 0.00 USD | 109.26 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 408,020.00 USD | 0.00 USD | 1,780.00 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 406,240.00 USD | 0.00 USD | 51,300.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 354,940.00 USD | 0.00 USD | 250.81 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 354,690.00 USD | 0.00 USD | 2,370.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 352,320.00 USD | 0.00 USD | 269,800.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 82,520.00 USD | 0.00 USD | 3,600.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 78,920.00 USD | 0.00 USD | 199.17 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 78,720.00 USD | 0.00 USD | 2,180.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 76,550.00 USD | 0.00 USD | 241.98 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 76,310.00 USD | 0.00 USD | 219.35 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 76,090.00 USD | 0.00 USD | 107.40 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 75,980.00 USD | 0.00 USD | 29,530.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 46,450.00 USD | 0.00 USD | 3,340.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 43,110.00 USD | 0.00 USD | 620.38 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 42,490.00 USD | 0.00 USD | 13,500.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 28,990.00 USD | 0.00 USD | 136.20 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 28,850.00 USD | 0.00 USD | 667.86 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 28,190.00 USD | 0.00 USD | 275.50 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 27,910.00 USD | 0.00 USD | 553.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 27,360.00 USD | 0.00 USD | 326.34 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 27,030.00 USD | 0.00 USD | 5,040.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 21,990.00 USD | 0.00 USD | 21,990.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 139.69 USD | 139.69 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 3,240.00 USD | 3,100.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 6,180.00 USD | 2,940.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 14,220.00 USD | 8,040.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 14,360.00 USD | 137.98 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 15,410.00 USD | 1,050.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 15,690.00 USD | 280.77 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 22,600.00 USD | 6,910.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 22,860.00 USD | 261.96 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 23,390.00 USD | 530.36 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 23,600.00 USD | 212.36 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 48,880.00 USD | 25,280.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 49,050.00 USD | 167.89 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 50,040.00 USD | 992.62 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 52,060.00 USD | 2,020.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 56,790.00 USD | 4,730.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 56,900.00 USD | 110.37 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 57,290.00 USD | 388.95 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 57,440.00 USD | 153.94 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 68,220.00 USD | 10,780.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 73,320.00 USD | 5,110.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 84,050.00 USD | 10,730.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 86,700.00 USD | 2,650.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 86,980.00 USD | 282.89 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 101,480.00 USD | 14,500.00 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 102,110.00 USD | 634.04 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 103,150.00 USD | 1,030.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 108,800.00 USD | 5,650.00 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 109,330.00 USD | 534.59 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 109,650.00 USD | 321.50 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 176,370.00 USD | 66,720.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 177,460.00 USD | 1,090.00 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 189,450.00 USD | 12,000.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 190,000.00 USD | 547.52 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 190,110.00 USD | 110.91 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 190,370.00 USD | 257.45 USD | 0.00 USD | `+23.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 190,540.00 USD | 174.25 USD | 0.00 USD | `+24.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 190,700.00 USD | 151.50 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 192,150.00 USD | 1,450.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 193,920.00 USD | 1,770.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 194,250.00 USD | 326.07 USD | 0.00 USD | `+29.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 195,080.00 USD | 826.60 USD | 0.00 USD | `+29.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 202,520.00 USD | 7,440.00 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 203,200.00 USD | 682.84 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 204,300.00 USD | 1,100.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 204,990.00 USD | 683.96 USD | 0.00 USD | `+41.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 205,190.00 USD | 199.75 USD | 0.00 USD | `+42.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 206,920.00 USD | 1,730.00 USD | 0.00 USD | `+43.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 207,960.00 USD | 1,040.00 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 208,330.00 USD | 376.71 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 208,490.00 USD | 158.86 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 214,390.00 USD | 5,900.00 USD | 0.00 USD | `+48.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 215,470.00 USD | 1,080.00 USD | 0.00 USD | `+51.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 217,170.00 USD | 1,700.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 218,730.00 USD | 1,550.00 USD | 0.00 USD | `+53.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 220,110.00 USD | 1,380.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 220,730.00 USD | 621.14 USD | 0.00 USD | `+55.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 223,010.00 USD | 2,280.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 223,230.00 USD | 222.75 USD | 0.00 USD | `+59.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 230,150.00 USD | 6,920.00 USD | 0.00 USD | `+60.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 236,070.00 USD | 5,920.00 USD | 0.00 USD | `+61.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 237,200.00 USD | 1,130.00 USD | 0.00 USD | `+64.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 244,830.00 USD | 7,630.00 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 245,810.00 USD | 975.00 USD | 0.00 USD | `+74.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 246,790.00 USD | 981.00 USD | 0.00 USD | `+75.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 247,290.00 USD | 499.50 USD | 0.00 USD | `+78.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,130,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+78.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,130,000.00 USD | 1,000.00 USD | 0.00 USD | `+79.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,140,000.00 USD | 1,040.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,140,000.00 USD | 340.67 USD | 0.00 USD | `+86.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,140,000.00 USD | 638.86 USD | 0.00 USD | `+98.73%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `237.80` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 5,120.00 USD | 146.67 USD | 13.64 USD |
| `7D` | `238.30` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 178.62 USD | 6,570.00 USD | 12,590.00 USD |
| `7D` | `238.80` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.80` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.30` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,980.00 USD |
| `7D` | `242.80` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD |
| `7D` | `243.30` | 10,200,000.00 USD | 0.00 USD | 10,200,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD |
| `7D` | `245.30` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,010.00 USD |
| `7D` | `246.30` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 4,590.00 USD | 472.85 USD | 1,730.00 USD |
| `7D` | `247.30` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,710.00 USD |
| `7D` | `247.80` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 3,560.00 USD | 4,920.00 USD | 8.00 USD |
| `7D` | `248.30` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,410.00 USD |
| `7D` | `248.80` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD |
| `7D` | `249.30` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,540.00 USD |
| `7D` | `249.80` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,080.00 USD |
| `7D` | `250.30` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,600.00 USD |
| `1D` | `250.50` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 13,910.00 USD | 7,600.00 USD | 12,270.00 USD |
| `7D` | `250.80` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,610.00 USD |
| `1D` | `250.90` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD |
| `1D` | `251.30` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 26,340.00 USD | 22,320.00 USD | 23,580.00 USD |
| `7D` | `251.30` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,140.00 USD |
| `1D` | `251.70` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 27,330.00 USD | 43,370.00 USD | 13,910.00 USD |
| `7D` | `251.80` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,360.00 USD |
| `1D` | `252.10` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 16,350.00 USD | 5,490.00 USD | 12,450.00 USD |
| `7D` | `252.30` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 69,530.00 USD | 40,300.00 USD | 17,360.00 USD |
| `1D` | `252.50` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 11,020.00 USD | 1,620.00 USD | 6,030.00 USD |
| `7D` | `252.80` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,330.00 USD |
| `1D` | `252.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 3,030.00 USD | 8,080.00 USD | 2,190.00 USD |
| `1D` | `253.30` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 12,560.00 USD | 9,060.00 USD | 14,790.00 USD |
| `7D` | `253.30` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,260.00 USD |
| `1D` | `253.70` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,830.00 USD | 17,470.00 USD | 12,960.00 USD |
| `7D` | `253.80` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,080.00 USD |
| `1D` | `254.10` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,650.00 USD | 7,170.00 USD | 5,790.00 USD |
| `7D` | `254.30` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,120.00 USD |
| `1D` | `254.50` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 8,310.00 USD | 11,590.00 USD | 3,630.00 USD |
| `7D` | `254.80` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 50,920.00 USD | 38,370.00 USD | 85,580.00 USD |
| `1D` | `254.90` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 9,050.00 USD | 12,090.00 USD | 32.03 USD |
| `1D` | `255.30` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 9,910.00 USD | 15,640.00 USD | 28,000.00 USD |
| `7D` | `255.30` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,510.00 USD |
| `1D` | `255.70` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 17,660.00 USD | 23,250.00 USD | 14,080.00 USD |
| `7D` | `255.80` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,160.00 USD |
| `1D` | `256.10` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD |
| `7D` | `256.30` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,900.00 USD |
| `1D` | `256.50` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD |
| `7D` | `256.80` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,320.00 USD |
| `1D` | `256.90` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,300.00 USD |
| `1D` | `257.30` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,760.00 USD |
| `7D` | `257.30` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,160.00 USD |
| `1D` | `257.70` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,840.00 USD |
| `7D` | `257.80` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 34,690.00 USD | 7,360.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,970.00 USD |
| `7D` | `258.30` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 98,560.00 USD | 37,040.00 USD | 71,570.00 USD |
| `1D` | `258.50` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,210.00 USD |
| `7D` | `258.80` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD |
| `1D` | `258.90` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,030.00 USD |
| `1D` | `259.30` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,050.00 USD |
| `1D` | `259.70` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,280.00 USD |
| `7D` | `259.80` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,150.00 USD |
| `1D` | `260.10` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 39,470.00 USD | 8,640.00 USD | 6,870.00 USD |
| `7D` | `260.30` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,910.00 USD |
| `1D` | `260.50` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 19,000.00 USD | 1,900.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,220.00 USD |
| `1D` | `260.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 9,090.00 USD | 50,950.00 USD | 13,930.00 USD |
| `1D` | `261.30` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,200.00 USD | 29,340.00 USD | 33,390.00 USD |
| `7D` | `261.30` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,550.00 USD |
| `1D` | `261.70` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 15,340.00 USD | 60,900.00 USD | 51,220.00 USD |
| `7D` | `261.80` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 68,120.00 USD | 83,380.00 USD | 45,170.00 USD |
| `1D` | `262.10` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 13,720.00 USD | 28,450.00 USD | 21,370.00 USD |
| `7D` | `262.30` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 43,780.00 USD | 83,970.00 USD | 48,020.00 USD |
| `1D` | `262.50` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 21,220.00 USD | 5,740.00 USD | 10,870.00 USD |
| `7D` | `262.80` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,780.00 USD |
| `1D` | `262.90` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 629.76 USD | 12,770.00 USD | 19,520.00 USD |
| `1D` | `263.30` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,380.00 USD |
| `7D` | `263.30` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 33,590.00 USD | 13,710.00 USD | 221.59 USD |
| `1D` | `263.70` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,500.00 USD |
| `7D` | `263.80` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 391,670.00 USD | 2,510.00 USD | 117,890.00 USD |
| `1D` | `264.10` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,250.00 USD |
| `7D` | `264.30` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 48,230.00 USD | 1,170.00 USD | 89.62 USD |
| `1D` | `264.50` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 1,300.00 USD | 19,920.00 USD | 106.31 USD |
| `7D` | `264.80` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 33,470.00 USD | 21,870.00 USD | 151.90 USD |
| `1D` | `264.90` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 33,320.00 USD | 2,320.00 USD | 53,210.00 USD |
| `1D` | `265.30` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 64,840.00 USD | 2,650.00 USD | 6.46 USD |
| `7D` | `265.30` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 256,440.00 USD | 2,330.00 USD | 33,980.00 USD |
| `1D` | `265.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 187.80 USD | 629.76 USD | 5.13 USD |
| `7D` | `265.80` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 69,380.00 USD | 0.00 USD | 91.75 USD |
| `1D` | `266.10` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 16,330.00 USD | 13,320.00 USD | 5.24 USD |
| `7D` | `266.30` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 216,090.00 USD | 1,450.00 USD | 51.56 USD |
| `1D` | `266.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 14,430.00 USD | 8,820.00 USD | 4,810.00 USD |
| `7D` | `266.80` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 136,640.00 USD | 63,260.00 USD | 51.44 USD |
| `1D` | `266.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 18,470.00 USD | 23,750.00 USD | 1.90 USD |
| `1D` | `267.30` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 33,620.00 USD | 69,850.00 USD | 12,590.00 USD |
| `7D` | `267.30` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 131,280.00 USD | 53,030.00 USD | 93.84 USD |
| `1D` | `267.70` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 10,330.00 USD | 36,440.00 USD | 28,740.00 USD |
| `7D` | `267.80` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,970.00 USD |
| `1D` | `268.10` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 19,060.00 USD | 28,480.00 USD | 59,880.00 USD |
| `7D` | `268.30` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,710.00 USD |
| `1D` | `268.50` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 18,310.00 USD | 18,920.00 USD | 248.37 USD |
| `7D` | `268.80` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 23,340.00 USD | 18,320.00 USD | 83.77 USD |
| `1D` | `268.90` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 21,330.00 USD | 11,500.00 USD | 156.69 USD |
| `1D` | `269.30` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 11,120.00 USD | 2,390.00 USD | 8,420.00 USD |
| `7D` | `269.30` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 3,490.00 USD | 44.11 USD |
| `1D` | `269.70` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 6,500.00 USD | 19,440.00 USD | 13,580.00 USD |
| `7D` | `269.80` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `270.10` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD |
| `1D` | `270.50` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 48,370.00 USD | 2,840.00 USD | 4,930.00 USD |
| `7D` | `270.80` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `270.90` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 505.00 USD | 17,560.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 12,710.00 USD | 1,780.00 USD | 16,960.00 USD |
| `7D` | `271.30` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 8,650.00 USD | 36,810.00 USD | 8,900.00 USD |
| `7D` | `271.80` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 61,810.00 USD | 7,250.00 USD | 61,070.00 USD |
| `1D` | `272.10` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 21,980.00 USD | 24,370.00 USD | 19,750.00 USD |
| `7D` | `272.30` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 6,060.00 USD | 38,280.00 USD | 47,580.00 USD |
| `7D` | `272.80` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `272.90` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 66,940.00 USD | 5,420.00 USD | 71,640.00 USD |
| `1D` | `273.30` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 28,730.00 USD | 121,350.00 USD | 40,460.00 USD |
| `7D` | `273.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD |
| `1D` | `273.70` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 60,550.00 USD | 67,190.00 USD | 69,760.00 USD |
| `7D` | `273.80` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.10` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 152,290.00 USD | 37,550.00 USD | 12,160.00 USD |
| `7D` | `274.30` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 157,790.00 USD | 21,440.00 USD | 54,030.00 USD |
| `7D` | `274.80` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `274.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 54,360.00 USD | 22,510.00 USD | 16,540.00 USD |
| `1D` | `275.30` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 11,720.00 USD | 3,760.00 USD | 6,780.00 USD |
| `7D` | `275.30` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.70` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD |
| `7D` | `275.80` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD |
| `1D` | `276.10` | 974,590.00 USD | 0.00 USD | 974,590.00 USD | 172,570.00 USD | 3,340.00 USD | 7,090.00 USD |
| `7D` | `276.30` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 791,600.00 USD | 0.00 USD | 791,600.00 USD | 11,920.00 USD | 16,150.00 USD | 18,670.00 USD |
| `7D` | `276.80` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 744,860.00 USD | 0.00 USD | 744,860.00 USD | 37,290.00 USD | 25,410.00 USD | 33,920.00 USD |
| `1D` | `277.30` | 648,240.00 USD | 0.00 USD | 648,240.00 USD | 17,610.00 USD | 22,050.00 USD | 17,800.00 USD |
| `7D` | `277.30` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 152,190.00 USD | 77,800.00 USD | 182,060.00 USD |
| `1D` | `277.70` | 590,780.00 USD | 0.00 USD | 590,780.00 USD | 13,750.00 USD | 16,920.00 USD | 20,310.00 USD |
| `7D` | `277.80` | 769,370.00 USD | 0.00 USD | 769,370.00 USD | 0.00 USD | 157,740.00 USD | 59,970.00 USD |
| `1D` | `278.10` | 539,790.00 USD | 0.00 USD | 539,790.00 USD | 12,120.00 USD | 97,470.00 USD | 95,180.00 USD |
| `7D` | `278.30` | 551,660.00 USD | 0.00 USD | 551,660.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD |
| `1D` | `278.50` | 335,020.00 USD | 0.00 USD | 335,020.00 USD | 93,830.00 USD | 56,870.00 USD | 47,890.00 USD |
| `7D` | `278.80` | 334,510.00 USD | 0.00 USD | 334,510.00 USD | 51,310.00 USD | 19,060.00 USD | 49.12 USD |
| `1D` | `278.90` | 136,450.00 USD | 0.00 USD | 136,450.00 USD | 19,260.00 USD | 10,830.00 USD | 43.32 USD |
| `1D` | `279.30` | 106,310.00 USD | 0.00 USD | 106,310.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD |
| `7D` | `279.30` | 264,080.00 USD | 0.00 USD | 264,080.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 65,220.00 USD | 0.00 USD | 65,220.00 USD | 0.00 USD | 0.00 USD | 24,350.00 USD |
| `1D` | `280.10` | 40,880.00 USD | 0.00 USD | 40,880.00 USD | 0.00 USD | 0.00 USD | 31,340.00 USD |
| `7D` | `280.80` | 261,420.00 USD | 0.00 USD | 261,420.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `7D` | `281.30` | 245,880.00 USD | 0.00 USD | 245,880.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD |
| `7D` | `281.80` | 152,050.00 USD | 0.00 USD | 152,050.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 9,540.00 USD | 0.00 USD | 9,540.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.30` | 29,670.00 USD | 0.00 USD | 29,670.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `283.30` | 1,280.00 USD | 0.00 USD | 1,280.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.30` | 5,440.00 USD | 0.00 USD | 5,440.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.80` | 2,000.00 USD | 0.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 15.61 USD | 15.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.61 USD |
| `7D` | `284.30` | 1,570.00 USD | 1,570.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD |
| `1D` | `284.50` | 11,420.00 USD | 11,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,400.00 USD |
| `7D` | `284.80` | 56,960.00 USD | 56,960.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD |
| `1D` | `284.90` | 47,770.00 USD | 47,770.00 USD | 0.00 USD | 28,720.00 USD | 7,620.00 USD | 5.66 USD |
| `1D` | `285.30` | 142,400.00 USD | 142,400.00 USD | 0.00 USD | 36,620.00 USD | 16,320.00 USD | 41,690.00 USD |
| `7D` | `285.30` | 478,930.00 USD | 478,930.00 USD | 0.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD |
| `1D` | `285.70` | 191,400.00 USD | 191,400.00 USD | 0.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD |
| `7D` | `285.80` | 712,480.00 USD | 712,480.00 USD | 0.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD |
| `1D` | `286.10` | 268,000.00 USD | 268,000.00 USD | 0.00 USD | 33,580.00 USD | 3,270.00 USD | 39,750.00 USD |
| `7D` | `286.30` | 756,690.00 USD | 756,690.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD |
| `1D` | `286.50` | 318,830.00 USD | 318,830.00 USD | 0.00 USD | 15,270.00 USD | 5,410.00 USD | 30,150.00 USD |
| `7D` | `286.80` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 473,690.00 USD | 473,690.00 USD | 0.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD |
| `1D` | `287.30` | 660,500.00 USD | 660,500.00 USD | 0.00 USD | 109,280.00 USD | 43,890.00 USD | 33,640.00 USD |
| `7D` | `287.30` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 11.42 USD |
| `1D` | `287.70` | 776,500.00 USD | 776,500.00 USD | 0.00 USD | 22,860.00 USD | 33,420.00 USD | 59,720.00 USD |
| `7D` | `287.80` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.10` | 868,880.00 USD | 868,880.00 USD | 0.00 USD | 21,420.00 USD | 26,660.00 USD | 44,300.00 USD |
| `7D` | `288.30` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD |
| `1D` | `288.50` | 987,410.00 USD | 987,410.00 USD | 0.00 USD | 52,260.00 USD | 29,840.00 USD | 36,430.00 USD |
| `7D` | `288.80` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 122,140.00 USD |
| `1D` | `288.90` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 44,740.00 USD | 30,590.00 USD | 9.45 USD |
| `1D` | `289.30` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 17,220.00 USD | 47,120.00 USD | 51,190.00 USD |
| `7D` | `289.30` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.70` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 67,250.00 USD | 67,790.00 USD | 103,620.00 USD |
| `7D` | `289.80` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD |
| `1D` | `290.10` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 65,110.00 USD | 51,750.00 USD | 114,530.00 USD |
| `7D` | `290.30` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 28,010.00 USD | 120,130.00 USD | 46,650.00 USD |
| `7D` | `290.80` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD |
| `1D` | `290.90` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD |
| `1D` | `291.30` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 27,020.00 USD | 12,070.00 USD | 24,340.00 USD |
| `7D` | `291.30` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD |
| `1D` | `291.70` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 12,850.00 USD | 24,830.00 USD | 30,420.00 USD |
| `7D` | `291.80` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 6,710.00 USD | 39,460.00 USD | 11,500.00 USD |
| `7D` | `292.30` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 49.86 USD |
| `1D` | `292.50` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 29,880.00 USD | 3,650.00 USD | 2,250.00 USD |
| `7D` | `292.80` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 126.47 USD |
| `1D` | `292.90` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 62,510.00 USD | 30,990.00 USD | 3,570.00 USD |
| `1D` | `293.30` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 27,950.00 USD | 23,500.00 USD | 32,300.00 USD |
| `7D` | `293.30` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 33,580.00 USD | 132,770.00 USD | 100.96 USD |
| `1D` | `293.70` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 76,710.00 USD | 47,640.00 USD | 70,130.00 USD |
| `7D` | `293.80` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 20,910.00 USD |
| `1D` | `294.10` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 21,460.00 USD | 25,650.00 USD | 52,800.00 USD |
| `7D` | `294.30` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 217,140.00 USD | 42,290.00 USD | 166,760.00 USD |
| `1D` | `294.50` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 96,690.00 USD | 80,200.00 USD | 85,220.00 USD |
| `7D` | `294.80` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,170.00 USD |
| `1D` | `294.90` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 33,490.00 USD | 17,570.00 USD | 48,710.00 USD |
| `1D` | `295.30` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 15,750.00 USD | 62,250.00 USD | 102,520.00 USD |
| `7D` | `295.30` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 46,330.00 USD | 83,600.00 USD | 345,600.00 USD |
| `1D` | `295.70` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 106,670.00 USD | 7,020.00 USD | 128,480.00 USD |
| `7D` | `295.80` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 165,320.00 USD | 82,100.00 USD | 197,370.00 USD |
| `1D` | `296.10` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 52,840.00 USD | 126,740.00 USD | 35,530.00 USD |
| `7D` | `296.30` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 43,710.00 USD | 167,940.00 USD | 121,050.00 USD |
| `1D` | `296.50` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 33,430.00 USD | 22,420.00 USD | 41,220.00 USD |
| `7D` | `296.80` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 133,820.00 USD | 4,410.00 USD | 201,460.00 USD |
| `1D` | `296.90` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 24,280.00 USD | 21,780.00 USD | 90,570.00 USD |
| `1D` | `297.30` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 61,380.00 USD | 1,000.00 USD | 31,550.00 USD |
| `7D` | `297.30` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 78,980.00 USD | 54,960.00 USD | 5.22 USD |
| `1D` | `297.70` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 15,920.00 USD | 11,340.00 USD | 12,210.00 USD |
| `7D` | `297.80` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 47,530.00 USD | 99,810.00 USD | 89,620.00 USD |
| `1D` | `298.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 51,960.00 USD | 10,200.00 USD | 41,580.00 USD |
| `7D` | `298.30` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 32,650.00 USD | 45,150.00 USD | 68,830.00 USD |
| `1D` | `298.50` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 5,730.00 USD | 1,480.00 USD | 56,400.00 USD |
| `7D` | `298.80` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 106.61 USD |
| `1D` | `298.90` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 28,220.00 USD | 5,580.00 USD | 94,690.00 USD |
| `1D` | `299.30` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 34,110.00 USD | 11,020.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 3,550.00 USD | 27,070.00 USD | 85,830.00 USD |
| `1D` | `299.70` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 8,350.00 USD | 11,780.00 USD | 27,680.00 USD |
| `7D` | `299.80` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 22,060.00 USD | 9,100.00 USD | 19,850.00 USD |
| `1D` | `300.10` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 20,020.00 USD | 37,550.00 USD | 64,320.00 USD |
| `7D` | `300.30` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 35,320.00 USD | 3,530.00 USD | 101.15 USD |
| `1D` | `300.50` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 23,270.00 USD | 1,700.00 USD | 17,180.00 USD |
| `7D` | `300.80` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,430.00 USD |
| `1D` | `300.90` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 269.05 USD | 1,020.00 USD | 29,350.00 USD |
| `1D` | `301.30` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 693.10 USD | 15,110.00 USD | 20,910.00 USD |
| `7D` | `301.30` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 73,320.00 USD | 58,690.00 USD | 150,550.00 USD |
| `1D` | `301.70` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 19,840.00 USD | 8,470.00 USD | 15,630.00 USD |
| `7D` | `301.80` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 89,300.00 USD | 131,150.00 USD | 26,380.00 USD |
| `1D` | `302.10` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 25,190.00 USD | 30,660.00 USD | 10,410.00 USD |
| `7D` | `302.30` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 1,560.00 USD | 181,550.00 USD | 12.67 USD |
| `1D` | `302.50` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 13,920.00 USD | 13,290.00 USD | 38,480.00 USD |
| `7D` | `302.80` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,830.00 USD |
| `1D` | `302.90` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 1,370.00 USD | 2,410.00 USD | 13,970.00 USD |
| `1D` | `303.30` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 21,200.00 USD | 2,760.00 USD | 9,350.00 USD |
| `7D` | `303.30` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD | 96.05 USD |
| `1D` | `303.70` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 391.16 USD | 8.92 USD |
| `7D` | `303.80` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,690.00 USD |
| `1D` | `304.10` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,440.00 USD |
| `1D` | `304.50` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 9,670.00 USD | 2,100.00 USD | 44,520.00 USD |
| `7D` | `304.80` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 35,470.00 USD | 11,790.00 USD | 4,060.00 USD |
| `1D` | `304.90` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD |
| `1D` | `305.30` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 83.23 USD | 172.52 USD | 2.65 USD |
| `7D` | `305.30` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,420.00 USD |
| `1D` | `305.70` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 6,340.00 USD | 3,500.00 USD | 5,870.00 USD |
| `7D` | `305.80` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 80,680.00 USD | 52,160.00 USD | 12,830.00 USD |
| `1D` | `306.10` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD |
| `1D` | `306.50` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 4,330.00 USD | 6.13 USD | 5,670.00 USD |
| `7D` | `306.80` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 94,690.00 USD | 74,510.00 USD | 69,930.00 USD |
| `1D` | `306.90` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 19,810.00 USD | 35,610.00 USD | 18,580.00 USD |
| `1D` | `307.30` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 11,240.00 USD | 32,670.00 USD | 22,250.00 USD |
| `7D` | `307.30` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 27,410.00 USD | 136,370.00 USD | 147,540.00 USD |
| `1D` | `307.70` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 24,280.00 USD | 20,210.00 USD | 3,730.00 USD |
| `7D` | `307.80` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 127,080.00 USD | 113,210.00 USD | 60,760.00 USD |
| `1D` | `308.10` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 14,750.00 USD | 4,740.00 USD | 12,420.00 USD |
| `7D` | `308.30` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 169,010.00 USD | 67,070.00 USD | 114,150.00 USD |
| `1D` | `308.50` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD |
| `7D` | `308.80` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,080.00 USD |
| `1D` | `308.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 7,510.00 USD | 6,640.00 USD | 3,490.00 USD |
| `1D` | `309.30` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 3,240.00 USD | 2,300.00 USD | 2,160.00 USD |
| `7D` | `309.30` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 34,260.00 USD | 36,030.00 USD | 36,670.00 USD |
| `1D` | `309.70` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 10,120.00 USD | 7,760.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,740.00 USD |
| `1D` | `310.10` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 14,750.00 USD | 6,170.00 USD | 12,940.00 USD |
| `7D` | `310.30` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 62,230.00 USD | 108,410.00 USD | 80,850.00 USD |
| `1D` | `310.50` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 176.40 USD | 5,020.00 USD | 5,790.00 USD |
| `7D` | `310.80` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 12,240.00 USD |
| `1D` | `310.90` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 5,080.00 USD | 73.70 USD | 2,180.00 USD |
| `1D` | `311.30` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 257.90 USD | 3,110.00 USD | 1,480.00 USD |
| `7D` | `311.30` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 72,080.00 USD |
| `1D` | `311.70` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 7,980.00 USD | 10,260.00 USD | 4,140.00 USD |
| `7D` | `311.80` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 19,570.00 USD | 11,240.00 USD | 25,520.00 USD |
| `1D` | `312.10` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 299.35 USD | 10,430.00 USD | 15,040.00 USD |
| `7D` | `312.30` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 27,490.00 USD |
| `1D` | `312.50` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 17,660.00 USD | 8,480.00 USD | 14,080.00 USD |
| `7D` | `312.80` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 21,990.00 USD | 14,880.00 USD | 19,310.00 USD |
| `1D` | `312.90` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD |
| `1D` | `313.30` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 3,580.00 USD | 18,130.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD |
| `1D` | `313.70` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 8,220.00 USD |
| `7D` | `313.80` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 32,780.00 USD | 1,570.00 USD | 44,160.00 USD |
| `7D` | `314.30` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `7D` | `314.80` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 17,720.00 USD | 0.00 USD | 10,270.00 USD |
| `7D` | `315.30` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 547.95 USD | 52.52 USD |
| `7D` | `315.80` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 1,670.00 USD | 33,700.00 USD | 29,990.00 USD |
| `7D` | `316.30` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD |
| `7D` | `316.80` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD |
| `7D` | `317.30` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 173.04 USD |
| `7D` | `317.80` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 21,110.00 USD | 8,380.00 USD | 5.74 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `306.41M` | Total OI Tokens: `1,078,572.5 BCH`
  * 1h OI Change: `+1.50%` | 4h OI Change: `-0.66%` | 24h OI Change: `+0.22%`
  * Exchange Breakdown: Binance=`88.90M` | Bybit=`38.08M` | OKX=`23.98M` | Hyperliquid=`7.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.29K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0095%` |
| **USDT Bybit** | `0.0067%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0090%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `54.81%` | `45.19%` | `1.21` | 1,770,000.00 USD |
| `15M` | `Binance` | `41.16%` | `58.84%` | `0.70` | 287,090.00 USD |
| `15M` | `OKX` | `43.39%` | `56.61%` | `0.77` | 250,640.00 USD |
| `15M` | `Bybit` | `44.9%` | `55.1%` | `0.81` | 79,760.00 USD |
| `15M` | `KuCoin` | `65.33%` | `34.67%` | `1.88` | 254,130.00 USD |
| `15M` | `Gate` | `69.54%` | `30.46%` | `2.28` | 12,010.00 USD |
| `15M` | `Bitget` | `67.51%` | `32.49%` | `2.08` | 21,420.00 USD |
| `15M` | `BingX` | `50.85%` | `49.15%` | `1.03` | 112,670.00 USD |
| `15M` | `MEXC` | `81.09%` | `18.91%` | `4.29` | 36,650.00 USD |
| `15M` | `Bitunix` | `56.91%` | `43.09%` | `1.32` | 30,500.00 USD |
| `15M` | `Hyperliquid` | `40.54%` | `59.46%` | `0.68` | 7,520.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.86%` | `50.14%` | `0.99` | 523,700.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.23%` | `0.77%` | `128.87` | 130,050.00 USD |
| `15M` | `HTX` | `30.19%` | `69.81%` | `0.43` | 979.31 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `81.16%` | `18.84%` | `4.31` | 4,670.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 842.34 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 14,600.00 USD |
| `15M` | `Whale Positions` | `41.16%` | `58.84%` | `0.70` | 287,090.00 USD |
| `15M` | `Global Accounts` | `54.81%` | `45.19%` | `1.21` | 1,770,000.00 USD |
| `1H` | `BCH` | `46.57%` | `53.43%` | `0.87` | 15,330,000.00 USD |
| `1H` | `Binance` | `43.61%` | `56.39%` | `0.77` | 4,360,000.00 USD |
| `1H` | `OKX` | `42.62%` | `57.38%` | `0.74` | 1,350,000.00 USD |
| `1H` | `Bybit` | `40.79%` | `59.21%` | `0.69` | 1,340,000.00 USD |
| `1H` | `KuCoin` | `50.71%` | `49.29%` | `1.03` | 100,580.00 USD |
| `1H` | `Gate` | `49.96%` | `50.04%` | `1.00` | 1,150,000.00 USD |
| `1H` | `Bitget` | `39.04%` | `60.96%` | `0.64` | 314,400.00 USD |
| `1H` | `BingX` | `27.14%` | `72.86%` | `0.37` | 3,310,000.00 USD |
| `1H` | `MEXC` | `75.8%` | `24.2%` | `3.13` | 307,820.00 USD |
| `1H` | `Bitunix` | `71.97%` | `28.03%` | `2.57` | 332,290.00 USD |
| `1H` | `Hyperliquid` | `40.09%` | `59.91%` | `0.67` | 51,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.77%` | `50.23%` | `0.99` | 274,410.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.36%` | `2.64%` | `36.88` | 1,580,000.00 USD |
| `1H` | `HTX` | `51.14%` | `48.86%` | `1.05` | 48,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `56.19%` | `43.81%` | `1.28` | 157,270.00 USD |
| `1H` | `Aster` | `63.83%` | `36.17%` | `1.76` | 11,980.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `27.83%` | `72.17%` | `0.39` | 634,370.00 USD |
| `1H` | `Whale Positions` | `43.61%` | `56.39%` | `0.77` | 4,360,000.00 USD |
| `1H` | `Global Accounts` | `46.57%` | `53.43%` | `0.87` | 15,330,000.00 USD |
| `4H` | `BCH` | `47.70%` | `52.30%` | `0.91` | 46,140,000.00 USD |
| `4H` | `Binance` | `47.86%` | `52.14%` | `0.92` | 13,000,000.00 USD |
| `4H` | `OKX` | `39.62%` | `60.38%` | `0.66` | 4,470,000.00 USD |
| `4H` | `Bybit` | `46.39%` | `53.61%` | `0.87` | 3,650,000.00 USD |
| `4H` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 315,610.00 USD |
| `4H` | `Gate` | `51.27%` | `48.73%` | `1.05` | 4,150,000.00 USD |
| `4H` | `Bitget` | `42.89%` | `57.11%` | `0.75` | 1,360,000.00 USD |
| `4H` | `BingX` | `33.64%` | `66.36%` | `0.51` | 10,760,000.00 USD |
| `4H` | `MEXC` | `57.96%` | `42.04%` | `1.38` | 1,150,000.00 USD |
| `4H` | `Bitunix` | `47.5%` | `52.5%` | `0.90` | 967,350.00 USD |
| `4H` | `Hyperliquid` | `45.04%` | `54.96%` | `0.82` | 370,400.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.76%` | `49.24%` | `1.03` | 1,080,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.83%` | `6.17%` | `15.21` | 3,860,000.00 USD |
| `4H` | `HTX` | `43.58%` | `56.42%` | `0.77` | 84,440.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.46%` | `37.54%` | `1.66` | 244,300.00 USD |
| `4H` | `Aster` | `45.78%` | `54.22%` | `0.84` | 28,160.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.65%` | `72.35%` | `0.38` | 645,830.00 USD |
| `4H` | `Whale Positions` | `47.86%` | `52.14%` | `0.92` | 13,000,000.00 USD |
| `4H` | `Global Accounts` | `47.70%` | `52.30%` | `0.91` | 46,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `283.12` | `282.91` | `283.12` | `283.64` | `281.86` | 898,717.53 USD | 422,080.39 USD | 476,637.13 USD | -54,556.74 USD | `-6.07%` | `22B / 36S` |
| `0:00 UTC` | `280.81` | `281.09` | `280.81` | `281.94` | `280.02` | 959,751.07 USD | 348,775.30 USD | 610,975.78 USD | -262,200.48 USD | `-27.32%` | `10B / 71S` |
| `5:00 UTC` | `278.88` | `279.51` | `278.88` | `280.56` | `278.74` | 1,525,848.29 USD | 843,855.80 USD | 681,992.49 USD | 161,863.30 USD | `+10.61%` | `26B / 51S` |
| `0:00 UTC` | `281.21` | `280.32` | `281.21` | `281.29` | `278.55` | 1,960,555.94 USD | 896,979.92 USD | 1,063,576.02 USD | -166,596.10 USD | `-8.50%` | `26B / 22S` |
| `5:00 UTC` | `279.18` | `279.58` | `279.18` | `280.70` | `279.06` | 617,038.04 USD | 332,886.00 USD | 284,152.04 USD | 48,733.95 USD | `+7.90%` | `32B / 38S` |
| `0:00 UTC` | `279.30` | `281.19` | `279.30` | `282.30` | `278.88` | 2,044,095.31 USD | 958,971.19 USD | 1,085,124.12 USD | -126,152.93 USD | `-6.17%` | `39B / 29S` |
| `5:00 UTC` | `281.23` | `281.19` | `281.23` | `281.62` | `280.50` | 432,406.23 USD | 225,151.97 USD | 207,254.26 USD | 17,897.70 USD | `+4.14%` | `20B / 20S` |
| `0:00 UTC` | `281.00` | `280.46` | `281.00` | `281.14` | `280.02` | 480,699.25 USD | 262,884.90 USD | 217,814.34 USD | 45,070.56 USD | `+9.38%` | `19B / 14S` |
| `5:00 UTC` | `282.00` | `281.11` | `282.00` | `282.22` | `280.16` | 658,245.44 USD | 414,390.84 USD | 243,854.60 USD | 170,536.24 USD | `+25.91%` | `33B / 5S` |
| `0:00 UTC` | `283.69` | `283.43` | `283.69` | `284.61` | `281.57` | 1,122,165.59 USD | 613,630.60 USD | 508,534.99 USD | 105,095.60 USD | `+9.37%` | `48B / 25S` |

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
| `5m` | 42,270.00 USD | 7,780.00 USD | **`ACCUMULATION`** |
| `15m` | 97,950.00 USD | 160,960.00 USD | **`ACCUMULATION`** |
| `30m` | 103,480.00 USD | 185,260.00 USD | **`ACCUMULATION`** |
| `1h` | 139,820.00 USD | 107,600.00 USD | **`ACCUMULATION`** |
| `2h` | -70,700.00 USD | -353,790.00 USD | **`DISTRIBUTION`** |
| `4h` | 134,390.00 USD | -447,660.00 USD | **`DISTRIBUTION`** |
| `6h` | 227,280.00 USD | 425,930.00 USD | **`ACCUMULATION`** |
| `8h` | 1,100,000.00 USD | 1,260,000.00 USD | **`ACCUMULATION`** |
| `12h` | 574,640.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 210,540.00 USD | -2,020,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -185,250.00 USD | -13,630,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,810,000.00 USD | -137,580,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+42.27K` | 15m=`+97.95K` | 1h=`+139.82K` | 24h=`+210.54K`
* Futures Capital Netflows: 5m=`+7.78K` | 15m=`+160.96K` | 1h=`+107.60K` | 24h=`-2.02M`
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
  * Execution Entry: `273.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `271.00` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `278.25`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `284.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `286.51` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `279.26`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`286.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
