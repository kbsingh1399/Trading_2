# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:54:57 IST` (`2026-10-29 21:24:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.73` | **Live Ask Quote**: `66.81` | **Mid Price**: `66.77`
- **Spread Points**: `72.00` | **Spread BPS**: `10.78 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `52.73` | VWAP Z-Score: `-1.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1854` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.35` | Lower -3.00σ Band: `51.11`
  * Upper +2.51σ Band: `54.09` | Lower -2.51σ Band: `51.38`
  * Upper +2.01σ Band: `53.82` | Lower -2.01σ Band: `51.65`
  * Upper +2.00σ Band: `53.81` | Lower -2.00σ Band: `51.65`
  * Upper +1.28σ Band: `53.42` | Lower -1.28σ Band: `52.04`
  * Upper +1.00σ Band: `53.27` | Lower -1.00σ Band: `52.19`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.20` | EMA-20=`52.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.45` (Slope: `+0.0000`) | EMA-100=`52.80`
  * Institutional Anchors: EMA-144=`53.00` | EMA-200=`53.18` (Slope: `-0.2508`) | EMA-233=`53.26`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.92` (Distance: `-1.43%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.55%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.35%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.50` - `67.04`
  * Optimal Trade Entry (OTE 0.705): `66.90`
  * Structural Invalidation Anchor (0.786): `67.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.05` | `52.10` | `52.03` | `52.10` | `876` | 45,636.10 USD | 34,709.14 USD | `+76.06%` | -545,360.26 USD | `+1.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.10` | `52.12` | `52.06` | `52.11` | `872` | 45,436.43 USD | 17,038.66 USD | `+37.50%` | -528,321.60 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.11` | `52.11` | `52.04` | `52.05` | `1,018` | 52,986.90 USD | -37,648.59 USD | `-71.05%` | -565,970.19 USD | `-0.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.07` | `52.12` | `51.97` | `52.01` | `3,883` | 201,935.42 USD | -89,675.27 USD | `-44.41%` | -1,557,683.39 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.01` | `52.12` | `51.99` | `52.11` | `2,857` | 148,866.84 USD | 118,862.67 USD | `+79.84%` | -1,438,820.71 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.11` | `52.11` | `51.97` | `51.97` | `2,782` | 144,591.67 USD | -130,132.50 USD | `-90.00%` | -1,568,953.21 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -226,622.82 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -872,961.26 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.01` | `52.12` | `51.95` | `52.08` | `9,961` | 518,719.08 USD | 235,233.07 USD | `+45.35%` | -637,728.19 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,894,512.32 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -3,185,036.74 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `52.14` | `3.9000` | 203.36 USD | 128,971.98 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `52.15` | `48.5200` | 2,530.51 USD | 87,517.30 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `44.6900` | 2,330.67 USD | 89,847.97 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `137.6100` | 7,176.50 USD | 97,024.47 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `161.8200` | 8,438.91 USD | 105,463.38 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `68.3700` | 3,565.43 USD | 109,028.81 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `82.6100` | 4,307.95 USD | 113,336.76 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `52.15` | `295.9300` | 15,431.86 USD | 128,768.62 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `52.16` | `98.8100` | 5,154.42 USD | 43,315.86 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `73.1400` | 3,815.27 USD | 47,131.13 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `201.0300` | 10,486.33 USD | 57,617.46 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `49.5800` | 2,586.14 USD | 60,203.61 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `60.2700` | 3,143.68 USD | 63,347.29 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `208.2900` | 10,864.20 USD | 74,211.49 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `196.3900` | 10,243.31 USD | 84,454.80 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.16` | `10.2000` | 531.99 USD | 84,986.79 USD | `2 orders` | `-0.03%` | `-` |
| `ASK` | `52.17` | `0.2000` | 10.43 USD | 10,023.81 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.17` | `191.9300` | 10,013.37 USD | 10,013.37 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.17` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.17` | `0.00%` | `-` |
| `BID` | `52.17` | `413.0000` | 21,546.62 USD | 21,546.62 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `52.17` | `82.6700` | 4,312.81 USD | 25,859.43 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.17` | `215.8000` | 11,257.64 USD | 37,117.07 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.17` | `20.0200` | 1,044.36 USD | 38,161.44 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `52.18` | `33.8100` | 1,764.34 USD | 34,573.61 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `158.1100` | 8,250.65 USD | 32,809.27 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `46.4700` | 2,424.90 USD | 24,558.61 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `5.0600` | 264.04 USD | 22,133.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `196.7100` | 10,264.33 USD | 21,869.68 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `30.3100` | 1,581.55 USD | 11,605.35 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.19` | `104.9000` | 5,475.15 USD | 80,587.59 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.19` | `88.6700` | 4,627.86 USD | 75,112.44 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.19` | `251.4900` | 13,125.51 USD | 70,484.57 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.19` | `52.7900` | 2,755.11 USD | 57,359.06 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.19` | `161.8200` | 8,445.06 USD | 54,603.95 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.19` | `102.5500` | 5,351.78 USD | 46,158.88 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.19` | `119.4500` | 6,233.50 USD | 40,807.11 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.20` | `670.6600` | 35,007.78 USD | 155,873.26 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `52.20` | `407.3100` | 21,260.77 USD | 120,865.48 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `52.20` | `192.8600` | 10,066.71 USD | 99,604.71 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `52.20` | `13.5700` | 708.30 USD | 89,538.00 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `52.20` | `157.9100` | 8,242.11 USD | 88,829.70 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `113` | `0x5b5d...c060` | `SHORT` | 17,455,819.56 USD | `334,575.73` | `59.13` | `52.17` | `591.17` | 2,328,204.09 USD | `+13.34%` | `5X Cross` |
| `122` | `0x4692...164f` | `SHORT` | 16,200,863.87 USD | `310,516.04` | `53.32` | `52.17` | `249.38` | 355,410.17 USD | `+2.19%` | `5X Cross` |
| `177` | `0x49e9...e1d0` | `SHORT` | 11,292,776.39 USD | `216,444.52` | `55.61` | `52.17` | `92.54` | 742,766.58 USD | `+6.58%` | `4X Cross` |
| `204` | `0xacb6...efbd` | `SHORT` | 10,491,516.76 USD | `201,133.33` | `59.63` | `52.17` | `76.56` | 1,501,140.36 USD | `+14.31%` | `6X Cross` |
| `236` | `0xc26c...b8f4` | `LONG` | 9,466,220.25 USD | `181,463.41` | `55.43` | `52.17` | `0.000000` | -592,534.83 USD | `-6.26%` | `2X Cross` |
| `351` | `0x645b...87b8` | `LONG` | 6,590,095.85 USD | `126,309.96` | `56.63` | `52.17` | `0.000000` | -563,385.03 USD | `-8.55%` | `3X Cross` |
| `352` | `0xd8c5...99b0` | `SHORT` | 6,589,484.89 USD | `126,320.04` | `61.98` | `52.17` | `198.53` | 1,239,852.96 USD | `+18.82%` | `3X Cross` |
| `392` | `0xe9ff...5903` | `SHORT` | 5,894,101.53 USD | `112,996.08` | `60.07` | `52.17` | `199.34` | 893,849.28 USD | `+15.17%` | `5X Cross` |
| `415` | `0xfc66...ca06` | `SHORT` | 5,409,296.92 USD | `103,683.98` | `54.61` | `52.17` | `445.35` | 252,483.61 USD | `+4.67%` | `3X Cross` |
| `611` | `0x9aa5...58af` | `LONG` | 3,716,199.80 USD | `71,243.43` | `61.59` | `52.17` | `0.000000` | -671,957.73 USD | `-18.08%` | `20X Cross` |
| `727` | `0x2056...8396` | `LONG` | 3,130,440.00 USD | `60,000.00` | `66.92` | `52.17` | `21.34` | -884,887.14 USD | `-28.27%` | `10X Cross` |
| `761` | `0x354b...6425` | `LONG` | 3,008,921.81 USD | `57,669.80` | `52.37` | `52.17` | `0.000000` | -11,479.74 USD | `-0.38%` | `10X Cross` |
| `871` | `0x0242...ffa1` | `SHORT` | 2,603,953.01 USD | `49,916.67` | `56.48` | `52.17` | `334.70` | 215,178.86 USD | `+8.26%` | `10X Cross` |
| `878` | `0x960b...f0fc` | `LONG` | 2,580,073.40 USD | `49,457.96` | `55.82` | `52.17` | `0.000000` | -180,863.63 USD | `-7.01%` | `25X Cross` |
| `965` | `0x8b9d...7b28` | `LONG` | 2,338,081.84 USD | `44,823.47` | `58.35` | `52.17` | `0.000000` | -277,366.70 USD | `-11.86%` | `10X Cross` |
| `1062` | `0x5647...e7de` | `LONG` | 2,100,150.10 USD | `40,262.07` | `57.38` | `52.17` | `0.000000` | -210,087.50 USD | `-10.00%` | `20X Cross` |
| `1070` | `0xa2ce...3126` | `LONG` | 2,086,880.00 USD | `40,000.00` | `74.30` | `52.17` | `0.000000` | -885,175.49 USD | `-42.42%` | `20X Cross` |
| `1092` | `0xb078...de15` | `SHORT` | 2,034,786.52 USD | `39,000.01` | `52.58` | `52.17` | `205.51` | 15,732.43 USD | `+0.77%` | `8X Cross` |
| `1438` | `0x3678...b209` | `LONG` | 1,564,950.00 USD | `30,000.00` | `57.15` | `52.17` | `0.000000` | -149,550.00 USD | `-9.56%` | `20X Cross` |
| `1439` | `0x5a88...d997` | `LONG` | 1,564,920.00 USD | `30,000.00` | `59.50` | `52.17` | `39.85` | -219,967.59 USD | `-14.06%` | `25X Cross` |
| `1650` | `0x7ea9...fc7f` | `LONG` | 1,304,050.00 USD | `25,000.00` | `53.60` | `52.17` | `18.23` | -35,954.05 USD | `-2.76%` | `25X Cross` |
| `1778` | `0xf517...c032` | `LONG` | 1,180,295.66 USD | `22,627.50` | `66.29` | `52.17` | `0.000000` | -319,699.45 USD | `-27.09%` | `20X Cross` |
| `1903` | `0xcc9f...d218` | `LONG` | 1,070,395.54 USD | `20,520.60` | `52.63` | `52.17` | `26.86` | -9,512.51 USD | `-0.89%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.30` (Vol: 3,200,000.00 USD, Dist: `+1.87%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.22%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.28%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.22%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.28%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.70%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.79%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.69%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

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
  * Current Rate: `12.36K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

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
  * `2026-10-30 02:15:01 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.66` (Risk Distance: `0.3305` pts)
  * +2.5R Take Profit: `52.81`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.25` (Risk Distance: `0.3305` pts)
  * +2.5R Take Profit: `52.10`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
