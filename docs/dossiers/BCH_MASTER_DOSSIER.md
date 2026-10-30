# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 15:33:13 IST` (`2026-10-30 10:03:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `280.76` | **Live Ask Quote**: `281.34` | **Mid Price**: `281.05`
- **Spread Points**: `580.00` | **Spread BPS**: `20.64 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `276.64` | VWAP Z-Score: `+0.69` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.17` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.52` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.01` | Lower -3.00σ Band: `258.27`
  * Upper +2.51σ Band: `292.01` | Lower -2.51σ Band: `261.27`
  * Upper +2.01σ Band: `288.94` | Lower -2.01σ Band: `264.33`
  * Upper +2.00σ Band: `288.88` | Lower -2.00σ Band: `264.39`
  * Upper +1.28σ Band: `284.48` | Lower -1.28σ Band: `268.80`
  * Upper +1.00σ Band: `282.76` | Lower -1.00σ Band: `270.52`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`280.52` | EMA-20=`280.88` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.29` (Slope: `+0.0000`) | EMA-100=`280.82`
  * Institutional Anchors: EMA-144=`281.71` | EMA-200=`283.31` (Slope: `-0.0971`) | EMA-233=`284.22`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `284.44` (Distance: `-1.19%`)
  * Point of Control (POC) = `276.23` (Distance: `+1.75%`)
  * Value Area Low (VAL) = `272.91` (Distance: `+2.98%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`282.74` | Low=`279.36`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `279.93` - `282.17`
  * Optimal Trade Entry (OTE 0.705): `281.61`
  * Structural Invalidation Anchor (0.786): `283.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `281.40` | `281.51` | `280.50` | `281.28` | `590` | 165,808.43 USD | 4,093.26 USD | `+2.47%` | -1,790,273.13 USD | `+0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `281.21` | `281.61` | `280.90` | `281.34` | `527` | 148,403.17 USD | 38,790.12 USD | `+26.14%` | -1,751,483.01 USD | `+0.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `281.34` | `281.40` | `281.02` | `281.22` | `393` | 110,436.40 USD | -17,407.97 USD | `-15.76%` | -1,768,890.98 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `280.08` | `280.70` | `279.05` | `279.56` | `2,207` | 617,038.04 USD | 48,733.95 USD | `+7.90%` | -1,668,213.46 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `279.56` | `282.29` | `278.87` | `281.40` | `7,270` | 2,044,095.31 USD | -126,152.93 USD | `-6.17%` | -1,794,366.39 USD | `-0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `281.40` | `281.61` | `280.50` | `281.22` | `1,510` | 424,648.00 USD | 25,475.41 USD | `+6.00%` | -1,768,890.98 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `283.68` | `284.86` | `280.79` | `281.78` | `11,868` | 3,357,238.13 USD | -360,522.64 USD | `-10.74%` | -1,826,347.97 USD | `-0.33` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `278.73` | `279.02` | `16,468` | 4,630,594.81 USD | 275,996.65 USD | `+5.96%` | -1,550,351.32 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `279.03` | `282.29` | `278.54` | `281.22` | `17,981` | 5,046,337.30 USD | -218,539.66 USD | `-4.33%` | -1,768,890.98 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `281.22` | `34,449` | 9,676,932.11 USD | 57,456.99 USD | `+0.59%` | -1,682,453.65 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `281.22` | `34,449` | 9,676,932.11 USD | 57,456.99 USD | `+0.59%` | -1,682,453.65 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`281.05`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1965` | `0x12d2...f97f` | `LONG` | 1,017,695.57 USD | `3,627,243,000,000.00` | `303.26` | `280.35` | `0.000000` | -82,303.77 USD | `-8.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+2.68%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--5.64%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+2.66%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.61%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+2.66%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.61%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+2.66%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.61%`)
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
| `7D` | `Long Liquidation` | `234.80` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 182.78 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 10,160,000.00 USD | 10,160,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 10,140,000.00 USD | 10,140,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 10,120,000.00 USD | 10,120,000.00 USD | 196.53 USD | 17,300.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 69,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 10,090,000.00 USD | 10,090,000.00 USD | 5,120.00 USD | 146.67 USD | 11.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 10,080,000.00 USD | 10,080,000.00 USD | 178.62 USD | 6,570.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `238.50` | 10,840.00 USD | 45,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `238.80` | 10,060,000.00 USD | 10,060,000.00 USD | 140.10 USD | 9,360.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 10,030,000.00 USD | 10,030,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 34,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,020,000.00 USD | 10,020,000.00 USD | 2,780.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 10,010,000.00 USD | 10,010,000.00 USD | 7,150.00 USD | 1,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 33,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 10,000,000.00 USD | 10,000,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 9,990,000.00 USD | 9,990,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.80` | 9,910,000.00 USD | 9,910,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 3,380.00 USD | 33,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 9,880,000.00 USD | 9,880,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 29,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 9,830,000.00 USD | 9,830,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 9,810,000.00 USD | 9,810,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 9,780,000.00 USD | 9,780,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 9,770,000.00 USD | 9,770,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 9,720,000.00 USD | 9,720,000.00 USD | 4,590.00 USD | 472.85 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 9,710,000.00 USD | 9,710,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,670,000.00 USD | 9,670,000.00 USD | 3,560.00 USD | 4,920.00 USD | 15.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,670,000.00 USD | 9,670,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,650,000.00 USD | 9,650,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,540,000.00 USD | 9,540,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,470,000.00 USD | 9,470,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,350,000.00 USD | 9,350,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 23,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.60` | 5,010,000.00 USD | 5,010,000.00 USD | 12,560.00 USD | 4,800.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,260,000.00 USD | 9,260,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.00` | 4,980,000.00 USD | 4,980,000.00 USD | 19,730.00 USD | 35,980.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 9,130,000.00 USD | 9,130,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.40` | 4,900,000.00 USD | 4,900,000.00 USD | 11,280.00 USD | 22,200.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.80` | 4,840,000.00 USD | 4,840,000.00 USD | 36,220.00 USD | 48,630.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.80` | 8,980,000.00 USD | 8,980,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.20` | 4,750,000.00 USD | 4,750,000.00 USD | 11,510.00 USD | 816.08 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 8,770,000.00 USD | 8,770,000.00 USD | 69,530.00 USD | 40,300.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.60` | 4,730,000.00 USD | 4,730,000.00 USD | 13,380.00 USD | 1,610.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,640,000.00 USD | 8,640,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.00` | 4,710,000.00 USD | 4,710,000.00 USD | 4,490.00 USD | 7,620.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,560,000.00 USD | 8,560,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.40` | 4,690,000.00 USD | 4,690,000.00 USD | 20,170.00 USD | 19,940.00 USD | 14,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.80` | 4,640,000.00 USD | 4,640,000.00 USD | 10,400.00 USD | 5,980.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,450,000.00 USD | 8,450,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.20` | 4,610,000.00 USD | 4,610,000.00 USD | 1,590.00 USD | 5,370.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,370,000.00 USD | 8,370,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.60` | 4,600,000.00 USD | 4,600,000.00 USD | 9,130.00 USD | 13,490.00 USD | 34.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,240,000.00 USD | 8,240,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.00` | 4,570,000.00 USD | 4,570,000.00 USD | 14,600.00 USD | 10,470.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 8,080,000.00 USD | 8,080,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.40` | 4,540,000.00 USD | 4,540,000.00 USD | 3,550.00 USD | 25,240.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.80` | 4,490,000.00 USD | 4,490,000.00 USD | 21,840.00 USD | 11,170.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 7,990,000.00 USD | 7,990,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.20` | 4,440,000.00 USD | 4,440,000.00 USD | 2,620.00 USD | 39,280.00 USD | 17,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 7,930,000.00 USD | 7,930,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.60` | 4,380,000.00 USD | 4,380,000.00 USD | 8,400.00 USD | 8,320.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 7,840,000.00 USD | 7,840,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.00` | 4,360,000.00 USD | 4,360,000.00 USD | 9,580.00 USD | 1,470.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 7,730,000.00 USD | 7,730,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.40` | 4,330,000.00 USD | 4,330,000.00 USD | 6,290.00 USD | 4,650.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.80` | 4,310,000.00 USD | 4,310,000.00 USD | 1,500.00 USD | 2,430.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,690,000.00 USD | 7,690,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.20` | 4,300,000.00 USD | 4,300,000.00 USD | 21,220.00 USD | 15,910.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,630,000.00 USD | 7,630,000.00 USD | 106,080.00 USD | 37,040.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 645.99 USD | 17,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.60` | 4,210,000.00 USD | 4,210,000.00 USD | 25,120.00 USD | 8,900.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,410,000.00 USD | 7,410,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.00` | 4,140,000.00 USD | 4,140,000.00 USD | 12,700.00 USD | 34,640.00 USD | 7.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,240,000.00 USD | 7,240,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.40` | 4,090,000.00 USD | 4,090,000.00 USD | 14,770.00 USD | 3,590.00 USD | 17,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.80` | 4,050,000.00 USD | 4,050,000.00 USD | 41,960.00 USD | 32,130.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 7,180,000.00 USD | 7,180,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.20` | 3,940,000.00 USD | 3,940,000.00 USD | 4,650.00 USD | 8,250.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 7,020,000.00 USD | 7,020,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,340.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.60` | 3,920,000.00 USD | 3,920,000.00 USD | 20,190.00 USD | 7,070.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 6,800,000.00 USD | 6,800,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.00` | 3,860,000.00 USD | 3,860,000.00 USD | 8,270.00 USD | 49,100.00 USD | 44,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,670,000.00 USD | 6,670,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.40` | 3,760,000.00 USD | 3,760,000.00 USD | 7,870.00 USD | 43,640.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.80` | 3,710,000.00 USD | 3,710,000.00 USD | 15,440.00 USD | 47,400.00 USD | 62,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,510,000.00 USD | 6,510,000.00 USD | 68,120.00 USD | 83,380.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.20` | 3,580,000.00 USD | 3,580,000.00 USD | 34,470.00 USD | 28,550.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,310,000.00 USD | 6,310,000.00 USD | 43,780.00 USD | 83,970.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.60` | 3,500,000.00 USD | 3,500,000.00 USD | 738.08 USD | 1,680.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,140,000.00 USD | 6,140,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.00` | 3,480,000.00 USD | 3,480,000.00 USD | 8,930.00 USD | 12,640.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 5,980,000.00 USD | 5,980,000.00 USD | 33,590.00 USD | 13,710.00 USD | 118.53 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.40` | 3,460,000.00 USD | 3,460,000.00 USD | 30,700.00 USD | 4,190.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `263.50` | 464.81 USD | 13,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `263.80` | 3,350,000.00 USD | 3,350,000.00 USD | 32,740.00 USD | 30,130.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 5,930,000.00 USD | 5,930,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.20` | 3,260,000.00 USD | 3,260,000.00 USD | 25,990.00 USD | 15,550.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,420,000.00 USD | 5,420,000.00 USD | 48,230.00 USD | 1,170.00 USD | 88.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.60` | 3,200,000.00 USD | 3,200,000.00 USD | 1,520.00 USD | 19,920.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,370,000.00 USD | 5,370,000.00 USD | 33,470.00 USD | 21,870.00 USD | 147.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.00` | 3,160,000.00 USD | 3,160,000.00 USD | 33,010.00 USD | 2,110.00 USD | 33,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,320,000.00 USD | 5,320,000.00 USD | 256,440.00 USD | 2,330.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.40` | 3,090,000.00 USD | 3,090,000.00 USD | 64,890.00 USD | 2,970.00 USD | 16.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.80` | 3,020,000.00 USD | 3,020,000.00 USD | 12,120.00 USD | 313.30 USD | 5.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 5,030,000.00 USD | 5,030,000.00 USD | 69,380.00 USD | 0.00 USD | 75.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.20` | 3,010,000.00 USD | 3,010,000.00 USD | 4,210.00 USD | 13,450.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 4,960,000.00 USD | 4,960,000.00 USD | 216,090.00 USD | 1,450.00 USD | 238.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.60` | 2,980,000.00 USD | 2,980,000.00 USD | 14,560.00 USD | 8,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 4,740,000.00 USD | 4,740,000.00 USD | 136,640.00 USD | 63,260.00 USD | 136.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.00` | 2,960,000.00 USD | 2,960,000.00 USD | 44,140.00 USD | 25,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,540,000.00 USD | 4,540,000.00 USD | 131,280.00 USD | 53,030.00 USD | 118.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.40` | 2,890,000.00 USD | 2,890,000.00 USD | 7,810.00 USD | 68,360.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.80` | 2,790,000.00 USD | 2,790,000.00 USD | 10,330.00 USD | 40,070.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,350,000.00 USD | 4,350,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.20` | 2,720,000.00 USD | 2,720,000.00 USD | 24,330.00 USD | 35,070.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,060,000.00 USD | 4,060,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.60` | 2,600,000.00 USD | 2,600,000.00 USD | 25,840.00 USD | 19,230.00 USD | 85.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,620,000.00 USD | 3,620,000.00 USD | 23,340.00 USD | 17,480.00 USD | 116.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.00` | 2,560,000.00 USD | 2,560,000.00 USD | 8,580.00 USD | 669.20 USD | 124.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 3,490.00 USD | 129.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.40` | 2,550,000.00 USD | 2,550,000.00 USD | 13,400.00 USD | 16,910.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.80` | 2,500,000.00 USD | 2,500,000.00 USD | 711.50 USD | 1,470.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.20` | 2,500,000.00 USD | 2,500,000.00 USD | 24,670.00 USD | 13,340.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.60` | 2,460,000.00 USD | 2,460,000.00 USD | 40,360.00 USD | 118.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,570,000.00 USD | 3,570,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.00` | 2,410,000.00 USD | 2,410,000.00 USD | 505.00 USD | 14,830.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.40` | 2,390,000.00 USD | 2,390,000.00 USD | 12,710.00 USD | 1,780.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.80` | 2,370,000.00 USD | 2,370,000.00 USD | 13,310.00 USD | 34,920.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,520,000.00 USD | 3,520,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.20` | 2,310,000.00 USD | 2,310,000.00 USD | 17,320.00 USD | 31,900.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.60` | 2,250,000.00 USD | 2,250,000.00 USD | 27,370.00 USD | 27,760.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,380,000.00 USD | 3,380,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.00` | 2,130,000.00 USD | 2,130,000.00 USD | 42,140.00 USD | 27,210.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.40` | 2,010,000.00 USD | 2,010,000.00 USD | 24,670.00 USD | 107,180.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.80` | 1,840,000.00 USD | 1,840,000.00 USD | 79,850.00 USD | 80,800.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 2,880,000.00 USD | 2,880,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.20` | 1,610,000.00 USD | 1,610,000.00 USD | 244,400.00 USD | 37,750.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,610,000.00 USD | 2,610,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.60` | 1,300,000.00 USD | 1,300,000.00 USD | 117,810.00 USD | 19,960.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 1,950,000.00 USD | 1,950,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.00` | 1,120,000.00 USD | 1,120,000.00 USD | 38,980.00 USD | 0.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,420,000.00 USD | 1,420,000.00 USD | 59,580.00 USD | 19,960.00 USD | 10.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.40` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.80` | 1,050,000.00 USD | 1,050,000.00 USD | 53,120.00 USD | 34,910.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,340,000.00 USD | 1,340,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.20` | 917,230.00 USD | 917,230.00 USD | 166,790.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,230,000.00 USD | 1,230,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.60` | 747,220.00 USD | 747,220.00 USD | 11,880.00 USD | 22,740.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 910,640.00 USD | 910,640.00 USD | 16,100.00 USD | 0.00 USD | 10.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.00` | 707,010.00 USD | 707,010.00 USD | 25,410.00 USD | 7,900.00 USD | 34,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 894,530.00 USD | 894,530.00 USD | 152,190.00 USD | 77,800.00 USD | 140,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.40` | 639,630.00 USD | 639,630.00 USD | 26,920.00 USD | 18,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.80` | 594,450.00 USD | 594,450.00 USD | 4,440.00 USD | 31,980.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 523,560.00 USD | 523,560.00 USD | 0.00 USD | 157,740.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.20` | 537,720.00 USD | 537,720.00 USD | 12,120.00 USD | 88,410.00 USD | 83,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 305,880.00 USD | 305,880.00 USD | 24,750.00 USD | 37,090.00 USD | 155,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.60` | 353,540.00 USD | 353,540.00 USD | 88,160.00 USD | 55,720.00 USD | 47,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 88,580.00 USD | 88,580.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.00` | 161,790.00 USD | 161,790.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 18,200.00 USD | 18,200.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.40` | 151,960.00 USD | 151,960.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.80` | 110,880.00 USD | 110,880.00 USD | 0.00 USD | 0.00 USD | 55,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.60` | 55,230.00 USD | 55,230.00 USD | 0.00 USD | 48,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 15,540.00 USD | 15,540.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.00` | 7,020.00 USD | 7,020.00 USD | 0.00 USD | 7,010.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.30` | 93,830.00 USD | 93,830.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.30` | 187,650.00 USD | 187,650.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.80` | 4,140.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.80` | 310,040.00 USD | 310,040.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.20` | 12,400.00 USD | 12,400.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.30` | 334,260.00 USD | 334,260.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.30` | 337,850.00 USD | 337,850.00 USD | 3,450.00 USD | 0.00 USD | 141.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.40` | 13,700.00 USD | 13,700.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 339,850.00 USD | 339,850.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 341,420.00 USD | 341,420.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.60` | 59,520.00 USD | 59,520.00 USD | 10,630.00 USD | 7,620.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 396,880.00 USD | 396,880.00 USD | 0.00 USD | 55,390.00 USD | 65.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.00` | 99,060.00 USD | 99,060.00 USD | 39,520.00 USD | 0.00 USD | 9.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 818,840.00 USD | 818,840.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.40` | 230,170.00 USD | 230,170.00 USD | 51,680.00 USD | 37,750.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.80` | 250,420.00 USD | 250,420.00 USD | 1,710.00 USD | 434.90 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 1,050,000.00 USD | 1,050,000.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.20` | 308,140.00 USD | 308,140.00 USD | 39,790.00 USD | 284.90 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 1,100,000.00 USD | 1,100,000.00 USD | 1,200.00 USD | 43,020.00 USD | 11.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.60` | 342,500.00 USD | 342,500.00 USD | 2,290.00 USD | 1,930.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,340,000.00 USD | 1,340,000.00 USD | 30,110.00 USD | 217,580.00 USD | 2.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.00` | 557,070.00 USD | 557,070.00 USD | 65,140.00 USD | 61,640.00 USD | 87,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,540,000.00 USD | 1,540,000.00 USD | 82,910.00 USD | 116,440.00 USD | 103.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.40` | 699,430.00 USD | 699,430.00 USD | 101,280.00 USD | 12,420.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.80` | 797,880.00 USD | 797,880.00 USD | 13,160.00 USD | 27,060.00 USD | 58,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,940,000.00 USD | 1,940,000.00 USD | 70,340.00 USD | 272,200.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.20` | 914,150.00 USD | 914,150.00 USD | 69,440.00 USD | 23,420.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.60` | 982,770.00 USD | 982,770.00 USD | 6,190.00 USD | 33,200.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 2,240,000.00 USD | 2,240,000.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.00` | 1,070,000.00 USD | 1,070,000.00 USD | 42,790.00 USD | 31,570.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.40` | 1,270,000.00 USD | 1,270,000.00 USD | 25,800.00 USD | 59,890.00 USD | 116,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.80` | 1,440,000.00 USD | 1,440,000.00 USD | 48,610.00 USD | 56,530.00 USD | 70,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,650,000.00 USD | 2,650,000.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.20` | 1,620,000.00 USD | 1,620,000.00 USD | 60,080.00 USD | 50,690.00 USD | 61,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,700,000.00 USD | 2,700,000.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.60` | 1,830,000.00 USD | 1,830,000.00 USD | 33,410.00 USD | 111,150.00 USD | 64,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,820,000.00 USD | 2,820,000.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.00` | 1,990,000.00 USD | 1,990,000.00 USD | 65,300.00 USD | 47,440.00 USD | 47,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,880,000.00 USD | 2,880,000.00 USD | 24,680.00 USD | 27,640.00 USD | 24.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.40` | 2,000,000.00 USD | 2,000,000.00 USD | 15,440.00 USD | 1,350.00 USD | 19.25 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.80` | 2,070,000.00 USD | 2,070,000.00 USD | 13,980.00 USD | 26,130.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 3,080,000.00 USD | 3,080,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.20` | 2,130,000.00 USD | 2,130,000.00 USD | 11,300.00 USD | 35,370.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 3,150,000.00 USD | 3,150,000.00 USD | 1,240.00 USD | 73,530.00 USD | 25.48 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 6,050.00 USD | 7,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `292.60` | 2,180,000.00 USD | 2,180,000.00 USD | 30,280.00 USD | 15,010.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 3,250,000.00 USD | 3,250,000.00 USD | 887.27 USD | 101,280.00 USD | 30.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.00` | 2,280,000.00 USD | 2,280,000.00 USD | 66,050.00 USD | 22,370.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,420,000.00 USD | 3,420,000.00 USD | 33,580.00 USD | 132,770.00 USD | 35.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.40` | 2,340,000.00 USD | 2,340,000.00 USD | 13,770.00 USD | 22,640.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.80` | 2,530,000.00 USD | 2,530,000.00 USD | 91,300.00 USD | 39,940.00 USD | 55,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,480,000.00 USD | 3,480,000.00 USD | 38,790.00 USD | 1,860.00 USD | 20,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.20` | 2,610,000.00 USD | 2,610,000.00 USD | 6,700.00 USD | 29,230.00 USD | 49,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,890,000.00 USD | 3,890,000.00 USD | 217,140.00 USD | 42,290.00 USD | 146,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.60` | 2,890,000.00 USD | 2,890,000.00 USD | 115,260.00 USD | 77,220.00 USD | 85,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 4,150,000.00 USD | 4,150,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.00` | 3,020,000.00 USD | 3,020,000.00 USD | 14,930.00 USD | 27,170.00 USD | 86,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,630,000.00 USD | 4,630,000.00 USD | 46,330.00 USD | 83,600.00 USD | 345,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.40` | 3,170,000.00 USD | 3,170,000.00 USD | 43,660.00 USD | 47,580.00 USD | 60,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.80` | 3,410,000.00 USD | 3,410,000.00 USD | 75,280.00 USD | 28,880.00 USD | 129,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 5,070,000.00 USD | 5,070,000.00 USD | 165,320.00 USD | 82,100.00 USD | 197,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.20` | 3,620,000.00 USD | 3,620,000.00 USD | 70,140.00 USD | 115,990.00 USD | 33,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 5,400,000.00 USD | 5,400,000.00 USD | 43,710.00 USD | 167,940.00 USD | 120,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.60` | 3,710,000.00 USD | 3,710,000.00 USD | 33,180.00 USD | 10,850.00 USD | 41,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,740,000.00 USD | 5,740,000.00 USD | 133,820.00 USD | 3,570.00 USD | 201,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.00` | 3,830,000.00 USD | 3,830,000.00 USD | 3,560.00 USD | 22,340.00 USD | 94,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,880,000.00 USD | 5,880,000.00 USD | 78,980.00 USD | 54,960.00 USD | 70.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.40` | 3,930,000.00 USD | 3,930,000.00 USD | 61,380.00 USD | 9,840.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.80` | 3,960,000.00 USD | 3,960,000.00 USD | 16,150.00 USD | 5,350.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 6,110,000.00 USD | 6,110,000.00 USD | 47,530.00 USD | 99,810.00 USD | 89,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.20` | 4,110,000.00 USD | 4,110,000.00 USD | 55,630.00 USD | 6,460.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 6,260,000.00 USD | 6,260,000.00 USD | 32,650.00 USD | 45,150.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.60` | 4,190,000.00 USD | 4,190,000.00 USD | 19,040.00 USD | 1,470.00 USD | 61,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,340,000.00 USD | 6,340,000.00 USD | 69,820.00 USD | 12,530.00 USD | 4.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.00` | 4,260,000.00 USD | 4,260,000.00 USD | 13,610.00 USD | 5,690.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,460,000.00 USD | 6,460,000.00 USD | 3,550.00 USD | 27,070.00 USD | 86,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.40` | 4,340,000.00 USD | 4,340,000.00 USD | 35,750.00 USD | 15,570.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.80` | 4,380,000.00 USD | 4,380,000.00 USD | 3,510.00 USD | 7,630.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,510,000.00 USD | 6,510,000.00 USD | 22,060.00 USD | 9,100.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.20` | 4,490,000.00 USD | 4,490,000.00 USD | 32,890.00 USD | 37,600.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,550,000.00 USD | 6,550,000.00 USD | 35,320.00 USD | 3,530.00 USD | 179.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.60` | 4,520,000.00 USD | 4,520,000.00 USD | 10,390.00 USD | 1,090.00 USD | 17,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,690,000.00 USD | 6,690,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.00` | 4,560,000.00 USD | 4,560,000.00 USD | 521.60 USD | 6,480.00 USD | 29,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 6,980,000.00 USD | 6,980,000.00 USD | 73,320.00 USD | 58,690.00 USD | 150,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.40` | 4,610,000.00 USD | 4,610,000.00 USD | 582.35 USD | 9,670.00 USD | 36,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.80` | 4,670,000.00 USD | 4,670,000.00 USD | 19,640.00 USD | 31,360.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 7,220,000.00 USD | 7,220,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.20` | 4,700,000.00 USD | 4,700,000.00 USD | 25,460.00 USD | 9,160.00 USD | 63.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 7,410,000.00 USD | 7,410,000.00 USD | 1,560.00 USD | 181,550.00 USD | 18.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `302.50` | 3,640.00 USD | 10,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `302.60` | 4,770,000.00 USD | 4,770,000.00 USD | 14,490.00 USD | 11,920.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,630,000.00 USD | 7,630,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.00` | 4,800,000.00 USD | 4,800,000.00 USD | 20,850.00 USD | 2,130.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 1,950.00 USD | 64.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.40` | 4,820,000.00 USD | 4,820,000.00 USD | 750.17 USD | 2,860.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.80` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 403.53 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,690,000.00 USD | 7,690,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.20` | 4,880,000.00 USD | 4,880,000.00 USD | 21,920.00 USD | 3,420.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,720,000.00 USD | 7,720,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.60` | 4,940,000.00 USD | 4,940,000.00 USD | 9,850.00 USD | 1,990.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,770,000.00 USD | 7,770,000.00 USD | 35,470.00 USD | 11,790.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.00` | 4,960,000.00 USD | 4,960,000.00 USD | 9,740.00 USD | 7,030.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 8,200,000.00 USD | 8,200,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.40` | 4,960,000.00 USD | 4,960,000.00 USD | 3,100.00 USD | 514.02 USD | 9.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.80` | 4,980,000.00 USD | 4,980,000.00 USD | 7,430.00 USD | 5,740.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,340,000.00 USD | 8,340,000.00 USD | 80,680.00 USD | 52,160.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.20` | 5,000,000.00 USD | 5,000,000.00 USD | 7,040.00 USD | 321.71 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,500,000.00 USD | 8,500,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.60` | 5,020,000.00 USD | 5,020,000.00 USD | 1,920.00 USD | 12,340.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,740,000.00 USD | 8,740,000.00 USD | 94,690.00 USD | 74,510.00 USD | 70,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.00` | 5,090,000.00 USD | 5,090,000.00 USD | 25,440.00 USD | 23,620.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 9,050,000.00 USD | 9,050,000.00 USD | 27,410.00 USD | 136,370.00 USD | 147,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.40` | 5,150,000.00 USD | 5,150,000.00 USD | 4,250.00 USD | 37,760.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.80` | 5,220,000.00 USD | 5,220,000.00 USD | 36,220.00 USD | 32,580.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,350,000.00 USD | 9,350,000.00 USD | 127,080.00 USD | 113,210.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.20` | 5,240,000.00 USD | 5,240,000.00 USD | 9,920.00 USD | 69.30 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,700,000.00 USD | 9,700,000.00 USD | 169,010.00 USD | 67,070.00 USD | 114,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.60` | 5,260,000.00 USD | 5,260,000.00 USD | 8,120.00 USD | 224.24 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,870,000.00 USD | 9,870,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.00` | 5,270,000.00 USD | 5,270,000.00 USD | 2,430.00 USD | 6,400.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 9,980,000.00 USD | 9,980,000.00 USD | 34,260.00 USD | 36,030.00 USD | 36,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.40` | 5,280,000.00 USD | 5,280,000.00 USD | 7,480.00 USD | 3,910.00 USD | 796.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.80` | 5,300,000.00 USD | 5,300,000.00 USD | 15,490.00 USD | 5,480.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,330,000.00 USD | 10,330,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.20` | 5,320,000.00 USD | 5,320,000.00 USD | 5,140.00 USD | 5,010.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,580,000.00 USD | 10,580,000.00 USD | 62,230.00 USD | 108,410.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.60` | 5,330,000.00 USD | 5,330,000.00 USD | 112.30 USD | 3,980.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,700,000.00 USD | 10,700,000.00 USD | 60,910.00 USD | 51,380.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.00` | 5,340,000.00 USD | 5,340,000.00 USD | 5,080.00 USD | 174.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,950,000.00 USD | 10,950,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.40` | 5,340,000.00 USD | 5,340,000.00 USD | 901.19 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.80` | 5,360,000.00 USD | 5,360,000.00 USD | 7,340.00 USD | 9,070.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 11,000,000.00 USD | 11,000,000.00 USD | 19,570.00 USD | 11,240.00 USD | 25,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.20` | 5,390,000.00 USD | 5,390,000.00 USD | 299.35 USD | 12,920.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 11,080,000.00 USD | 11,080,000.00 USD | 43,780.00 USD | 11,410.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,420,000.00 USD | 5,420,000.00 USD | 14,340.00 USD | 5,090.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 11,140,000.00 USD | 11,140,000.00 USD | 21,990.00 USD | 14,880.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 11,220,000.00 USD | 11,220,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 11,290,000.00 USD | 11,290,000.00 USD | 32,780.00 USD | 1,570.00 USD | 44,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 11,380,000.00 USD | 11,380,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,420,000.00 USD | 11,420,000.00 USD | 24,660.00 USD | 0.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 547.95 USD | 50.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,490,000.00 USD | 11,490,000.00 USD | 9,200.00 USD | 33,700.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,590,000.00 USD | 11,590,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,650,000.00 USD | 11,650,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,670,000.00 USD | 11,670,000.00 USD | 15,590.00 USD | 748.91 USD | 171.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,700,000.00 USD | 11,700,000.00 USD | 21,640.00 USD | 8,380.00 USD | 164.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 11,760,000.00 USD | 11,760,000.00 USD | 627.00 USD | 31,660.00 USD | 32,070.00 USD | `Tier 1 CEX` |
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
| `7D` | `234.80` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 0.00 USD | 182.78 USD | 3,080.00 USD |
| `7D` | `235.30` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD |
| `7D` | `236.30` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `236.80` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 196.53 USD | 17,300.00 USD | 10,010.00 USD |
| `7D` | `237.30` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 5,120.00 USD | 146.67 USD | 11.79 USD |
| `7D` | `238.30` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 178.62 USD | 6,570.00 USD | 12,580.00 USD |
| `7D` | `238.80` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 140.10 USD | 9,360.00 USD | 19,440.00 USD |
| `7D` | `239.30` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.80` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 2,780.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `241.30` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 7,150.00 USD | 1,180.00 USD | 0.00 USD |
| `7D` | `241.80` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.30` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.30` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD |
| `7D` | `245.30` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 4,590.00 USD | 472.85 USD | 1,740.00 USD |
| `7D` | `247.30` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,690.00 USD |
| `7D` | `247.80` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 3,560.00 USD | 4,920.00 USD | 15.84 USD |
| `7D` | `248.30` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,400.00 USD |
| `7D` | `248.80` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,190.00 USD |
| `7D` | `249.30` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,560.00 USD |
| `7D` | `249.80` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,080.00 USD |
| `7D` | `250.30` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,560.00 USD |
| `1D` | `250.60` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 12,560.00 USD | 4,800.00 USD | 12,280.00 USD |
| `7D` | `250.80` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,620.00 USD |
| `1D` | `251.00` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 19,730.00 USD | 35,980.00 USD | 16,660.00 USD |
| `7D` | `251.30` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,110.00 USD |
| `1D` | `251.40` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 11,280.00 USD | 22,200.00 USD | 29,830.00 USD |
| `1D` | `251.80` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 36,220.00 USD | 48,630.00 USD | 6,420.00 USD |
| `7D` | `251.80` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,350.00 USD |
| `1D` | `252.20` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 11,510.00 USD | 816.08 USD | 10,980.00 USD |
| `7D` | `252.30` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 69,530.00 USD | 40,300.00 USD | 17,420.00 USD |
| `1D` | `252.60` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 13,380.00 USD | 1,610.00 USD | 6,000.00 USD |
| `7D` | `252.80` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,340.00 USD |
| `1D` | `253.00` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 4,490.00 USD | 7,620.00 USD | 2,170.00 USD |
| `7D` | `253.30` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,280.00 USD |
| `1D` | `253.40` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 20,170.00 USD | 19,940.00 USD | 14,790.00 USD |
| `1D` | `253.80` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 10,400.00 USD | 5,980.00 USD | 11,050.00 USD |
| `7D` | `253.80` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD |
| `1D` | `254.20` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 1,590.00 USD | 5,370.00 USD | 5,820.00 USD |
| `7D` | `254.30` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,120.00 USD |
| `1D` | `254.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 9,130.00 USD | 13,490.00 USD | 34.32 USD |
| `7D` | `254.80` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,350.00 USD |
| `1D` | `255.00` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 14,600.00 USD | 10,470.00 USD | 3,250.00 USD |
| `7D` | `255.30` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,510.00 USD |
| `1D` | `255.40` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,550.00 USD | 25,240.00 USD | 24,770.00 USD |
| `1D` | `255.80` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 21,840.00 USD | 11,170.00 USD | 16,160.00 USD |
| `7D` | `255.80` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD |
| `1D` | `256.20` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 2,620.00 USD | 39,280.00 USD | 17,240.00 USD |
| `7D` | `256.30` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,860.00 USD |
| `1D` | `256.60` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 8,400.00 USD | 8,320.00 USD | 8,220.00 USD |
| `7D` | `256.80` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 32,310.00 USD | 13,750.00 USD | 64,390.00 USD |
| `1D` | `257.00` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 9,580.00 USD | 1,470.00 USD | 13,740.00 USD |
| `7D` | `257.30` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,120.00 USD |
| `1D` | `257.40` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 6,290.00 USD | 4,650.00 USD | 8,330.00 USD |
| `1D` | `257.80` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 1,500.00 USD | 2,430.00 USD | 6,450.00 USD |
| `7D` | `257.80` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,220.00 USD |
| `1D` | `258.20` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 21,220.00 USD | 15,910.00 USD | 56,550.00 USD |
| `7D` | `258.30` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 106,080.00 USD | 37,040.00 USD | 71,510.00 USD |
| `1D` | `258.60` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 25,120.00 USD | 8,900.00 USD | 40,000.00 USD |
| `7D` | `258.80` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,330.00 USD |
| `1D` | `259.00` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 12,700.00 USD | 34,640.00 USD | 7.60 USD |
| `7D` | `259.30` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,050.00 USD |
| `1D` | `259.40` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 14,770.00 USD | 3,590.00 USD | 17,640.00 USD |
| `1D` | `259.80` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 41,960.00 USD | 32,130.00 USD | 39,290.00 USD |
| `7D` | `259.80` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,230.00 USD |
| `1D` | `260.20` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 4,650.00 USD | 8,250.00 USD | 6,870.00 USD |
| `7D` | `260.30` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,860.00 USD |
| `1D` | `260.60` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 20,190.00 USD | 7,070.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,150.00 USD |
| `1D` | `261.00` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 8,270.00 USD | 49,100.00 USD | 44,780.00 USD |
| `7D` | `261.30` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,700.00 USD |
| `1D` | `261.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 7,870.00 USD | 43,640.00 USD | 2,570.00 USD |
| `1D` | `261.80` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 15,440.00 USD | 47,400.00 USD | 62,120.00 USD |
| `7D` | `261.80` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 68,120.00 USD | 83,380.00 USD | 45,150.00 USD |
| `1D` | `262.20` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 34,470.00 USD | 28,550.00 USD | 21,320.00 USD |
| `7D` | `262.30` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 43,780.00 USD | 83,970.00 USD | 48,040.00 USD |
| `1D` | `262.60` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 738.08 USD | 1,680.00 USD | 13,400.00 USD |
| `7D` | `262.80` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,770.00 USD |
| `1D` | `263.00` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 8,930.00 USD | 12,640.00 USD | 6,210.00 USD |
| `7D` | `263.30` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 33,590.00 USD | 13,710.00 USD | 118.53 USD |
| `1D` | `263.40` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 30,700.00 USD | 4,190.00 USD | 74,280.00 USD |
| `1D` | `263.80` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 32,740.00 USD | 30,130.00 USD | 28,530.00 USD |
| `7D` | `263.80` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,900.00 USD |
| `1D` | `264.20` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 25,990.00 USD | 15,550.00 USD | 17,230.00 USD |
| `7D` | `264.30` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 48,230.00 USD | 1,170.00 USD | 88.50 USD |
| `1D` | `264.60` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,520.00 USD | 19,920.00 USD | 19,940.00 USD |
| `7D` | `264.80` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 33,470.00 USD | 21,870.00 USD | 147.83 USD |
| `1D` | `265.00` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 33,010.00 USD | 2,110.00 USD | 33,370.00 USD |
| `7D` | `265.30` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 256,440.00 USD | 2,330.00 USD | 33,850.00 USD |
| `1D` | `265.40` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 64,890.00 USD | 2,970.00 USD | 16.32 USD |
| `1D` | `265.80` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 12,120.00 USD | 313.30 USD | 5.24 USD |
| `7D` | `265.80` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 69,380.00 USD | 0.00 USD | 75.80 USD |
| `1D` | `266.20` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 4,210.00 USD | 13,450.00 USD | 4,800.00 USD |
| `7D` | `266.30` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 216,090.00 USD | 1,450.00 USD | 238.29 USD |
| `1D` | `266.60` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 14,560.00 USD | 8,680.00 USD | 0.00 USD |
| `7D` | `266.80` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 136,640.00 USD | 63,260.00 USD | 136.12 USD |
| `1D` | `267.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 44,140.00 USD | 25,440.00 USD | 0.00 USD |
| `7D` | `267.30` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 131,280.00 USD | 53,030.00 USD | 118.58 USD |
| `1D` | `267.40` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 7,810.00 USD | 68,360.00 USD | 22,320.00 USD |
| `1D` | `267.80` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 10,330.00 USD | 40,070.00 USD | 19,100.00 USD |
| `7D` | `267.80` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,710.00 USD |
| `1D` | `268.20` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 24,330.00 USD | 35,070.00 USD | 59,950.00 USD |
| `7D` | `268.30` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,890.00 USD |
| `1D` | `268.60` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 25,840.00 USD | 19,230.00 USD | 85.16 USD |
| `7D` | `268.80` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 23,340.00 USD | 17,480.00 USD | 116.16 USD |
| `1D` | `269.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 8,580.00 USD | 669.20 USD | 124.66 USD |
| `7D` | `269.30` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 0.00 USD | 3,490.00 USD | 129.06 USD |
| `1D` | `269.40` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 13,400.00 USD | 16,910.00 USD | 16,470.00 USD |
| `1D` | `269.80` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 711.50 USD | 1,470.00 USD | 3,510.00 USD |
| `7D` | `269.80` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `270.20` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 24,670.00 USD | 13,340.00 USD | 3,540.00 USD |
| `1D` | `270.60` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 40,360.00 USD | 118.00 USD | 0.00 USD |
| `7D` | `270.80` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.00` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 505.00 USD | 14,830.00 USD | 7,360.00 USD |
| `7D` | `271.30` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.40` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 12,710.00 USD | 1,780.00 USD | 9,670.00 USD |
| `1D` | `271.80` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 13,310.00 USD | 34,920.00 USD | 9,610.00 USD |
| `7D` | `271.80` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD |
| `1D` | `272.20` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 17,320.00 USD | 31,900.00 USD | 10,160.00 USD |
| `7D` | `272.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.60` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 27,370.00 USD | 27,760.00 USD | 68,320.00 USD |
| `7D` | `272.80` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `273.00` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 42,140.00 USD | 27,210.00 USD | 47,800.00 USD |
| `7D` | `273.30` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD |
| `1D` | `273.40` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 24,670.00 USD | 107,180.00 USD | 37,810.00 USD |
| `1D` | `273.80` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 79,850.00 USD | 80,800.00 USD | 69,750.00 USD |
| `7D` | `273.80` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.20` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 244,400.00 USD | 37,750.00 USD | 25,020.00 USD |
| `7D` | `274.30` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD |
| `1D` | `274.60` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 117,810.00 USD | 19,960.00 USD | 41,170.00 USD |
| `7D` | `274.80` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `275.00` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 38,980.00 USD | 0.00 USD | 12,550.00 USD |
| `7D` | `275.30` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 59,580.00 USD | 19,960.00 USD | 10.44 USD |
| `1D` | `275.40` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD |
| `1D` | `275.80` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 53,120.00 USD | 34,910.00 USD | 40,360.00 USD |
| `7D` | `275.80` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,530.00 USD |
| `1D` | `276.20` | 917,230.00 USD | 0.00 USD | 917,230.00 USD | 166,790.00 USD | 0.00 USD | 3,220.00 USD |
| `7D` | `276.30` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.60` | 747,220.00 USD | 0.00 USD | 747,220.00 USD | 11,880.00 USD | 22,740.00 USD | 5,600.00 USD |
| `7D` | `276.80` | 910,640.00 USD | 0.00 USD | 910,640.00 USD | 16,100.00 USD | 0.00 USD | 10.77 USD |
| `1D` | `277.00` | 707,010.00 USD | 0.00 USD | 707,010.00 USD | 25,410.00 USD | 7,900.00 USD | 34,070.00 USD |
| `7D` | `277.30` | 894,530.00 USD | 0.00 USD | 894,530.00 USD | 152,190.00 USD | 77,800.00 USD | 140,990.00 USD |
| `1D` | `277.40` | 639,630.00 USD | 0.00 USD | 639,630.00 USD | 26,920.00 USD | 18,260.00 USD | 0.00 USD |
| `1D` | `277.80` | 594,450.00 USD | 0.00 USD | 594,450.00 USD | 4,440.00 USD | 31,980.00 USD | 20,300.00 USD |
| `7D` | `277.80` | 523,560.00 USD | 0.00 USD | 523,560.00 USD | 0.00 USD | 157,740.00 USD | 59,940.00 USD |
| `1D` | `278.20` | 537,720.00 USD | 0.00 USD | 537,720.00 USD | 12,120.00 USD | 88,410.00 USD | 83,650.00 USD |
| `7D` | `278.30` | 305,880.00 USD | 0.00 USD | 305,880.00 USD | 24,750.00 USD | 37,090.00 USD | 155,460.00 USD |
| `1D` | `278.60` | 353,540.00 USD | 0.00 USD | 353,540.00 USD | 88,160.00 USD | 55,720.00 USD | 47,870.00 USD |
| `7D` | `278.80` | 88,580.00 USD | 0.00 USD | 88,580.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `279.00` | 161,790.00 USD | 0.00 USD | 161,790.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.30` | 18,200.00 USD | 0.00 USD | 18,200.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.40` | 151,960.00 USD | 0.00 USD | 151,960.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD |
| `1D` | `279.80` | 110,880.00 USD | 0.00 USD | 110,880.00 USD | 0.00 USD | 0.00 USD | 55,650.00 USD |
| `1D` | `280.60` | 55,230.00 USD | 0.00 USD | 55,230.00 USD | 0.00 USD | 48,210.00 USD | 0.00 USD |
| `7D` | `280.80` | 15,540.00 USD | 0.00 USD | 15,540.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `281.00` | 7,020.00 USD | 0.00 USD | 7,020.00 USD | 0.00 USD | 7,010.00 USD | 12.68 USD |
| `7D` | `281.30` | 93,830.00 USD | 93,830.00 USD | 0.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD |
| `7D` | `281.30` | 187,650.00 USD | 187,650.00 USD | 0.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD |
| `1D` | `281.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `281.80` | 4,140.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD |
| `7D` | `281.80` | 310,040.00 USD | 310,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.20` | 12,400.00 USD | 12,400.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.30` | 334,260.00 USD | 334,260.00 USD | 0.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `7D` | `283.30` | 337,850.00 USD | 337,850.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 141.02 USD |
| `1D` | `283.40` | 13,700.00 USD | 13,700.00 USD | 0.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD |
| `7D` | `283.80` | 339,850.00 USD | 339,850.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.30` | 341,420.00 USD | 341,420.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD |
| `1D` | `284.60` | 59,520.00 USD | 59,520.00 USD | 0.00 USD | 10,630.00 USD | 7,620.00 USD | 27,570.00 USD |
| `7D` | `284.80` | 396,880.00 USD | 396,880.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 65.52 USD |
| `1D` | `285.00` | 99,060.00 USD | 99,060.00 USD | 0.00 USD | 39,520.00 USD | 0.00 USD | 9.04 USD |
| `7D` | `285.30` | 818,840.00 USD | 818,840.00 USD | 0.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD |
| `1D` | `285.40` | 230,170.00 USD | 230,170.00 USD | 0.00 USD | 51,680.00 USD | 37,750.00 USD | 41,680.00 USD |
| `1D` | `285.80` | 250,420.00 USD | 250,420.00 USD | 0.00 USD | 1,710.00 USD | 434.90 USD | 18,110.00 USD |
| `7D` | `285.80` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD |
| `1D` | `286.20` | 308,140.00 USD | 308,140.00 USD | 0.00 USD | 39,790.00 USD | 284.90 USD | 17,650.00 USD |
| `7D` | `286.30` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 11.42 USD |
| `1D` | `286.60` | 342,500.00 USD | 342,500.00 USD | 0.00 USD | 2,290.00 USD | 1,930.00 USD | 30,140.00 USD |
| `7D` | `286.80` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 2.56 USD |
| `1D` | `287.00` | 557,070.00 USD | 557,070.00 USD | 0.00 USD | 65,140.00 USD | 61,640.00 USD | 87,790.00 USD |
| `7D` | `287.30` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 103.44 USD |
| `1D` | `287.40` | 699,430.00 USD | 699,430.00 USD | 0.00 USD | 101,280.00 USD | 12,420.00 USD | 28,650.00 USD |
| `1D` | `287.80` | 797,880.00 USD | 797,880.00 USD | 0.00 USD | 13,160.00 USD | 27,060.00 USD | 58,230.00 USD |
| `7D` | `287.80` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 70,340.00 USD | 272,200.00 USD | 53,290.00 USD |
| `1D` | `288.20` | 914,150.00 USD | 914,150.00 USD | 0.00 USD | 69,440.00 USD | 23,420.00 USD | 23,410.00 USD |
| `7D` | `288.30` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD |
| `1D` | `288.60` | 982,770.00 USD | 982,770.00 USD | 0.00 USD | 6,190.00 USD | 33,200.00 USD | 29,230.00 USD |
| `7D` | `288.80` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD |
| `1D` | `289.00` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 42,790.00 USD | 31,570.00 USD | 9,870.00 USD |
| `7D` | `289.30` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.40` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 25,800.00 USD | 59,890.00 USD | 116,530.00 USD |
| `1D` | `289.80` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 48,610.00 USD | 56,530.00 USD | 70,120.00 USD |
| `7D` | `289.80` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD |
| `1D` | `290.20` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 60,080.00 USD | 50,690.00 USD | 61,310.00 USD |
| `7D` | `290.30` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.60` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 33,410.00 USD | 111,150.00 USD | 64,600.00 USD |
| `7D` | `290.80` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD |
| `1D` | `291.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 65,300.00 USD | 47,440.00 USD | 47,450.00 USD |
| `7D` | `291.30` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 24,680.00 USD | 27,640.00 USD | 24.20 USD |
| `1D` | `291.40` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 15,440.00 USD | 1,350.00 USD | 19.25 USD |
| `1D` | `291.80` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 13,980.00 USD | 26,130.00 USD | 28,430.00 USD |
| `7D` | `291.80` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,500.00 USD |
| `1D` | `292.20` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 11,300.00 USD | 35,370.00 USD | 11,500.00 USD |
| `7D` | `292.30` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 25.48 USD |
| `1D` | `292.60` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 30,280.00 USD | 15,010.00 USD | 2,240.00 USD |
| `7D` | `292.80` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 30.72 USD |
| `1D` | `293.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 66,050.00 USD | 22,370.00 USD | 16,840.00 USD |
| `7D` | `293.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 33,580.00 USD | 132,770.00 USD | 35.37 USD |
| `1D` | `293.40` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 13,770.00 USD | 22,640.00 USD | 23,920.00 USD |
| `1D` | `293.80` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 91,300.00 USD | 39,940.00 USD | 55,120.00 USD |
| `7D` | `293.80` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 20,880.00 USD |
| `1D` | `294.20` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 6,700.00 USD | 29,230.00 USD | 49,220.00 USD |
| `7D` | `294.30` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 217,140.00 USD | 42,290.00 USD | 146,130.00 USD |
| `1D` | `294.60` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 115,260.00 USD | 77,220.00 USD | 85,210.00 USD |
| `7D` | `294.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,240.00 USD |
| `1D` | `295.00` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 14,930.00 USD | 27,170.00 USD | 86,290.00 USD |
| `7D` | `295.30` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 46,330.00 USD | 83,600.00 USD | 345,600.00 USD |
| `1D` | `295.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 43,660.00 USD | 47,580.00 USD | 60,520.00 USD |
| `1D` | `295.80` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 75,280.00 USD | 28,880.00 USD | 129,740.00 USD |
| `7D` | `295.80` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 165,320.00 USD | 82,100.00 USD | 197,390.00 USD |
| `1D` | `296.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 70,140.00 USD | 115,990.00 USD | 33,030.00 USD |
| `7D` | `296.30` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 43,710.00 USD | 167,940.00 USD | 120,940.00 USD |
| `1D` | `296.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 33,180.00 USD | 10,850.00 USD | 41,250.00 USD |
| `7D` | `296.80` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 133,820.00 USD | 3,570.00 USD | 201,510.00 USD |
| `1D` | `297.00` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 3,560.00 USD | 22,340.00 USD | 94,450.00 USD |
| `7D` | `297.30` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 78,980.00 USD | 54,960.00 USD | 70.59 USD |
| `1D` | `297.40` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 61,380.00 USD | 9,840.00 USD | 27,540.00 USD |
| `1D` | `297.80` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 16,150.00 USD | 5,350.00 USD | 12,070.00 USD |
| `7D` | `297.80` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 47,530.00 USD | 99,810.00 USD | 89,550.00 USD |
| `1D` | `298.20` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 55,630.00 USD | 6,460.00 USD | 85,030.00 USD |
| `7D` | `298.30` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 32,650.00 USD | 45,150.00 USD | 68,810.00 USD |
| `1D` | `298.60` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 19,040.00 USD | 1,470.00 USD | 61,070.00 USD |
| `7D` | `298.80` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 4.18 USD |
| `1D` | `299.00` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 13,610.00 USD | 5,690.00 USD | 46,700.00 USD |
| `7D` | `299.30` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 3,550.00 USD | 27,070.00 USD | 86,040.00 USD |
| `1D` | `299.40` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 35,750.00 USD | 15,570.00 USD | 31,470.00 USD |
| `1D` | `299.80` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 3,510.00 USD | 7,630.00 USD | 30,240.00 USD |
| `7D` | `299.80` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 22,060.00 USD | 9,100.00 USD | 19,870.00 USD |
| `1D` | `300.20` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 32,890.00 USD | 37,600.00 USD | 42,600.00 USD |
| `7D` | `300.30` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 35,320.00 USD | 3,530.00 USD | 179.44 USD |
| `1D` | `300.60` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 10,390.00 USD | 1,090.00 USD | 17,190.00 USD |
| `7D` | `300.80` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,320.00 USD |
| `1D` | `301.00` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 521.60 USD | 6,480.00 USD | 29,470.00 USD |
| `7D` | `301.30` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 73,320.00 USD | 58,690.00 USD | 150,540.00 USD |
| `1D` | `301.40` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 582.35 USD | 9,670.00 USD | 36,360.00 USD |
| `1D` | `301.80` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 19,640.00 USD | 31,360.00 USD | 10,440.00 USD |
| `7D` | `301.80` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,360.00 USD |
| `1D` | `302.20` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 25,460.00 USD | 9,160.00 USD | 63.87 USD |
| `7D` | `302.30` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 1,560.00 USD | 181,550.00 USD | 18.68 USD |
| `1D` | `302.60` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 14,490.00 USD | 11,920.00 USD | 38,380.00 USD |
| `7D` | `302.80` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,940.00 USD |
| `1D` | `303.00` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 20,850.00 USD | 2,130.00 USD | 14,080.00 USD |
| `7D` | `303.30` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD | 64.10 USD |
| `1D` | `303.40` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 750.17 USD | 2,860.00 USD | 9,360.00 USD |
| `1D` | `303.80` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 403.53 USD | 1.44 USD |
| `7D` | `303.80` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,580.00 USD |
| `1D` | `304.20` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 21,920.00 USD | 3,420.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,470.00 USD |
| `1D` | `304.60` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 9,850.00 USD | 1,990.00 USD | 44,520.00 USD |
| `7D` | `304.80` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 35,470.00 USD | 11,790.00 USD | 4,140.00 USD |
| `1D` | `305.00` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 9,740.00 USD | 7,030.00 USD | 2,030.00 USD |
| `7D` | `305.30` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,460.00 USD |
| `1D` | `305.40` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 3,100.00 USD | 514.02 USD | 9.35 USD |
| `1D` | `305.80` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 7,430.00 USD | 5,740.00 USD | 5,870.00 USD |
| `7D` | `305.80` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 80,680.00 USD | 52,160.00 USD | 12,680.00 USD |
| `1D` | `306.20` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 7,040.00 USD | 321.71 USD | 6,370.00 USD |
| `7D` | `306.30` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,700.00 USD |
| `1D` | `306.60` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 1,920.00 USD | 12,340.00 USD | 10,300.00 USD |
| `7D` | `306.80` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 94,690.00 USD | 74,510.00 USD | 70,000.00 USD |
| `1D` | `307.00` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 25,440.00 USD | 23,620.00 USD | 16,980.00 USD |
| `7D` | `307.30` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 27,410.00 USD | 136,370.00 USD | 147,550.00 USD |
| `1D` | `307.40` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 4,250.00 USD | 37,760.00 USD | 19,580.00 USD |
| `1D` | `307.80` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 36,220.00 USD | 32,580.00 USD | 6,040.00 USD |
| `7D` | `307.80` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 127,080.00 USD | 113,210.00 USD | 60,830.00 USD |
| `1D` | `308.20` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 9,920.00 USD | 69.30 USD | 10,930.00 USD |
| `7D` | `308.30` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 169,010.00 USD | 67,070.00 USD | 114,200.00 USD |
| `1D` | `308.60` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 8,120.00 USD | 224.24 USD | 5,990.00 USD |
| `7D` | `308.80` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,030.00 USD |
| `1D` | `309.00` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 2,430.00 USD | 6,400.00 USD | 1,350.00 USD |
| `7D` | `309.30` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 34,260.00 USD | 36,030.00 USD | 36,680.00 USD |
| `1D` | `309.40` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 7,480.00 USD | 3,910.00 USD | 796.24 USD |
| `1D` | `309.80` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 15,490.00 USD | 5,480.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,780.00 USD |
| `1D` | `310.20` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 5,140.00 USD | 5,010.00 USD | 11,030.00 USD |
| `7D` | `310.30` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 62,230.00 USD | 108,410.00 USD | 80,840.00 USD |
| `1D` | `310.60` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 112.30 USD | 3,980.00 USD | 5,810.00 USD |
| `7D` | `310.80` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 12,150.00 USD |
| `1D` | `311.00` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 5,080.00 USD | 174.00 USD | 0.00 USD |
| `7D` | `311.30` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,800.00 USD |
| `1D` | `311.40` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 901.19 USD | 2,250.00 USD | 0.00 USD |
| `1D` | `311.80` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 7,340.00 USD | 9,070.00 USD | 4,060.00 USD |
| `7D` | `311.80` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 19,570.00 USD | 11,240.00 USD | 25,480.00 USD |
| `1D` | `312.20` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 299.35 USD | 12,920.00 USD | 15,040.00 USD |
| `7D` | `312.30` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 27,510.00 USD |
| `1D` | `312.50` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 14,340.00 USD | 5,090.00 USD | 11,780.00 USD |
| `7D` | `312.80` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 21,990.00 USD | 14,880.00 USD | 19,190.00 USD |
| `7D` | `313.30` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,460.00 USD |
| `7D` | `313.80` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 32,780.00 USD | 1,570.00 USD | 44,150.00 USD |
| `7D` | `314.30` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `7D` | `314.80` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,310.00 USD |
| `7D` | `315.30` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 547.95 USD | 50.67 USD |
| `7D` | `315.80` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 9,200.00 USD | 33,700.00 USD | 29,940.00 USD |
| `7D` | `316.30` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,450.00 USD |
| `7D` | `316.80` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,370.00 USD |
| `7D` | `317.30` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 171.23 USD |
| `7D` | `317.80` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 164.65 USD |
| `7D` | `318.30` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 627.00 USD | 31,660.00 USD | 32,070.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `302.98M` | Total OI Tokens: `1,078,487.0 BCH`
  * 1h OI Change: `-0.06%` | 4h OI Change: `-1.94%` | 24h OI Change: `-0.66%`
  * Exchange Breakdown: Binance=`88.09M` | Bybit=`37.60M` | OKX=`23.75M` | Hyperliquid=`7.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.17K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0090%` |
