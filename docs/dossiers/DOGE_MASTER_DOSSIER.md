# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 17:19:12 IST` (`2026-10-30 11:49:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0747` | **Live Ask Quote**: `0.0768` | **Mid Price**: `0.0757`
- **Spread Points**: `21.00` | **Spread BPS**: `277.23 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0738` | VWAP Z-Score: `+0.87` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000424` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.24` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0769` | Lower -3.00σ Band: `0.0707`
  * Upper +2.51σ Band: `0.0764` | Lower -2.51σ Band: `0.0712`
  * Upper +2.01σ Band: `0.0759` | Lower -2.01σ Band: `0.0717`
  * Upper +2.00σ Band: `0.0759` | Lower -2.00σ Band: `0.0718`
  * Upper +1.28σ Band: `0.0751` | Lower -1.28σ Band: `0.0725`
  * Upper +1.00σ Band: `0.0748` | Lower -1.00σ Band: `0.0728`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0746` | EMA-20=`0.0746` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0749` (Slope: `+0.0000`) | EMA-100=`0.0756`
  * Institutional Anchors: EMA-144=`0.0760` | EMA-200=`0.0763` (Slope: `-0.3082`) | EMA-233=`0.0765`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0754` (Distance: `+0.51%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.15%`)
  * Value Area Low (VAL) = `0.0737` (Distance: `+2.78%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0747`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0756` | Low=`0.0741`
  * New York Session (13:00-21:00 UTC): High=`0.0751` | Low=`0.0741`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0754` - `0.0761`
  * Optimal Trade Entry (OTE 0.705): `0.0759`
  * Structural Invalidation Anchor (0.786): `0.0764`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0761` | `0.0762` | `0.0759` | `0.0759` | `27,840,414` | 2,117,226.86 USD | -109,892.59 USD | `-5.19%` | -36,081,940.72 USD | `-0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0760` | `0.0760` | `0.0757` | `0.0758` | `17,651,423` | 1,339,513.15 USD | -204,213.51 USD | `-15.25%` | -36,286,154.23 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.0758` | `0.0759` | `0.0758` | `0.0758` | `2,124,584` | 161,036.21 USD | -82,348.87 USD | `-51.14%` | -36,368,503.10 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0755` | `0.0760` | `0.0754` | `0.0758` | `53,265,206` | 4,037,679.84 USD | 45,145.39 USD | `+1.12%` | -35,586,611.42 USD | `+0.87` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0758` | `0.0761` | `0.0756` | `0.0761` | `45,780,065` | 3,472,621.71 USD | -385,436.71 USD | `-11.10%` | -35,972,048.13 USD | `-0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0761` | `0.0762` | `0.0757` | `0.0758` | `47,606,421` | 3,617,018.52 USD | -397,212.67 USD | `-10.98%` | -36,369,260.80 USD | `-0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0756` | `0.0758` | `0.0752` | `0.0755` | `120,232,507` | 9,072,419.63 USD | -620,139.43 USD | `-6.84%` | -34,891,363.53 USD | `+0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0755` | `0.0761` | `0.0752` | `0.0761` | `183,491,006` | 13,873,684.21 USD | -478,013.81 USD | `-3.45%` | -35,369,377.34 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0761` | `0.0762` | `0.0757` | `0.0758` | `47,616,421` | 3,617,776.22 USD | -396,454.97 USD | `-10.96%` | -35,765,832.31 USD | `+0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0762` | `0.0752` | `0.0758` | `545,982,953` | 41,292,375.46 USD | -4,067,381.30 USD | `-9.85%` | -35,766,590.01 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | 1,581,082.63 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -21,458,643.59 USD | `-1.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0762` | `0.0752` | `0.0758` | `545,982,953` | 41,292,375.46 USD | -4,067,381.30 USD | `-9.85%` | -35,766,590.01 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.0757`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0758` | `322135.0000` | 24,430.40 USD | 198,343.82 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0758` | `361195.0000` | 27,392.31 USD | 173,913.43 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `0.0758` | `49935.0000` | 3,786.87 USD | 146,521.12 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `91690.0000` | 6,953.04 USD | 142,734.25 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `468443.0000` | 35,522.50 USD | 135,781.21 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `265449.0000` | 20,129.00 USD | 100,258.71 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `85990.0000` | 6,520.54 USD | 80,129.71 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `18127.0000` | 1,374.53 USD | 73,609.18 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `18127.0000` | 1,374.52 USD | 72,234.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `39583.0000` | 3,001.42 USD | 70,860.13 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `18130.0000` | 1,374.71 USD | 67,858.71 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `19038.0000` | 1,443.54 USD | 66,484.00 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `39590.0000` | 3,001.75 USD | 65,040.46 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `18130.0000` | 1,374.62 USD | 62,038.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `52662.0000` | 3,992.78 USD | 60,664.09 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `49357.0000` | 3,742.15 USD | 56,671.31 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `158340.0000` | 12,004.55 USD | 52,929.16 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `408173.0000` | 30,945.23 USD | 40,924.62 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `83575.0000` | 6,335.90 USD | 9,979.39 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `48062.0000` | 3,643.48 USD | 3,643.48 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0758` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0758` | `16780.0000` | 1,271.89 USD | 1,271.89 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `50101.0000` | 3,797.36 USD | 5,069.25 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `21453.0000` | 1,625.99 USD | 6,695.23 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `16089.0000` | 1,219.40 USD | 7,914.63 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `21453.0000` | 1,625.90 USD | 9,540.54 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `32029.0000` | 2,427.41 USD | 11,967.95 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `67900.0000` | 5,145.94 USD | 17,113.89 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `38107.0000` | 2,887.98 USD | 20,001.86 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `82899.0000` | 6,282.42 USD | 26,284.28 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `26287.0000` | 1,992.11 USD | 28,276.39 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `408294.0000` | 30,940.52 USD | 59,216.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `247363.0000` | 18,744.92 USD | 77,961.83 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `21454.0000` | 1,625.74 USD | 79,587.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `158340.0000` | 11,998.53 USD | 91,586.10 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `112030.0000` | 8,489.19 USD | 100,075.29 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `88262.0000` | 6,687.96 USD | 106,763.25 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `21453.0000` | 1,625.54 USD | 108,388.79 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0758` | `83842.0000` | 6,352.54 USD | 114,741.33 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `42472.0000` | 3,217.89 USD | 117,959.22 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0758` | `450705.0000` | 34,147.21 USD | 152,106.43 USD | `1 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `308` | `0xb83d...6e36` | `SHORT` | 7,778,918.78 USD | `102,645,925.00` | `0.0946` | `0.0758` | `1.06` | 1,928,422.87 USD | `+24.79%` | `3X Cross` |
| `317` | `0xc63a...a3cd` | `LONG` | 7,579,600.00 USD | `100,000,000.00` | `0.0856` | `0.0758` | `0.000000` | -985,221.96 USD | `-13.00%` | `10X Cross` |
| `320` | `0x610b...b613` | `LONG` | 7,476,645.61 USD | `98,666,424.00` | `0.0872` | `0.0758` | `0.0606` | -1,123,536.29 USD | `-15.03%` | `5X Cross` |
| `558` | `0xecb6...2b00` | `SHORT` | 4,012,135.51 USD | `52,933,341.00` | `0.0782` | `0.0758` | `0.6888` | 129,523.08 USD | `+3.23%` | `10X Cross` |
| `605` | `0x5b5d...c060` | `SHORT` | 3,749,366.77 USD | `49,478,955.00` | `0.0946` | `0.0758` | `2.95` | 932,149.83 USD | `+24.86%` | `3X Cross` |
| `641` | `0xca49...53c8` | `SHORT` | 3,527,746.62 USD | `46,542,649.00` | `0.0929` | `0.0758` | `0.3927` | 798,298.06 USD | `+22.63%` | `10X Cross` |
| `656` | `0x45d2...4029` | `SHORT` | 3,443,109.10 USD | `45,426,000.00` | `0.0954` | `0.0758` | `0.9585` | 892,520.12 USD | `+25.92%` | `10X Cross` |
| `1194` | `0x458d...ab3b` | `LONG` | 1,853,300.07 USD | `24,454,063.00` | `0.1002` | `0.0758` | `0.0714` | -597,621.83 USD | `-32.25%` | `3X Isolated` |
| `1197` | `0xeadc...9d55` | `LONG` | 1,843,091.73 USD | `24,317,440.00` | `0.0926` | `0.0758` | `0.000000` | -408,502.84 USD | `-22.16%` | `10X Cross` |
| `1337` | `0xf48f...10fe` | `LONG` | 1,623,419.84 USD | `21,424,497.00` | `0.0968` | `0.0758` | `0.0462` | -450,884.77 USD | `-27.77%` | `4X Cross` |
| `1359` | `0x9946...0852` | `SHORT` | 1,579,987.86 USD | `20,845,267.00` | `0.0859` | `0.0758` | `0.1505` | 211,298.16 USD | `+13.37%` | `10X Cross` |
| `1598` | `0x0d6a...ca57` | `LONG` | 1,335,768.01 USD | `17,626,455.00` | `0.0875` | `0.0758` | `0.0626` | -206,336.95 USD | `-15.45%` | `3X Isolated` |
| `1657` | `0x4808...a82c` | `LONG` | 1,275,388.13 USD | `16,828,143.00` | `0.0883` | `0.0758` | `0.0632` | -211,084.85 USD | `-16.55%` | `3X Cross` |
| `1718` | `0x9aa5...58af` | `SHORT` | 1,226,407.78 USD | `16,182,084.00` | `0.0907` | `0.0758` | `0.6214` | 240,797.41 USD | `+19.63%` | `10X Cross` |
| `1798` | `0x31ef...f715` | `LONG` | 1,154,350.35 USD | `15,230,102.00` | `0.0936` | `0.0758` | `0.0668` | -271,345.58 USD | `-23.51%` | `3X Isolated` |
| `1818` | `0xbfc7...80b4` | `SHORT` | 1,138,320.74 USD | `15,020,000.00` | `0.0920` | `0.0758` | `0.1758` | 244,078.55 USD | `+21.44%` | `10X Cross` |
| `1904` | `0x7cee...fc93` | `SHORT` | 1,062,052.71 USD | `14,013,468.00` | `0.0863` | `0.0758` | `0.2654` | 146,824.65 USD | `+13.82%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 7,301.12 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.30K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |
| `ANNOUNCEMENT` | `INFO` | `0.0796` | 6,511.06 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.51K USD at 0.0796 USD [API] | `2026-10-29 18:04:30` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 5,148.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.15K USD at 0.0793 USD [API] | `2026-10-29 18:28:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 8,833.99 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.83K USD at 0.0792 USD [API] | `2026-10-29 18:38:32` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 10,392.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.39K USD at 0.0792 USD [API] | `2026-10-29 18:38:32` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 9,242.18 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.24K USD at 0.0792 USD [API] | `2026-10-29 18:51:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 182.03 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.18K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 23,344.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 23.34K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 8,679.08 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.68K USD at 0.0791 USD [API] | `2026-10-29 19:07:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 23,344.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 23.34K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 622.87 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.62K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0814` | 10,475.77 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 10.48K USD at 0.0814 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 9,558.25 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0793 USD [API] | `2026-10-29 19:38:02` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 7,332.37 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.33K USD at 0.0793 USD [API] | `2026-10-29 19:54:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0933` | 4,799.26 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 4.80K USD at 0.0933 USD [API] | `2026-09-28 05:30:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0933` | 706.28 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.71K USD at 0.0933 USD [API] | `2026-09-28 05:30:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0774` | 6,079.72 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.08K USD at 0.0774 USD [API] | `2026-10-29 20:36:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`0.0725` (Vol: 1,700,000.00 USD, Dist: `--4.32%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0155` | 1,720.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0158` | 1,180.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 1,380.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0167` | 5,320.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 100.76 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0187` | 600.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0213` | 2,120.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0220` | 136.22 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0228` | 853.31 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0239` | 935.22 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 21,850.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0250` | 896.66 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0251` | 3,990.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0253` | 37,590.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 12,720.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0256` | 760.04 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0265` | 416.51 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 468.69 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 151.50 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0286` | 5,390.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0291` | 118.49 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0302` | 977.01 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0303` | 262.35 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0319` | 447.08 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0324` | 5,110.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0335` | 173.34 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 672.56 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 13,700.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 1,670.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 35,010.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 168.64 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 19,880.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,800.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 182.59 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 40,860.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 316.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 56,710.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 2,140.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 6,130.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0418` | 5,120.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.68 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 1,130.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 2,960.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 110,940.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 1,110.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 15,060.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,600.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 36,270.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 2,620.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 955,460.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 92,290.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 694.39 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 1,220.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 14,010.00 USD | 14,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 5,520.00 USD | 14,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 2,580.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 1,600.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 58,890.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 1,780.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0486` | 4,370.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 4,420.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 4,780.00 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 106.23 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,310.00 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 252.75 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,880.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 313.08 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 46,390.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 6,570.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,420.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 328.50 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 4,790.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 1,180.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 205,110.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0530` | 3,050.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 10,280.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 33,740.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 42,580.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 800.95 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 1,040.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 223.18 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 258.10 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 4,080.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,350.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 903.30 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 8,030.00 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 15,580.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 1,100.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 4,060.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 478.50 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 7,950.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 622.09 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 4,300.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 16,920.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 3,320.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 543.17 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,940.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 1,610.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 3,580.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 5,960,000.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 825.71 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 1,940.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 1,440.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,800.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,470,000.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 1,120.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 9,740.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 25,600.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 3,420.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 733.80 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 75,530.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,840.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 367.23 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0650` | 21,580.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 14,160.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0657` | 30,770,000.00 USD | 30,770,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0661` | 30,750,000.00 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0662` | 30,710,000.00 USD | 30,710,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0663` | 13,740.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0665` | 30,710,000.00 USD | 30,710,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 8,880.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0669` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 6,120.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 4,830.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0674` | 30,520,000.00 USD | 30,520,000.00 USD | 5,520.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0675` | 30,510,000.00 USD | 30,510,000.00 USD | 19,910.00 USD | 4,530.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0676` | 30,470,000.00 USD | 30,470,000.00 USD | 6,810.00 USD | 0.00 USD | 475.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0677` | 19,630,000.00 USD | 19,630,000.00 USD | 67,140.00 USD | 96,830.00 USD | 32,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0677` | 30,460,000.00 USD | 30,460,000.00 USD | 3,660.00 USD | 9,140.00 USD | 609.05 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 38,220.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 19,440,000.00 USD | 19,440,000.00 USD | 40,890.00 USD | 47,200.00 USD | 80,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0678` | 30,450,000.00 USD | 30,450,000.00 USD | 12,840.00 USD | 51,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 19,270,000.00 USD | 19,270,000.00 USD | 72,650.00 USD | 39,580.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0679` | 30,380,000.00 USD | 30,380,000.00 USD | 19,040.00 USD | 8,140.00 USD | 74,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 19,150,000.00 USD | 19,150,000.00 USD | 51,680.00 USD | 43,850.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0680` | 30,280,000.00 USD | 30,280,000.00 USD | 84,730.00 USD | 47,420.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 390.81 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 19,010,000.00 USD | 19,010,000.00 USD | 51,100.00 USD | 71,350.00 USD | 155,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0681` | 29,990,000.00 USD | 29,990,000.00 USD | 54,210.00 USD | 14,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 49,360.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 18,730,000.00 USD | 18,730,000.00 USD | 55,450.00 USD | 77,700.00 USD | 32,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0682` | 29,920,000.00 USD | 29,920,000.00 USD | 0.00 USD | 35,790.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,340.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 18,570,000.00 USD | 18,570,000.00 USD | 27,820.00 USD | 32,750.00 USD | 746.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0683` | 29,810,000.00 USD | 29,810,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,390.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 18,510,000.00 USD | 18,510,000.00 USD | 37,320.00 USD | 33,850.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0684` | 29,790,000.00 USD | 29,790,000.00 USD | 111,040.00 USD | 4,760.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 79,490.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 18,430,000.00 USD | 18,430,000.00 USD | 72,460.00 USD | 14,450.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0685` | 29,670,000.00 USD | 29,670,000.00 USD | 31,800.00 USD | 73,160.00 USD | 24,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 8,890.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 18,320,000.00 USD | 18,320,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0686` | 29,550,000.00 USD | 29,550,000.00 USD | 57,320.00 USD | 64,030.00 USD | 388.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 4,840.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 18,230,000.00 USD | 18,230,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0687` | 29,420,000.00 USD | 29,420,000.00 USD | 44,400.00 USD | 64,060.00 USD | 617.20 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 18,150,000.00 USD | 18,150,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0688` | 29,310,000.00 USD | 29,310,000.00 USD | 40,320.00 USD | 0.00 USD | 60,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 345.83 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 18,090,000.00 USD | 18,090,000.00 USD | 10,400.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0689` | 29,210,000.00 USD | 29,210,000.00 USD | 185,160.00 USD | 77,640.00 USD | 277.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0690` | 28,950,000.00 USD | 28,950,000.00 USD | 112,090.00 USD | 64,360.00 USD | 73,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 18,070,000.00 USD | 18,070,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0691` | 28,700,000.00 USD | 28,700,000.00 USD | 49,920.00 USD | 30,660.00 USD | 57,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 18,070,000.00 USD | 18,070,000.00 USD | 23,110.00 USD | 0.00 USD | 670.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0692` | 28,560,000.00 USD | 28,560,000.00 USD | 78,440.00 USD | 76,890.00 USD | 41,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,140.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 18,050,000.00 USD | 18,050,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0693` | 28,360,000.00 USD | 28,360,000.00 USD | 128,710.00 USD | 113,280.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 18,030,000.00 USD | 18,030,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0694` | 28,080,000.00 USD | 28,080,000.00 USD | 169,230.00 USD | 67,150.00 USD | 102,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 5,650.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 18,000,000.00 USD | 18,000,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0695` | 27,750,000.00 USD | 27,750,000.00 USD | 113,240.00 USD | 145,370.00 USD | 110,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 27,380,000.00 USD | 27,380,000.00 USD | 100,230.00 USD | 61,080.00 USD | 186,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 4,950.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 18,000,000.00 USD | 18,000,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0697` | 27,030,000.00 USD | 27,030,000.00 USD | 41,960.00 USD | 87,540.00 USD | 76,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,970.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 17,940,000.00 USD | 17,940,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 26,820,000.00 USD | 26,820,000.00 USD | 127,350.00 USD | 103,870.00 USD | 71,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 17,900,000.00 USD | 17,900,000.00 USD | 38,680.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0699` | 26,520,000.00 USD | 26,520,000.00 USD | 198,220.00 USD | 101,580.00 USD | 67,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 17,870,000.00 USD | 17,870,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 26,150,000.00 USD | 26,150,000.00 USD | 117,390.00 USD | 110,810.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 17,740,000.00 USD | 17,740,000.00 USD | 32,570.00 USD | 108,360.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0701` | 25,840,000.00 USD | 25,840,000.00 USD | 166,270.00 USD | 8,980.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,180.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 17,600,000.00 USD | 17,600,000.00 USD | 47,790.00 USD | 0.00 USD | 474.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 25,610,000.00 USD | 25,610,000.00 USD | 168,320.00 USD | 97,270.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 17,550,000.00 USD | 17,550,000.00 USD | 139,990.00 USD | 57,870.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0703` | 25,290,000.00 USD | 25,290,000.00 USD | 107,990.00 USD | 23,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 3,790.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 17,350,000.00 USD | 17,350,000.00 USD | 4,460.00 USD | 31,030.00 USD | 347.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 25,160,000.00 USD | 25,160,000.00 USD | 139,040.00 USD | 55,790.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 1,260.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 17,310,000.00 USD | 17,310,000.00 USD | 41,640.00 USD | 30,720.00 USD | 35,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0705` | 24,950,000.00 USD | 24,950,000.00 USD | 85,040.00 USD | 77,390.00 USD | 160,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 17,200,000.00 USD | 17,200,000.00 USD | 30,200.00 USD | 1,120.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 24,620,000.00 USD | 24,620,000.00 USD | 25,760.00 USD | 13,870.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 608.86 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 17,160,000.00 USD | 17,160,000.00 USD | 101,610.00 USD | 63,050.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 24,540,000.00 USD | 24,540,000.00 USD | 145,730.00 USD | 23,290.00 USD | 109,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 16,970,000.00 USD | 16,970,000.00 USD | 62,040.00 USD | 62,000.00 USD | 108,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 24,260,000.00 USD | 24,260,000.00 USD | 20,200.00 USD | 31,420.00 USD | 51,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 16,740,000.00 USD | 16,740,000.00 USD | 38,730.00 USD | 82,010.00 USD | 148,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 24,160,000.00 USD | 24,160,000.00 USD | 465,090.00 USD | 128,300.00 USD | 87,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 351.63 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 16,470,000.00 USD | 16,470,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 23,470,000.00 USD | 23,470,000.00 USD | 196,450.00 USD | 161,070.00 USD | 62,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 16,140,000.00 USD | 16,140,000.00 USD | 49,210.00 USD | 25,670.00 USD | 42,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 23,050,000.00 USD | 23,050,000.00 USD | 89,280.00 USD | 91,060.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,700.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 16,020,000.00 USD | 16,020,000.00 USD | 165,590.00 USD | 46,690.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 22,850,000.00 USD | 22,850,000.00 USD | 200,920.00 USD | 117,120.00 USD | 72,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,740.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 15,810,000.00 USD | 15,810,000.00 USD | 75,840.00 USD | 85,230.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0713` | 22,450,000.00 USD | 22,450,000.00 USD | 178,680.00 USD | 54,360.00 USD | 67,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 15,580,000.00 USD | 15,580,000.00 USD | 123,320.00 USD | 51,930.00 USD | 46,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 22,150,000.00 USD | 22,150,000.00 USD | 92,880.00 USD | 49,400.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 13,270.00 USD | 408,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 15,360,000.00 USD | 15,360,000.00 USD | 81,850.00 USD | 238,460.00 USD | 43,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0715` | 21,970,000.00 USD | 21,970,000.00 USD | 138,920.00 USD | 2,060.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 395,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 14,990,000.00 USD | 14,990,000.00 USD | 19,480.00 USD | 51,080.00 USD | 42.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 21,800,000.00 USD | 21,800,000.00 USD | 123,820.00 USD | 189,070.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 4,540.00 USD | 387,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 14,920,000.00 USD | 14,920,000.00 USD | 238,310.00 USD | 96,160.00 USD | 615.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 21,470,000.00 USD | 21,470,000.00 USD | 156,500.00 USD | 1,810.00 USD | 32,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 48,110.00 USD | 382,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 14,590,000.00 USD | 14,590,000.00 USD | 66,150.00 USD | 101,030.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 21,280,000.00 USD | 21,280,000.00 USD | 61,410.00 USD | 22,840.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 334,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 14,410,000.00 USD | 14,410,000.00 USD | 239,170.00 USD | 45,330.00 USD | 72,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 21,150,000.00 USD | 21,150,000.00 USD | 163,670.00 USD | 29,960.00 USD | 228,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 333,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 14,050,000.00 USD | 14,050,000.00 USD | 141,760.00 USD | 50,600.00 USD | 70,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 20,730,000.00 USD | 20,730,000.00 USD | 282,840.00 USD | 169,120.00 USD | 54,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 5,090.00 USD | 331,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 13,790,000.00 USD | 13,790,000.00 USD | 311,990.00 USD | 298,040.00 USD | 69,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 20,220,000.00 USD | 20,220,000.00 USD | 139,860.00 USD | 116,340.00 USD | 40,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 613.35 USD | 326,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 13,110,000.00 USD | 13,110,000.00 USD | 199,310.00 USD | 130,350.00 USD | 150,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 19,930,000.00 USD | 19,930,000.00 USD | 54,310.00 USD | 26,930.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 38,130.00 USD | 325,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 12,630,000.00 USD | 12,630,000.00 USD | 166,340.00 USD | 283,230.00 USD | 369,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 19,840,000.00 USD | 19,840,000.00 USD | 204,990.00 USD | 144,790.00 USD | 126,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 286,760.00 USD | 287,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 11,810,000.00 USD | 11,810,000.00 USD | 224,260.00 USD | 256,770.00 USD | 401,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 19,360,000.00 USD | 19,360,000.00 USD | 1,050,000.00 USD | 84,550.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 984.89 USD | 984.89 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 10,930,000.00 USD | 10,930,000.00 USD | 276,150.00 USD | 262,460.00 USD | 311,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 18,040,000.00 USD | 18,040,000.00 USD | 174,770.00 USD | 304,550.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 10,080,000.00 USD | 10,080,000.00 USD | 154,940.00 USD | 148,810.00 USD | 62,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 17,540,000.00 USD | 17,540,000.00 USD | 167,610.00 USD | 227,020.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 9,710,000.00 USD | 9,710,000.00 USD | 229,850.00 USD | 201,110.00 USD | 60,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 17,050,000.00 USD | 17,050,000.00 USD | 81,590.00 USD | 205,010.00 USD | 558.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 9,220,000.00 USD | 9,220,000.00 USD | 173,330.00 USD | 202,780.00 USD | 65,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 16,770,000.00 USD | 16,770,000.00 USD | 34,520.00 USD | 22,770.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 8,780,000.00 USD | 8,780,000.00 USD | 89,610.00 USD | 41,110.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 16,680,000.00 USD | 16,680,000.00 USD | 112,700.00 USD | 82,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 8,630,000.00 USD | 8,630,000.00 USD | 156,020.00 USD | 73,580.00 USD | 50,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 16,480,000.00 USD | 16,480,000.00 USD | 384,130.00 USD | 25,240.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 8,350,000.00 USD | 8,350,000.00 USD | 80,020.00 USD | 88,000.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 16,060,000.00 USD | 16,060,000.00 USD | 181,180.00 USD | 24,050.00 USD | 8,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 8,150,000.00 USD | 8,150,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 15,850,000.00 USD | 15,850,000.00 USD | 344,710.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 7,810,000.00 USD | 7,810,000.00 USD | 64,680.00 USD | 96,060.00 USD | 32,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 15,500,000.00 USD | 15,500,000.00 USD | 125,410.00 USD | 0.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 7,620,000.00 USD | 7,620,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 15,350,000.00 USD | 15,350,000.00 USD | 183,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 7,180,000.00 USD | 7,180,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 15,170,000.00 USD | 15,170,000.00 USD | 406,040.00 USD | 93,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 7,000,000.00 USD | 7,000,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 14,670,000.00 USD | 14,670,000.00 USD | 272,970.00 USD | 385,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 6,760,000.00 USD | 6,760,000.00 USD | 145,660.00 USD | 69,370.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 14,010,000.00 USD | 14,010,000.00 USD | 233,090.00 USD | 153,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 6,500,000.00 USD | 6,500,000.00 USD | 226,750.00 USD | 73,230.00 USD | 85,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 13,620,000.00 USD | 13,620,000.00 USD | 265,850.00 USD | 474,350.00 USD | 40,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 6,110,000.00 USD | 6,110,000.00 USD | 294,920.00 USD | 101,560.00 USD | 62,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 12,840,000.00 USD | 12,840,000.00 USD | 218,050.00 USD | 40,680.00 USD | 69,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 5,650,000.00 USD | 5,650,000.00 USD | 99,850.00 USD | 121,290.00 USD | 117,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 12,510,000.00 USD | 12,510,000.00 USD | 101,490.00 USD | 91,130.00 USD | 37,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 5,310,000.00 USD | 5,310,000.00 USD | 217,950.00 USD | 184,620.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 12,280,000.00 USD | 12,280,000.00 USD | 66,970.00 USD | 251,010.00 USD | 178,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,810,000.00 USD | 4,810,000.00 USD | 155,160.00 USD | 369,400.00 USD | 116,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 11,790,000.00 USD | 11,790,000.00 USD | 478,860.00 USD | 163,570.00 USD | 481,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 4,170,000.00 USD | 4,170,000.00 USD | 457,820.00 USD | 277,230.00 USD | 319,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 10,660,000.00 USD | 10,660,000.00 USD | 295,530.00 USD | 45,530.00 USD | 635,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,110,000.00 USD | 3,110,000.00 USD | 274,880.00 USD | 118,720.00 USD | 120,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 9,690,000.00 USD | 9,690,000.00 USD | 325,550.00 USD | 495,640.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,600,000.00 USD | 2,600,000.00 USD | 153,440.00 USD | 125,290.00 USD | 47,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 8,730,000.00 USD | 8,730,000.00 USD | 1,100,000.00 USD | 455,650.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,270,000.00 USD | 2,270,000.00 USD | 160,050.00 USD | 100,590.00 USD | 142,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 6,980,000.00 USD | 6,980,000.00 USD | 784,410.00 USD | 925,150.00 USD | 364,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,870,000.00 USD | 1,870,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 4,910,000.00 USD | 4,910,000.00 USD | 626,490.00 USD | 907,690.00 USD | 285,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 883,930.00 USD | 883,930.00 USD | 80,900.00 USD | 109,690.00 USD | 198,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 3,090,000.00 USD | 3,090,000.00 USD | 706,340.00 USD | 324,980.00 USD | 181,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 494,490.00 USD | 494,490.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 134,940.00 USD | 694,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 149,440.00 USD | 149,440.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 84,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 85,100.00 USD | 85,100.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 961,320.00 USD | 961,320.00 USD | 0.00 USD | 30,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 37,070.00 USD | 37,070.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 930,410.00 USD | 930,410.00 USD | 751,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 12,650.00 USD | 12,650.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 179,300.00 USD | 179,300.00 USD | 0.00 USD | 53,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 125,430.00 USD | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 19,100.00 USD | 19,100.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 38,200.00 USD | 38,200.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0758` | 104,490.00 USD | 104,490.00 USD | 0.00 USD | 66,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0759` | 144,860.00 USD | 144,860.00 USD | 40,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0760` | 424.91 USD | 424.91 USD | 0.00 USD | 0.00 USD | 424.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 837.25 USD | 837.25 USD | 0.00 USD | 0.00 USD | 412.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 15,660.00 USD | 15,660.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0764` | 399,460.00 USD | 399,460.00 USD | 0.00 USD | 254,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 363,970.00 USD | 363,970.00 USD | 211,600.00 USD | 37,120.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0765` | 1,410,000.00 USD | 1,410,000.00 USD | 772,480.00 USD | 241,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,140,000.00 USD | 1,140,000.00 USD | 352,420.00 USD | 421,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0766` | 2,100,000.00 USD | 2,100,000.00 USD | 594,350.00 USD | 90,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 1,800,000.00 USD | 1,800,000.00 USD | 164,440.00 USD | 335,150.00 USD | 159,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0767` | 2,730,000.00 USD | 2,730,000.00 USD | 587,940.00 USD | 45,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,970,000.00 USD | 2,970,000.00 USD | 352,400.00 USD | 143,560.00 USD | 680,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0768` | 2,950,000.00 USD | 2,950,000.00 USD | 117,000.00 USD | 7,860.00 USD | 92,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,190,000.00 USD | 4,190,000.00 USD | 420,080.00 USD | 469,120.00 USD | 325,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0769` | 4,330,000.00 USD | 4,330,000.00 USD | 861,620.00 USD | 76,450.00 USD | 445,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,120,000.00 USD | 5,120,000.00 USD | 282,920.00 USD | 275,070.00 USD | 370,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0770` | 5,340,000.00 USD | 5,340,000.00 USD | 392,100.00 USD | 325,170.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,180,000.00 USD | 6,180,000.00 USD | 368,880.00 USD | 460,320.00 USD | 236,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 597,990.00 USD | 520,750.00 USD | 540,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 7,940,000.00 USD | 7,940,000.00 USD | 545,340.00 USD | 406,470.00 USD | 802,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0772` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 284,970.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 9,090,000.00 USD | 9,090,000.00 USD | 412,480.00 USD | 464,690.00 USD | 278,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0773` | 7,480,000.00 USD | 7,480,000.00 USD | 69,030.00 USD | 62,610.00 USD | 62,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,560,000.00 USD | 9,560,000.00 USD | 176,230.00 USD | 246,740.00 USD | 49,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0774` | 7,830,000.00 USD | 7,830,000.00 USD | 137,990.00 USD | 210,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 10,200,000.00 USD | 10,200,000.00 USD | 354,430.00 USD | 217,430.00 USD | 61,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0775` | 8,700,000.00 USD | 8,700,000.00 USD | 707,860.00 USD | 164,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,930,000.00 USD | 10,930,000.00 USD | 356,410.00 USD | 228,210.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0776` | 8,990,000.00 USD | 8,990,000.00 USD | 250,110.00 USD | 39,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 11,830,000.00 USD | 11,830,000.00 USD | 401,010.00 USD | 342,630.00 USD | 163,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0777` | 9,260,000.00 USD | 9,260,000.00 USD | 15,870.00 USD | 247,550.00 USD | 693.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 12,690,000.00 USD | 12,690,000.00 USD | 116,640.00 USD | 340,450.00 USD | 399,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0778` | 9,650,000.00 USD | 9,650,000.00 USD | 229,240.00 USD | 86,160.00 USD | 78,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 13,450,000.00 USD | 13,450,000.00 USD | 345,840.00 USD | 210,420.00 USD | 206,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0779` | 10,270,000.00 USD | 10,270,000.00 USD | 41,210.00 USD | 215,530.00 USD | 359,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 13,780,000.00 USD | 13,780,000.00 USD | 212,580.00 USD | 78,920.00 USD | 38,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0780` | 10,510,000.00 USD | 10,510,000.00 USD | 169,380.00 USD | 64,660.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 14,150,000.00 USD | 14,150,000.00 USD | 151,030.00 USD | 193,800.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0781` | 10,600,000.00 USD | 10,600,000.00 USD | 17,030.00 USD | 77,790.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 14,410,000.00 USD | 14,410,000.00 USD | 87,770.00 USD | 92,890.00 USD | 80,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0782` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 148,920.00 USD | 195,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 15,000,000.00 USD | 15,000,000.00 USD | 129,550.00 USD | 239,780.00 USD | 220,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 11,160,000.00 USD | 11,160,000.00 USD | 32,110.00 USD | 159,820.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 15,660,000.00 USD | 15,660,000.00 USD | 436,380.00 USD | 152,210.00 USD | 70,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0784` | 11,500,000.00 USD | 11,500,000.00 USD | 109,020.00 USD | 45,010.00 USD | 187,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 16,190,000.00 USD | 16,190,000.00 USD | 238,930.00 USD | 171,160.00 USD | 121,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 12,010,000.00 USD | 12,010,000.00 USD | 248,170.00 USD | 120,330.00 USD | 144,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 17,050,000.00 USD | 17,050,000.00 USD | 353,390.00 USD | 218,960.00 USD | 294,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0786` | 12,900,000.00 USD | 12,900,000.00 USD | 201,610.00 USD | 202,070.00 USD | 488,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 18,380,000.00 USD | 18,380,000.00 USD | 418,420.00 USD | 504,080.00 USD | 404,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 13,610,000.00 USD | 13,610,000.00 USD | 235,890.00 USD | 143,980.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 354.19 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 19,110,000.00 USD | 19,110,000.00 USD | 280,900.00 USD | 310,220.00 USD | 139,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0788` | 13,850,000.00 USD | 13,850,000.00 USD | 74,330.00 USD | 22,770.00 USD | 146,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0789` | 2,430.00 USD | 2,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0789` | 19,800,000.00 USD | 19,800,000.00 USD | 343,470.00 USD | 233,260.00 USD | 111,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0789` | 14,450,000.00 USD | 14,450,000.00 USD | 260,530.00 USD | 236,420.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 20,120,000.00 USD | 20,120,000.00 USD | 189,430.00 USD | 105,510.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0790` | 14,870,000.00 USD | 14,870,000.00 USD | 353,930.00 USD | 65,630.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0790` | 5,710.00 USD | 8,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0791` | 20,630,000.00 USD | 20,630,000.00 USD | 241,350.00 USD | 140,450.00 USD | 123,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 15,040,000.00 USD | 15,040,000.00 USD | 142,610.00 USD | 15,670.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0791` | 1,650.00 USD | 10,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0792` | 20,990,000.00 USD | 20,990,000.00 USD | 224,560.00 USD | 57,840.00 USD | 75,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0792` | 15,110,000.00 USD | 15,110,000.00 USD | 13,630.00 USD | 61,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0793` | 20,990,000.00 USD | 20,990,000.00 USD | 5,950.00 USD | 0.00 USD | 462.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 15,370,000.00 USD | 15,370,000.00 USD | 13,920.00 USD | 0.00 USD | 244,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0794` | 3,550.00 USD | 13,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 21,350,000.00 USD | 21,350,000.00 USD | 160,150.00 USD | 96,210.00 USD | 100,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0794` | 15,630,000.00 USD | 15,630,000.00 USD | 23,360.00 USD | 0.00 USD | 234,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 5,910.00 USD | 19,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 21,600,000.00 USD | 21,600,000.00 USD | 102,330.00 USD | 45,380.00 USD | 105,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 16,050,000.00 USD | 16,050,000.00 USD | 183,540.00 USD | 0.00 USD | 235,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 21,820,000.00 USD | 21,820,000.00 USD | 202,390.00 USD | 12,890.00 USD | 588.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 16,610,000.00 USD | 16,610,000.00 USD | 334,830.00 USD | 149,090.00 USD | 77,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 22,130,000.00 USD | 22,130,000.00 USD | 210,380.00 USD | 89,760.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 17,010,000.00 USD | 17,010,000.00 USD | 305,960.00 USD | 54,460.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 22,200,000.00 USD | 22,200,000.00 USD | 58,670.00 USD | 9,940.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 17,660,000.00 USD | 17,660,000.00 USD | 520,400.00 USD | 54,200.00 USD | 73,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 22,460,000.00 USD | 22,460,000.00 USD | 43,250.00 USD | 191,860.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 17,780,000.00 USD | 17,780,000.00 USD | 41,190.00 USD | 76,670.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 22,610,000.00 USD | 22,610,000.00 USD | 48,550.00 USD | 9,760.00 USD | 94,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0800` | 17,930,000.00 USD | 17,930,000.00 USD | 46,190.00 USD | 0.00 USD | 102,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 22,640,000.00 USD | 22,640,000.00 USD | 25,740.00 USD | 0.00 USD | 3,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0801` | 17,970,000.00 USD | 17,970,000.00 USD | 38,850.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 22,670,000.00 USD | 22,670,000.00 USD | 27,390.00 USD | 1,770.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0802` | 17,990,000.00 USD | 17,990,000.00 USD | 12,270.00 USD | 0.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 22,780,000.00 USD | 22,780,000.00 USD | 25,660.00 USD | 43,340.00 USD | 38,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 18,030,000.00 USD | 18,030,000.00 USD | 45,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 213.09 USD | 19,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0804` | 22,790,000.00 USD | 22,790,000.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 18,140,000.00 USD | 18,140,000.00 USD | 108,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 826.14 USD | 20,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0805` | 22,960,000.00 USD | 22,960,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 18,360,000.00 USD | 18,360,000.00 USD | 120,200.00 USD | 43,910.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 23,220,000.00 USD | 23,220,000.00 USD | 28,730.00 USD | 21,040.00 USD | 215,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 18,460,000.00 USD | 18,460,000.00 USD | 99,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0806` | 213.40 USD | 20,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0807` | 23,630,000.00 USD | 23,630,000.00 USD | 229,530.00 USD | 143,670.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 19,800,000.00 USD | 19,800,000.00 USD | 118,470.00 USD | 934,840.00 USD | 294,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0808` | 214.31 USD | 21,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0808` | 24,290,000.00 USD | 24,290,000.00 USD | 158,180.00 USD | 116,140.00 USD | 382,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 20,720,000.00 USD | 20,720,000.00 USD | 9,880.00 USD | 910,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 24,630,000.00 USD | 24,630,000.00 USD | 111,710.00 USD | 220,760.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 851,040.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 25,070,000.00 USD | 25,070,000.00 USD | 177,780.00 USD | 127,690.00 USD | 133,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 21,970,000.00 USD | 21,970,000.00 USD | 131,030.00 USD | 264,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 25,270,000.00 USD | 25,270,000.00 USD | 100,060.00 USD | 85,950.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 466,230.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0811` | 215.29 USD | 21,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0812` | 25,520,000.00 USD | 25,520,000.00 USD | 133,170.00 USD | 101,130.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 22,780,000.00 USD | 22,780,000.00 USD | 138,370.00 USD | 200,500.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 25,640,000.00 USD | 25,640,000.00 USD | 37,200.00 USD | 28,660.00 USD | 55,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 23,510,000.00 USD | 23,510,000.00 USD | 378,950.00 USD | 347,890.00 USD | 874.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 25,940,000.00 USD | 25,940,000.00 USD | 41,140.00 USD | 108,690.00 USD | 143,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 24,100,000.00 USD | 24,100,000.00 USD | 142,940.00 USD | 446,780.00 USD | 3,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0814` | 216.17 USD | 21,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0815` | 26,050,000.00 USD | 26,050,000.00 USD | 10,870.00 USD | 6,740.00 USD | 96,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 24,960,000.00 USD | 24,960,000.00 USD | 447,170.00 USD | 144,240.00 USD | 265,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 26,670,000.00 USD | 26,670,000.00 USD | 287,650.00 USD | 167,460.00 USD | 165,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 25,820,000.00 USD | 25,820,000.00 USD | 267,850.00 USD | 451,830.00 USD | 145,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 27,050,000.00 USD | 27,050,000.00 USD | 191,130.00 USD | 121,600.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 27,340,000.00 USD | 27,340,000.00 USD | 789,320.00 USD | 294,010.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 595.63 USD | 22,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 27,670,000.00 USD | 27,670,000.00 USD | 195,830.00 USD | 161,260.00 USD | 260,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 28,310,000.00 USD | 28,310,000.00 USD | 249,420.00 USD | 327,510.00 USD | 388,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 22,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 28,270,000.00 USD | 28,270,000.00 USD | 153,870.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 29,460,000.00 USD | 29,460,000.00 USD | 422,920.00 USD | 184,980.00 USD | 540,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 28,800,000.00 USD | 28,800,000.00 USD | 42,510.00 USD | 172,050.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 30,350,000.00 USD | 30,350,000.00 USD | 288,610.00 USD | 382,680.00 USD | 217,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 29,080,000.00 USD | 29,080,000.00 USD | 144,440.00 USD | 48,110.00 USD | 84,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 31,810,000.00 USD | 31,810,000.00 USD | 916,830.00 USD | 377,990.00 USD | 172,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 29,630,000.00 USD | 29,630,000.00 USD | 247,310.00 USD | 151,600.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 32,520,000.00 USD | 32,520,000.00 USD | 374,110.00 USD | 203,780.00 USD | 128,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 29,980,000.00 USD | 29,980,000.00 USD | 267,050.00 USD | 72,540.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 33,590,000.00 USD | 33,590,000.00 USD | 510,700.00 USD | 317,120.00 USD | 237,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 30,540,000.00 USD | 30,540,000.00 USD | 158,060.00 USD | 204,930.00 USD | 191,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 34,530,000.00 USD | 34,530,000.00 USD | 470,790.00 USD | 274,570.00 USD | 194,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 120.38 USD | 22,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0825` | 30,780,000.00 USD | 30,780,000.00 USD | 99,620.00 USD | 125,690.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 35,170,000.00 USD | 35,170,000.00 USD | 290,680.00 USD | 239,750.00 USD | 112,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0825` | 217.85 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0826` | 31,210,000.00 USD | 31,210,000.00 USD | 131,950.00 USD | 125,260.00 USD | 169,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 36,000,000.00 USD | 36,000,000.00 USD | 514,230.00 USD | 68,910.00 USD | 251,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 31,310,000.00 USD | 31,310,000.00 USD | 19,540.00 USD | 65,440.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 36,330,000.00 USD | 36,330,000.00 USD | 144,110.00 USD | 160,890.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 31,690,000.00 USD | 31,690,000.00 USD | 211,700.00 USD | 83,250.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 36,870,000.00 USD | 36,870,000.00 USD | 376,390.00 USD | 110,640.00 USD | 54,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 218.81 USD | 23,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 31,980,000.00 USD | 31,980,000.00 USD | 198,070.00 USD | 89,690.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 37,400,000.00 USD | 37,400,000.00 USD | 283,400.00 USD | 67,100.00 USD | 173,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0829` | 220.48 USD | 23,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 32,120,000.00 USD | 32,120,000.00 USD | 54,060.00 USD | 37,820.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 37,760,000.00 USD | 37,760,000.00 USD | 112,420.00 USD | 80,560.00 USD | 173,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 32,200,000.00 USD | 32,200,000.00 USD | 20,050.00 USD | 16,920.00 USD | 45,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 38,210,000.00 USD | 38,210,000.00 USD | 294,840.00 USD | 53,670.00 USD | 98,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 26,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 32,580,000.00 USD | 32,580,000.00 USD | 182,710.00 USD | 93,160.00 USD | 100,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 38,820,000.00 USD | 38,820,000.00 USD | 186,700.00 USD | 262,800.00 USD | 160,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 33,030,000.00 USD | 33,030,000.00 USD | 137,070.00 USD | 126,610.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 39,340,000.00 USD | 39,340,000.00 USD | 266,360.00 USD | 152,020.00 USD | 100,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 33,480,000.00 USD | 33,480,000.00 USD | 163,150.00 USD | 137,940.00 USD | 148,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 39,840,000.00 USD | 39,840,000.00 USD | 90,460.00 USD | 146,730.00 USD | 265,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 33,850,000.00 USD | 33,850,000.00 USD | 119,790.00 USD | 188,990.00 USD | 65,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 40,500,000.00 USD | 40,500,000.00 USD | 275,000.00 USD | 115,070.00 USD | 271,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 34,140,000.00 USD | 34,140,000.00 USD | 57,220.00 USD | 82,000.00 USD | 147,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 40,820,000.00 USD | 40,820,000.00 USD | 204,620.00 USD | 27,680.00 USD | 88,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 26,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 34,380,000.00 USD | 34,380,000.00 USD | 144,720.00 USD | 32,170.00 USD | 62,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0837` | 41,290,000.00 USD | 41,290,000.00 USD | 239,800.00 USD | 199,750.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 28,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 34,680,000.00 USD | 34,680,000.00 USD | 172,840.00 USD | 85,610.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 41,580,000.00 USD | 41,580,000.00 USD | 199,340.00 USD | 64,030.00 USD | 31,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 221.45 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0839` | 34,780,000.00 USD | 34,780,000.00 USD | 43,590.00 USD | 32,460.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0839` | 41,750,000.00 USD | 41,750,000.00 USD | 94,520.00 USD | 64,060.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 221.54 USD | 29,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0840` | 41,930,000.00 USD | 41,930,000.00 USD | 117,710.00 USD | 0.00 USD | 62,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0841` | 42,020,000.00 USD | 42,020,000.00 USD | 87,460.00 USD | 0.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 42,350,000.00 USD | 42,350,000.00 USD | 220,360.00 USD | 33,520.00 USD | 81,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 264.21 USD | 29,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0843` | 42,520,000.00 USD | 42,520,000.00 USD | 117,190.00 USD | 44,120.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 42,820,000.00 USD | 42,820,000.00 USD | 164,260.00 USD | 64,360.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0845` | 42,980,000.00 USD | 42,980,000.00 USD | 70,690.00 USD | 30,660.00 USD | 57,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 43,210,000.00 USD | 43,210,000.00 USD | 106,330.00 USD | 76,890.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 223.39 USD | 29,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0847` | 43,490,000.00 USD | 43,490,000.00 USD | 137,750.00 USD | 113,280.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 43,770,000.00 USD | 43,770,000.00 USD | 117,070.00 USD | 57,210.00 USD | 99,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 29,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0853` | 224.97 USD | 30,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0854` | 1,030.00 USD | 31,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 31,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,250.00 USD | 35,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0864` | 841.68 USD | 36,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0868` | 155.98 USD | 36,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 36,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0877` | 231.57 USD | 36,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 37,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 37,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 38,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 38,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0901` | 237.64 USD | 38,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0902` | 2,740.00 USD | 41,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 48,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 49,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 54,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 54,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 55,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 95,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0945` | 47,230.00 USD | 142,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0948` | 4,260.00 USD | 146,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 171,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 761.26 USD | 171,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0954` | 194.04 USD | 172,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 172,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0970` | 365.68 USD | 173,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 173,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 173,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 202.21 USD | 173,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 181,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 184,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 184,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1041` | 3,230.00 USD | 188,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 194,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 194,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1084` | 1,860.00 USD | 196,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 200,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1137` | 147.86 USD | 200,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1152` | 147.05 USD | 200,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1197` | 863.75 USD | 201,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 201,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1239` | 119.52 USD | 202,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 202,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1281` | 5,730.00 USD | 207,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1288` | 15,200.00 USD | 223,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 223,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 225,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1313` | 44,950.00 USD | 270,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 270,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 270,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1354` | 134.64 USD | 270,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1376` | 1,160.00 USD | 272,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1386` | 1,210.00 USD | 273,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1401` | 22,710.00 USD | 295,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 296,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1421` | 31,460.00 USD | 328,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 1,800.00 USD | 329,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 331,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 331,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 13,770.00 USD | 345,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 347,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1446` | 144.55 USD | 347,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1447` | 1,830.00 USD | 349,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1457` | 1,930.00 USD | 351,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,090.00 USD | 359,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1482` | 3,090,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1495` | 448.65 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0155` | 16,410,000.00 USD | 0.00 USD | 1,720.00 USD | `-79.70%` | `111,254.00` |
| `Live` | `Long` | `0.0158` | 16,410,000.00 USD | 0.00 USD | 1,180.00 USD | `-79.31%` | `75,012.00` |
| `Live` | `Long` | `0.0160` | 16,410,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.91%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,400,000.00 USD | 0.00 USD | 1,380.00 USD | `-78.39%` | `84,060.00` |
| `Live` | `Long` | `0.0167` | 16,400,000.00 USD | 0.00 USD | 5,320.00 USD | `-78.12%` | `319,394.00` |
| `Live` | `Long` | `0.0186` | 16,400,000.00 USD | 0.00 USD | 100.76 USD | `-75.63%` | `5,432.00` |
| `Live` | `Long` | `0.0187` | 16,400,000.00 USD | 0.00 USD | 600.00 USD | `-75.36%` | `32,000.00` |
| `Live` | `Long` | `0.0213` | 16,400,000.00 USD | 0.00 USD | 2,120.00 USD | `-72.08%` | `100,000.00` |
| `Live` | `Long` | `0.0215` | 16,390,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.69%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,380,000.00 USD | 0.00 USD | 541.25 USD | `-71.55%` | `25,000.00` |
| `Live` | `Long` | `0.0220` | 16,370,000.00 USD | 0.00 USD | 136.22 USD | `-71.16%` | `6,206.00` |
| `Live` | `Long` | `0.0228` | 16,370,000.00 USD | 0.00 USD | 853.31 USD | `-69.98%` | `37,344.00` |
| `Live` | `Long` | `0.0239` | 16,370,000.00 USD | 0.00 USD | 935.22 USD | `-68.53%` | `39,049.00` |
| `Live` | `Long` | `0.0244` | 16,370,000.00 USD | 0.00 USD | 21,850.00 USD | `-67.88%` | `893,720.00` |
| `Live` | `Long` | `0.0250` | 16,350,000.00 USD | 0.00 USD | 896.66 USD | `-67.09%` | `35,795.00` |
| `Live` | `Long` | `0.0251` | 16,350,000.00 USD | 0.00 USD | 3,990.00 USD | `-66.96%` | `158,606.00` |
| `Live` | `Long` | `0.0253` | 16,350,000.00 USD | 0.00 USD | 37,590.00 USD | `-66.82%` | `1,488,849.00` |
| `Live` | `Long` | `0.0255` | 16,310,000.00 USD | 0.00 USD | 12,720.00 USD | `-66.56%` | `500,000.00` |
| `Live` | `Long` | `0.0256` | 16,300,000.00 USD | 0.00 USD | 760.04 USD | `-66.30%` | `29,631.00` |
| `Live` | `Long` | `0.0265` | 16,290,000.00 USD | 0.00 USD | 416.51 USD | `-65.25%` | `15,747.00` |
| `Live` | `Long` | `0.0272` | 16,290,000.00 USD | 0.00 USD | 468.69 USD | `-64.33%` | `17,263.00` |
| `Live` | `Long` | `0.0279` | 16,290,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.28%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 16,290,000.00 USD | 0.00 USD | 151.50 USD | `-62.75%` | `5,344.00` |
| `Live` | `Long` | `0.0286` | 16,290,000.00 USD | 0.00 USD | 5,390.00 USD | `-62.36%` | `187,979.00` |
| `Live` | `Long` | `0.0291` | 16,290,000.00 USD | 0.00 USD | 118.49 USD | `-61.70%` | `4,065.00` |
| `Live` | `Long` | `0.0302` | 16,290,000.00 USD | 0.00 USD | 977.01 USD | `-60.25%` | `32,298.00` |
| `Live` | `Long` | `0.0303` | 16,290,000.00 USD | 0.00 USD | 262.35 USD | `-60.12%` | `8,644.00` |
| `Live` | `Long` | `0.0306` | 16,290,000.00 USD | 0.00 USD | 137.41 USD | `-59.86%` | `4,498.00` |
| `Live` | `Long` | `0.0319` | 16,290,000.00 USD | 0.00 USD | 447.08 USD | `-58.15%` | `14,037.00` |
| `Live` | `Long` | `0.0324` | 16,280,000.00 USD | 0.00 USD | 5,110.00 USD | `-57.36%` | `157,443.00` |
| `Live` | `Long` | `0.0335` | 16,280,000.00 USD | 0.00 USD | 173.34 USD | `-56.05%` | `5,182.00` |
| `Live` | `Long` | `0.0336` | 16,280,000.00 USD | 0.00 USD | 393.23 USD | `-55.79%` | `11,686.00` |
| `Live` | `Long` | `0.0340` | 16,280,000.00 USD | 0.00 USD | 672.56 USD | `-55.26%` | `19,752.00` |
| `Live` | `Long` | `0.0352` | 16,280,000.00 USD | 0.00 USD | 13,700.00 USD | `-53.82%` | `389,633.00` |
| `Live` | `Long` | `0.0352` | 16,260,000.00 USD | 0.00 USD | 1,670.00 USD | `-53.69%` | `47,501.00` |
| `Live` | `Long` | `0.0358` | 16,260,000.00 USD | 0.00 USD | 214.53 USD | `-52.90%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,260,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.77%` | `233,408.00` |
| `Live` | `Long` | `0.0369` | 16,250,000.00 USD | 0.00 USD | 35,010.00 USD | `-51.58%` | `950,000.00` |
| `Live` | `Long` | `0.0374` | 16,220,000.00 USD | 0.00 USD | 168.64 USD | `-50.93%` | `4,515.00` |
| `Live` | `Long` | `0.0377` | 16,220,000.00 USD | 0.00 USD | 19,880.00 USD | `-50.40%` | `526,651.00` |
| `Live` | `Long` | `0.0381` | 16,200,000.00 USD | 0.00 USD | 1,800.00 USD | `-50.01%` | `47,278.00` |
| `Live` | `Long` | `0.0386` | 16,200,000.00 USD | 0.00 USD | 121.74 USD | `-49.35%` | `3,158.00` |
| `Live` | `Long` | `0.0389` | 16,200,000.00 USD | 0.00 USD | 182.59 USD | `-48.96%` | `4,700.00` |
| `Live` | `Long` | `0.0393` | 16,200,000.00 USD | 0.00 USD | 221.10 USD | `-48.43%` | `5,633.00` |
| `Live` | `Long` | `0.0396` | 16,200,000.00 USD | 0.00 USD | 40,860.00 USD | `-47.90%` | `1,030,567.00` |
| `Live` | `Long` | `0.0399` | 16,160,000.00 USD | 0.00 USD | 103.31 USD | `-47.51%` | `2,586.00` |
| `Live` | `Long` | `0.0403` | 16,160,000.00 USD | 0.00 USD | 316.00 USD | `-47.12%` | `7,851.00` |
| `Live` | `Long` | `0.0403` | 16,160,000.00 USD | 0.00 USD | 56,710.00 USD | `-46.98%` | `1,405,488.00` |
| `Live` | `Long` | `0.0404` | 16,100,000.00 USD | 0.00 USD | 2,140.00 USD | `-46.85%` | `52,846.00` |
| `Live` | `Long` | `0.0408` | 16,100,000.00 USD | 0.00 USD | 419.28 USD | `-46.46%` | `10,289.00` |
| `Live` | `Long` | `0.0415` | 16,100,000.00 USD | 0.00 USD | 6,130.00 USD | `-45.54%` | `147,817.00` |
| `Live` | `Long` | `0.0415` | 16,090,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.41%` | `24,809.00` |
| `Live` | `Long` | `0.0418` | 16,090,000.00 USD | 0.00 USD | 5,120.00 USD | `-45.01%` | `122,306.00` |
| `Live` | `Long` | `0.0420` | 16,080,000.00 USD | 0.00 USD | 266.68 USD | `-44.75%` | `6,342.00` |
| `Live` | `Long` | `0.0421` | 16,080,000.00 USD | 0.00 USD | 1,130.00 USD | `-44.62%` | `26,900.00` |
| `Live` | `Long` | `0.0423` | 16,080,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.49%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,080,000.00 USD | 0.00 USD | 267.52 USD | `-44.36%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,080,000.00 USD | 0.00 USD | 455.06 USD | `-44.23%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,080,000.00 USD | 0.00 USD | 883.34 USD | `-44.09%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,080,000.00 USD | 0.00 USD | 2,960.00 USD | `-43.96%` | `69,502.00` |
| `Live` | `Long` | `0.0428` | 16,080,000.00 USD | 0.00 USD | 110,940.00 USD | `-43.70%` | `2,589,112.00` |
| `Live` | `Long` | `0.0430` | 15,970,000.00 USD | 0.00 USD | 859.00 USD | `-43.57%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 15,960,000.00 USD | 0.00 USD | 1,110.00 USD | `-43.31%` | `25,729.00` |
| `Live` | `Long` | `0.0432` | 15,960,000.00 USD | 0.00 USD | 15,060.00 USD | `-43.17%` | `348,236.00` |
| `Live` | `Long` | `0.0433` | 15,950,000.00 USD | 0.00 USD | 2,600.00 USD | `-43.04%` | `59,880.00` |
| `Live` | `Long` | `0.0437` | 15,950,000.00 USD | 0.00 USD | 36,270.00 USD | `-42.52%` | `829,067.00` |
| `Live` | `Long` | `0.0439` | 15,910,000.00 USD | 0.00 USD | 2,620.00 USD | `-42.39%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 15,910,000.00 USD | 0.00 USD | 750.58 USD | `-42.25%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 15,910,000.00 USD | 0.00 USD | 955,460.00 USD | `-42.12%` | `21,690,444.00` |
| `Live` | `Long` | `0.0444` | 14,950,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.73%` | `2,287,370.00` |
| `Live` | `Long` | `0.0445` | 14,850,000.00 USD | 0.00 USD | 92,290.00 USD | `-41.60%` | `2,076,269.00` |
| `Live` | `Long` | `0.0447` | 14,760,000.00 USD | 0.00 USD | 694.39 USD | `-41.20%` | `15,517.00` |
| `Live` | `Long` | `0.0449` | 14,760,000.00 USD | 0.00 USD | 810.81 USD | `-40.94%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 14,760,000.00 USD | 0.00 USD | 1,220.00 USD | `-40.55%` | `27,061.00` |
| `Live` | `Long` | `0.0454` | 14,750,000.00 USD | 0.00 USD | 2,170.00 USD | `-40.28%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,750,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.15%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,720,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.89%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 14,710,000.00 USD | 0.00 USD | 14,010.00 USD | `-39.63%` | `305,000.00` |
| `Live` | `Long` | `0.0461` | 14,700,000.00 USD | 0.00 USD | 5,520.00 USD | `-39.50%` | `119,796.00` |
| `Live` | `Long` | `0.0461` | 14,690,000.00 USD | 0.00 USD | 114.36 USD | `-39.36%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 14,690,000.00 USD | 0.00 USD | 362.87 USD | `-39.10%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,690,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.97%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,680,000.00 USD | 0.00 USD | 2,580.00 USD | `-38.84%` | `55,490.00` |
| `Live` | `Long` | `0.0466` | 14,670,000.00 USD | 0.00 USD | 109.49 USD | `-38.71%` | `2,347.00` |
| `Live` | `Long` | `0.0473` | 14,670,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.92%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 14,670,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.79%` | `29,884.00` |
| `Live` | `Long` | `0.0481` | 14,670,000.00 USD | 0.00 USD | 58,890.00 USD | `-36.74%` | `1,223,127.00` |
| `Live` | `Long` | `0.0483` | 14,610,000.00 USD | 0.00 USD | 1,780.00 USD | `-36.47%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,610,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.34%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,610,000.00 USD | 0.00 USD | 4,370.00 USD | `-36.21%` | `90,000.00` |
| `Live` | `Long` | `0.0488` | 14,610,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.82%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,600,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.69%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,600,000.00 USD | 0.00 USD | 4,420.00 USD | `-35.55%` | `90,201.00` |
| `Live` | `Long` | `0.0493` | 14,590,000.00 USD | 0.00 USD | 4,780.00 USD | `-35.29%` | `96,957.00` |
| `Live` | `Long` | `0.0498` | 14,590,000.00 USD | 0.00 USD | 253.82 USD | `-34.63%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,590,000.00 USD | 0.00 USD | 501.50 USD | `-34.24%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,590,000.00 USD | 0.00 USD | 106.23 USD | `-33.98%` | `2,114.00` |
| `Live` | `Long` | `0.0503` | 14,590,000.00 USD | 0.00 USD | 5,310.00 USD | `-33.85%` | `105,458.00` |
| `Live` | `Long` | `0.0505` | 14,580,000.00 USD | 0.00 USD | 334.89 USD | `-33.71%` | `6,638.00` |
| `Live` | `Long` | `0.0505` | 14,580,000.00 USD | 0.00 USD | 252.75 USD | `-33.58%` | `5,000.00` |
| `Live` | `Long` | `0.0507` | 14,580,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.45%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,580,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.32%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,580,000.00 USD | 0.00 USD | 535.43 USD | `-33.06%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,580,000.00 USD | 0.00 USD | 566.65 USD | `-32.93%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,580,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.79%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,560,000.00 USD | 0.00 USD | 1,880.00 USD | `-32.66%` | `36,681.00` |
| `Live` | `Long` | `0.0513` | 14,560,000.00 USD | 0.00 USD | 313.08 USD | `-32.53%` | `6,097.00` |
| `Live` | `Long` | `0.0515` | 14,560,000.00 USD | 0.00 USD | 46,390.00 USD | `-32.27%` | `899,807.00` |
| `Live` | `Long` | `0.0519` | 14,520,000.00 USD | 0.00 USD | 6,570.00 USD | `-31.87%` | `126,763.00` |
| `Live` | `Long` | `0.0520` | 14,510,000.00 USD | 0.00 USD | 277.72 USD | `-31.74%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,510,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.61%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,500,000.00 USD | 0.00 USD | 275,090.00 USD | `-31.35%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,230,000.00 USD | 0.00 USD | 328.50 USD | `-31.22%` | `6,275.00` |
| `Live` | `Long` | `0.0524` | 14,230,000.00 USD | 0.00 USD | 1,170.00 USD | `-31.09%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,230,000.00 USD | 0.00 USD | 4,790.00 USD | `-30.96%` | `91,115.00` |
| `Live` | `Long` | `0.0527` | 14,220,000.00 USD | 0.00 USD | 1,180.00 USD | `-30.82%` | `22,344.00` |
| `Live` | `Long` | `0.0527` | 14,220,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.69%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,220,000.00 USD | 0.00 USD | 673.52 USD | `-30.56%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,220,000.00 USD | 0.00 USD | 205,110.00 USD | `-30.43%` | `3,873,649.00` |
| `Live` | `Long` | `0.0530` | 14,010,000.00 USD | 0.00 USD | 3,050.00 USD | `-30.30%` | `57,404.00` |
| `Live` | `Long` | `0.0532` | 14,010,000.00 USD | 0.00 USD | 10,280.00 USD | `-30.17%` | `193,499.00` |
| `Live` | `Long` | `0.0532` | 14,000,000.00 USD | 0.00 USD | 33,740.00 USD | `-30.04%` | `633,564.00` |
| `Live` | `Long` | `0.0534` | 13,970,000.00 USD | 0.00 USD | 42,580.00 USD | `-29.90%` | `798,082.00` |
| `Live` | `Long` | `0.0534` | 13,920,000.00 USD | 0.00 USD | 800.95 USD | `-29.77%` | `14,985.00` |
| `Live` | `Long` | `0.0536` | 13,920,000.00 USD | 0.00 USD | 1,040.00 USD | `-29.64%` | `19,489.00` |
| `Live` | `Long` | `0.0537` | 13,920,000.00 USD | 0.00 USD | 223.18 USD | `-29.51%` | `4,160.00` |
| `Live` | `Long` | `0.0539` | 13,920,000.00 USD | 0.00 USD | 258.10 USD | `-29.25%` | `4,793.00` |
| `Live` | `Long` | `0.0539` | 13,920,000.00 USD | 0.00 USD | 5,290.00 USD | `-29.12%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,920,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.98%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,910,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.85%` | `75,394.00` |
| `Live` | `Long` | `0.0542` | 13,910,000.00 USD | 0.00 USD | 96,350.00 USD | `-28.72%` | `1,775,957.00` |
| `Live` | `Long` | `0.0544` | 13,810,000.00 USD | 0.00 USD | 903.30 USD | `-28.59%` | `16,620.00` |
| `Live` | `Long` | `0.0546` | 13,810,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.20%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,810,000.00 USD | 0.00 USD | 188.07 USD | `-28.06%` | `3,435.00` |
| `Live` | `Long` | `0.0551` | 13,810,000.00 USD | 0.00 USD | 8,030.00 USD | `-27.54%` | `145,555.00` |
| `Live` | `Long` | `0.0554` | 13,800,000.00 USD | 0.00 USD | 15,580.00 USD | `-27.28%` | `281,570.00` |
| `Live` | `Long` | `0.0556` | 13,790,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.01%` | `19,864.00` |
| `Live` | `Long` | `0.0561` | 13,780,000.00 USD | 0.00 USD | 8,410.00 USD | `-26.36%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 13,780,000.00 USD | 0.00 USD | 144.08 USD | `-26.23%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,780,000.00 USD | 0.00 USD | 40,620.00 USD | `-26.09%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,740,000.00 USD | 0.00 USD | 351.85 USD | `-25.96%` | `6,244.00` |
| `Live` | `Long` | `0.0568` | 13,740,000.00 USD | 0.00 USD | 568.50 USD | `-25.31%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,730,000.00 USD | 0.00 USD | 315.67 USD | `-25.17%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,730,000.00 USD | 0.00 USD | 8,350.00 USD | `-25.04%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,730,000.00 USD | 0.00 USD | 814.04 USD | `-24.91%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,730,000.00 USD | 0.00 USD | 4,060.00 USD | `-24.65%` | `70,727.00` |
| `Live` | `Long` | `0.0575` | 13,720,000.00 USD | 0.00 USD | 478.50 USD | `-24.52%` | `8,329.00` |
| `Live` | `Long` | `0.0575` | 13,720,000.00 USD | 0.00 USD | 3,960.00 USD | `-24.39%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 13,720,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.25%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,710,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.12%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,690,000.00 USD | 0.00 USD | 7,950.00 USD | `-23.99%` | `137,358.00` |
| `Live` | `Long` | `0.0580` | 13,680,000.00 USD | 0.00 USD | 622.09 USD | `-23.86%` | `10,735.00` |
| `Live` | `Long` | `0.0580` | 13,680,000.00 USD | 0.00 USD | 431.14 USD | `-23.73%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,680,000.00 USD | 0.00 USD | 447.17 USD | `-23.60%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,680,000.00 USD | 0.00 USD | 4,300.00 USD | `-23.47%` | `73,773.00` |
| `Live` | `Long` | `0.0583` | 13,680,000.00 USD | 0.00 USD | 16,920.00 USD | `-23.33%` | `289,914.00` |
| `Live` | `Long` | `0.0585` | 13,660,000.00 USD | 0.00 USD | 3,320.00 USD | `-23.20%` | `56,811.00` |
| `Live` | `Long` | `0.0585` | 13,660,000.00 USD | 0.00 USD | 543.17 USD | `-23.07%` | `9,277.00` |
| `Live` | `Long` | `0.0587` | 13,660,000.00 USD | 0.00 USD | 305.15 USD | `-22.81%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,660,000.00 USD | 0.00 USD | 212.22 USD | `-22.55%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,660,000.00 USD | 0.00 USD | 26,980.00 USD | `-22.28%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,630,000.00 USD | 0.00 USD | 546.26 USD | `-22.02%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,630,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.89%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,630,000.00 USD | 0.00 USD | 3,940.00 USD | `-21.76%` | `66,174.00` |
| `Live` | `Long` | `0.0597` | 13,620,000.00 USD | 0.00 USD | 1,610.00 USD | `-21.63%` | `27,029.00` |
| `Live` | `Long` | `0.0599` | 13,620,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.36%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,620,000.00 USD | 0.00 USD | 3,580.00 USD | `-21.23%` | `59,709.00` |
| `Live` | `Long` | `0.0600` | 13,610,000.00 USD | 0.00 USD | 7,210.00 USD | `-21.10%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,610,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.97%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 13,600,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-20.71%` | `98,707,875.00` |
| `Live` | `Long` | `0.0605` | 7,640,000.00 USD | 0.00 USD | 32,090.00 USD | `-20.44%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,610,000.00 USD | 0.00 USD | 622.63 USD | `-20.31%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 7,610,000.00 USD | 0.00 USD | 825.71 USD | `-20.18%` | `13,592.00` |
| `Live` | `Long` | `0.0609` | 7,610,000.00 USD | 0.00 USD | 1,940.00 USD | `-20.05%` | `31,875.00` |
| `Live` | `Long` | `0.0609` | 7,610,000.00 USD | 0.00 USD | 5,110.00 USD | `-19.92%` | `83,914.00` |
| `Live` | `Long` | `0.0612` | 7,600,000.00 USD | 0.00 USD | 629.72 USD | `-19.66%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,600,000.00 USD | 0.00 USD | 298.17 USD | `-19.52%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,600,000.00 USD | 0.00 USD | 655.16 USD | `-19.39%` | `10,679.00` |
| `Live` | `Long` | `0.0614` | 7,600,000.00 USD | 0.00 USD | 1,440.00 USD | `-19.26%` | `23,446.00` |
| `Live` | `Long` | `0.0616` | 7,600,000.00 USD | 0.00 USD | 1,890.00 USD | `-19.13%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,600,000.00 USD | 0.00 USD | 11,100.00 USD | `-19.00%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 7,580,000.00 USD | 0.00 USD | 158.08 USD | `-18.87%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,580,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.47%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,560,000.00 USD | 0.00 USD | 345.86 USD | `-18.34%` | `5,565.00` |
| `Live` | `Long` | `0.0624` | 7,560,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.08%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,560,000.00 USD | 0.00 USD | 43,800.00 USD | `-17.95%` | `701,306.00` |
| `Live` | `Long` | `0.0625` | 7,510,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-17.82%` | `23,518,235.00` |
| `Live` | `Long` | `0.0626` | 6,040,000.00 USD | 0.00 USD | 1,120.00 USD | `-17.68%` | `17,888.00` |
| `Live` | `Long` | `0.0628` | 6,040,000.00 USD | 0.00 USD | 461.78 USD | `-17.55%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,040,000.00 USD | 0.00 USD | 6,400.00 USD | `-17.42%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,030,000.00 USD | 0.00 USD | 2,430.00 USD | `-17.16%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,030,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-17.03%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.90%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.77%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.63%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-16.50%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 633.38 USD | `-16.37%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 4,950,000.00 USD | 0.00 USD | 9,740.00 USD | `-16.24%` | `152,837.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 25,600.00 USD | `-16.11%` | `400,960.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.98%` | `31,194.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 3,420.00 USD | `-15.71%` | `53,255.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 733.80 USD | `-15.58%` | `11,421.00` |
| `Live` | `Long` | `0.0644` | 4,910,000.00 USD | 0.00 USD | 75,530.00 USD | `-15.45%` | `1,173,665.00` |
| `Live` | `Long` | `0.0644` | 4,830,000.00 USD | 0.00 USD | 27,840.00 USD | `-15.32%` | `432,001.00` |
| `Live` | `Long` | `0.0645` | 4,800,000.00 USD | 0.00 USD | 631.94 USD | `-15.19%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,800,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.93%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.79%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,630,000.00 USD | 0.00 USD | 367.23 USD | `-14.66%` | `5,654.00` |
| `Live` | `Long` | `0.0650` | 4,630,000.00 USD | 0.00 USD | 21,580.00 USD | `-14.53%` | `331,693.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.40%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,610,000.00 USD | 0.00 USD | 13,770.00 USD | `-14.27%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,590,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.87%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,580,000.00 USD | 0.00 USD | 14,160.00 USD | `-13.74%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,570,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.61%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,500,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.48%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.35%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-13.09%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,480,000.00 USD | 0.00 USD | 13,740.00 USD | `-12.95%` | `207,423.00` |
| `Live` | `Long` | `0.0664` | 4,460,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.82%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.69%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,440,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.43%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 8,880.00 USD | `-12.30%` | `133,009.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-12.17%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,250,000.00 USD | 0.00 USD | 1,180.00 USD | `-12.04%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,250,000.00 USD | 0.00 USD | 6,120.00 USD | `-11.90%` | `91,206.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.64%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 4,830.00 USD | `-11.51%` | `71,711.00` |
| `Live` | `Long` | `0.0674` | 3,230,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.38%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,230,000.00 USD | 0.00 USD | 112,780.00 USD | `-11.25%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,120,000.00 USD | 0.00 USD | 12,610.00 USD | `-11.12%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,110,000.00 USD | 0.00 USD | 38,220.00 USD | `-10.98%` | `564,100.00` |
| `Live` | `Long` | `0.0678` | 3,070,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.85%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,030,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.72%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,020,000.00 USD | 0.00 USD | 390.81 USD | `-10.59%` | `5,743.00` |
| `Live` | `Long` | `0.0682` | 3,020,000.00 USD | 0.00 USD | 49,360.00 USD | `-10.46%` | `724,293.00` |
| `Live` | `Long` | `0.0683` | 2,970,000.00 USD | 0.00 USD | 6,340.00 USD | `-10.33%` | `92,831.00` |
| `Live` | `Long` | `0.0683` | 2,960,000.00 USD | 0.00 USD | 6,390.00 USD | `-10.20%` | `93,467.00` |
| `Live` | `Long` | `0.0684` | 2,950,000.00 USD | 0.00 USD | 79,490.00 USD | `-10.06%` | `1,161,220.00` |
| `Live` | `Long` | `0.0685` | 2,870,000.00 USD | 0.00 USD | 8,890.00 USD | `-9.93%` | `129,646.00` |
| `Live` | `Long` | `0.0687` | 2,870,000.00 USD | 0.00 USD | 4,840.00 USD | `-9.80%` | `70,447.00` |
| `Live` | `Long` | `0.0688` | 2,860,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.67%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,850,000.00 USD | 0.00 USD | 345.83 USD | `-9.54%` | `5,023.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.41%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,340,000.00 USD | 0.00 USD | 6,960.00 USD | `-9.28%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,330,000.00 USD | 0.00 USD | 13,510.00 USD | `-9.14%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,320,000.00 USD | 0.00 USD | 9,140.00 USD | `-9.01%` | `131,951.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.88%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,310,000.00 USD | 0.00 USD | 5,650.00 USD | `-8.75%` | `81,317.00` |
| `Live` | `Long` | `0.0697` | 2,300,000.00 USD | 0.00 USD | 4,950.00 USD | `-8.49%` | `71,115.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 6,970.00 USD | `-8.36%` | `99,923.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 2,910.00 USD | `-8.22%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,280,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.09%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,280,000.00 USD | 0.00 USD | 9,620.00 USD | `-7.96%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,270,000.00 USD | 0.00 USD | 8,180.00 USD | `-7.83%` | `116,620.00` |
| `Live` | `Long` | `0.0703` | 2,270,000.00 USD | 0.00 USD | 1,070.00 USD | `-7.70%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 3,790.00 USD | `-7.57%` | `53,920.00` |
| `Live` | `Long` | `0.0704` | 2,260,000.00 USD | 0.00 USD | 1,260.00 USD | `-7.44%` | `17,910.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 608.86 USD | `-7.17%` | `8,618.00` |
| `Live` | `Long` | `0.0707` | 2,260,000.00 USD | 0.00 USD | 94,410.00 USD | `-7.04%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,160,000.00 USD | 0.00 USD | 351.63 USD | `-6.78%` | `4,956.00` |
| `Live` | `Long` | `0.0711` | 2,160,000.00 USD | 0.00 USD | 4,720.00 USD | `-6.65%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 1,700.00 USD | `-6.52%` | `23,908.00` |
| `Live` | `Long` | `0.0712` | 2,160,000.00 USD | 0.00 USD | 1,740.00 USD | `-6.39%` | `24,442.00` |
| `Live` | `Long` | `0.0713` | 2,160,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.25%` | `24,494,524.00` |
| `Live` | `Long` | `0.0714` | 408,480.00 USD | 0.00 USD | 13,270.00 USD | `-6.12%` | `185,735.00` |
| `Live` | `Long` | `0.0716` | 395,210.00 USD | 0.00 USD | 8,120.00 USD | `-5.99%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 387,090.00 USD | 0.00 USD | 4,540.00 USD | `-5.86%` | `63,429.00` |
| `Live` | `Long` | `0.0717` | 382,550.00 USD | 0.00 USD | 48,110.00 USD | `-5.73%` | `670,525.00` |
| `Live` | `Long` | `0.0718` | 334,440.00 USD | 0.00 USD | 960.13 USD | `-5.60%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 333,480.00 USD | 0.00 USD | 1,900.00 USD | `-5.47%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 331,580.00 USD | 0.00 USD | 5,090.00 USD | `-5.33%` | `70,701.00` |
| `Live` | `Long` | `0.0722` | 326,490.00 USD | 0.00 USD | 613.35 USD | `-5.20%` | `8,501.00` |
| `Live` | `Long` | `0.0722` | 325,870.00 USD | 0.00 USD | 38,130.00 USD | `-5.07%` | `527,683.00` |
| `Live` | `Long` | `0.0723` | 287,750.00 USD | 0.00 USD | 286,760.00 USD | `-4.94%` | `3,963,544.00` |
| `Live` | `Long` | `0.0725` | 984.89 USD | 0.00 USD | 984.89 USD | `-4.81%` | `13,594.00` |
| `Live` | `Short` | `0.0775` | 240.95 USD | 240.95 USD | 0.00 USD | `+1.89%` | `3,107.00` |
| `Live` | `Short` | `0.0788` | 354.19 USD | 113.24 USD | 0.00 USD | `+3.47%` | `1,438.00` |
| `Live` | `Short` | `0.0789` | 2,780.00 USD | 2,430.00 USD | 0.00 USD | `+3.60%` | `30,807.00` |
| `Live` | `Short` | `0.0790` | 8,490.00 USD | 5,710.00 USD | 0.00 USD | `+3.86%` | `72,197.00` |
| `Live` | `Short` | `0.0791` | 10,140.00 USD | 1,650.00 USD | 0.00 USD | `+3.99%` | `20,832.00` |
| `Live` | `Short` | `0.0794` | 13,690.00 USD | 3,550.00 USD | 0.00 USD | `+4.26%` | `44,701.00` |
| `Live` | `Short` | `0.0795` | 19,590.00 USD | 5,910.00 USD | 0.00 USD | `+4.39%` | `74,367.00` |
| `Live` | `Short` | `0.0804` | 19,810.00 USD | 213.09 USD | 0.00 USD | `+5.57%` | `2,652.00` |
| `Live` | `Short` | `0.0804` | 20,630.00 USD | 826.14 USD | 0.00 USD | `+5.70%` | `10,269.00` |
| `Live` | `Short` | `0.0806` | 20,850.00 USD | 213.40 USD | 0.00 USD | `+5.97%` | `2,646.00` |
| `Live` | `Short` | `0.0808` | 21,060.00 USD | 214.31 USD | 0.00 USD | `+6.10%` | `2,654.00` |
| `Live` | `Short` | `0.0811` | 21,280.00 USD | 215.29 USD | 0.00 USD | `+6.62%` | `2,653.00` |
| `Live` | `Short` | `0.0814` | 21,490.00 USD | 216.17 USD | 0.00 USD | `+7.02%` | `2,654.00` |
| `Live` | `Short` | `0.0818` | 22,090.00 USD | 595.63 USD | 0.00 USD | `+7.41%` | `7,286.00` |
| `Live` | `Short` | `0.0819` | 22,470.00 USD | 380.85 USD | 0.00 USD | `+7.54%` | `4,653.00` |
| `Live` | `Short` | `0.0824` | 22,590.00 USD | 120.38 USD | 0.00 USD | `+8.33%` | `1,460.00` |
| `Live` | `Short` | `0.0825` | 22,810.00 USD | 217.85 USD | 0.00 USD | `+8.46%` | `2,639.00` |
| `Live` | `Short` | `0.0828` | 23,030.00 USD | 218.81 USD | 0.00 USD | `+8.86%` | `2,641.00` |
| `Live` | `Short` | `0.0829` | 23,250.00 USD | 220.48 USD | 0.00 USD | `+8.99%` | `2,658.00` |
| `Live` | `Short` | `0.0832` | 26,700.00 USD | 3,450.00 USD | 0.00 USD | `+9.25%` | `41,543.00` |
| `Live` | `Short` | `0.0837` | 26,990.00 USD | 293.44 USD | 0.00 USD | `+9.91%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 28,570.00 USD | 1,570.00 USD | 0.00 USD | `+10.04%` | `18,767.00` |
| `Live` | `Short` | `0.0838` | 28,790.00 USD | 221.45 USD | 0.00 USD | `+10.17%` | `2,641.00` |
| `Live` | `Short` | `0.0839` | 29,010.00 USD | 221.54 USD | 0.00 USD | `+10.30%` | `2,639.00` |
| `Live` | `Short` | `0.0843` | 29,270.00 USD | 264.21 USD | 0.00 USD | `+10.70%` | `3,136.00` |
| `Live` | `Short` | `0.0847` | 29,500.00 USD | 223.39 USD | 0.00 USD | `+11.22%` | `2,639.00` |
| `Live` | `Short` | `0.0848` | 29,920.00 USD | 426.71 USD | 0.00 USD | `+11.48%` | `5,029.00` |
| `Live` | `Short` | `0.0853` | 30,150.00 USD | 224.97 USD | 0.00 USD | `+12.01%` | `2,639.00` |
| `Live` | `Short` | `0.0854` | 31,180.00 USD | 1,030.00 USD | 0.00 USD | `+12.27%` | `12,089.00` |
| `Live` | `Short` | `0.0858` | 31,300.00 USD | 115.30 USD | 0.00 USD | `+12.80%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 35,540.00 USD | 4,250.00 USD | 0.00 USD | `+12.93%` | `49,397.00` |
| `Live` | `Short` | `0.0864` | 36,380.00 USD | 841.68 USD | 0.00 USD | `+13.59%` | `9,736.00` |
| `Live` | `Short` | `0.0868` | 36,540.00 USD | 155.98 USD | 0.00 USD | `+14.11%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 36,680.00 USD | 138.58 USD | 0.00 USD | `+14.37%` | `1,592.00` |
| `Live` | `Short` | `0.0877` | 36,910.00 USD | 231.57 USD | 0.00 USD | `+15.29%` | `2,639.00` |
| `Live` | `Short` | `0.0881` | 37,380.00 USD | 465.17 USD | 0.00 USD | `+15.69%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 37,790.00 USD | 411.53 USD | 0.00 USD | `+16.61%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 38,210.00 USD | 418.80 USD | 0.00 USD | `+17.00%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 38,490.00 USD | 285.70 USD | 0.00 USD | `+17.53%` | `3,194.00` |
| `Live` | `Short` | `0.0901` | 38,730.00 USD | 237.64 USD | 0.00 USD | `+18.32%` | `2,639.00` |
| `Live` | `Short` | `0.0902` | 41,460.00 USD | 2,740.00 USD | 0.00 USD | `+18.58%` | `30,308.00` |
| `Live` | `Short` | `0.0905` | 48,230.00 USD | 6,760.00 USD | 0.00 USD | `+18.84%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 49,540.00 USD | 1,310.00 USD | 0.00 USD | `+19.10%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 54,480.00 USD | 4,940.00 USD | 0.00 USD | `+19.76%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 54,650.00 USD | 171.49 USD | 0.00 USD | `+20.94%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 55,450.00 USD | 805.37 USD | 0.00 USD | `+22.39%` | `8,646.00` |
| `Live` | `Short` | `0.0944` | 95,160.00 USD | 39,700.00 USD | 0.00 USD | `+23.97%` | `420,808.00` |
| `Live` | `Short` | `0.0945` | 142,380.00 USD | 47,230.00 USD | 0.00 USD | `+24.10%` | `500,000.00` |
| `Live` | `Short` | `0.0948` | 146,650.00 USD | 4,260.00 USD | 0.00 USD | `+24.49%` | `45,000.00` |
| `Live` | `Short` | `0.0950` | 171,110.00 USD | 24,460.00 USD | 0.00 USD | `+24.75%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 171,870.00 USD | 761.26 USD | 0.00 USD | `+24.89%` | `8,009.00` |
| `Live` | `Short` | `0.0954` | 172,070.00 USD | 194.04 USD | 0.00 USD | `+25.28%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 172,670.00 USD | 609.59 USD | 0.00 USD | `+26.33%` | `6,340.00` |
| `Live` | `Short` | `0.0970` | 173,040.00 USD | 365.68 USD | 0.00 USD | `+27.51%` | `3,768.00` |
| `Live` | `Short` | `0.0974` | 173,160.00 USD | 121.23 USD | 0.00 USD | `+28.04%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 173,640.00 USD | 477.50 USD | 0.00 USD | `+29.09%` | `4,860.00` |
| `Live` | `Short` | `0.1003` | 173,840.00 USD | 202.21 USD | 0.00 USD | `+31.85%` | `2,015.00` |
| `Live` | `Short` | `0.1014` | 181,470.00 USD | 7,630.00 USD | 0.00 USD | `+33.29%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 184,440.00 USD | 2,970.00 USD | 0.00 USD | `+33.56%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 184,930.00 USD | 492.85 USD | 0.00 USD | `+33.82%` | `4,839.00` |
| `Live` | `Short` | `0.1041` | 188,160.00 USD | 3,230.00 USD | 0.00 USD | `+36.71%` | `31,000.00` |
| `Live` | `Short` | `0.1061` | 194,260.00 USD | 6,110.00 USD | 0.00 USD | `+39.47%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 194,880.00 USD | 616.19 USD | 0.00 USD | `+41.44%` | `5,724.00` |
| `Live` | `Short` | `0.1084` | 196,740.00 USD | 1,860.00 USD | 0.00 USD | `+42.36%` | `17,184.00` |
| `Live` | `Short` | `0.1085` | 199,980.00 USD | 3,240.00 USD | 0.00 USD | `+42.62%` | `29,849.00` |
| `Live` | `Short` | `0.1127` | 200,200.00 USD | 214.15 USD | 0.00 USD | `+48.01%` | `1,901.00` |
| `Live` | `Short` | `0.1137` | 200,340.00 USD | 147.86 USD | 0.00 USD | `+49.32%` | `1,301.00` |
| `Live` | `Short` | `0.1152` | 200,490.00 USD | 147.05 USD | 0.00 USD | `+51.29%` | `1,277.00` |
| `Live` | `Short` | `0.1197` | 201,360.00 USD | 863.75 USD | 0.00 USD | `+57.21%` | `7,219.00` |
| `Live` | `Short` | `0.1222` | 201,990.00 USD | 637.53 USD | 0.00 USD | `+60.62%` | `5,215.00` |
| `Live` | `Short` | `0.1239` | 202,110.00 USD | 119.52 USD | 0.00 USD | `+62.73%` | `965.00` |
| `Live` | `Short` | `0.1270` | 202,220.00 USD | 108.80 USD | 0.00 USD | `+66.80%` | `857.00` |
| `Live` | `Short` | `0.1281` | 207,950.00 USD | 5,730.00 USD | 0.00 USD | `+68.37%` | `44,734.00` |
| `Live` | `Short` | `0.1288` | 223,150.00 USD | 15,200.00 USD | 0.00 USD | `+69.29%` | `117,965.00` |
| `Live` | `Short` | `0.1296` | 223,330.00 USD | 171.66 USD | 0.00 USD | `+70.35%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 225,460.00 USD | 2,140.00 USD | 0.00 USD | `+72.32%` | `16,310.00` |
| `Live` | `Short` | `0.1313` | 270,420.00 USD | 44,950.00 USD | 0.00 USD | `+72.58%` | `342,231.00` |
| `Live` | `Short` | `0.1318` | 270,520.00 USD | 102.97 USD | 0.00 USD | `+73.24%` | `781.00` |
| `Live` | `Short` | `0.1338` | 270,730.00 USD | 205.31 USD | 0.00 USD | `+75.73%` | `1,535.00` |
| `Live` | `Short` | `0.1354` | 270,860.00 USD | 134.64 USD | 0.00 USD | `+77.97%` | `994.00` |
| `Live` | `Short` | `0.1376` | 272,020.00 USD | 1,160.00 USD | 0.00 USD | `+80.86%` | `8,437.00` |
| `Live` | `Short` | `0.1386` | 273,230.00 USD | 1,210.00 USD | 0.00 USD | `+82.04%` | `8,712.00` |
| `Live` | `Short` | `0.1401` | 295,940.00 USD | 22,710.00 USD | 0.00 USD | `+84.01%` | `162,180.00` |
| `Live` | `Short` | `0.1404` | 296,600.00 USD | 663.63 USD | 0.00 USD | `+84.54%` | `4,725.00` |
| `Live` | `Short` | `0.1421` | 328,060.00 USD | 31,460.00 USD | 0.00 USD | `+86.77%` | `221,300.00` |
| `Live` | `Short` | `0.1426` | 329,870.00 USD | 1,800.00 USD | 0.00 USD | `+87.29%` | `12,652.00` |
| `Live` | `Short` | `0.1432` | 331,730.00 USD | 1,860.00 USD | 0.00 USD | `+88.21%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 331,930.00 USD | 196.63 USD | 0.00 USD | `+89.27%` | `1,365.00` |
| `Live` | `Short` | `0.1442` | 345,700.00 USD | 13,770.00 USD | 0.00 USD | `+89.40%` | `95,545.00` |
| `Live` | `Short` | `0.1444` | 347,240.00 USD | 1,540.00 USD | 0.00 USD | `+89.66%` | `10,691.00` |
| `Live` | `Short` | `0.1446` | 347,390.00 USD | 144.55 USD | 0.00 USD | `+89.92%` | `1,000.00` |
| `Live` | `Short` | `0.1447` | 349,210.00 USD | 1,830.00 USD | 0.00 USD | `+90.19%` | `12,616.00` |
| `Live` | `Short` | `0.1457` | 351,140.00 USD | 1,930.00 USD | 0.00 USD | `+91.50%` | `13,240.00` |
| `Live` | `Short` | `0.1479` | 359,230.00 USD | 8,090.00 USD | 0.00 USD | `+94.26%` | `54,718.00` |
| `Live` | `Short` | `0.1482` | 3,450,000.00 USD | 3,090,000.00 USD | 0.00 USD | `+94.65%` | `20,845,267.00` |
| `Live` | `Short` | `0.1495` | 3,450,000.00 USD | 448.65 USD | 0.00 USD | `+96.49%` | `3,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 786,830.00 USD | 0.00 USD | 375.42 USD | `-66.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 786,450.00 USD | 0.00 USD | 409.59 USD | `-47.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 786,040.00 USD | 0.00 USD | 132.68 USD | `-46.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 785,910.00 USD | 0.00 USD | 788.27 USD | `-45.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 785,120.00 USD | 0.00 USD | 527.05 USD | `-45.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 784,590.00 USD | 0.00 USD | 286.87 USD | `-40.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 784,310.00 USD | 0.00 USD | 252.42 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 784,060.00 USD | 0.00 USD | 468.67 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 783,590.00 USD | 0.00 USD | 5,160.00 USD | `-35.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 778,430.00 USD | 0.00 USD | 920.48 USD | `-35.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 777,510.00 USD | 0.00 USD | 236.01 USD | `-34.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 777,270.00 USD | 0.00 USD | 175.41 USD | `-32.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 777,100.00 USD | 0.00 USD | 242.96 USD | `-32.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 776,850.00 USD | 0.00 USD | 2,670.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 774,180.00 USD | 0.00 USD | 1,370.00 USD | `-27.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 772,810.00 USD | 0.00 USD | 437.58 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0578` | 772,370.00 USD | 0.00 USD | 945.31 USD | `-24.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 771,420.00 USD | 0.00 USD | 183.30 USD | `-23.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 771,240.00 USD | 0.00 USD | 752.54 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 770,490.00 USD | 0.00 USD | 1,020.00 USD | `-22.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 769,470.00 USD | 0.00 USD | 668.84 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 768,800.00 USD | 0.00 USD | 273.90 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 768,530.00 USD | 0.00 USD | 8,800.00 USD | `-20.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 759,730.00 USD | 0.00 USD | 838.79 USD | `-20.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 758,890.00 USD | 0.00 USD | 218.94 USD | `-20.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 758,670.00 USD | 0.00 USD | 504.26 USD | `-18.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 758,170.00 USD | 0.00 USD | 2,280.00 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 755,890.00 USD | 0.00 USD | 118.27 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 755,770.00 USD | 0.00 USD | 1,280.00 USD | `-18.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 754,490.00 USD | 0.00 USD | 1,820.00 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 752,670.00 USD | 0.00 USD | 1,340.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 751,330.00 USD | 0.00 USD | 386.70 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 750,950.00 USD | 0.00 USD | 644.50 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 750,300.00 USD | 0.00 USD | 11,270.00 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 739,030.00 USD | 0.00 USD | 362.24 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 738,670.00 USD | 0.00 USD | 3,140.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 735,530.00 USD | 0.00 USD | 1,100.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 734,430.00 USD | 0.00 USD | 1,200.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 733,240.00 USD | 0.00 USD | 996.31 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 732,240.00 USD | 0.00 USD | 909.85 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 731,330.00 USD | 0.00 USD | 115.57 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 731,210.00 USD | 0.00 USD | 33,620.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 697,590.00 USD | 0.00 USD | 12,860.00 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 684,730.00 USD | 0.00 USD | 1,540.00 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 683,190.00 USD | 0.00 USD | 108.08 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 683,080.00 USD | 0.00 USD | 19,540.00 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 663,540.00 USD | 0.00 USD | 1,430.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 662,100.00 USD | 0.00 USD | 8,540.00 USD | `-10.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 653,570.00 USD | 0.00 USD | 8,580.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 644,990.00 USD | 0.00 USD | 4,970.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 640,020.00 USD | 0.00 USD | 3,100.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 636,930.00 USD | 0.00 USD | 160.31 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 636,770.00 USD | 0.00 USD | 38,710.00 USD | `-9.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 598,060.00 USD | 0.00 USD | 19,520.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 578,540.00 USD | 0.00 USD | 3,190.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 575,350.00 USD | 0.00 USD | 478.66 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 574,870.00 USD | 0.00 USD | 176.08 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 574,690.00 USD | 0.00 USD | 142.09 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 574,550.00 USD | 0.00 USD | 925.29 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 573,630.00 USD | 0.00 USD | 797.80 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 572,830.00 USD | 0.00 USD | 71,220.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 501,610.00 USD | 0.00 USD | 141.77 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 501,460.00 USD | 0.00 USD | 895.27 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 500,570.00 USD | 0.00 USD | 523.23 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 500,050.00 USD | 0.00 USD | 468.88 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 499,580.00 USD | 0.00 USD | 235.12 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 499,340.00 USD | 0.00 USD | 1,090.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 498,260.00 USD | 0.00 USD | 71,660.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0711` | 426,590.00 USD | 0.00 USD | 729.61 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 425,860.00 USD | 0.00 USD | 355.75 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 425,510.00 USD | 0.00 USD | 20,180.00 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 405,330.00 USD | 0.00 USD | 608.76 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 404,720.00 USD | 0.00 USD | 16,880.00 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 387,840.00 USD | 0.00 USD | 110.12 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 387,730.00 USD | 0.00 USD | 1,670.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 386,060.00 USD | 0.00 USD | 17,760.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 368,300.00 USD | 0.00 USD | 13,210.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 355,090.00 USD | 0.00 USD | 551.98 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 354,530.00 USD | 0.00 USD | 138,380.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 216,150.00 USD | 0.00 USD | 36,100.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 180,050.00 USD | 0.00 USD | 34,460.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 145,590.00 USD | 0.00 USD | 2,030.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 143,560.00 USD | 0.00 USD | 2,340.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 141,220.00 USD | 0.00 USD | 383.97 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 140,840.00 USD | 0.00 USD | 2,540.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 138,300.00 USD | 0.00 USD | 4,030.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 134,260.00 USD | 0.00 USD | 386.09 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 133,880.00 USD | 0.00 USD | 1,950.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 131,930.00 USD | 0.00 USD | 1,720.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 130,210.00 USD | 0.00 USD | 227.92 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 129,980.00 USD | 0.00 USD | 397.76 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 129,580.00 USD | 0.00 USD | 398.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 129,180.00 USD | 0.00 USD | 797.39 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 128,390.00 USD | 0.00 USD | 59,820.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 68,560.00 USD | 0.00 USD | 1,640.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 66,920.00 USD | 0.00 USD | 189.57 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 66,730.00 USD | 0.00 USD | 1,480.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 65,250.00 USD | 0.00 USD | 334.27 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 64,920.00 USD | 0.00 USD | 415.62 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 64,500.00 USD | 0.00 USD | 16,520.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 47,990.00 USD | 0.00 USD | 3,170.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 44,810.00 USD | 0.00 USD | 7,460.00 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 37,350.00 USD | 0.00 USD | 391.32 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 36,960.00 USD | 0.00 USD | 198.95 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 36,760.00 USD | 0.00 USD | 1,490.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 35,260.00 USD | 0.00 USD | 398.52 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 34,870.00 USD | 0.00 USD | 19,650.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 15,210.00 USD | 0.00 USD | 198.96 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 15,010.00 USD | 0.00 USD | 1,700.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 13,310.00 USD | 0.00 USD | 151.35 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 13,160.00 USD | 0.00 USD | 7,490.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 5,670.00 USD | 0.00 USD | 150.85 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 5,520.00 USD | 0.00 USD | 1,210.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 4,300.00 USD | 0.00 USD | 504.10 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 3,800.00 USD | 0.00 USD | 398.13 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 3,400.00 USD | 0.00 USD | 3,400.00 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 2,840.00 USD | 814.81 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 6,610.00 USD | 3,770.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 6,720.00 USD | 109.63 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 7,970.00 USD | 1,250.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 8,150.00 USD | 183.50 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 8,760.00 USD | 608.32 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 9,970.00 USD | 1,210.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 10,790.00 USD | 816.05 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 11,910.00 USD | 1,120.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 14,530.00 USD | 2,620.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 14,970.00 USD | 444.42 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 18,910.00 USD | 3,930.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 19,310.00 USD | 407.23 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 19,630.00 USD | 321.13 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 20,040.00 USD | 409.84 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 22,290.00 USD | 2,240.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 22,620.00 USD | 329.23 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 22,770.00 USD | 155.43 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 23,600.00 USD | 823.90 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 26,520.00 USD | 2,920.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 27,490.00 USD | 975.23 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 27,910.00 USD | 413.84 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,070.00 USD | 157.14 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 28,200.00 USD | 130.71 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 70,160.00 USD | 41,960.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 70,300.00 USD | 141.44 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 71,070.00 USD | 773.68 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 71,760.00 USD | 687.81 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 77,180.00 USD | 5,420.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 78,000.00 USD | 812.79 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 83,370.00 USD | 5,370.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 92,380.00 USD | 9,020.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 92,700.00 USD | 312.56 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 93,150.00 USD | 455.34 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 93,280.00 USD | 125.45 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 93,510.00 USD | 230.40 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 93,830.00 USD | 319.16 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 94,840.00 USD | 1,010.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 117,580.00 USD | 22,750.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 117,990.00 USD | 400.91 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 118,190.00 USD | 200.46 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 118,440.00 USD | 259.13 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 121,650.00 USD | 3,200.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 130,650.00 USD | 9,010.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 227,430.00 USD | 96,780.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 228,240.00 USD | 807.50 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 228,500.00 USD | 257.18 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 228,920.00 USD | 424.74 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 229,020.00 USD | 101.80 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 230,410.00 USD | 1,380.00 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 232,430.00 USD | 2,030.00 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 233,870.00 USD | 1,430.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 234,000.00 USD | 129.67 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 235,010.00 USD | 1,020.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 235,270.00 USD | 256.05 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 236,300.00 USD | 1,030.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 239,320.00 USD | 3,020.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 239,650.00 USD | 327.80 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 240,100.00 USD | 457.92 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 240,800.00 USD | 691.29 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 241,600.00 USD | 800.79 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 242,110.00 USD | 512.05 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 242,600.00 USD | 495.36 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 242,990.00 USD | 389.31 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 243,150.00 USD | 154.58 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 243,450.00 USD | 303.56 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 243,810.00 USD | 360.58 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 244,190.00 USD | 381.45 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 244,350.00 USD | 155.82 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 288,740.00 USD | 44,390.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 289,040.00 USD | 309.23 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 290,300.00 USD | 1,260.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 291,550.00 USD | 1,240.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0837` | 291,660.00 USD | 109.92 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,040,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,040,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,040,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,040,000.00 USD | 107.71 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,040,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,050,000.00 USD | 529.92 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,050,000.00 USD | 219.07 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,050,000.00 USD | 242.84 USD | 0.00 USD | `+11.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,060,000.00 USD | 10,140.00 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,060,000.00 USD | 876.11 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,060,000.00 USD | 812.54 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,060,000.00 USD | 126.76 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,060,000.00 USD | 307.41 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,060,000.00 USD | 614.09 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,060,000.00 USD | 859.50 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,060,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,110,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,110,000.00 USD | 123.94 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,110,000.00 USD | 271.53 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,110,000.00 USD | 1,660.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,110,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,110,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,110,000.00 USD | 117.71 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,110,000.00 USD | 111.61 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,110,000.00 USD | 571.18 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,110,000.00 USD | 375.94 USD | 0.00 USD | `+15.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,110,000.00 USD | 627.55 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,110,000.00 USD | 211.04 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,110,000.00 USD | 108.36 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,110,000.00 USD | 543.32 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,120,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,120,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,140,000.00 USD | 17,680.00 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,140,000.00 USD | 5,630.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,140,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,140,000.00 USD | 224.86 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,170,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,170,000.00 USD | 114.93 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,170,000.00 USD | 679.12 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,170,000.00 USD | 173.36 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,170,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,170,000.00 USD | 1,580.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,170,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,170,000.00 USD | 541.32 USD | 0.00 USD | `+21.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,310,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,310,000.00 USD | 691.07 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,320,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,330,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,330,000.00 USD | 734.82 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,330,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,330,000.00 USD | 105.00 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,330,000.00 USD | 184.09 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,330,000.00 USD | 1,120.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,340,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,340,000.00 USD | 1,070.00 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,340,000.00 USD | 512.15 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,340,000.00 USD | 6,620.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,340,000.00 USD | 404.96 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,340,000.00 USD | 129.85 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,350,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,350,000.00 USD | 409.17 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,350,000.00 USD | 203.74 USD | 0.00 USD | `+26.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,350,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,350,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,350,000.00 USD | 694.56 USD | 0.00 USD | `+28.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,350,000.00 USD | 940.91 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,360,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,360,000.00 USD | 104.99 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,360,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,380,000.00 USD | 19,950.00 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,380,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,380,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,380,000.00 USD | 438.96 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,380,000.00 USD | 973.76 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,390,000.00 USD | 10,000.00 USD | 0.00 USD | `+31.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,390,000.00 USD | 175.59 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,400,000.00 USD | 2,060.00 USD | 0.00 USD | `+31.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,400,000.00 USD | 482.89 USD | 0.00 USD | `+32.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,400,000.00 USD | 201.90 USD | 0.00 USD | `+32.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,400,000.00 USD | 489.46 USD | 0.00 USD | `+32.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,400,000.00 USD | 103.68 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,400,000.00 USD | 2,590.00 USD | 0.00 USD | `+33.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,400,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,410,000.00 USD | 11,200.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,420,000.00 USD | 4,330.00 USD | 0.00 USD | `+34.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,420,000.00 USD | 205.50 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,420,000.00 USD | 3,490.00 USD | 0.00 USD | `+35.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,420,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,420,000.00 USD | 207.50 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,420,000.00 USD | 813.88 USD | 0.00 USD | `+36.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,450,000.00 USD | 23,160.00 USD | 0.00 USD | `+37.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 209.30 USD | 0.00 USD | `+37.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,450,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,460,000.00 USD | 585.32 USD | 0.00 USD | `+38.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,460,000.00 USD | 210.90 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,460,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,460,000.00 USD | 105.75 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,460,000.00 USD | 3,220.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,460,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,460,000.00 USD | 212.90 USD | 0.00 USD | `+39.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,460,000.00 USD | 472.63 USD | 0.00 USD | `+40.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,460,000.00 USD | 214.50 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,460,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,460,000.00 USD | 136.12 USD | 0.00 USD | `+41.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,460,000.00 USD | 216.10 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,470,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,470,000.00 USD | 217.90 USD | 0.00 USD | `+43.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,470,000.00 USD | 219.70 USD | 0.00 USD | `+44.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,470,000.00 USD | 7,780.00 USD | 0.00 USD | `+44.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,470,000.00 USD | 154.22 USD | 0.00 USD | `+45.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,470,000.00 USD | 221.30 USD | 0.00 USD | `+45.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,480,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,500,000.00 USD | 24,190.00 USD | 0.00 USD | `+45.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,500,000.00 USD | 223.10 USD | 0.00 USD | `+46.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,500,000.00 USD | 224.70 USD | 0.00 USD | `+47.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,500,000.00 USD | 226.30 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 950.34 USD | 0.00 USD | `+49.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,500,000.00 USD | 229.50 USD | 0.00 USD | `+50.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,500,000.00 USD | 771.08 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,500,000.00 USD | 942.95 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,500,000.00 USD | 230.90 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,500,000.00 USD | 619.10 USD | 0.00 USD | `+52.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,510,000.00 USD | 1,250.00 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,510,000.00 USD | 232.30 USD | 0.00 USD | `+52.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,510,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,510,000.00 USD | 3,730.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,510,000.00 USD | 676.22 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,510,000.00 USD | 648.25 USD | 0.00 USD | `+54.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,520,000.00 USD | 1,510.00 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,520,000.00 USD | 448.52 USD | 0.00 USD | `+55.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,520,000.00 USD | 124.58 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,520,000.00 USD | 691.80 USD | 0.00 USD | `+57.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,640,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,640,000.00 USD | 143.22 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,640,000.00 USD | 1,380.00 USD | 0.00 USD | `+59.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,640,000.00 USD | 2,270.00 USD | 0.00 USD | `+60.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,640,000.00 USD | 871.99 USD | 0.00 USD | `+60.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,670,000.00 USD | 29,610.00 USD | 0.00 USD | `+66.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,670,000.00 USD | 400.21 USD | 0.00 USD | `+66.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,670,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,680,000.00 USD | 4,160.00 USD | 0.00 USD | `+78.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,680,000.00 USD | 114.70 USD | 0.00 USD | `+79.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,680,000.00 USD | 278.50 USD | 0.00 USD | `+83.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,680,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,680,000.00 USD | 173.57 USD | 0.00 USD | `+86.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,680,000.00 USD | 380.09 USD | 0.00 USD | `+86.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,700,000.00 USD | 17,150.00 USD | 0.00 USD | `+87.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,700,000.00 USD | 1,440.00 USD | 0.00 USD | `+89.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,700,000.00 USD | 433.35 USD | 0.00 USD | `+89.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,700,000.00 USD | 452.26 USD | 0.00 USD | `+91.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,700,000.00 USD | 3,640.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,760,000.00 USD | 55,720.00 USD | 0.00 USD | `+94.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,760,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,780,000.00 USD | 19,850.00 USD | 0.00 USD | `+97.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,780,000.00 USD | 1,620.00 USD | 0.00 USD | `+98.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1515` | 2,780,000.00 USD | 1,710.00 USD | 0.00 USD | `+98.99%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0657` | 30,770,000.00 USD | 0.00 USD | 30,770,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0661` | 30,750,000.00 USD | 0.00 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD |
| `7D` | `0.0662` | 30,710,000.00 USD | 0.00 USD | 30,710,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.0665` | 30,710,000.00 USD | 0.00 USD | 30,710,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD |
| `7D` | `0.0669` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `0.0674` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 5,520.00 USD | 3,930.00 USD | 0.00 USD |
| `7D` | `0.0675` | 30,510,000.00 USD | 0.00 USD | 30,510,000.00 USD | 19,910.00 USD | 4,530.00 USD | 19,470.00 USD |
| `7D` | `0.0676` | 30,470,000.00 USD | 0.00 USD | 30,470,000.00 USD | 6,810.00 USD | 0.00 USD | 475.18 USD |
| `1D` | `0.0677` | 19,630,000.00 USD | 0.00 USD | 19,630,000.00 USD | 67,140.00 USD | 96,830.00 USD | 32,900.00 USD |
| `7D` | `0.0677` | 30,460,000.00 USD | 0.00 USD | 30,460,000.00 USD | 3,660.00 USD | 9,140.00 USD | 609.05 USD |
| `1D` | `0.0678` | 19,440,000.00 USD | 0.00 USD | 19,440,000.00 USD | 40,890.00 USD | 47,200.00 USD | 80,440.00 USD |
| `7D` | `0.0678` | 30,450,000.00 USD | 0.00 USD | 30,450,000.00 USD | 12,840.00 USD | 51,630.00 USD | 0.00 USD |
| `1D` | `0.0679` | 19,270,000.00 USD | 0.00 USD | 19,270,000.00 USD | 72,650.00 USD | 39,580.00 USD | 8,030.00 USD |
| `7D` | `0.0679` | 30,380,000.00 USD | 0.00 USD | 30,380,000.00 USD | 19,040.00 USD | 8,140.00 USD | 74,820.00 USD |
| `1D` | `0.0680` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 51,680.00 USD | 43,850.00 USD | 41,660.00 USD |
| `7D` | `0.0680` | 30,280,000.00 USD | 0.00 USD | 30,280,000.00 USD | 84,730.00 USD | 47,420.00 USD | 164,800.00 USD |
| `1D` | `0.0681` | 19,010,000.00 USD | 0.00 USD | 19,010,000.00 USD | 51,100.00 USD | 71,350.00 USD | 155,440.00 USD |
| `7D` | `0.0681` | 29,990,000.00 USD | 0.00 USD | 29,990,000.00 USD | 54,210.00 USD | 14,460.00 USD | 0.00 USD |
| `1D` | `0.0682` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 55,450.00 USD | 77,700.00 USD | 32,040.00 USD |
| `7D` | `0.0682` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 0.00 USD | 35,790.00 USD | 66,930.00 USD |
| `1D` | `0.0683` | 18,570,000.00 USD | 0.00 USD | 18,570,000.00 USD | 27,820.00 USD | 32,750.00 USD | 746.81 USD |
| `7D` | `0.0683` | 29,810,000.00 USD | 0.00 USD | 29,810,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD |
| `1D` | `0.0684` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 37,320.00 USD | 33,850.00 USD | 3,120.00 USD |
| `7D` | `0.0684` | 29,790,000.00 USD | 0.00 USD | 29,790,000.00 USD | 111,040.00 USD | 4,760.00 USD | 1,160.00 USD |
| `1D` | `0.0685` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 72,460.00 USD | 14,450.00 USD | 28,630.00 USD |
| `7D` | `0.0685` | 29,670,000.00 USD | 0.00 USD | 29,670,000.00 USD | 31,800.00 USD | 73,160.00 USD | 24,220.00 USD |
| `1D` | `0.0686` | 18,320,000.00 USD | 0.00 USD | 18,320,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,200.00 USD |
| `7D` | `0.0686` | 29,550,000.00 USD | 0.00 USD | 29,550,000.00 USD | 57,320.00 USD | 64,030.00 USD | 388.90 USD |
| `1D` | `0.0687` | 18,230,000.00 USD | 0.00 USD | 18,230,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,070.00 USD |
| `7D` | `0.0687` | 29,420,000.00 USD | 0.00 USD | 29,420,000.00 USD | 44,400.00 USD | 64,060.00 USD | 617.20 USD |
| `1D` | `0.0688` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD |
| `7D` | `0.0688` | 29,310,000.00 USD | 0.00 USD | 29,310,000.00 USD | 40,320.00 USD | 0.00 USD | 60,810.00 USD |
| `1D` | `0.0689` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 10,400.00 USD | 0.00 USD | 1,990.00 USD |
| `7D` | `0.0689` | 29,210,000.00 USD | 0.00 USD | 29,210,000.00 USD | 185,160.00 USD | 77,640.00 USD | 277.73 USD |
| `1D` | `0.0690` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `0.0690` | 28,950,000.00 USD | 0.00 USD | 28,950,000.00 USD | 112,090.00 USD | 64,360.00 USD | 73,160.00 USD |
| `1D` | `0.0691` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0691` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 49,920.00 USD | 30,660.00 USD | 57,750.00 USD |
| `1D` | `0.0692` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 23,110.00 USD | 0.00 USD | 670.09 USD |
| `7D` | `0.0692` | 28,560,000.00 USD | 0.00 USD | 28,560,000.00 USD | 78,440.00 USD | 76,890.00 USD | 41,990.00 USD |
| `1D` | `0.0693` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0693` | 28,360,000.00 USD | 0.00 USD | 28,360,000.00 USD | 128,710.00 USD | 113,280.00 USD | 38,210.00 USD |
| `1D` | `0.0694` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0694` | 28,080,000.00 USD | 0.00 USD | 28,080,000.00 USD | 169,230.00 USD | 67,150.00 USD | 102,450.00 USD |
| `1D` | `0.0695` | 18,000,000.00 USD | 0.00 USD | 18,000,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0695` | 27,750,000.00 USD | 0.00 USD | 27,750,000.00 USD | 113,240.00 USD | 145,370.00 USD | 110,100.00 USD |
| `7D` | `0.0696` | 27,380,000.00 USD | 0.00 USD | 27,380,000.00 USD | 100,230.00 USD | 61,080.00 USD | 186,810.00 USD |
| `1D` | `0.0697` | 18,000,000.00 USD | 0.00 USD | 18,000,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD |
| `7D` | `0.0697` | 27,030,000.00 USD | 0.00 USD | 27,030,000.00 USD | 41,960.00 USD | 87,540.00 USD | 76,690.00 USD |
| `1D` | `0.0698` | 17,940,000.00 USD | 0.00 USD | 17,940,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD |
| `7D` | `0.0698` | 26,820,000.00 USD | 0.00 USD | 26,820,000.00 USD | 127,350.00 USD | 103,870.00 USD | 71,040.00 USD |
| `1D` | `0.0699` | 17,900,000.00 USD | 0.00 USD | 17,900,000.00 USD | 38,680.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.0699` | 26,520,000.00 USD | 0.00 USD | 26,520,000.00 USD | 198,220.00 USD | 101,580.00 USD | 67,180.00 USD |
| `1D` | `0.0700` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,060.00 USD |
| `7D` | `0.0700` | 26,150,000.00 USD | 0.00 USD | 26,150,000.00 USD | 117,390.00 USD | 110,810.00 USD | 86,640.00 USD |
| `1D` | `0.0701` | 17,740,000.00 USD | 0.00 USD | 17,740,000.00 USD | 32,570.00 USD | 108,360.00 USD | 4,760.00 USD |
| `7D` | `0.0701` | 25,840,000.00 USD | 0.00 USD | 25,840,000.00 USD | 166,270.00 USD | 8,980.00 USD | 56,110.00 USD |
| `1D` | `0.0702` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 47,790.00 USD | 0.00 USD | 474.32 USD |
| `7D` | `0.0702` | 25,610,000.00 USD | 0.00 USD | 25,610,000.00 USD | 168,320.00 USD | 97,270.00 USD | 50,390.00 USD |
| `1D` | `0.0703` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 139,990.00 USD | 57,870.00 USD | 4,100.00 USD |
| `7D` | `0.0703` | 25,290,000.00 USD | 0.00 USD | 25,290,000.00 USD | 107,990.00 USD | 23,160.00 USD | 1,240.00 USD |
| `1D` | `0.0704` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 4,460.00 USD | 31,030.00 USD | 347.04 USD |
| `7D` | `0.0704` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 139,040.00 USD | 55,790.00 USD | 17,600.00 USD |
| `1D` | `0.0705` | 17,310,000.00 USD | 0.00 USD | 17,310,000.00 USD | 41,640.00 USD | 30,720.00 USD | 35,100.00 USD |
| `7D` | `0.0705` | 24,950,000.00 USD | 0.00 USD | 24,950,000.00 USD | 85,040.00 USD | 77,390.00 USD | 160,970.00 USD |
| `1D` | `0.0706` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 30,200.00 USD | 1,120.00 USD | 15,560.00 USD |
| `7D` | `0.0706` | 24,620,000.00 USD | 0.00 USD | 24,620,000.00 USD | 25,760.00 USD | 13,870.00 USD | 46,870.00 USD |
| `1D` | `0.0707` | 17,160,000.00 USD | 0.00 USD | 17,160,000.00 USD | 101,610.00 USD | 63,050.00 USD | 23,020.00 USD |
| `7D` | `0.0707` | 24,540,000.00 USD | 0.00 USD | 24,540,000.00 USD | 145,730.00 USD | 23,290.00 USD | 109,250.00 USD |
| `1D` | `0.0708` | 16,970,000.00 USD | 0.00 USD | 16,970,000.00 USD | 62,040.00 USD | 62,000.00 USD | 108,590.00 USD |
| `7D` | `0.0708` | 24,260,000.00 USD | 0.00 USD | 24,260,000.00 USD | 20,200.00 USD | 31,420.00 USD | 51,150.00 USD |
| `1D` | `0.0709` | 16,740,000.00 USD | 0.00 USD | 16,740,000.00 USD | 38,730.00 USD | 82,010.00 USD | 148,890.00 USD |
| `7D` | `0.0709` | 24,160,000.00 USD | 0.00 USD | 24,160,000.00 USD | 465,090.00 USD | 128,300.00 USD | 87,930.00 USD |
| `1D` | `0.0710` | 16,470,000.00 USD | 0.00 USD | 16,470,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,550.00 USD |
| `7D` | `0.0710` | 23,470,000.00 USD | 0.00 USD | 23,470,000.00 USD | 196,450.00 USD | 161,070.00 USD | 62,470.00 USD |
| `1D` | `0.0711` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 49,210.00 USD | 25,670.00 USD | 42,400.00 USD |
| `7D` | `0.0711` | 23,050,000.00 USD | 0.00 USD | 23,050,000.00 USD | 89,280.00 USD | 91,060.00 USD | 28,720.00 USD |
| `1D` | `0.0712` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 165,590.00 USD | 46,690.00 USD | 3,090.00 USD |
| `7D` | `0.0712` | 22,850,000.00 USD | 0.00 USD | 22,850,000.00 USD | 200,920.00 USD | 117,120.00 USD | 72,910.00 USD |
| `1D` | `0.0713` | 15,810,000.00 USD | 0.00 USD | 15,810,000.00 USD | 75,840.00 USD | 85,230.00 USD | 67,120.00 USD |
| `7D` | `0.0713` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 178,680.00 USD | 54,360.00 USD | 67,050.00 USD |
| `1D` | `0.0714` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 123,320.00 USD | 51,930.00 USD | 46,750.00 USD |
| `7D` | `0.0714` | 22,150,000.00 USD | 0.00 USD | 22,150,000.00 USD | 92,880.00 USD | 49,400.00 USD | 38,070.00 USD |
| `1D` | `0.0715` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 81,850.00 USD | 238,460.00 USD | 43,180.00 USD |
| `7D` | `0.0715` | 21,970,000.00 USD | 0.00 USD | 21,970,000.00 USD | 138,920.00 USD | 2,060.00 USD | 29,970.00 USD |
| `1D` | `0.0716` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 19,480.00 USD | 51,080.00 USD | 42.32 USD |
| `7D` | `0.0716` | 21,800,000.00 USD | 0.00 USD | 21,800,000.00 USD | 123,820.00 USD | 189,070.00 USD | 15,490.00 USD |
| `1D` | `0.0717` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 238,310.00 USD | 96,160.00 USD | 615.64 USD |
| `7D` | `0.0717` | 21,470,000.00 USD | 0.00 USD | 21,470,000.00 USD | 156,500.00 USD | 1,810.00 USD | 32,890.00 USD |
| `1D` | `0.0718` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 66,150.00 USD | 101,030.00 USD | 12,930.00 USD |
| `7D` | `0.0718` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 61,410.00 USD | 22,840.00 USD | 47,910.00 USD |
| `1D` | `0.0719` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 239,170.00 USD | 45,330.00 USD | 72,320.00 USD |
| `7D` | `0.0719` | 21,150,000.00 USD | 0.00 USD | 21,150,000.00 USD | 163,670.00 USD | 29,960.00 USD | 228,140.00 USD |
| `1D` | `0.0720` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 141,760.00 USD | 50,600.00 USD | 70,650.00 USD |
| `7D` | `0.0720` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 282,840.00 USD | 169,120.00 USD | 54,740.00 USD |
| `1D` | `0.0721` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 311,990.00 USD | 298,040.00 USD | 69,200.00 USD |
| `7D` | `0.0721` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 139,860.00 USD | 116,340.00 USD | 40,930.00 USD |
| `1D` | `0.0722` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 199,310.00 USD | 130,350.00 USD | 150,440.00 USD |
| `7D` | `0.0722` | 19,930,000.00 USD | 0.00 USD | 19,930,000.00 USD | 54,310.00 USD | 26,930.00 USD | 5,890.00 USD |
| `1D` | `0.0723` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 166,340.00 USD | 283,230.00 USD | 369,710.00 USD |
| `7D` | `0.0723` | 19,840,000.00 USD | 0.00 USD | 19,840,000.00 USD | 204,990.00 USD | 144,790.00 USD | 126,410.00 USD |
| `1D` | `0.0724` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 224,260.00 USD | 256,770.00 USD | 401,950.00 USD |
| `7D` | `0.0724` | 19,360,000.00 USD | 0.00 USD | 19,360,000.00 USD | 1,050,000.00 USD | 84,550.00 USD | 186,070.00 USD |
| `1D` | `0.0725` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 276,150.00 USD | 262,460.00 USD | 311,790.00 USD |
| `7D` | `0.0725` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 174,770.00 USD | 304,550.00 USD | 20,160.00 USD |
| `1D` | `0.0726` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 154,940.00 USD | 148,810.00 USD | 62,150.00 USD |
| `7D` | `0.0726` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 167,610.00 USD | 227,020.00 USD | 91,610.00 USD |
| `1D` | `0.0727` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 229,850.00 USD | 201,110.00 USD | 60,570.00 USD |
| `7D` | `0.0727` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 81,590.00 USD | 205,010.00 USD | 558.98 USD |
| `1D` | `0.0728` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 173,330.00 USD | 202,780.00 USD | 65,620.00 USD |
| `7D` | `0.0728` | 16,770,000.00 USD | 0.00 USD | 16,770,000.00 USD | 34,520.00 USD | 22,770.00 USD | 32,990.00 USD |
| `1D` | `0.0729` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 89,610.00 USD | 41,110.00 USD | 16,850.00 USD |
| `7D` | `0.0729` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 112,700.00 USD | 82,650.00 USD | 4,030.00 USD |
| `1D` | `0.0730` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 156,020.00 USD | 73,580.00 USD | 50,190.00 USD |
| `7D` | `0.0730` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 384,130.00 USD | 25,240.00 USD | 4,280.00 USD |
| `1D` | `0.0731` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 80,020.00 USD | 88,000.00 USD | 28,420.00 USD |
| `7D` | `0.0731` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 181,180.00 USD | 24,050.00 USD | 8,510.00 USD |
| `1D` | `0.0732` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,620.00 USD |
| `7D` | `0.0732` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 344,710.00 USD | 0.00 USD | 1,540.00 USD |
| `1D` | `0.0733` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 64,680.00 USD | 96,060.00 USD | 32,880.00 USD |
| `7D` | `0.0733` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 125,410.00 USD | 0.00 USD | 28,420.00 USD |
| `1D` | `0.0734` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD |
| `7D` | `0.0734` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 183,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0735` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD |
| `7D` | `0.0735` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 406,040.00 USD | 93,670.00 USD | 0.00 USD |
| `1D` | `0.0736` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `7D` | `0.0736` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 272,970.00 USD | 385,750.00 USD | 0.00 USD |
| `1D` | `0.0737` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 145,660.00 USD | 69,370.00 USD | 49,860.00 USD |
| `7D` | `0.0737` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 233,090.00 USD | 153,990.00 USD | 0.00 USD |
| `1D` | `0.0738` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 226,750.00 USD | 73,230.00 USD | 85,530.00 USD |
| `7D` | `0.0738` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 265,850.00 USD | 474,350.00 USD | 40,090.00 USD |
| `1D` | `0.0739` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 294,920.00 USD | 101,560.00 USD | 62,540.00 USD |
| `7D` | `0.0739` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 218,050.00 USD | 40,680.00 USD | 69,010.00 USD |
| `1D` | `0.0740` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 99,850.00 USD | 121,290.00 USD | 117,450.00 USD |
| `7D` | `0.0740` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 101,490.00 USD | 91,130.00 USD | 37,850.00 USD |
| `1D` | `0.0741` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 217,950.00 USD | 184,620.00 USD | 102,820.00 USD |
| `7D` | `0.0741` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 66,970.00 USD | 251,010.00 USD | 178,730.00 USD |
| `1D` | `0.0742` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 155,160.00 USD | 369,400.00 USD | 116,210.00 USD |
| `7D` | `0.0742` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 478,860.00 USD | 163,570.00 USD | 481,020.00 USD |
| `1D` | `0.0743` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 457,820.00 USD | 277,230.00 USD | 319,340.00 USD |
| `7D` | `0.0743` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 295,530.00 USD | 45,530.00 USD | 635,320.00 USD |
| `1D` | `0.0744` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 274,880.00 USD | 118,720.00 USD | 120,490.00 USD |
| `7D` | `0.0744` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 325,550.00 USD | 495,640.00 USD | 129,160.00 USD |
| `1D` | `0.0745` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 153,440.00 USD | 125,290.00 USD | 47,060.00 USD |
| `7D` | `0.0745` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 1,100,000.00 USD | 455,650.00 USD | 196,840.00 USD |
| `1D` | `0.0746` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 160,050.00 USD | 100,590.00 USD | 142,900.00 USD |
| `7D` | `0.0746` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 784,410.00 USD | 925,150.00 USD | 364,110.00 USD |
| `1D` | `0.0747` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,850.00 USD |
| `7D` | `0.0747` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 626,490.00 USD | 907,690.00 USD | 285,310.00 USD |
| `1D` | `0.0748` | 883,930.00 USD | 0.00 USD | 883,930.00 USD | 80,900.00 USD | 109,690.00 USD | 198,860.00 USD |
| `7D` | `0.0748` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 706,340.00 USD | 324,980.00 USD | 181,500.00 USD |
| `1D` | `0.0749` | 494,490.00 USD | 0.00 USD | 494,490.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD |
| `7D` | `0.0749` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 134,940.00 USD | 694,350.00 USD |
| `1D` | `0.0750` | 149,440.00 USD | 0.00 USD | 149,440.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD |
| `7D` | `0.0750` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 84,880.00 USD |
| `1D` | `0.0751` | 85,100.00 USD | 0.00 USD | 85,100.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD |
| `7D` | `0.0751` | 961,320.00 USD | 0.00 USD | 961,320.00 USD | 0.00 USD | 30,900.00 USD | 0.00 USD |
| `1D` | `0.0752` | 37,070.00 USD | 0.00 USD | 37,070.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `7D` | `0.0752` | 930,410.00 USD | 0.00 USD | 930,410.00 USD | 751,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0753` | 12,650.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD |
| `7D` | `0.0753` | 179,300.00 USD | 0.00 USD | 179,300.00 USD | 0.00 USD | 53,860.00 USD | 0.00 USD |
| `7D` | `0.0756` | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD | 125,430.00 USD | 0.00 USD |
| `7D` | `0.0757` | 19,100.00 USD | 19,100.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD |
| `7D` | `0.0757` | 38,200.00 USD | 38,200.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD | 0.00 USD |
| `7D` | `0.0758` | 104,490.00 USD | 104,490.00 USD | 0.00 USD | 0.00 USD | 66,300.00 USD | 0.00 USD |
| `1D` | `0.0759` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0759` | 144,860.00 USD | 144,860.00 USD | 0.00 USD | 40,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0760` | 424.91 USD | 424.91 USD | 0.00 USD | 0.00 USD | 0.00 USD | 424.91 USD |
| `1D` | `0.0761` | 837.25 USD | 837.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | 412.34 USD |
| `1D` | `0.0764` | 15,660.00 USD | 15,660.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD |
| `7D` | `0.0764` | 399,460.00 USD | 399,460.00 USD | 0.00 USD | 0.00 USD | 254,610.00 USD | 0.00 USD |
| `1D` | `0.0765` | 363,970.00 USD | 363,970.00 USD | 0.00 USD | 211,600.00 USD | 37,120.00 USD | 99,590.00 USD |
| `7D` | `0.0765` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 772,480.00 USD | 241,990.00 USD | 0.00 USD |
| `1D` | `0.0766` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 352,420.00 USD | 421,720.00 USD | 0.00 USD |
| `7D` | `0.0766` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 594,350.00 USD | 90,730.00 USD | 0.00 USD |
| `1D` | `0.0767` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 164,440.00 USD | 335,150.00 USD | 159,150.00 USD |
| `7D` | `0.0767` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 587,940.00 USD | 45,720.00 USD | 0.00 USD |
| `1D` | `0.0768` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 352,400.00 USD | 143,560.00 USD | 680,630.00 USD |
| `7D` | `0.0768` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 117,000.00 USD | 7,860.00 USD | 92,730.00 USD |
| `1D` | `0.0769` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 420,080.00 USD | 469,120.00 USD | 325,940.00 USD |
| `7D` | `0.0769` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 861,620.00 USD | 76,450.00 USD | 445,860.00 USD |
| `1D` | `0.0770` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 282,920.00 USD | 275,070.00 USD | 370,450.00 USD |
| `7D` | `0.0770` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 392,100.00 USD | 325,170.00 USD | 291,470.00 USD |
| `1D` | `0.0771` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 368,880.00 USD | 460,320.00 USD | 236,250.00 USD |
| `7D` | `0.0771` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 597,990.00 USD | 520,750.00 USD | 540,700.00 USD |
| `1D` | `0.0772` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 545,340.00 USD | 406,470.00 USD | 802,080.00 USD |
| `7D` | `0.0772` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 0.00 USD | 284,970.00 USD | 1,630.00 USD |
| `1D` | `0.0773` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 412,480.00 USD | 464,690.00 USD | 278,550.00 USD |
| `7D` | `0.0773` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 69,030.00 USD | 62,610.00 USD | 62,430.00 USD |
| `1D` | `0.0774` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 176,230.00 USD | 246,740.00 USD | 49,420.00 USD |
| `7D` | `0.0774` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 137,990.00 USD | 210,270.00 USD | 0.00 USD |
| `1D` | `0.0775` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 354,430.00 USD | 217,430.00 USD | 61,780.00 USD |
| `7D` | `0.0775` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 707,860.00 USD | 164,830.00 USD | 0.00 USD |
| `1D` | `0.0776` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 356,410.00 USD | 228,210.00 USD | 142,590.00 USD |
| `7D` | `0.0776` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 250,110.00 USD | 39,020.00 USD | 0.00 USD |
| `1D` | `0.0777` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 401,010.00 USD | 342,630.00 USD | 163,450.00 USD |
| `7D` | `0.0777` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 15,870.00 USD | 247,550.00 USD | 693.20 USD |
| `1D` | `0.0778` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 116,640.00 USD | 340,450.00 USD | 399,210.00 USD |
| `7D` | `0.0778` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 229,240.00 USD | 86,160.00 USD | 78,860.00 USD |
| `1D` | `0.0779` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 345,840.00 USD | 210,420.00 USD | 206,320.00 USD |
| `7D` | `0.0779` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 41,210.00 USD | 215,530.00 USD | 359,800.00 USD |
| `1D` | `0.0780` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 212,580.00 USD | 78,920.00 USD | 38,440.00 USD |
| `7D` | `0.0780` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 169,380.00 USD | 64,660.00 USD | 3,180.00 USD |
| `1D` | `0.0781` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 20,270.00 USD |
| `7D` | `0.0781` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 17,030.00 USD | 77,790.00 USD | 1,190.00 USD |
| `1D` | `0.0782` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 87,770.00 USD | 92,890.00 USD | 80,080.00 USD |
| `7D` | `0.0782` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 148,920.00 USD | 195,010.00 USD |
| `1D` | `0.0783` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 129,550.00 USD | 239,780.00 USD | 220,140.00 USD |
| `7D` | `0.0783` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 32,110.00 USD | 159,820.00 USD | 20,040.00 USD |
| `1D` | `0.0784` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 436,380.00 USD | 152,210.00 USD | 70,560.00 USD |
| `7D` | `0.0784` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 109,020.00 USD | 45,010.00 USD | 187,060.00 USD |
| `1D` | `0.0785` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 238,930.00 USD | 171,160.00 USD | 121,140.00 USD |
| `7D` | `0.0785` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 248,170.00 USD | 120,330.00 USD | 144,620.00 USD |
| `1D` | `0.0786` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 353,390.00 USD | 218,960.00 USD | 294,890.00 USD |
| `7D` | `0.0786` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 201,610.00 USD | 202,070.00 USD | 488,040.00 USD |
| `1D` | `0.0787` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 418,420.00 USD | 504,080.00 USD | 404,970.00 USD |
| `7D` | `0.0787` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 235,890.00 USD | 143,980.00 USD | 324,670.00 USD |
| `1D` | `0.0788` | 19,110,000.00 USD | 19,110,000.00 USD | 0.00 USD | 280,900.00 USD | 310,220.00 USD | 139,850.00 USD |
| `7D` | `0.0788` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 74,330.00 USD | 22,770.00 USD | 146,160.00 USD |
| `1D` | `0.0789` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 343,470.00 USD | 233,260.00 USD | 111,600.00 USD |
| `7D` | `0.0789` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 260,530.00 USD | 236,420.00 USD | 103,190.00 USD |
| `1D` | `0.0790` | 20,120,000.00 USD | 20,120,000.00 USD | 0.00 USD | 189,430.00 USD | 105,510.00 USD | 27,520.00 USD |
| `7D` | `0.0790` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 353,930.00 USD | 65,630.00 USD | 3,910.00 USD |
| `1D` | `0.0791` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 241,350.00 USD | 140,450.00 USD | 123,720.00 USD |
| `7D` | `0.0791` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 142,610.00 USD | 15,670.00 USD | 2,660.00 USD |
| `1D` | `0.0792` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 224,560.00 USD | 57,840.00 USD | 75,070.00 USD |
| `7D` | `0.0792` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 13,630.00 USD | 61,220.00 USD | 2,100.00 USD |
| `1D` | `0.0793` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 5,950.00 USD | 0.00 USD | 462.96 USD |
| `7D` | `0.0793` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 13,920.00 USD | 0.00 USD | 244,240.00 USD |
| `1D` | `0.0794` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 160,150.00 USD | 96,210.00 USD | 100,920.00 USD |
| `7D` | `0.0794` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 23,360.00 USD | 0.00 USD | 234,520.00 USD |
| `1D` | `0.0795` | 21,600,000.00 USD | 21,600,000.00 USD | 0.00 USD | 102,330.00 USD | 45,380.00 USD | 105,010.00 USD |
| `7D` | `0.0795` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 183,540.00 USD | 0.00 USD | 235,440.00 USD |
| `1D` | `0.0796` | 21,820,000.00 USD | 21,820,000.00 USD | 0.00 USD | 202,390.00 USD | 12,890.00 USD | 588.52 USD |
| `7D` | `0.0796` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 334,830.00 USD | 149,090.00 USD | 77,660.00 USD |
| `1D` | `0.0797` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 210,380.00 USD | 89,760.00 USD | 7,040.00 USD |
| `7D` | `0.0797` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 305,960.00 USD | 54,460.00 USD | 41,520.00 USD |
| `1D` | `0.0798` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 58,670.00 USD | 9,940.00 USD | 2,070.00 USD |
| `7D` | `0.0798` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 520,400.00 USD | 54,200.00 USD | 73,200.00 USD |
| `1D` | `0.0799` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 43,250.00 USD | 191,860.00 USD | 24,180.00 USD |
| `7D` | `0.0799` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 41,190.00 USD | 76,670.00 USD | 4,850.00 USD |
| `1D` | `0.0800` | 22,610,000.00 USD | 22,610,000.00 USD | 0.00 USD | 48,550.00 USD | 9,760.00 USD | 94,110.00 USD |
| `7D` | `0.0800` | 17,930,000.00 USD | 17,930,000.00 USD | 0.00 USD | 46,190.00 USD | 0.00 USD | 102,900.00 USD |
| `1D` | `0.0801` | 22,640,000.00 USD | 22,640,000.00 USD | 0.00 USD | 25,740.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `0.0801` | 17,970,000.00 USD | 17,970,000.00 USD | 0.00 USD | 38,850.00 USD | 0.00 USD | 1,950.00 USD |
| `1D` | `0.0802` | 22,670,000.00 USD | 22,670,000.00 USD | 0.00 USD | 27,390.00 USD | 1,770.00 USD | 3,070.00 USD |
| `7D` | `0.0802` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 12,270.00 USD | 0.00 USD | 2,390.00 USD |
| `1D` | `0.0803` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 25,660.00 USD | 43,340.00 USD | 38,680.00 USD |
| `7D` | `0.0803` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 45,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0804` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0804` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 108,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 22,960,000.00 USD | 22,960,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,140.00 USD |
| `7D` | `0.0805` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 120,200.00 USD | 43,910.00 USD | 53,390.00 USD |
| `1D` | `0.0806` | 23,220,000.00 USD | 23,220,000.00 USD | 0.00 USD | 28,730.00 USD | 21,040.00 USD | 215,650.00 USD |
| `7D` | `0.0806` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 99,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 23,630,000.00 USD | 23,630,000.00 USD | 0.00 USD | 229,530.00 USD | 143,670.00 USD | 30,480.00 USD |
| `7D` | `0.0807` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 118,470.00 USD | 934,840.00 USD | 294,860.00 USD |
| `1D` | `0.0808` | 24,290,000.00 USD | 24,290,000.00 USD | 0.00 USD | 158,180.00 USD | 116,140.00 USD | 382,880.00 USD |
| `7D` | `0.0808` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 9,880.00 USD | 910,170.00 USD | 0.00 USD |
| `1D` | `0.0809` | 24,630,000.00 USD | 24,630,000.00 USD | 0.00 USD | 111,710.00 USD | 220,760.00 USD | 12,790.00 USD |
| `7D` | `0.0809` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 0.00 USD | 851,040.00 USD | 1,700.00 USD |
| `1D` | `0.0810` | 25,070,000.00 USD | 25,070,000.00 USD | 0.00 USD | 177,780.00 USD | 127,690.00 USD | 133,260.00 USD |
| `7D` | `0.0810` | 21,970,000.00 USD | 21,970,000.00 USD | 0.00 USD | 131,030.00 USD | 264,390.00 USD | 0.00 USD |
| `1D` | `0.0811` | 25,270,000.00 USD | 25,270,000.00 USD | 0.00 USD | 100,060.00 USD | 85,950.00 USD | 10,910.00 USD |
| `7D` | `0.0811` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 466,230.00 USD | 1,610.00 USD |
| `1D` | `0.0812` | 25,520,000.00 USD | 25,520,000.00 USD | 0.00 USD | 133,170.00 USD | 101,130.00 USD | 20,000.00 USD |
| `7D` | `0.0812` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 138,370.00 USD | 200,500.00 USD | 1,600.00 USD |
| `1D` | `0.0813` | 25,640,000.00 USD | 25,640,000.00 USD | 0.00 USD | 37,200.00 USD | 28,660.00 USD | 55,750.00 USD |
| `7D` | `0.0813` | 23,510,000.00 USD | 23,510,000.00 USD | 0.00 USD | 378,950.00 USD | 347,890.00 USD | 874.59 USD |
| `1D` | `0.0814` | 25,940,000.00 USD | 25,940,000.00 USD | 0.00 USD | 41,140.00 USD | 108,690.00 USD | 143,010.00 USD |
| `7D` | `0.0814` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 142,940.00 USD | 446,780.00 USD | 3,190.00 USD |
| `1D` | `0.0815` | 26,050,000.00 USD | 26,050,000.00 USD | 0.00 USD | 10,870.00 USD | 6,740.00 USD | 96,260.00 USD |
| `7D` | `0.0815` | 24,960,000.00 USD | 24,960,000.00 USD | 0.00 USD | 447,170.00 USD | 144,240.00 USD | 265,690.00 USD |
| `1D` | `0.0816` | 26,670,000.00 USD | 26,670,000.00 USD | 0.00 USD | 287,650.00 USD | 167,460.00 USD | 165,540.00 USD |
| `7D` | `0.0816` | 25,820,000.00 USD | 25,820,000.00 USD | 0.00 USD | 267,850.00 USD | 451,830.00 USD | 145,480.00 USD |
| `1D` | `0.0817` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 191,130.00 USD | 121,600.00 USD | 72,280.00 USD |
| `7D` | `0.0817` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 789,320.00 USD | 294,010.00 USD | 437,490.00 USD |
| `1D` | `0.0818` | 27,670,000.00 USD | 27,670,000.00 USD | 0.00 USD | 195,830.00 USD | 161,260.00 USD | 260,360.00 USD |
| `7D` | `0.0818` | 28,310,000.00 USD | 28,310,000.00 USD | 0.00 USD | 249,420.00 USD | 327,510.00 USD | 388,760.00 USD |
| `1D` | `0.0819` | 28,270,000.00 USD | 28,270,000.00 USD | 0.00 USD | 153,870.00 USD | 312,480.00 USD | 128,220.00 USD |
| `7D` | `0.0819` | 29,460,000.00 USD | 29,460,000.00 USD | 0.00 USD | 422,920.00 USD | 184,980.00 USD | 540,240.00 USD |
| `1D` | `0.0820` | 28,800,000.00 USD | 28,800,000.00 USD | 0.00 USD | 42,510.00 USD | 172,050.00 USD | 320,170.00 USD |
| `7D` | `0.0820` | 30,350,000.00 USD | 30,350,000.00 USD | 0.00 USD | 288,610.00 USD | 382,680.00 USD | 217,720.00 USD |
| `1D` | `0.0821` | 29,080,000.00 USD | 29,080,000.00 USD | 0.00 USD | 144,440.00 USD | 48,110.00 USD | 84,710.00 USD |
| `7D` | `0.0821` | 31,810,000.00 USD | 31,810,000.00 USD | 0.00 USD | 916,830.00 USD | 377,990.00 USD | 172,610.00 USD |
| `1D` | `0.0822` | 29,630,000.00 USD | 29,630,000.00 USD | 0.00 USD | 247,310.00 USD | 151,600.00 USD | 156,380.00 USD |
| `7D` | `0.0822` | 32,520,000.00 USD | 32,520,000.00 USD | 0.00 USD | 374,110.00 USD | 203,780.00 USD | 128,840.00 USD |
| `1D` | `0.0823` | 29,980,000.00 USD | 29,980,000.00 USD | 0.00 USD | 267,050.00 USD | 72,540.00 USD | 8,390.00 USD |
| `7D` | `0.0823` | 33,590,000.00 USD | 33,590,000.00 USD | 0.00 USD | 510,700.00 USD | 317,120.00 USD | 237,850.00 USD |
| `1D` | `0.0824` | 30,540,000.00 USD | 30,540,000.00 USD | 0.00 USD | 158,060.00 USD | 204,930.00 USD | 191,440.00 USD |
| `7D` | `0.0824` | 34,530,000.00 USD | 34,530,000.00 USD | 0.00 USD | 470,790.00 USD | 274,570.00 USD | 194,990.00 USD |
| `1D` | `0.0825` | 30,780,000.00 USD | 30,780,000.00 USD | 0.00 USD | 99,620.00 USD | 125,690.00 USD | 21,450.00 USD |
| `7D` | `0.0825` | 35,170,000.00 USD | 35,170,000.00 USD | 0.00 USD | 290,680.00 USD | 239,750.00 USD | 112,380.00 USD |
| `1D` | `0.0826` | 31,210,000.00 USD | 31,210,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 169,970.00 USD |
| `7D` | `0.0826` | 36,000,000.00 USD | 36,000,000.00 USD | 0.00 USD | 514,230.00 USD | 68,910.00 USD | 251,430.00 USD |
| `1D` | `0.0827` | 31,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 19,540.00 USD | 65,440.00 USD | 17,300.00 USD |
| `7D` | `0.0827` | 36,330,000.00 USD | 36,330,000.00 USD | 0.00 USD | 144,110.00 USD | 160,890.00 USD | 20,850.00 USD |
| `1D` | `0.0828` | 31,690,000.00 USD | 31,690,000.00 USD | 0.00 USD | 211,700.00 USD | 83,250.00 USD | 80,450.00 USD |
| `7D` | `0.0828` | 36,870,000.00 USD | 36,870,000.00 USD | 0.00 USD | 376,390.00 USD | 110,640.00 USD | 54,090.00 USD |
| `1D` | `0.0829` | 31,980,000.00 USD | 31,980,000.00 USD | 0.00 USD | 198,070.00 USD | 89,690.00 USD | 8,410.00 USD |
| `7D` | `0.0829` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 283,400.00 USD | 67,100.00 USD | 173,780.00 USD |
| `1D` | `0.0830` | 32,120,000.00 USD | 32,120,000.00 USD | 0.00 USD | 54,060.00 USD | 37,820.00 USD | 42,990.00 USD |
| `7D` | `0.0830` | 37,760,000.00 USD | 37,760,000.00 USD | 0.00 USD | 112,420.00 USD | 80,560.00 USD | 173,830.00 USD |
| `1D` | `0.0831` | 32,200,000.00 USD | 32,200,000.00 USD | 0.00 USD | 20,050.00 USD | 16,920.00 USD | 45,230.00 USD |
| `7D` | `0.0831` | 38,210,000.00 USD | 38,210,000.00 USD | 0.00 USD | 294,840.00 USD | 53,670.00 USD | 98,180.00 USD |
| `1D` | `0.0832` | 32,580,000.00 USD | 32,580,000.00 USD | 0.00 USD | 182,710.00 USD | 93,160.00 USD | 100,280.00 USD |
| `7D` | `0.0832` | 38,820,000.00 USD | 38,820,000.00 USD | 0.00 USD | 186,700.00 USD | 262,800.00 USD | 160,430.00 USD |
| `1D` | `0.0833` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 137,070.00 USD | 126,610.00 USD | 186,780.00 USD |
| `7D` | `0.0833` | 39,340,000.00 USD | 39,340,000.00 USD | 0.00 USD | 266,360.00 USD | 152,020.00 USD | 100,110.00 USD |
| `1D` | `0.0834` | 33,480,000.00 USD | 33,480,000.00 USD | 0.00 USD | 163,150.00 USD | 137,940.00 USD | 148,990.00 USD |
| `7D` | `0.0834` | 39,840,000.00 USD | 39,840,000.00 USD | 0.00 USD | 90,460.00 USD | 146,730.00 USD | 265,290.00 USD |
| `1D` | `0.0835` | 33,850,000.00 USD | 33,850,000.00 USD | 0.00 USD | 119,790.00 USD | 188,990.00 USD | 65,070.00 USD |
| `7D` | `0.0835` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 275,000.00 USD | 115,070.00 USD | 271,030.00 USD |
| `1D` | `0.0836` | 34,140,000.00 USD | 34,140,000.00 USD | 0.00 USD | 57,220.00 USD | 82,000.00 USD | 147,210.00 USD |
| `7D` | `0.0836` | 40,820,000.00 USD | 40,820,000.00 USD | 0.00 USD | 204,620.00 USD | 27,680.00 USD | 88,950.00 USD |
| `1D` | `0.0837` | 34,380,000.00 USD | 34,380,000.00 USD | 0.00 USD | 144,720.00 USD | 32,170.00 USD | 62,600.00 USD |
| `7D` | `0.0837` | 41,290,000.00 USD | 41,290,000.00 USD | 0.00 USD | 239,800.00 USD | 199,750.00 USD | 26,260.00 USD |
| `1D` | `0.0838` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 172,840.00 USD | 85,610.00 USD | 42,460.00 USD |
| `7D` | `0.0838` | 41,580,000.00 USD | 41,580,000.00 USD | 0.00 USD | 199,340.00 USD | 64,030.00 USD | 31,610.00 USD |
| `1D` | `0.0839` | 34,780,000.00 USD | 34,780,000.00 USD | 0.00 USD | 43,590.00 USD | 32,460.00 USD | 29,490.00 USD |
| `7D` | `0.0839` | 41,750,000.00 USD | 41,750,000.00 USD | 0.00 USD | 94,520.00 USD | 64,060.00 USD | 4,690.00 USD |
| `7D` | `0.0840` | 41,930,000.00 USD | 41,930,000.00 USD | 0.00 USD | 117,710.00 USD | 0.00 USD | 62,190.00 USD |
| `7D` | `0.0841` | 42,020,000.00 USD | 42,020,000.00 USD | 0.00 USD | 87,460.00 USD | 0.00 USD | 2,760.00 USD |
| `7D` | `0.0842` | 42,350,000.00 USD | 42,350,000.00 USD | 0.00 USD | 220,360.00 USD | 33,520.00 USD | 81,570.00 USD |
| `7D` | `0.0843` | 42,520,000.00 USD | 42,520,000.00 USD | 0.00 USD | 117,190.00 USD | 44,120.00 USD | 3,500.00 USD |
| `7D` | `0.0844` | 42,820,000.00 USD | 42,820,000.00 USD | 0.00 USD | 164,260.00 USD | 64,360.00 USD | 77,300.00 USD |
| `7D` | `0.0845` | 42,980,000.00 USD | 42,980,000.00 USD | 0.00 USD | 70,690.00 USD | 30,660.00 USD | 57,750.00 USD |
| `7D` | `0.0846` | 43,210,000.00 USD | 43,210,000.00 USD | 0.00 USD | 106,330.00 USD | 76,890.00 USD | 40,580.00 USD |
| `7D` | `0.0847` | 43,490,000.00 USD | 43,490,000.00 USD | 0.00 USD | 137,750.00 USD | 113,280.00 USD | 35,260.00 USD |
| `7D` | `0.0848` | 43,770,000.00 USD | 43,770,000.00 USD | 0.00 USD | 117,070.00 USD | 57,210.00 USD | 99,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.06B` | Total OI Tokens: `14,045,643,265.2 DOGE`
  * 1h OI Change: `+0.14%` | 4h OI Change: `-0.02%` | 24h OI Change: `-5.76%`
  * Exchange Breakdown: Binance=`240.43M` | Bybit=`106.39M` | OKX=`111.05M` | Hyperliquid=`75.54M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.69K` | Last 24h: `49.48K` | Last 3d: `238.63K` | Last 7d: `304.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0053%` |
| **USDT Bybit** | `-0.0111%` | **USDT KuCoin** | `0.0046%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0036%` | **USDT Bitget** | `0.0004%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0066%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `42.91%` | `57.09%` | `0.75` | 218,610,000.00 USD |
| `15M` | `Binance` | `40.01%` | `59.99%` | `0.67` | 69,050,000.00 USD |
| `15M` | `OKX` | `38.73%` | `61.27%` | `0.63` | 42,670,000.00 USD |
| `15M` | `Bybit` | `51.71%` | `48.29%` | `1.07` | 12,750,000.00 USD |
| `15M` | `KuCoin` | `42.14%` | `57.86%` | `0.73` | 750,990.00 USD |
| `15M` | `Gate` | `43.77%` | `56.23%` | `0.78` | 36,530,000.00 USD |
| `15M` | `Bitget` | `37.49%` | `62.51%` | `0.60` | 9,570,000.00 USD |
| `15M` | `BingX` | `47.22%` | `52.78%` | `0.89` | 4,630,000.00 USD |
| `15M` | `MEXC` | `44.98%` | `55.02%` | `0.82` | 13,290,000.00 USD |
| `15M` | `Bitunix` | `39.18%` | `60.82%` | `0.64` | 8,170,000.00 USD |
| `15M` | `Hyperliquid` | `68.56%` | `31.44%` | `2.18` | 3,620,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `26.59%` | `73.41%` | `0.36` | 528,440.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `86.92%` | `13.08%` | `6.65` | 2,840,000.00 USD |
| `15M` | `HTX` | `62.22%` | `37.78%` | `1.65` | 2,520,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `63.45%` | `36.55%` | `1.74` | 1,210,000.00 USD |
| `15M` | `Bitfinex` | `72.52%` | `27.48%` | `2.64` | 12,330.00 USD |
| `15M` | `Kraken` | `68.53%` | `31.47%` | `2.18` | 681,430.00 USD |
| `15M` | `Aster` | `40.97%` | `59.03%` | `0.69` | 5,790,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.35%` | `61.65%` | `0.62` | 4,010,000.00 USD |
| `15M` | `Whale Positions` | `40.01%` | `59.99%` | `0.67` | 69,050,000.00 USD |
| `15M` | `Global Accounts` | `42.91%` | `57.09%` | `0.75` | 218,610,000.00 USD |
| `1H` | `DOGE` | `46.51%` | `53.49%` | `0.87` | 62,980,000.00 USD |
| `1H` | `Binance` | `42.56%` | `57.44%` | `0.74` | 37,130,000.00 USD |
| `1H` | `OKX` | `52.65%` | `47.35%` | `1.11` | 6,400,000.00 USD |
| `1H` | `Bybit` | `51.34%` | `48.66%` | `1.06` | 5,560,000.00 USD |
| `1H` | `KuCoin` | `48.45%` | `51.55%` | `0.94` | 458,540.00 USD |
| `1H` | `Gate` | `53%` | `47%` | `1.13` | 2,760,000.00 USD |
| `1H` | `Bitget` | `55.03%` | `44.97%` | `1.22` | 898,590.00 USD |
| `1H` | `BingX` | `36.69%` | `63.31%` | `0.58` | 1,590,000.00 USD |
| `1H` | `MEXC` | `66.13%` | `33.87%` | `1.95` | 986,160.00 USD |
| `1H` | `Bitunix` | `52.87%` | `47.13%` | `1.12` | 2,250,000.00 USD |
| `1H` | `Hyperliquid` | `59.09%` | `40.91%` | `1.44` | 2,390,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.79%` | `55.21%` | `0.81` | 699,480.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `40.57%` | `59.43%` | `0.68` | 299,660.00 USD |
| `1H` | `HTX` | `40.56%` | `59.44%` | `0.68` | 388,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.16%` | `52.84%` | `0.89` | 87,500.00 USD |
| `1H` | `Aster` | `57.78%` | `42.22%` | `1.37` | 786,120.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.86%` | `46.14%` | `1.17` | 302,310.00 USD |
| `1H` | `Whale Positions` | `42.56%` | `57.44%` | `0.74` | 37,130,000.00 USD |
| `1H` | `Global Accounts` | `46.51%` | `53.49%` | `0.87` | 62,980,000.00 USD |
| `4H` | `DOGE` | `50.68%` | `49.32%` | `1.03` | 6,690,000,000.00 USD |
| `4H` | `Binance` | `49.75%` | `50.25%` | `0.99` | 2,070,000,000.00 USD |
| `4H` | `OKX` | `49.58%` | `50.42%` | `0.98` | 1,220,000,000.00 USD |
| `4H` | `Bybit` | `48.72%` | `51.28%` | `0.95` | 397,710,000.00 USD |
| `4H` | `KuCoin` | `54.13%` | `45.87%` | `1.18` | 28,730,000.00 USD |
| `4H` | `Gate` | `50.12%` | `49.88%` | `1.00` | 981,380,000.00 USD |
| `4H` | `Bitget` | `49.67%` | `50.33%` | `0.99` | 225,100,000.00 USD |
| `4H` | `BingX` | `49.27%` | `50.73%` | `0.97` | 89,050,000.00 USD |
| `4H` | `MEXC` | `50.66%` | `49.34%` | `1.03` | 243,900,000.00 USD |
| `4H` | `Bitunix` | `49.69%` | `50.31%` | `0.99` | 220,080,000.00 USD |
| `4H` | `Hyperliquid` | `49.38%` | `50.62%` | `0.98` | 362,060,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.03%` | `51.97%` | `0.92` | 31,890,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `65.15%` | `34.85%` | `1.87` | 483,970,000.00 USD |
| `4H` | `HTX` | `35.11%` | `64.89%` | `0.54` | 91,200,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.07%` | `49.93%` | `1.00` | 69,250,000.00 USD |
| `4H` | `Bitfinex` | `49.24%` | `50.76%` | `0.97` | 2,020,000.00 USD |
| `4H` | `Kraken` | `46.69%` | `53.31%` | `0.88` | 23,240,000.00 USD |
| `4H` | `Aster` | `50.29%` | `49.71%` | `1.01` | 63,350,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.93%` | `46.07%` | `1.17` | 78,690,000.00 USD |
| `4H` | `Whale Positions` | `49.75%` | `50.25%` | `0.99` | 2,070,000,000.00 USD |
| `4H` | `Global Accounts` | `50.68%` | `49.32%` | `1.03` | 6,690,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0754` | 2,313,298.65 USD | 1,197,641.49 USD | 1,115,657.16 USD | 81,984.32 USD | `+3.54%` | `3B / 4S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0756` | `0.0753` | 2,260,519.88 USD | 1,007,921.72 USD | 1,252,598.16 USD | -244,676.43 USD | `-10.82%` | `2B / 8S` |
| `0:00 UTC` | `0.0755` | `0.0754` | `0.0755` | `0.0756` | `0.0752` | 2,922,007.92 USD | 1,333,625.48 USD | 1,588,382.44 USD | -254,756.96 USD | `-8.72%` | `6B / 8S` |
| `5:00 UTC` | `0.0754` | `0.0754` | `0.0754` | `0.0755` | `0.0753` | 1,576,593.18 USD | 686,951.41 USD | 889,641.77 USD | -202,690.36 USD | `-12.86%` | `0B / 6S` |
| `0:00 UTC` | `0.0753` | `0.0753` | `0.0753` | `0.0755` | `0.0752` | 4,029,142.63 USD | 2,078,130.01 USD | 1,951,012.62 USD | 127,117.39 USD | `+3.15%` | `4B / 6S` |
| `5:00 UTC` | `0.0753` | `0.0754` | `0.0753` | `0.0756` | `0.0752` | 2,334,240.03 USD | 1,034,700.08 USD | 1,299,539.95 USD | -264,839.88 USD | `-11.35%` | `4B / 9S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0760` | `0.0754` | 4,037,679.84 USD | 2,041,412.62 USD | 1,996,267.22 USD | 45,145.39 USD | `+1.12%` | `14B / 6S` |
| `5:00 UTC` | `0.0757` | `0.0759` | `0.0757` | `0.0761` | `0.0756` | 3,472,621.71 USD | 1,543,592.50 USD | 1,929,029.21 USD | -385,436.71 USD | `-11.10%` | `10B / 7S` |
| `0:00 UTC` | `0.0758` | `0.0759` | `0.0758` | `0.0762` | `0.0758` | 4,537,587.82 USD | 2,186,610.43 USD | 2,350,977.40 USD | -164,366.97 USD | `-3.62%` | `4B / 11S` |
| `5:00 UTC` | `0.0758` | `0.0757` | `0.0758` | `0.0758` | `0.0756` | 1,554,945.93 USD | 782,317.80 USD | 772,628.13 USD | 9,689.67 USD | `+0.62%` | `7B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:51` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 20:12` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Volume 100M DOGE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Volume 100M DOGE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.0786` | 17,000,000.00 USD | 0.00 USD |
| `10-28 17:27` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0799` | 0.00 USD | 0.00 USD |
| `10-28 16:36` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0800` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0803` | 0.00 USD | 0.00 USD |
| `10-28 15:16` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 15:13` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 13:51` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0804` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0802` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 100M DOGE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0797` | 0.00 USD | 0.00 USD |
| `10-28 07:56` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0793` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 07:07` | `Range 0.0002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.0794` | 74,000,000.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -22,990.00 USD | 109,680.00 USD | **`ACCUMULATION`** |
| `15m` | -357,030.00 USD | -722,620.00 USD | **`DISTRIBUTION`** |
| `30m` | -396,730.00 USD | 115,300.00 USD | **`DISTRIBUTION`** |
| `1h` | -167,670.00 USD | 296,320.00 USD | **`ACCUMULATION`** |
| `2h` | 277,310.00 USD | -385,970.00 USD | **`DISTRIBUTION`** |
| `4h` | -828,110.00 USD | -7,820,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,420,000.00 USD | -10,020,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 767,340.00 USD | -4,490,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,340,000.00 USD | -31,020,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,250,000.00 USD | -62,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -59,920,000.00 USD | -193,610,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -284,140,000.00 USD | -827,520,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-22.99K` | 15m=`-357.03K` | 1h=`-167.67K` | 24h=`-18.25M`
* Futures Capital Netflows: 5m=`+109.68K` | 15m=`-722.62K` | 1h=`+296.32K` | 24h=`-62.08M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0737` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0700` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0842`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0754` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0790` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0649`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0764`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
