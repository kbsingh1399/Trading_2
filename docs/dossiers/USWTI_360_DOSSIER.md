# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 16:45:52 IST` (`2026-10-30 11:15:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.77` | **Live Ask Quote**: `104.82` | **Mid Price**: `104.79`
- **Spread Points**: `56.00` | **Spread BPS**: `5.34 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1,000.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `10.00 USD` | Point Value (0.01 Lot): `0.1000 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `104.79` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.53` | Lower -3.00σ Band: `104.06`
  * Upper +2.51σ Band: `105.37` | Lower -2.51σ Band: `104.22`
  * Upper +2.01σ Band: `105.23` | Lower -2.01σ Band: `104.35`
  * Upper +2.00σ Band: `105.21` | Lower -2.00σ Band: `104.37`
  * Upper +1.28σ Band: `105.09` | Lower -1.28σ Band: `104.50`
  * Upper +1.00σ Band: `105.00` | Lower -1.00σ Band: `104.58`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.79` | EMA-20=`104.79` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`104.79` (Slope: `+0.0000`) | EMA-100=`104.79`
  * Institutional Anchors: EMA-144=`104.79` | EMA-200=`104.79` (Slope: `+0.0000`) | EMA-233=`104.79`
- **Range Boundaries**: 24H High=`105.84` | 24H Low=`103.75` | Weekly High=`106.89` | Weekly Low=`102.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.97` (Distance: `-0.17%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.71%`)
  * Value Area Low (VAL) = `103.63` (Distance: `+1.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.44` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.95` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.95` | Low=`104.33`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.37` - `105.21`
  * Optimal Trade Entry (OTE 0.705): `105.00`
  * Structural Invalidation Anchor (0.786): `105.63`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.45` | `104.59` | `104.30` | `104.50` | `555` | 57,996.39 USD | 14,744.84 USD | `+25.42%` | 571,263.44 USD | `+0.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.49` | `104.61` | `104.45` | `104.54` | `440` | 45,998.92 USD | 10,781.00 USD | `+23.44%` | 582,044.44 USD | `-0.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.55` | `104.58` | `104.37` | `104.43` | `408` | 42,606.62 USD | -22,342.50 USD | `-52.44%` | 559,701.94 USD | `-1.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.12` | `104.42` | `103.92` | `104.35` | `1,106` | 115,408.89 USD | 68,091.24 USD | `+59.00%` | 823,310.43 USD | `+1.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.34` | `104.72` | `104.19` | `104.45` | `1,247` | 130,246.66 USD | 11,058.68 USD | `+8.49%` | 834,369.11 USD | `+0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `104.45` | `104.61` | `104.30` | `104.43` | `1,403` | 146,512.48 USD | -18,604.76 USD | `-12.70%` | 815,764.35 USD | `-0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `103.90` | `104.09` | `103.08` | `103.45` | `4,485` | 463,964.28 USD | -168,609.15 USD | `-36.34%` | 630,221.87 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `104.72` | `103.46` | `104.45` | `4,423` | 461,973.50 USD | 311,329.97 USD | `+67.39%` | 941,551.84 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.45` | `104.61` | `104.03` | `104.25` | `5,972` | 622,598.92 USD | -182,485.89 USD | `-29.31%` | 759,065.96 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,724,296.99 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 3,306,037.16 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,321,092.69 USD | `300,817.26` | `98.89` | `104.14` | `30.68` | 1,571,591.66 USD | `+5.02%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,508,750.31 USD | `177,712.44` | `100.98` | `104.14` | `93.19` | 563,348.43 USD | `+3.04%` | `10X Isolated` |
| `285` | `0x7fda...17d1` | `SHORT` | 8,191,145.35 USD | `78,647.58` | `100.15` | `104.14` | `209.87` | -314,523.50 USD | `-3.84%` | `20X Cross` |
| `329` | `0x10e1...f4bd` | `LONG` | 7,043,235.09 USD | `67,625.88` | `84.36` | `104.14` | `58.53` | 1,338,004.71 USD | `+19.00%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,742,351.79 USD | `55,151.29` | `89.22` | `104.14` | `233.50` | -821,627.30 USD | `-14.31%` | `20X Cross` |
| `490` | `0x5989...bc29` | `SHORT` | 4,550,055.62 USD | `43,691.72` | `99.48` | `104.14` | `113.23` | -203,748.71 USD | `-4.48%` | `10X Cross` |
| `508` | `0x354b...6425` | `SHORT` | 4,422,113.98 USD | `42,446.86` | `102.98` | `104.14` | `363.79` | -50,758.46 USD | `-1.15%` | `8X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,166,000.00 USD | `40,000.00` | `101.97` | `104.14` | `118.61` | -87,370.00 USD | `-2.10%` | `20X Cross` |
| `535` | `0xd507...c948` | `LONG` | 4,146,054.96 USD | `39,808.50` | `93.57` | `104.14` | `85.21` | 420,979.55 USD | `+10.15%` | `7X Isolated` |
| `560` | `0x4692...164f` | `SHORT` | 3,986,286.90 USD | `38,259.78` | `103.67` | `104.14` | `1794.22` | -19,736.02 USD | `-0.50%` | `5X Cross` |
| `692` | `0xb5e7...eff1` | `SHORT` | 3,242,427.80 USD | `31,132.29` | `91.71` | `104.14` | `144.71` | -387,219.15 USD | `-11.94%` | `20X Cross` |
| `726` | `0xbd33...4200` | `SHORT` | 3,122,697.68 USD | `29,982.69` | `104.89` | `104.14` | `403.27` | 22,187.19 USD | `+0.71%` | `20X Cross` |
| `787` | `0x61d7...7dee` | `LONG` | 2,901,140.97 USD | `27,858.08` | `88.25` | `104.14` | `83.50` | 442,664.97 USD | `+15.26%` | `20X Cross` |
| `864` | `0xf0ae...2f74` | `SHORT` | 2,603,750.00 USD | `25,000.00` | `100.78` | `104.14` | `175.49` | -84,231.39 USD | `-3.24%` | `20X Cross` |
| `867` | `0x645b...87b8` | `SHORT` | 2,592,576.96 USD | `24,895.11` | `101.26` | `104.14` | `134.75` | -71,621.51 USD | `-2.76%` | `3X Isolated` |
| `873` | `0x40f2...6a9e` | `LONG` | 2,567,549.33 USD | `24,652.42` | `103.40` | `104.14` | `101.29` | 18,483.81 USD | `+0.72%` | `20X Cross` |
| `1035` | `0xebe1...4070` | `LONG` | 2,082,397.50 USD | `19,999.98` | `101.87` | `104.14` | `0.000000` | 44,972.76 USD | `+2.16%` | `20X Cross` |
| `1058` | `0x9aa5...58af` | `SHORT` | 2,048,734.65 USD | `19,671.00` | `101.76` | `104.14` | `563.61` | -46,983.72 USD | `-2.29%` | `20X Cross` |
| `1230` | `0x4169...6f06` | `LONG` | 1,788,796.04 USD | `17,175.19` | `76.61` | `104.14` | `82.98` | 473,028.04 USD | `+26.44%` | `12X Isolated` |
| `1244` | `0x6788...98d4` | `SHORT` | 1,770,040.00 USD | `17,000.00` | `99.31` | `104.14` | `195.30` | -81,715.41 USD | `-4.62%` | `20X Cross` |
| `1290` | `0xa99c...40d5` | `SHORT` | 1,676,332.00 USD | `16,100.00` | `101.02` | `104.14` | `149.06` | -49,874.63 USD | `-2.98%` | `20X Cross` |
| `1299` | `0x1bf6...5bfa` | `SHORT` | 1,666,400.00 USD | `16,000.00` | `99.60` | `104.14` | `226.81` | -72,777.69 USD | `-4.37%` | `20X Cross` |
| `1351` | `0xfc27...9d9d` | `LONG` | 1,586,988.42 USD | `15,233.14` | `102.72` | `104.14` | `0.000000` | 22,295.36 USD | `+1.40%` | `20X Cross` |
| `1374` | `0x5d6f...6f8a` | `LONG` | 1,562,250.00 USD | `15,000.00` | `101.91` | `104.14` | `24.68` | 33,595.00 USD | `+2.15%` | `20X Cross` |
| `1375` | `0x34ea...2f47` | `SHORT` | 1,561,800.00 USD | `15,000.00` | `99.80` | `104.14` | `196.79` | -64,798.69 USD | `-4.15%` | `20X Cross` |
| `1401` | `0xe5dd...ecba` | `SHORT` | 1,537,575.09 USD | `14,763.08` | `102.71` | `104.14` | `146.66` | -21,265.77 USD | `-1.38%` | `20X Cross` |
| `1506` | `0xfb29...21dd` | `LONG` | 1,431,905.24 USD | `13,744.53` | `89.85` | `104.14` | `84.65` | 196,911.28 USD | `+13.75%` | `20X Cross` |
| `1527` | `0x6fa6...825e` | `SHORT` | 1,405,890.00 USD | `13,500.00` | `102.95` | `104.14` | `135.50` | -16,115.73 USD | `-1.15%` | `20X Isolated` |
| `1555` | `0xa9d9...b48e` | `SHORT` | 1,388,666.63 USD | `13,333.33` | `96.39` | `104.14` | `173.39` | -103,419.45 USD | `-7.45%` | `20X Cross` |
| `1593` | `0xce97...7e78` | `SHORT` | 1,334,947.10 USD | `12,817.54` | `103.18` | `104.14` | `120.81` | -12,381.02 USD | `-0.93%` | `5X Isolated` |
| `1606` | `0x936c...bb0f` | `SHORT` | 1,321,064.98 USD | `12,687.91` | `101.39` | `104.14` | `163.64` | -34,592.11 USD | `-2.62%` | `2X Isolated` |
| `1639` | `0x89c2...c94b` | `LONG` | 1,287,411.63 USD | `12,364.69` | `75.25` | `104.14` | `45.76` | 356,928.48 USD | `+27.72%` | `3X Isolated` |
| `1680` | `0xcd81...36e3` | `SHORT` | 1,256,099.93 USD | `12,063.96` | `97.96` | `104.14` | `109.60` | -74,261.01 USD | `-5.91%` | `20X Cross` |
| `1687` | `0x436c...b3d1` | `SHORT` | 1,249,440.00 USD | `12,000.00` | `101.05` | `104.14` | `218.72` | -36,780.17 USD | `-2.94%` | `20X Cross` |
| `1749` | `0x9dea...d617` | `LONG` | 1,187,393.11 USD | `11,400.80` | `90.37` | `104.14` | `4.36` | 157,119.39 USD | `+13.23%` | `20X Cross` |
| `1761` | `0x17c3...a868` | `LONG` | 1,177,129.81 USD | `11,306.60` | `95.13` | `104.14` | `64.99` | 101,482.95 USD | `+8.62%` | `3X Isolated` |
| `1811` | `0x8607...08d5` | `SHORT` | 1,145,452.32 USD | `10,998.10` | `92.18` | `104.14` | `135.02` | -131,662.62 USD | `-11.49%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.86%`)
  * 48H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.35%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.89%`)
  * 7D Horizon: Short MP=`105.22` (Vol: 4,800,000.00 USD, Dist: `+0.96%`) | Long MP=`99.12` (Vol: 8,000,000.00 USD, Dist: `--4.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `104.01` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.75` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

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
  * Current Rate: `-152.14K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0243%` | **USDT OKX** | `-0.0280%` |
| **USDT Bybit** | `-0.0581%` | **USDT KuCoin** | `-0.0225%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0427%` | **USDT Bitget** | `-0.0208%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

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
| `10:30:00` | `104.29` | `104.29` | `104.29` | `104.30` | `103.92` | 37,649.77 USD | 32,026.75 USD | 5,623.02 USD | 26,403.74 USD | `+70.13%` | `1B / 0S` |
| `10:35:00` | `104.24` | `104.24` | `104.24` | `104.39` | `104.19` | 37,942.27 USD | 10,766.12 USD | 27,176.15 USD | -16,410.03 USD | `-43.25%` | `0B / 1S` |
| `10:40:00` | `104.35` | `104.35` | `104.35` | `104.42` | `104.24` | 39,756.59 USD | 27,897.38 USD | 11,859.21 USD | 16,038.17 USD | `+40.34%` | `1B / 0S` |
| `10:45:00` | `104.40` | `104.40` | `104.40` | `104.40` | `104.19` | 37,792.08 USD | 30,593.59 USD | 7,198.49 USD | 23,395.09 USD | `+61.90%` | `1B / 0S` |
| `10:45:00` | `104.45` | `104.45` | `104.45` | `104.72` | `104.19` | 130,246.66 USD | 70,652.67 USD | 59,593.99 USD | 11,058.68 USD | `+8.49%` | `1B / 0S` |
| `10:50:00` | `104.65` | `104.65` | `104.65` | `104.72` | `104.40` | 47,824.14 USD | 39,417.55 USD | 8,406.59 USD | 31,010.96 USD | `+64.84%` | `1B / 0S` |
| `10:55:00` | `104.45` | `104.45` | `104.45` | `104.70` | `104.38` | 44,703.74 USD | 8,381.95 USD | 36,321.79 USD | -27,939.84 USD | `-62.50%` | `0B / 1S` |
| `11:00:00` | `104.25` | `104.25` | `104.25` | `104.61` | `104.03` | 622,598.92 USD | 220,056.51 USD | 402,542.40 USD | -182,485.89 USD | `-29.31%` | `0B / 1S` |
| `11:00:00` | `104.50` | `104.50` | `104.50` | `104.59` | `104.30` | 57,996.39 USD | 36,370.62 USD | 21,625.77 USD | 14,744.84 USD | `+25.42%` | `1B / 0S` |
| `11:00:00` | `104.43` | `104.43` | `104.43` | `104.61` | `104.30` | 146,512.48 USD | 63,953.86 USD | 82,558.62 USD | -18,604.76 USD | `-12.70%` | `0B / 1S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `104.13` | `104.11` | `104.13` | `104.23` | `103.91` | 11,480,392.01 USD | 6,191,179.30 USD | 5,289,212.71 USD | 901,966.59 USD | `+7.86%` | `6B / 4S` |
| `0:00 UTC` | `104.13` | `104.08` | `104.13` | `104.30` | `103.81` | 32,456,048.03 USD | 16,079,340.84 USD | 16,376,707.20 USD | -297,366.36 USD | `-0.92%` | `6B / 5S` |
| `5:00 UTC` | `104.27` | `104.27` | `104.27` | `104.38` | `104.16` | 6,725,440.32 USD | 3,224,158.80 USD | 3,501,281.52 USD | -277,122.71 USD | `-4.12%` | `3B / 5S` |
| `0:00 UTC` | `104.25` | `104.18` | `104.25` | `104.31` | `104.02` | 8,036,249.92 USD | 3,423,895.23 USD | 4,612,354.69 USD | -1,188,459.46 USD | `-14.79%` | `2B / 6S` |
| `5:00 UTC` | `104.35` | `104.33` | `104.35` | `104.43` | `104.18` | 7,252,663.05 USD | 2,783,961.75 USD | 4,468,701.30 USD | -1,684,739.55 USD | `-23.23%` | `4B / 5S` |
| `0:00 UTC` | `104.30` | `104.27` | `104.30` | `104.41` | `104.12` | 12,776,351.50 USD | 5,809,244.29 USD | 6,967,107.21 USD | -1,157,862.92 USD | `-9.06%` | `5B / 4S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | WTI_OIL Macro Delta Flow: AGGRESSIVE BUY | `102.68` | 803,986.89 USD | 803,986.89 USD |
| `10-28 18:20` | `Volume 200K CL` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `102.21` | 51,000.00 USD | 0.00 USD |
| `10-28 11:54` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.96` | 0.00 USD | 0.00 USD |
| `10-28 07:12` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.50` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.63` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.35` (Risk Distance: `1.28` pts)
  * +2.5R Take Profit: `106.84`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.28 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `106.25` (Risk Distance: `1.28` pts)
  * +2.5R Take Profit: `101.76`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.28 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