| **USDT Bybit** | `-0.0034%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0095%` | **USDT Bitget** | `0.0077%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `52.29%` | `47.71%` | `1.10` | 1,780,000.00 USD |
| `15M` | `Binance` | `37.62%` | `62.38%` | `0.60` | 315,370.00 USD |
| `15M` | `OKX` | `40.65%` | `59.35%` | `0.68` | 152,790.00 USD |
| `15M` | `Bybit` | `46.03%` | `53.97%` | `0.85` | 72,520.00 USD |
| `15M` | `KuCoin` | `49.25%` | `50.75%` | `0.97` | 99,970.00 USD |
| `15M` | `Gate` | `73.77%` | `26.23%` | `2.81` | 41,850.00 USD |
| `15M` | `Bitget` | `53.23%` | `46.77%` | `1.14` | 29,610.00 USD |
| `15M` | `BingX` | `50.68%` | `49.32%` | `1.03` | 120,100.00 USD |
| `15M` | `MEXC` | `49.49%` | `50.51%` | `0.98` | 34,980.00 USD |
| `15M` | `Bitunix` | `59.37%` | `40.63%` | `1.46` | 38,490.00 USD |
| `15M` | `Hyperliquid` | `29.67%` | `70.33%` | `0.42` | 3,780.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.4%` | `49.6%` | `1.02` | 503,630.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `71.64%` | `28.36%` | `2.53` | 353,340.00 USD |
| `15M` | `HTX` | `34.93%` | `65.07%` | `0.54` | 518.60 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.68%` | `33.32%` | `2.00` | 4,610.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 5.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `94.21%` | `5.79%` | `16.27` | 9,550.00 USD |
| `15M` | `Whale Positions` | `37.62%` | `62.38%` | `0.60` | 315,370.00 USD |
| `15M` | `Global Accounts` | `52.29%` | `47.71%` | `1.10` | 1,780,000.00 USD |
| `1H` | `BCH` | `50.52%` | `49.48%` | `1.02` | 8,080,000.00 USD |
| `1H` | `Binance` | `35.35%` | `64.65%` | `0.55` | 1,500,000.00 USD |
| `1H` | `OKX` | `45.03%` | `54.97%` | `0.82` | 574,340.00 USD |
| `1H` | `Bybit` | `38.7%` | `61.3%` | `0.63` | 414,750.00 USD |
| `1H` | `KuCoin` | `49.71%` | `50.29%` | `0.99` | 335,710.00 USD |
| `1H` | `Gate` | `60.68%` | `39.32%` | `1.54` | 111,870.00 USD |
| `1H` | `Bitget` | `67.05%` | `32.95%` | `2.03` | 155,230.00 USD |
| `1H` | `BingX` | `51.05%` | `48.95%` | `1.04` | 395,640.00 USD |
| `1H` | `MEXC` | `41.2%` | `58.8%` | `0.70` | 228,980.00 USD |
| `1H` | `Bitunix` | `48.56%` | `51.44%` | `0.94` | 121,370.00 USD |
| `1H` | `Hyperliquid` | `22.27%` | `77.73%` | `0.29` | 104,140.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.98%` | `50.02%` | `1.00` | 3,200,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `88.23%` | `11.77%` | `7.50` | 880,820.00 USD |
| `1H` | `HTX` | `29.93%` | `70.07%` | `0.43` | 4,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `62.52%` | `37.48%` | `1.67` | 30,210.00 USD |
| `1H` | `Aster` | `45.34%` | `54.66%` | `0.83` | 991.42 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `89.29%` | `10.71%` | `8.34` | 19,230.00 USD |
| `1H` | `Whale Positions` | `35.35%` | `64.65%` | `0.55` | 1,500,000.00 USD |
| `1H` | `Global Accounts` | `50.52%` | `49.48%` | `1.02` | 8,080,000.00 USD |
| `4H` | `BCH` | `50.51%` | `49.49%` | `1.02` | 454,800,000.00 USD |
| `4H` | `Binance` | `52.89%` | `47.11%` | `1.12` | 196,710,000.00 USD |
| `4H` | `OKX` | `48.56%` | `51.44%` | `0.94` | 49,460,000.00 USD |
| `4H` | `Bybit` | `47.77%` | `52.23%` | `0.91` | 59,460,000.00 USD |
| `4H` | `KuCoin` | `57.56%` | `42.44%` | `1.36` | 5,340,000.00 USD |
| `4H` | `Gate` | `53.69%` | `46.31%` | `1.16` | 11,250,000.00 USD |
| `4H` | `Bitget` | `53.06%` | `46.94%` | `1.13` | 24,600,000.00 USD |
| `4H` | `BingX` | `44.29%` | `55.71%` | `0.80` | 19,500,000.00 USD |
| `4H` | `MEXC` | `47.33%` | `52.67%` | `0.90` | 17,050,000.00 USD |
| `4H` | `Bitunix` | `49.58%` | `50.42%` | `0.98` | 8,290,000.00 USD |
| `4H` | `Hyperliquid` | `50.7%` | `49.3%` | `1.03` | 40,040,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.51%` | `50.49%` | `0.98` | 1,880,000.00 USD |
| `4H` | `Crypto.com` | `59.25%` | `40.75%` | `1.45` | 74,990.00 USD |
| `4H` | `WhiteBIT` | `39.08%` | `60.92%` | `0.64` | 15,380,000.00 USD |
| `4H` | `HTX` | `58.13%` | `41.87%` | `1.39` | 542,570.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.09%` | `53.91%` | `0.85` | 1,560,000.00 USD |
| `4H` | `Aster` | `51.66%` | `48.34%` | `1.07` | 1,300,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.48%` | `46.52%` | `1.15` | 2,370,000.00 USD |
| `4H` | `Whale Positions` | `52.89%` | `47.11%` | `1.12` | 196,710,000.00 USD |
| `4H` | `Global Accounts` | `50.51%` | `49.49%` | `1.02` | 454,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `282.15` | `283.00` | `282.15` | `284.87` | `281.41` | 1,285,912.66 USD | 419,903.43 USD | 866,009.23 USD | -446,105.80 USD | `-34.69%` | `7B / 53S` |
| `5:00 UTC` | `281.32` | `281.51` | `281.32` | `282.72` | `280.80` | 1,039,042.65 USD | 453,949.26 USD | 585,093.39 USD | -131,144.13 USD | `-12.62%` | `25B / 59S` |
| `0:00 UTC` | `281.50` | `282.15` | `281.50` | `283.26` | `281.24` | 1,246,277.92 USD | 838,584.24 USD | 407,693.68 USD | 430,890.56 USD | `+34.57%` | `32B / 6S` |
| `5:00 UTC` | `283.12` | `282.91` | `283.12` | `283.64` | `281.86` | 898,717.53 USD | 422,080.39 USD | 476,637.13 USD | -54,556.74 USD | `-6.07%` | `22B / 36S` |
| `0:00 UTC` | `280.81` | `281.09` | `280.81` | `281.94` | `280.02` | 959,751.07 USD | 348,775.30 USD | 610,975.78 USD | -262,200.48 USD | `-27.32%` | `10B / 71S` |
| `5:00 UTC` | `278.88` | `279.51` | `278.88` | `280.56` | `278.74` | 1,525,848.29 USD | 843,855.80 USD | 681,992.49 USD | 161,863.30 USD | `+10.61%` | `26B / 51S` |
| `0:00 UTC` | `281.21` | `280.32` | `281.21` | `281.29` | `278.55` | 1,960,555.94 USD | 896,979.92 USD | 1,063,576.02 USD | -166,596.10 USD | `-8.50%` | `26B / 22S` |
| `5:00 UTC` | `279.18` | `279.58` | `279.18` | `280.70` | `279.06` | 617,038.04 USD | 332,886.00 USD | 284,152.04 USD | 48,733.95 USD | `+7.90%` | `32B / 38S` |
| `0:00 UTC` | `279.30` | `281.19` | `279.30` | `282.30` | `278.88` | 2,044,095.31 USD | 958,971.19 USD | 1,085,124.12 USD | -126,152.93 USD | `-6.17%` | `39B / 29S` |
| `5:00 UTC` | `281.37` | `281.19` | `281.37` | `281.62` | `280.50` | 339,711.45 USD | 192,518.07 USD | 147,193.38 USD | 45,324.69 USD | `+13.34%` | `26B / 19S` |

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
| `5m` | -12,510.00 USD | -19,890.00 USD | **`DISTRIBUTION`** |
| `15m` | -58,160.00 USD | 41,090.00 USD | **`DISTRIBUTION`** |
| `30m` | 33,210.00 USD | -173,640.00 USD | **`DISTRIBUTION`** |
| `1h` | 35,130.00 USD | -335,980.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,700.00 USD | 170,780.00 USD | **`ACCUMULATION`** |
| `4h` | 58,040.00 USD | -777,050.00 USD | **`DISTRIBUTION`** |
| `6h` | 507,420.00 USD | -206,260.00 USD | **`ACCUMULATION`** |
| `8h` | 1,540,000.00 USD | 1,940,000.00 USD | **`ACCUMULATION`** |
| `12h` | 945,660.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 133,000.00 USD | -2,260,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -404,680.00 USD | -14,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,930,000.00 USD | -137,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.51K` | 15m=`-58.16K` | 1h=`+35.13K` | 24h=`+133.00K`
* Futures Capital Netflows: 5m=`-19.89K` | 15m=`+41.09K` | 1h=`-335.98K` | 24h=`-2.26M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `272.91` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `269.43` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `281.61`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `284.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `287.92` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `275.74`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`283.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
