# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:54:16 IST` (`2026-10-29 20:24:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.27` | **Live Ask Quote**: `1.27` | **Mid Price**: `1.27`
- **Spread Points**: `3.00` | **Spread BPS**: `23.61 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-1.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0064` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.31` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.28` | EMA-20=`1.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.29` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.1599`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-2.54%`)
  * Point of Control (POC) = `1.29` (Distance: `-1.67%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-1.19%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.32`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.30` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.31` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.28`
  * London Session (08:00-16:00 UTC): High=`1.30` | Low=`1.28`
  * New York Session (13:00-21:00 UTC): High=`1.31` | Low=`1.28`
  * Initial Balance (First Hour): IB High=`1.30` | IB Low=`1.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.27` - `1.28`
  * Optimal Trade Entry (OTE 0.705): `1.27`
  * Structural Invalidation Anchor (0.786): `1.28`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.28` | `1.28` | `1.27` | `1.27` | `15,412,704` | 19,663,012.67 USD | -7,212,135.40 USD | `-36.68%` | -49,587,242.36 USD | `-2.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.27` | `1.27` | `1.26` | `1.27` | `13,434,632` | 17,036,419.98 USD | -2,542,123.46 USD | `-14.92%` | -52,129,365.81 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.27` | `1.27` | `1.27` | `1.27` | `3,534,004` | 4,484,691.04 USD | 236,745.78 USD | `+5.28%` | -51,892,620.03 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.29` | `2,940,674` | 3,779,916.77 USD | 146,563.75 USD | `+3.88%` | -41,133,315.92 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.28` | `6,055,937` | 7,767,016.10 USD | -1,241,791.04 USD | `-15.99%` | -42,375,106.96 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.28` | `1.26` | `1.27` | `32,367,920` | 41,167,097.38 USD | -9,500,537.52 USD | `-23.08%` | -51,875,644.48 USD | `-2.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `38,773,350` | 49,794,344.17 USD | -9,116,518.67 USD | `-18.31%` | -40,138,234.48 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `17,509,907` | 22,469,016.48 USD | -1,419,504.92 USD | `-6.32%` | -41,557,739.40 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.26` | `1.27` | `32,369,913` | 41,169,625.97 USD | -9,503,066.11 USD | `-23.08%` | -51,060,805.51 USD | `-1.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.26` | `1.27` | `32,357,788` | 41,154,241.14 USD | -9,513,330.07 USD | `-23.12%` | -49,452,359.88 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.26` | `1.27` | `32,357,788` | 41,154,241.14 USD | -9,513,330.07 USD | `-23.12%` | -49,452,359.88 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`1.27`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.27` | `543675.0000` | 691,174.03 USD | 3,185,479.74 USD | `9 orders` | `+0.15%` | `-` |
| `ASK` | `1.27` | `52259.0000` | 66,431.64 USD | 2,494,305.71 USD | `8 orders` | `+0.15%` | `-` |
| `ASK` | `1.27` | `101592.0000` | 129,133.59 USD | 2,427,874.07 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `1.27` | `235229.0000` | 298,976.06 USD | 2,298,740.48 USD | `10 orders` | `+0.13%` | `-` |
| `ASK` | `1.27` | `328369.0000` | 417,324.16 USD | 1,999,764.42 USD | `8 orders` | `+0.12%` | `-` |
| `ASK` | `1.27` | `11128.0000` | 14,141.46 USD | 1,582,440.26 USD | `4 orders` | `+0.11%` | `-` |
| `ASK` | `1.27` | `19081.0000` | 24,246.23 USD | 1,568,298.80 USD | `4 orders` | `+0.11%` | `-` |
| `ASK` | `1.27` | `71860.0000` | 91,305.32 USD | 1,544,052.57 USD | `6 orders` | `+0.10%` | `-` |
| `ASK` | `1.27` | `60436.0000` | 76,783.94 USD | 1,452,747.25 USD | `12 orders` | `+0.09%` | `-` |
| `ASK` | `1.27` | `79999.0000` | 101,630.73 USD | 1,375,963.32 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `1.27` | `341512.0000` | 433,822.69 USD | 1,274,332.59 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `1.27` | `71682.0000` | 91,050.48 USD | 840,509.89 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `1.27` | `300768.0000` | 382,005.44 USD | 749,459.42 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `1.27` | `12620.0000` | 16,027.40 USD | 367,453.98 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `1.27` | `81968.0000` | 104,091.16 USD | 351,426.58 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `1.27` | `88392.0000` | 112,240.16 USD | 247,335.42 USD | `16 orders` | `+0.04%` | `-` |
| `ASK` | `1.27` | `42785.0000` | 54,324.11 USD | 135,095.25 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `1.27` | `16618.0000` | 21,098.21 USD | 80,771.14 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `1.27` | `35109.0000` | 44,570.88 USD | 59,672.93 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `1.27` | `11897.0000` | 15,102.05 USD | 15,102.05 USD | `5 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.27` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.27` | `0.00%` | `-` |
| `BID` | `1.27` | `25761.0000` | 32,698.44 USD | 32,698.44 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `1.27` | `29959.0000` | 38,023.96 USD | 70,722.40 USD | `13 orders` | `-0.01%` | `-` |
| `BID` | `1.27` | `30528.0000` | 38,743.08 USD | 109,465.48 USD | `16 orders` | `-0.02%` | `-` |
| `BID` | `1.27` | `108363.0000` | 137,512.65 USD | 246,978.13 USD | `16 orders` | `-0.03%` | `-` |
| `BID` | `1.27` | `6017.0000` | 7,634.97 USD | 254,613.10 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `1.27` | `22100.0000` | 28,040.48 USD | 282,653.58 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.27` | `91193.0000` | 115,696.56 USD | 398,350.14 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `1.27` | `90669.0000` | 115,022.69 USD | 513,372.84 USD | `13 orders` | `-0.06%` | `-` |
| `BID` | `1.27` | `36585.0000` | 46,408.07 USD | 559,780.91 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `1.27` | `52162.0000` | 66,162.28 USD | 625,943.19 USD | `13 orders` | `-0.07%` | `-` |
| `BID` | `1.27` | `329496.0000` | 417,899.78 USD | 1,043,842.97 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `1.27` | `109349.0000` | 138,676.40 USD | 1,182,519.37 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `1.27` | `42884.0000` | 54,381.20 USD | 1,236,900.57 USD | `12 orders` | `-0.10%` | `-` |
| `BID` | `1.27` | `50359.0000` | 63,855.21 USD | 1,300,755.78 USD | `9 orders` | `-0.11%` | `-` |
| `BID` | `1.27` | `38288.0000` | 48,545.36 USD | 1,349,301.14 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.27` | `136008.0000` | 172,430.94 USD | 1,521,732.08 USD | `16 orders` | `-0.12%` | `-` |
| `BID` | `1.27` | `418540.0000` | 530,583.16 USD | 2,052,315.24 USD | `16 orders` | `-0.13%` | `-` |
| `BID` | `1.27` | `28415.0000` | 36,018.85 USD | 2,088,334.09 USD | `11 orders` | `-0.14%` | `-` |
| `BID` | `1.27` | `67398.0000` | 85,426.97 USD | 2,173,761.05 USD | `11 orders` | `-0.15%` | `-` |
| `BID` | `1.27` | `108579.0000` | 137,613.02 USD | 2,311,374.08 USD | `6 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,475,903.53 USD | `35,031,430.00` | `1.13` | `1.27` | `0.9612` | 4,897,020.26 USD | `+11.01%` | `10X Cross` |
| `88` | `0x5b5d...c060` | `SHORT` | 20,309,720.12 USD | `15,964,251.00` | `1.44` | `1.27` | `11.43` | 2,606,348.59 USD | `+12.83%` | `5X Cross` |
| `150` | `0x58f0...0d20` | `LONG` | 13,875,516.69 USD | `10,931,629.00` | `1.36` | `1.27` | `1.25` | -989,636.27 USD | `-7.13%` | `20X Cross` |
| `154` | `0xb83d...6e36` | `SHORT` | 13,403,310.41 USD | `10,555,450.00` | `1.50` | `1.27` | `14.24` | 2,419,259.23 USD | `+18.05%` | `5X Cross` |
| `435` | `0xca49...53c8` | `SHORT` | 5,266,318.55 USD | `4,138,886.00` | `1.44` | `1.27` | `4.49` | 687,004.19 USD | `+13.05%` | `20X Cross` |
| `440` | `0xfc27...9d9d` | `SHORT` | 5,201,325.67 USD | `4,089,414.00` | `1.31` | `1.27` | `4.96` | 169,149.46 USD | `+3.25%` | `20X Cross` |
| `501` | `0x610b...b613` | `LONG` | 4,500,102.63 USD | `3,543,946.00` | `1.44` | `1.27` | `0.7509` | -599,889.98 USD | `-13.33%` | `5X Cross` |
| `540` | `0xc30c...a4c9` | `SHORT` | 4,183,669.84 USD | `3,295,209.00` | `1.42` | `1.27` | `1.60` | 505,481.74 USD | `+12.08%` | `8X Cross` |
| `543` | `0xdd53...2b13` | `SHORT` | 4,174,572.91 USD | `3,281,381.00` | `1.44` | `1.27` | `19.02` | 539,904.68 USD | `+12.93%` | `3X Cross` |
| `574` | `0xecb6...2b00` | `SHORT` | 4,018,941.99 USD | `3,159,794.00` | `1.31` | `1.27` | `10.19` | 105,086.16 USD | `+2.61%` | `10X Cross` |
| `596` | `0x77ee...a018` | `LONG` | 3,890,523.81 USD | `3,065,094.00` | `1.28` | `1.27` | `0.000000` | -25,692.41 USD | `-0.66%` | `20X Cross` |
| `600` | `0x9946...0852` | `SHORT` | 3,848,546.21 USD | `3,025,111.00` | `1.43` | `1.27` | `1.68` | 464,638.34 USD | `+12.07%` | `20X Cross` |
| `689` | `0x9aa5...58af` | `SHORT` | 3,306,925.00 USD | `2,604,083.00` | `1.46` | `1.27` | `4.33` | 490,795.65 USD | `+14.84%` | `20X Cross` |
| `705` | `0xf48f...10fe` | `LONG` | 3,256,486.71 USD | `2,565,779.00` | `1.53` | `1.27` | `0.9452` | -668,154.02 USD | `-20.52%` | `4X Cross` |
| `706` | `0x023a...2355` | `SHORT` | 3,231,056.10 USD | `2,544,339.00` | `1.33` | `1.27` | `4.49` | 145,036.59 USD | `+4.49%` | `20X Cross` |
| `739` | `0x45d2...4029` | `SHORT` | 3,119,970.70 USD | `2,453,000.00` | `1.48` | `1.27` | `16.80` | 518,309.72 USD | `+16.61%` | `20X Cross` |
| `971` | `0xfc66...ca06` | `SHORT` | 2,318,044.57 USD | `1,825,807.00` | `1.31` | `1.27` | `20.68` | 66,126.26 USD | `+2.85%` | `20X Cross` |
| `1027` | `0xc179...e0c8` | `SHORT` | 2,160,083.50 USD | `1,697,645.00` | `1.30` | `1.27` | `4.82` | 49,161.28 USD | `+2.28%` | `10X Cross` |
| `1084` | `0xeadc...9d55` | `LONG` | 2,056,018.49 USD | `1,619,805.00` | `1.21` | `1.27` | `0.000000` | 97,175.46 USD | `+4.73%` | `20X Cross` |
| `1161` | `0x94b2...599e` | `SHORT` | 1,955,605.43 USD | `1,540,696.00` | `1.36` | `1.27` | `1.84` | 144,861.02 USD | `+7.41%` | `20X Cross` |
| `1171` | `0xbcd4...0dd2` | `SHORT` | 1,943,944.93 USD | `1,529,461.00` | `1.31` | `1.27` | `2.07` | 60,599.67 USD | `+3.12%` | `20X Cross` |
| `1186` | `0x3fc5...c0c1` | `SHORT` | 1,919,354.62 USD | `1,511,779.00` | `1.52` | `1.27` | `2.73` | 372,259.98 USD | `+19.40%` | `20X Cross` |
| `1208` | `0x31ef...f715` | `LONG` | 1,872,319.04 USD | `1,475,080.00` | `1.49` | `1.27` | `1.04` | -326,946.36 USD | `-17.46%` | `3X Isolated` |
| `1268` | `0x7737...bf66` | `SHORT` | 1,794,536.43 USD | `1,413,466.00` | `1.41` | `1.27` | `13.82` | 204,332.21 USD | `+11.39%` | `10X Cross` |
| `1282` | `0xef96...9383` | `SHORT` | 1,766,535.35 USD | `1,390,999.00` | `1.34` | `1.27` | `4.14` | 97,249.87 USD | `+5.51%` | `20X Cross` |
| `1359` | `0xee2b...d67e` | `LONG` | 1,660,156.34 USD | `1,306,284.00` | `1.55` | `1.27` | `0.2904` | -370,498.57 USD | `-22.32%` | `4X Cross` |
| `1424` | `0x4537...8732` | `SHORT` | 1,594,707.03 USD | `1,256,801.00` | `1.31` | `1.27` | `2.05` | 48,762.44 USD | `+3.06%` | `10X Cross` |
| `1428` | `0x215d...f80a` | `LONG` | 1,588,505.01 USD | `1,251,777.00` | `1.32` | `1.27` | `1.15` | -65,949.21 USD | `-4.15%` | `14X Cross` |
| `1459` | `0x123d...3bff` | `LONG` | 1,543,264.87 USD | `1,215,329.00` | `1.35` | `1.27` | `0.000000` | -93,804.35 USD | `-6.08%` | `10X Cross` |
| `1477` | `0x95da...2328` | `LONG` | 1,529,264.06 USD | `1,204,809.00` | `1.36` | `1.27` | `0.000000` | -114,378.77 USD | `-7.48%` | `5X Cross` |
| `1520` | `0xdf95...7d72` | `SHORT` | 1,476,130.33 USD | `1,160,115.00` | `1.37` | `1.27` | `33.78` | 117,228.93 USD | `+7.94%` | `20X Cross` |
| `1549` | `0x5fa3...35b7` | `SHORT` | 1,440,305.96 USD | `1,132,138.00` | `1.31` | `1.27` | `3.13` | 41,443.27 USD | `+2.88%` | `20X Cross` |
| `1672` | `0xb1ce...681b` | `LONG` | 1,299,888.16 USD | `1,021,764.00` | `1.49` | `1.27` | `1.16` | -224,168.33 USD | `-17.25%` | `4X Isolated` |
| `1772` | `0x3c36...461a` | `LONG` | 1,194,112.00 USD | `940,051.00` | `1.30` | `1.27` | `1.06` | -24,968.61 USD | `-2.09%` | `10X Cross` |
| `1903` | `0xe9d1...d2d3` | `SHORT` | 1,077,218.81 USD | `846,737.00` | `1.31` | `1.27` | `2.53` | 28,483.74 USD | `+2.64%` | `10X Cross` |
| `1987` | `0xbfc7...80b4` | `SHORT` | 1,015,920.00 USD | `800,000.00` | `1.48` | `1.27` | `7.23` | 167,534.65 USD | `+16.49%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:55:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,782.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.78K USD at 1.3233 USD [API] | `2026-10-27 22:01:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,988.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.99K USD at 1.3234 USD [API] | `2026-10-27 22:01:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,801.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.80K USD at 1.3232 USD [API] | `2026-10-27 22:01:07` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 273.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.27K USD at 1.3255 USD [API] | `2026-10-27 15:24:40` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 18,012.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 18.01K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 15,118.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.12K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,482.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.48K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,542.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.54K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,355.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.36K USD at 1.3251 USD [API] | `2026-10-27 22:07:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3254 USD [API] | `2026-10-27 22:07:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,415.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.42K USD at 1.3251 USD [API] | `2026-10-27 22:11:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,907.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.91K USD at 1.3251 USD [API] | `2026-10-27 22:11:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,416.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.42K USD at 1.3252 USD [API] | `2026-10-27 22:10:49` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,280.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.28K USD at 1.3268 USD [API] | `2026-10-27 22:18:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3269 USD [API] | `2026-10-27 22:18:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,049.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.05K USD at 1.3248 USD [API] | `2026-10-27 22:22:42` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,530.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.53K USD at 1.3234 USD [API] | `2026-10-27 22:27:14` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,697.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.70K USD at 1.3230 USD [API] | `2026-10-27 22:29:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 35,708.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 35.71K USD at 1.3223 USD [API] | `2026-10-27 22:30:20` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 25,123.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.12K USD at 1.3223 USD [API] | `2026-10-27 22:30:20` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,672.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.67K USD at 1.3241 USD [API] | `2026-10-27 22:35:15` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,149.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.15K USD at 1.3241 USD [API] | `2026-10-27 22:35:15` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,796.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.80K USD at 1.3262 USD [API] | `2026-10-27 22:53:15` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 1,425.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.43K USD at 2.7053 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 340.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.34K USD at 2.7053 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 873.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 2.7053 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 500.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 2.7054 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 1,057.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.06K USD at 2.7054 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 165.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 2.7054 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 148.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.15K USD at 2.7055 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `2.71` | 689.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 2.7055 USD [API] | `2025-10-10 18:48:24` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,374.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.37K USD at 1.3296 USD [API] | `2026-10-27 23:03:56` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,036.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.04K USD at 1.3303 USD [API] | `2026-10-27 23:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,692.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.69K USD at 1.3284 USD [API] | `2026-10-27 23:17:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,664.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.66K USD at 1.3267 USD [API] | `2026-10-27 23:19:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,245.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.25K USD at 1.3261 USD [API] | `2026-10-27 23:25:00` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,219.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.22K USD at 1.3259 USD [API] | `2026-10-27 23:24:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3259 USD [API] | `2026-10-27 23:24:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 101.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.3304 USD [API] | `2026-10-27 23:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,042.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.04K USD at 1.3280 USD [API] | `2026-10-27 23:30:56` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,004.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.00K USD at 1.3284 USD [API] | `2026-10-27 23:33:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,395.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.40K USD at 1.3284 USD [API] | `2026-10-27 23:33:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3284 USD [API] | `2026-10-27 23:33:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,347.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.35K USD at 1.3282 USD [API] | `2026-10-27 23:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3281 USD [API] | `2026-10-27 23:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 23,095.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 23.10K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,127.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.13K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,788.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.79K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 99.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.2928 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 139.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,786.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.79K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 50.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 49.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,798.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.80K USD at 1.2930 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,872.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.87K USD at 1.2930 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,687.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.69K USD at 1.2931 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,388.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.39K USD at 1.2931 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,777.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.78K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 536.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.54K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |


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
| `Live` | `Long Liquidation` | `0.2550` | 334,350.00 USD | 75,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 154.76 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 378.20 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 905.65 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 373.01 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 75,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 5,350.00 USD | 75,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 6,720.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 103.50 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,180.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,020.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 4,510.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 631.78 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,710.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 1,650.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 996.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 9,520.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 12,480.00 USD | 75,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 880.65 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 5,510.00 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 133,990.00 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 11,730.00 USD | 74,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 5,220.00 USD | 74,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 2,360.00 USD | 74,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 1,620.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 19,720.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 8,080.00 USD | 74,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 16,260.00 USD | 74,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 23,320.00 USD | 74,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 5,600.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 1,920.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 27,710.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 51,530.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 16,680.00 USD | 74,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 35,250.00 USD | 74,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,060.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 976.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 8,300.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 19,440.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 18,800.00 USD | 74,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 46,410.00 USD | 74,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 23,300.00 USD | 74,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 8,280.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 24,470.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 70,160.00 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 2,790,000.00 USD | 74,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 25,110.00 USD | 71,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 55,080.00 USD | 71,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 107,340.00 USD | 71,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 156,970.00 USD | 71,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 6,520.00 USD | 71,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 42,380.00 USD | 71,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 23,920.00 USD | 71,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 27,910.00 USD | 71,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,940.00 USD | 71,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 13,120.00 USD | 71,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 74,930.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 58,890.00 USD | 71,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 31,450.00 USD | 71,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 516,010.00 USD | 71,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 118,940.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 428,590.00 USD | 70,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 116,840.00 USD | 70,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 118,560.00 USD | 69,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 2,370,000.00 USD | 69,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 76,920.00 USD | 67,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 187,890.00 USD | 67,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 268,870.00 USD | 67,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 697,810.00 USD | 66,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 66,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 157,800.00 USD | 32,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 450,020.00 USD | 32,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 481,930.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 523,400.00 USD | 31,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 263,670.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 138,580.00 USD | 30,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 88,490.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,080,000.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 401,440.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 459,350.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 784,410.00 USD | 26,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 99,690.00 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 59,350.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 592,630.00 USD | 25,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 276,220.00 USD | 24,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 134,840,000.00 USD | 134,840,000.00 USD | 144,660.00 USD | 944.65 USD | 225,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 76,470.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 134,470,000.00 USD | 134,470,000.00 USD | 79,780.00 USD | 43,440.00 USD | 71,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 134,270,000.00 USD | 134,270,000.00 USD | 0.00 USD | 0.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 39,680,000.00 USD | 39,680,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 134,260,000.00 USD | 134,260,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 39,610,000.00 USD | 39,610,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 134,220,000.00 USD | 134,220,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 39,540,000.00 USD | 39,540,000.00 USD | 48,530.00 USD | 495.40 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 134,080,000.00 USD | 134,080,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 614,970.00 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 134,070,000.00 USD | 134,070,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 39,410,000.00 USD | 39,410,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 134,010,000.00 USD | 134,010,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 133,640,000.00 USD | 133,640,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 39,400,000.00 USD | 39,400,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 133,480,000.00 USD | 133,480,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 39,330,000.00 USD | 39,330,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 133,320,000.00 USD | 133,320,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 119,460.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 38,950,000.00 USD | 38,950,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 132,440,000.00 USD | 132,440,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 38,830,000.00 USD | 38,830,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 132,200,000.00 USD | 132,200,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 38,650,000.00 USD | 38,650,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 131,350,000.00 USD | 131,350,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 38,270,000.00 USD | 38,270,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 130,610,000.00 USD | 130,610,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 37,530,000.00 USD | 37,530,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 129,560,000.00 USD | 129,560,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,600,000.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 37,100,000.00 USD | 37,100,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 128,230,000.00 USD | 128,230,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 36,770,000.00 USD | 36,770,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 127,260,000.00 USD | 127,260,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 36,590,000.00 USD | 36,590,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 126,200,000.00 USD | 126,200,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 36,430,000.00 USD | 36,430,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 124,170,000.00 USD | 124,170,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 36,210,000.00 USD | 36,210,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 123,320,000.00 USD | 123,320,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,810.00 USD | 21,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 35,940,000.00 USD | 35,940,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 122,430,000.00 USD | 122,430,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 35,710,000.00 USD | 35,710,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 121,770,000.00 USD | 121,770,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 35,540,000.00 USD | 35,540,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 121,350,000.00 USD | 121,350,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 35,460,000.00 USD | 35,460,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 120,740,000.00 USD | 120,740,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 35,380,000.00 USD | 35,380,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 120,500,000.00 USD | 120,500,000.00 USD | 116,030.00 USD | 65,900.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,220,000.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 35,260,000.00 USD | 35,260,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 120,080,000.00 USD | 120,080,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 35,220,000.00 USD | 35,220,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 119,900,000.00 USD | 119,900,000.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 35,170,000.00 USD | 35,170,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 118,990,000.00 USD | 118,990,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 35,140,000.00 USD | 35,140,000.00 USD | 20,520.00 USD | 17,640.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 118,410,000.00 USD | 118,410,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 35,050,000.00 USD | 35,050,000.00 USD | 111,560.00 USD | 42,920.00 USD | 83,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 118,040,000.00 USD | 118,040,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 671,140.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 34,810,000.00 USD | 34,810,000.00 USD | 40,880.00 USD | 18,340.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 117,280,000.00 USD | 117,280,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 34,720,000.00 USD | 34,720,000.00 USD | 107,530.00 USD | 7,010.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 116,570,000.00 USD | 116,570,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 34,600,000.00 USD | 34,600,000.00 USD | 0.00 USD | 14,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 116,510,000.00 USD | 116,510,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 116,380,000.00 USD | 116,380,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 116,080,000.00 USD | 116,080,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 644,280.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 115,920,000.00 USD | 115,920,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 115,900,000.00 USD | 115,900,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 115,640,000.00 USD | 115,640,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 114,670,000.00 USD | 114,670,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 34,580,000.00 USD | 34,580,000.00 USD | 9,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 114,150,000.00 USD | 114,150,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 369,930.00 USD | 18,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 34,570,000.00 USD | 34,570,000.00 USD | 77,860.00 USD | 0.00 USD | 78,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 113,970,000.00 USD | 113,970,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 34,420,000.00 USD | 34,420,000.00 USD | 174,270.00 USD | 1,870.00 USD | 59,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 113,870,000.00 USD | 113,870,000.00 USD | 316,090.00 USD | 3,350.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 34,180,000.00 USD | 34,180,000.00 USD | 157,550.00 USD | 1,240.00 USD | 208,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 113,530,000.00 USD | 113,530,000.00 USD | 104,420.00 USD | 2,640.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 33,810,000.00 USD | 33,810,000.00 USD | 0.00 USD | 211.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 113,400,000.00 USD | 113,400,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 33,810,000.00 USD | 33,810,000.00 USD | 40,080.00 USD | 206.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 113,180,000.00 USD | 113,180,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,560,000.00 USD | 17,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 112,510,000.00 USD | 112,510,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 33,770,000.00 USD | 33,770,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 111,720,000.00 USD | 111,720,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 33,720,000.00 USD | 33,720,000.00 USD | 203,290.00 USD | 28,070.00 USD | 518,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 111,040,000.00 USD | 111,040,000.00 USD | 254,940.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,970,000.00 USD | 32,970,000.00 USD | 295,580.00 USD | 131,700.00 USD | 492,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 109,880,000.00 USD | 109,880,000.00 USD | 944,780.00 USD | 474,960.00 USD | 940,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,060,000.00 USD | 32,060,000.00 USD | 97,740.00 USD | 1,800.00 USD | 73,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 107,520,000.00 USD | 107,520,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 570,730.00 USD | 16,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 31,880,000.00 USD | 31,880,000.00 USD | 517,670.00 USD | 120,320.00 USD | 554,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 104,480,000.00 USD | 104,480,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 30,690,000.00 USD | 30,690,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 99,990,000.00 USD | 99,990,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 28,230,000.00 USD | 28,230,000.00 USD | 961,180.00 USD | 493,310.00 USD | 740,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 95,090,000.00 USD | 95,090,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 26,030,000.00 USD | 26,030,000.00 USD | 503,460.00 USD | 188,510.00 USD | 497,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 89,170,000.00 USD | 89,170,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 24,840,000.00 USD | 24,840,000.00 USD | 721,110.00 USD | 126,130.00 USD | 635,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 86,120,000.00 USD | 86,120,000.00 USD | 1,660,000.00 USD | 544,230.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 242,000.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 23,360,000.00 USD | 23,360,000.00 USD | 861,120.00 USD | 132,180.00 USD | 578,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 82,250,000.00 USD | 82,250,000.00 USD | 2,730,000.00 USD | 695,090.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 21,790,000.00 USD | 21,790,000.00 USD | 218,430.00 USD | 101,820.00 USD | 355,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 75,770,000.00 USD | 75,770,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 21,110,000.00 USD | 21,110,000.00 USD | 257,560.00 USD | 103,030.00 USD | 457,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 66,320,000.00 USD | 66,320,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 20,300,000.00 USD | 20,300,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 59,910,000.00 USD | 59,910,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 19,430,000.00 USD | 19,430,000.00 USD | 520,500.00 USD | 43,020.00 USD | 944,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 55,550,000.00 USD | 55,550,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 830,060.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 17,920,000.00 USD | 17,920,000.00 USD | 1,470,000.00 USD | 258,360.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 53,920,000.00 USD | 53,920,000.00 USD | 2,900,000.00 USD | 1,090,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 14,430,000.00 USD | 14,430,000.00 USD | 1,080,000.00 USD | 212,550.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 46,990,000.00 USD | 46,990,000.00 USD | 1,490,000.00 USD | 211,890.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 11,570,000.00 USD | 11,570,000.00 USD | 412,030.00 USD | 72,400.00 USD | 171,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 44,290,000.00 USD | 44,290,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 1,150,000.00 USD | 254,090.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 40,810,000.00 USD | 40,810,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 8,360,000.00 USD | 8,360,000.00 USD | 670,330.00 USD | 1,360,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 35,870,000.00 USD | 35,870,000.00 USD | 3,140,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 14,310,000.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 1,030,000.00 USD | 874,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 27,230,000.00 USD | 27,230,000.00 USD | 4,220,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 483,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 14,500,000.00 USD | 14,500,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 776,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 2,580,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 1,650,000.00 USD | 1,650,000.00 USD | 961,090.00 USD | 316,540.00 USD | 368,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 9,980,000.00 USD | 9,980,000.00 USD | 306,560.00 USD | 2,550,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 19,960,000.00 USD | 19,960,000.00 USD | 306,560.00 USD | 2,550,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 2,310,000.00 USD | 2,310,000.00 USD | 100,310.00 USD | 547,830.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 35,430,000.00 USD | 35,430,000.00 USD | 2,220,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 169,550.00 USD | 169,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 6,610,000.00 USD | 6,610,000.00 USD | 105,090.00 USD | 1,280,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 47,910,000.00 USD | 47,910,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 20,040,000.00 USD | 20,040,000.00 USD | 6,170,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 63,640,000.00 USD | 63,640,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 21,990,000.00 USD | 21,990,000.00 USD | 188,330.00 USD | 1,450,000.00 USD | 312,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 65,140,000.00 USD | 65,140,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 22,750,000.00 USD | 22,750,000.00 USD | 547,110.00 USD | 0.00 USD | 210,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 66,270,000.00 USD | 66,270,000.00 USD | 1,030,000.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 24,320,000.00 USD | 24,320,000.00 USD | 578,780.00 USD | 161,530.00 USD | 834,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 66,820,000.00 USD | 66,820,000.00 USD | 417,680.00 USD | 6,660.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 24,790,000.00 USD | 24,790,000.00 USD | 143,950.00 USD | 327,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 68,220,000.00 USD | 68,220,000.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 25,280,000.00 USD | 25,280,000.00 USD | 382,250.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 68,660,000.00 USD | 68,660,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 25,300,000.00 USD | 25,300,000.00 USD | 18,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 69,130,000.00 USD | 69,130,000.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 27,030,000.00 USD | 27,030,000.00 USD | 349,940.00 USD | 0.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 70,820,000.00 USD | 70,820,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 30,690,000.00 USD | 30,690,000.00 USD | 1,110,000.00 USD | 113,790.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 74,240,000.00 USD | 74,240,000.00 USD | 1,740,000.00 USD | 6,700.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 35,590,000.00 USD | 35,590,000.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 81,170,000.00 USD | 81,170,000.00 USD | 1,940,000.00 USD | 1,570,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 36,220,000.00 USD | 36,220,000.00 USD | 344,680.00 USD | 422.50 USD | 288,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 82,410,000.00 USD | 82,410,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 83,380,000.00 USD | 83,380,000.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 39,080,000.00 USD | 39,080,000.00 USD | 602,010.00 USD | 910,970.00 USD | 659,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 84,240,000.00 USD | 84,240,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 39,490,000.00 USD | 39,490,000.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 86,190,000.00 USD | 86,190,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 900.45 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 40,620,000.00 USD | 40,620,000.00 USD | 493,480.00 USD | 313,760.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 88,130,000.00 USD | 88,130,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 43,130,000.00 USD | 43,130,000.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 92,360,000.00 USD | 92,360,000.00 USD | 1,240,000.00 USD | 590,530.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 45,630,000.00 USD | 45,630,000.00 USD | 890,710.00 USD | 396,100.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 94,120,000.00 USD | 94,120,000.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 48,460,000.00 USD | 48,460,000.00 USD | 1,700,000.00 USD | 444,160.00 USD | 688,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 97,870,000.00 USD | 97,870,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 50,170,000.00 USD | 50,170,000.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 99,020,000.00 USD | 99,020,000.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 86,800.00 USD | 91,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 56,150,000.00 USD | 56,150,000.00 USD | 222,150.00 USD | 1,830,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 103,210,000.00 USD | 103,210,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 63,180,000.00 USD | 63,180,000.00 USD | 2,310,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 108,050,000.00 USD | 108,050,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 66,530,000.00 USD | 66,530,000.00 USD | 1,680,000.00 USD | 689,260.00 USD | 980,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 110,070,000.00 USD | 110,070,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 71,160,000.00 USD | 71,160,000.00 USD | 1,870,000.00 USD | 843,870.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 113,270,000.00 USD | 113,270,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 74,160,000.00 USD | 74,160,000.00 USD | 1,770,000.00 USD | 259,620.00 USD | 968,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 115,890,000.00 USD | 115,890,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 54,470.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 76,450,000.00 USD | 76,450,000.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 117,700,000.00 USD | 117,700,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 78,640,000.00 USD | 78,640,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 118,750,000.00 USD | 118,750,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 81,080,000.00 USD | 81,080,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 120,370,000.00 USD | 120,370,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 83,340,000.00 USD | 83,340,000.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 122,790,000.00 USD | 122,790,000.00 USD | 829,540.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 85,670,000.00 USD | 85,670,000.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 124,820,000.00 USD | 124,820,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 52,400.00 USD | 198,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 88,110,000.00 USD | 88,110,000.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 126,370,000.00 USD | 126,370,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 90,790,000.00 USD | 90,790,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 128,810,000.00 USD | 128,810,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 94,030,000.00 USD | 94,030,000.00 USD | 1,470,000.00 USD | 549,090.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 130,670,000.00 USD | 130,670,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 97,750,000.00 USD | 97,750,000.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 136,590,000.00 USD | 136,590,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 101,760,000.00 USD | 101,760,000.00 USD | 2,140,000.00 USD | 696,110.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 143,820,000.00 USD | 143,820,000.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 161,520.00 USD | 359,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 103,070,000.00 USD | 103,070,000.00 USD | 498,430.00 USD | 331,800.00 USD | 481,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 154,570,000.00 USD | 154,570,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 104,330,000.00 USD | 104,330,000.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 163,400,000.00 USD | 163,400,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 105,820,000.00 USD | 105,820,000.00 USD | 771,840.00 USD | 230,360.00 USD | 490,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 172,610,000.00 USD | 172,610,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 107,160,000.00 USD | 107,160,000.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 181,860,000.00 USD | 181,860,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 109,020,000.00 USD | 109,020,000.00 USD | 805,600.00 USD | 299,340.00 USD | 757,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 189,400,000.00 USD | 189,400,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 4,370.00 USD | 364,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 110,400,000.00 USD | 110,400,000.00 USD | 565,230.00 USD | 199,730.00 USD | 611,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 196,560,000.00 USD | 196,560,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 111,620,000.00 USD | 111,620,000.00 USD | 732,680.00 USD | 76,930.00 USD | 416,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 199,090,000.00 USD | 199,090,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 112,120,000.00 USD | 112,120,000.00 USD | 266,880.00 USD | 118,570.00 USD | 116,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 202,160,000.00 USD | 202,160,000.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 112,770,000.00 USD | 112,770,000.00 USD | 222,740.00 USD | 103,400.00 USD | 317,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 205,940,000.00 USD | 205,940,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 112,910,000.00 USD | 112,910,000.00 USD | 80,160.00 USD | 26,460.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 208,690,000.00 USD | 208,690,000.00 USD | 1,430,000.00 USD | 614,410.00 USD | 702,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 198,460.00 USD | 562,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 113,080,000.00 USD | 113,080,000.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 209,430,000.00 USD | 209,430,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 113,270,000.00 USD | 113,270,000.00 USD | 84,710.00 USD | 57,700.00 USD | 44,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 210,540,000.00 USD | 210,540,000.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 113,450,000.00 USD | 113,450,000.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 212,130,000.00 USD | 212,130,000.00 USD | 477,130.00 USD | 362,580.00 USD | 755,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 113,590,000.00 USD | 113,590,000.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 214,200,000.00 USD | 214,200,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 113,730,000.00 USD | 113,730,000.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 216,320,000.00 USD | 216,320,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 464.75 USD | 562,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 113,980,000.00 USD | 113,980,000.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 217,990,000.00 USD | 217,990,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 114,490,000.00 USD | 114,490,000.00 USD | 231,710.00 USD | 71,960.00 USD | 200,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 219,540,000.00 USD | 219,540,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 115,050,000.00 USD | 115,050,000.00 USD | 314,100.00 USD | 98,360.00 USD | 149,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 221,580,000.00 USD | 221,580,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 115,300,000.00 USD | 115,300,000.00 USD | 106,800.00 USD | 53,840.00 USD | 92,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 223,860,000.00 USD | 223,860,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 115,670,000.00 USD | 115,670,000.00 USD | 300,730.00 USD | 17,520.00 USD | 52,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 224,550,000.00 USD | 224,550,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 36,950.00 USD | 599,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 115,710,000.00 USD | 115,710,000.00 USD | 0.00 USD | 35,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 225,470,000.00 USD | 225,470,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 226,340,000.00 USD | 226,340,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 227,070,000.00 USD | 227,070,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 115,710,000.00 USD | 115,710,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 227,400,000.00 USD | 227,400,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 115,780,000.00 USD | 115,780,000.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 227,460,000.00 USD | 227,460,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 177,010.00 USD | 776,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 115,850,000.00 USD | 115,850,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 227,680,000.00 USD | 227,680,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 115,980,000.00 USD | 115,980,000.00 USD | 48,530.00 USD | 495.40 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 227,690,000.00 USD | 227,690,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 227,750,000.00 USD | 227,750,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 227,830,000.00 USD | 227,830,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 116,000,000.00 USD | 116,000,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 228,120,000.00 USD | 228,120,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 1,110.00 USD | 778,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 228,280,000.00 USD | 228,280,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 116,060,000.00 USD | 116,060,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 228,440,000.00 USD | 228,440,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 116,440,000.00 USD | 116,440,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 229,320,000.00 USD | 229,320,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 116,570,000.00 USD | 116,570,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 229,560,000.00 USD | 229,560,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 116,570,000.00 USD | 116,570,000.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 229,850,000.00 USD | 229,850,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 781,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 116,740,000.00 USD | 116,740,000.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 230,410,000.00 USD | 230,410,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 117,120,000.00 USD | 117,120,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 231,150,000.00 USD | 231,150,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 117,860,000.00 USD | 117,860,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 232,200,000.00 USD | 232,200,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 118,290,000.00 USD | 118,290,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 233,540,000.00 USD | 233,540,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 118,370,000.00 USD | 118,370,000.00 USD | 9,670.00 USD | 54,510.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 233,730,000.00 USD | 233,730,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 94,400.00 USD | 876,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 118,580,000.00 USD | 118,580,000.00 USD | 99,870.00 USD | 35,450.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 234,500,000.00 USD | 234,500,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 235,570,000.00 USD | 235,570,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 237,590,000.00 USD | 237,590,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 238,440,000.00 USD | 238,440,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 239,330,000.00 USD | 239,330,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 32,780.00 USD | 909,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 239,360,000.00 USD | 239,360,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 239,990,000.00 USD | 239,990,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 240,410,000.00 USD | 240,410,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 241,020,000.00 USD | 241,020,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 241,260,000.00 USD | 241,260,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 588,370.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 241,360,000.00 USD | 241,360,000.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 241,680,000.00 USD | 241,680,000.00 USD | 65,610.00 USD | 26,800.00 USD | 226,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 241,860,000.00 USD | 241,860,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 242,780,000.00 USD | 242,780,000.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 243,330,000.00 USD | 243,330,000.00 USD | 193,090.00 USD | 81,140.00 USD | 278,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 243,530,000.00 USD | 243,530,000.00 USD | 58,970.00 USD | 42,150.00 USD | 100,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 3,360.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 41,640.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 10,700.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 40,610.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 734.44 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 6,630.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 234.85 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,010.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 5,260,000.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 599.17 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 3,350.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 5,010,000.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 135,930.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 18,860.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 242.38 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,690.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 15,070.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,960.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 149.17 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 4,010.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 838.53 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 406.98 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 3,060,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 6,300.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 732.73 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,340.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 219.38 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 13,850.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 5,760.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 9,900.00 USD | 15,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 113,600.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 620,680.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 1,760.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 318,940.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 401.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 971.23 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 1,810.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 241,070.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,330.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 40,840.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,250,000.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 173,550.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 515.05 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,730.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 703.57 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 2,820.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 8,920.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 2,320,000.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 1,350.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 4,010.00 USD | 22,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 12,490.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 51,650.00 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 22,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 67,070.00 USD | 22,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 5,770.00 USD | 22,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 77,580.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,670.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 90,600.00 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,870.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 950,110.00 USD | 23,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 257.58 USD | 23,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 181,260.00 USD | 23,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 92,830.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,590.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 1,120.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,720.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 311.79 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 4,190.00 USD | 24,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 14,040.00 USD | 24,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 4,730.00 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,970.00 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 496.86 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 117.07 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 11,280.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 187.25 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 75,490,000.00 USD | 0.00 USD | 334,350.00 USD | `-80.11%` | `1,311,184.00` |
| `Live` | `Long` | `0.2650` | 75,160,000.00 USD | 0.00 USD | 154.76 USD | `-79.33%` | `584.00` |
| `Live` | `Long` | `0.2850` | 75,160,000.00 USD | 0.00 USD | 378.20 USD | `-77.77%` | `1,327.00` |
| `Live` | `Long` | `0.2950` | 75,160,000.00 USD | 0.00 USD | 905.65 USD | `-76.99%` | `3,070.00` |
| `Live` | `Long` | `0.3050` | 75,160,000.00 USD | 0.00 USD | 373.01 USD | `-76.21%` | `1,223.00` |
| `Live` | `Long` | `0.3150` | 75,150,000.00 USD | 0.00 USD | 4,910.00 USD | `-75.43%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 75,150,000.00 USD | 0.00 USD | 5,350.00 USD | `-74.65%` | `16,466.00` |
| `Live` | `Long` | `0.3350` | 75,140,000.00 USD | 0.00 USD | 6,720.00 USD | `-73.87%` | `20,071.00` |
| `Live` | `Long` | `0.3450` | 75,140,000.00 USD | 0.00 USD | 103.50 USD | `-73.09%` | `300.00` |
| `Live` | `Long` | `0.3550` | 75,140,000.00 USD | 0.00 USD | 2,180.00 USD | `-72.31%` | `6,137.00` |
| `Live` | `Long` | `0.3650` | 75,140,000.00 USD | 0.00 USD | 1,020.00 USD | `-71.53%` | `2,790.00` |
| `Live` | `Long` | `0.3750` | 75,130,000.00 USD | 0.00 USD | 4,510.00 USD | `-70.75%` | `12,021.00` |
| `Live` | `Long` | `0.3850` | 75,130,000.00 USD | 0.00 USD | 631.78 USD | `-69.97%` | `1,641.00` |
| `Live` | `Long` | `0.3950` | 75,130,000.00 USD | 0.00 USD | 1,710.00 USD | `-69.19%` | `4,340.00` |
| `Live` | `Long` | `0.4050` | 75,130,000.00 USD | 0.00 USD | 1,650.00 USD | `-68.41%` | `4,073.00` |
| `Live` | `Long` | `0.4150` | 75,130,000.00 USD | 0.00 USD | 996.00 USD | `-67.63%` | `2,400.00` |
| `Live` | `Long` | `0.4250` | 75,130,000.00 USD | 0.00 USD | 9,520.00 USD | `-66.85%` | `22,401.00` |
| `Live` | `Long` | `0.4350` | 75,120,000.00 USD | 0.00 USD | 12,480.00 USD | `-66.07%` | `28,690.00` |
| `Live` | `Long` | `0.4450` | 75,100,000.00 USD | 0.00 USD | 880.65 USD | `-65.29%` | `1,979.00` |
| `Live` | `Long` | `0.4550` | 75,100,000.00 USD | 0.00 USD | 5,510.00 USD | `-64.51%` | `12,100.00` |
| `Live` | `Long` | `0.4650` | 75,100,000.00 USD | 0.00 USD | 133,990.00 USD | `-63.73%` | `288,140.00` |
| `Live` | `Long` | `0.4750` | 74,960,000.00 USD | 0.00 USD | 11,730.00 USD | `-62.95%` | `24,687.00` |
| `Live` | `Long` | `0.4850` | 74,950,000.00 USD | 0.00 USD | 5,220.00 USD | `-62.17%` | `10,755.00` |
| `Live` | `Long` | `0.4950` | 74,950,000.00 USD | 0.00 USD | 2,360.00 USD | `-61.39%` | `4,766.00` |
| `Live` | `Long` | `0.5050` | 74,940,000.00 USD | 0.00 USD | 1,620.00 USD | `-60.61%` | `3,199.00` |
| `Live` | `Long` | `0.5150` | 74,940,000.00 USD | 0.00 USD | 19,720.00 USD | `-59.83%` | `38,298.00` |
| `Live` | `Long` | `0.5250` | 74,920,000.00 USD | 0.00 USD | 8,080.00 USD | `-59.05%` | `15,391.00` |
| `Live` | `Long` | `0.5350` | 74,910,000.00 USD | 0.00 USD | 16,260.00 USD | `-58.27%` | `30,395.00` |
| `Live` | `Long` | `0.5450` | 74,900,000.00 USD | 0.00 USD | 23,320.00 USD | `-57.49%` | `42,797.00` |
| `Live` | `Long` | `0.5550` | 74,870,000.00 USD | 0.00 USD | 5,600.00 USD | `-56.72%` | `10,087.00` |
| `Live` | `Long` | `0.5650` | 74,870,000.00 USD | 0.00 USD | 1,920.00 USD | `-55.94%` | `3,392.00` |
| `Live` | `Long` | `0.5750` | 74,870,000.00 USD | 0.00 USD | 27,710.00 USD | `-55.16%` | `48,190.00` |
| `Live` | `Long` | `0.5950` | 74,840,000.00 USD | 0.00 USD | 51,530.00 USD | `-53.60%` | `86,604.00` |
| `Live` | `Long` | `0.6050` | 74,790,000.00 USD | 0.00 USD | 16,680.00 USD | `-52.82%` | `27,571.00` |
| `Live` | `Long` | `0.6150` | 74,770,000.00 USD | 0.00 USD | 35,250.00 USD | `-52.04%` | `57,311.00` |
| `Live` | `Long` | `0.6250` | 74,740,000.00 USD | 0.00 USD | 1,060.00 USD | `-51.26%` | `1,704.00` |
| `Live` | `Long` | `0.6350` | 74,730,000.00 USD | 0.00 USD | 976.00 USD | `-50.48%` | `1,537.00` |
| `Live` | `Long` | `0.6450` | 74,730,000.00 USD | 0.00 USD | 8,300.00 USD | `-49.70%` | `12,875.00` |
| `Live` | `Long` | `0.6550` | 74,730,000.00 USD | 0.00 USD | 19,440.00 USD | `-48.92%` | `29,679.00` |
| `Live` | `Long` | `0.6650` | 74,710,000.00 USD | 0.00 USD | 18,800.00 USD | `-48.14%` | `28,277.00` |
| `Live` | `Long` | `0.6750` | 74,690,000.00 USD | 0.00 USD | 46,410.00 USD | `-47.36%` | `68,753.00` |
| `Live` | `Long` | `0.6850` | 74,640,000.00 USD | 0.00 USD | 23,300.00 USD | `-46.58%` | `34,021.00` |
| `Live` | `Long` | `0.6950` | 74,620,000.00 USD | 0.00 USD | 8,280.00 USD | `-45.80%` | `11,914.00` |
| `Live` | `Long` | `0.7050` | 74,610,000.00 USD | 0.00 USD | 24,470.00 USD | `-45.02%` | `34,716.00` |
| `Live` | `Long` | `0.7150` | 74,580,000.00 USD | 0.00 USD | 70,160.00 USD | `-44.24%` | `98,129.00` |
| `Live` | `Long` | `0.7250` | 74,510,000.00 USD | 0.00 USD | 2,790,000.00 USD | `-43.46%` | `3,847,640.00` |
| `Live` | `Long` | `0.7350` | 71,730,000.00 USD | 0.00 USD | 25,110.00 USD | `-42.68%` | `34,166.00` |
| `Live` | `Long` | `0.7450` | 71,700,000.00 USD | 0.00 USD | 55,080.00 USD | `-41.90%` | `73,927.00` |
| `Live` | `Long` | `0.7550` | 71,640,000.00 USD | 0.00 USD | 107,340.00 USD | `-41.12%` | `142,167.00` |
| `Live` | `Long` | `0.7650` | 71,540,000.00 USD | 0.00 USD | 156,970.00 USD | `-40.34%` | `205,196.00` |
| `Live` | `Long` | `0.7750` | 71,380,000.00 USD | 0.00 USD | 6,520.00 USD | `-39.56%` | `8,409.00` |
| `Live` | `Long` | `0.7850` | 71,370,000.00 USD | 0.00 USD | 42,380.00 USD | `-38.78%` | `53,984.00` |
| `Live` | `Long` | `0.7950` | 71,330,000.00 USD | 0.00 USD | 23,920.00 USD | `-38.00%` | `30,093.00` |
| `Live` | `Long` | `0.8050` | 71,310,000.00 USD | 0.00 USD | 27,910.00 USD | `-37.22%` | `34,674.00` |
| `Live` | `Long` | `0.8150` | 71,280,000.00 USD | 0.00 USD | 22,940.00 USD | `-36.44%` | `28,152.00` |
| `Live` | `Long` | `0.8250` | 71,260,000.00 USD | 0.00 USD | 13,120.00 USD | `-35.66%` | `15,905.00` |
| `Live` | `Long` | `0.8350` | 71,240,000.00 USD | 0.00 USD | 74,930.00 USD | `-34.88%` | `89,742.00` |
| `Live` | `Long` | `0.8450` | 71,170,000.00 USD | 0.00 USD | 58,890.00 USD | `-34.10%` | `69,688.00` |
| `Live` | `Long` | `0.8550` | 71,110,000.00 USD | 0.00 USD | 31,450.00 USD | `-33.32%` | `36,784.00` |
| `Live` | `Long` | `0.8650` | 71,080,000.00 USD | 0.00 USD | 516,010.00 USD | `-32.54%` | `596,538.00` |
| `Live` | `Long` | `0.8750` | 70,560,000.00 USD | 0.00 USD | 118,940.00 USD | `-31.76%` | `135,937.00` |
| `Live` | `Long` | `0.8850` | 70,440,000.00 USD | 0.00 USD | 428,590.00 USD | `-30.98%` | `484,277.00` |
| `Live` | `Long` | `0.8950` | 70,010,000.00 USD | 0.00 USD | 116,840.00 USD | `-30.20%` | `130,546.00` |
| `Live` | `Long` | `0.9050` | 69,900,000.00 USD | 0.00 USD | 118,560.00 USD | `-29.42%` | `131,002.00` |
| `Live` | `Long` | `0.9150` | 69,780,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-28.64%` | `2,593,953.00` |
| `Live` | `Long` | `0.9250` | 67,410,000.00 USD | 0.00 USD | 76,920.00 USD | `-27.86%` | `83,155.00` |
| `Live` | `Long` | `0.9350` | 67,330,000.00 USD | 0.00 USD | 187,890.00 USD | `-27.08%` | `200,956.00` |
| `Live` | `Long` | `0.9450` | 67,140,000.00 USD | 0.00 USD | 268,870.00 USD | `-26.30%` | `284,522.00` |
| `Live` | `Long` | `0.9550` | 66,870,000.00 USD | 0.00 USD | 697,810.00 USD | `-25.52%` | `730,689.00` |
| `Live` | `Long` | `0.9650` | 66,170,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-24.74%` | `35,153,532.00` |
| `Live` | `Long` | `0.9750` | 32,250,000.00 USD | 0.00 USD | 157,800.00 USD | `-23.96%` | `161,850.00` |
| `Live` | `Long` | `0.9850` | 32,090,000.00 USD | 0.00 USD | 450,020.00 USD | `-23.18%` | `456,870.00` |
| `Live` | `Long` | `0.9950` | 31,640,000.00 USD | 0.00 USD | 481,930.00 USD | `-22.40%` | `484,347.00` |
| `Live` | `Long` | `1.00` | 31,160,000.00 USD | 0.00 USD | 523,400.00 USD | `-21.62%` | `520,792.00` |
| `Live` | `Long` | `1.01` | 30,640,000.00 USD | 0.00 USD | 263,670.00 USD | `-20.84%` | `259,774.00` |
| `Live` | `Long` | `1.02` | 30,370,000.00 USD | 0.00 USD | 138,580.00 USD | `-20.06%` | `135,203.00` |
| `Live` | `Long` | `1.03` | 30,240,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-19.28%` | `2,045,946.00` |
| `Live` | `Long` | `1.04` | 28,120,000.00 USD | 0.00 USD | 88,490.00 USD | `-18.50%` | `84,684.00` |
| `Live` | `Long` | `1.05` | 28,030,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-17.72%` | `1,021,357.00` |
| `Live` | `Long` | `1.06` | 26,950,000.00 USD | 0.00 USD | 401,440.00 USD | `-16.94%` | `376,943.00` |
| `Live` | `Long` | `1.07` | 26,550,000.00 USD | 0.00 USD | 459,350.00 USD | `-16.16%` | `427,300.00` |
| `Live` | `Long` | `1.08` | 26,090,000.00 USD | 0.00 USD | 784,410.00 USD | `-15.38%` | `722,954.00` |
| `Live` | `Long` | `1.09` | 25,310,000.00 USD | 0.00 USD | 99,690.00 USD | `-14.60%` | `91,042.00` |
| `Live` | `Long` | `1.10` | 25,210,000.00 USD | 0.00 USD | 59,350.00 USD | `-13.82%` | `53,706.00` |
| `Live` | `Long` | `1.11` | 25,150,000.00 USD | 0.00 USD | 592,630.00 USD | `-13.04%` | `531,506.00` |
| `Live` | `Long` | `1.12` | 24,560,000.00 USD | 0.00 USD | 276,220.00 USD | `-12.26%` | `245,528.00` |
| `Live` | `Long` | `1.14` | 24,280,000.00 USD | 0.00 USD | 76,470.00 USD | `-11.48%` | `67,372.00` |
| `Live` | `Long` | `1.15` | 24,200,000.00 USD | 0.00 USD | 614,970.00 USD | `-10.70%` | `537,095.00` |
| `Live` | `Long` | `1.16` | 23,590,000.00 USD | 0.00 USD | 119,460.00 USD | `-9.92%` | `103,428.00` |
| `Live` | `Long` | `1.17` | 23,470,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-9.14%` | `1,375,427.00` |
| `Live` | `Long` | `1.18` | 21,870,000.00 USD | 0.00 USD | 274,810.00 USD | `-8.36%` | `233,878.00` |
| `Live` | `Long` | `1.19` | 21,590,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-7.58%` | `1,874,152.00` |
| `Live` | `Long` | `1.20` | 19,370,000.00 USD | 0.00 USD | 671,140.00 USD | `-6.80%` | `561,627.00` |
| `Live` | `Long` | `1.21` | 18,700,000.00 USD | 0.00 USD | 644,280.00 USD | `-6.02%` | `534,673.00` |
| `Live` | `Long` | `1.22` | 18,050,000.00 USD | 0.00 USD | 369,930.00 USD | `-5.24%` | `304,470.00` |
| `Live` | `Long` | `1.23` | 17,690,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-4.46%` | `1,273,262.00` |
| `Live` | `Long` | `1.24` | 16,130,000.00 USD | 0.00 USD | 570,730.00 USD | `-3.68%` | `462,127.00` |
| `Live` | `Long` | `1.25` | 15,550,000.00 USD | 0.00 USD | 242,000.00 USD | `-2.90%` | `194,380.00` |
| `Live` | `Long` | `1.25` | 15,310,000.00 USD | 0.00 USD | 830,060.00 USD | `-2.12%` | `661,400.00` |
| `Live` | `Long` | `1.26` | 14,480,000.00 USD | 0.00 USD | 14,310,000.00 USD | `-1.34%` | `11,314,602.00` |
| `Live` | `Long` | `1.27` | 169,550.00 USD | 0.00 USD | 169,550.00 USD | `-0.56%` | `132,978.00` |
| `Live` | `Short` | `1.29` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | `+1.00%` | `2,770.00` |
| `Live` | `Short` | `1.30` | 4,490.00 USD | 900.45 USD | 0.00 USD | `+1.78%` | `690.00` |
| `Live` | `Short` | `1.31` | 91,290.00 USD | 86,800.00 USD | 0.00 USD | `+2.56%` | `66,008.00` |
| `Live` | `Short` | `1.32` | 145,760.00 USD | 54,470.00 USD | 0.00 USD | `+3.34%` | `41,110.00` |
| `Live` | `Short` | `1.33` | 198,160.00 USD | 52,400.00 USD | 0.00 USD | `+4.12%` | `39,254.00` |
| `Live` | `Short` | `1.34` | 359,680.00 USD | 161,520.00 USD | 0.00 USD | `+4.90%` | `120,086.00` |
| `Live` | `Short` | `1.35` | 364,050.00 USD | 4,370.00 USD | 0.00 USD | `+5.68%` | `3,224.00` |
| `Live` | `Short` | `1.36` | 562,510.00 USD | 198,460.00 USD | 0.00 USD | `+6.46%` | `145,394.00` |
| `Live` | `Short` | `1.38` | 562,970.00 USD | 464.75 USD | 0.00 USD | `+7.24%` | `338.00` |
| `Live` | `Short` | `1.39` | 599,920.00 USD | 36,950.00 USD | 0.00 USD | `+8.02%` | `26,678.00` |
| `Live` | `Short` | `1.40` | 776,940.00 USD | 177,010.00 USD | 0.00 USD | `+8.80%` | `126,891.00` |
| `Live` | `Short` | `1.41` | 778,050.00 USD | 1,110.00 USD | 0.00 USD | `+9.58%` | `793.00` |
| `Live` | `Short` | `1.42` | 781,910.00 USD | 3,860.00 USD | 0.00 USD | `+10.36%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 876,310.00 USD | 94,400.00 USD | 0.00 USD | `+11.14%` | `66,249.00` |
| `Live` | `Short` | `1.44` | 909,100.00 USD | 32,780.00 USD | 0.00 USD | `+11.92%` | `22,845.00` |
| `Live` | `Short` | `1.45` | 1,500,000.00 USD | 588,370.00 USD | 0.00 USD | `+12.70%` | `407,175.00` |
| `Live` | `Short` | `1.46` | 1,500,000.00 USD | 3,360.00 USD | 0.00 USD | `+13.48%` | `2,310.00` |
| `Live` | `Short` | `1.47` | 1,540,000.00 USD | 41,640.00 USD | 0.00 USD | `+14.26%` | `28,425.00` |
| `Live` | `Short` | `1.48` | 1,550,000.00 USD | 10,700.00 USD | 0.00 USD | `+15.04%` | `7,254.00` |
| `Live` | `Short` | `1.49` | 1,590,000.00 USD | 40,610.00 USD | 0.00 USD | `+15.82%` | `27,347.00` |
| `Live` | `Short` | `1.50` | 1,610,000.00 USD | 11,950.00 USD | 0.00 USD | `+16.60%` | `7,994.00` |
| `Live` | `Short` | `1.50` | 1,610,000.00 USD | 734.44 USD | 0.00 USD | `+17.38%` | `488.00` |
| `Live` | `Short` | `1.51` | 1,610,000.00 USD | 6,630.00 USD | 0.00 USD | `+18.16%` | `4,373.00` |
| `Live` | `Short` | `1.52` | 1,610,000.00 USD | 234.85 USD | 0.00 USD | `+18.94%` | `154.00` |
| `Live` | `Short` | `1.53` | 1,610,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.72%` | `658.00` |
| `Live` | `Short` | `1.54` | 1,620,000.00 USD | 1,370.00 USD | 0.00 USD | `+20.50%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,620,000.00 USD | 1,360.00 USD | 0.00 USD | `+21.28%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,620,000.00 USD | 555.57 USD | 0.00 USD | `+22.06%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,620,000.00 USD | 2,840.00 USD | 0.00 USD | `+22.84%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 6,880,000.00 USD | 5,260,000.00 USD | 0.00 USD | `+23.62%` | `3,320,020.00` |
| `Live` | `Short` | `1.61` | 6,880,000.00 USD | 599.17 USD | 0.00 USD | `+25.96%` | `371.00` |
| `Live` | `Short` | `1.62` | 6,890,000.00 USD | 3,350.00 USD | 0.00 USD | `+26.74%` | `2,063.00` |
| `Live` | `Short` | `1.64` | 6,900,000.00 USD | 11,270.00 USD | 0.00 USD | `+27.52%` | `6,892.00` |
| `Live` | `Short` | `1.66` | 11,900,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+29.08%` | `3,025,200.00` |
| `Live` | `Short` | `1.67` | 12,040,000.00 USD | 135,930.00 USD | 0.00 USD | `+29.85%` | `81,640.00` |
| `Live` | `Short` | `1.68` | 12,040,000.00 USD | 760.45 USD | 0.00 USD | `+30.63%` | `454.00` |
| `Live` | `Short` | `1.69` | 12,060,000.00 USD | 18,860.00 USD | 0.00 USD | `+31.41%` | `11,195.00` |
| `Live` | `Short` | `1.70` | 12,060,000.00 USD | 242.38 USD | 0.00 USD | `+32.19%` | `143.00` |
| `Live` | `Short` | `1.71` | 12,060,000.00 USD | 1,980.00 USD | 0.00 USD | `+32.97%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 12,060,000.00 USD | 1,690.00 USD | 0.00 USD | `+34.53%` | `977.00` |
| `Live` | `Short` | `1.74` | 12,080,000.00 USD | 15,070.00 USD | 0.00 USD | `+35.31%` | `8,683.00` |
| `Live` | `Short` | `1.75` | 12,080,000.00 USD | 2,960.00 USD | 0.00 USD | `+36.09%` | `1,699.00` |
| `Live` | `Short` | `1.75` | 12,080,000.00 USD | 149.17 USD | 0.00 USD | `+36.87%` | `85.00` |
| `Live` | `Short` | `1.76` | 12,080,000.00 USD | 808.37 USD | 0.00 USD | `+37.65%` | `458.00` |
| `Live` | `Short` | `1.78` | 12,210,000.00 USD | 129,540.00 USD | 0.00 USD | `+39.21%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 12,220,000.00 USD | 4,010.00 USD | 0.00 USD | `+39.99%` | `2,232.00` |
| `Live` | `Short` | `1.80` | 12,220,000.00 USD | 889.87 USD | 0.00 USD | `+40.77%` | `493.00` |
| `Live` | `Short` | `1.81` | 12,220,000.00 USD | 838.53 USD | 0.00 USD | `+41.55%` | `462.00` |
| `Live` | `Short` | `1.82` | 12,220,000.00 USD | 406.98 USD | 0.00 USD | `+42.33%` | `223.00` |
| `Live` | `Short` | `1.83` | 15,280,000.00 USD | 3,060,000.00 USD | 0.00 USD | `+43.11%` | `1,666,029.00` |
| `Live` | `Short` | `1.84` | 15,280,000.00 USD | 6,300.00 USD | 0.00 USD | `+43.89%` | `3,415.00` |
| `Live` | `Short` | `1.85` | 15,280,000.00 USD | 732.73 USD | 0.00 USD | `+44.67%` | `395.00` |
| `Live` | `Short` | `1.86` | 15,290,000.00 USD | 2,340.00 USD | 0.00 USD | `+45.45%` | `1,255.00` |
| `Live` | `Short` | `1.88` | 15,290,000.00 USD | 219.38 USD | 0.00 USD | `+46.23%` | `117.00` |
| `Live` | `Short` | `1.89` | 15,300,000.00 USD | 13,850.00 USD | 0.00 USD | `+47.01%` | `7,347.00` |
| `Live` | `Short` | `1.90` | 15,310,000.00 USD | 5,760.00 USD | 0.00 USD | `+47.79%` | `3,039.00` |
| `Live` | `Short` | `1.91` | 15,320,000.00 USD | 9,900.00 USD | 0.00 USD | `+48.57%` | `5,196.00` |
| `Live` | `Short` | `1.94` | 15,430,000.00 USD | 113,600.00 USD | 0.00 USD | `+50.91%` | `58,706.00` |
| `Live` | `Short` | `1.96` | 15,430,000.00 USD | 293.25 USD | 0.00 USD | `+52.47%` | `150.00` |
| `Live` | `Short` | `1.97` | 16,050,000.00 USD | 620,680.00 USD | 0.00 USD | `+53.25%` | `315,869.00` |
| `Live` | `Short` | `1.98` | 16,050,000.00 USD | 1,760.00 USD | 0.00 USD | `+54.03%` | `891.00` |
| `Live` | `Short` | `1.99` | 16,370,000.00 USD | 318,940.00 USD | 0.00 USD | `+54.81%` | `160,677.00` |
| `Live` | `Short` | `2.00` | 16,370,000.00 USD | 401.00 USD | 0.00 USD | `+56.37%` | `200.00` |
| `Live` | `Short` | `2.02` | 16,370,000.00 USD | 971.23 USD | 0.00 USD | `+57.15%` | `482.00` |
| `Live` | `Short` | `2.04` | 16,370,000.00 USD | 1,810.00 USD | 0.00 USD | `+59.49%` | `886.00` |
| `Live` | `Short` | `2.06` | 16,610,000.00 USD | 241,070.00 USD | 0.00 USD | `+60.27%` | `117,308.00` |
| `Live` | `Short` | `2.06` | 16,620,000.00 USD | 5,330.00 USD | 0.00 USD | `+61.05%` | `2,583.00` |
| `Live` | `Short` | `2.08` | 16,660,000.00 USD | 40,840.00 USD | 0.00 USD | `+62.61%` | `19,588.00` |
| `Live` | `Short` | `2.10` | 16,660,000.00 USD | 331.01 USD | 0.00 USD | `+63.39%` | `158.00` |
| `Live` | `Short` | `2.10` | 16,660,000.00 USD | 294.70 USD | 0.00 USD | `+64.17%` | `140.00` |
| `Live` | `Short` | `2.12` | 16,660,000.00 USD | 3,100.00 USD | 0.00 USD | `+64.95%` | `1,468.00` |
| `Live` | `Short` | `2.12` | 19,910,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+65.73%` | `1,529,461.00` |
| `Live` | `Short` | `2.13` | 20,090,000.00 USD | 173,550.00 USD | 0.00 USD | `+66.51%` | `81,287.00` |
| `Live` | `Short` | `2.15` | 20,090,000.00 USD | 515.05 USD | 0.00 USD | `+68.07%` | `239.00` |
| `Live` | `Short` | `2.17` | 20,090,000.00 USD | 2,730.00 USD | 0.00 USD | `+69.63%` | `1,253.00` |
| `Live` | `Short` | `2.19` | 20,090,000.00 USD | 703.57 USD | 0.00 USD | `+70.41%` | `322.00` |
| `Live` | `Short` | `2.19` | 20,090,000.00 USD | 2,820.00 USD | 0.00 USD | `+71.19%` | `1,286.00` |
| `Live` | `Short` | `2.21` | 20,100,000.00 USD | 8,920.00 USD | 0.00 USD | `+71.97%` | `4,046.00` |
| `Live` | `Short` | `2.23` | 22,420,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+73.53%` | `1,041,436.00` |
| `Live` | `Short` | `2.23` | 22,420,000.00 USD | 1,350.00 USD | 0.00 USD | `+74.31%` | `604.00` |
| `Live` | `Short` | `2.25` | 22,430,000.00 USD | 4,010.00 USD | 0.00 USD | `+75.09%` | `1,784.00` |
| `Live` | `Short` | `2.25` | 22,440,000.00 USD | 12,490.00 USD | 0.00 USD | `+75.87%` | `5,539.00` |
| `Live` | `Short` | `2.27` | 22,490,000.00 USD | 51,650.00 USD | 0.00 USD | `+76.65%` | `22,804.00` |
| `Live` | `Short` | `2.27` | 22,510,000.00 USD | 14,930.00 USD | 0.00 USD | `+77.43%` | `6,561.00` |
| `Live` | `Short` | `2.29` | 22,570,000.00 USD | 67,070.00 USD | 0.00 USD | `+78.99%` | `29,225.00` |
| `Live` | `Short` | `2.31` | 22,580,000.00 USD | 5,770.00 USD | 0.00 USD | `+79.77%` | `2,502.00` |
| `Live` | `Short` | `2.31` | 22,660,000.00 USD | 77,580.00 USD | 0.00 USD | `+80.55%` | `33,513.00` |
| `Live` | `Short` | `2.33` | 22,660,000.00 USD | 2,670.00 USD | 0.00 USD | `+81.33%` | `1,147.00` |
| `Live` | `Short` | `2.33` | 22,750,000.00 USD | 90,600.00 USD | 0.00 USD | `+82.11%` | `38,799.00` |
| `Live` | `Short` | `2.35` | 22,760,000.00 USD | 11,870.00 USD | 0.00 USD | `+82.89%` | `5,062.00` |
| `Live` | `Short` | `2.38` | 23,710,000.00 USD | 950,110.00 USD | 0.00 USD | `+85.23%` | `400,046.00` |
| `Live` | `Short` | `2.38` | 23,710,000.00 USD | 257.58 USD | 0.00 USD | `+86.01%` | `108.00` |
| `Live` | `Short` | `2.40` | 23,890,000.00 USD | 181,260.00 USD | 0.00 USD | `+87.57%` | `75,369.00` |
| `Live` | `Short` | `2.42` | 23,990,000.00 USD | 92,830.00 USD | 0.00 USD | `+88.35%` | `38,440.00` |
| `Live` | `Short` | `2.42` | 23,990,000.00 USD | 2,590.00 USD | 0.00 USD | `+89.13%` | `1,070.00` |
| `Live` | `Short` | `2.44` | 23,990,000.00 USD | 1,120.00 USD | 0.00 USD | `+89.91%` | `459.00` |
| `Live` | `Short` | `2.44` | 24,010,000.00 USD | 24,720.00 USD | 0.00 USD | `+90.69%` | `10,111.00` |
| `Live` | `Short` | `2.46` | 24,010,000.00 USD | 311.79 USD | 0.00 USD | `+91.47%` | `127.00` |
| `Live` | `Short` | `2.46` | 24,020,000.00 USD | 4,190.00 USD | 0.00 USD | `+92.25%` | `1,698.00` |
| `Live` | `Short` | `2.48` | 24,030,000.00 USD | 14,040.00 USD | 0.00 USD | `+93.81%` | `5,648.00` |
| `Live` | `Short` | `2.50` | 24,040,000.00 USD | 4,730.00 USD | 0.00 USD | `+95.37%` | `1,888.00` |
| `Live` | `Short` | `2.52` | 24,040,000.00 USD | 5,970.00 USD | 0.00 USD | `+96.15%` | `2,374.00` |
| `Live` | `Short` | `2.52` | 24,090,000.00 USD | 42,710.00 USD | 0.00 USD | `+96.93%` | `16,914.00` |
| `Live` | `Short` | `2.54` | 24,090,000.00 USD | 496.86 USD | 0.00 USD | `+97.71%` | `196.00` |
| `Live` | `Short` | `2.54` | 24,090,000.00 USD | 117.07 USD | 0.00 USD | `+98.49%` | `46.00` |
| `Live` | `Short` | `2.56` | 24,100,000.00 USD | 11,280.00 USD | 0.00 USD | `+99.27%` | `4,414.00` |
| `Live` | `Short` | `2.56` | 24,100,000.00 USD | 187.25 USD | 0.00 USD | `+100.05%` | `73.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,270,000.00 USD | 0.00 USD | 112.45 USD | `-80.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3050` | 3,270,000.00 USD | 0.00 USD | 147.62 USD | `-76.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,270,000.00 USD | 0.00 USD | 139.12 USD | `-70.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 3,270,000.00 USD | 0.00 USD | 200.86 USD | `-67.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,270,000.00 USD | 0.00 USD | 408.51 USD | `-65.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,270,000.00 USD | 0.00 USD | 520.52 USD | `-64.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,270,000.00 USD | 0.00 USD | 151.12 USD | `-63.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,270,000.00 USD | 0.00 USD | 190.00 USD | `-62.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,270,000.00 USD | 0.00 USD | 145.50 USD | `-62.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,270,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,270,000.00 USD | 0.00 USD | 306.60 USD | `-59.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,270,000.00 USD | 0.00 USD | 6,750.00 USD | `-56.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,260,000.00 USD | 0.00 USD | 374.60 USD | `-55.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,260,000.00 USD | 0.00 USD | 100.62 USD | `-54.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,260,000.00 USD | 0.00 USD | 791.85 USD | `-50.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,260,000.00 USD | 0.00 USD | 573.40 USD | `-49.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,260,000.00 USD | 0.00 USD | 3,450.00 USD | `-48.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,260,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,260,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,260,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,250,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,250,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,250,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 3,250,000.00 USD | 0.00 USD | 798.57 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 3,250,000.00 USD | 0.00 USD | 690.38 USD | `-31.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 3,250,000.00 USD | 0.00 USD | 1,420.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 3,250,000.00 USD | 0.00 USD | 3,230.00 USD | `-30.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 3,240,000.00 USD | 0.00 USD | 838.94 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 3,240,000.00 USD | 0.00 USD | 188.49 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 3,240,000.00 USD | 0.00 USD | 2,730.00 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 3,240,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 3,240,000.00 USD | 0.00 USD | 112.46 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 3,240,000.00 USD | 0.00 USD | 2,360.00 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 3,230,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 3,230,000.00 USD | 0.00 USD | 546,370.00 USD | `-23.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,680,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,680,000.00 USD | 0.00 USD | 897.49 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,680,000.00 USD | 0.00 USD | 15,070.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,660,000.00 USD | 0.00 USD | 4,330.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,660,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,660,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,620,000.00 USD | 0.00 USD | 2,280.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,620,000.00 USD | 0.00 USD | 7,090.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 2,610,000.00 USD | 0.00 USD | 3,230.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 2,610,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 2,570,000.00 USD | 0.00 USD | 973.25 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 2,570,000.00 USD | 0.00 USD | 8,000.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 2,560,000.00 USD | 0.00 USD | 2,970.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 2,560,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 2,550,000.00 USD | 0.00 USD | 79,110.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 2,470,000.00 USD | 0.00 USD | 12,910.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 2,460,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 2,440,000.00 USD | 0.00 USD | 31,630.00 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 2,410,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 2,400,000.00 USD | 0.00 USD | 4,790.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 2,390,000.00 USD | 0.00 USD | 90,010.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,300,000.00 USD | 0.00 USD | 12,570.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 2,290,000.00 USD | 0.00 USD | 52,130.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 2,240,000.00 USD | 0.00 USD | 57,160.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 2,180,000.00 USD | 0.00 USD | 146,570.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 2,030,000.00 USD | 0.00 USD | 381,390.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,650,000.00 USD | 0.00 USD | 338,320.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,310,000.00 USD | 0.00 USD | 684,480.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 628,350.00 USD | 0.00 USD | 137,880.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 490,470.00 USD | 0.00 USD | 490,470.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 167,680.00 USD | 165,400.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 261,700.00 USD | 94,020.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 473,630.00 USD | 211,930.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 718,280.00 USD | 244,650.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 815,950.00 USD | 97,670.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 992,180.00 USD | 176,230.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,020,000.00 USD | 27,390.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,300,000.00 USD | 281,080.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,370,000.00 USD | 73,500.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,450,000.00 USD | 73,380.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,520,000.00 USD | 71,640.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,860,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,890,000.00 USD | 30,880.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,910,000.00 USD | 19,640.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,000,000.00 USD | 82,400.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,190,000.00 USD | 193,480.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,230,000.00 USD | 43,500.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,260,000.00 USD | 27,080.00 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,370,000.00 USD | 108,480.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,450,000.00 USD | 78,610.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,460,000.00 USD | 14,970.00 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,580,000.00 USD | 115,020.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,600,000.00 USD | 18,210.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,700,000.00 USD | 103,290.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,760,000.00 USD | 57,450.00 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,790,000.00 USD | 37,230.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,800,000.00 USD | 6,110.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,810,000.00 USD | 6,300.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,810,000.00 USD | 6,080.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,820,000.00 USD | 9,700.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,960,000.00 USD | 141,350.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,970,000.00 USD | 2,730.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,050,000.00 USD | 81,600.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,050,000.00 USD | 464.75 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,250,000.00 USD | 199,230.00 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,250,000.00 USD | 3,370.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,280,000.00 USD | 33,550.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,290,000.00 USD | 6,720.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,310,000.00 USD | 18,770.00 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,380,000.00 USD | 70,850.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,390,000.00 USD | 8,570.00 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,650,000.00 USD | 259,410.00 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,660,000.00 USD | 14,030.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,680,000.00 USD | 14,560.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,720,000.00 USD | 44,100.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,730,000.00 USD | 4,710.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,730,000.00 USD | 6,330.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,750,000.00 USD | 21,720.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,880,000.00 USD | 122,650.00 USD | 0.00 USD | `+38.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,970,000.00 USD | 96,900.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,010,000.00 USD | 40,420.00 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,010,000.00 USD | 254.51 USD | 0.00 USD | `+40.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,020,000.00 USD | 2,530.00 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,020,000.00 USD | 1,830.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,030,000.00 USD | 7,630.00 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,030,000.00 USD | 1,900.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,040,000.00 USD | 8,390.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,040,000.00 USD | 4,550.00 USD | 0.00 USD | `+46.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,040,000.00 USD | 591.89 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,090,000.00 USD | 44,350.00 USD | 0.00 USD | `+47.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,130,000.00 USD | 39,680.00 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 8,130,000.00 USD | 7,410.00 USD | 0.00 USD | `+49.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,130,000.00 USD | 265.10 USD | 0.00 USD | `+50.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,140,000.00 USD | 2,040.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,140,000.00 USD | 1,510.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,150,000.00 USD | 14,120.00 USD | 0.00 USD | `+53.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,150,000.00 USD | 4,010.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,160,000.00 USD | 325.54 USD | 0.00 USD | `+54.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,160,000.00 USD | 7,020.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,300,000.00 USD | 138,900.00 USD | 0.00 USD | `+56.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,300,000.00 USD | 781.82 USD | 0.00 USD | `+57.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,300,000.00 USD | 222.75 USD | 0.00 USD | `+57.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,300,000.00 USD | 862.84 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,310,000.00 USD | 3,490.00 USD | 0.00 USD | `+59.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,310,000.00 USD | 3,940.00 USD | 0.00 USD | `+61.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,310,000.00 USD | 661.93 USD | 0.00 USD | `+61.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,440,000.00 USD | 124,400.00 USD | 0.00 USD | `+63.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,440,000.00 USD | 1,580.00 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,450,000.00 USD | 13,900.00 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,480,000.00 USD | 24,840.00 USD | 0.00 USD | `+67.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,530,000.00 USD | 50,580.00 USD | 0.00 USD | `+68.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,530,000.00 USD | 1,710.00 USD | 0.00 USD | `+68.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,530,000.00 USD | 1,970.00 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,680,000.00 USD | 151,380.00 USD | 0.00 USD | `+72.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,690,000.00 USD | 7,340.00 USD | 0.00 USD | `+74.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,690,000.00 USD | 3,120.00 USD | 0.00 USD | `+77.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,690,000.00 USD | 1,140.00 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,710,000.00 USD | 12,150.00 USD | 0.00 USD | `+78.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,710,000.00 USD | 370.40 USD | 0.00 USD | `+80.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,710,000.00 USD | 733.19 USD | 0.00 USD | `+82.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,710,000.00 USD | 2,410.00 USD | 0.00 USD | `+84.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,710,000.00 USD | 475.00 USD | 0.00 USD | `+85.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,710,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,960,000.00 USD | 251,200.00 USD | 0.00 USD | `+87.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+88.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,960,000.00 USD | 564.92 USD | 0.00 USD | `+89.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,970,000.00 USD | 8,110.00 USD | 0.00 USD | `+91.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,980,000.00 USD | 3,420.00 USD | 0.00 USD | `+93.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,980,000.00 USD | 124.75 USD | 0.00 USD | `+94.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 9,020,000.00 USD | 42,600.00 USD | 0.00 USD | `+95.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 9,020,000.00 USD | 378.75 USD | 0.00 USD | `+96.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 9,020,000.00 USD | 389.88 USD | 0.00 USD | `+100.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.13` | 134,840,000.00 USD | 0.00 USD | 134,840,000.00 USD | 144,660.00 USD | 944.65 USD | 225,720.00 USD |
| `7D` | `1.14` | 134,470,000.00 USD | 0.00 USD | 134,470,000.00 USD | 79,780.00 USD | 43,440.00 USD | 71,350.00 USD |
| `7D` | `1.14` | 134,270,000.00 USD | 0.00 USD | 134,270,000.00 USD | 0.00 USD | 0.00 USD | 13,580.00 USD |
| `1D` | `1.14` | 39,680,000.00 USD | 0.00 USD | 39,680,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 134,260,000.00 USD | 0.00 USD | 134,260,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 39,610,000.00 USD | 0.00 USD | 39,610,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 134,220,000.00 USD | 0.00 USD | 134,220,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 39,540,000.00 USD | 0.00 USD | 39,540,000.00 USD | 48,530.00 USD | 495.40 USD | 83,450.00 USD |
| `7D` | `1.14` | 134,080,000.00 USD | 0.00 USD | 134,080,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.15` | 134,070,000.00 USD | 0.00 USD | 134,070,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 39,410,000.00 USD | 0.00 USD | 39,410,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 134,010,000.00 USD | 0.00 USD | 134,010,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `7D` | `1.15` | 133,640,000.00 USD | 0.00 USD | 133,640,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 39,400,000.00 USD | 0.00 USD | 39,400,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 133,480,000.00 USD | 0.00 USD | 133,480,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 39,330,000.00 USD | 0.00 USD | 39,330,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 133,320,000.00 USD | 0.00 USD | 133,320,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 38,950,000.00 USD | 0.00 USD | 38,950,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 132,440,000.00 USD | 0.00 USD | 132,440,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 38,830,000.00 USD | 0.00 USD | 38,830,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 132,200,000.00 USD | 0.00 USD | 132,200,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 38,650,000.00 USD | 0.00 USD | 38,650,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 131,350,000.00 USD | 0.00 USD | 131,350,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 38,270,000.00 USD | 0.00 USD | 38,270,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 130,610,000.00 USD | 0.00 USD | 130,610,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.16` | 37,530,000.00 USD | 0.00 USD | 37,530,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.16` | 129,560,000.00 USD | 0.00 USD | 129,560,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.17` | 37,100,000.00 USD | 0.00 USD | 37,100,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 128,230,000.00 USD | 0.00 USD | 128,230,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD |
| `1D` | `1.17` | 36,770,000.00 USD | 0.00 USD | 36,770,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 127,260,000.00 USD | 0.00 USD | 127,260,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 36,590,000.00 USD | 0.00 USD | 36,590,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 126,200,000.00 USD | 0.00 USD | 126,200,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 36,430,000.00 USD | 0.00 USD | 36,430,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 124,170,000.00 USD | 0.00 USD | 124,170,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `1D` | `1.17` | 36,210,000.00 USD | 0.00 USD | 36,210,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.17` | 123,320,000.00 USD | 0.00 USD | 123,320,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `1D` | `1.18` | 35,940,000.00 USD | 0.00 USD | 35,940,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 122,430,000.00 USD | 0.00 USD | 122,430,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 35,710,000.00 USD | 0.00 USD | 35,710,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 121,770,000.00 USD | 0.00 USD | 121,770,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `1D` | `1.18` | 35,540,000.00 USD | 0.00 USD | 35,540,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 121,350,000.00 USD | 0.00 USD | 121,350,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `1D` | `1.18` | 35,460,000.00 USD | 0.00 USD | 35,460,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 120,740,000.00 USD | 0.00 USD | 120,740,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 35,380,000.00 USD | 0.00 USD | 35,380,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.18` | 120,500,000.00 USD | 0.00 USD | 120,500,000.00 USD | 116,030.00 USD | 65,900.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 35,260,000.00 USD | 0.00 USD | 35,260,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 120,080,000.00 USD | 0.00 USD | 120,080,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `1D` | `1.19` | 35,220,000.00 USD | 0.00 USD | 35,220,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 119,900,000.00 USD | 0.00 USD | 119,900,000.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD |
| `1D` | `1.19` | 35,170,000.00 USD | 0.00 USD | 35,170,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 118,990,000.00 USD | 0.00 USD | 118,990,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD |
| `1D` | `1.19` | 35,140,000.00 USD | 0.00 USD | 35,140,000.00 USD | 20,520.00 USD | 17,640.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 118,410,000.00 USD | 0.00 USD | 118,410,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD |
| `1D` | `1.19` | 35,050,000.00 USD | 0.00 USD | 35,050,000.00 USD | 111,560.00 USD | 42,920.00 USD | 83,580.00 USD |
| `7D` | `1.19` | 118,040,000.00 USD | 0.00 USD | 118,040,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD |
| `1D` | `1.20` | 34,810,000.00 USD | 0.00 USD | 34,810,000.00 USD | 40,880.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 117,280,000.00 USD | 0.00 USD | 117,280,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD |
| `1D` | `1.20` | 34,720,000.00 USD | 0.00 USD | 34,720,000.00 USD | 107,530.00 USD | 7,010.00 USD | 9,050.00 USD |
| `7D` | `1.20` | 116,570,000.00 USD | 0.00 USD | 116,570,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD |
| `1D` | `1.20` | 34,600,000.00 USD | 0.00 USD | 34,600,000.00 USD | 0.00 USD | 14,280.00 USD | 0.00 USD |
| `7D` | `1.20` | 116,510,000.00 USD | 0.00 USD | 116,510,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD |
| `7D` | `1.20` | 116,380,000.00 USD | 0.00 USD | 116,380,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD |
| `7D` | `1.20` | 116,080,000.00 USD | 0.00 USD | 116,080,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD |
| `7D` | `1.21` | 115,920,000.00 USD | 0.00 USD | 115,920,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD |
| `7D` | `1.21` | 115,900,000.00 USD | 0.00 USD | 115,900,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD |
| `7D` | `1.21` | 115,640,000.00 USD | 0.00 USD | 115,640,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD |
| `7D` | `1.21` | 114,670,000.00 USD | 0.00 USD | 114,670,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD |
| `1D` | `1.21` | 34,580,000.00 USD | 0.00 USD | 34,580,000.00 USD | 9,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.21` | 114,150,000.00 USD | 0.00 USD | 114,150,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD |
| `1D` | `1.22` | 34,570,000.00 USD | 0.00 USD | 34,570,000.00 USD | 77,860.00 USD | 0.00 USD | 78,080.00 USD |
| `7D` | `1.22` | 113,970,000.00 USD | 0.00 USD | 113,970,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.22` | 34,420,000.00 USD | 0.00 USD | 34,420,000.00 USD | 174,270.00 USD | 1,870.00 USD | 59,510.00 USD |
| `7D` | `1.22` | 113,870,000.00 USD | 0.00 USD | 113,870,000.00 USD | 316,090.00 USD | 3,350.00 USD | 27,810.00 USD |
| `1D` | `1.22` | 34,180,000.00 USD | 0.00 USD | 34,180,000.00 USD | 157,550.00 USD | 1,240.00 USD | 208,620.00 USD |
| `7D` | `1.22` | 113,530,000.00 USD | 0.00 USD | 113,530,000.00 USD | 104,420.00 USD | 2,640.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 33,810,000.00 USD | 0.00 USD | 33,810,000.00 USD | 0.00 USD | 211.25 USD | 0.00 USD |
| `7D` | `1.22` | 113,400,000.00 USD | 0.00 USD | 113,400,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD |
| `1D` | `1.22` | 33,810,000.00 USD | 0.00 USD | 33,810,000.00 USD | 40,080.00 USD | 206.80 USD | 0.00 USD |
| `7D` | `1.22` | 113,180,000.00 USD | 0.00 USD | 113,180,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD |
| `7D` | `1.23` | 112,510,000.00 USD | 0.00 USD | 112,510,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD |
| `1D` | `1.23` | 33,770,000.00 USD | 0.00 USD | 33,770,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 111,720,000.00 USD | 0.00 USD | 111,720,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD |
| `1D` | `1.23` | 33,720,000.00 USD | 0.00 USD | 33,720,000.00 USD | 203,290.00 USD | 28,070.00 USD | 518,460.00 USD |
| `7D` | `1.23` | 111,040,000.00 USD | 0.00 USD | 111,040,000.00 USD | 254,940.00 USD | 112,100.00 USD | 795,530.00 USD |
| `1D` | `1.23` | 32,970,000.00 USD | 0.00 USD | 32,970,000.00 USD | 295,580.00 USD | 131,700.00 USD | 492,180.00 USD |
| `7D` | `1.23` | 109,880,000.00 USD | 0.00 USD | 109,880,000.00 USD | 944,780.00 USD | 474,960.00 USD | 940,390.00 USD |
| `1D` | `1.23` | 32,060,000.00 USD | 0.00 USD | 32,060,000.00 USD | 97,740.00 USD | 1,800.00 USD | 73,470.00 USD |
| `7D` | `1.23` | 107,520,000.00 USD | 0.00 USD | 107,520,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD |
| `1D` | `1.24` | 31,880,000.00 USD | 0.00 USD | 31,880,000.00 USD | 517,670.00 USD | 120,320.00 USD | 554,790.00 USD |
| `7D` | `1.24` | 104,480,000.00 USD | 0.00 USD | 104,480,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD |
| `1D` | `1.24` | 30,690,000.00 USD | 0.00 USD | 30,690,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 99,990,000.00 USD | 0.00 USD | 99,990,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD |
| `1D` | `1.24` | 28,230,000.00 USD | 0.00 USD | 28,230,000.00 USD | 961,180.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 95,090,000.00 USD | 0.00 USD | 95,090,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD |
| `1D` | `1.24` | 26,030,000.00 USD | 0.00 USD | 26,030,000.00 USD | 503,460.00 USD | 188,510.00 USD | 497,840.00 USD |
| `7D` | `1.24` | 89,170,000.00 USD | 0.00 USD | 89,170,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD |
| `1D` | `1.24` | 24,840,000.00 USD | 0.00 USD | 24,840,000.00 USD | 721,110.00 USD | 126,130.00 USD | 635,620.00 USD |
| `7D` | `1.24` | 86,120,000.00 USD | 0.00 USD | 86,120,000.00 USD | 1,660,000.00 USD | 544,230.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 23,360,000.00 USD | 0.00 USD | 23,360,000.00 USD | 861,120.00 USD | 132,180.00 USD | 578,850.00 USD |
| `7D` | `1.25` | 82,250,000.00 USD | 0.00 USD | 82,250,000.00 USD | 2,730,000.00 USD | 695,090.00 USD | 3,060,000.00 USD |
| `1D` | `1.25` | 21,790,000.00 USD | 0.00 USD | 21,790,000.00 USD | 218,430.00 USD | 101,820.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 75,770,000.00 USD | 0.00 USD | 75,770,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.25` | 21,110,000.00 USD | 0.00 USD | 21,110,000.00 USD | 257,560.00 USD | 103,030.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 66,320,000.00 USD | 0.00 USD | 66,320,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD |
| `1D` | `1.25` | 20,300,000.00 USD | 0.00 USD | 20,300,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 59,910,000.00 USD | 0.00 USD | 59,910,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 520,500.00 USD | 43,020.00 USD | 944,650.00 USD |
| `7D` | `1.25` | 55,550,000.00 USD | 0.00 USD | 55,550,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD |
| `1D` | `1.26` | 17,920,000.00 USD | 0.00 USD | 17,920,000.00 USD | 1,470,000.00 USD | 258,360.00 USD | 1,760,000.00 USD |
| `7D` | `1.26` | 53,920,000.00 USD | 0.00 USD | 53,920,000.00 USD | 2,900,000.00 USD | 1,090,000.00 USD | 2,940,000.00 USD |
| `1D` | `1.26` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 1,080,000.00 USD | 212,550.00 USD | 1,570,000.00 USD |
| `7D` | `1.26` | 46,990,000.00 USD | 0.00 USD | 46,990,000.00 USD | 1,490,000.00 USD | 211,890.00 USD | 1,000,000.00 USD |
| `1D` | `1.26` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 412,030.00 USD | 72,400.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 44,290,000.00 USD | 0.00 USD | 44,290,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD |
| `1D` | `1.26` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 1,150,000.00 USD | 254,090.00 USD | 1,140,000.00 USD |
| `7D` | `1.26` | 40,810,000.00 USD | 0.00 USD | 40,810,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD |
| `1D` | `1.26` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 670,330.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 35,870,000.00 USD | 0.00 USD | 35,870,000.00 USD | 3,140,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD |
| `1D` | `1.27` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 1,030,000.00 USD | 874,390.00 USD |
| `7D` | `1.27` | 27,230,000.00 USD | 0.00 USD | 27,230,000.00 USD | 4,220,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD |
| `1D` | `1.27` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 483,650.00 USD | 0.00 USD |
| `7D` | `1.27` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,100,000.00 USD |
| `1D` | `1.27` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 776,250.00 USD | 0.00 USD |
| `7D` | `1.27` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 0.00 USD | 2,580,000.00 USD | 6,460,000.00 USD |
| `1D` | `1.27` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 961,090.00 USD | 316,540.00 USD | 368,510.00 USD |
| `7D` | `1.27` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 306,560.00 USD | 2,550,000.00 USD | 7,120,000.00 USD |
| `7D` | `1.27` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 306,560.00 USD | 2,550,000.00 USD | 7,120,000.00 USD |
| `1D` | `1.27` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.27` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 100,310.00 USD | 547,830.00 USD | 1,660,000.00 USD |
| `7D` | `1.27` | 35,430,000.00 USD | 35,430,000.00 USD | 0.00 USD | 2,220,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD |
| `1D` | `1.28` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 105,090.00 USD | 1,280,000.00 USD | 2,920,000.00 USD |
| `7D` | `1.28` | 47,910,000.00 USD | 47,910,000.00 USD | 0.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD |
| `1D` | `1.28` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 6,170,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 63,640,000.00 USD | 63,640,000.00 USD | 0.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.28` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 188,330.00 USD | 1,450,000.00 USD | 312,320.00 USD |
| `7D` | `1.28` | 65,140,000.00 USD | 65,140,000.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 547,110.00 USD | 0.00 USD | 210,010.00 USD |
| `7D` | `1.28` | 66,270,000.00 USD | 66,270,000.00 USD | 0.00 USD | 1,030,000.00 USD | 22,110.00 USD | 85,990.00 USD |
| `1D` | `1.28` | 24,320,000.00 USD | 24,320,000.00 USD | 0.00 USD | 578,780.00 USD | 161,530.00 USD | 834,480.00 USD |
| `7D` | `1.28` | 66,820,000.00 USD | 66,820,000.00 USD | 0.00 USD | 417,680.00 USD | 6,660.00 USD | 123,100.00 USD |
| `1D` | `1.29` | 24,790,000.00 USD | 24,790,000.00 USD | 0.00 USD | 143,950.00 USD | 327,360.00 USD | 0.00 USD |
| `7D` | `1.29` | 68,220,000.00 USD | 68,220,000.00 USD | 0.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD |
| `1D` | `1.29` | 25,280,000.00 USD | 25,280,000.00 USD | 0.00 USD | 382,250.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 68,660,000.00 USD | 68,660,000.00 USD | 0.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 25,300,000.00 USD | 25,300,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 69,130,000.00 USD | 69,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD |
| `1D` | `1.29` | 27,030,000.00 USD | 27,030,000.00 USD | 0.00 USD | 349,940.00 USD | 0.00 USD | 1,380,000.00 USD |
| `7D` | `1.29` | 70,820,000.00 USD | 70,820,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD |
| `1D` | `1.29` | 30,690,000.00 USD | 30,690,000.00 USD | 0.00 USD | 1,110,000.00 USD | 113,790.00 USD | 2,430,000.00 USD |
| `7D` | `1.29` | 74,240,000.00 USD | 74,240,000.00 USD | 0.00 USD | 1,740,000.00 USD | 6,700.00 USD | 1,680,000.00 USD |
| `1D` | `1.30` | 35,590,000.00 USD | 35,590,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD |
| `7D` | `1.30` | 81,170,000.00 USD | 81,170,000.00 USD | 0.00 USD | 1,940,000.00 USD | 1,570,000.00 USD | 3,420,000.00 USD |
| `1D` | `1.30` | 36,220,000.00 USD | 36,220,000.00 USD | 0.00 USD | 344,680.00 USD | 422.50 USD | 288,210.00 USD |
| `7D` | `1.30` | 82,410,000.00 USD | 82,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 83,380,000.00 USD | 83,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 39,080,000.00 USD | 39,080,000.00 USD | 0.00 USD | 602,010.00 USD | 910,970.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 84,240,000.00 USD | 84,240,000.00 USD | 0.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD |
| `1D` | `1.30` | 39,490,000.00 USD | 39,490,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `7D` | `1.30` | 86,190,000.00 USD | 86,190,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD |
| `1D` | `1.31` | 40,620,000.00 USD | 40,620,000.00 USD | 0.00 USD | 493,480.00 USD | 313,760.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 88,130,000.00 USD | 88,130,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 43,130,000.00 USD | 43,130,000.00 USD | 0.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD |
| `7D` | `1.31` | 92,360,000.00 USD | 92,360,000.00 USD | 0.00 USD | 1,240,000.00 USD | 590,530.00 USD | 2,390,000.00 USD |
| `1D` | `1.31` | 45,630,000.00 USD | 45,630,000.00 USD | 0.00 USD | 890,710.00 USD | 396,100.00 USD | 1,210,000.00 USD |
| `7D` | `1.31` | 94,120,000.00 USD | 94,120,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD |
| `1D` | `1.31` | 48,460,000.00 USD | 48,460,000.00 USD | 0.00 USD | 1,700,000.00 USD | 444,160.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 97,870,000.00 USD | 97,870,000.00 USD | 0.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 50,170,000.00 USD | 50,170,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 99,020,000.00 USD | 99,020,000.00 USD | 0.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD |
| `1D` | `1.32` | 56,150,000.00 USD | 56,150,000.00 USD | 0.00 USD | 222,150.00 USD | 1,830,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.32` | 103,210,000.00 USD | 103,210,000.00 USD | 0.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 63,180,000.00 USD | 63,180,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 108,050,000.00 USD | 108,050,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 66,530,000.00 USD | 66,530,000.00 USD | 0.00 USD | 1,680,000.00 USD | 689,260.00 USD | 980,940.00 USD |
| `7D` | `1.32` | 110,070,000.00 USD | 110,070,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 71,160,000.00 USD | 71,160,000.00 USD | 0.00 USD | 1,870,000.00 USD | 843,870.00 USD | 1,920,000.00 USD |
| `7D` | `1.32` | 113,270,000.00 USD | 113,270,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,140,000.00 USD |
| `1D` | `1.32` | 74,160,000.00 USD | 74,160,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 115,890,000.00 USD | 115,890,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD |
| `1D` | `1.33` | 76,450,000.00 USD | 76,450,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 117,700,000.00 USD | 117,700,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 78,640,000.00 USD | 78,640,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 118,750,000.00 USD | 118,750,000.00 USD | 0.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 81,080,000.00 USD | 81,080,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 120,370,000.00 USD | 120,370,000.00 USD | 0.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 83,340,000.00 USD | 83,340,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 122,790,000.00 USD | 122,790,000.00 USD | 0.00 USD | 829,540.00 USD | 236,880.00 USD | 1,360,000.00 USD |
| `1D` | `1.33` | 85,670,000.00 USD | 85,670,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 124,820,000.00 USD | 124,820,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 88,110,000.00 USD | 88,110,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 126,370,000.00 USD | 126,370,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 90,790,000.00 USD | 90,790,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 128,810,000.00 USD | 128,810,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 94,030,000.00 USD | 94,030,000.00 USD | 0.00 USD | 1,470,000.00 USD | 549,090.00 USD | 1,230,000.00 USD |
| `7D` | `1.34` | 130,670,000.00 USD | 130,670,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 97,750,000.00 USD | 97,750,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 136,590,000.00 USD | 136,590,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD |
| `1D` | `1.34` | 101,760,000.00 USD | 101,760,000.00 USD | 0.00 USD | 2,140,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 143,820,000.00 USD | 143,820,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 2,990,000.00 USD |
| `1D` | `1.35` | 103,070,000.00 USD | 103,070,000.00 USD | 0.00 USD | 498,430.00 USD | 331,800.00 USD | 481,220.00 USD |
| `7D` | `1.35` | 154,570,000.00 USD | 154,570,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,810,000.00 USD |
| `1D` | `1.35` | 104,330,000.00 USD | 104,330,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 163,400,000.00 USD | 163,400,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD |
| `1D` | `1.35` | 105,820,000.00 USD | 105,820,000.00 USD | 0.00 USD | 771,840.00 USD | 230,360.00 USD | 490,590.00 USD |
| `7D` | `1.35` | 172,610,000.00 USD | 172,610,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 107,160,000.00 USD | 107,160,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD |
| `7D` | `1.35` | 181,860,000.00 USD | 181,860,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 109,020,000.00 USD | 109,020,000.00 USD | 0.00 USD | 805,600.00 USD | 299,340.00 USD | 757,810.00 USD |
| `7D` | `1.35` | 189,400,000.00 USD | 189,400,000.00 USD | 0.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD |
| `1D` | `1.36` | 110,400,000.00 USD | 110,400,000.00 USD | 0.00 USD | 565,230.00 USD | 199,730.00 USD | 611,840.00 USD |
| `7D` | `1.36` | 196,560,000.00 USD | 196,560,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD |
| `1D` | `1.36` | 111,620,000.00 USD | 111,620,000.00 USD | 0.00 USD | 732,680.00 USD | 76,930.00 USD | 416,300.00 USD |
| `7D` | `1.36` | 199,090,000.00 USD | 199,090,000.00 USD | 0.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 112,120,000.00 USD | 112,120,000.00 USD | 0.00 USD | 266,880.00 USD | 118,570.00 USD | 116,960.00 USD |
| `7D` | `1.36` | 202,160,000.00 USD | 202,160,000.00 USD | 0.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 112,770,000.00 USD | 112,770,000.00 USD | 0.00 USD | 222,740.00 USD | 103,400.00 USD | 317,870.00 USD |
| `7D` | `1.36` | 205,940,000.00 USD | 205,940,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 112,910,000.00 USD | 112,910,000.00 USD | 0.00 USD | 80,160.00 USD | 26,460.00 USD | 31,150.00 USD |
| `7D` | `1.36` | 208,690,000.00 USD | 208,690,000.00 USD | 0.00 USD | 1,430,000.00 USD | 614,410.00 USD | 702,320.00 USD |
| `1D` | `1.37` | 113,080,000.00 USD | 113,080,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 209,430,000.00 USD | 209,430,000.00 USD | 0.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 113,270,000.00 USD | 113,270,000.00 USD | 0.00 USD | 84,710.00 USD | 57,700.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 210,540,000.00 USD | 210,540,000.00 USD | 0.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 113,450,000.00 USD | 113,450,000.00 USD | 0.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 212,130,000.00 USD | 212,130,000.00 USD | 0.00 USD | 477,130.00 USD | 362,580.00 USD | 755,690.00 USD |
| `1D` | `1.37` | 113,590,000.00 USD | 113,590,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 214,200,000.00 USD | 214,200,000.00 USD | 0.00 USD | 743,900.00 USD | 285,210.00 USD | 1,040,000.00 USD |
| `1D` | `1.37` | 113,730,000.00 USD | 113,730,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.37` | 216,320,000.00 USD | 216,320,000.00 USD | 0.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD |
| `1D` | `1.38` | 113,980,000.00 USD | 113,980,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 217,990,000.00 USD | 217,990,000.00 USD | 0.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD |
| `1D` | `1.38` | 114,490,000.00 USD | 114,490,000.00 USD | 0.00 USD | 231,710.00 USD | 71,960.00 USD | 200,640.00 USD |
| `7D` | `1.38` | 219,540,000.00 USD | 219,540,000.00 USD | 0.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD |
| `1D` | `1.38` | 115,050,000.00 USD | 115,050,000.00 USD | 0.00 USD | 314,100.00 USD | 98,360.00 USD | 149,980.00 USD |
| `7D` | `1.38` | 221,580,000.00 USD | 221,580,000.00 USD | 0.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD |
| `1D` | `1.38` | 115,300,000.00 USD | 115,300,000.00 USD | 0.00 USD | 106,800.00 USD | 53,840.00 USD | 92,660.00 USD |
| `7D` | `1.38` | 223,860,000.00 USD | 223,860,000.00 USD | 0.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD |
| `1D` | `1.38` | 115,670,000.00 USD | 115,670,000.00 USD | 0.00 USD | 300,730.00 USD | 17,520.00 USD | 52,070.00 USD |
| `7D` | `1.38` | 224,550,000.00 USD | 224,550,000.00 USD | 0.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 115,710,000.00 USD | 115,710,000.00 USD | 0.00 USD | 0.00 USD | 35,700.00 USD | 0.00 USD |
| `7D` | `1.39` | 225,470,000.00 USD | 225,470,000.00 USD | 0.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD |
| `7D` | `1.39` | 226,340,000.00 USD | 226,340,000.00 USD | 0.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD |
| `7D` | `1.39` | 227,070,000.00 USD | 227,070,000.00 USD | 0.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD |
| `1D` | `1.39` | 115,710,000.00 USD | 115,710,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 227,400,000.00 USD | 227,400,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 115,780,000.00 USD | 115,780,000.00 USD | 0.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.39` | 227,460,000.00 USD | 227,460,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 115,850,000.00 USD | 115,850,000.00 USD | 0.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.40` | 227,680,000.00 USD | 227,680,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.40` | 115,980,000.00 USD | 115,980,000.00 USD | 0.00 USD | 48,530.00 USD | 495.40 USD | 83,450.00 USD |
| `7D` | `1.40` | 227,690,000.00 USD | 227,690,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 227,750,000.00 USD | 227,750,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 227,830,000.00 USD | 227,830,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `1D` | `1.40` | 116,000,000.00 USD | 116,000,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.40` | 228,120,000.00 USD | 228,120,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 228,280,000.00 USD | 228,280,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.41` | 116,060,000.00 USD | 116,060,000.00 USD | 0.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.41` | 228,440,000.00 USD | 228,440,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.41` | 116,440,000.00 USD | 116,440,000.00 USD | 0.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.41` | 229,320,000.00 USD | 229,320,000.00 USD | 0.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.41` | 116,570,000.00 USD | 116,570,000.00 USD | 0.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 229,560,000.00 USD | 229,560,000.00 USD | 0.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.41` | 116,570,000.00 USD | 116,570,000.00 USD | 0.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD |
| `7D` | `1.41` | 229,850,000.00 USD | 229,850,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `1D` | `1.42` | 116,740,000.00 USD | 116,740,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 230,410,000.00 USD | 230,410,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `1D` | `1.42` | 117,120,000.00 USD | 117,120,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 231,150,000.00 USD | 231,150,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.42` | 117,860,000.00 USD | 117,860,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 232,200,000.00 USD | 232,200,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.42` | 118,290,000.00 USD | 118,290,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 233,540,000.00 USD | 233,540,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.42` | 118,370,000.00 USD | 118,370,000.00 USD | 0.00 USD | 9,670.00 USD | 54,510.00 USD | 21,210.00 USD |
| `7D` | `1.42` | 233,730,000.00 USD | 233,730,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `1D` | `1.43` | 118,580,000.00 USD | 118,580,000.00 USD | 0.00 USD | 99,870.00 USD | 35,450.00 USD | 73,570.00 USD |
| `7D` | `1.43` | 234,500,000.00 USD | 234,500,000.00 USD | 0.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD |
| `7D` | `1.43` | 235,570,000.00 USD | 235,570,000.00 USD | 0.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `7D` | `1.43` | 237,590,000.00 USD | 237,590,000.00 USD | 0.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `7D` | `1.43` | 238,440,000.00 USD | 238,440,000.00 USD | 0.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `7D` | `1.43` | 239,330,000.00 USD | 239,330,000.00 USD | 0.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `7D` | `1.44` | 239,360,000.00 USD | 239,360,000.00 USD | 0.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD |
| `7D` | `1.44` | 239,990,000.00 USD | 239,990,000.00 USD | 0.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD |
| `7D` | `1.44` | 240,410,000.00 USD | 240,410,000.00 USD | 0.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `7D` | `1.44` | 241,020,000.00 USD | 241,020,000.00 USD | 0.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `7D` | `1.44` | 241,260,000.00 USD | 241,260,000.00 USD | 0.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `7D` | `1.45` | 241,360,000.00 USD | 241,360,000.00 USD | 0.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 241,680,000.00 USD | 241,680,000.00 USD | 0.00 USD | 65,610.00 USD | 26,800.00 USD | 226,740.00 USD |
| `7D` | `1.45` | 241,860,000.00 USD | 241,860,000.00 USD | 0.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `7D` | `1.45` | 242,780,000.00 USD | 242,780,000.00 USD | 0.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD |
| `7D` | `1.45` | 243,330,000.00 USD | 243,330,000.00 USD | 0.00 USD | 193,090.00 USD | 81,140.00 USD | 278,630.00 USD |
| `7D` | `1.46` | 243,530,000.00 USD | 243,530,000.00 USD | 0.00 USD | 58,970.00 USD | 42,150.00 USD | 100,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.97B` | Total OI Tokens: `2,337,149,555.3 XRP`
  * 1h OI Change: `-0.86%` | 4h OI Change: `-2.25%` | 24h OI Change: `-0.31%`
  * Exchange Breakdown: Binance=`490.59M` | Bybit=`328.01M` | OKX=`97.79M` | Hyperliquid=`228.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `40.76K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0059%` | **USDT OKX** | `0.0096%` |
| **USDT Bybit** | `0.0019%` | **USDT KuCoin** | `0.0085%` |
| **USDT MEXC** | `0.0059%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0031%` | **USDT Bitget** | `0.0033%` |
| **CoinM Binance** | `0.0092%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `43.75%` | `56.25%` | `0.78` | 1,990,000,000.00 USD |
| `15M` | `Binance` | `41.27%` | `58.73%` | `0.70` | 661,590,000.00 USD |
| `15M` | `OKX` | `40.37%` | `59.63%` | `0.68` | 357,340,000.00 USD |
| `15M` | `Bybit` | `37.04%` | `62.96%` | `0.59` | 135,600,000.00 USD |
| `15M` | `KuCoin` | `49.01%` | `50.99%` | `0.96` | 4,960,000.00 USD |
| `15M` | `Gate` | `47.53%` | `52.47%` | `0.91` | 328,170,000.00 USD |
| `15M` | `Bitget` | `43.67%` | `56.33%` | `0.78` | 98,410,000.00 USD |
| `15M` | `BingX` | `48.25%` | `51.75%` | `0.93` | 41,290,000.00 USD |
| `15M` | `MEXC` | `50.62%` | `49.38%` | `1.03` | 70,480,000.00 USD |
| `15M` | `Bitunix` | `47.59%` | `52.41%` | `0.91` | 77,290,000.00 USD |
| `15M` | `Hyperliquid` | `28.18%` | `71.82%` | `0.39` | 48,750,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.82%` | `48.18%` | `1.08` | 5,110,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `80.2%` | `19.8%` | `4.05` | 66,820,000.00 USD |
| `15M` | `HTX` | `20.89%` | `79.11%` | `0.26` | 28,870,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `43.78%` | `56.22%` | `0.78` | 7,790,000.00 USD |
| `15M` | `Bitfinex` | `32.44%` | `67.56%` | `0.48` | 979,570.00 USD |
| `15M` | `Kraken` | `68.76%` | `31.24%` | `2.20` | 4,220,000.00 USD |
| `15M` | `Aster` | `42.26%` | `57.74%` | `0.73` | 18,960,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.12%` | `44.88%` | `1.23` | 35,070,000.00 USD |
| `15M` | `Whale Positions` | `41.27%` | `58.73%` | `0.70` | 661,590,000.00 USD |
| `15M` | `Global Accounts` | `43.75%` | `56.25%` | `0.78` | 1,990,000,000.00 USD |
| `1H` | `XRP` | `40.26%` | `59.74%` | `0.67` | 201,460,000.00 USD |
| `1H` | `Binance` | `40.56%` | `59.44%` | `0.68` | 68,270,000.00 USD |
| `1H` | `OKX` | `33.58%` | `66.42%` | `0.51` | 25,610,000.00 USD |
| `1H` | `Bybit` | `37.12%` | `62.88%` | `0.59` | 26,250,000.00 USD |
| `1H` | `KuCoin` | `44.99%` | `55.01%` | `0.82` | 2,580,000.00 USD |
| `1H` | `Gate` | `40.81%` | `59.19%` | `0.69` | 8,150,000.00 USD |
| `1H` | `Bitget` | `35.56%` | `64.44%` | `0.55` | 14,000,000.00 USD |
| `1H` | `BingX` | `20.76%` | `79.24%` | `0.26` | 5,430,000.00 USD |
| `1H` | `MEXC` | `40.55%` | `59.45%` | `0.68` | 22,960,000.00 USD |
| `1H` | `Bitunix` | `39.51%` | `60.49%` | `0.65` | 11,110,000.00 USD |
| `1H` | `Hyperliquid` | `35.62%` | `64.38%` | `0.55` | 5,260,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.13%` | `47.87%` | `1.09` | 713,600.00 USD |
| `1H` | `Crypto.com` | `50.7%` | `49.3%` | `1.03` | 311,630.00 USD |
| `1H` | `WhiteBIT` | `98.85%` | `1.15%` | `85.96` | 6,920,000.00 USD |
| `1H` | `HTX` | `38.11%` | `61.89%` | `0.62` | 146,530.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.73%` | `80.27%` | `0.25` | 1,090,000.00 USD |
| `1H` | `Aster` | `48.04%` | `51.96%` | `0.92` | 2,390,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.82%` | `53.18%` | `0.88` | 270,010.00 USD |
| `1H` | `Whale Positions` | `40.56%` | `59.44%` | `0.68` | 68,270,000.00 USD |
| `1H` | `Global Accounts` | `40.26%` | `59.74%` | `0.67` | 201,460,000.00 USD |
| `4H` | `XRP` | `46.21%` | `53.79%` | `0.86` | 8,160,000,000.00 USD |
| `4H` | `Binance` | `43%` | `57%` | `0.75` | 2,490,000,000.00 USD |
| `4H` | `OKX` | `44.13%` | `55.87%` | `0.79` | 1,510,000,000.00 USD |
| `4H` | `Bybit` | `43.5%` | `56.5%` | `0.77` | 594,470,000.00 USD |
| `4H` | `KuCoin` | `45.5%` | `54.5%` | `0.83` | 18,460,000.00 USD |
| `4H` | `Gate` | `49.15%` | `50.85%` | `0.97` | 1,300,000,000.00 USD |
| `4H` | `Bitget` | `49.71%` | `50.29%` | `0.99` | 446,100,000.00 USD |
| `4H` | `BingX` | `49.28%` | `50.72%` | `0.97` | 126,550,000.00 USD |
| `4H` | `MEXC` | `51.23%` | `48.77%` | `1.05` | 353,580,000.00 USD |
| `4H` | `Bitunix` | `48.78%` | `51.22%` | `0.95` | 300,560,000.00 USD |
| `4H` | `Hyperliquid` | `46.93%` | `53.07%` | `0.88` | 196,340,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `46.46%` | `53.54%` | `0.87` | 24,260,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.33%` | `36.67%` | `1.73` | 359,630,000.00 USD |
| `4H` | `HTX` | `26.8%` | `73.2%` | `0.37` | 126,570,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.3%` | `50.7%` | `0.97` | 55,040,000.00 USD |
| `4H` | `Bitfinex` | `31.25%` | `68.75%` | `0.45` | 1,980,000.00 USD |
| `4H` | `Kraken` | `48.09%` | `51.91%` | `0.93` | 26,520,000.00 USD |
| `4H` | `Aster` | `41.17%` | `58.83%` | `0.70` | 81,240,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.31%` | `48.69%` | `1.05` | 156,280,000.00 USD |
| `4H` | `Whale Positions` | `43%` | `57%` | `0.75` | 2,490,000,000.00 USD |
| `4H` | `Global Accounts` | `46.21%` | `53.79%` | `0.86` | 8,160,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,908,299.96 USD | 2,545,215.27 USD | 2,363,084.69 USD | 182,130.57 USD | `+3.71%` | `7B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 30,348,241.89 USD | 10,177,546.51 USD | 20,170,695.38 USD | -9,993,148.87 USD | `-32.93%` | `4B / 38S` |
| `5:00 UTC` | `1.29` | `1.28` | `1.29` | `1.29` | `1.28` | 10,140,362.32 USD | 5,667,315.95 USD | 4,473,046.37 USD | 1,194,269.58 USD | `+11.78%` | `17B / 12S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,885,752.93 USD | 2,814,674.62 USD | 3,071,078.30 USD | -256,403.68 USD | `-4.36%` | `5B / 13S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,036,330.68 USD | 2,484,228.37 USD | 2,552,102.32 USD | -67,873.95 USD | `-1.35%` | `8B / 7S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.28` | 3,779,916.77 USD | 1,963,240.26 USD | 1,816,676.51 USD | 146,563.75 USD | `+3.88%` | `6B / 5S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 7,767,016.10 USD | 3,262,612.53 USD | 4,504,403.57 USD | -1,241,791.04 USD | `-15.99%` | `7B / 12S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.28` | `1.26` | 41,778,066.41 USD | 16,233,527.16 USD | 25,544,539.25 USD | -9,311,012.09 USD | `-22.29%` | `4B / 58S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 4,267,305.75 USD | 2,004,015.34 USD | 2,263,290.41 USD | -259,275.08 USD | `-6.08%` | `7B / 10S` |

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
| `5m` | 199,030.00 USD | 1,610,000.00 USD | **`ACCUMULATION`** |
| `15m` | -6,190,000.00 USD | -28,320,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -5,950,000.00 USD | -28,150,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -5,510,000.00 USD | -27,740,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -11,370,000.00 USD | -43,430,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -17,230,000.00 USD | -59,070,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -9,760,000.00 USD | -53,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,000,000.00 USD | -56,430,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,170,000.00 USD | -54,160,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -36,410,000.00 USD | -114,860,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -83,630,000.00 USD | -110,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -562,100,000.00 USD | -1,220,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+199.03K` | 15m=`-6.19M` | 1h=`-5.51M` | 24h=`-36.41M`
* Futures Capital Netflows: 5m=`+1.61M` | 15m=`-28.32M` | 1h=`-27.74M` | 24h=`-114.86M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.28` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0122` pts)
  * +2.5R Take Profit: `1.31`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0122` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.28`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
