# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:41:23 IST` (`2026-10-29 19:11:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.28` | **Live Ask Quote**: `1.28` | **Mid Price**: `1.28`
- **Spread Points**: `3.00` | **Spread BPS**: `23.41 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-1.22` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0068` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.21` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.31` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.29` | EMA-20=`1.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.29` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.1000`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-1.34%`)
  * Point of Control (POC) = `1.29` (Distance: `-0.57%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-0.20%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.32`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.30` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.31` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.28`
  * London Session (08:00-16:00 UTC): High=`1.30` | Low=`1.28`
  * New York Session (13:00-21:00 UTC): High=`1.31` | Low=`1.28`
  * Initial Balance (First Hour): IB High=`1.30` | IB Low=`1.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.28` - `1.29`
  * Optimal Trade Entry (OTE 0.705): `1.28`
  * Structural Invalidation Anchor (0.786): `1.29`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.28` | `1.29` | `1.28` | `1.29` | `3,269,548` | 4,203,740.56 USD | 1,283,492.94 USD | `+30.53%` | -35,586,913.28 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.29` | `1.29` | `1.29` | `1.29` | `1,978,678` | 2,547,100.83 USD | 239,687.54 USD | `+9.41%` | -35,347,225.73 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.29` | `1.29` | `1.28` | `1.28` | `2,052,115` | 2,634,239.28 USD | -143,623.64 USD | `-5.45%` | -35,490,849.38 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.28` | `1.28` | `23,675,158` | 30,348,241.89 USD | -9,993,148.87 USD | `-32.93%` | -36,111,342.66 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.29` | `7,892,687` | 10,140,362.32 USD | 1,194,269.58 USD | `+11.78%` | -34,917,073.08 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.28` | `1.28` | `2,059,918` | 2,644,246.50 USD | -153,431.30 USD | `-5.80%` | -35,070,504.38 USD | `+0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.29` | `27,238,695` | 35,241,786.93 USD | -1,210,810.88 USD | `-3.44%` | -29,377,946.50 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `38,773,350` | 49,794,344.17 USD | -9,116,518.67 USD | `-18.31%` | -38,494,465.17 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `2,059,868` | 2,644,182.38 USD | -153,367.18 USD | `-5.80%` | -38,647,832.34 USD | `+0.47` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `98,598,228` | 127,534,898.07 USD | -14,135,913.67 USD | `-11.08%` | -38,638,088.81 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `98,598,228` | 127,534,898.07 USD | -14,135,913.67 USD | `-11.08%` | -38,638,088.81 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.28`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.28` | `44935.0000` | 57,736.98 USD | 3,215,734.34 USD | `8 orders` | `+0.15%` | `-` |
| `ASK` | `1.28` | `60542.0000` | 77,784.36 USD | 3,157,997.36 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `1.28` | `218288.0000` | 280,434.59 USD | 3,080,213.00 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `1.28` | `343611.0000` | 441,402.69 USD | 2,799,778.40 USD | `11 orders` | `+0.13%` | `-` |
| `ASK` | `1.28` | `120086.0000` | 154,250.47 USD | 2,358,375.71 USD | `7 orders` | `+0.12%` | `-` |
| `ASK` | `1.28` | `330542.0000` | 424,548.14 USD | 2,204,125.25 USD | `10 orders` | `+0.11%` | `-` |
| `ASK` | `1.28` | `103236.0000` | 132,585.99 USD | 1,779,577.10 USD | `15 orders` | `+0.11%` | `-` |
| `ASK` | `1.28` | `266648.0000` | 342,429.36 USD | 1,646,991.11 USD | `14 orders` | `+0.10%` | `-` |
| `ASK` | `1.28` | `85230.0000` | 109,443.84 USD | 1,304,561.74 USD | `9 orders` | `+0.09%` | `-` |
| `ASK` | `1.28` | `54803.0000` | 70,367.05 USD | 1,195,117.90 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `1.28` | `116945.0000` | 150,145.69 USD | 1,124,750.85 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `61795.0000` | 79,332.42 USD | 974,605.16 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `322669.0000` | 414,210.20 USD | 895,272.74 USD | `16 orders` | `+0.06%` | `-` |
| `ASK` | `1.28` | `85587.0000` | 109,859.47 USD | 481,062.55 USD | `14 orders` | `+0.05%` | `-` |
| `ASK` | `1.28` | `46929.0000` | 60,233.37 USD | 371,203.07 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `76506.0000` | 98,187.80 USD | 310,969.70 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `70204.0000` | 90,092.79 USD | 212,781.90 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `1.28` | `36913.0000` | 47,366.76 USD | 122,689.11 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `1.28` | `38326.0000` | 49,176.09 USD | 75,322.35 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `1.28` | `20379.0000` | 26,146.26 USD | 26,146.26 USD | `9 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.28` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.28` | `0.00%` | `-` |
| `BID` | `1.28` | `448.0000` | 574.74 USD | 574.74 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `1.28` | `6903.0000` | 8,855.17 USD | 9,429.91 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `1.28` | `36303.0000` | 46,565.86 USD | 55,995.77 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `1.28` | `24009.0000` | 30,793.94 USD | 86,789.71 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `1.28` | `75362.0000` | 96,651.76 USD | 183,441.47 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `27373.0000` | 35,103.14 USD | 218,544.61 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `101664.0000` | 130,363.75 USD | 348,908.36 USD | `18 orders` | `-0.05%` | `-` |
| `BID` | `1.28` | `85817.0000` | 110,034.56 USD | 458,942.91 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `1.28` | `102856.0000` | 131,871.68 USD | 590,814.59 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `45501.0000` | 58,332.28 USD | 649,146.87 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `132363.0000` | 169,676.13 USD | 818,823.00 USD | `17 orders` | `-0.08%` | `-` |
| `BID` | `1.28` | `137042.0000` | 175,660.44 USD | 994,483.44 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `1.28` | `62236.0000` | 79,767.88 USD | 1,074,251.32 USD | `14 orders` | `-0.10%` | `-` |
| `BID` | `1.28` | `71362.0000` | 91,457.54 USD | 1,165,708.86 USD | `14 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `89615.0000` | 114,841.62 USD | 1,280,550.48 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `296473.0000` | 379,900.50 USD | 1,660,450.98 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.28` | `705349.0000` | 903,763.67 USD | 2,564,214.66 USD | `11 orders` | `-0.13%` | `-` |
| `BID` | `1.28` | `95999.0000` | 122,993.92 USD | 2,687,208.58 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `81507.0000` | 104,418.62 USD | 2,791,627.19 USD | `9 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `124655.0000` | 159,683.05 USD | 2,951,310.25 USD | `10 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,962,840.41 USD | `35,031,430.00` | `1.13` | `1.28` | `0.9612` | 5,383,957.14 USD | `+11.97%` | `10X Cross` |
| `88` | `0x5b5d...c060` | `SHORT` | 20,430,419.40 USD | `15,916,500.00` | `1.44` | `1.28` | `11.18` | 2,424,342.06 USD | `+11.87%` | `5X Cross` |
| `149` | `0x58f0...0d20` | `LONG` | 14,032,319.98 USD | `10,931,629.00` | `1.36` | `1.28` | `1.26` | -832,832.98 USD | `-5.94%` | `20X Cross` |
| `155` | `0xb83d...6e36` | `SHORT` | 13,550,031.16 USD | `10,555,450.00` | `1.50` | `1.28` | `13.82` | 2,272,538.48 USD | `+16.77%` | `5X Cross` |
| `435` | `0xca49...53c8` | `SHORT` | 5,311,018.52 USD | `4,138,886.00` | `1.44` | `1.28` | `4.41` | 642,304.22 USD | `+12.09%` | `20X Cross` |
| `455` | `0xfc27...9d9d` | `SHORT` | 5,084,106.89 USD | `3,962,671.00` | `1.31` | `1.28` | `4.92` | 125,017.87 USD | `+2.46%` | `20X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,549,129.58 USD | `3,543,946.00` | `1.44` | `1.28` | `0.7123` | -550,863.03 USD | `-12.11%` | `5X Cross` |
| `536` | `0xc30c...a4c9` | `SHORT` | 4,239,526.04 USD | `3,302,753.00` | `1.42` | `1.28` | `1.59` | 460,360.80 USD | `+10.86%` | `8X Cross` |
| `548` | `0xdd53...2b13` | `SHORT` | 4,170,363.11 USD | `3,249,718.00` | `1.44` | `1.28` | `18.80` | 503,768.14 USD | `+12.08%` | `3X Cross` |
| `600` | `0x9946...0852` | `SHORT` | 3,882,729.97 USD | `3,025,111.00` | `1.43` | `1.28` | `1.65` | 430,454.59 USD | `+11.09%` | `20X Cross` |
| `606` | `0xecb6...2b00` | `SHORT` | 3,869,209.81 USD | `3,014,239.00` | `1.31` | `1.28` | `10.35` | 68,591.66 USD | `+1.77%` | `10X Cross` |
| `693` | `0x9aa5...58af` | `SHORT` | 3,341,968.15 USD | `2,604,083.00` | `1.46` | `1.28` | `4.23` | 455,752.51 USD | `+13.64%` | `20X Cross` |
| `703` | `0xf48f...10fe` | `LONG` | 3,293,690.50 USD | `2,565,779.00` | `1.53` | `1.28` | `0.9232` | -630,950.22 USD | `-19.16%` | `4X Cross` |
| `724` | `0x023a...2355` | `SHORT` | 3,229,176.88 USD | `2,515,523.00` | `1.33` | `1.28` | `4.57` | 110,026.24 USD | `+3.41%` | `20X Cross` |
| `747` | `0x45d2...4029` | `SHORT` | 3,147,199.00 USD | `2,453,000.00` | `1.48` | `1.28` | `16.40` | 491,081.42 USD | `+15.60%` | `20X Cross` |
| `1019` | `0xc179...e0c8` | `SHORT` | 2,232,397.41 USD | `1,739,123.00` | `1.30` | `1.28` | `4.73` | 30,825.11 USD | `+1.38%` | `10X Cross` |
| `1078` | `0xfc66...ca06` | `SHORT` | 2,088,422.05 USD | `1,626,929.00` | `1.31` | `1.28` | `22.89` | 43,144.65 USD | `+2.07%` | `20X Cross` |
| `1087` | `0xeadc...9d55` | `LONG` | 2,079,181.70 USD | `1,619,805.00` | `1.21` | `1.28` | `0.000000` | 120,338.67 USD | `+5.79%` | `20X Cross` |
| `1160` | `0x94b2...599e` | `SHORT` | 1,977,483.32 USD | `1,540,696.00` | `1.36` | `1.28` | `1.83` | 122,983.13 USD | `+6.22%` | `20X Cross` |
| `1168` | `0xbcd4...0dd2` | `SHORT` | 1,963,369.09 USD | `1,529,461.00` | `1.31` | `1.28` | `2.17` | 41,175.51 USD | `+2.10%` | `20X Cross` |
| `1185` | `0x3fc5...c0c1` | `SHORT` | 1,940,608.72 USD | `1,511,779.00` | `1.52` | `1.28` | `2.66` | 351,005.88 USD | `+18.09%` | `20X Cross` |
| `1208` | `0x31ef...f715` | `LONG` | 1,893,477.59 USD | `1,475,080.00` | `1.49` | `1.28` | `1.04` | -305,787.81 USD | `-16.15%` | `3X Isolated` |
| `1266` | `0x7737...bf66` | `SHORT` | 1,814,183.61 USD | `1,413,466.00` | `1.41` | `1.28` | `13.95` | 184,685.04 USD | `+10.18%` | `10X Cross` |
| `1283` | `0x77ee...a018` | `LONG` | 1,790,602.75 USD | `1,394,985.00` | `1.28` | `1.28` | `0.000000` | -1,257.41 USD | `-0.07%` | `20X Cross` |
| `1285` | `0xef96...9383` | `SHORT` | 1,785,533.61 USD | `1,390,999.00` | `1.34` | `1.28` | `4.06` | 78,251.61 USD | `+4.38%` | `20X Cross` |
| `1357` | `0xee2b...d67e` | `LONG` | 1,676,484.89 USD | `1,306,284.00` | `1.55` | `1.28` | `0.2499` | -354,170.02 USD | `-21.13%` | `4X Cross` |
| `1421` | `0x215d...f80a` | `LONG` | 1,606,655.78 USD | `1,251,777.00` | `1.32` | `1.28` | `1.19` | -47,798.45 USD | `-2.98%` | `14X Cross` |
| `1457` | `0x123d...3bff` | `LONG` | 1,560,037.63 USD | `1,215,329.00` | `1.35` | `1.28` | `0.000000` | -77,031.60 USD | `-4.94%` | `10X Cross` |
| `1501` | `0x95da...2328` | `LONG` | 1,504,144.30 USD | `1,171,817.00` | `1.37` | `1.28` | `0.000000` | -97,631.69 USD | `-6.49%` | `5X Cross` |
| `1512` | `0xdf95...7d72` | `SHORT` | 1,489,007.60 USD | `1,160,115.00` | `1.37` | `1.28` | `33.19` | 104,351.66 USD | `+7.01%` | `20X Cross` |
| `1556` | `0x5fa3...35b7` | `SHORT` | 1,431,981.70 USD | `1,115,685.00` | `1.31` | `1.28` | `3.08` | 28,746.55 USD | `+2.01%` | `20X Cross` |
| `1640` | `0x4537...8732` | `SHORT` | 1,334,439.55 USD | `1,039,688.00` | `1.32` | `1.28` | `2.22` | 33,016.40 USD | `+2.47%` | `10X Cross` |
| `1666` | `0xb1ce...681b` | `LONG` | 1,310,923.21 USD | `1,021,764.00` | `1.49` | `1.28` | `1.16` | -213,133.28 USD | `-16.26%` | `4X Isolated` |
| `1770` | `0x3c36...461a` | `LONG` | 1,206,649.46 USD | `940,051.00` | `1.30` | `1.28` | `1.06` | -12,431.15 USD | `-1.03%` | `10X Cross` |
| `1983` | `0xbfc7...80b4` | `SHORT` | 1,026,685.60 USD | `800,000.00` | `1.48` | `1.28` | `6.95` | 156,769.05 USD | `+15.27%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.33` | 184.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.18K USD at 1.3303 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,482.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.48K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,630.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.63K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,000,000.00 USD, Dist: `+2.87%`) | Long MP=`1.28` (Vol: 3,100,000.00 USD, Dist: `--0.59%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.85%`) | Long MP=`1.28` (Vol: 3,000,000.00 USD, Dist: `--0.60%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,200,000.00 USD, Dist: `+5.35%`) | Long MP=`1.28` (Vol: 4,300,000.00 USD, Dist: `--0.68%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+5.09%`) | Long MP=`1.28` (Vol: 4,000,000.00 USD, Dist: `--0.65%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2750` | 651.75 USD | 74,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 378.20 USD | 74,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 213.50 USD | 74,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 9,070.00 USD | 74,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 397.48 USD | 74,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 275.71 USD | 74,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 9,160.00 USD | 74,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,180.00 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,020.00 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 112.50 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 472.78 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,100.00 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 7,220.00 USD | 74,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 19,260.00 USD | 74,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 3,710.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 201.59 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 1,970.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 134,340.00 USD | 74,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 9,640.00 USD | 74,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 7,260.00 USD | 74,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 1,370.00 USD | 74,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 3,020.00 USD | 74,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 1,020.00 USD | 74,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 8,140.00 USD | 74,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 30,280.00 USD | 74,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 10,700.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 1,910.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 22,180.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,520.00 USD | 74,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 470.92 USD | 74,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 52,680.00 USD | 74,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 37,700.00 USD | 74,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 29,470.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 108.75 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 4,640.00 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 9,610.00 USD | 74,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 22,600.00 USD | 74,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 15,760.00 USD | 74,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 35,860.00 USD | 74,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 20,460.00 USD | 74,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 25,490.00 USD | 74,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 21,000.00 USD | 74,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 2,600,000.00 USD | 74,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 218,750.00 USD | 71,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 19,400.00 USD | 71,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 59,650.00 USD | 71,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 113,340.00 USD | 71,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 155,420.00 USD | 71,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 7,570.00 USD | 71,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 31,670.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 71,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 35,400.00 USD | 71,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 39,600.00 USD | 71,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 7,330.00 USD | 71,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 50,690.00 USD | 71,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 79,280.00 USD | 71,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 35,540.00 USD | 70,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 6,370.00 USD | 70,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 657,260.00 USD | 70,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 404,170.00 USD | 70,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 117,220.00 USD | 69,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 118,190.00 USD | 69,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 25,730.00 USD | 69,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 65,090.00 USD | 69,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 2,500,000.00 USD | 69,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 83,620.00 USD | 67,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 978,460.00 USD | 66,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 66,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 156,880.00 USD | 32,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 846,530.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 82,520.00 USD | 31,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 470,330.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 253,600.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 197,110.00 USD | 30,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 89,760.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,070,000.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 406,520.00 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 454,780.00 USD | 26,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 750,760.00 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 113,690.00 USD | 25,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 87,360.00 USD | 25,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 543,620.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 605,630.00 USD | 24,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 87,280.00 USD | 23,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 263,670.00 USD | 23,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 193,800,000.00 USD | 193,800,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 193,350,000.00 USD | 193,350,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 69,400,000.00 USD | 69,400,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 193,200,000.00 USD | 193,200,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 69,330,000.00 USD | 69,330,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 193,030,000.00 USD | 193,030,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 160,170.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,170,000.00 USD | 69,170,000.00 USD | 5,330.00 USD | 14,540.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 192,510,000.00 USD | 192,510,000.00 USD | 45,120.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,070,000.00 USD | 69,070,000.00 USD | 66,460.00 USD | 27,280.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 192,280,000.00 USD | 192,280,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 68,900,000.00 USD | 68,900,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 191,420,000.00 USD | 191,420,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 68,520,000.00 USD | 68,520,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 190,690,000.00 USD | 190,690,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 67,780,000.00 USD | 67,780,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 189,640,000.00 USD | 189,640,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,590,000.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,340,000.00 USD | 67,340,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 188,300,000.00 USD | 188,300,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,020,000.00 USD | 67,020,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 187,340,000.00 USD | 187,340,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 66,840,000.00 USD | 66,840,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 186,270,000.00 USD | 186,270,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 66,670,000.00 USD | 66,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 184,250,000.00 USD | 184,250,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 66,450,000.00 USD | 66,450,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 183,390,000.00 USD | 183,390,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 287,030.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,180,000.00 USD | 66,180,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 182,500,000.00 USD | 182,500,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,960,000.00 USD | 65,960,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 181,850,000.00 USD | 181,850,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,780,000.00 USD | 65,780,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 181,430,000.00 USD | 181,430,000.00 USD | 270,280.00 USD | 156,990.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,700,000.00 USD | 65,700,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 180,790,000.00 USD | 180,790,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,620,000.00 USD | 65,620,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 180,550,000.00 USD | 180,550,000.00 USD | 119,620.00 USD | 66,800.00 USD | 377,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,180,000.00 USD | 21,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,510,000.00 USD | 65,510,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 179,990,000.00 USD | 179,990,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,460,000.00 USD | 65,460,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 179,810,000.00 USD | 179,810,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,420,000.00 USD | 65,420,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 178,890,000.00 USD | 178,890,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,380,000.00 USD | 65,380,000.00 USD | 20,520.00 USD | 18,150.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 178,320,000.00 USD | 178,320,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,290,000.00 USD | 65,290,000.00 USD | 130,470.00 USD | 43,820.00 USD | 83,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 177,950,000.00 USD | 177,950,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 472,230.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,030,000.00 USD | 65,030,000.00 USD | 60,910.00 USD | 18,340.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 177,190,000.00 USD | 177,190,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 64,920,000.00 USD | 64,920,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 176,480,000.00 USD | 176,480,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 64,790,000.00 USD | 64,790,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 176,410,000.00 USD | 176,410,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 64,740,000.00 USD | 64,740,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 176,290,000.00 USD | 176,290,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 175,980,000.00 USD | 175,980,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 838,010.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 64,610,000.00 USD | 64,610,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 175,820,000.00 USD | 175,820,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 64,600,000.00 USD | 64,600,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 175,810,000.00 USD | 175,810,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 175,540,000.00 USD | 175,540,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 174,570,000.00 USD | 174,570,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 174,050,000.00 USD | 174,050,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 371,240.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 173,880,000.00 USD | 173,880,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 173,780,000.00 USD | 173,780,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 173,750,000.00 USD | 173,750,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 173,730,000.00 USD | 173,730,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 173,510,000.00 USD | 173,510,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 172,840,000.00 USD | 172,840,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 64,570,000.00 USD | 64,570,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 172,050,000.00 USD | 172,050,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 64,520,000.00 USD | 64,520,000.00 USD | 102,730.00 USD | 374.17 USD | 215,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 171,370,000.00 USD | 171,370,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 64,200,000.00 USD | 64,200,000.00 USD | 181,600.00 USD | 36,650.00 USD | 416,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 170,230,000.00 USD | 170,230,000.00 USD | 610,450.00 USD | 225,890.00 USD | 556,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 63,570,000.00 USD | 63,570,000.00 USD | 11,570.00 USD | 1,550.00 USD | 73,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 168,830,000.00 USD | 168,830,000.00 USD | 1,120,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 556,980.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 63,480,000.00 USD | 63,480,000.00 USD | 517,670.00 USD | 120,320.00 USD | 554,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 165,810,000.00 USD | 165,810,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 62,290,000.00 USD | 62,290,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 161,320,000.00 USD | 161,320,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 59,830,000.00 USD | 59,830,000.00 USD | 942,890.00 USD | 493,310.00 USD | 740,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 156,420,000.00 USD | 156,420,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 57,650,000.00 USD | 57,650,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 150,500,000.00 USD | 150,500,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 56,770,000.00 USD | 56,770,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 147,450,000.00 USD | 147,450,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 263,760.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 55,760,000.00 USD | 55,760,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 144,220,000.00 USD | 144,220,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 54,930,000.00 USD | 54,930,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 137,950,000.00 USD | 137,950,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 54,250,000.00 USD | 54,250,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 128,500,000.00 USD | 128,500,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 53,510,000.00 USD | 53,510,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 122,080,000.00 USD | 122,080,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 52,640,000.00 USD | 52,640,000.00 USD | 332,170.00 USD | 42,640.00 USD | 632,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 117,720,000.00 USD | 117,720,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 553,020.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,640,000.00 USD | 51,640,000.00 USD | 610,960.00 USD | 49,250.00 USD | 790,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 116,090,000.00 USD | 116,090,000.00 USD | 1,170,000.00 USD | 588,910.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 50,190,000.00 USD | 50,190,000.00 USD | 343,480.00 USD | 176,550.00 USD | 734,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 112,460,000.00 USD | 112,460,000.00 USD | 1,040,000.00 USD | 211,890.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 48,930,000.00 USD | 48,930,000.00 USD | 284,670.00 USD | 71,910.00 USD | 171,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 109,910,000.00 USD | 109,910,000.00 USD | 1,220,000.00 USD | 691,780.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 48,400,000.00 USD | 48,400,000.00 USD | 992,410.00 USD | 254,090.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 106,430,000.00 USD | 106,430,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 46,020,000.00 USD | 46,020,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 101,470,000.00 USD | 101,470,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 14,450,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 40,920,000.00 USD | 40,920,000.00 USD | 2,080,000.00 USD | 1,030,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 92,480,000.00 USD | 92,480,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 36,240,000.00 USD | 36,240,000.00 USD | 1,160,000.00 USD | 377,270.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 79,500,000.00 USD | 79,500,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 33,090,000.00 USD | 33,090,000.00 USD | 1,520,000.00 USD | 418,950.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 71,130,000.00 USD | 71,130,000.00 USD | 2,710,000.00 USD | 1,640,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 28,330,000.00 USD | 28,330,000.00 USD | 1,320,000.00 USD | 332,670.00 USD | 812,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 61,850,000.00 USD | 61,850,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 25,870,000.00 USD | 25,870,000.00 USD | 1,460,000.00 USD | 567,700.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 47,560,000.00 USD | 47,560,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 169,550.00 USD | 173,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 22,110,000.00 USD | 22,110,000.00 USD | 2,960,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 29,710,000.00 USD | 29,710,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 14,930,000.00 USD | 14,930,000.00 USD | 6,210,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,230,000.00 USD | 17,230,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 108,100.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 216,200.00 USD | 216,200.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 3,380,000.00 USD | 3,380,000.00 USD | 1,140,000.00 USD | 161,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 4,600,000.00 USD | 4,600,000.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 3,680.00 USD | 3,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 5,100,000.00 USD | 5,100,000.00 USD | 1,390,000.00 USD | 327,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 6,010,000.00 USD | 6,010,000.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 5,430,000.00 USD | 5,430,000.00 USD | 221,930.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 6,450,000.00 USD | 6,450,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 6,850,000.00 USD | 6,850,000.00 USD | 194,230.00 USD | 0.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 8,600,000.00 USD | 8,600,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 8,340,000.00 USD | 8,340,000.00 USD | 389,390.00 USD | 0.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 11,390,000.00 USD | 11,390,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 11,410,000.00 USD | 11,410,000.00 USD | 673,070.00 USD | 739,400.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 14,240,000.00 USD | 14,240,000.00 USD | 393,240.00 USD | 574,140.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 288,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 14,470,000.00 USD | 14,470,000.00 USD | 521,850.00 USD | 910,560.00 USD | 659,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 14,880,000.00 USD | 14,880,000.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 291.02 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 16,010,000.00 USD | 16,010,000.00 USD | 493,480.00 USD | 319,190.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 21,200,000.00 USD | 21,200,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 17,250,000.00 USD | 17,250,000.00 USD | 455,910.00 USD | 3,540.00 USD | 776,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 23,160,000.00 USD | 23,160,000.00 USD | 530,720.00 USD | 92,380.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 19,550,000.00 USD | 19,550,000.00 USD | 728,090.00 USD | 360,110.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 25,190,000.00 USD | 25,190,000.00 USD | 1,320,000.00 USD | 0.00 USD | 708,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 22,250,000.00 USD | 22,250,000.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 28,940,000.00 USD | 28,940,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 23,970,000.00 USD | 23,970,000.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 30,090,000.00 USD | 30,090,000.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,240.00 USD | 52,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 30,190,000.00 USD | 30,190,000.00 USD | 213,000.00 USD | 1,830,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 34,280,000.00 USD | 34,280,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 37,170,000.00 USD | 37,170,000.00 USD | 2,340,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 39,120,000.00 USD | 39,120,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 40,690,000.00 USD | 40,690,000.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 40,830,000.00 USD | 40,830,000.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 45,220,000.00 USD | 45,220,000.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 43,920,000.00 USD | 43,920,000.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 48,220,000.00 USD | 48,220,000.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 46,540,000.00 USD | 46,540,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 70,310.00 USD | 122,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 50,460,000.00 USD | 50,460,000.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 48,340,000.00 USD | 48,340,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 52,650,000.00 USD | 52,650,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 49,400,000.00 USD | 49,400,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 55,090,000.00 USD | 55,090,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 51,020,000.00 USD | 51,020,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 56,920,000.00 USD | 56,920,000.00 USD | 365,160.00 USD | 249,050.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,420,000.00 USD | 53,420,000.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 58,960,000.00 USD | 58,960,000.00 USD | 1,000,000.00 USD | 131,000.00 USD | 909,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 54,480,000.00 USD | 54,480,000.00 USD | 354,380.00 USD | 48,510.00 USD | 659,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 52,610.00 USD | 175,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 61,320,000.00 USD | 61,320,000.00 USD | 842,300.00 USD | 333,780.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 56,010,000.00 USD | 56,010,000.00 USD | 639,650.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 64,000,000.00 USD | 64,000,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 58,450,000.00 USD | 58,450,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 67,800,000.00 USD | 67,800,000.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 60,340,000.00 USD | 60,340,000.00 USD | 804,660.00 USD | 472,920.00 USD | 605,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 71,510,000.00 USD | 71,510,000.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 66,260,000.00 USD | 66,260,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 75,630,000.00 USD | 75,630,000.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 73,700,000.00 USD | 73,700,000.00 USD | 2,030,000.00 USD | 2,270,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 167,450.00 USD | 342,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 77,540,000.00 USD | 77,540,000.00 USD | 825,410.00 USD | 386,900.00 USD | 692,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 84,460,000.00 USD | 84,460,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 79,390,000.00 USD | 79,390,000.00 USD | 786,490.00 USD | 263,070.00 USD | 799,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 93,290,000.00 USD | 93,290,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 81,910,000.00 USD | 81,910,000.00 USD | 1,120,000.00 USD | 301,120.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 102,500,000.00 USD | 102,500,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 83,240,000.00 USD | 83,240,000.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 111,750,000.00 USD | 111,750,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 85,440,000.00 USD | 85,440,000.00 USD | 935,850.00 USD | 359,860.00 USD | 904,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 119,290,000.00 USD | 119,290,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 346,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 87,360,000.00 USD | 87,360,000.00 USD | 741,530.00 USD | 199,730.00 USD | 978,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 126,460,000.00 USD | 126,460,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,680,000.00 USD | 88,680,000.00 USD | 812,050.00 USD | 76,930.00 USD | 425,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 128,990,000.00 USD | 128,990,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 89,490,000.00 USD | 89,490,000.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 132,050,000.00 USD | 132,050,000.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 90,440,000.00 USD | 90,440,000.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 135,840,000.00 USD | 135,840,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 91,100,000.00 USD | 91,100,000.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 138,680,000.00 USD | 138,680,000.00 USD | 1,430,000.00 USD | 701,190.00 USD | 708,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 198,460.00 USD | 544,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,270,000.00 USD | 91,270,000.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 139,420,000.00 USD | 139,420,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,510,000.00 USD | 91,510,000.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 140,550,000.00 USD | 140,550,000.00 USD | 544,160.00 USD | 184,050.00 USD | 397,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,880,000.00 USD | 91,880,000.00 USD | 76,400.00 USD | 25,940.00 USD | 270,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 142,580,000.00 USD | 142,580,000.00 USD | 538,260.00 USD | 390,570.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 92,020,000.00 USD | 92,020,000.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 144,730,000.00 USD | 144,730,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 92,160,000.00 USD | 92,160,000.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 146,840,000.00 USD | 146,840,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 323.12 USD | 545,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,420,000.00 USD | 92,420,000.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 148,520,000.00 USD | 148,520,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,920,000.00 USD | 92,920,000.00 USD | 231,710.00 USD | 73,260.00 USD | 200,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 150,070,000.00 USD | 150,070,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,630,000.00 USD | 93,630,000.00 USD | 379,220.00 USD | 100,600.00 USD | 223,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 152,110,000.00 USD | 152,110,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,950,000.00 USD | 93,950,000.00 USD | 156,890.00 USD | 53,840.00 USD | 115,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 154,380,000.00 USD | 154,380,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 94,370,000.00 USD | 94,370,000.00 USD | 340,420.00 USD | 17,520.00 USD | 56,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 155,080,000.00 USD | 155,080,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,550.00 USD | 576,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,560,000.00 USD | 94,560,000.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,000,000.00 USD | 156,000,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,710,000.00 USD | 94,710,000.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,860,000.00 USD | 156,860,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,970,000.00 USD | 94,970,000.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,600,000.00 USD | 157,600,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,920,000.00 USD | 157,920,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,990,000.00 USD | 94,990,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,990,000.00 USD | 157,990,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 177,010.00 USD | 753,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 95,090,000.00 USD | 95,090,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,080,000.00 USD | 158,080,000.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,090,000.00 USD | 158,090,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,150,000.00 USD | 158,150,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,230,000.00 USD | 158,230,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,520,000.00 USD | 158,520,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 1,310.00 USD | 755,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,680,000.00 USD | 158,680,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 95,160,000.00 USD | 95,160,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,840,000.00 USD | 158,840,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 95,320,000.00 USD | 95,320,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 159,370,000.00 USD | 159,370,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 95,420,000.00 USD | 95,420,000.00 USD | 5,330.00 USD | 14,540.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 159,590,000.00 USD | 159,590,000.00 USD | 45,120.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 95,430,000.00 USD | 95,430,000.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 159,890,000.00 USD | 159,890,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 758,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,600,000.00 USD | 95,600,000.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 160,450,000.00 USD | 160,450,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,980,000.00 USD | 95,980,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 161,190,000.00 USD | 161,190,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,720,000.00 USD | 96,720,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 162,240,000.00 USD | 162,240,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 97,150,000.00 USD | 97,150,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 163,570,000.00 USD | 163,570,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 97,230,000.00 USD | 97,230,000.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 163,770,000.00 USD | 163,770,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 94,400.00 USD | 853,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 97,480,000.00 USD | 97,480,000.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 164,530,000.00 USD | 164,530,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 97,650,000.00 USD | 97,650,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 165,600,000.00 USD | 165,600,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 97,810,000.00 USD | 97,810,000.00 USD | 39,480.00 USD | 20,150.00 USD | 91,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 167,630,000.00 USD | 167,630,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 168,480,000.00 USD | 168,480,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 169,370,000.00 USD | 169,370,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 33,430.00 USD | 886,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 169,400,000.00 USD | 169,400,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 170,030,000.00 USD | 170,030,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 170,450,000.00 USD | 170,450,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 171,080,000.00 USD | 171,080,000.00 USD | 270,280.00 USD | 156,990.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 171,320,000.00 USD | 171,320,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 599,610.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 171,430,000.00 USD | 171,430,000.00 USD | 50,420.00 USD | 39,100.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 171,890,000.00 USD | 171,890,000.00 USD | 69,200.00 USD | 27,700.00 USD | 365,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,070,000.00 USD | 172,070,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,980,000.00 USD | 172,980,000.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 173,510,000.00 USD | 173,510,000.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 3,300.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 30,250.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 10,700.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 227.20 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 48,310.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 6,630.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 234.85 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,010.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 7,570.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 5,300,000.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 599.17 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 3,350.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 5,140,000.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 8,640.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 10,400.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,690.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 4,070.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 7,510.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,540.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 6,600.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,850.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 406.98 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 2,830,000.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 6,900.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 231,020.00 USD | 15,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,040.00 USD | 15,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 12,520.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 1,720.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,350.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 383,000.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 112,960.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 228,620.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 319,100.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 397.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 971.23 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 249,200.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 40,080.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 10,990.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 176,910.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,630.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 502.55 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 3,360,000.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.43 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 8,860.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 2,320,000.00 USD | 22,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 4,010.00 USD | 22,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 983.18 USD | 22,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 11,660.00 USD | 22,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 66,700.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 991.69 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 1,530.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 4,230.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 143.53 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 3,140.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 67,230.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 90,660.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 109.25 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 954,260.00 USD | 23,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 73,120.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 183,560.00 USD | 24,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 327.38 USD | 24,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 117,950.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 205.38 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 424.72 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 4,190.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 193.83 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 4,710.00 USD | 24,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,760.00 USD | 24,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 496.86 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 117.07 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 102.20 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 25,690.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 2,250.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2750` | 74,990,000.00 USD | 0.00 USD | 651.75 USD | `-78.63%` | `2,370.00` |
| `Live` | `Long` | `0.2850` | 74,990,000.00 USD | 0.00 USD | 378.20 USD | `-77.85%` | `1,327.00` |
| `Live` | `Long` | `0.3050` | 74,990,000.00 USD | 0.00 USD | 213.50 USD | `-76.30%` | `700.00` |
| `Live` | `Long` | `0.3150` | 74,990,000.00 USD | 0.00 USD | 9,070.00 USD | `-75.52%` | `28,791.00` |
| `Live` | `Long` | `0.3250` | 74,980,000.00 USD | 0.00 USD | 397.48 USD | `-74.74%` | `1,223.00` |
| `Live` | `Long` | `0.3350` | 74,980,000.00 USD | 0.00 USD | 275.71 USD | `-73.96%` | `823.00` |
| `Live` | `Long` | `0.3450` | 74,980,000.00 USD | 0.00 USD | 9,160.00 USD | `-73.19%` | `26,562.00` |
| `Live` | `Long` | `0.3550` | 74,970,000.00 USD | 0.00 USD | 2,180.00 USD | `-72.41%` | `6,137.00` |
| `Live` | `Long` | `0.3650` | 74,970,000.00 USD | 0.00 USD | 1,020.00 USD | `-71.63%` | `2,790.00` |
| `Live` | `Long` | `0.3750` | 74,970,000.00 USD | 0.00 USD | 112.50 USD | `-70.86%` | `300.00` |
| `Live` | `Long` | `0.3850` | 74,970,000.00 USD | 0.00 USD | 472.78 USD | `-70.08%` | `1,228.00` |
| `Live` | `Long` | `0.3950` | 74,970,000.00 USD | 0.00 USD | 1,100.00 USD | `-69.30%` | `2,796.00` |
| `Live` | `Long` | `0.4150` | 74,970,000.00 USD | 0.00 USD | 7,220.00 USD | `-67.75%` | `17,407.00` |
| `Live` | `Long` | `0.4250` | 74,960,000.00 USD | 0.00 USD | 19,260.00 USD | `-66.97%` | `45,306.00` |
| `Live` | `Long` | `0.4350` | 74,940,000.00 USD | 0.00 USD | 3,710.00 USD | `-66.19%` | `8,529.00` |
| `Live` | `Long` | `0.4450` | 74,940,000.00 USD | 0.00 USD | 201.59 USD | `-65.41%` | `453.00` |
| `Live` | `Long` | `0.4550` | 74,940,000.00 USD | 0.00 USD | 1,970.00 USD | `-64.64%` | `4,324.00` |
| `Live` | `Long` | `0.4650` | 74,930,000.00 USD | 0.00 USD | 134,340.00 USD | `-63.86%` | `288,906.00` |
| `Live` | `Long` | `0.4750` | 74,800,000.00 USD | 0.00 USD | 9,640.00 USD | `-63.08%` | `20,301.00` |
| `Live` | `Long` | `0.4850` | 74,790,000.00 USD | 0.00 USD | 7,260.00 USD | `-62.31%` | `14,966.00` |
| `Live` | `Long` | `0.4950` | 74,780,000.00 USD | 0.00 USD | 1,370.00 USD | `-61.53%` | `2,766.00` |
| `Live` | `Long` | `0.5050` | 74,780,000.00 USD | 0.00 USD | 3,020.00 USD | `-60.75%` | `5,974.00` |
| `Live` | `Long` | `0.5150` | 74,780,000.00 USD | 0.00 USD | 1,020.00 USD | `-59.97%` | `1,981.00` |
| `Live` | `Long` | `0.5250` | 74,780,000.00 USD | 0.00 USD | 8,140.00 USD | `-59.20%` | `15,514.00` |
| `Live` | `Long` | `0.5350` | 74,770,000.00 USD | 0.00 USD | 30,280.00 USD | `-58.42%` | `56,599.00` |
| `Live` | `Long` | `0.5450` | 74,740,000.00 USD | 0.00 USD | 10,700.00 USD | `-57.64%` | `19,634.00` |
| `Live` | `Long` | `0.5550` | 74,730,000.00 USD | 0.00 USD | 1,910.00 USD | `-56.87%` | `3,436.00` |
| `Live` | `Long` | `0.5650` | 74,730,000.00 USD | 0.00 USD | 22,180.00 USD | `-56.09%` | `39,259.00` |
| `Live` | `Long` | `0.5750` | 74,700,000.00 USD | 0.00 USD | 8,520.00 USD | `-55.31%` | `14,812.00` |
| `Live` | `Long` | `0.5850` | 74,700,000.00 USD | 0.00 USD | 470.92 USD | `-54.53%` | `805.00` |
| `Live` | `Long` | `0.5950` | 74,700,000.00 USD | 0.00 USD | 52,680.00 USD | `-53.76%` | `88,542.00` |
| `Live` | `Long` | `0.6050` | 74,640,000.00 USD | 0.00 USD | 37,700.00 USD | `-52.98%` | `62,315.00` |
| `Live` | `Long` | `0.6150` | 74,610,000.00 USD | 0.00 USD | 29,470.00 USD | `-52.20%` | `47,921.00` |
| `Live` | `Long` | `0.6250` | 74,580,000.00 USD | 0.00 USD | 108.75 USD | `-51.43%` | `174.00` |
| `Live` | `Long` | `0.6350` | 74,580,000.00 USD | 0.00 USD | 4,640.00 USD | `-50.65%` | `7,305.00` |
| `Live` | `Long` | `0.6450` | 74,570,000.00 USD | 0.00 USD | 9,610.00 USD | `-49.87%` | `14,902.00` |
| `Live` | `Long` | `0.6550` | 74,560,000.00 USD | 0.00 USD | 22,600.00 USD | `-49.09%` | `34,508.00` |
| `Live` | `Long` | `0.6650` | 74,540,000.00 USD | 0.00 USD | 15,760.00 USD | `-48.32%` | `23,703.00` |
| `Live` | `Long` | `0.6750` | 74,520,000.00 USD | 0.00 USD | 35,860.00 USD | `-47.54%` | `53,131.00` |
| `Live` | `Long` | `0.6850` | 74,490,000.00 USD | 0.00 USD | 20,460.00 USD | `-46.76%` | `29,872.00` |
| `Live` | `Long` | `0.6950` | 74,470,000.00 USD | 0.00 USD | 25,490.00 USD | `-45.99%` | `36,671.00` |
| `Live` | `Long` | `0.7050` | 74,440,000.00 USD | 0.00 USD | 21,000.00 USD | `-45.21%` | `29,788.00` |
| `Live` | `Long` | `0.7150` | 74,420,000.00 USD | 0.00 USD | 2,600,000.00 USD | `-44.43%` | `3,640,372.00` |
| `Live` | `Long` | `0.7250` | 71,820,000.00 USD | 0.00 USD | 218,750.00 USD | `-43.65%` | `301,725.00` |
| `Live` | `Long` | `0.7350` | 71,600,000.00 USD | 0.00 USD | 19,400.00 USD | `-42.88%` | `26,388.00` |
| `Live` | `Long` | `0.7450` | 71,580,000.00 USD | 0.00 USD | 59,650.00 USD | `-42.10%` | `80,069.00` |
| `Live` | `Long` | `0.7550` | 71,520,000.00 USD | 0.00 USD | 113,340.00 USD | `-41.32%` | `150,116.00` |
| `Live` | `Long` | `0.7650` | 71,410,000.00 USD | 0.00 USD | 155,420.00 USD | `-40.54%` | `203,160.00` |
| `Live` | `Long` | `0.7750` | 71,250,000.00 USD | 0.00 USD | 7,570.00 USD | `-39.77%` | `9,769.00` |
| `Live` | `Long` | `0.7850` | 71,240,000.00 USD | 0.00 USD | 31,670.00 USD | `-38.99%` | `40,345.00` |
| `Live` | `Long` | `0.7950` | 71,210,000.00 USD | 0.00 USD | 11,250.00 USD | `-38.21%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 71,200,000.00 USD | 0.00 USD | 35,400.00 USD | `-37.44%` | `43,970.00` |
| `Live` | `Long` | `0.8150` | 71,160,000.00 USD | 0.00 USD | 39,600.00 USD | `-36.66%` | `48,588.00` |
| `Live` | `Long` | `0.8250` | 71,130,000.00 USD | 0.00 USD | 7,330.00 USD | `-35.88%` | `8,882.00` |
| `Live` | `Long` | `0.8350` | 71,120,000.00 USD | 0.00 USD | 50,690.00 USD | `-35.10%` | `60,709.00` |
| `Live` | `Long` | `0.8450` | 71,070,000.00 USD | 0.00 USD | 79,280.00 USD | `-34.33%` | `93,824.00` |
| `Live` | `Long` | `0.8550` | 70,990,000.00 USD | 0.00 USD | 35,540.00 USD | `-33.55%` | `41,566.00` |
| `Live` | `Long` | `0.8650` | 70,950,000.00 USD | 0.00 USD | 6,370.00 USD | `-32.77%` | `7,362.00` |
| `Live` | `Long` | `0.8750` | 70,950,000.00 USD | 0.00 USD | 657,260.00 USD | `-32.00%` | `751,152.00` |
| `Live` | `Long` | `0.8850` | 70,290,000.00 USD | 0.00 USD | 404,170.00 USD | `-31.22%` | `456,686.00` |
| `Live` | `Long` | `0.8950` | 69,880,000.00 USD | 0.00 USD | 117,220.00 USD | `-30.44%` | `130,973.00` |
| `Live` | `Long` | `0.9050` | 69,770,000.00 USD | 0.00 USD | 118,190.00 USD | `-29.66%` | `130,593.00` |
| `Live` | `Long` | `0.9150` | 69,650,000.00 USD | 0.00 USD | 25,730.00 USD | `-28.89%` | `28,116.00` |
| `Live` | `Long` | `0.9250` | 69,620,000.00 USD | 0.00 USD | 65,090.00 USD | `-28.11%` | `70,365.00` |
| `Live` | `Long` | `0.9350` | 69,560,000.00 USD | 0.00 USD | 2,500,000.00 USD | `-27.33%` | `2,675,179.00` |
| `Live` | `Long` | `0.9450` | 67,060,000.00 USD | 0.00 USD | 83,620.00 USD | `-26.56%` | `88,482.00` |
| `Live` | `Long` | `0.9550` | 66,970,000.00 USD | 0.00 USD | 978,460.00 USD | `-25.78%` | `1,024,565.00` |
| `Live` | `Long` | `0.9650` | 66,000,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-25.00%` | `35,152,879.00` |
| `Live` | `Long` | `0.9750` | 32,070,000.00 USD | 0.00 USD | 156,880.00 USD | `-24.22%` | `160,900.00` |
| `Live` | `Long` | `0.9850` | 31,920,000.00 USD | 0.00 USD | 846,530.00 USD | `-23.45%` | `859,419.00` |
| `Live` | `Long` | `0.9950` | 31,070,000.00 USD | 0.00 USD | 82,520.00 USD | `-22.67%` | `82,933.00` |
| `Live` | `Long` | `1.00` | 30,990,000.00 USD | 0.00 USD | 470,330.00 USD | `-21.89%` | `467,987.00` |
| `Live` | `Long` | `1.01` | 30,520,000.00 USD | 0.00 USD | 253,600.00 USD | `-21.11%` | `249,849.00` |
| `Live` | `Long` | `1.02` | 30,260,000.00 USD | 0.00 USD | 197,110.00 USD | `-20.34%` | `192,305.00` |
| `Live` | `Long` | `1.03` | 30,070,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-19.56%` | `2,048,951.00` |
| `Live` | `Long` | `1.04` | 27,940,000.00 USD | 0.00 USD | 89,760.00 USD | `-18.78%` | `85,898.00` |
| `Live` | `Long` | `1.05` | 27,860,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-18.01%` | `1,016,926.00` |
| `Live` | `Long` | `1.06` | 26,780,000.00 USD | 0.00 USD | 406,520.00 USD | `-17.23%` | `381,711.00` |
| `Live` | `Long` | `1.07` | 26,380,000.00 USD | 0.00 USD | 454,780.00 USD | `-16.45%` | `423,055.00` |
| `Live` | `Long` | `1.08` | 25,920,000.00 USD | 0.00 USD | 750,760.00 USD | `-15.67%` | `691,949.00` |
| `Live` | `Long` | `1.09` | 25,170,000.00 USD | 0.00 USD | 113,690.00 USD | `-14.90%` | `103,826.00` |
| `Live` | `Long` | `1.10` | 25,060,000.00 USD | 0.00 USD | 87,360.00 USD | `-14.12%` | `79,063.00` |
| `Live` | `Long` | `1.11` | 24,970,000.00 USD | 0.00 USD | 543,620.00 USD | `-13.34%` | `487,553.00` |
| `Live` | `Long` | `1.12` | 24,430,000.00 USD | 0.00 USD | 605,630.00 USD | `-12.57%` | `538,338.00` |
| `Live` | `Long` | `1.14` | 23,820,000.00 USD | 0.00 USD | 87,280.00 USD | `-11.79%` | `76,895.00` |
| `Live` | `Long` | `1.15` | 23,730,000.00 USD | 0.00 USD | 263,670.00 USD | `-11.01%` | `230,281.00` |
| `Live` | `Long` | `1.16` | 23,470,000.00 USD | 0.00 USD | 160,170.00 USD | `-10.23%` | `138,671.00` |
| `Live` | `Long` | `1.17` | 23,310,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-9.46%` | `1,367,042.00` |
| `Live` | `Long` | `1.18` | 21,720,000.00 USD | 0.00 USD | 287,030.00 USD | `-8.68%` | `244,281.00` |
| `Live` | `Long` | `1.19` | 21,430,000.00 USD | 0.00 USD | 2,180,000.00 USD | `-7.90%` | `1,837,633.00` |
| `Live` | `Long` | `1.20` | 19,250,000.00 USD | 0.00 USD | 472,230.00 USD | `-7.13%` | `395,171.00` |
| `Live` | `Long` | `1.21` | 18,780,000.00 USD | 0.00 USD | 838,010.00 USD | `-6.35%` | `695,441.00` |
| `Live` | `Long` | `1.22` | 17,940,000.00 USD | 0.00 USD | 371,240.00 USD | `-5.57%` | `305,551.00` |
| `Live` | `Long` | `1.23` | 17,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-4.79%` | `1,282,409.00` |
| `Live` | `Long` | `1.24` | 16,000,000.00 USD | 0.00 USD | 556,980.00 USD | `-4.02%` | `450,994.00` |
| `Live` | `Long` | `1.25` | 15,440,000.00 USD | 0.00 USD | 263,760.00 USD | `-3.24%` | `211,855.00` |
| `Live` | `Long` | `1.25` | 15,180,000.00 USD | 0.00 USD | 553,020.00 USD | `-2.46%` | `440,657.00` |
| `Live` | `Long` | `1.26` | 14,630,000.00 USD | 0.00 USD | 14,450,000.00 USD | `-1.69%` | `11,424,689.00` |
| `Live` | `Long` | `1.27` | 173,230.00 USD | 0.00 USD | 169,550.00 USD | `-0.91%` | `132,978.00` |
| `Live` | `Long` | `1.28` | 3,680.00 USD | 0.00 USD | 3,680.00 USD | `-0.13%` | `2,865.00` |
| `Live` | `Short` | `1.29` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | `+0.65%` | `21,307.00` |
| `Live` | `Short` | `1.30` | 27,880.00 USD | 291.02 USD | 0.00 USD | `+1.42%` | `223.00` |
| `Live` | `Short` | `1.31` | 52,120.00 USD | 24,240.00 USD | 0.00 USD | `+2.20%` | `18,430.00` |
| `Live` | `Short` | `1.32` | 122,420.00 USD | 70,310.00 USD | 0.00 USD | `+2.98%` | `53,061.00` |
| `Live` | `Short` | `1.33` | 175,040.00 USD | 52,610.00 USD | 0.00 USD | `+3.76%` | `39,410.00` |
| `Live` | `Short` | `1.34` | 342,480.00 USD | 167,450.00 USD | 0.00 USD | `+4.53%` | `124,495.00` |
| `Live` | `Short` | `1.35` | 346,480.00 USD | 3,990.00 USD | 0.00 USD | `+5.31%` | `2,947.00` |
| `Live` | `Short` | `1.36` | 544,940.00 USD | 198,460.00 USD | 0.00 USD | `+6.09%` | `145,394.00` |
| `Live` | `Short` | `1.38` | 545,260.00 USD | 323.12 USD | 0.00 USD | `+6.86%` | `235.00` |
| `Live` | `Short` | `1.39` | 576,810.00 USD | 31,550.00 USD | 0.00 USD | `+7.64%` | `22,777.00` |
| `Live` | `Short` | `1.40` | 753,820.00 USD | 177,010.00 USD | 0.00 USD | `+8.42%` | `126,891.00` |
| `Live` | `Short` | `1.41` | 755,130.00 USD | 1,310.00 USD | 0.00 USD | `+9.20%` | `935.00` |
| `Live` | `Short` | `1.42` | 758,990.00 USD | 3,860.00 USD | 0.00 USD | `+9.97%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 853,400.00 USD | 94,400.00 USD | 0.00 USD | `+10.75%` | `66,249.00` |
| `Live` | `Short` | `1.44` | 886,830.00 USD | 33,430.00 USD | 0.00 USD | `+11.53%` | `23,295.00` |
| `Live` | `Short` | `1.45` | 1,490,000.00 USD | 599,610.00 USD | 0.00 USD | `+12.30%` | `414,953.00` |
| `Live` | `Short` | `1.46` | 1,490,000.00 USD | 3,300.00 USD | 0.00 USD | `+13.08%` | `2,268.00` |
| `Live` | `Short` | `1.47` | 1,520,000.00 USD | 30,250.00 USD | 0.00 USD | `+13.86%` | `20,647.00` |
| `Live` | `Short` | `1.48` | 1,530,000.00 USD | 10,700.00 USD | 0.00 USD | `+14.64%` | `7,254.00` |
| `Live` | `Short` | `1.49` | 1,530,000.00 USD | 227.20 USD | 0.00 USD | `+15.41%` | `153.00` |
| `Live` | `Short` | `1.50` | 1,540,000.00 USD | 11,950.00 USD | 0.00 USD | `+16.19%` | `7,994.00` |
| `Live` | `Short` | `1.50` | 1,590,000.00 USD | 48,310.00 USD | 0.00 USD | `+16.97%` | `32,099.00` |
| `Live` | `Short` | `1.51` | 1,600,000.00 USD | 6,630.00 USD | 0.00 USD | `+17.74%` | `4,373.00` |
| `Live` | `Short` | `1.52` | 1,600,000.00 USD | 234.85 USD | 0.00 USD | `+18.52%` | `154.00` |
| `Live` | `Short` | `1.53` | 1,600,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.30%` | `658.00` |
| `Live` | `Short` | `1.54` | 1,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+20.08%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,600,000.00 USD | 1,360.00 USD | 0.00 USD | `+20.85%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,600,000.00 USD | 555.57 USD | 0.00 USD | `+21.63%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,610,000.00 USD | 2,840.00 USD | 0.00 USD | `+22.41%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 1,610,000.00 USD | 7,570.00 USD | 0.00 USD | `+23.19%` | `4,773.00` |
| `Live` | `Short` | `1.60` | 6,910,000.00 USD | 5,300,000.00 USD | 0.00 USD | `+24.74%` | `3,303,247.00` |
| `Live` | `Short` | `1.61` | 6,920,000.00 USD | 599.17 USD | 0.00 USD | `+25.52%` | `371.00` |
| `Live` | `Short` | `1.62` | 6,920,000.00 USD | 3,350.00 USD | 0.00 USD | `+26.29%` | `2,063.00` |
| `Live` | `Short` | `1.64` | 6,930,000.00 USD | 11,270.00 USD | 0.00 USD | `+27.07%` | `6,892.00` |
| `Live` | `Short` | `1.66` | 12,070,000.00 USD | 5,140,000.00 USD | 0.00 USD | `+28.63%` | `3,106,410.00` |
| `Live` | `Short` | `1.67` | 12,070,000.00 USD | 586.08 USD | 0.00 USD | `+29.40%` | `352.00` |
| `Live` | `Short` | `1.68` | 12,070,000.00 USD | 760.45 USD | 0.00 USD | `+30.18%` | `454.00` |
| `Live` | `Short` | `1.69` | 12,080,000.00 USD | 8,640.00 USD | 0.00 USD | `+30.96%` | `5,127.00` |
| `Live` | `Short` | `1.70` | 12,090,000.00 USD | 10,400.00 USD | 0.00 USD | `+31.73%` | `6,133.00` |
| `Live` | `Short` | `1.71` | 12,090,000.00 USD | 1,980.00 USD | 0.00 USD | `+32.51%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 12,090,000.00 USD | 1,690.00 USD | 0.00 USD | `+34.07%` | `977.00` |
| `Live` | `Short` | `1.74` | 12,100,000.00 USD | 2,970.00 USD | 0.00 USD | `+34.84%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 12,100,000.00 USD | 4,070.00 USD | 0.00 USD | `+35.62%` | `2,331.00` |
| `Live` | `Short` | `1.75` | 12,110,000.00 USD | 7,510.00 USD | 0.00 USD | `+36.40%` | `4,278.00` |
| `Live` | `Short` | `1.76` | 12,110,000.00 USD | 2,540.00 USD | 0.00 USD | `+37.17%` | `1,440.00` |
| `Live` | `Short` | `1.77` | 12,120,000.00 USD | 6,600.00 USD | 0.00 USD | `+37.95%` | `3,720.00` |
| `Live` | `Short` | `1.78` | 12,250,000.00 USD | 129,540.00 USD | 0.00 USD | `+38.73%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 12,250,000.00 USD | 2,850.00 USD | 0.00 USD | `+39.51%` | `1,590.00` |
| `Live` | `Short` | `1.80` | 12,250,000.00 USD | 889.87 USD | 0.00 USD | `+40.28%` | `493.00` |
| `Live` | `Short` | `1.82` | 12,250,000.00 USD | 406.98 USD | 0.00 USD | `+41.84%` | `223.00` |
| `Live` | `Short` | `1.83` | 15,080,000.00 USD | 2,830,000.00 USD | 0.00 USD | `+42.61%` | `1,541,914.00` |
| `Live` | `Short` | `1.84` | 15,090,000.00 USD | 6,900.00 USD | 0.00 USD | `+43.39%` | `3,742.00` |
| `Live` | `Short` | `1.85` | 15,320,000.00 USD | 231,020.00 USD | 0.00 USD | `+44.17%` | `124,538.00` |
| `Live` | `Short` | `1.86` | 15,320,000.00 USD | 2,040.00 USD | 0.00 USD | `+44.95%` | `1,095.00` |
| `Live` | `Short` | `1.88` | 15,330,000.00 USD | 12,520.00 USD | 0.00 USD | `+45.72%` | `6,677.00` |
| `Live` | `Short` | `1.89` | 15,340,000.00 USD | 1,720.00 USD | 0.00 USD | `+46.50%` | `915.00` |
| `Live` | `Short` | `1.90` | 15,340,000.00 USD | 4,350.00 USD | 0.00 USD | `+47.28%` | `2,297.00` |
| `Live` | `Short` | `1.91` | 15,340,000.00 USD | 373.38 USD | 0.00 USD | `+48.06%` | `196.00` |
| `Live` | `Short` | `1.92` | 15,720,000.00 USD | 383,000.00 USD | 0.00 USD | `+48.83%` | `200,000.00` |
| `Live` | `Short` | `1.94` | 15,840,000.00 USD | 112,960.00 USD | 0.00 USD | `+50.39%` | `58,378.00` |
| `Live` | `Short` | `1.96` | 15,840,000.00 USD | 293.25 USD | 0.00 USD | `+51.94%` | `150.00` |
| `Live` | `Short` | `1.97` | 16,070,000.00 USD | 228,620.00 USD | 0.00 USD | `+52.72%` | `116,345.00` |
| `Live` | `Short` | `1.98` | 16,380,000.00 USD | 319,100.00 USD | 0.00 USD | `+53.50%` | `161,568.00` |
| `Live` | `Short` | `1.99` | 16,380,000.00 USD | 397.00 USD | 0.00 USD | `+54.27%` | `200.00` |
| `Live` | `Short` | `2.02` | 16,390,000.00 USD | 971.23 USD | 0.00 USD | `+56.60%` | `482.00` |
| `Live` | `Short` | `2.04` | 16,390,000.00 USD | 198.36 USD | 0.00 USD | `+58.94%` | `97.00` |
| `Live` | `Short` | `2.06` | 16,640,000.00 USD | 249,200.00 USD | 0.00 USD | `+60.49%` | `120,680.00` |
| `Live` | `Short` | `2.08` | 16,680,000.00 USD | 40,080.00 USD | 0.00 USD | `+61.27%` | `19,317.00` |
| `Live` | `Short` | `2.08` | 16,690,000.00 USD | 10,990.00 USD | 0.00 USD | `+62.04%` | `5,271.00` |
| `Live` | `Short` | `2.10` | 16,690,000.00 USD | 331.01 USD | 0.00 USD | `+62.82%` | `158.00` |
| `Live` | `Short` | `2.10` | 16,860,000.00 USD | 176,910.00 USD | 0.00 USD | `+63.60%` | `84,043.00` |
| `Live` | `Short` | `2.12` | 16,870,000.00 USD | 3,100.00 USD | 0.00 USD | `+64.38%` | `1,468.00` |
| `Live` | `Short` | `2.15` | 16,870,000.00 USD | 196.11 USD | 0.00 USD | `+67.49%` | `91.00` |
| `Live` | `Short` | `2.17` | 16,870,000.00 USD | 2,630.00 USD | 0.00 USD | `+69.04%` | `1,207.00` |
| `Live` | `Short` | `2.19` | 16,870,000.00 USD | 502.55 USD | 0.00 USD | `+69.82%` | `230.00` |
| `Live` | `Short` | `2.19` | 20,230,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+70.59%` | `1,529,829.00` |
| `Live` | `Short` | `2.21` | 20,230,000.00 USD | 101.43 USD | 0.00 USD | `+71.37%` | `46.00` |
| `Live` | `Short` | `2.21` | 20,240,000.00 USD | 8,860.00 USD | 0.00 USD | `+72.15%` | `4,000.00` |
| `Live` | `Short` | `2.23` | 22,560,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+72.93%` | `1,042,040.00` |
| `Live` | `Short` | `2.25` | 22,560,000.00 USD | 4,010.00 USD | 0.00 USD | `+74.48%` | `1,784.00` |
| `Live` | `Short` | `2.25` | 22,560,000.00 USD | 983.18 USD | 0.00 USD | `+75.26%` | `436.00` |
| `Live` | `Short` | `2.27` | 22,570,000.00 USD | 11,660.00 USD | 0.00 USD | `+76.03%` | `5,149.00` |
| `Live` | `Short` | `2.27` | 22,640,000.00 USD | 66,700.00 USD | 0.00 USD | `+76.81%` | `29,319.00` |
| `Live` | `Short` | `2.29` | 22,640,000.00 USD | 991.69 USD | 0.00 USD | `+77.59%` | `434.00` |
| `Live` | `Short` | `2.29` | 22,640,000.00 USD | 1,530.00 USD | 0.00 USD | `+78.37%` | `665.00` |
| `Live` | `Short` | `2.31` | 22,650,000.00 USD | 4,230.00 USD | 0.00 USD | `+79.14%` | `1,837.00` |
| `Live` | `Short` | `2.31` | 22,650,000.00 USD | 143.53 USD | 0.00 USD | `+79.92%` | `62.00` |
| `Live` | `Short` | `2.33` | 22,650,000.00 USD | 3,140.00 USD | 0.00 USD | `+80.70%` | `1,349.00` |
| `Live` | `Short` | `2.33` | 22,720,000.00 USD | 67,230.00 USD | 0.00 USD | `+81.47%` | `28,791.00` |
| `Live` | `Short` | `2.35` | 22,810,000.00 USD | 90,660.00 USD | 0.00 USD | `+82.25%` | `38,659.00` |
| `Live` | `Short` | `2.38` | 22,810,000.00 USD | 109.25 USD | 0.00 USD | `+84.58%` | `46.00` |
| `Live` | `Short` | `2.38` | 23,760,000.00 USD | 954,260.00 USD | 0.00 USD | `+85.36%` | `400,108.00` |
| `Live` | `Short` | `2.40` | 23,830,000.00 USD | 73,120.00 USD | 0.00 USD | `+86.14%` | `30,532.00` |
| `Live` | `Short` | `2.40` | 24,020,000.00 USD | 183,560.00 USD | 0.00 USD | `+86.92%` | `76,323.00` |
| `Live` | `Short` | `2.42` | 24,020,000.00 USD | 327.38 USD | 0.00 USD | `+88.47%` | `135.00` |
| `Live` | `Short` | `2.44` | 24,140,000.00 USD | 117,950.00 USD | 0.00 USD | `+89.25%` | `48,440.00` |
| `Live` | `Short` | `2.44` | 24,140,000.00 USD | 205.38 USD | 0.00 USD | `+90.02%` | `84.00` |
| `Live` | `Short` | `2.46` | 24,140,000.00 USD | 424.72 USD | 0.00 USD | `+90.80%` | `173.00` |
| `Live` | `Short` | `2.46` | 24,140,000.00 USD | 4,190.00 USD | 0.00 USD | `+91.58%` | `1,698.00` |
| `Live` | `Short` | `2.48` | 24,140,000.00 USD | 193.83 USD | 0.00 USD | `+93.13%` | `78.00` |
| `Live` | `Short` | `2.50` | 24,150,000.00 USD | 4,710.00 USD | 0.00 USD | `+93.91%` | `1,888.00` |
| `Live` | `Short` | `2.52` | 24,150,000.00 USD | 5,760.00 USD | 0.00 USD | `+95.46%` | `2,290.00` |
| `Live` | `Short` | `2.52` | 24,190,000.00 USD | 42,710.00 USD | 0.00 USD | `+96.24%` | `16,914.00` |
| `Live` | `Short` | `2.54` | 24,190,000.00 USD | 496.86 USD | 0.00 USD | `+97.02%` | `196.00` |
| `Live` | `Short` | `2.54` | 24,190,000.00 USD | 117.07 USD | 0.00 USD | `+97.80%` | `46.00` |
| `Live` | `Short` | `2.56` | 24,200,000.00 USD | 102.20 USD | 0.00 USD | `+98.57%` | `40.00` |
| `Live` | `Short` | `2.56` | 24,220,000.00 USD | 25,690.00 USD | 0.00 USD | `+99.35%` | `10,017.00` |
| `Live` | `Short` | `2.58` | 24,220,000.00 USD | 2,250.00 USD | 0.00 USD | `+100.13%` | `875.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3050` | 67,390,000.00 USD | 0.00 USD | 147.62 USD | `-76.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3250` | 67,390,000.00 USD | 0.00 USD | 145.28 USD | `-74.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 67,390,000.00 USD | 0.00 USD | 139.12 USD | `-70.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 67,390,000.00 USD | 0.00 USD | 200.86 USD | `-67.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 67,390,000.00 USD | 0.00 USD | 408.51 USD | `-65.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 67,390,000.00 USD | 0.00 USD | 520.52 USD | `-64.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 67,390,000.00 USD | 0.00 USD | 151.12 USD | `-63.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 67,390,000.00 USD | 0.00 USD | 190.00 USD | `-63.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 67,390,000.00 USD | 0.00 USD | 145.50 USD | `-62.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 67,390,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 67,390,000.00 USD | 0.00 USD | 306.60 USD | `-59.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 67,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-56.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 67,380,000.00 USD | 0.00 USD | 374.60 USD | `-56.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 67,380,000.00 USD | 0.00 USD | 100.62 USD | `-54.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 67,380,000.00 USD | 0.00 USD | 791.85 USD | `-50.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 67,380,000.00 USD | 0.00 USD | 573.40 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 67,380,000.00 USD | 0.00 USD | 3,450.00 USD | `-49.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 67,380,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 67,370,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 67,370,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 67,370,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 67,370,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 67,370,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 67,370,000.00 USD | 0.00 USD | 798.57 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 67,370,000.00 USD | 0.00 USD | 690.38 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 67,370,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 67,360,000.00 USD | 0.00 USD | 1,910.00 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 67,360,000.00 USD | 0.00 USD | 838.94 USD | `-29.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 67,360,000.00 USD | 0.00 USD | 188.49 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 67,360,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 67,360,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 67,360,000.00 USD | 0.00 USD | 112.46 USD | `-26.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 67,360,000.00 USD | 0.00 USD | 2,360.00 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 67,350,000.00 USD | 0.00 USD | 3,910.00 USD | `-25.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 67,350,000.00 USD | 0.00 USD | 546,370.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 66,800,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 66,800,000.00 USD | 0.00 USD | 897.49 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 66,800,000.00 USD | 0.00 USD | 15,070.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 66,780,000.00 USD | 0.00 USD | 4,330.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 66,780,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 66,780,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 66,740,000.00 USD | 0.00 USD | 3,970.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 66,730,000.00 USD | 0.00 USD | 7,090.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 66,730,000.00 USD | 0.00 USD | 3,230.00 USD | `-17.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 66,720,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 66,690,000.00 USD | 0.00 USD | 973.25 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 66,690,000.00 USD | 0.00 USD | 8,250.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 66,680,000.00 USD | 0.00 USD | 2,970.00 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 66,680,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 66,670,000.00 USD | 0.00 USD | 77,120.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 66,590,000.00 USD | 0.00 USD | 12,910.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 66,580,000.00 USD | 0.00 USD | 35,220.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 66,540,000.00 USD | 0.00 USD | 5,360.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 66,540,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 66,520,000.00 USD | 0.00 USD | 4,790.00 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 66,520,000.00 USD | 0.00 USD | 90,010.00 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 66,430,000.00 USD | 0.00 USD | 12,570.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 66,420,000.00 USD | 0.00 USD | 57,020.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 66,360,000.00 USD | 0.00 USD | 57,160.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 66,300,000.00 USD | 0.00 USD | 144,860.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 66,160,000.00 USD | 0.00 USD | 398,990.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 65,760,000.00 USD | 0.00 USD | 258,780.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 65,500,000.00 USD | 0.00 USD | 480,130.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 65,020,000.00 USD | 0.00 USD | 134,550.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 64,880,000.00 USD | 0.00 USD | 360,930.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.28` | 64,520,000.00 USD | 0.00 USD | 64,520,000.00 USD | `-0.13%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.29` | 129,630,000.00 USD | 129,630,000.00 USD | 0.00 USD | `+0.65%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.30` | 129,640,000.00 USD | 2,670.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 129,700,000.00 USD | 66,700.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 129,990,000.00 USD | 283,070.00 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 130,100,000.00 USD | 110,440.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 130,270,000.00 USD | 172,830.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 130,300,000.00 USD | 28,410.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 130,600,000.00 USD | 300,090.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 130,670,000.00 USD | 73,650.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 130,740,000.00 USD | 71,640.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 130,820,000.00 USD | 81,740.00 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 135,200,000.00 USD | 4,370,000.00 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 135,230,000.00 USD | 31,160.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 135,250,000.00 USD | 19,800.00 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 135,330,000.00 USD | 82,400.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 135,590,000.00 USD | 260,610.00 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 135,640,000.00 USD | 44,870.00 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 135,660,000.00 USD | 27,080.00 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 135,770,000.00 USD | 108,480.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 135,860,000.00 USD | 84,290.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 135,870,000.00 USD | 15,160.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 135,960,000.00 USD | 84,680.00 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 135,980,000.00 USD | 18,210.00 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 136,010,000.00 USD | 32,440.00 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 136,070,000.00 USD | 57,450.00 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 136,100,000.00 USD | 36,160.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 136,110,000.00 USD | 6,110.00 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 136,110,000.00 USD | 6,300.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 136,120,000.00 USD | 6,410.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 136,130,000.00 USD | 9,700.00 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 136,260,000.00 USD | 126,740.00 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 136,260,000.00 USD | 1,130.00 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 136,340,000.00 USD | 83,090.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 136,340,000.00 USD | 464.75 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 136,540,000.00 USD | 199,230.00 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 136,540,000.00 USD | 3,970.00 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 136,580,000.00 USD | 33,550.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 136,590,000.00 USD | 8,220.00 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 136,590,000.00 USD | 5,760.00 USD | 0.00 USD | `+30.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 136,660,000.00 USD | 70,850.00 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 136,670,000.00 USD | 8,570.00 USD | 0.00 USD | `+31.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 136,930,000.00 USD | 259,410.00 USD | 0.00 USD | `+32.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 136,940,000.00 USD | 14,030.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 136,960,000.00 USD | 14,560.00 USD | 0.00 USD | `+34.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 137,000,000.00 USD | 44,100.00 USD | 0.00 USD | `+34.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 137,010,000.00 USD | 4,710.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 137,010,000.00 USD | 6,330.00 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 137,040,000.00 USD | 21,720.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 137,160,000.00 USD | 122,200.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 137,260,000.00 USD | 96,900.00 USD | 0.00 USD | `+38.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 137,290,000.00 USD | 33,690.00 USD | 0.00 USD | `+39.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 137,290,000.00 USD | 254.51 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 137,290,000.00 USD | 2,530.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 137,290,000.00 USD | 1,830.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 137,300,000.00 USD | 7,630.00 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 137,310,000.00 USD | 5,700.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 137,320,000.00 USD | 8,390.00 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 137,320,000.00 USD | 4,550.00 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 137,320,000.00 USD | 591.89 USD | 0.00 USD | `+46.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 137,360,000.00 USD | 44,350.00 USD | 0.00 USD | `+47.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 137,370,000.00 USD | 10,020.00 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 137,380,000.00 USD | 7,410.00 USD | 0.00 USD | `+48.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 137,380,000.00 USD | 265.10 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 137,380,000.00 USD | 2,040.00 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 137,390,000.00 USD | 1,510.00 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 137,400,000.00 USD | 14,120.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 137,400,000.00 USD | 4,010.00 USD | 0.00 USD | `+53.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 137,400,000.00 USD | 325.54 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 137,410,000.00 USD | 7,020.00 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 137,550,000.00 USD | 138,900.00 USD | 0.00 USD | `+55.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 137,550,000.00 USD | 781.82 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 137,550,000.00 USD | 222.75 USD | 0.00 USD | `+57.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 137,550,000.00 USD | 862.84 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 137,560,000.00 USD | 3,490.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 137,560,000.00 USD | 3,940.00 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 137,560,000.00 USD | 661.93 USD | 0.00 USD | `+61.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 137,680,000.00 USD | 124,400.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 137,690,000.00 USD | 1,580.00 USD | 0.00 USD | `+63.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 137,700,000.00 USD | 13,900.00 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 137,730,000.00 USD | 24,840.00 USD | 0.00 USD | `+66.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 137,780,000.00 USD | 50,580.00 USD | 0.00 USD | `+67.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 137,780,000.00 USD | 1,710.00 USD | 0.00 USD | `+68.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 137,780,000.00 USD | 1,970.00 USD | 0.00 USD | `+70.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 137,930,000.00 USD | 151,380.00 USD | 0.00 USD | `+72.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 137,940,000.00 USD | 7,340.00 USD | 0.00 USD | `+73.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 137,940,000.00 USD | 3,120.00 USD | 0.00 USD | `+76.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 137,940,000.00 USD | 1,140.00 USD | 0.00 USD | `+77.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 137,950,000.00 USD | 12,150.00 USD | 0.00 USD | `+78.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 137,950,000.00 USD | 370.40 USD | 0.00 USD | `+79.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 138,000,000.00 USD | 47,430.00 USD | 0.00 USD | `+81.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 138,000,000.00 USD | 2,410.00 USD | 0.00 USD | `+83.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 138,010,000.00 USD | 475.00 USD | 0.00 USD | `+84.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 138,010,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 138,260,000.00 USD | 251,200.00 USD | 0.00 USD | `+86.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 138,260,000.00 USD | 1,370.00 USD | 0.00 USD | `+87.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 138,260,000.00 USD | 564.92 USD | 0.00 USD | `+89.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 138,270,000.00 USD | 8,110.00 USD | 0.00 USD | `+90.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 138,270,000.00 USD | 3,420.00 USD | 0.00 USD | `+93.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 138,270,000.00 USD | 124.75 USD | 0.00 USD | `+93.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 138,320,000.00 USD | 42,600.00 USD | 0.00 USD | `+94.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 138,320,000.00 USD | 378.75 USD | 0.00 USD | `+96.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 138,320,000.00 USD | 389.88 USD | 0.00 USD | `+99.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.15` | 193,800,000.00 USD | 0.00 USD | 193,800,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD |
| `7D` | `1.15` | 193,350,000.00 USD | 0.00 USD | 193,350,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 69,400,000.00 USD | 0.00 USD | 69,400,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.15` | 193,200,000.00 USD | 0.00 USD | 193,200,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 69,330,000.00 USD | 0.00 USD | 69,330,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.15` | 193,030,000.00 USD | 0.00 USD | 193,030,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD |
| `1D` | `1.16` | 69,170,000.00 USD | 0.00 USD | 69,170,000.00 USD | 5,330.00 USD | 14,540.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 192,510,000.00 USD | 0.00 USD | 192,510,000.00 USD | 45,120.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 69,070,000.00 USD | 0.00 USD | 69,070,000.00 USD | 66,460.00 USD | 27,280.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 192,280,000.00 USD | 0.00 USD | 192,280,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 68,900,000.00 USD | 0.00 USD | 68,900,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 191,420,000.00 USD | 0.00 USD | 191,420,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 68,520,000.00 USD | 0.00 USD | 68,520,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 190,690,000.00 USD | 0.00 USD | 190,690,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.16` | 67,780,000.00 USD | 0.00 USD | 67,780,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.16` | 189,640,000.00 USD | 0.00 USD | 189,640,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.17` | 67,340,000.00 USD | 0.00 USD | 67,340,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 188,300,000.00 USD | 0.00 USD | 188,300,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD |
| `1D` | `1.17` | 67,020,000.00 USD | 0.00 USD | 67,020,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 187,340,000.00 USD | 0.00 USD | 187,340,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 66,840,000.00 USD | 0.00 USD | 66,840,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 186,270,000.00 USD | 0.00 USD | 186,270,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 66,670,000.00 USD | 0.00 USD | 66,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 184,250,000.00 USD | 0.00 USD | 184,250,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `1D` | `1.17` | 66,450,000.00 USD | 0.00 USD | 66,450,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.17` | 183,390,000.00 USD | 0.00 USD | 183,390,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `1D` | `1.18` | 66,180,000.00 USD | 0.00 USD | 66,180,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 182,500,000.00 USD | 0.00 USD | 182,500,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 65,960,000.00 USD | 0.00 USD | 65,960,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 181,850,000.00 USD | 0.00 USD | 181,850,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `1D` | `1.18` | 65,780,000.00 USD | 0.00 USD | 65,780,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 181,430,000.00 USD | 0.00 USD | 181,430,000.00 USD | 270,280.00 USD | 156,990.00 USD | 209,010.00 USD |
| `1D` | `1.18` | 65,700,000.00 USD | 0.00 USD | 65,700,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 180,790,000.00 USD | 0.00 USD | 180,790,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 65,620,000.00 USD | 0.00 USD | 65,620,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.18` | 180,550,000.00 USD | 0.00 USD | 180,550,000.00 USD | 119,620.00 USD | 66,800.00 USD | 377,200.00 USD |
| `1D` | `1.19` | 65,510,000.00 USD | 0.00 USD | 65,510,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 179,990,000.00 USD | 0.00 USD | 179,990,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `1D` | `1.19` | 65,460,000.00 USD | 0.00 USD | 65,460,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 179,810,000.00 USD | 0.00 USD | 179,810,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD |
| `1D` | `1.19` | 65,420,000.00 USD | 0.00 USD | 65,420,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 178,890,000.00 USD | 0.00 USD | 178,890,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD |
| `1D` | `1.19` | 65,380,000.00 USD | 0.00 USD | 65,380,000.00 USD | 20,520.00 USD | 18,150.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 178,320,000.00 USD | 0.00 USD | 178,320,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD |
| `1D` | `1.19` | 65,290,000.00 USD | 0.00 USD | 65,290,000.00 USD | 130,470.00 USD | 43,820.00 USD | 83,580.00 USD |
| `7D` | `1.19` | 177,950,000.00 USD | 0.00 USD | 177,950,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD |
| `1D` | `1.20` | 65,030,000.00 USD | 0.00 USD | 65,030,000.00 USD | 60,910.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 177,190,000.00 USD | 0.00 USD | 177,190,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD |
| `1D` | `1.20` | 64,920,000.00 USD | 0.00 USD | 64,920,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 176,480,000.00 USD | 0.00 USD | 176,480,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD |
| `1D` | `1.20` | 64,790,000.00 USD | 0.00 USD | 64,790,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 176,410,000.00 USD | 0.00 USD | 176,410,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 64,740,000.00 USD | 0.00 USD | 64,740,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 176,290,000.00 USD | 0.00 USD | 176,290,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD |
| `7D` | `1.20` | 175,980,000.00 USD | 0.00 USD | 175,980,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 64,610,000.00 USD | 0.00 USD | 64,610,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 175,820,000.00 USD | 0.00 USD | 175,820,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD |
| `1D` | `1.21` | 64,600,000.00 USD | 0.00 USD | 64,600,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 175,810,000.00 USD | 0.00 USD | 175,810,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD |
| `7D` | `1.21` | 175,540,000.00 USD | 0.00 USD | 175,540,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD |
| `7D` | `1.21` | 174,570,000.00 USD | 0.00 USD | 174,570,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD |
| `7D` | `1.21` | 174,050,000.00 USD | 0.00 USD | 174,050,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD |
| `7D` | `1.22` | 173,880,000.00 USD | 0.00 USD | 173,880,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 173,780,000.00 USD | 0.00 USD | 173,780,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `1.22` | 173,750,000.00 USD | 0.00 USD | 173,750,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD |
| `7D` | `1.22` | 173,730,000.00 USD | 0.00 USD | 173,730,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD |
| `7D` | `1.22` | 173,510,000.00 USD | 0.00 USD | 173,510,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD |
| `7D` | `1.23` | 172,840,000.00 USD | 0.00 USD | 172,840,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD |
| `1D` | `1.23` | 64,570,000.00 USD | 0.00 USD | 64,570,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 172,050,000.00 USD | 0.00 USD | 172,050,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD |
| `1D` | `1.23` | 64,520,000.00 USD | 0.00 USD | 64,520,000.00 USD | 102,730.00 USD | 374.17 USD | 215,900.00 USD |
| `7D` | `1.23` | 171,370,000.00 USD | 0.00 USD | 171,370,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD |
| `1D` | `1.23` | 64,200,000.00 USD | 0.00 USD | 64,200,000.00 USD | 181,600.00 USD | 36,650.00 USD | 416,160.00 USD |
| `7D` | `1.23` | 170,230,000.00 USD | 0.00 USD | 170,230,000.00 USD | 610,450.00 USD | 225,890.00 USD | 556,760.00 USD |
| `1D` | `1.23` | 63,570,000.00 USD | 0.00 USD | 63,570,000.00 USD | 11,570.00 USD | 1,550.00 USD | 73,470.00 USD |
| `7D` | `1.23` | 168,830,000.00 USD | 0.00 USD | 168,830,000.00 USD | 1,120,000.00 USD | 364,060.00 USD | 1,540,000.00 USD |
| `1D` | `1.24` | 63,480,000.00 USD | 0.00 USD | 63,480,000.00 USD | 517,670.00 USD | 120,320.00 USD | 554,790.00 USD |
| `7D` | `1.24` | 165,810,000.00 USD | 0.00 USD | 165,810,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD |
| `1D` | `1.24` | 62,290,000.00 USD | 0.00 USD | 62,290,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 161,320,000.00 USD | 0.00 USD | 161,320,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD |
| `1D` | `1.24` | 59,830,000.00 USD | 0.00 USD | 59,830,000.00 USD | 942,890.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 156,420,000.00 USD | 0.00 USD | 156,420,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD |
| `1D` | `1.24` | 57,650,000.00 USD | 0.00 USD | 57,650,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD |
| `7D` | `1.24` | 150,500,000.00 USD | 0.00 USD | 150,500,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD |
| `1D` | `1.24` | 56,770,000.00 USD | 0.00 USD | 56,770,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD |
| `7D` | `1.24` | 147,450,000.00 USD | 0.00 USD | 147,450,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 55,760,000.00 USD | 0.00 USD | 55,760,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD |
| `7D` | `1.25` | 144,220,000.00 USD | 0.00 USD | 144,220,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD |
| `1D` | `1.25` | 54,930,000.00 USD | 0.00 USD | 54,930,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 137,950,000.00 USD | 0.00 USD | 137,950,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.25` | 54,250,000.00 USD | 0.00 USD | 54,250,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 128,500,000.00 USD | 0.00 USD | 128,500,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD |
| `1D` | `1.25` | 53,510,000.00 USD | 0.00 USD | 53,510,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 122,080,000.00 USD | 0.00 USD | 122,080,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 52,640,000.00 USD | 0.00 USD | 52,640,000.00 USD | 332,170.00 USD | 42,640.00 USD | 632,330.00 USD |
| `7D` | `1.25` | 117,720,000.00 USD | 0.00 USD | 117,720,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD |
| `1D` | `1.26` | 51,640,000.00 USD | 0.00 USD | 51,640,000.00 USD | 610,960.00 USD | 49,250.00 USD | 790,470.00 USD |
| `7D` | `1.26` | 116,090,000.00 USD | 0.00 USD | 116,090,000.00 USD | 1,170,000.00 USD | 588,910.00 USD | 1,880,000.00 USD |
| `1D` | `1.26` | 50,190,000.00 USD | 0.00 USD | 50,190,000.00 USD | 343,480.00 USD | 176,550.00 USD | 734,200.00 USD |
| `7D` | `1.26` | 112,460,000.00 USD | 0.00 USD | 112,460,000.00 USD | 1,040,000.00 USD | 211,890.00 USD | 1,300,000.00 USD |
| `1D` | `1.26` | 48,930,000.00 USD | 0.00 USD | 48,930,000.00 USD | 284,670.00 USD | 71,910.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 109,910,000.00 USD | 0.00 USD | 109,910,000.00 USD | 1,220,000.00 USD | 691,780.00 USD | 1,580,000.00 USD |
| `1D` | `1.26` | 48,400,000.00 USD | 0.00 USD | 48,400,000.00 USD | 992,410.00 USD | 254,090.00 USD | 1,140,000.00 USD |
| `7D` | `1.26` | 106,430,000.00 USD | 0.00 USD | 106,430,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD |
| `1D` | `1.26` | 46,020,000.00 USD | 0.00 USD | 46,020,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 101,470,000.00 USD | 0.00 USD | 101,470,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD |
| `1D` | `1.27` | 40,920,000.00 USD | 0.00 USD | 40,920,000.00 USD | 2,080,000.00 USD | 1,030,000.00 USD | 1,570,000.00 USD |
| `7D` | `1.27` | 92,480,000.00 USD | 0.00 USD | 92,480,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD |
| `1D` | `1.27` | 36,240,000.00 USD | 0.00 USD | 36,240,000.00 USD | 1,160,000.00 USD | 377,270.00 USD | 1,610,000.00 USD |
| `7D` | `1.27` | 79,500,000.00 USD | 0.00 USD | 79,500,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD |
| `1D` | `1.27` | 33,090,000.00 USD | 0.00 USD | 33,090,000.00 USD | 1,520,000.00 USD | 418,950.00 USD | 2,810,000.00 USD |
| `7D` | `1.27` | 71,130,000.00 USD | 0.00 USD | 71,130,000.00 USD | 2,710,000.00 USD | 1,640,000.00 USD | 4,930,000.00 USD |
| `1D` | `1.27` | 28,330,000.00 USD | 0.00 USD | 28,330,000.00 USD | 1,320,000.00 USD | 332,670.00 USD | 812,070.00 USD |
| `7D` | `1.27` | 61,850,000.00 USD | 0.00 USD | 61,850,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD |
| `1D` | `1.27` | 25,870,000.00 USD | 0.00 USD | 25,870,000.00 USD | 1,460,000.00 USD | 567,700.00 USD | 1,730,000.00 USD |
| `7D` | `1.27` | 47,560,000.00 USD | 0.00 USD | 47,560,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD |
| `1D` | `1.28` | 22,110,000.00 USD | 0.00 USD | 22,110,000.00 USD | 2,960,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `1.28` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD |
| `1D` | `1.28` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 6,210,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 17,230,000.00 USD | 0.00 USD | 17,230,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.28` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `1D` | `1.28` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 108,100.00 USD | 108,100.00 USD | 0.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD |
| `7D` | `1.28` | 216,200.00 USD | 216,200.00 USD | 0.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD |
| `1D` | `1.28` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 1,140,000.00 USD | 161,530.00 USD | 0.00 USD |
| `7D` | `1.28` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD |
| `1D` | `1.29` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 1,390,000.00 USD | 327,360.00 USD | 0.00 USD |
| `7D` | `1.29` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD |
| `1D` | `1.29` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 221,930.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD |
| `1D` | `1.29` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 194,230.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `1.29` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD |
| `1D` | `1.29` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 389,390.00 USD | 0.00 USD | 1,100,000.00 USD |
| `7D` | `1.29` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD |
| `1D` | `1.30` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 673,070.00 USD | 739,400.00 USD | 1,660,000.00 USD |
| `7D` | `1.30` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 393,240.00 USD | 574,140.00 USD | 1,880,000.00 USD |
| `1D` | `1.30` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,210.00 USD |
| `7D` | `1.30` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 521,850.00 USD | 910,560.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `7D` | `1.30` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD |
| `1D` | `1.31` | 16,010,000.00 USD | 16,010,000.00 USD | 0.00 USD | 493,480.00 USD | 319,190.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 455,910.00 USD | 3,540.00 USD | 776,190.00 USD |
| `7D` | `1.31` | 23,160,000.00 USD | 23,160,000.00 USD | 0.00 USD | 530,720.00 USD | 92,380.00 USD | 1,330,000.00 USD |
| `1D` | `1.31` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 728,090.00 USD | 360,110.00 USD | 1,210,000.00 USD |
| `7D` | `1.31` | 25,190,000.00 USD | 25,190,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 708,690.00 USD |
| `1D` | `1.31` | 22,250,000.00 USD | 22,250,000.00 USD | 0.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 28,940,000.00 USD | 28,940,000.00 USD | 0.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 23,970,000.00 USD | 23,970,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 30,090,000.00 USD | 30,090,000.00 USD | 0.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD |
| `1D` | `1.32` | 30,190,000.00 USD | 30,190,000.00 USD | 0.00 USD | 213,000.00 USD | 1,830,000.00 USD | 4,170,000.00 USD |
| `7D` | `1.32` | 34,280,000.00 USD | 34,280,000.00 USD | 0.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 37,170,000.00 USD | 37,170,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 39,120,000.00 USD | 39,120,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 40,690,000.00 USD | 40,690,000.00 USD | 0.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 40,830,000.00 USD | 40,830,000.00 USD | 0.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 45,220,000.00 USD | 45,220,000.00 USD | 0.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD |
| `7D` | `1.32` | 43,920,000.00 USD | 43,920,000.00 USD | 0.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD |
| `1D` | `1.32` | 48,220,000.00 USD | 48,220,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 46,540,000.00 USD | 46,540,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD |
| `1D` | `1.33` | 50,460,000.00 USD | 50,460,000.00 USD | 0.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 48,340,000.00 USD | 48,340,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 52,650,000.00 USD | 52,650,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 49,400,000.00 USD | 49,400,000.00 USD | 0.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 55,090,000.00 USD | 55,090,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 51,020,000.00 USD | 51,020,000.00 USD | 0.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 56,920,000.00 USD | 56,920,000.00 USD | 0.00 USD | 365,160.00 USD | 249,050.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 53,420,000.00 USD | 53,420,000.00 USD | 0.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD |
| `1D` | `1.33` | 58,960,000.00 USD | 58,960,000.00 USD | 0.00 USD | 1,000,000.00 USD | 131,000.00 USD | 909,000.00 USD |
| `7D` | `1.33` | 54,480,000.00 USD | 54,480,000.00 USD | 0.00 USD | 354,380.00 USD | 48,510.00 USD | 659,460.00 USD |
| `1D` | `1.34` | 61,320,000.00 USD | 61,320,000.00 USD | 0.00 USD | 842,300.00 USD | 333,780.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 56,010,000.00 USD | 56,010,000.00 USD | 0.00 USD | 639,650.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 64,000,000.00 USD | 64,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 58,450,000.00 USD | 58,450,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 67,800,000.00 USD | 67,800,000.00 USD | 0.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,520,000.00 USD |
| `7D` | `1.34` | 60,340,000.00 USD | 60,340,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 605,360.00 USD |
| `1D` | `1.34` | 71,510,000.00 USD | 71,510,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 66,260,000.00 USD | 66,260,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD |
| `1D` | `1.34` | 75,630,000.00 USD | 75,630,000.00 USD | 0.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 73,700,000.00 USD | 73,700,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,270,000.00 USD | 3,140,000.00 USD |
| `1D` | `1.35` | 77,540,000.00 USD | 77,540,000.00 USD | 0.00 USD | 825,410.00 USD | 386,900.00 USD | 692,690.00 USD |
| `7D` | `1.35` | 84,460,000.00 USD | 84,460,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 79,390,000.00 USD | 79,390,000.00 USD | 0.00 USD | 786,490.00 USD | 263,070.00 USD | 799,350.00 USD |
| `7D` | `1.35` | 93,290,000.00 USD | 93,290,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD |
| `1D` | `1.35` | 81,910,000.00 USD | 81,910,000.00 USD | 0.00 USD | 1,120,000.00 USD | 301,120.00 USD | 1,100,000.00 USD |
| `7D` | `1.35` | 102,500,000.00 USD | 102,500,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 83,240,000.00 USD | 83,240,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD |
| `7D` | `1.35` | 111,750,000.00 USD | 111,750,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 85,440,000.00 USD | 85,440,000.00 USD | 0.00 USD | 935,850.00 USD | 359,860.00 USD | 904,800.00 USD |
| `7D` | `1.35` | 119,290,000.00 USD | 119,290,000.00 USD | 0.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD |
| `1D` | `1.36` | 87,360,000.00 USD | 87,360,000.00 USD | 0.00 USD | 741,530.00 USD | 199,730.00 USD | 978,960.00 USD |
| `7D` | `1.36` | 126,460,000.00 USD | 126,460,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD |
| `1D` | `1.36` | 88,680,000.00 USD | 88,680,000.00 USD | 0.00 USD | 812,050.00 USD | 76,930.00 USD | 425,930.00 USD |
| `7D` | `1.36` | 128,990,000.00 USD | 128,990,000.00 USD | 0.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 89,490,000.00 USD | 89,490,000.00 USD | 0.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD |
| `7D` | `1.36` | 132,050,000.00 USD | 132,050,000.00 USD | 0.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 90,440,000.00 USD | 90,440,000.00 USD | 0.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD |
| `7D` | `1.36` | 135,840,000.00 USD | 135,840,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 91,100,000.00 USD | 91,100,000.00 USD | 0.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD |
| `7D` | `1.36` | 138,680,000.00 USD | 138,680,000.00 USD | 0.00 USD | 1,430,000.00 USD | 701,190.00 USD | 708,120.00 USD |
| `1D` | `1.37` | 91,270,000.00 USD | 91,270,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 139,420,000.00 USD | 139,420,000.00 USD | 0.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 91,510,000.00 USD | 91,510,000.00 USD | 0.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD |
| `7D` | `1.37` | 140,550,000.00 USD | 140,550,000.00 USD | 0.00 USD | 544,160.00 USD | 184,050.00 USD | 397,850.00 USD |
| `1D` | `1.37` | 91,880,000.00 USD | 91,880,000.00 USD | 0.00 USD | 76,400.00 USD | 25,940.00 USD | 270,940.00 USD |
| `7D` | `1.37` | 142,580,000.00 USD | 142,580,000.00 USD | 0.00 USD | 538,260.00 USD | 390,570.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 92,020,000.00 USD | 92,020,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 144,730,000.00 USD | 144,730,000.00 USD | 0.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD |
| `1D` | `1.37` | 92,160,000.00 USD | 92,160,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.37` | 146,840,000.00 USD | 146,840,000.00 USD | 0.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD |
| `1D` | `1.38` | 92,420,000.00 USD | 92,420,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 148,520,000.00 USD | 148,520,000.00 USD | 0.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD |
| `1D` | `1.38` | 92,920,000.00 USD | 92,920,000.00 USD | 0.00 USD | 231,710.00 USD | 73,260.00 USD | 200,640.00 USD |
| `7D` | `1.38` | 150,070,000.00 USD | 150,070,000.00 USD | 0.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD |
| `1D` | `1.38` | 93,630,000.00 USD | 93,630,000.00 USD | 0.00 USD | 379,220.00 USD | 100,600.00 USD | 223,470.00 USD |
| `7D` | `1.38` | 152,110,000.00 USD | 152,110,000.00 USD | 0.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD |
| `1D` | `1.38` | 93,950,000.00 USD | 93,950,000.00 USD | 0.00 USD | 156,890.00 USD | 53,840.00 USD | 115,580.00 USD |
| `7D` | `1.38` | 154,380,000.00 USD | 154,380,000.00 USD | 0.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD |
| `1D` | `1.38` | 94,370,000.00 USD | 94,370,000.00 USD | 0.00 USD | 340,420.00 USD | 17,520.00 USD | 56,890.00 USD |
| `7D` | `1.38` | 155,080,000.00 USD | 155,080,000.00 USD | 0.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 94,560,000.00 USD | 94,560,000.00 USD | 0.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 156,000,000.00 USD | 156,000,000.00 USD | 0.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD |
| `1D` | `1.39` | 94,710,000.00 USD | 94,710,000.00 USD | 0.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 156,860,000.00 USD | 156,860,000.00 USD | 0.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD |
| `1D` | `1.39` | 94,970,000.00 USD | 94,970,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 157,600,000.00 USD | 157,600,000.00 USD | 0.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD |
| `7D` | `1.39` | 157,920,000.00 USD | 157,920,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 94,990,000.00 USD | 94,990,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.39` | 157,990,000.00 USD | 157,990,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 95,090,000.00 USD | 95,090,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 158,080,000.00 USD | 158,080,000.00 USD | 0.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 158,090,000.00 USD | 158,090,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 158,150,000.00 USD | 158,150,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 158,230,000.00 USD | 158,230,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 158,520,000.00 USD | 158,520,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 158,680,000.00 USD | 158,680,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.41` | 95,160,000.00 USD | 95,160,000.00 USD | 0.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.41` | 158,840,000.00 USD | 158,840,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.41` | 95,320,000.00 USD | 95,320,000.00 USD | 0.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.41` | 159,370,000.00 USD | 159,370,000.00 USD | 0.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD |
| `1D` | `1.41` | 95,420,000.00 USD | 95,420,000.00 USD | 0.00 USD | 5,330.00 USD | 14,540.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 159,590,000.00 USD | 159,590,000.00 USD | 0.00 USD | 45,120.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.41` | 95,430,000.00 USD | 95,430,000.00 USD | 0.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD |
| `7D` | `1.41` | 159,890,000.00 USD | 159,890,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `1D` | `1.42` | 95,600,000.00 USD | 95,600,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 160,450,000.00 USD | 160,450,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `1D` | `1.42` | 95,980,000.00 USD | 95,980,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 161,190,000.00 USD | 161,190,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.42` | 96,720,000.00 USD | 96,720,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 162,240,000.00 USD | 162,240,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.42` | 97,150,000.00 USD | 97,150,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 163,570,000.00 USD | 163,570,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.42` | 97,230,000.00 USD | 97,230,000.00 USD | 0.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD |
| `7D` | `1.42` | 163,770,000.00 USD | 163,770,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `1D` | `1.43` | 97,480,000.00 USD | 97,480,000.00 USD | 0.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD |
| `7D` | `1.43` | 164,530,000.00 USD | 164,530,000.00 USD | 0.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD |
| `1D` | `1.43` | 97,650,000.00 USD | 97,650,000.00 USD | 0.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.43` | 165,600,000.00 USD | 165,600,000.00 USD | 0.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.43` | 97,810,000.00 USD | 97,810,000.00 USD | 0.00 USD | 39,480.00 USD | 20,150.00 USD | 91,060.00 USD |
| `7D` | `1.43` | 167,630,000.00 USD | 167,630,000.00 USD | 0.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `7D` | `1.43` | 168,480,000.00 USD | 168,480,000.00 USD | 0.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `7D` | `1.43` | 169,370,000.00 USD | 169,370,000.00 USD | 0.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `7D` | `1.44` | 169,400,000.00 USD | 169,400,000.00 USD | 0.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD |
| `7D` | `1.44` | 170,030,000.00 USD | 170,030,000.00 USD | 0.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD |
| `7D` | `1.44` | 170,450,000.00 USD | 170,450,000.00 USD | 0.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `7D` | `1.44` | 171,080,000.00 USD | 171,080,000.00 USD | 0.00 USD | 270,280.00 USD | 156,990.00 USD | 209,010.00 USD |
| `7D` | `1.44` | 171,320,000.00 USD | 171,320,000.00 USD | 0.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD |
| `7D` | `1.45` | 171,430,000.00 USD | 171,430,000.00 USD | 0.00 USD | 50,420.00 USD | 39,100.00 USD | 12,180.00 USD |
| `7D` | `1.45` | 171,890,000.00 USD | 171,890,000.00 USD | 0.00 USD | 69,200.00 USD | 27,700.00 USD | 365,030.00 USD |
| `7D` | `1.45` | 172,070,000.00 USD | 172,070,000.00 USD | 0.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `7D` | `1.45` | 172,980,000.00 USD | 172,980,000.00 USD | 0.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD |
| `7D` | `1.45` | 173,510,000.00 USD | 173,510,000.00 USD | 0.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.99B` | Total OI Tokens: `2,332,910,055.1 XRP`
  * 1h OI Change: `-0.43%` | 4h OI Change: `-1.02%` | 24h OI Change: `+0.56%`
  * Exchange Breakdown: Binance=`491.39M` | Bybit=`330.06M` | OKX=`100.34M` | Hyperliquid=`225.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `59.92K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0093%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0034%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0094%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0037%` |
| **CoinM Binance** | `0.0085%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `57.76%` | `42.24%` | `1.37` | 302,240,000.00 USD |
| `15M` | `Binance` | `55.53%` | `44.47%` | `1.25` | 80,380,000.00 USD |
| `15M` | `OKX` | `60.34%` | `39.66%` | `1.52` | 49,780,000.00 USD |
| `15M` | `Bybit` | `53.81%` | `46.19%` | `1.16` | 27,690,000.00 USD |
| `15M` | `KuCoin` | `100%` | `0%` | `1.00` | 195.46 USD |
| `15M` | `Gate` | `47.41%` | `52.59%` | `0.90` | 46,000,000.00 USD |
| `15M` | `Bitget` | `62.74%` | `37.26%` | `1.68` | 17,730,000.00 USD |
| `15M` | `BingX` | `42.83%` | `57.17%` | `0.75` | 9,330,000.00 USD |
| `15M` | `MEXC` | `62.88%` | `37.12%` | `1.69` | 11,700,000.00 USD |
| `15M` | `Bitunix` | `44.29%` | `55.71%` | `0.80` | 10,060,000.00 USD |
| `15M` | `Hyperliquid` | `45%` | `55%` | `0.82` | 3,510,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `74.78%` | `25.22%` | `2.97` | 1,420,000.00 USD |
| `15M` | `Crypto.com` | `68.3%` | `31.7%` | `2.15` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.09%` | `1.91%` | `51.36` | 21,570,000.00 USD |
| `15M` | `HTX` | `59.8%` | `40.2%` | `1.49` | 5,900,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 702,510.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 11,700.00 USD |
| `15M` | `Kraken` | `54.53%` | `45.47%` | `1.20` | 3,320,000.00 USD |
| `15M` | `Aster` | `46.43%` | `53.57%` | `0.87` | 2,340,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.81%` | `67.19%` | `0.49` | 10,800,000.00 USD |
| `15M` | `Whale Positions` | `55.53%` | `44.47%` | `1.25` | 80,380,000.00 USD |
| `15M` | `Global Accounts` | `57.76%` | `42.24%` | `1.37` | 302,240,000.00 USD |
| `1H` | `XRP` | `47.16%` | `52.84%` | `0.89` | 1,520,000,000.00 USD |
| `1H` | `Binance` | `44.63%` | `55.37%` | `0.81` | 450,020,000.00 USD |
| `1H` | `OKX` | `44.77%` | `55.23%` | `0.81` | 273,640,000.00 USD |
| `1H` | `Bybit` | `47.49%` | `52.51%` | `0.90` | 120,960,000.00 USD |
| `1H` | `KuCoin` | `39.05%` | `60.95%` | `0.64` | 2,620,000.00 USD |
| `1H` | `Gate` | `49.91%` | `50.09%` | `1.00` | 254,770,000.00 USD |
| `1H` | `Bitget` | `50.89%` | `49.11%` | `1.04` | 98,750,000.00 USD |
| `1H` | `BingX` | `54.32%` | `45.68%` | `1.19` | 22,470,000.00 USD |
| `1H` | `MEXC` | `51.7%` | `48.3%` | `1.07` | 70,510,000.00 USD |
| `1H` | `Bitunix` | `50.26%` | `49.74%` | `1.01` | 52,350,000.00 USD |
| `1H` | `Hyperliquid` | `33.87%` | `66.13%` | `0.51` | 16,450,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.21%` | `49.79%` | `1.01` | 3,680,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `49.69%` | `50.31%` | `0.99` | 81,560,000.00 USD |
| `1H` | `HTX` | `42.24%` | `57.76%` | `0.73` | 18,330,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `43.77%` | `56.23%` | `0.78` | 9,570,000.00 USD |
| `1H` | `Bitfinex` | `61.37%` | `38.63%` | `1.59` | 67,620.00 USD |
| `1H` | `Kraken` | `54.27%` | `45.73%` | `1.19` | 5,700,000.00 USD |
| `1H` | `Aster` | `46.84%` | `53.16%` | `0.88` | 11,060,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.1%` | `47.9%` | `1.09` | 29,500,000.00 USD |
| `1H` | `Whale Positions` | `44.63%` | `55.37%` | `0.81` | 450,020,000.00 USD |
| `1H` | `Global Accounts` | `47.16%` | `52.84%` | `0.89` | 1,520,000,000.00 USD |
| `4H` | `XRP` | `45.47%` | `54.53%` | `0.83` | 9,730,000,000.00 USD |
| `4H` | `Binance` | `46.17%` | `53.83%` | `0.86` | 2,910,000,000.00 USD |
| `4H` | `OKX` | `44.76%` | `55.24%` | `0.81` | 1,870,000,000.00 USD |
| `4H` | `Bybit` | `44.18%` | `55.82%` | `0.79` | 712,020,000.00 USD |
| `4H` | `KuCoin` | `46.67%` | `53.33%` | `0.88` | 29,610,000.00 USD |
| `4H` | `Gate` | `47.54%` | `52.46%` | `0.91` | 1,530,000,000.00 USD |
| `4H` | `Bitget` | `45.38%` | `54.62%` | `0.83` | 532,360,000.00 USD |
| `4H` | `BingX` | `33.94%` | `66.06%` | `0.51` | 140,800,000.00 USD |
| `4H` | `MEXC` | `49%` | `51%` | `0.96` | 406,470,000.00 USD |
| `4H` | `Bitunix` | `48.52%` | `51.48%` | `0.94` | 352,380,000.00 USD |
| `4H` | `Hyperliquid` | `42.86%` | `57.14%` | `0.75` | 266,700,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.07%` | `44.93%` | `1.23` | 25,360,000.00 USD |
| `4H` | `Crypto.com` | `51.3%` | `48.7%` | `1.05` | 0.00 USD |
| `4H` | `WhiteBIT` | `33.84%` | `66.16%` | `0.51` | 488,110,000.00 USD |
| `4H` | `HTX` | `65.56%` | `34.44%` | `1.90` | 149,660,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 54,200,000.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 1,640,000.00 USD |
| `4H` | `Kraken` | `52.72%` | `47.28%` | `1.12` | 46,530,000.00 USD |
| `4H` | `Aster` | `41.16%` | `58.84%` | `0.70` | 91,270,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.99%` | `55.01%` | `0.82` | 127,160,000.00 USD |
| `4H` | `Whale Positions` | `46.17%` | `53.83%` | `0.86` | 2,910,000,000.00 USD |
| `4H` | `Global Accounts` | `45.47%` | `54.53%` | `0.83` | 9,730,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 9,199,982.08 USD | 4,187,578.87 USD | 5,012,403.21 USD | -824,824.35 USD | `-8.97%` | `4B / 7S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 5,359,755.08 USD | 2,909,456.29 USD | 2,450,298.78 USD | 459,157.51 USD | `+8.57%` | `5B / 3S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 8,857,459.31 USD | 3,136,112.07 USD | 5,721,347.24 USD | -2,585,235.17 USD | `-29.19%` | `5B / 22S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 11,824,590.46 USD | 6,782,340.79 USD | 5,042,249.67 USD | 1,740,091.12 USD | `+14.72%` | `12B / 8S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,908,299.96 USD | 2,545,215.27 USD | 2,363,084.69 USD | 182,130.57 USD | `+3.71%` | `7B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 30,348,241.89 USD | 10,177,546.51 USD | 20,170,695.38 USD | -9,993,148.87 USD | `-32.93%` | `4B / 38S` |
| `5:00 UTC` | `1.29` | `1.28` | `1.29` | `1.29` | `1.28` | 10,140,362.32 USD | 5,667,315.95 USD | 4,473,046.37 USD | 1,194,269.58 USD | `+11.78%` | `17B / 12S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 4,524,791.78 USD | 2,182,409.83 USD | 2,342,381.94 USD | -159,972.11 USD | `-3.54%` | `5B / 13S` |

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
| `5m` | 288,650.00 USD | 373,460.00 USD | **`ACCUMULATION`** |
| `15m` | 1,070,000.00 USD | 1,870,000.00 USD | **`ACCUMULATION`** |
| `30m` | -831,930.00 USD | 931,620.00 USD | **`ACCUMULATION`** |
| `1h` | -5,940,000.00 USD | -15,470,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,530,000.00 USD | -22,340,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -9,370,000.00 USD | -29,150,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,570,000.00 USD | -23,060,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -8,900,000.00 USD | -25,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,450,000.00 USD | -25,540,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -29,300,000.00 USD | -75,560,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,100,000.00 USD | -95,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -559,760,000.00 USD | -1,190,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+288.65K` | 15m=`+1.07M` | 1h=`-5.94M` | 24h=`-29.30M`
* Futures Capital Netflows: 5m=`+373.46K` | 15m=`+1.87M` | 1h=`-15.47M` | 24h=`-75.56M`
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
  * `2026-10-30 00:17:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:38:29 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0127` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0127` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
