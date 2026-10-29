# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:51:54 IST` (`2026-10-29 21:21:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `24.03 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-2.06` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0118` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `29.42` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.23`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.24`
  * Upper +2.01σ Band: `1.32` | Lower -2.01σ Band: `1.25`
  * Upper +2.00σ Band: `1.32` | Lower -2.00σ Band: `1.25`
  * Upper +1.28σ Band: `1.31` | Lower -1.28σ Band: `1.26`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.27`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.26` | EMA-20=`1.27` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.3045`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.22` | Weekly High=`1.34` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.25` (Distance: `-0.11%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.20%`)
  * Value Area Low (VAL) = `1.24` (Distance: `+1.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.25` | Low=`1.23`
  * London Session (08:00-16:00 UTC): High=`1.25` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.25` | IB Low=`1.24`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.24` - `1.25`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.23` | `1.25` | `1.23` | `1.25` | `9,893,442` | 12,283,673.61 USD | 1,562,420.62 USD | `+12.72%` | -77,427,982.97 USD | `+0.84` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `8,402,769` | 10,490,018.16 USD | 771,198.35 USD | `+7.35%` | -76,656,784.62 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `256,213` | 320,114.78 USD | -142,553.87 USD | `-44.53%` | -76,799,338.49 USD | `+0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.24` | `1.25` | `1.22` | `1.24` | `78,367,361` | 96,971,024.45 USD | -4,605,357.71 USD | `-4.75%` | -78,887,194.88 USD | `-0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.24` | `1.25` | `1.23` | `1.25` | `34,560,808` | 42,899,530.36 USD | 2,631,101.42 USD | `+6.13%` | -76,256,093.46 USD | `+0.88` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `284,448` | 355,390.13 USD | -135,948.33 USD | `-38.25%` | -76,392,041.79 USD | `+0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `17,509,907` | 22,469,016.48 USD | -1,419,504.92 USD | `-6.32%` | -40,597,161.54 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.22` | `1.24` | `208,906,305` | 260,797,546.37 USD | -37,805,029.03 USD | `-14.50%` | -78,402,190.57 USD | `-3.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.24` | `1.25` | `1.23` | `1.25` | `34,853,966` | 43,265,799.20 USD | 2,501,024.06 USD | `+5.78%` | -75,901,166.51 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `243,705,985` | 303,995,527.35 USD | -35,325,589.74 USD | `-11.62%` | -75,264,619.55 USD | `-1.69` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `243,705,985` | 303,995,527.35 USD | -35,325,589.74 USD | `-11.62%` | -75,264,619.55 USD | `-1.69` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.25` | `11550.0000` | 14,452.52 USD | 1,022,647.20 USD | `8 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `62664.0000` | 78,405.20 USD | 1,008,194.68 USD | `9 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `51629.0000` | 64,593.04 USD | 929,789.49 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `76475.0000` | 95,670.22 USD | 865,196.44 USD | `8 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `20959.0000` | 26,217.61 USD | 769,526.22 USD | `7 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `66767.0000` | 83,512.16 USD | 743,308.61 USD | `8 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `63337.0000` | 79,215.59 USD | 659,796.44 USD | `12 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `122225.0000` | 152,854.58 USD | 580,580.86 USD | `10 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `13089.0000` | 16,367.79 USD | 427,726.27 USD | `4 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `25719.0000` | 32,159.04 USD | 411,358.48 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `70657.0000` | 88,342.45 USD | 379,199.44 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `28397.0000` | 35,501.93 USD | 290,856.99 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `34906.0000` | 43,635.99 USD | 255,355.06 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `38261.0000` | 47,826.25 USD | 211,719.07 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `30034.0000` | 37,539.50 USD | 163,892.82 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `18035.0000` | 22,540.14 USD | 126,353.33 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `54852.0000` | 68,548.54 USD | 103,813.18 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `6264.0000` | 7,827.49 USD | 35,264.64 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `15694.0000` | 19,609.65 USD | 27,437.14 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `6265.0000` | 7,827.49 USD | 7,827.49 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `26919.0000` | 33,629.91 USD | 33,629.91 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `10860.0000` | 13,566.31 USD | 47,196.22 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `16869.0000` | 21,071.07 USD | 68,267.29 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `61933.0000` | 77,354.32 USD | 145,621.60 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `51679.0000` | 64,541.90 USD | 210,163.51 USD | `14 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `40300.0000` | 50,326.64 USD | 260,490.15 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `21797.0000` | 27,217.91 USD | 287,708.06 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `204291.0000` | 255,077.74 USD | 542,785.80 USD | `17 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `66618.0000` | 83,172.57 USD | 625,958.38 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `243466.0000` | 303,942.95 USD | 929,901.33 USD | `10 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `47205.0000` | 58,926.00 USD | 988,827.33 USD | `10 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `46123.0000` | 57,570.73 USD | 1,046,398.06 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `93419.0000` | 116,596.25 USD | 1,162,994.31 USD | `7 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `24540.0000` | 30,625.92 USD | 1,193,620.23 USD | `7 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `13010.0000` | 16,235.18 USD | 1,209,855.41 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `944273.0000` | 1,178,263.85 USD | 2,388,119.26 USD | `9 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `99759.0000` | 124,469.30 USD | 2,512,588.57 USD | `9 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `24874.0000` | 31,032.80 USD | 2,543,621.37 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `83423.0000` | 104,070.19 USD | 2,647,691.56 USD | `7 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `44365.0000` | 55,340.90 USD | 2,703,032.46 USD | `8 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,775,274.93 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,196,391.66 USD | `+9.59%` | `10X Cross` |
| `89` | `0x5b5d...c060` | `SHORT` | 19,979,260.13 USD | `15,964,251.00` | `1.44` | `1.25` | `12.20` | 2,936,808.58 USD | `+14.70%` | `5X Cross` |
| `154` | `0xb83d...6e36` | `SHORT` | 13,206,979.04 USD | `10,555,450.00` | `1.50` | `1.25` | `15.25` | 2,615,590.60 USD | `+19.80%` | `5X Cross` |
| `278` | `0x58f0...0d20` | `LONG` | 8,547,623.88 USD | `6,840,288.00` | `1.25` | `1.25` | `1.21` | 18,888.30 USD | `+0.22%` | `20X Cross` |
| `379` | `0x77ee...a018` | `LONG` | 6,182,591.22 USD | `4,943,700.00` | `1.27` | `1.25` | `0.4169` | -95,907.78 USD | `-1.55%` | `20X Cross` |
| `425` | `0xca49...53c8` | `SHORT` | 5,178,160.27 USD | `4,138,886.00` | `1.44` | `1.25` | `4.74` | 775,162.46 USD | `+14.97%` | `20X Cross` |
| `490` | `0xecb6...2b00` | `SHORT` | 4,508,056.93 USD | `3,602,123.00` | `1.29` | `1.25` | `8.54` | 137,149.56 USD | `+3.04%` | `10X Cross` |
| `497` | `0x610b...b613` | `LONG` | 4,437,374.79 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8132` | -662,617.82 USD | `-14.93%` | `5X Cross` |
| `521` | `0xfc27...9d9d` | `SHORT` | 4,191,286.02 USD | `3,349,010.00` | `1.31` | `1.25` | `6.29` | 187,955.16 USD | `+4.48%` | `20X Cross` |
| `527` | `0xdd53...2b13` | `SHORT` | 4,169,514.09 USD | `3,331,081.00` | `1.43` | `1.25` | `19.91` | 603,580.36 USD | `+14.48%` | `3X Cross` |
| `607` | `0x9946...0852` | `SHORT` | 3,738,225.00 USD | `2,990,580.00` | `1.43` | `1.25` | `1.76` | 525,725.47 USD | `+14.06%` | `20X Cross` |
| `683` | `0xc30c...a4c9` | `SHORT` | 3,281,424.61 USD | `2,625,980.00` | `1.42` | `1.25` | `1.65` | 455,400.05 USD | `+13.88%` | `7X Cross` |
| `699` | `0x9aa5...58af` | `SHORT` | 3,223,073.53 USD | `2,604,083.00` | `1.46` | `1.25` | `4.77` | 574,647.13 USD | `+17.83%` | `20X Cross` |
| `701` | `0xf48f...10fe` | `LONG` | 3,211,329.00 USD | `2,565,779.00` | `1.53` | `1.25` | `1.01` | -713,311.73 USD | `-22.21%` | `4X Cross` |
| `747` | `0x45d2...4029` | `SHORT` | 3,065,514.10 USD | `2,453,000.00` | `1.48` | `1.25` | `17.93` | 572,766.32 USD | `+18.68%` | `20X Cross` |
| `752` | `0x023a...2355` | `SHORT` | 3,054,947.79 USD | `2,441,029.00` | `1.32` | `1.25` | `4.45` | 174,368.83 USD | `+5.71%` | `20X Cross` |
| `936` | `0xfc66...ca06` | `SHORT` | 2,410,352.97 USD | `1,926,433.00` | `1.30` | `1.25` | `19.88` | 95,541.23 USD | `+3.96%` | `20X Cross` |
| `1066` | `0xc179...e0c8` | `SHORT` | 2,093,571.54 USD | `1,676,064.00` | `1.30` | `1.25` | `5.37` | 87,588.61 USD | `+4.18%` | `10X Cross` |
| `1113` | `0xeadc...9d55` | `LONG` | 2,004,103.74 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 45,260.71 USD | `+2.26%` | `20X Cross` |
| `1183` | `0xbcd4...0dd2` | `SHORT` | 1,914,273.39 USD | `1,529,461.00` | `1.31` | `1.25` | `2.06` | 90,271.21 USD | `+4.72%` | `20X Cross` |
| `1191` | `0x94b2...599e` | `SHORT` | 1,906,226.13 USD | `1,540,696.00` | `1.36` | `1.25` | `1.87` | 194,240.32 USD | `+10.19%` | `20X Cross` |
| `1197` | `0x3fc5...c0c1` | `SHORT` | 1,892,747.31 USD | `1,511,779.00` | `1.52` | `1.25` | `2.63` | 398,867.29 USD | `+21.07%` | `20X Cross` |
| `1231` | `0x31ef...f715` | `LONG` | 1,843,259.97 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -356,005.43 USD | `-19.31%` | `3X Isolated` |
| `1273` | `0xe9d1...d2d3` | `SHORT` | 1,779,401.59 USD | `1,422,156.00` | `1.27` | `1.25` | `2.02` | 27,482.54 USD | `+1.54%` | `10X Cross` |
| `1285` | `0x4537...8732` | `SHORT` | 1,758,064.74 USD | `1,406,902.00` | `1.25` | `1.25` | `1.96` | -4,322.04 USD | `-0.25%` | `10X Cross` |
| `1292` | `0x7737...bf66` | `SHORT` | 1,749,446.87 USD | `1,413,466.00` | `1.41` | `1.25` | `13.43` | 249,421.78 USD | `+14.26%` | `10X Cross` |
| `1348` | `0x95da...2328` | `LONG` | 1,656,889.93 USD | `1,324,876.00` | `1.35` | `1.25` | `0.0450` | -136,751.17 USD | `-8.25%` | `5X Cross` |
| `1357` | `0xef96...9383` | `SHORT` | 1,648,343.61 USD | `1,319,097.00` | `1.34` | `1.25` | `4.52` | 119,100.86 USD | `+7.23%` | `20X Cross` |
| `1376` | `0xee2b...d67e` | `LONG` | 1,632,201.86 USD | `1,306,284.00` | `1.55` | `1.25` | `0.3797` | -398,453.04 USD | `-24.41%` | `4X Cross` |
| `1402` | `0x215d...f80a` | `LONG` | 1,591,133.74 USD | `1,251,777.00` | `1.32` | `1.25` | `1.15` | -63,320.48 USD | `-3.98%` | `14X Cross` |
| `1470` | `0x123d...3bff` | `LONG` | 1,521,713.44 USD | `1,215,329.00` | `1.35` | `1.25` | `0.000000` | -115,355.78 USD | `-7.58%` | `10X Cross` |
| `1527` | `0xdf95...7d72` | `SHORT` | 1,449,590.54 USD | `1,160,508.00` | `1.37` | `1.25` | `35.58` | 143,863.05 USD | `+9.92%` | `20X Cross` |
| `1533` | `0x5fa3...35b7` | `SHORT` | 1,445,281.86 USD | `1,156,133.00` | `1.31` | `1.25` | `3.37` | 66,511.72 USD | `+4.60%` | `20X Cross` |
| `1679` | `0xb1ce...681b` | `LONG` | 1,276,898.47 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -247,158.02 USD | `-19.36%` | `4X Isolated` |
| `1782` | `0x3c36...461a` | `LONG` | 1,175,439.77 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -43,640.84 USD | `-3.71%` | `10X Cross` |
| `2003` | `0x2577...4897` | `SHORT` | 1,003,949.14 USD | `803,738.00` | `1.28` | `1.25` | `5.34` | 22,868.91 USD | `+2.28%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,504.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.50K USD at 1.3325 USD [API] | `2026-10-28 04:12:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,033.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.03K USD at 1.3286 USD [API] | `2026-10-28 04:23:34` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 17,296.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.30K USD at 1.3295 USD [API] | `2026-10-28 04:52:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,198.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.20K USD at 1.3281 USD [API] | `2026-10-28 05:00:54` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 275.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.3441 USD [API] | `2026-10-28 03:32:52` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 15,001.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.00K USD at 1.3270 USD [API] | `2026-10-28 05:03:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,704.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.70K USD at 1.3279 USD [API] | `2026-10-28 05:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,052.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.05K USD at 1.3280 USD [API] | `2026-10-28 05:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3280 USD [API] | `2026-10-28 05:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3282 USD [API] | `2026-10-28 05:17:41` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 15,824.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.82K USD at 1.3272 USD [API] | `2026-10-28 05:37:14` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 21,286.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 21.29K USD at 1.3245 USD [API] | `2026-10-28 07:29:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,168.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.17K USD at 1.3241 USD [API] | `2026-10-28 07:31:17` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,240.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.24K USD at 1.3280 USD [API] | `2026-10-28 07:53:43` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,384.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.38K USD at 1.3287 USD [API] | `2026-10-28 07:58:42` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3287 USD [API] | `2026-10-28 07:58:42` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3288 USD [API] | `2026-10-28 07:58:42` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,007.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3345 USD [API] | `2026-10-28 08:28:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,819.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.82K USD at 1.3346 USD [API] | `2026-10-28 08:28:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3346 USD [API] | `2026-10-28 08:28:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,414.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.41K USD at 1.3335 USD [API] | `2026-10-28 08:32:35` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25,032.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 25.03K USD at 1.3335 USD [API] | `2026-10-28 08:32:35` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,733.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.73K USD at 1.3334 USD [API] | `2026-10-28 08:32:35` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,820.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.82K USD at 1.3334 USD [API] | `2026-10-28 08:32:35` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 11,447.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.45K USD at 1.3358 USD [API] | `2026-10-28 08:44:03` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,819.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.82K USD at 1.3324 USD [API] | `2026-10-28 09:12:39` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3332 USD [API] | `2026-10-28 09:17:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3331 USD [API] | `2026-10-28 09:20:09` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,551.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.55K USD at 1.3310 USD [API] | `2026-10-28 09:26:36` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 15,000.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.00K USD at 1.3310 USD [API] | `2026-10-28 09:48:56` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,832.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.83K USD at 1.3303 USD [API] | `2026-10-28 09:51:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,909.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.91K USD at 1.3303 USD [API] | `2026-10-28 09:51:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3315 USD [API] | `2026-10-28 09:59:30` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,923.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.92K USD at 1.3319 USD [API] | `2026-10-28 10:00:03` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,947.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.95K USD at 1.3311 USD [API] | `2026-10-28 10:00:43` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,123.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.12K USD at 1.3285 USD [API] | `2026-10-28 10:12:47` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,844.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.84K USD at 1.3301 USD [API] | `2026-10-28 10:16:31` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3301 USD [API] | `2026-10-28 10:16:31` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,819.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.82K USD at 1.3301 USD [API] | `2026-10-28 10:16:31` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3301 USD [API] | `2026-10-28 10:16:31` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,694.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.69K USD at 1.3291 USD [API] | `2026-10-28 10:17:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,936.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.94K USD at 1.3306 USD [API] | `2026-10-28 10:31:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,935.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.94K USD at 1.3305 USD [API] | `2026-10-28 10:31:48` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 5,885.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.89K USD at 1.4571 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 276.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.4571 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 294.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.4571 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 30.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.4571 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 1,350.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.35K USD at 1.4571 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 10,738.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.74K USD at 1.4572 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 11.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4573 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 2,126.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.13K USD at 1.4573 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 9,994.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.99K USD at 1.4574 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 9,668.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.67K USD at 1.4574 USD [API] | `2026-10-07 02:01:09` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3292 USD [API] | `2026-10-28 10:38:42` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3287 USD [API] | `2026-10-28 10:58:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,687.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.69K USD at 1.3255 USD [API] | `2026-10-28 11:10:20` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,807.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.81K USD at 1.3269 USD [API] | `2026-10-28 11:26:39` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 433.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.43K USD at 1.3812 USD [API] | `2026-10-21 14:50:30` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25,222.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.22K USD at 1.3275 USD [API] | `2026-10-28 11:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,929.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.93K USD at 1.3245 USD [API] | `2026-10-28 11:57:28` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,638.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.64K USD at 1.3249 USD [API] | `2026-10-28 11:58:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3198 USD [API] | `2026-10-28 12:09:04` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,000,000.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+6.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+6.24%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+6.33%`) | Long MP=`1.27` (Vol: 2,800,000.00 USD, Dist: `--0.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 354.96 USD | 70,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 25,040.00 USD | 70,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 2,740.00 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 6,670.00 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 14,270.00 USD | 70,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 1,380.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 114,130.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 708.53 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 12,510.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 30,620.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 17,450.00 USD | 70,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 421.88 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 346.88 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 530,350.00 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 7,840.00 USD | 70,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 2,210,000.00 USD | 70,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 1,600.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 551.96 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 1,930.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 63,660.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 6,260.00 USD | 67,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,890.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 1,780.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 588.50 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 7,290.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 633.26 USD | 67,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 3,540.00 USD | 67,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,870.00 USD | 67,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 168,060.00 USD | 67,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 2,980.00 USD | 67,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 29,530.00 USD | 67,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 32,370.00 USD | 67,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 67,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 22,110.00 USD | 67,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 1,560.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,030.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 15,700.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 30,110.00 USD | 67,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 21,150.00 USD | 67,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 7,810.00 USD | 67,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 28,070.00 USD | 67,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,440.00 USD | 67,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 244,720.00 USD | 67,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 21,910.00 USD | 67,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 62,010.00 USD | 67,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 107,370.00 USD | 67,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 218,080.00 USD | 66,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,760.00 USD | 66,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 27,790.00 USD | 66,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 12,080.00 USD | 66,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 23,890.00 USD | 66,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 14,900.00 USD | 66,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 55,220.00 USD | 66,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 66,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 283,660.00 USD | 63,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 72,590.00 USD | 63,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 6,060.00 USD | 63,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 85,730.00 USD | 63,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 371,120.00 USD | 63,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 102,690.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 148,850.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 50,060.00 USD | 62,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 147,510.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 87,100.00 USD | 62,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 97,300.00 USD | 62,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 116,510.00 USD | 62,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 62,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 158,540.00 USD | 28,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 450,730.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 98,040.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 451,390.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 181,040.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 3,440,000.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 1,280,000.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,130,000.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 532,180.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 440,750.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 758,070.00 USD | 17,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 603,690.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 65,590.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 38,640,000.00 USD | 38,640,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 18,970,000.00 USD | 18,970,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 18,840,000.00 USD | 18,840,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 38,620,000.00 USD | 38,620,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 249,040.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 18,810,000.00 USD | 18,810,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 38,610,000.00 USD | 38,610,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 18,810,000.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 38,530,000.00 USD | 38,530,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 267,340.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 18,750,000.00 USD | 18,750,000.00 USD | 0.00 USD | 783.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 18,750,000.00 USD | 18,750,000.00 USD | 0.00 USD | 41,620.00 USD | 76,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 38,530,000.00 USD | 38,530,000.00 USD | 5,450.00 USD | 2,160.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 38,520,000.00 USD | 38,520,000.00 USD | 144,660.00 USD | 0.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 18,630,000.00 USD | 18,630,000.00 USD | 7,260.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 38,230,000.00 USD | 38,230,000.00 USD | 0.00 USD | 88,050.00 USD | 150,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 215,570.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 18,620,000.00 USD | 18,620,000.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 37,990,000.00 USD | 37,990,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 37,890,000.00 USD | 37,890,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 18,580,000.00 USD | 18,580,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 37,880,000.00 USD | 37,880,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 18,510,000.00 USD | 18,510,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 37,820,000.00 USD | 37,820,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 18,440,000.00 USD | 18,440,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 37,700,000.00 USD | 37,700,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 1,710,000.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 37,690,000.00 USD | 37,690,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 18,310,000.00 USD | 18,310,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 37,550,000.00 USD | 37,550,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 37,190,000.00 USD | 37,190,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 18,290,000.00 USD | 18,290,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 37,030,000.00 USD | 37,030,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 18,230,000.00 USD | 18,230,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 36,650,000.00 USD | 36,650,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 482,060.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 17,850,000.00 USD | 17,850,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 36,000,000.00 USD | 36,000,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 17,730,000.00 USD | 17,730,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 35,200,000.00 USD | 35,200,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 17,550,000.00 USD | 17,550,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 34,680,000.00 USD | 34,680,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 17,170,000.00 USD | 17,170,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 33,650,000.00 USD | 33,650,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 16,430,000.00 USD | 16,430,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 32,280,000.00 USD | 32,280,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,510,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 16,000,000.00 USD | 16,000,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 31,650,000.00 USD | 31,650,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 15,670,000.00 USD | 15,670,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 30,270,000.00 USD | 30,270,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 15,490,000.00 USD | 15,490,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 28,770,000.00 USD | 28,770,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 15,330,000.00 USD | 15,330,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 27,380,000.00 USD | 27,380,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 15,110,000.00 USD | 15,110,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 26,580,000.00 USD | 26,580,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 481,590.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 14,840,000.00 USD | 14,840,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 25,700,000.00 USD | 25,700,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 14,610,000.00 USD | 14,610,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 25,240,000.00 USD | 25,240,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 14,440,000.00 USD | 14,440,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 24,530,000.00 USD | 24,530,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 14,340,000.00 USD | 14,340,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 24,150,000.00 USD | 24,150,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 14,260,000.00 USD | 14,260,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 24,020,000.00 USD | 24,020,000.00 USD | 131,590.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 741,690.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 14,150,000.00 USD | 14,150,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 23,500,000.00 USD | 23,500,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 13,920,000.00 USD | 13,920,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 22,730,000.00 USD | 22,730,000.00 USD | 186,430.00 USD | 132,500.00 USD | 282,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 13,120,000.00 USD | 13,120,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 22,130,000.00 USD | 22,130,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 13,090,000.00 USD | 13,090,000.00 USD | 40,460.00 USD | 17,640.00 USD | 92,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 21,440,000.00 USD | 21,440,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 12,940,000.00 USD | 12,940,000.00 USD | 66,050.00 USD | 221,930.00 USD | 81,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 20,770,000.00 USD | 20,770,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 379,860.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 12,570,000.00 USD | 12,570,000.00 USD | 31,180.00 USD | 6,070.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 20,070,000.00 USD | 20,070,000.00 USD | 5,350.00 USD | 97,860.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 12,500,000.00 USD | 12,500,000.00 USD | 39,940.00 USD | 0.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 19,780,000.00 USD | 19,780,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 14,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 19,630,000.00 USD | 19,630,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 19,550,000.00 USD | 19,550,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 12,440,000.00 USD | 12,440,000.00 USD | 31,120.00 USD | 104,040.00 USD | 191,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 9,230,000.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 19,150,000.00 USD | 19,150,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 19,060,000.00 USD | 19,060,000.00 USD | 468,800.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 12,110,000.00 USD | 12,110,000.00 USD | 135,040.00 USD | 244,960.00 USD | 71,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 18,190,000.00 USD | 18,190,000.00 USD | 180,260.00 USD | 264,440.00 USD | 783,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 11,660,000.00 USD | 11,660,000.00 USD | 419,060.00 USD | 94,800.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 16,960,000.00 USD | 16,960,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 9,910,000.00 USD | 9,910,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 16,550,000.00 USD | 16,550,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 710,620.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 9,890,000.00 USD | 9,890,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 16,380,000.00 USD | 16,380,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 9,650,000.00 USD | 9,650,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 15,830,000.00 USD | 15,830,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 8,960,000.00 USD | 8,960,000.00 USD | 157,550.00 USD | 6,840.00 USD | 208,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 15,530,000.00 USD | 15,530,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 211.25 USD | 47,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 191,360.00 USD | 659,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 8,540,000.00 USD | 8,540,000.00 USD | 40,080.00 USD | 486,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 14,180,000.00 USD | 14,180,000.00 USD | 627,450.00 USD | 191,250.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 421,580.00 USD | 425,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 6,850,000.00 USD | 6,850,000.00 USD | 449,150.00 USD | 0.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 13,350,000.00 USD | 13,350,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 5,250,000.00 USD | 5,250,000.00 USD | 48,560.00 USD | 3,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 917,970.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 5,200,000.00 USD | 5,200,000.00 USD | 191,290.00 USD | 236,160.00 USD | 543,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 11,950,000.00 USD | 11,950,000.00 USD | 782,590.00 USD | 475,720.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 4,220,000.00 USD | 4,220,000.00 USD | 271,900.00 USD | 757,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 10,690,000.00 USD | 10,690,000.00 USD | 656,500.00 USD | 135,640.00 USD | 91,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 3,190,000.00 USD | 3,190,000.00 USD | 86,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 9,800,000.00 USD | 9,800,000.00 USD | 996,240.00 USD | 513,510.00 USD | 29,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 4,170.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 8,260,000.00 USD | 8,260,000.00 USD | 1,640,000.00 USD | 1,110,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 5,510,000.00 USD | 5,510,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 340,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 3,740,000.00 USD | 3,740,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 2,770,000.00 USD | 2,770,000.00 USD | 112,970.00 USD | 0.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 1,910,000.00 USD | 1,910,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 1,400,000.00 USD | 1,400,000.00 USD | 721,110.00 USD | 0.00 USD | 678,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 4,340,000.00 USD | 4,340,000.00 USD | 2,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 8,680,000.00 USD | 8,680,000.00 USD | 2,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 8,790.00 USD | 8,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.25` | 1,490,000.00 USD | 1,490,000.00 USD | 861,120.00 USD | 81,840.00 USD | 551,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 18,610,000.00 USD | 18,610,000.00 USD | 2,330,000.00 USD | 1,140,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 4,570,000.00 USD | 4,570,000.00 USD | 218,430.00 USD | 833,450.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 26,530,000.00 USD | 26,530,000.00 USD | 2,720,000.00 USD | 1,770,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 6,850,000.00 USD | 6,850,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 32,230,000.00 USD | 32,230,000.00 USD | 2,810,000.00 USD | 888,720.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 7,200,000.00 USD | 7,200,000.00 USD | 351,630.00 USD | 0.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 36,410,000.00 USD | 36,410,000.00 USD | 1,240,000.00 USD | 1,460,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 7,760,000.00 USD | 7,760,000.00 USD | 551,630.00 USD | 0.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 39,270,000.00 USD | 39,270,000.00 USD | 998,540.00 USD | 441,280.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 39,570.00 USD | 48,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.26` | 9,980,000.00 USD | 9,980,000.00 USD | 1,460,000.00 USD | 760,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 44,410,000.00 USD | 44,410,000.00 USD | 2,180,000.00 USD | 992,480.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 11,010,000.00 USD | 11,010,000.00 USD | 1,030,000.00 USD | 2,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 47,210,000.00 USD | 47,210,000.00 USD | 107,140.00 USD | 0.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 11,740,000.00 USD | 11,740,000.00 USD | 472,940.00 USD | 246,640.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 48,740,000.00 USD | 48,740,000.00 USD | 0.00 USD | 0.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 13,400,000.00 USD | 13,400,000.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 50,650,000.00 USD | 50,650,000.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 23,320.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 57,590,000.00 USD | 57,590,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 45,120.00 USD | 93,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 16,100,000.00 USD | 16,100,000.00 USD | 39,860.00 USD | 1,030,000.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 68,500,000.00 USD | 68,500,000.00 USD | 2,620,000.00 USD | 1,990,000.00 USD | 6,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 1,280,000.00 USD | 794,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 73,280,000.00 USD | 73,280,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 18,950,000.00 USD | 18,950,000.00 USD | 0.00 USD | 780,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 75,200,000.00 USD | 75,200,000.00 USD | 178,380.00 USD | 1,620,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 20,290,000.00 USD | 20,290,000.00 USD | 961,090.00 USD | 313,930.00 USD | 57,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 78,590,000.00 USD | 78,590,000.00 USD | 186,960.00 USD | 3,000,000.00 USD | 207,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 22,850,000.00 USD | 22,850,000.00 USD | 60,090.00 USD | 761,570.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 92,970,000.00 USD | 92,970,000.00 USD | 4,420,000.00 USD | 1,750,000.00 USD | 8,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 234,140.00 USD | 327,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 27,620,000.00 USD | 27,620,000.00 USD | 481,200.00 USD | 1,370,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 111,240,000.00 USD | 111,240,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 40,880,000.00 USD | 40,880,000.00 USD | 6,010,000.00 USD | 2,720,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 116,370,000.00 USD | 116,370,000.00 USD | 3,260,000.00 USD | 1,750,000.00 USD | 120,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,420,000.00 USD | 43,420,000.00 USD | 188,330.00 USD | 1,650,000.00 USD | 695,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 117,320,000.00 USD | 117,320,000.00 USD | 0.00 USD | 869,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 44,380,000.00 USD | 44,380,000.00 USD | 547,110.00 USD | 0.00 USD | 405,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 118,460,000.00 USD | 118,460,000.00 USD | 1,080,000.00 USD | 16,490.00 USD | 45,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 46,190,000.00 USD | 46,190,000.00 USD | 673,540.00 USD | 284,010.00 USD | 854,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 121,540,000.00 USD | 121,540,000.00 USD | 639,910.00 USD | 895,200.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 102,990.00 USD | 430,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 47,940,000.00 USD | 47,940,000.00 USD | 303,010.00 USD | 454,190.00 USD | 998,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 122,700,000.00 USD | 122,700,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 48,700,000.00 USD | 48,700,000.00 USD | 584,100.00 USD | 166,940.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 122,820,000.00 USD | 122,820,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 48,730,000.00 USD | 48,730,000.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 124,900,000.00 USD | 124,900,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 50,510,000.00 USD | 50,510,000.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 125,330,000.00 USD | 125,330,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 54,460,000.00 USD | 54,460,000.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 134,960,000.00 USD | 134,960,000.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 1,550.00 USD | 432,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 59,360,000.00 USD | 59,360,000.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 136,190,000.00 USD | 136,190,000.00 USD | 209,360.00 USD | 393,370.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 60,090,000.00 USD | 60,090,000.00 USD | 344,680.00 USD | 422.50 USD | 383,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 137,430,000.00 USD | 137,430,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 60,770,000.00 USD | 60,770,000.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 138,690,000.00 USD | 138,690,000.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 62,940,000.00 USD | 62,940,000.00 USD | 602,010.00 USD | 912,930.00 USD | 659,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 141,210,000.00 USD | 141,210,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 63,650,000.00 USD | 63,650,000.00 USD | 188,510.00 USD | 202,150.00 USD | 319,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 4,310.00 USD | 436,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 64,780,000.00 USD | 64,780,000.00 USD | 493,480.00 USD | 313,760.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 144,210,000.00 USD | 144,210,000.00 USD | 2,140,000.00 USD | 178,660.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 67,290,000.00 USD | 67,290,000.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 147,990,000.00 USD | 147,990,000.00 USD | 1,480,000.00 USD | 590,530.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 69,870,000.00 USD | 69,870,000.00 USD | 908,870.00 USD | 396,100.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 151,230,000.00 USD | 151,230,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 72,950,000.00 USD | 72,950,000.00 USD | 1,800,000.00 USD | 538,960.00 USD | 745,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 154,080,000.00 USD | 154,080,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 74,670,000.00 USD | 74,670,000.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 156,540,000.00 USD | 156,540,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,700.00 USD | 438,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 80,530,000.00 USD | 80,530,000.00 USD | 222,150.00 USD | 1,720,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 161,160,000.00 USD | 161,160,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 87,330,000.00 USD | 87,330,000.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 164,240,000.00 USD | 164,240,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 90,730,000.00 USD | 90,730,000.00 USD | 1,680,000.00 USD | 689,260.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 166,070,000.00 USD | 166,070,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 95,370,000.00 USD | 95,370,000.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 170,530,000.00 USD | 170,530,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 98,410,000.00 USD | 98,410,000.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 172,900,000.00 USD | 172,900,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 46,520.00 USD | 484,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 100,700,000.00 USD | 100,700,000.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 173,430,000.00 USD | 173,430,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 102,890,000.00 USD | 102,890,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 174,590,000.00 USD | 174,590,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,330,000.00 USD | 105,330,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 176,310,000.00 USD | 176,310,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,590,000.00 USD | 107,590,000.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 180,360,000.00 USD | 180,360,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 109,920,000.00 USD | 109,920,000.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 180,900,000.00 USD | 180,900,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 3,460.00 USD | 488,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 112,360,000.00 USD | 112,360,000.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 182,850,000.00 USD | 182,850,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 115,040,000.00 USD | 115,040,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 185,200,000.00 USD | 185,200,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,680,000.00 USD | 117,680,000.00 USD | 1,020,000.00 USD | 389,350.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 189,900,000.00 USD | 189,900,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 121,280,000.00 USD | 121,280,000.00 USD | 1,630,000.00 USD | 761,510.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 195,580,000.00 USD | 195,580,000.00 USD | 1,730,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 124,540,000.00 USD | 124,540,000.00 USD | 1,470,000.00 USD | 626,040.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 206,640,000.00 USD | 206,640,000.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 1,920.00 USD | 490,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,850,000.00 USD | 125,850,000.00 USD | 498,430.00 USD | 331,800.00 USD | 481,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 213,800,000.00 USD | 213,800,000.00 USD | 2,430,000.00 USD | 2,230,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 127,120,000.00 USD | 127,120,000.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 224,110,000.00 USD | 224,110,000.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 128,610,000.00 USD | 128,610,000.00 USD | 771,840.00 USD | 230,360.00 USD | 488,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 231,880,000.00 USD | 231,880,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 129,930,000.00 USD | 129,930,000.00 USD | 558,120.00 USD | 207,050.00 USD | 556,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 240,210,000.00 USD | 240,210,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 131,400,000.00 USD | 131,400,000.00 USD | 503,350.00 USD | 214,770.00 USD | 753,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 248,440,000.00 USD | 248,440,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 23,410.00 USD | 513,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 132,660,000.00 USD | 132,660,000.00 USD | 510,040.00 USD | 138,360.00 USD | 608,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 252,530,000.00 USD | 252,530,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 133,520,000.00 USD | 133,520,000.00 USD | 412,060.00 USD | 41,890.00 USD | 413,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 256,320,000.00 USD | 256,320,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,140,000.00 USD | 134,140,000.00 USD | 266,880.00 USD | 118,570.00 USD | 233,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 258,450,000.00 USD | 258,450,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,810,000.00 USD | 134,810,000.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 262,550,000.00 USD | 262,550,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,950,000.00 USD | 134,950,000.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 264,270,000.00 USD | 264,270,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 255,670.00 USD | 769,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,140,000.00 USD | 135,140,000.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 264,760,000.00 USD | 264,760,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,380,000.00 USD | 135,380,000.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 266,180,000.00 USD | 266,180,000.00 USD | 538,230.00 USD | 136,720.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,550,000.00 USD | 135,550,000.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 267,360,000.00 USD | 267,360,000.00 USD | 345,700.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,690,000.00 USD | 135,690,000.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 269,980,000.00 USD | 269,980,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,830,000.00 USD | 135,830,000.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 271,580,000.00 USD | 271,580,000.00 USD | 536,130.00 USD | 294,500.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,090,000.00 USD | 136,090,000.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 273,130,000.00 USD | 273,130,000.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,590,000.00 USD | 136,590,000.00 USD | 231,710.00 USD | 71,930.00 USD | 195,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 275,070,000.00 USD | 275,070,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,070,000.00 USD | 137,070,000.00 USD | 162,970.00 USD | 97,690.00 USD | 224,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 277,620,000.00 USD | 277,620,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,270,000.00 USD | 137,270,000.00 USD | 79,200.00 USD | 23,150.00 USD | 90,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 278,700,000.00 USD | 278,700,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,450,000.00 USD | 137,450,000.00 USD | 131,770.00 USD | 0.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 279,800,000.00 USD | 279,800,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 770,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,490,000.00 USD | 137,490,000.00 USD | 7,260.00 USD | 35,700.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 280,340,000.00 USD | 280,340,000.00 USD | 86,820.00 USD | 248,490.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,540,000.00 USD | 137,540,000.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 281,440,000.00 USD | 281,440,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 281,600,000.00 USD | 281,600,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,540,000.00 USD | 137,540,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 281,930,000.00 USD | 281,930,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,600,000.00 USD | 137,600,000.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 282,100,000.00 USD | 282,100,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,640.00 USD | 782,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 137,670,000.00 USD | 137,670,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 282,220,000.00 USD | 282,220,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 137,800,000.00 USD | 137,800,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 282,230,000.00 USD | 282,230,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 282,360,000.00 USD | 282,360,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 282,480,000.00 USD | 282,480,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 137,820,000.00 USD | 137,820,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 282,720,000.00 USD | 282,720,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 5,310.00 USD | 787,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 282,890,000.00 USD | 282,890,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 137,890,000.00 USD | 137,890,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 283,270,000.00 USD | 283,270,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 138,270,000.00 USD | 138,270,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 283,920,000.00 USD | 283,920,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 138,390,000.00 USD | 138,390,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 284,090,000.00 USD | 284,090,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 138,400,000.00 USD | 138,400,000.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 284,710,000.00 USD | 284,710,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,400.00 USD | 790,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 138,560,000.00 USD | 138,560,000.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 285,240,000.00 USD | 285,240,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 138,940,000.00 USD | 138,940,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 286,260,000.00 USD | 286,260,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 139,680,000.00 USD | 139,680,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 287,640,000.00 USD | 287,640,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 140,110,000.00 USD | 140,110,000.00 USD | 154,900.00 USD | 92,570.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 140,190,000.00 USD | 140,190,000.00 USD | 9,670.00 USD | 54,510.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 288,270,000.00 USD | 288,270,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 288,630,000.00 USD | 288,630,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,140.00 USD | 883,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 289,640,000.00 USD | 289,640,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 291,150,000.00 USD | 291,150,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 292,540,000.00 USD | 292,540,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 293,340,000.00 USD | 293,340,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 293,870,000.00 USD | 293,870,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 258.30 USD | 884,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 294,220,000.00 USD | 294,220,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 294,680,000.00 USD | 294,680,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 295,390,000.00 USD | 295,390,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 295,760,000.00 USD | 295,760,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 295,890,000.00 USD | 295,890,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 296,020,000.00 USD | 296,020,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 296,360,000.00 USD | 296,360,000.00 USD | 70,540.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 296,970,000.00 USD | 296,970,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 297,540,000.00 USD | 297,540,000.00 USD | 186,430.00 USD | 128,180.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 298,000,000.00 USD | 298,000,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 1,590.00 USD | 885,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.46` | 298,160,000.00 USD | 298,160,000.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 298,630,000.00 USD | 298,630,000.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 298,840,000.00 USD | 298,840,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 28,460.00 USD | 914,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 11,470.00 USD | 925,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 128,990.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 468,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 1,600.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 776.71 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,130.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 6,800.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,420.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 599.17 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 133,590.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 177.55 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 2,130.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 4,530,000.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,280.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 1,680.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 5,310,000.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,970.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 20,140.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 128.45 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 534.24 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,980,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 870.87 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 308,670.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 13,110.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 794.73 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 3,120,000.00 USD | 18,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 9,960.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,680.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 2,920.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 404,290.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 122.10 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,710,000.00 USD | 24,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 6,230.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 2,050.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 251,210.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 747.25 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 259.55 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,630.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 627.77 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.43 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 47,420.00 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 75,930.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 205.62 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 4,980.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 214.22 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 155,670.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 104.65 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 2,760.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 11,900.00 USD | 25,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,550.00 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 114.90 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 146.01 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 108.79 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 109.71 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 57,050.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 591.63 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 3,710.00 USD | 25,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 282,730.00 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 171.85 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 70,900,000.00 USD | 0.00 USD | 354.96 USD | `-79.39%` | `1,392.00` |
| `Live` | `Long` | `0.2650` | 70,900,000.00 USD | 0.00 USD | 25,040.00 USD | `-78.58%` | `94,507.00` |
| `Live` | `Long` | `0.2750` | 70,880,000.00 USD | 0.00 USD | 2,740.00 USD | `-77.77%` | `9,956.00` |
| `Live` | `Long` | `0.2850` | 70,880,000.00 USD | 0.00 USD | 6,670.00 USD | `-76.97%` | `23,409.00` |
| `Live` | `Long` | `0.2950` | 70,870,000.00 USD | 0.00 USD | 14,270.00 USD | `-76.16%` | `48,379.00` |
| `Live` | `Long` | `0.3050` | 70,850,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.35%` | `4,526.00` |
| `Live` | `Long` | `0.3150` | 70,850,000.00 USD | 0.00 USD | 4,910.00 USD | `-74.54%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 70,850,000.00 USD | 0.00 USD | 114,130.00 USD | `-73.73%` | `351,158.00` |
| `Live` | `Long` | `0.3350` | 70,730,000.00 USD | 0.00 USD | 708.53 USD | `-72.92%` | `2,115.00` |
| `Live` | `Long` | `0.3450` | 70,730,000.00 USD | 0.00 USD | 12,510.00 USD | `-72.12%` | `36,260.00` |
| `Live` | `Long` | `0.3550` | 70,720,000.00 USD | 0.00 USD | 30,620.00 USD | `-71.31%` | `86,246.00` |
| `Live` | `Long` | `0.3650` | 70,690,000.00 USD | 0.00 USD | 17,450.00 USD | `-70.50%` | `47,796.00` |
| `Live` | `Long` | `0.3750` | 70,670,000.00 USD | 0.00 USD | 421.88 USD | `-69.69%` | `1,125.00` |
| `Live` | `Long` | `0.3850` | 70,670,000.00 USD | 0.00 USD | 346.88 USD | `-68.88%` | `901.00` |
| `Live` | `Long` | `0.3950` | 70,670,000.00 USD | 0.00 USD | 174.59 USD | `-68.08%` | `442.00` |
| `Live` | `Long` | `0.4050` | 70,670,000.00 USD | 0.00 USD | 530,350.00 USD | `-67.27%` | `1,309,498.00` |
| `Live` | `Long` | `0.4350` | 70,140,000.00 USD | 0.00 USD | 7,840.00 USD | `-64.84%` | `18,023.00` |
| `Live` | `Long` | `0.4450` | 70,130,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-64.03%` | `4,965,142.00` |
| `Live` | `Long` | `0.4550` | 67,920,000.00 USD | 0.00 USD | 1,600.00 USD | `-63.23%` | `3,523.00` |
| `Live` | `Long` | `0.4650` | 67,920,000.00 USD | 0.00 USD | 551.96 USD | `-62.42%` | `1,187.00` |
| `Live` | `Long` | `0.4850` | 67,920,000.00 USD | 0.00 USD | 1,930.00 USD | `-60.80%` | `3,971.00` |
| `Live` | `Long` | `0.4950` | 67,920,000.00 USD | 0.00 USD | 63,660.00 USD | `-59.99%` | `128,596.00` |
| `Live` | `Long` | `0.5050` | 67,860,000.00 USD | 0.00 USD | 6,260.00 USD | `-59.19%` | `12,395.00` |
| `Live` | `Long` | `0.5150` | 67,850,000.00 USD | 0.00 USD | 2,890.00 USD | `-58.38%` | `5,606.00` |
| `Live` | `Long` | `0.5250` | 67,850,000.00 USD | 0.00 USD | 1,780.00 USD | `-57.57%` | `3,400.00` |
| `Live` | `Long` | `0.5350` | 67,850,000.00 USD | 0.00 USD | 588.50 USD | `-56.76%` | `1,100.00` |
| `Live` | `Long` | `0.5450` | 67,850,000.00 USD | 0.00 USD | 7,290.00 USD | `-55.95%` | `13,376.00` |
| `Live` | `Long` | `0.5550` | 67,840,000.00 USD | 0.00 USD | 633.26 USD | `-55.14%` | `1,141.00` |
| `Live` | `Long` | `0.5650` | 67,840,000.00 USD | 0.00 USD | 3,540.00 USD | `-54.34%` | `6,270.00` |
| `Live` | `Long` | `0.5750` | 67,830,000.00 USD | 0.00 USD | 8,870.00 USD | `-53.53%` | `15,431.00` |
| `Live` | `Long` | `0.5850` | 67,820,000.00 USD | 0.00 USD | 168,060.00 USD | `-52.72%` | `287,275.00` |
| `Live` | `Long` | `0.5950` | 67,660,000.00 USD | 0.00 USD | 2,980.00 USD | `-51.91%` | `5,015.00` |
| `Live` | `Long` | `0.6050` | 67,650,000.00 USD | 0.00 USD | 29,530.00 USD | `-51.10%` | `48,804.00` |
| `Live` | `Long` | `0.6150` | 67,620,000.00 USD | 0.00 USD | 32,370.00 USD | `-50.29%` | `52,627.00` |
| `Live` | `Long` | `0.6250` | 67,590,000.00 USD | 0.00 USD | 1,130.00 USD | `-49.49%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 67,590,000.00 USD | 0.00 USD | 22,110.00 USD | `-48.68%` | `34,821.00` |
| `Live` | `Long` | `0.6450` | 67,570,000.00 USD | 0.00 USD | 1,560.00 USD | `-47.87%` | `2,412.00` |
| `Live` | `Long` | `0.6550` | 67,570,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.06%` | `1,579.00` |
| `Live` | `Long` | `0.6650` | 67,570,000.00 USD | 0.00 USD | 15,700.00 USD | `-46.25%` | `23,602.00` |
| `Live` | `Long` | `0.6750` | 67,550,000.00 USD | 0.00 USD | 30,110.00 USD | `-45.45%` | `44,612.00` |
| `Live` | `Long` | `0.6850` | 67,520,000.00 USD | 0.00 USD | 21,150.00 USD | `-44.64%` | `30,869.00` |
| `Live` | `Long` | `0.6950` | 67,500,000.00 USD | 0.00 USD | 7,810.00 USD | `-43.83%` | `11,236.00` |
| `Live` | `Long` | `0.7050` | 67,490,000.00 USD | 0.00 USD | 28,070.00 USD | `-43.02%` | `39,817.00` |
| `Live` | `Long` | `0.7150` | 67,460,000.00 USD | 0.00 USD | 67,440.00 USD | `-42.21%` | `94,326.00` |
| `Live` | `Long` | `0.7250` | 67,400,000.00 USD | 0.00 USD | 244,720.00 USD | `-41.40%` | `337,538.00` |
| `Live` | `Long` | `0.7350` | 67,150,000.00 USD | 0.00 USD | 21,910.00 USD | `-40.60%` | `29,816.00` |
| `Live` | `Long` | `0.7450` | 67,130,000.00 USD | 0.00 USD | 62,010.00 USD | `-39.79%` | `83,239.00` |
| `Live` | `Long` | `0.7550` | 67,070,000.00 USD | 0.00 USD | 107,370.00 USD | `-38.98%` | `142,217.00` |
| `Live` | `Long` | `0.7650` | 66,960,000.00 USD | 0.00 USD | 218,080.00 USD | `-38.17%` | `285,075.00` |
| `Live` | `Long` | `0.7750` | 66,740,000.00 USD | 0.00 USD | 5,760.00 USD | `-37.36%` | `7,427.00` |
| `Live` | `Long` | `0.7850` | 66,740,000.00 USD | 0.00 USD | 27,790.00 USD | `-36.56%` | `35,403.00` |
| `Live` | `Long` | `0.7950` | 66,710,000.00 USD | 0.00 USD | 12,080.00 USD | `-35.75%` | `15,195.00` |
| `Live` | `Long` | `0.8050` | 66,700,000.00 USD | 0.00 USD | 23,890.00 USD | `-34.94%` | `29,676.00` |
| `Live` | `Long` | `0.8150` | 66,670,000.00 USD | 0.00 USD | 14,900.00 USD | `-34.13%` | `18,284.00` |
| `Live` | `Long` | `0.8250` | 66,660,000.00 USD | 0.00 USD | 55,220.00 USD | `-33.32%` | `66,938.00` |
| `Live` | `Long` | `0.8350` | 66,600,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-32.51%` | `3,597,985.00` |
| `Live` | `Long` | `0.8450` | 63,600,000.00 USD | 0.00 USD | 283,660.00 USD | `-31.71%` | `335,694.00` |
| `Live` | `Long` | `0.8550` | 63,310,000.00 USD | 0.00 USD | 72,590.00 USD | `-30.90%` | `84,898.00` |
| `Live` | `Long` | `0.8650` | 63,240,000.00 USD | 0.00 USD | 6,060.00 USD | `-30.09%` | `7,005.00` |
| `Live` | `Long` | `0.8750` | 63,240,000.00 USD | 0.00 USD | 85,730.00 USD | `-29.28%` | `97,974.00` |
| `Live` | `Long` | `0.8850` | 63,150,000.00 USD | 0.00 USD | 371,120.00 USD | `-28.47%` | `419,341.00` |
| `Live` | `Long` | `0.8950` | 62,780,000.00 USD | 0.00 USD | 102,690.00 USD | `-27.67%` | `114,739.00` |
| `Live` | `Long` | `0.9050` | 62,680,000.00 USD | 0.00 USD | 148,850.00 USD | `-26.86%` | `164,474.00` |
| `Live` | `Long` | `0.9150` | 62,530,000.00 USD | 0.00 USD | 50,060.00 USD | `-26.05%` | `54,713.00` |
| `Live` | `Long` | `0.9250` | 62,480,000.00 USD | 0.00 USD | 147,510.00 USD | `-25.24%` | `159,475.00` |
| `Live` | `Long` | `0.9350` | 62,330,000.00 USD | 0.00 USD | 87,100.00 USD | `-24.43%` | `93,153.00` |
| `Live` | `Long` | `0.9450` | 62,240,000.00 USD | 0.00 USD | 97,300.00 USD | `-23.62%` | `102,963.00` |
| `Live` | `Long` | `0.9550` | 62,150,000.00 USD | 0.00 USD | 116,510.00 USD | `-22.82%` | `121,996.00` |
| `Live` | `Long` | `0.9650` | 62,030,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-22.01%` | `35,150,501.00` |
| `Live` | `Long` | `0.9750` | 28,110,000.00 USD | 0.00 USD | 158,540.00 USD | `-21.20%` | `162,607.00` |
| `Live` | `Long` | `0.9850` | 27,950,000.00 USD | 0.00 USD | 450,730.00 USD | `-20.39%` | `457,598.00` |
| `Live` | `Long` | `0.9950` | 27,500,000.00 USD | 0.00 USD | 98,040.00 USD | `-19.58%` | `98,536.00` |
| `Live` | `Long` | `1.00` | 27,400,000.00 USD | 0.00 USD | 451,390.00 USD | `-18.77%` | `449,144.00` |
| `Live` | `Long` | `1.01` | 26,950,000.00 USD | 0.00 USD | 181,040.00 USD | `-17.97%` | `178,361.00` |
| `Live` | `Long` | `1.02` | 26,770,000.00 USD | 0.00 USD | 3,440,000.00 USD | `-17.16%` | `3,352,579.00` |
| `Live` | `Long` | `1.03` | 23,330,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-16.35%` | `2,044,058.00` |
| `Live` | `Long` | `1.04` | 21,220,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-15.54%` | `1,228,581.00` |
| `Live` | `Long` | `1.05` | 19,930,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-14.73%` | `1,069,141.00` |
| `Live` | `Long` | `1.06` | 18,800,000.00 USD | 0.00 USD | 532,180.00 USD | `-13.93%` | `499,701.00` |
| `Live` | `Long` | `1.07` | 18,270,000.00 USD | 0.00 USD | 440,750.00 USD | `-13.12%` | `409,998.00` |
| `Live` | `Long` | `1.08` | 17,830,000.00 USD | 0.00 USD | 758,070.00 USD | `-12.31%` | `698,686.00` |
| `Live` | `Long` | `1.09` | 17,070,000.00 USD | 0.00 USD | 603,690.00 USD | `-11.50%` | `551,316.00` |
| `Live` | `Long` | `1.10` | 16,470,000.00 USD | 0.00 USD | 65,590.00 USD | `-10.69%` | `59,353.00` |
| `Live` | `Long` | `1.11` | 16,400,000.00 USD | 0.00 USD | 249,040.00 USD | `-9.88%` | `223,353.00` |
| `Live` | `Long` | `1.12` | 16,160,000.00 USD | 0.00 USD | 267,340.00 USD | `-9.08%` | `237,638.00` |
| `Live` | `Long` | `1.14` | 15,890,000.00 USD | 0.00 USD | 215,570.00 USD | `-8.27%` | `189,933.00` |
| `Live` | `Long` | `1.15` | 15,670,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-7.46%` | `1,491,595.00` |
| `Live` | `Long` | `1.16` | 13,960,000.00 USD | 0.00 USD | 482,060.00 USD | `-6.65%` | `417,368.00` |
| `Live` | `Long` | `1.17` | 13,480,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-5.84%` | `1,294,842.00` |
| `Live` | `Long` | `1.18` | 11,970,000.00 USD | 0.00 USD | 481,590.00 USD | `-5.04%` | `409,867.00` |
| `Live` | `Long` | `1.19` | 11,490,000.00 USD | 0.00 USD | 741,690.00 USD | `-4.23%` | `625,902.00` |
| `Live` | `Long` | `1.20` | 10,750,000.00 USD | 0.00 USD | 379,860.00 USD | `-3.42%` | `317,875.00` |
| `Live` | `Long` | `1.21` | 10,370,000.00 USD | 0.00 USD | 9,230,000.00 USD | `-2.61%` | `7,663,579.00` |
| `Live` | `Long` | `1.22` | 1,140,000.00 USD | 0.00 USD | 710,620.00 USD | `-1.80%` | `584,872.00` |
| `Live` | `Long` | `1.23` | 425,740.00 USD | 0.00 USD | 421,580.00 USD | `-0.99%` | `344,143.00` |
| `Live` | `Long` | `1.24` | 4,170.00 USD | 0.00 USD | 4,170.00 USD | `-0.19%` | `3,373.00` |
| `Live` | `Short` | `1.25` | 8,790.00 USD | 8,790.00 USD | 0.00 USD | `+0.62%` | `7,061.00` |
| `Live` | `Short` | `1.25` | 48,360.00 USD | 39,570.00 USD | 0.00 USD | `+1.43%` | `31,530.00` |
| `Live` | `Short` | `1.26` | 93,480.00 USD | 45,120.00 USD | 0.00 USD | `+2.24%` | `35,671.00` |
| `Live` | `Short` | `1.27` | 327,630.00 USD | 234,140.00 USD | 0.00 USD | `+3.05%` | `183,641.00` |
| `Live` | `Short` | `1.28` | 430,620.00 USD | 102,990.00 USD | 0.00 USD | `+3.86%` | `80,151.00` |
| `Live` | `Short` | `1.29` | 432,180.00 USD | 1,550.00 USD | 0.00 USD | `+4.66%` | `1,200.00` |
| `Live` | `Short` | `1.30` | 436,480.00 USD | 4,310.00 USD | 0.00 USD | `+5.47%` | `3,300.00` |
| `Live` | `Short` | `1.31` | 438,180.00 USD | 1,700.00 USD | 0.00 USD | `+6.28%` | `1,292.00` |
| `Live` | `Short` | `1.32` | 484,710.00 USD | 46,520.00 USD | 0.00 USD | `+7.09%` | `35,113.00` |
| `Live` | `Short` | `1.33` | 488,160.00 USD | 3,460.00 USD | 0.00 USD | `+7.90%` | `2,589.00` |
| `Live` | `Short` | `1.34` | 490,090.00 USD | 1,920.00 USD | 0.00 USD | `+8.70%` | `1,431.00` |
| `Live` | `Short` | `1.35` | 513,500.00 USD | 23,410.00 USD | 0.00 USD | `+9.51%` | `17,276.00` |
| `Live` | `Short` | `1.36` | 769,170.00 USD | 255,670.00 USD | 0.00 USD | `+10.32%` | `187,304.00` |
| `Live` | `Short` | `1.39` | 770,440.00 USD | 1,280.00 USD | 0.00 USD | `+11.94%` | `921.00` |
| `Live` | `Short` | `1.40` | 782,080.00 USD | 11,640.00 USD | 0.00 USD | `+12.75%` | `8,341.00` |
| `Live` | `Short` | `1.41` | 787,390.00 USD | 5,310.00 USD | 0.00 USD | `+13.55%` | `3,782.00` |
| `Live` | `Short` | `1.42` | 790,790.00 USD | 3,400.00 USD | 0.00 USD | `+14.36%` | `2,403.00` |
| `Live` | `Short` | `1.43` | 883,930.00 USD | 93,140.00 USD | 0.00 USD | `+15.17%` | `65,362.00` |
| `Live` | `Short` | `1.44` | 884,190.00 USD | 258.30 USD | 0.00 USD | `+15.98%` | `180.00` |
| `Live` | `Short` | `1.46` | 885,780.00 USD | 1,590.00 USD | 0.00 USD | `+17.59%` | `1,090.00` |
| `Live` | `Short` | `1.47` | 914,240.00 USD | 28,460.00 USD | 0.00 USD | `+18.40%` | `19,428.00` |
| `Live` | `Short` | `1.48` | 925,710.00 USD | 11,470.00 USD | 0.00 USD | `+19.21%` | `7,778.00` |
| `Live` | `Short` | `1.49` | 1,050,000.00 USD | 128,990.00 USD | 0.00 USD | `+20.02%` | `86,861.00` |
| `Live` | `Short` | `1.50` | 1,070,000.00 USD | 11,950.00 USD | 0.00 USD | `+20.83%` | `7,994.00` |
| `Live` | `Short` | `1.51` | 1,530,000.00 USD | 468,000.00 USD | 0.00 USD | `+22.44%` | `308,913.00` |
| `Live` | `Short` | `1.52` | 1,540,000.00 USD | 1,600.00 USD | 0.00 USD | `+23.25%` | `1,052.00` |
| `Live` | `Short` | `1.53` | 1,540,000.00 USD | 776.71 USD | 0.00 USD | `+24.06%` | `506.00` |
| `Live` | `Short` | `1.54` | 1,540,000.00 USD | 2,130.00 USD | 0.00 USD | `+24.87%` | `1,377.00` |
| `Live` | `Short` | `1.55` | 1,550,000.00 USD | 6,800.00 USD | 0.00 USD | `+25.68%` | `4,373.00` |
| `Live` | `Short` | `1.56` | 1,550,000.00 USD | 555.57 USD | 0.00 USD | `+26.49%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,550,000.00 USD | 2,420.00 USD | 0.00 USD | `+27.29%` | `1,539.00` |
| `Live` | `Short` | `1.58` | 1,550,000.00 USD | 123.63 USD | 0.00 USD | `+28.10%` | `78.00` |
| `Live` | `Short` | `1.61` | 1,550,000.00 USD | 599.17 USD | 0.00 USD | `+30.53%` | `371.00` |
| `Live` | `Short` | `1.62` | 1,550,000.00 USD | 271.38 USD | 0.00 USD | `+31.33%` | `167.00` |
| `Live` | `Short` | `1.64` | 1,560,000.00 USD | 11,270.00 USD | 0.00 USD | `+32.14%` | `6,892.00` |
| `Live` | `Short` | `1.65` | 1,690,000.00 USD | 133,590.00 USD | 0.00 USD | `+32.95%` | `81,210.00` |
| `Live` | `Short` | `1.66` | 1,690,000.00 USD | 147.30 USD | 0.00 USD | `+33.76%` | `89.00` |
| `Live` | `Short` | `1.67` | 1,700,000.00 USD | 586.08 USD | 0.00 USD | `+34.57%` | `352.00` |
| `Live` | `Short` | `1.68` | 1,700,000.00 USD | 177.55 USD | 0.00 USD | `+35.38%` | `106.00` |
| `Live` | `Short` | `1.69` | 1,700,000.00 USD | 4,180.00 USD | 0.00 USD | `+36.18%` | `2,483.00` |
| `Live` | `Short` | `1.70` | 1,700,000.00 USD | 2,130.00 USD | 0.00 USD | `+36.99%` | `1,256.00` |
| `Live` | `Short` | `1.71` | 1,700,000.00 USD | 1,980.00 USD | 0.00 USD | `+37.80%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 6,230,000.00 USD | 4,530,000.00 USD | 0.00 USD | `+39.42%` | `2,626,058.00` |
| `Live` | `Short` | `1.74` | 6,240,000.00 USD | 2,970.00 USD | 0.00 USD | `+40.22%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,240,000.00 USD | 2,730.00 USD | 0.00 USD | `+41.03%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 6,240,000.00 USD | 1,280.00 USD | 0.00 USD | `+41.84%` | `727.00` |
| `Live` | `Short` | `1.76` | 6,240,000.00 USD | 1,680.00 USD | 0.00 USD | `+42.65%` | `952.00` |
| `Live` | `Short` | `1.77` | 11,550,000.00 USD | 5,310,000.00 USD | 0.00 USD | `+43.46%` | `2,990,580.00` |
| `Live` | `Short` | `1.78` | 11,680,000.00 USD | 129,540.00 USD | 0.00 USD | `+44.27%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,680,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.07%` | `2,211.00` |
| `Live` | `Short` | `1.80` | 11,690,000.00 USD | 889.87 USD | 0.00 USD | `+45.88%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,710,000.00 USD | 20,140.00 USD | 0.00 USD | `+46.69%` | `11,096.00` |
| `Live` | `Short` | `1.82` | 11,710,000.00 USD | 260.98 USD | 0.00 USD | `+47.50%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,710,000.00 USD | 128.45 USD | 0.00 USD | `+48.31%` | `70.00` |
| `Live` | `Short` | `1.84` | 11,720,000.00 USD | 9,340.00 USD | 0.00 USD | `+49.12%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,720,000.00 USD | 534.24 USD | 0.00 USD | `+49.92%` | `288.00` |
| `Live` | `Short` | `1.86` | 14,690,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+50.73%` | `1,595,959.00` |
| `Live` | `Short` | `1.89` | 14,690,000.00 USD | 870.87 USD | 0.00 USD | `+52.35%` | `462.00` |
| `Live` | `Short` | `1.90` | 15,000,000.00 USD | 308,670.00 USD | 0.00 USD | `+53.16%` | `162,888.00` |
| `Live` | `Short` | `1.91` | 15,010,000.00 USD | 13,110.00 USD | 0.00 USD | `+53.96%` | `6,882.00` |
| `Live` | `Short` | `1.92` | 15,020,000.00 USD | 794.73 USD | 0.00 USD | `+54.77%` | `415.00` |
| `Live` | `Short` | `1.93` | 18,140,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+55.58%` | `1,622,843.00` |
| `Live` | `Short` | `1.94` | 18,150,000.00 USD | 9,960.00 USD | 0.00 USD | `+56.39%` | `5,145.00` |
| `Live` | `Short` | `1.96` | 18,150,000.00 USD | 293.25 USD | 0.00 USD | `+58.01%` | `150.00` |
| `Live` | `Short` | `1.97` | 18,380,000.00 USD | 227,680.00 USD | 0.00 USD | `+58.81%` | `115,869.00` |
| `Live` | `Short` | `1.98` | 18,380,000.00 USD | 2,920.00 USD | 0.00 USD | `+59.62%` | `1,478.00` |
| `Live` | `Short` | `2.02` | 18,780,000.00 USD | 404,290.00 USD | 0.00 USD | `+62.85%` | `200,642.00` |
| `Live` | `Short` | `2.04` | 18,780,000.00 USD | 122.10 USD | 0.00 USD | `+64.47%` | `60.00` |
| `Live` | `Short` | `2.04` | 18,790,000.00 USD | 198.36 USD | 0.00 USD | `+65.28%` | `97.00` |
| `Live` | `Short` | `2.06` | 24,500,000.00 USD | 5,710,000.00 USD | 0.00 USD | `+66.09%` | `2,780,943.00` |
| `Live` | `Short` | `2.06` | 24,510,000.00 USD | 6,230.00 USD | 0.00 USD | `+66.90%` | `3,017.00` |
| `Live` | `Short` | `2.08` | 24,510,000.00 USD | 2,050.00 USD | 0.00 USD | `+67.70%` | `989.00` |
| `Live` | `Short` | `2.10` | 24,510,000.00 USD | 331.01 USD | 0.00 USD | `+69.32%` | `158.00` |
| `Live` | `Short` | `2.10` | 24,510,000.00 USD | 294.70 USD | 0.00 USD | `+70.13%` | `140.00` |
| `Live` | `Short` | `2.12` | 24,760,000.00 USD | 251,210.00 USD | 0.00 USD | `+70.94%` | `118,776.00` |
| `Live` | `Short` | `2.13` | 24,760,000.00 USD | 747.25 USD | 0.00 USD | `+72.55%` | `350.00` |
| `Live` | `Short` | `2.15` | 24,760,000.00 USD | 259.55 USD | 0.00 USD | `+73.36%` | `121.00` |
| `Live` | `Short` | `2.15` | 24,760,000.00 USD | 196.11 USD | 0.00 USD | `+74.17%` | `91.00` |
| `Live` | `Short` | `2.17` | 24,760,000.00 USD | 2,630.00 USD | 0.00 USD | `+75.79%` | `1,207.00` |
| `Live` | `Short` | `2.19` | 24,760,000.00 USD | 100.51 USD | 0.00 USD | `+76.59%` | `46.00` |
| `Live` | `Short` | `2.19` | 24,760,000.00 USD | 627.77 USD | 0.00 USD | `+77.40%` | `286.00` |
| `Live` | `Short` | `2.21` | 24,760,000.00 USD | 101.43 USD | 0.00 USD | `+78.21%` | `46.00` |
| `Live` | `Short` | `2.21` | 24,810,000.00 USD | 47,420.00 USD | 0.00 USD | `+79.02%` | `21,408.00` |
| `Live` | `Short` | `2.23` | 24,890,000.00 USD | 75,930.00 USD | 0.00 USD | `+79.83%` | `34,127.00` |
| `Live` | `Short` | `2.23` | 24,890,000.00 USD | 205.62 USD | 0.00 USD | `+80.64%` | `92.00` |
| `Live` | `Short` | `2.25` | 24,890,000.00 USD | 4,980.00 USD | 0.00 USD | `+81.44%` | `2,218.00` |
| `Live` | `Short` | `2.25` | 24,890,000.00 USD | 214.22 USD | 0.00 USD | `+82.25%` | `95.00` |
| `Live` | `Short` | `2.27` | 25,050,000.00 USD | 155,670.00 USD | 0.00 USD | `+83.06%` | `68,730.00` |
| `Live` | `Short` | `2.27` | 25,050,000.00 USD | 104.65 USD | 0.00 USD | `+83.87%` | `46.00` |
| `Live` | `Short` | `2.29` | 25,050,000.00 USD | 105.57 USD | 0.00 USD | `+85.48%` | `46.00` |
| `Live` | `Short` | `2.31` | 25,050,000.00 USD | 2,760.00 USD | 0.00 USD | `+87.10%` | `1,193.00` |
| `Live` | `Short` | `2.33` | 25,060,000.00 USD | 11,900.00 USD | 0.00 USD | `+87.91%` | `5,119.00` |
| `Live` | `Short` | `2.33` | 25,070,000.00 USD | 1,550.00 USD | 0.00 USD | `+88.72%` | `665.00` |
| `Live` | `Short` | `2.35` | 25,070,000.00 USD | 114.90 USD | 0.00 USD | `+89.53%` | `49.00` |
| `Live` | `Short` | `2.35` | 25,070,000.00 USD | 146.01 USD | 0.00 USD | `+90.33%` | `62.00` |
| `Live` | `Short` | `2.37` | 25,070,000.00 USD | 108.79 USD | 0.00 USD | `+91.14%` | `46.00` |
| `Live` | `Short` | `2.38` | 25,070,000.00 USD | 109.71 USD | 0.00 USD | `+92.76%` | `46.00` |
| `Live` | `Short` | `2.40` | 25,120,000.00 USD | 57,050.00 USD | 0.00 USD | `+93.57%` | `23,820.00` |
| `Live` | `Short` | `2.40` | 25,120,000.00 USD | 591.63 USD | 0.00 USD | `+94.37%` | `246.00` |
| `Live` | `Short` | `2.42` | 25,130,000.00 USD | 3,710.00 USD | 0.00 USD | `+95.99%` | `1,528.00` |
| `Live` | `Short` | `2.44` | 25,410,000.00 USD | 282,730.00 USD | 0.00 USD | `+96.80%` | `116,111.00` |
| `Live` | `Short` | `2.46` | 25,410,000.00 USD | 171.85 USD | 0.00 USD | `+98.42%` | `70.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 7,500,000.00 USD | 0.00 USD | 112.45 USD | `-79.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 7,500,000.00 USD | 0.00 USD | 139.12 USD | `-69.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 7,500,000.00 USD | 0.00 USD | 200.86 USD | `-66.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 7,500,000.00 USD | 0.00 USD | 408.51 USD | `-64.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 7,500,000.00 USD | 0.00 USD | 273.00 USD | `-63.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 7,500,000.00 USD | 0.00 USD | 151.12 USD | `-62.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 7,500,000.00 USD | 0.00 USD | 142.50 USD | `-61.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 7,500,000.00 USD | 0.00 USD | 145.50 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 7,500,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 7,500,000.00 USD | 0.00 USD | 285.82 USD | `-58.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 7,500,000.00 USD | 0.00 USD | 306.60 USD | `-57.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 7,500,000.00 USD | 0.00 USD | 121.55 USD | `-55.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 7,500,000.00 USD | 0.00 USD | 374.60 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 7,500,000.00 USD | 0.00 USD | 100.62 USD | `-52.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 7,500,000.00 USD | 0.00 USD | 791.85 USD | `-48.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 7,500,000.00 USD | 0.00 USD | 573.40 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 7,500,000.00 USD | 0.00 USD | 364.18 USD | `-47.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 7,500,000.00 USD | 0.00 USD | 3,010.00 USD | `-46.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 7,500,000.00 USD | 0.00 USD | 503.55 USD | `-45.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 7,500,000.00 USD | 0.00 USD | 480.19 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 7,490,000.00 USD | 0.00 USD | 11,870.00 USD | `-43.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 7,480,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 7,480,000.00 USD | 0.00 USD | 536.50 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 7,480,000.00 USD | 0.00 USD | 1,300.00 USD | `-38.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 7,480,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 7,480,000.00 USD | 0.00 USD | 878.48 USD | `-35.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 7,470,000.00 USD | 0.00 USD | 798.57 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 7,470,000.00 USD | 0.00 USD | 690.38 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 7,470,000.00 USD | 0.00 USD | 1,060.00 USD | `-28.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 7,470,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 7,470,000.00 USD | 0.00 USD | 838.94 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 7,470,000.00 USD | 0.00 USD | 188.49 USD | `-26.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 7,470,000.00 USD | 0.00 USD | 2,730.00 USD | `-25.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 7,470,000.00 USD | 0.00 USD | 1,180.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 7,460,000.00 USD | 0.00 USD | 112.46 USD | `-23.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 7,460,000.00 USD | 0.00 USD | 2,360.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 7,460,000.00 USD | 0.00 USD | 3,910.00 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 7,460,000.00 USD | 0.00 USD | 546,370.00 USD | `-21.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 6,910,000.00 USD | 0.00 USD | 4,360.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 6,910,000.00 USD | 0.00 USD | 805.95 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 6,910,000.00 USD | 0.00 USD | 15,150.00 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 6,890,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 6,890,000.00 USD | 0.00 USD | 2,020.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 6,880,000.00 USD | 0.00 USD | 38,000.00 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 6,850,000.00 USD | 0.00 USD | 3,490.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 6,840,000.00 USD | 0.00 USD | 2,110.00 USD | `-14.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 6,840,000.00 USD | 0.00 USD | 2,800.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 6,840,000.00 USD | 0.00 USD | 48,080.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 6,790,000.00 USD | 0.00 USD | 3,760.00 USD | `-12.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 6,790,000.00 USD | 0.00 USD | 5,110.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 6,780,000.00 USD | 0.00 USD | 3,650.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 6,780,000.00 USD | 0.00 USD | 9,460.00 USD | `-9.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 6,770,000.00 USD | 0.00 USD | 80,260.00 USD | `-9.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 6,690,000.00 USD | 0.00 USD | 13,830.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 6,670,000.00 USD | 0.00 USD | 15,230.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 6,660,000.00 USD | 0.00 USD | 30,270.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 6,630,000.00 USD | 0.00 USD | 18,740.00 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 6,610,000.00 USD | 0.00 USD | 6,300.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 6,600,000.00 USD | 0.00 USD | 136,710.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 6,470,000.00 USD | 0.00 USD | 12,840.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 6,450,000.00 USD | 0.00 USD | 151,430.00 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 6,300,000.00 USD | 0.00 USD | 131,030.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 6,170,000.00 USD | 0.00 USD | 6,120,000.00 USD | `-0.99%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1.24` | 52,660.00 USD | 0.00 USD | 52,660.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 26,840.00 USD | 22,770.00 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 34,310.00 USD | 7,460.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 6,340,000.00 USD | 6,310,000.00 USD | 0.00 USD | `+3.05%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.28` | 6,360,000.00 USD | 21,440.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 6,370,000.00 USD | 7,760.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 6,390,000.00 USD | 17,230.00 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 6,780,000.00 USD | 393,840.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 6,990,000.00 USD | 204,110.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 7,020,000.00 USD | 34,350.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 7,190,000.00 USD | 167,640.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 7,190,000.00 USD | 907.85 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 7,460,000.00 USD | 275,480.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 7,550,000.00 USD | 82,810.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 7,600,000.00 USD | 49,450.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 7,600,000.00 USD | 6,060.00 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 11,890,000.00 USD | 4,290,000.00 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 11,890,000.00 USD | 1,980.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 11,900,000.00 USD | 10,470.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 11,980,000.00 USD | 80,260.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 12,190,000.00 USD | 203,890.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 12,190,000.00 USD | 7,510.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 12,220,000.00 USD | 23,130.00 USD | 0.00 USD | `+18.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 12,320,000.00 USD | 107,960.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 12,380,000.00 USD | 55,680.00 USD | 0.00 USD | `+20.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 12,390,000.00 USD | 13,980.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 12,430,000.00 USD | 32,340.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 12,440,000.00 USD | 18,000.00 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 12,540,000.00 USD | 93,330.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 12,580,000.00 USD | 45,870.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 12,610,000.00 USD | 22,270.00 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 12,610,000.00 USD | 2,220.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 12,610,000.00 USD | 6,450.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 12,620,000.00 USD | 5,940.00 USD | 0.00 USD | `+27.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 12,630,000.00 USD | 11,620.00 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 12,780,000.00 USD | 148,780.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 12,780,000.00 USD | 1,840.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 12,860,000.00 USD | 80,320.00 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 12,860,000.00 USD | 464.75 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 13,050,000.00 USD | 184,300.00 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 13,050,000.00 USD | 2,670.00 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 13,070,000.00 USD | 18,210.00 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 13,070,000.00 USD | 6,080.00 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 13,090,000.00 USD | 18,400.00 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 13,160,000.00 USD | 70,850.00 USD | 0.00 USD | `+36.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 13,170,000.00 USD | 2,770.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 13,410,000.00 USD | 240,380.00 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 13,420,000.00 USD | 14,030.00 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 13,430,000.00 USD | 5,910.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 13,470,000.00 USD | 44,100.00 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 13,480,000.00 USD | 4,710.00 USD | 0.00 USD | `+41.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 13,480,000.00 USD | 5,510.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 13,500,000.00 USD | 21,720.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 13,630,000.00 USD | 124,420.00 USD | 0.00 USD | `+43.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 13,720,000.00 USD | 96,600.00 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 13,760,000.00 USD | 36,490.00 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 13,760,000.00 USD | 254.51 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 13,760,000.00 USD | 2,530.00 USD | 0.00 USD | `+46.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 13,770,000.00 USD | 1,830.00 USD | 0.00 USD | `+47.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 13,770,000.00 USD | 7,630.00 USD | 0.00 USD | `+48.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 13,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+49.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 13,780,000.00 USD | 8,390.00 USD | 0.00 USD | `+49.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 13,790,000.00 USD | 4,250.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 13,790,000.00 USD | 591.89 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 13,830,000.00 USD | 38,610.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 13,860,000.00 USD | 38,940.00 USD | 0.00 USD | `+53.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 13,870,000.00 USD | 7,410.00 USD | 0.00 USD | `+54.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 13,870,000.00 USD | 265.10 USD | 0.00 USD | `+56.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 13,870,000.00 USD | 2,040.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 13,880,000.00 USD | 1,660.00 USD | 0.00 USD | `+58.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 13,890,000.00 USD | 14,120.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 13,890,000.00 USD | 4,010.00 USD | 0.00 USD | `+59.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 13,890,000.00 USD | 325.54 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 13,900,000.00 USD | 7,020.00 USD | 0.00 USD | `+61.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 14,020,000.00 USD | 122,910.00 USD | 0.00 USD | `+62.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 14,030,000.00 USD | 781.82 USD | 0.00 USD | `+62.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 14,030,000.00 USD | 222.75 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 14,030,000.00 USD | 862.84 USD | 0.00 USD | `+64.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 14,030,000.00 USD | 382.41 USD | 0.00 USD | `+65.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 14,030,000.00 USD | 3,420.00 USD | 0.00 USD | `+66.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 14,030,000.00 USD | 661.93 USD | 0.00 USD | `+67.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 14,160,000.00 USD | 124,400.00 USD | 0.00 USD | `+69.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 14,160,000.00 USD | 1,580.00 USD | 0.00 USD | `+70.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 14,170,000.00 USD | 13,900.00 USD | 0.00 USD | `+71.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 14,200,000.00 USD | 24,840.00 USD | 0.00 USD | `+73.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 14,250,000.00 USD | 50,580.00 USD | 0.00 USD | `+74.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 14,250,000.00 USD | 2,690.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 14,270,000.00 USD | 20,370.00 USD | 0.00 USD | `+77.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 14,420,000.00 USD | 151,380.00 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 14,430,000.00 USD | 7,340.00 USD | 0.00 USD | `+80.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 14,430,000.00 USD | 3,120.00 USD | 0.00 USD | `+83.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 14,430,000.00 USD | 1,140.00 USD | 0.00 USD | `+84.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 14,460,000.00 USD | 25,760.00 USD | 0.00 USD | `+85.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 14,460,000.00 USD | 370.40 USD | 0.00 USD | `+87.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 14,460,000.00 USD | 733.19 USD | 0.00 USD | `+88.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 14,460,000.00 USD | 2,410.00 USD | 0.00 USD | `+91.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 14,460,000.00 USD | 475.00 USD | 0.00 USD | `+91.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 14,460,000.00 USD | 2,540.00 USD | 0.00 USD | `+93.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 14,470,000.00 USD | 721.50 USD | 0.00 USD | `+94.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 14,470,000.00 USD | 2,240.00 USD | 0.00 USD | `+95.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 14,490,000.00 USD | 19,590.00 USD | 0.00 USD | `+95.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 14,490,000.00 USD | 564.92 USD | 0.00 USD | `+96.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 14,500,000.00 USD | 8,110.00 USD | 0.00 USD | `+98.42%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.11` | 63,850,000.00 USD | 0.00 USD | 63,850,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 29,980,000.00 USD | 0.00 USD | 29,980,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD |
| `1D` | `1.11` | 29,840,000.00 USD | 0.00 USD | 29,840,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD |
| `7D` | `1.11` | 63,830,000.00 USD | 0.00 USD | 63,830,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 29,820,000.00 USD | 0.00 USD | 29,820,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD |
| `7D` | `1.12` | 63,820,000.00 USD | 0.00 USD | 63,820,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 29,820,000.00 USD | 0.00 USD | 29,820,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD |
| `1D` | `1.12` | 29,800,000.00 USD | 0.00 USD | 29,800,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD |
| `7D` | `1.12` | 63,740,000.00 USD | 0.00 USD | 63,740,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.13` | 29,760,000.00 USD | 0.00 USD | 29,760,000.00 USD | 0.00 USD | 783.15 USD | 0.00 USD |
| `7D` | `1.13` | 63,740,000.00 USD | 0.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 194,460.00 USD |
| `1D` | `1.13` | 29,750,000.00 USD | 0.00 USD | 29,750,000.00 USD | 0.00 USD | 41,620.00 USD | 76,730.00 USD |
| `7D` | `1.13` | 63,540,000.00 USD | 0.00 USD | 63,540,000.00 USD | 5,450.00 USD | 2,160.00 USD | 3,970.00 USD |
| `7D` | `1.13` | 63,530,000.00 USD | 0.00 USD | 63,530,000.00 USD | 144,660.00 USD | 0.00 USD | 142,970.00 USD |
| `1D` | `1.13` | 29,640,000.00 USD | 0.00 USD | 29,640,000.00 USD | 7,260.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.14` | 63,240,000.00 USD | 0.00 USD | 63,240,000.00 USD | 0.00 USD | 88,050.00 USD | 150,130.00 USD |
| `1D` | `1.14` | 29,630,000.00 USD | 0.00 USD | 29,630,000.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD |
| `7D` | `1.14` | 63,010,000.00 USD | 0.00 USD | 63,010,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `7D` | `1.14` | 62,910,000.00 USD | 0.00 USD | 62,910,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,590,000.00 USD | 0.00 USD | 29,590,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 62,900,000.00 USD | 0.00 USD | 62,900,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,520,000.00 USD | 0.00 USD | 29,520,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 62,830,000.00 USD | 0.00 USD | 62,830,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.14` | 29,450,000.00 USD | 0.00 USD | 29,450,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.15` | 62,710,000.00 USD | 0.00 USD | 62,710,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 62,710,000.00 USD | 0.00 USD | 62,710,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 62,570,000.00 USD | 0.00 USD | 62,570,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 62,210,000.00 USD | 0.00 USD | 62,210,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 29,300,000.00 USD | 0.00 USD | 29,300,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 62,040,000.00 USD | 0.00 USD | 62,040,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.15` | 29,230,000.00 USD | 0.00 USD | 29,230,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.16` | 61,660,000.00 USD | 0.00 USD | 61,660,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 28,850,000.00 USD | 0.00 USD | 28,850,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 61,020,000.00 USD | 0.00 USD | 61,020,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 28,730,000.00 USD | 0.00 USD | 28,730,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 60,220,000.00 USD | 0.00 USD | 60,220,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 28,560,000.00 USD | 0.00 USD | 28,560,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 59,690,000.00 USD | 0.00 USD | 59,690,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 28,180,000.00 USD | 0.00 USD | 28,180,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 58,670,000.00 USD | 0.00 USD | 58,670,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 27,440,000.00 USD | 0.00 USD | 27,440,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 57,290,000.00 USD | 0.00 USD | 57,290,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 27,010,000.00 USD | 0.00 USD | 27,010,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 56,670,000.00 USD | 0.00 USD | 56,670,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 26,680,000.00 USD | 0.00 USD | 26,680,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 55,290,000.00 USD | 0.00 USD | 55,290,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 26,500,000.00 USD | 0.00 USD | 26,500,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 53,780,000.00 USD | 0.00 USD | 53,780,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 26,330,000.00 USD | 0.00 USD | 26,330,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 52,390,000.00 USD | 0.00 USD | 52,390,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 26,120,000.00 USD | 0.00 USD | 26,120,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 51,590,000.00 USD | 0.00 USD | 51,590,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 25,840,000.00 USD | 0.00 USD | 25,840,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 50,710,000.00 USD | 0.00 USD | 50,710,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 25,620,000.00 USD | 0.00 USD | 25,620,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 50,260,000.00 USD | 0.00 USD | 50,260,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 25,440,000.00 USD | 0.00 USD | 25,440,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 49,540,000.00 USD | 0.00 USD | 49,540,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 25,350,000.00 USD | 0.00 USD | 25,350,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 49,170,000.00 USD | 0.00 USD | 49,170,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.18` | 25,270,000.00 USD | 0.00 USD | 25,270,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 49,040,000.00 USD | 0.00 USD | 49,040,000.00 USD | 127,700.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 25,150,000.00 USD | 0.00 USD | 25,150,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD |
| `7D` | `1.19` | 48,520,000.00 USD | 0.00 USD | 48,520,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 24,920,000.00 USD | 0.00 USD | 24,920,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD |
| `7D` | `1.19` | 47,750,000.00 USD | 0.00 USD | 47,750,000.00 USD | 186,430.00 USD | 132,500.00 USD | 282,840.00 USD |
| `1D` | `1.19` | 24,130,000.00 USD | 0.00 USD | 24,130,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD |
| `7D` | `1.19` | 47,150,000.00 USD | 0.00 USD | 47,150,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD |
| `1D` | `1.19` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 40,460.00 USD | 17,640.00 USD | 92,300.00 USD |
| `7D` | `1.19` | 46,460,000.00 USD | 0.00 USD | 46,460,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 23,940,000.00 USD | 0.00 USD | 23,940,000.00 USD | 66,050.00 USD | 221,930.00 USD | 81,030.00 USD |
| `7D` | `1.20` | 45,790,000.00 USD | 0.00 USD | 45,790,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 23,570,000.00 USD | 0.00 USD | 23,570,000.00 USD | 31,180.00 USD | 6,070.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 45,090,000.00 USD | 0.00 USD | 45,090,000.00 USD | 5,350.00 USD | 97,860.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 23,510,000.00 USD | 0.00 USD | 23,510,000.00 USD | 39,940.00 USD | 0.00 USD | 9,050.00 USD |
| `7D` | `1.20` | 44,800,000.00 USD | 0.00 USD | 44,800,000.00 USD | 67,200.00 USD | 57,670.00 USD | 201,810.00 USD |
| `1D` | `1.20` | 23,460,000.00 USD | 0.00 USD | 23,460,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD |
| `7D` | `1.20` | 44,470,000.00 USD | 0.00 USD | 44,470,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD |
| `7D` | `1.20` | 44,390,000.00 USD | 0.00 USD | 44,390,000.00 USD | 202,570.00 USD | 53,170.00 USD | 534,450.00 USD |
| `1D` | `1.20` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 31,120.00 USD | 104,040.00 USD | 191,830.00 USD |
| `7D` | `1.21` | 43,600,000.00 USD | 0.00 USD | 43,600,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `7D` | `1.21` | 43,510,000.00 USD | 0.00 USD | 43,510,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `7D` | `1.21` | 43,410,000.00 USD | 0.00 USD | 43,410,000.00 USD | 468,800.00 USD | 45,260.00 USD | 357,420.00 USD |
| `1D` | `1.21` | 23,120,000.00 USD | 0.00 USD | 23,120,000.00 USD | 135,040.00 USD | 244,960.00 USD | 71,590.00 USD |
| `7D` | `1.21` | 42,540,000.00 USD | 0.00 USD | 42,540,000.00 USD | 180,260.00 USD | 264,440.00 USD | 783,620.00 USD |
| `1D` | `1.21` | 22,670,000.00 USD | 0.00 USD | 22,670,000.00 USD | 419,060.00 USD | 94,800.00 USD | 1,230,000.00 USD |
| `7D` | `1.21` | 41,310,000.00 USD | 0.00 USD | 41,310,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.21` | 20,920,000.00 USD | 0.00 USD | 20,920,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `1.22` | 40,910,000.00 USD | 0.00 USD | 40,910,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD |
| `7D` | `1.22` | 40,730,000.00 USD | 0.00 USD | 40,730,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD |
| `1D` | `1.22` | 20,660,000.00 USD | 0.00 USD | 20,660,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD |
| `7D` | `1.22` | 40,180,000.00 USD | 0.00 USD | 40,180,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 19,970,000.00 USD | 0.00 USD | 19,970,000.00 USD | 157,550.00 USD | 6,840.00 USD | 208,620.00 USD |
| `7D` | `1.22` | 39,880,000.00 USD | 0.00 USD | 39,880,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 19,600,000.00 USD | 0.00 USD | 19,600,000.00 USD | 0.00 USD | 211.25 USD | 47,550.00 USD |
| `7D` | `1.22` | 39,380,000.00 USD | 0.00 USD | 39,380,000.00 USD | 0.00 USD | 191,360.00 USD | 1,020,000.00 USD |
| `1D` | `1.22` | 19,550,000.00 USD | 0.00 USD | 19,550,000.00 USD | 40,080.00 USD | 486,000.00 USD | 1,160,000.00 USD |
| `7D` | `1.23` | 38,170,000.00 USD | 0.00 USD | 38,170,000.00 USD | 627,450.00 USD | 191,250.00 USD | 4,910.00 USD |
| `1D` | `1.23` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 449,150.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `1.23` | 37,350,000.00 USD | 0.00 USD | 37,350,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 48,560.00 USD | 3,920.00 USD | 0.00 USD |
| `7D` | `1.23` | 36,890,000.00 USD | 0.00 USD | 36,890,000.00 USD | 0.00 USD | 917,970.00 USD | 996,580.00 USD |
| `1D` | `1.23` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 191,290.00 USD | 236,160.00 USD | 543,750.00 USD |
| `7D` | `1.23` | 34,970,000.00 USD | 0.00 USD | 34,970,000.00 USD | 782,590.00 USD | 475,720.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 271,900.00 USD | 757,410.00 USD | 0.00 USD |
| `7D` | `1.23` | 33,710,000.00 USD | 0.00 USD | 33,710,000.00 USD | 656,500.00 USD | 135,640.00 USD | 91,200.00 USD |
| `1D` | `1.23` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 86,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.24` | 32,820,000.00 USD | 0.00 USD | 32,820,000.00 USD | 996,240.00 USD | 513,510.00 USD | 29,060.00 USD |
| `7D` | `1.24` | 31,290,000.00 USD | 0.00 USD | 31,290,000.00 USD | 1,640,000.00 USD | 1,110,000.00 USD | 719,360.00 USD |
| `7D` | `1.24` | 27,810,000.00 USD | 0.00 USD | 27,810,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 340,590.00 USD |
| `7D` | `1.24` | 26,040,000.00 USD | 0.00 USD | 26,040,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,940,000.00 USD |
| `1D` | `1.24` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 112,970.00 USD | 0.00 USD | 1,260,000.00 USD |
| `7D` | `1.24` | 22,270,000.00 USD | 0.00 USD | 22,270,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `1.24` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 721,110.00 USD | 0.00 USD | 678,260.00 USD |
| `7D` | `1.25` | 20,360,000.00 USD | 0.00 USD | 20,360,000.00 USD | 2,670,000.00 USD | 0.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 11,010,000.00 USD | 0.00 USD | 11,010,000.00 USD | 861,120.00 USD | 81,840.00 USD | 551,670.00 USD |
| `7D` | `1.25` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 2,330,000.00 USD | 1,140,000.00 USD | 0.00 USD |
| `1D` | `1.25` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 218,430.00 USD | 833,450.00 USD | 2,020,000.00 USD |
| `7D` | `1.25` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 2,720,000.00 USD | 1,770,000.00 USD | 51,920.00 USD |
| `1D` | `1.25` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,170,000.00 USD |
| `7D` | `1.25` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 2,810,000.00 USD | 888,720.00 USD | 44,180.00 USD |
| `1D` | `1.25` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 351,630.00 USD | 0.00 USD | 4,230.00 USD |
| `7D` | `1.25` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 1,240,000.00 USD | 1,460,000.00 USD | 104,700.00 USD |
| `1D` | `1.25` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 551,630.00 USD | 0.00 USD | 6,120.00 USD |
| `7D` | `1.25` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 998,540.00 USD | 441,280.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 1,460,000.00 USD | 760,010.00 USD | 0.00 USD |
| `7D` | `1.26` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 2,180,000.00 USD | 992,480.00 USD | 0.00 USD |
| `7D` | `1.26` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 2,180,000.00 USD | 992,480.00 USD | 0.00 USD |
| `1D` | `1.26` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,030,000.00 USD | 2,680.00 USD | 0.00 USD |
| `1D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 729,530.00 USD | 729,530.00 USD | 0.00 USD | 472,940.00 USD | 246,640.00 USD | 9,950.00 USD |
| `7D` | `1.26` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 485,150.00 USD |
| `1D` | `1.26` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `1.26` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 23,320.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 39,860.00 USD | 1,030,000.00 USD | 82,450.00 USD |
| `7D` | `1.27` | 28,650,000.00 USD | 28,650,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,990,000.00 USD | 8,250,000.00 USD |
| `1D` | `1.27` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 1,280,000.00 USD | 794,130.00 USD |
| `7D` | `1.27` | 33,420,000.00 USD | 33,420,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 780,430.00 USD | 0.00 USD |
| `7D` | `1.27` | 35,340,000.00 USD | 35,340,000.00 USD | 0.00 USD | 178,380.00 USD | 1,620,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 961,090.00 USD | 313,930.00 USD | 57,120.00 USD |
| `7D` | `1.27` | 39,090,000.00 USD | 39,090,000.00 USD | 0.00 USD | 186,960.00 USD | 3,000,000.00 USD | 567,370.00 USD |
| `1D` | `1.27` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 60,090.00 USD | 761,570.00 USD | 1,740,000.00 USD |
| `7D` | `1.27` | 53,470,000.00 USD | 53,470,000.00 USD | 0.00 USD | 4,420,000.00 USD | 1,750,000.00 USD | 8,210,000.00 USD |
| `1D` | `1.28` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 481,200.00 USD | 1,370,000.00 USD | 2,920,000.00 USD |
| `7D` | `1.28` | 71,740,000.00 USD | 71,740,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 6,010,000.00 USD | 2,720,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 77,850,000.00 USD | 77,850,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,750,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 32,390,000.00 USD | 32,390,000.00 USD | 0.00 USD | 188,330.00 USD | 1,630,000.00 USD | 695,980.00 USD |
| `7D` | `1.28` | 78,800,000.00 USD | 78,800,000.00 USD | 0.00 USD | 0.00 USD | 869,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 33,340,000.00 USD | 33,340,000.00 USD | 0.00 USD | 547,110.00 USD | 0.00 USD | 405,670.00 USD |
| `7D` | `1.28` | 79,940,000.00 USD | 79,940,000.00 USD | 0.00 USD | 1,080,000.00 USD | 16,490.00 USD | 45,690.00 USD |
| `1D` | `1.28` | 35,160,000.00 USD | 35,160,000.00 USD | 0.00 USD | 673,540.00 USD | 284,010.00 USD | 854,890.00 USD |
| `7D` | `1.28` | 83,010,000.00 USD | 83,010,000.00 USD | 0.00 USD | 639,910.00 USD | 895,200.00 USD | 1,540,000.00 USD |
| `1D` | `1.29` | 36,910,000.00 USD | 36,910,000.00 USD | 0.00 USD | 303,010.00 USD | 454,190.00 USD | 998,230.00 USD |
| `7D` | `1.29` | 84,180,000.00 USD | 84,180,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 37,670,000.00 USD | 37,670,000.00 USD | 0.00 USD | 584,100.00 USD | 166,940.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 84,290,000.00 USD | 84,290,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 37,690,000.00 USD | 37,690,000.00 USD | 0.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD |
| `7D` | `1.29` | 86,380,000.00 USD | 86,380,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD |
| `1D` | `1.29` | 39,480,000.00 USD | 39,480,000.00 USD | 0.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `1.29` | 86,800,000.00 USD | 86,800,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 43,430,000.00 USD | 43,430,000.00 USD | 0.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD |
| `7D` | `1.29` | 96,430,000.00 USD | 96,430,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 48,330,000.00 USD | 48,330,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD |
| `7D` | `1.30` | 97,670,000.00 USD | 97,670,000.00 USD | 0.00 USD | 209,360.00 USD | 393,370.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 49,060,000.00 USD | 49,060,000.00 USD | 0.00 USD | 344,680.00 USD | 422.50 USD | 383,310.00 USD |
| `7D` | `1.30` | 99,090,000.00 USD | 99,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD |
| `1D` | `1.30` | 49,740,000.00 USD | 49,740,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 100,340,000.00 USD | 100,340,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 51,910,000.00 USD | 51,910,000.00 USD | 0.00 USD | 602,010.00 USD | 912,930.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 103,350,000.00 USD | 103,350,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 486,150.00 USD |
| `1D` | `1.30` | 52,620,000.00 USD | 52,620,000.00 USD | 0.00 USD | 188,510.00 USD | 202,150.00 USD | 319,160.00 USD |
| `1D` | `1.31` | 53,750,000.00 USD | 53,750,000.00 USD | 0.00 USD | 493,480.00 USD | 313,760.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 106,350,000.00 USD | 106,350,000.00 USD | 0.00 USD | 2,140,000.00 USD | 178,660.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 56,260,000.00 USD | 56,260,000.00 USD | 0.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD |
| `7D` | `1.31` | 110,130,000.00 USD | 110,130,000.00 USD | 0.00 USD | 1,480,000.00 USD | 590,530.00 USD | 1,710,000.00 USD |
| `1D` | `1.31` | 58,840,000.00 USD | 58,840,000.00 USD | 0.00 USD | 908,870.00 USD | 396,100.00 USD | 1,270,000.00 USD |
| `7D` | `1.31` | 113,370,000.00 USD | 113,370,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,970,000.00 USD |
| `1D` | `1.31` | 61,920,000.00 USD | 61,920,000.00 USD | 0.00 USD | 1,800,000.00 USD | 538,960.00 USD | 745,480.00 USD |
| `7D` | `1.31` | 116,220,000.00 USD | 116,220,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 63,640,000.00 USD | 63,640,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 118,680,000.00 USD | 118,680,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 69,500,000.00 USD | 69,500,000.00 USD | 0.00 USD | 222,150.00 USD | 1,720,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.32` | 123,300,000.00 USD | 123,300,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 76,300,000.00 USD | 76,300,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 126,380,000.00 USD | 126,380,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 79,610,000.00 USD | 79,610,000.00 USD | 0.00 USD | 1,680,000.00 USD | 608,860.00 USD | 1,030,000.00 USD |
| `7D` | `1.32` | 128,210,000.00 USD | 128,210,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 84,250,000.00 USD | 84,250,000.00 USD | 0.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD |
| `7D` | `1.32` | 132,670,000.00 USD | 132,670,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 87,300,000.00 USD | 87,300,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD |
| `7D` | `1.32` | 135,030,000.00 USD | 135,030,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 89,590,000.00 USD | 89,590,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 135,570,000.00 USD | 135,570,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 91,780,000.00 USD | 91,780,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 136,730,000.00 USD | 136,730,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 94,220,000.00 USD | 94,220,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 138,450,000.00 USD | 138,450,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 96,480,000.00 USD | 96,480,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 142,500,000.00 USD | 142,500,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 98,810,000.00 USD | 98,810,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 143,040,000.00 USD | 143,040,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 101,250,000.00 USD | 101,250,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 144,990,000.00 USD | 144,990,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 103,930,000.00 USD | 103,930,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 147,340,000.00 USD | 147,340,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 106,570,000.00 USD | 106,570,000.00 USD | 0.00 USD | 1,020,000.00 USD | 389,350.00 USD | 1,230,000.00 USD |
| `7D` | `1.34` | 152,040,000.00 USD | 152,040,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 110,160,000.00 USD | 110,160,000.00 USD | 0.00 USD | 1,630,000.00 USD | 761,510.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 157,710,000.00 USD | 157,710,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 113,430,000.00 USD | 113,430,000.00 USD | 0.00 USD | 1,470,000.00 USD | 626,040.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 168,780,000.00 USD | 168,780,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 114,660,000.00 USD | 114,660,000.00 USD | 0.00 USD | 498,430.00 USD | 251,400.00 USD | 481,220.00 USD |
| `7D` | `1.35` | 175,940,000.00 USD | 175,940,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,230,000.00 USD | 2,500,000.00 USD |
| `1D` | `1.35` | 115,920,000.00 USD | 115,920,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 186,250,000.00 USD | 186,250,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 117,410,000.00 USD | 117,410,000.00 USD | 0.00 USD | 771,840.00 USD | 230,360.00 USD | 488,180.00 USD |
| `7D` | `1.35` | 194,020,000.00 USD | 194,020,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 118,730,000.00 USD | 118,730,000.00 USD | 0.00 USD | 558,120.00 USD | 207,050.00 USD | 556,870.00 USD |
| `7D` | `1.35` | 202,340,000.00 USD | 202,340,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 120,210,000.00 USD | 120,210,000.00 USD | 0.00 USD | 503,350.00 USD | 214,770.00 USD | 753,540.00 USD |
| `7D` | `1.35` | 210,580,000.00 USD | 210,580,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 121,460,000.00 USD | 121,460,000.00 USD | 0.00 USD | 510,040.00 USD | 138,360.00 USD | 608,510.00 USD |
| `7D` | `1.36` | 214,670,000.00 USD | 214,670,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 122,330,000.00 USD | 122,330,000.00 USD | 0.00 USD | 412,060.00 USD | 41,890.00 USD | 413,280.00 USD |
| `7D` | `1.36` | 218,450,000.00 USD | 218,450,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 122,910,000.00 USD | 122,910,000.00 USD | 0.00 USD | 266,880.00 USD | 78,370.00 USD | 233,330.00 USD |
| `7D` | `1.36` | 220,590,000.00 USD | 220,590,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 123,580,000.00 USD | 123,580,000.00 USD | 0.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD |
| `7D` | `1.36` | 224,690,000.00 USD | 224,690,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 123,710,000.00 USD | 123,710,000.00 USD | 0.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD |
| `7D` | `1.36` | 226,410,000.00 USD | 226,410,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 123,910,000.00 USD | 123,910,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD |
| `7D` | `1.37` | 226,890,000.00 USD | 226,890,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 124,140,000.00 USD | 124,140,000.00 USD | 0.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 228,310,000.00 USD | 228,310,000.00 USD | 0.00 USD | 528,490.00 USD | 136,720.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 124,320,000.00 USD | 124,320,000.00 USD | 0.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 229,490,000.00 USD | 229,490,000.00 USD | 0.00 USD | 345,700.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 124,460,000.00 USD | 124,460,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 232,110,000.00 USD | 232,110,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,280,000.00 USD |
| `1D` | `1.37` | 124,600,000.00 USD | 124,600,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.38` | 233,710,000.00 USD | 233,710,000.00 USD | 0.00 USD | 536,130.00 USD | 294,500.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 124,850,000.00 USD | 124,850,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 235,260,000.00 USD | 235,260,000.00 USD | 0.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 125,350,000.00 USD | 125,350,000.00 USD | 0.00 USD | 231,710.00 USD | 71,930.00 USD | 195,200.00 USD |
| `7D` | `1.38` | 237,400,000.00 USD | 237,400,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 125,840,000.00 USD | 125,840,000.00 USD | 0.00 USD | 162,970.00 USD | 97,690.00 USD | 224,580.00 USD |
| `7D` | `1.38` | 239,940,000.00 USD | 239,940,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 126,030,000.00 USD | 126,030,000.00 USD | 0.00 USD | 79,200.00 USD | 23,150.00 USD | 90,990.00 USD |
| `7D` | `1.38` | 241,030,000.00 USD | 241,030,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 126,210,000.00 USD | 126,210,000.00 USD | 0.00 USD | 131,770.00 USD | 0.00 USD | 50,560.00 USD |
| `7D` | `1.39` | 242,130,000.00 USD | 242,130,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 126,240,000.00 USD | 126,240,000.00 USD | 0.00 USD | 7,260.00 USD | 15,600.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 242,660,000.00 USD | 242,660,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 126,280,000.00 USD | 126,280,000.00 USD | 0.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD |
| `7D` | `1.39` | 243,760,000.00 USD | 243,760,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 243,930,000.00 USD | 243,930,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 126,290,000.00 USD | 126,290,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 244,260,000.00 USD | 244,260,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 126,350,000.00 USD | 126,350,000.00 USD | 0.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.40` | 244,420,000.00 USD | 244,420,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 126,420,000.00 USD | 126,420,000.00 USD | 0.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.40` | 244,540,000.00 USD | 244,540,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.40` | 126,550,000.00 USD | 126,550,000.00 USD | 0.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.40` | 244,550,000.00 USD | 244,550,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 244,690,000.00 USD | 244,690,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 244,810,000.00 USD | 244,810,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `1D` | `1.40` | 126,570,000.00 USD | 126,570,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.41` | 245,050,000.00 USD | 245,050,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 245,210,000.00 USD | 245,210,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.41` | 126,630,000.00 USD | 126,630,000.00 USD | 0.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.41` | 245,590,000.00 USD | 245,590,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.41` | 127,010,000.00 USD | 127,010,000.00 USD | 0.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.41` | 246,240,000.00 USD | 246,240,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.41` | 127,140,000.00 USD | 127,140,000.00 USD | 0.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 246,420,000.00 USD | 246,420,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 127,140,000.00 USD | 127,140,000.00 USD | 0.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD |
| `7D` | `1.42` | 247,040,000.00 USD | 247,040,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `1D` | `1.42` | 127,310,000.00 USD | 127,310,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 247,560,000.00 USD | 247,560,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.42` | 127,690,000.00 USD | 127,690,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 248,590,000.00 USD | 248,590,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 128,430,000.00 USD | 128,430,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 249,960,000.00 USD | 249,960,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 128,850,000.00 USD | 128,850,000.00 USD | 0.00 USD | 154,900.00 USD | 92,570.00 USD | 175,760.00 USD |
| `1D` | `1.42` | 128,940,000.00 USD | 128,940,000.00 USD | 0.00 USD | 9,670.00 USD | 54,510.00 USD | 20,180.00 USD |
| `7D` | `1.42` | 250,590,000.00 USD | 250,590,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 250,950,000.00 USD | 250,950,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 251,970,000.00 USD | 251,970,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 253,480,000.00 USD | 253,480,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 254,860,000.00 USD | 254,860,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 255,660,000.00 USD | 255,660,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 256,190,000.00 USD | 256,190,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 256,540,000.00 USD | 256,540,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 257,000,000.00 USD | 257,000,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 257,720,000.00 USD | 257,720,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 258,090,000.00 USD | 258,090,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 258,220,000.00 USD | 258,220,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 258,340,000.00 USD | 258,340,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 258,680,000.00 USD | 258,680,000.00 USD | 0.00 USD | 66,640.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 259,290,000.00 USD | 259,290,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 259,860,000.00 USD | 259,860,000.00 USD | 0.00 USD | 186,430.00 USD | 128,180.00 USD | 255,270.00 USD |
| `7D` | `1.46` | 260,320,000.00 USD | 260,320,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 260,480,000.00 USD | 260,480,000.00 USD | 0.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 260,950,000.00 USD | 260,950,000.00 USD | 0.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 261,160,000.00 USD | 261,160,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.88B` | Total OI Tokens: `2,297,959,789.7 XRP`
  * 1h OI Change: `-2.95%` | 4h OI Change: `-4.36%` | 24h OI Change: `-3.38%`
  * Exchange Breakdown: Binance=`469.15M` | Bybit=`321.07M` | OKX=`95.22M` | Hyperliquid=`219.86M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.97K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `0.0052%` |
| **USDT Bybit** | `-0.0048%` | **USDT KuCoin** | `0.0051%` |
| **USDT MEXC** | `0.0020%` | **USDT BingX** | `0.0055%` |
| **USDT Gate** | `-0.0011%` | **USDT Bitget** | `0.0002%` |
| **CoinM Binance** | `0.0079%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `56.43%` | `43.57%` | `1.30` | 2,690,000,000.00 USD |
| `15M` | `Binance` | `52.02%` | `47.98%` | `1.08` | 793,360,000.00 USD |
| `15M` | `OKX` | `51.36%` | `48.64%` | `1.06` | 363,300,000.00 USD |
| `15M` | `Bybit` | `56.36%` | `43.64%` | `1.29` | 211,640,000.00 USD |
| `15M` | `KuCoin` | `59.64%` | `40.36%` | `1.48` | 28,350,000.00 USD |
| `15M` | `Gate` | `49.89%` | `50.11%` | `1.00` | 332,840,000.00 USD |
| `15M` | `Bitget` | `59.08%` | `40.92%` | `1.44` | 70,590,000.00 USD |
| `15M` | `BingX` | `50.2%` | `49.8%` | `1.01` | 27,770,000.00 USD |
| `15M` | `MEXC` | `54.57%` | `45.43%` | `1.20` | 57,170,000.00 USD |
| `15M` | `Bitunix` | `50.99%` | `49.01%` | `1.04` | 70,650,000.00 USD |
| `15M` | `Hyperliquid` | `63.38%` | `36.62%` | `1.73` | 83,340,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `66%` | `34%` | `1.94` | 7,560,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `70.32%` | `29.68%` | `2.37` | 549,810,000.00 USD |
| `15M` | `HTX` | `50.02%` | `49.98%` | `1.00` | 14,280,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `65.5%` | `34.5%` | `1.90` | 11,030,000.00 USD |
| `15M` | `Bitfinex` | `38.67%` | `61.33%` | `0.63` | 877,070.00 USD |
| `15M` | `Kraken` | `57.42%` | `42.58%` | `1.35` | 12,450,000.00 USD |
| `15M` | `Aster` | `48.2%` | `51.8%` | `0.93` | 23,720,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.23%` | `49.77%` | `1.01` | 29,570,000.00 USD |
| `15M` | `Whale Positions` | `52.02%` | `47.98%` | `1.08` | 793,360,000.00 USD |
| `15M` | `Global Accounts` | `56.43%` | `43.57%` | `1.30` | 2,690,000,000.00 USD |
| `1H` | `XRP` | `44.03%` | `55.97%` | `0.79` | 16,710,000,000.00 USD |
| `1H` | `Binance` | `43.84%` | `56.16%` | `0.78` | 4,740,000,000.00 USD |
| `1H` | `OKX` | `42.3%` | `57.7%` | `0.73` | 2,100,000,000.00 USD |
| `1H` | `Bybit` | `41.39%` | `58.61%` | `0.71` | 2,080,000,000.00 USD |
| `1H` | `KuCoin` | `45.99%` | `54.01%` | `0.85` | 88,410,000.00 USD |
| `1H` | `Gate` | `50.39%` | `49.61%` | `1.02` | 1,000,000,000.00 USD |
| `1H` | `Bitget` | `50.04%` | `49.96%` | `1.00` | 711,100,000.00 USD |
| `1H` | `BingX` | `50.98%` | `49.02%` | `1.04` | 215,960,000.00 USD |
| `1H` | `MEXC` | `48.73%` | `51.27%` | `0.95` | 692,610,000.00 USD |
| `1H` | `Bitunix` | `49.68%` | `50.32%` | `0.99` | 707,270,000.00 USD |
| `1H` | `Hyperliquid` | `44.68%` | `55.32%` | `0.81` | 1,070,000,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.59%` | `46.41%` | `1.15` | 81,450,000.00 USD |
| `1H` | `Crypto.com` | `50.12%` | `49.88%` | `1.00` | 89,660,000.00 USD |
| `1H` | `WhiteBIT` | `39.08%` | `60.92%` | `0.64` | 2,370,000,000.00 USD |
| `1H` | `HTX` | `41.07%` | `58.93%` | `0.70` | 56,680,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `46.89%` | `53.11%` | `0.88` | 273,740,000.00 USD |
| `1H` | `Bitfinex` | `29.54%` | `70.46%` | `0.42` | 7,690,000.00 USD |
| `1H` | `Kraken` | `39.88%` | `60.12%` | `0.66` | 138,500,000.00 USD |
| `1H` | `Aster` | `43.23%` | `56.77%` | `0.76` | 145,380,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.58%` | `53.42%` | `0.87` | 141,360,000.00 USD |
| `1H` | `Whale Positions` | `43.84%` | `56.16%` | `0.78` | 4,740,000,000.00 USD |
| `1H` | `Global Accounts` | `44.03%` | `55.97%` | `0.79` | 16,710,000,000.00 USD |
| `4H` | `XRP` | `46.73%` | `53.27%` | `0.88` | 20,660,000,000.00 USD |
| `4H` | `Binance` | `44.49%` | `55.51%` | `0.80` | 6,170,000,000.00 USD |
| `4H` | `OKX` | `44.53%` | `55.47%` | `0.80` | 3,570,000,000.00 USD |
| `4H` | `Bybit` | `44.19%` | `55.81%` | `0.79` | 1,490,000,000.00 USD |
| `4H` | `KuCoin` | `53.36%` | `46.64%` | `1.14` | 188,130,000.00 USD |
| `4H` | `Gate` | `49.21%` | `50.79%` | `0.97` | 2,030,000,000.00 USD |
| `4H` | `Bitget` | `51.44%` | `48.56%` | `1.06` | 986,260,000.00 USD |
| `4H` | `BingX` | `49.81%` | `50.19%` | `0.99` | 221,520,000.00 USD |
| `4H` | `MEXC` | `48.66%` | `51.34%` | `0.95` | 597,470,000.00 USD |
| `4H` | `Bitunix` | `47.3%` | `52.7%` | `0.90` | 662,130,000.00 USD |
| `4H` | `Hyperliquid` | `50.41%` | `49.59%` | `1.02` | 965,220,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.31%` | `47.69%` | `1.10` | 49,950,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `50.3%` | `49.7%` | `1.01` | 2,900,000,000.00 USD |
| `4H` | `HTX` | `34.19%` | `65.81%` | `0.52` | 198,070,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `47.72%` | `52.28%` | `0.91` | 115,320,000.00 USD |
| `4H` | `Bitfinex` | `26.84%` | `73.16%` | `0.37` | 7,460,000.00 USD |
| `4H` | `Kraken` | `47.43%` | `52.57%` | `0.90` | 67,130,000.00 USD |
| `4H` | `Aster` | `46.52%` | `53.48%` | `0.87` | 183,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49%` | `51%` | `0.96` | 275,360,000.00 USD |
| `4H` | `Whale Positions` | `44.49%` | `55.51%` | `0.80` | 6,170,000,000.00 USD |
| `4H` | `Global Accounts` | `46.73%` | `53.27%` | `0.88` | 20,660,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.29` | `1.28` | `1.29` | `1.29` | `1.28` | 10,140,362.32 USD | 5,667,315.95 USD | 4,473,046.37 USD | 1,194,269.58 USD | `+11.78%` | `17B / 12S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,885,752.93 USD | 2,814,674.62 USD | 3,071,078.30 USD | -256,403.68 USD | `-4.36%` | `5B / 13S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,036,330.68 USD | 2,484,228.37 USD | 2,552,102.32 USD | -67,873.95 USD | `-1.35%` | `8B / 7S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.28` | 3,779,916.77 USD | 1,963,240.26 USD | 1,816,676.51 USD | 146,563.75 USD | `+3.88%` | `6B / 5S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 7,767,016.10 USD | 3,262,612.53 USD | 4,504,403.57 USD | -1,241,791.04 USD | `-15.99%` | `7B / 12S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.28` | `1.26` | 41,778,066.41 USD | 16,233,527.16 USD | 25,544,539.25 USD | -9,311,012.09 USD | `-22.29%` | `4B / 58S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 9,197,225.16 USD | 4,639,147.41 USD | 4,558,077.75 USD | 81,069.66 USD | `+0.88%` | `4B / 5S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.27` | `1.23` | 112,851,214.34 USD | 44,440,734.72 USD | 68,410,479.62 USD | -23,969,744.90 USD | `-21.24%` | `0B / 35S` |
| `5:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.22` | 96,971,024.45 USD | 46,182,833.37 USD | 50,788,191.08 USD | -4,605,357.71 USD | `-4.75%` | `1B / 8S` |
| `0:00 UTC` | `1.25` | `1.24` | `1.25` | `1.25` | `1.23` | 38,011,001.96 USD | 20,068,667.84 USD | 17,942,334.12 USD | 2,126,333.71 USD | `+5.59%` | `20B / 5S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.31` | 0.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Trapped longs` | **`BEARISH`** | Failed breakout | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 18:52` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 1,200,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 3,000,000.00 USD | 0.00 USD |
| `10-28 12:56` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.32` | 0.00 USD | 0.00 USD |
| `10-28 10:21` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,600,000.00 USD | 0.00 USD |
| `10-28 08:33` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 2,100,000.00 USD | 0.00 USD |
| `10-28 08:12` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,700,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 10M XRP` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:20` | `Volume 10M XRP` | `Divergence` | **`BULLISH`** | Drop without taker selling | `1.33` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 186,910.00 USD | 67,890.00 USD | **`ACCUMULATION`** |
| `15m` | -1,120,000.00 USD | 2,780,000.00 USD | **`ACCUMULATION`** |
| `30m` | -3,710,000.00 USD | -8,300,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -25,490,000.00 USD | -66,030,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -31,010,000.00 USD | -93,180,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -38,960,000.00 USD | -113,330,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -41,050,000.00 USD | -126,050,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -38,010,000.00 USD | -119,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -39,900,000.00 USD | -122,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -59,260,000.00 USD | -175,970,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -106,030,000.00 USD | -185,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -587,230,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+186.91K` | 15m=`-1.12M` | 1h=`-25.49M` | 24h=`-59.26M`
* Futures Capital Netflows: 5m=`+67.89K` | 15m=`+2.78M` | 1h=`-66.03M` | 24h=`-175.97M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0187` pts)
  * +2.5R Take Profit: `1.28`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0187` pts)
  * +2.5R Take Profit: `1.20`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
