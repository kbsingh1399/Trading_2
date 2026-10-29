# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:23:52 IST` (`2026-10-29 19:53:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.28` | **Live Ask Quote**: `1.28` | **Mid Price**: `1.28`
- **Spread Points**: `3.00` | **Spread BPS**: `23.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.28` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.29` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.29` | Lower -2.51σ Band: `1.28`
  * Upper +2.01σ Band: `1.29` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.29` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.29` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.29` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.28` | EMA-20=`1.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.28`
  * Institutional Anchors: EMA-144=`1.28` | EMA-200=`1.28` (Slope: `+0.0000`) | EMA-233=`1.28`
- **Range Boundaries**: 24H High=`1.30` | 24H Low=`1.27` | Weekly High=`1.31` | Weekly Low=`1.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-1.32%`)
  * Point of Control (POC) = `1.29` (Distance: `-0.50%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-0.12%`)
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
  * Optimal Trade Entry (OTE 0.705): `1.29`
  * Structural Invalidation Anchor (0.786): `1.29`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.28` | `1.29` | `1.28` | `1.29` | `1,239,175` | 1,592,910.27 USD | 177,637.10 USD | `+11.15%` | -36,941,324.71 USD | `+0.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.29` | `1.29` | `1.28` | `1.28` | `753,102` | 967,730.17 USD | -76,753.17 USD | `-7.93%` | -37,018,077.88 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.28` | `1.29` | `1.28` | `1.29` | `615,079` | 790,793.26 USD | 113,161.77 USD | `+14.31%` | -36,904,916.11 USD | `+0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.28` | `1.28` | `4,587,205` | 5,885,752.93 USD | -256,403.68 USD | `-4.36%` | -37,051,087.85 USD | `+0.17` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.28` | `3,926,090` | 5,036,330.68 USD | -67,873.95 USD | `-1.35%` | -37,118,961.81 USD | `+0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.29` | `2,607,356` | 3,351,433.70 USD | 214,045.70 USD | `+6.39%` | -36,904,916.11 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.29` | `27,238,695` | 35,241,786.93 USD | -1,210,810.88 USD | `-3.44%` | -29,377,946.50 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `38,773,350` | 49,794,344.17 USD | -9,116,518.67 USD | `-18.31%` | -38,494,465.17 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `11,108,703` | 14,258,160.33 USD | -125,588.91 USD | `-0.88%` | -38,620,054.08 USD | `+0.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.29` | `107,654,816` | 139,158,819.11 USD | -14,117,878.94 USD | `-10.15%` | -38,620,054.08 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.29` | `107,654,816` | 139,158,819.11 USD | -14,117,878.94 USD | `-10.15%` | -38,620,054.08 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.28` | `74507.0000` | 95,741.49 USD | 902,949.48 USD | `7 orders` | `+0.09%` | `-` |
| `ASK` | `1.28` | `88224.0000` | 113,359.02 USD | 807,207.98 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `1.28` | `107423.0000` | 138,017.07 USD | 693,848.96 USD | `16 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `65859.0000` | 84,609.06 USD | 555,831.89 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `120256.0000` | 154,480.86 USD | 471,222.84 USD | `18 orders` | `+0.06%` | `-` |
| `ASK` | `1.28` | `25758.0000` | 33,086.15 USD | 316,741.98 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `1.28` | `39516.0000` | 50,754.35 USD | 283,655.83 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `62168.0000` | 79,842.36 USD | 232,901.48 USD | `13 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `43997.0000` | 56,500.95 USD | 153,059.11 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `1.28` | `43582.0000` | 55,963.65 USD | 96,558.17 USD | `10 orders` | `+0.02%` | `-` |
| `ASK` | `1.28` | `14540.0000` | 18,669.36 USD | 40,594.52 USD | `9 orders` | `+0.01%` | `-` |
| `ASK` | `1.28` | `17077.0000` | 21,925.16 USD | 21,925.16 USD | `8 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.28` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.28` | `0.00%` | `-` |
| `BID` | `1.28` | `8505.0000` | 10,918.72 USD | 10,918.72 USD | `4 orders` | `-0.00%` | `-` |
| `BID` | `1.28` | `3458.0000` | 4,439.03 USD | 15,357.75 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `1.28` | `7028.0000` | 9,021.14 USD | 24,378.89 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `1.28` | `38479.0000` | 49,387.80 USD | 73,766.69 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `1.28` | `60293.0000` | 77,380.04 USD | 151,146.73 USD | `19 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `96188.0000` | 123,438.06 USD | 274,584.79 USD | `14 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `77888.0000` | 99,945.88 USD | 374,530.67 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `1.28` | `52230.0000` | 67,016.31 USD | 441,546.98 USD | `18 orders` | `-0.06%` | `-` |
| `BID` | `1.28` | `150748.0000` | 193,409.68 USD | 634,956.67 USD | `21 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `98109.0000` | 125,864.04 USD | 760,820.70 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `107457.0000` | 137,845.84 USD | 898,666.54 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `1.28` | `101565.0000` | 130,277.43 USD | 1,028,943.97 USD | `10 orders` | `-0.09%` | `-` |
| `BID` | `1.28` | `35409.0000` | 45,415.58 USD | 1,074,359.55 USD | `7 orders` | `-0.10%` | `-` |
| `BID` | `1.28` | `95991.0000` | 123,108.46 USD | 1,197,468.01 USD | `12 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `664017.0000` | 851,535.40 USD | 2,049,003.41 USD | `9 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `68665.0000` | 88,049.13 USD | 2,137,052.54 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.28` | `46413.0000` | 59,510.75 USD | 2,196,563.29 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.28` | `64190.0000` | 82,298.00 USD | 2,278,861.29 USD | `9 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `45489.0000` | 58,316.90 USD | 2,337,178.18 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `358905.0000` | 460,080.32 USD | 2,797,258.50 USD | `8 orders` | `-0.15%` | `-` |
| `ASK` | `1.29` | `22609.0000` | 29,070.65 USD | 2,474,223.70 USD | `10 orders` | `+0.15%` | `-` |
| `ASK` | `1.29` | `12963.0000` | 16,666.53 USD | 2,445,153.05 USD | `5 orders` | `+0.14%` | `-` |
| `ASK` | `1.29` | `79847.0000` | 102,651.30 USD | 2,428,486.52 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `1.29` | `477691.0000` | 614,071.78 USD | 2,325,835.21 USD | `13 orders` | `+0.13%` | `-` |
| `ASK` | `1.29` | `30839.0000` | 39,640.45 USD | 1,711,763.43 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.29` | `262640.0000` | 337,571.19 USD | 1,672,122.98 USD | `6 orders` | `+0.11%` | `-` |
| `ASK` | `1.29` | `66198.0000` | 85,077.67 USD | 1,334,551.79 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.29` | `269648.0000` | 346,524.64 USD | 1,249,474.12 USD | `12 orders` | `+0.10%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 45,036,406.41 USD | `35,031,430.00` | `1.13` | `1.28` | `0.9612` | 5,457,523.14 USD | `+12.12%` | `10X Cross` |
| `87` | `0x5b5d...c060` | `SHORT` | 20,490,446.78 USD | `15,947,114.00` | `1.44` | `1.28` | `11.15` | 2,403,615.82 USD | `+11.73%` | `5X Cross` |
| `149` | `0x58f0...0d20` | `LONG` | 14,051,515.92 USD | `10,931,629.00` | `1.36` | `1.28` | `1.26` | -813,637.04 USD | `-5.79%` | `20X Cross` |
| `155` | `0xb83d...6e36` | `SHORT` | 13,572,197.61 USD | `10,555,450.00` | `1.50` | `1.28` | `13.77` | 2,250,372.03 USD | `+16.58%` | `5X Cross` |
| `434` | `0xca49...53c8` | `SHORT` | 5,321,779.62 USD | `4,138,886.00` | `1.44` | `1.28` | `4.39` | 631,543.11 USD | `+11.87%` | `20X Cross` |
| `452` | `0xfc27...9d9d` | `SHORT` | 5,116,049.07 USD | `3,981,671.00` | `1.31` | `1.28` | `4.90` | 117,464.10 USD | `+2.30%` | `20X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,556,805.77 USD | `3,543,946.00` | `1.44` | `1.28` | `0.7175` | -543,186.84 USD | `-11.92%` | `5X Cross` |
| `535` | `0xc30c...a4c9` | `SHORT` | 4,246,679.81 USD | `3,302,753.00` | `1.42` | `1.28` | `1.58` | 453,207.04 USD | `+10.67%` | `8X Cross` |
| `545` | `0xdd53...2b13` | `SHORT` | 4,186,269.78 USD | `3,255,568.00` | `1.44` | `1.28` | `18.77` | 495,371.44 USD | `+11.83%` | `3X Cross` |
| `593` | `0xecb6...2b00` | `SHORT` | 3,924,390.41 USD | `3,054,238.00` | `1.31` | `1.28` | `10.26` | 64,723.67 USD | `+1.65%` | `10X Cross` |
| `598` | `0x9946...0852` | `SHORT` | 3,889,926.71 USD | `3,025,111.00` | `1.43` | `1.28` | `1.65` | 423,257.85 USD | `+10.88%` | `20X Cross` |
| `692` | `0x9aa5...58af` | `SHORT` | 3,347,288.29 USD | `2,604,083.00` | `1.46` | `1.28` | `4.22` | 450,432.37 USD | `+13.46%` | `20X Cross` |
| `704` | `0xf48f...10fe` | `LONG` | 3,299,078.64 USD | `2,565,779.00` | `1.53` | `1.28` | `0.9192` | -625,562.09 USD | `-18.96%` | `4X Cross` |
| `714` | `0x023a...2355` | `SHORT` | 3,245,110.03 USD | `2,525,574.00` | `1.33` | `1.28` | `4.58` | 106,986.98 USD | `+3.30%` | `20X Cross` |
| `744` | `0x45d2...4029` | `SHORT` | 3,154,263.64 USD | `2,453,000.00` | `1.48` | `1.28` | `16.34` | 484,016.78 USD | `+15.34%` | `20X Cross` |
| `1014` | `0xc179...e0c8` | `SHORT` | 2,234,599.14 USD | `1,739,123.00` | `1.30` | `1.28` | `4.82` | 28,623.38 USD | `+1.28%` | `10X Cross` |
| `1077` | `0xfc66...ca06` | `SHORT` | 2,090,441.07 USD | `1,626,929.00` | `1.31` | `1.28` | `22.90` | 41,125.63 USD | `+1.97%` | `20X Cross` |
| `1080` | `0xeadc...9d55` | `LONG` | 2,082,421.31 USD | `1,619,805.00` | `1.21` | `1.28` | `0.000000` | 123,578.28 USD | `+5.93%` | `20X Cross` |
| `1153` | `0x94b2...599e` | `SHORT` | 1,980,410.64 USD | `1,540,696.00` | `1.36` | `1.28` | `1.83` | 120,055.81 USD | `+6.06%` | `20X Cross` |
| `1166` | `0xbcd4...0dd2` | `SHORT` | 1,966,580.95 USD | `1,529,461.00` | `1.31` | `1.28` | `2.13` | 37,963.64 USD | `+1.93%` | `20X Cross` |
| `1182` | `0x3fc5...c0c1` | `SHORT` | 1,943,694.26 USD | `1,511,779.00` | `1.52` | `1.28` | `2.66` | 347,920.34 USD | `+17.90%` | `20X Cross` |
| `1208` | `0x31ef...f715` | `LONG` | 1,896,067.83 USD | `1,475,080.00` | `1.49` | `1.28` | `1.04` | -303,197.57 USD | `-15.99%` | `3X Isolated` |
| `1267` | `0x7737...bf66` | `SHORT` | 1,816,869.20 USD | `1,413,466.00` | `1.41` | `1.28` | `13.88` | 181,999.45 USD | `+10.02%` | `10X Cross` |
| `1279` | `0x77ee...a018` | `LONG` | 1,793,113.72 USD | `1,394,985.00` | `1.28` | `1.28` | `0.000000` | 1,253.56 USD | `+0.07%` | `20X Cross` |
| `1281` | `0xef96...9383` | `SHORT` | 1,788,546.51 USD | `1,390,999.00` | `1.34` | `1.28` | `4.10` | 75,238.71 USD | `+4.21%` | `20X Cross` |
| `1357` | `0xee2b...d67e` | `LONG` | 1,679,750.60 USD | `1,306,284.00` | `1.55` | `1.28` | `0.2519` | -350,904.31 USD | `-20.89%` | `4X Cross` |
| `1422` | `0x215d...f80a` | `LONG` | 1,609,034.16 USD | `1,251,777.00` | `1.32` | `1.28` | `1.19` | -45,420.07 USD | `-2.82%` | `14X Cross` |
| `1456` | `0x123d...3bff` | `LONG` | 1,562,670.03 USD | `1,215,329.00` | `1.35` | `1.28` | `0.000000` | -74,399.19 USD | `-4.76%` | `10X Cross` |
| `1503` | `0x95da...2328` | `LONG` | 1,506,487.94 USD | `1,171,817.00` | `1.37` | `1.28` | `0.000000` | -95,288.05 USD | `-6.33%` | `5X Cross` |
| `1513` | `0xdf95...7d72` | `SHORT` | 1,490,631.76 USD | `1,160,115.00` | `1.37` | `1.28` | `33.14` | 102,727.50 USD | `+6.89%` | `20X Cross` |
| `1549` | `0x5fa3...35b7` | `SHORT` | 1,444,255.41 USD | `1,123,165.00` | `1.31` | `1.28` | `3.06` | 26,071.87 USD | `+1.81%` | `20X Cross` |
| `1642` | `0x4537...8732` | `SHORT` | 1,336,622.89 USD | `1,039,688.00` | `1.32` | `1.28` | `2.22` | 30,833.06 USD | `+2.31%` | `10X Cross` |
| `1667` | `0xb1ce...681b` | `LONG` | 1,313,865.89 USD | `1,021,764.00` | `1.49` | `1.28` | `1.16` | -210,190.60 USD | `-16.00%` | `4X Isolated` |
| `1770` | `0x3c36...461a` | `LONG` | 1,208,717.58 USD | `940,051.00` | `1.30` | `1.28` | `1.06` | -10,363.04 USD | `-0.86%` | `10X Cross` |
| `1981` | `0xbfc7...80b4` | `SHORT` | 1,028,320.00 USD | `800,000.00` | `1.48` | `1.28` | `6.96` | 155,134.65 USD | `+15.09%` | `20X Cross` |

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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.97%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--0.49%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.97%`) | Long MP=`1.28` (Vol: 3,000,000.00 USD, Dist: `--0.49%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,400,000.00 USD, Dist: `+5.10%`) | Long MP=`1.28` (Vol: 4,500,000.00 USD, Dist: `--0.49%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+5.21%`) | Long MP=`1.28` (Vol: 4,000,000.00 USD, Dist: `--0.53%`)
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
| `7D` | `Long Liquidation` | `1.15` | 198,300,000.00 USD | 198,300,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 197,860,000.00 USD | 197,860,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 197,710,000.00 USD | 197,710,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 73,140,000.00 USD | 73,140,000.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 197,540,000.00 USD | 197,540,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,950,000.00 USD | 72,950,000.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 160,170.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 196,810,000.00 USD | 196,810,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,680,000.00 USD | 72,680,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 196,580,000.00 USD | 196,580,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,610,000.00 USD | 72,610,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 195,720,000.00 USD | 195,720,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,300,000.00 USD | 72,300,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 194,980,000.00 USD | 194,980,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 71,680,000.00 USD | 71,680,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 193,930,000.00 USD | 193,930,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 71,060,000.00 USD | 71,060,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,590,000.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 192,600,000.00 USD | 192,600,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,850,000.00 USD | 70,850,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 191,640,000.00 USD | 191,640,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,530,000.00 USD | 70,530,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 190,570,000.00 USD | 190,570,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,370,000.00 USD | 70,370,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 188,540,000.00 USD | 188,540,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,200,000.00 USD | 70,200,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 187,690,000.00 USD | 187,690,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,950,000.00 USD | 69,950,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 287,030.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 186,800,000.00 USD | 186,800,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,600,000.00 USD | 69,600,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 186,150,000.00 USD | 186,150,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,480,000.00 USD | 69,480,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 185,720,000.00 USD | 185,720,000.00 USD | 270,280.00 USD | 134,360.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,310,000.00 USD | 69,310,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 185,110,000.00 USD | 185,110,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,280,000.00 USD | 69,280,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 184,870,000.00 USD | 184,870,000.00 USD | 119,620.00 USD | 65,900.00 USD | 286,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,170,000.00 USD | 69,170,000.00 USD | 48,820.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,180,000.00 USD | 21,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 184,400,000.00 USD | 184,400,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,080,000.00 USD | 69,080,000.00 USD | 1,560.00 USD | 16,590.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 184,220,000.00 USD | 184,220,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,050,000.00 USD | 69,050,000.00 USD | 29,730.00 USD | 103.33 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 183,300,000.00 USD | 183,300,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,000,000.00 USD | 69,000,000.00 USD | 28,290.00 USD | 10,480.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 182,730,000.00 USD | 182,730,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 68,920,000.00 USD | 68,920,000.00 USD | 48,530.00 USD | 27,990.00 USD | 102,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 182,360,000.00 USD | 182,360,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,740,000.00 USD | 68,740,000.00 USD | 83,580.00 USD | 33,950.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 472,230.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 181,600,000.00 USD | 181,600,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,590,000.00 USD | 68,590,000.00 USD | 109,050.00 USD | 6,620.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,890,000.00 USD | 180,890,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,450,000.00 USD | 68,450,000.00 USD | 25,830.00 USD | 21,290.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,820,000.00 USD | 180,820,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,400,000.00 USD | 68,400,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,700,000.00 USD | 180,700,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,370,000.00 USD | 68,370,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,390,000.00 USD | 180,390,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 838,010.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 180,240,000.00 USD | 180,240,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 68,260,000.00 USD | 68,260,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 180,220,000.00 USD | 180,220,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 68,250,000.00 USD | 68,250,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 179,950,000.00 USD | 179,950,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 178,980,000.00 USD | 178,980,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 178,460,000.00 USD | 178,460,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 371,240.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 178,290,000.00 USD | 178,290,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 178,190,000.00 USD | 178,190,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 178,160,000.00 USD | 178,160,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 178,140,000.00 USD | 178,140,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 177,920,000.00 USD | 177,920,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 177,250,000.00 USD | 177,250,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 176,460,000.00 USD | 176,460,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 68,210,000.00 USD | 68,210,000.00 USD | 100,480.00 USD | 374.17 USD | 160,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 175,780,000.00 USD | 175,780,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 67,950,000.00 USD | 67,950,000.00 USD | 265,980.00 USD | 67,310.00 USD | 639,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 174,640,000.00 USD | 174,640,000.00 USD | 706,530.00 USD | 355,960.00 USD | 940,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 66,980,000.00 USD | 66,980,000.00 USD | 91,890.00 USD | 54,570.00 USD | 208,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 172,640,000.00 USD | 172,640,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 66,630,000.00 USD | 66,630,000.00 USD | 119,360.00 USD | 22,970.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 556,980.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 169,600,000.00 USD | 169,600,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 66,480,000.00 USD | 66,480,000.00 USD | 802,870.00 USD | 317,390.00 USD | 716,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 165,110,000.00 USD | 165,110,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 64,640,000.00 USD | 64,640,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 160,200,000.00 USD | 160,200,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 61,730,000.00 USD | 61,730,000.00 USD | 576,610.00 USD | 333,360.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 154,290,000.00 USD | 154,290,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 60,250,000.00 USD | 60,250,000.00 USD | 207,000.00 USD | 233,640.00 USD | 324,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 151,240,000.00 USD | 151,240,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 59,480,000.00 USD | 59,480,000.00 USD | 546,970.00 USD | 84,110.00 USD | 349,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 263,760.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.25` | 148,000,000.00 USD | 148,000,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 58,500,000.00 USD | 58,500,000.00 USD | 384,220.00 USD | 90,850.00 USD | 261,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 141,740,000.00 USD | 141,740,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 57,770,000.00 USD | 57,770,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 132,290,000.00 USD | 132,290,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 57,060,000.00 USD | 57,060,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 125,870,000.00 USD | 125,870,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 56,290,000.00 USD | 56,290,000.00 USD | 471,210.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 121,510,000.00 USD | 121,510,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 55,270,000.00 USD | 55,270,000.00 USD | 607,050.00 USD | 98,250.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 553,020.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.26` | 119,880,000.00 USD | 119,880,000.00 USD | 1,360,000.00 USD | 849,040.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 53,440,000.00 USD | 53,440,000.00 USD | 640,510.00 USD | 336,810.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 114,740,000.00 USD | 114,740,000.00 USD | 1,070,000.00 USD | 211,890.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,440,000.00 USD | 51,440,000.00 USD | 327,310.00 USD | 3,600.00 USD | 313,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 112,450,000.00 USD | 112,450,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 50,790,000.00 USD | 50,790,000.00 USD | 437,560.00 USD | 218,760.00 USD | 631,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 108,970,000.00 USD | 108,970,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 49,500,000.00 USD | 49,500,000.00 USD | 1,470,000.00 USD | 545,220.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 104,020,000.00 USD | 104,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 46,410,000.00 USD | 46,410,000.00 USD | 2,670,000.00 USD | 1,350,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 14,450,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.27` | 95,020,000.00 USD | 95,020,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 40,410,000.00 USD | 40,410,000.00 USD | 1,620,000.00 USD | 666,960.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 82,050,000.00 USD | 82,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 36,270,000.00 USD | 36,270,000.00 USD | 1,520,000.00 USD | 733,250.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 73,670,000.00 USD | 73,670,000.00 USD | 3,090,000.00 USD | 2,160,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 30,750,000.00 USD | 30,750,000.00 USD | 1,480,000.00 USD | 431,480.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 61,960,000.00 USD | 61,960,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 27,140,000.00 USD | 27,140,000.00 USD | 1,410,000.00 USD | 341,030.00 USD | 735,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 47,670,000.00 USD | 47,670,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 24,650,000.00 USD | 24,650,000.00 USD | 2,290,000.00 USD | 848,600.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 169,550.00 USD | 173,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.28` | 29,820,000.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 18,720,000.00 USD | 18,720,000.00 USD | 4,640,000.00 USD | 2,800,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,330,000.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 7,310,000.00 USD | 7,310,000.00 USD | 3,070,000.00 USD | 2,050,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 234,790.00 USD | 234,790.00 USD | 0.00 USD | 234,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 108,100.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 4,390,000.00 USD | 4,390,000.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 8,770,000.00 USD | 8,770,000.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 1,740,000.00 USD | 1,740,000.00 USD | 1,250,000.00 USD | 488,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 3,680.00 USD | 3,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 10,180,000.00 USD | 10,180,000.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 2,210,000.00 USD | 2,210,000.00 USD | 365,870.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 10,620,000.00 USD | 10,620,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 12,770,000.00 USD | 12,770,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 4,460,000.00 USD | 4,460,000.00 USD | 388,000.00 USD | 0.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 15,560,000.00 USD | 15,560,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 8,760,000.00 USD | 8,760,000.00 USD | 1,060,000.00 USD | 449,340.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 20,850,000.00 USD | 20,850,000.00 USD | 777,570.00 USD | 1,090,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 10,490,000.00 USD | 10,490,000.00 USD | 278,090.00 USD | 626,520.00 USD | 829,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 22,090,000.00 USD | 22,090,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 10,750,000.00 USD | 10,750,000.00 USD | 175,900.00 USD | 86,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 23,060,000.00 USD | 23,060,000.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,200,000.00 USD | 12,200,000.00 USD | 193,920.00 USD | 81,320.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 23,920,000.00 USD | 23,920,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 13,620,000.00 USD | 13,620,000.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 14,410,000.00 USD | 14,410,000.00 USD | 299,990.00 USD | 353,430.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 291.02 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 27,810,000.00 USD | 27,810,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 16,160,000.00 USD | 16,160,000.00 USD | 594,820.00 USD | 120,350.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 31,280,000.00 USD | 31,280,000.00 USD | 722,880.00 USD | 352,510.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 18,740,000.00 USD | 18,740,000.00 USD | 785,890.00 USD | 186,820.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 33,040,000.00 USD | 33,040,000.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 20,640,000.00 USD | 20,640,000.00 USD | 767,720.00 USD | 688,780.00 USD | 450,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 36,800,000.00 USD | 36,800,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 23,390,000.00 USD | 23,390,000.00 USD | 1,290,000.00 USD | 511,150.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 37,950,000.00 USD | 37,950,000.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 26,860,000.00 USD | 26,860,000.00 USD | 372,630.00 USD | 572,040.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,240.00 USD | 52,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 42,130,000.00 USD | 42,130,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 33,390,000.00 USD | 33,390,000.00 USD | 1,250,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 46,980,000.00 USD | 46,980,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 38,880,000.00 USD | 38,880,000.00 USD | 1,990,000.00 USD | 977,080.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 48,680,000.00 USD | 48,680,000.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 42,110,000.00 USD | 42,110,000.00 USD | 1,510,000.00 USD | 706,650.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 51,770,000.00 USD | 51,770,000.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 46,700,000.00 USD | 46,700,000.00 USD | 1,970,000.00 USD | 720,740.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 54,390,000.00 USD | 54,390,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 48,690,000.00 USD | 48,690,000.00 USD | 1,080,000.00 USD | 287,550.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 70,310.00 USD | 122,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 56,200,000.00 USD | 56,200,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 51,180,000.00 USD | 51,180,000.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 57,250,000.00 USD | 57,250,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 53,430,000.00 USD | 53,430,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 58,870,000.00 USD | 58,870,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 56,270,000.00 USD | 56,270,000.00 USD | 848,670.00 USD | 298,620.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 61,280,000.00 USD | 61,280,000.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 58,480,000.00 USD | 58,480,000.00 USD | 979,210.00 USD | 152,260.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 62,950,000.00 USD | 62,950,000.00 USD | 450,460.00 USD | 178,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 60,520,000.00 USD | 60,520,000.00 USD | 809,250.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 52,610.00 USD | 175,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 64,490,000.00 USD | 64,490,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 62,590,000.00 USD | 62,590,000.00 USD | 876,830.00 USD | 219,260.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 66,930,000.00 USD | 66,930,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 65,460,000.00 USD | 65,460,000.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 68,800,000.00 USD | 68,800,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 69,050,000.00 USD | 69,050,000.00 USD | 1,780,000.00 USD | 821,890.00 USD | 996,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 74,720,000.00 USD | 74,720,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 73,780,000.00 USD | 73,780,000.00 USD | 2,510,000.00 USD | 785,850.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 82,100,000.00 USD | 82,100,000.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 76,230,000.00 USD | 76,230,000.00 USD | 918,290.00 USD | 629,160.00 USD | 904,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 167,450.00 USD | 342,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 92,860,000.00 USD | 92,860,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 77,630,000.00 USD | 77,630,000.00 USD | 585,620.00 USD | 289,260.00 USD | 527,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 101,690,000.00 USD | 101,690,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 80,630,000.00 USD | 80,630,000.00 USD | 1,290,000.00 USD | 356,450.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 110,900,000.00 USD | 110,900,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 81,720,000.00 USD | 81,720,000.00 USD | 507,940.00 USD | 127,500.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 120,150,000.00 USD | 120,150,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 83,590,000.00 USD | 83,590,000.00 USD | 749,290.00 USD | 397,350.00 USD | 728,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 127,690,000.00 USD | 127,690,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 85,720,000.00 USD | 85,720,000.00 USD | 722,260.00 USD | 297,760.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 346,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 134,860,000.00 USD | 134,860,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 87,460,000.00 USD | 87,460,000.00 USD | 983,180.00 USD | 66,140.00 USD | 685,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 137,390,000.00 USD | 137,390,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,170,000.00 USD | 88,170,000.00 USD | 396,550.00 USD | 150,540.00 USD | 163,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 140,450,000.00 USD | 140,450,000.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,970,000.00 USD | 88,970,000.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 144,240,000.00 USD | 144,240,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 90,070,000.00 USD | 90,070,000.00 USD | 452,880.00 USD | 103,540.00 USD | 545,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 147,020,000.00 USD | 147,020,000.00 USD | 1,430,000.00 USD | 643,080.00 USD | 708,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 90,120,000.00 USD | 90,120,000.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 198,460.00 USD | 544,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 147,760,000.00 USD | 147,760,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,440,000.00 USD | 90,440,000.00 USD | 68,130.00 USD | 85,100.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 148,870,000.00 USD | 148,870,000.00 USD | 544,160.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,830,000.00 USD | 90,830,000.00 USD | 159,370.00 USD | 1,410.00 USD | 229,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 150,600,000.00 USD | 150,600,000.00 USD | 477,130.00 USD | 362,580.00 USD | 883,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,020,000.00 USD | 91,020,000.00 USD | 1,740.00 USD | 66,370.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 152,750,000.00 USD | 152,750,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,170,000.00 USD | 91,170,000.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 154,860,000.00 USD | 154,860,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,290,000.00 USD | 91,290,000.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 323.12 USD | 545,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 156,540,000.00 USD | 156,540,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,620,000.00 USD | 91,620,000.00 USD | 112,910.00 USD | 50,330.00 USD | 164,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 158,090,000.00 USD | 158,090,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,180,000.00 USD | 92,180,000.00 USD | 271,120.00 USD | 72,410.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 160,130,000.00 USD | 160,130,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,660,000.00 USD | 92,660,000.00 USD | 264,080.00 USD | 108,980.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 162,400,000.00 USD | 162,400,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,060,000.00 USD | 93,060,000.00 USD | 304,540.00 USD | 24,460.00 USD | 77,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 163,100,000.00 USD | 163,100,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 93,250,000.00 USD | 93,250,000.00 USD | 91,420.00 USD | 54,030.00 USD | 40,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,550.00 USD | 576,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 164,020,000.00 USD | 164,020,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 93,340,000.00 USD | 93,340,000.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 164,880,000.00 USD | 164,880,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 93,730,000.00 USD | 93,730,000.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 165,620,000.00 USD | 165,620,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 165,940,000.00 USD | 165,940,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 166,010,000.00 USD | 166,010,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 93,750,000.00 USD | 93,750,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 177,010.00 USD | 753,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 166,100,000.00 USD | 166,100,000.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 93,850,000.00 USD | 93,850,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 166,110,000.00 USD | 166,110,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 166,170,000.00 USD | 166,170,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 166,250,000.00 USD | 166,250,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 166,540,000.00 USD | 166,540,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 1,310.00 USD | 755,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 166,700,000.00 USD | 166,700,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 166,860,000.00 USD | 166,860,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,050,000.00 USD | 94,050,000.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 167,590,000.00 USD | 167,590,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,310,000.00 USD | 94,310,000.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 167,820,000.00 USD | 167,820,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,340,000.00 USD | 94,340,000.00 USD | 0.00 USD | 383.75 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 168,120,000.00 USD | 168,120,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,380,000.00 USD | 94,380,000.00 USD | 29,120.00 USD | 9,190.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 758,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 168,680,000.00 USD | 168,680,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,690,000.00 USD | 94,690,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 169,420,000.00 USD | 169,420,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,310,000.00 USD | 95,310,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 170,470,000.00 USD | 170,470,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,930,000.00 USD | 95,930,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 171,800,000.00 USD | 171,800,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,150,000.00 USD | 96,150,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 172,000,000.00 USD | 172,000,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 96,230,000.00 USD | 96,230,000.00 USD | 29,370.00 USD | 27,060.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 94,400.00 USD | 853,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 96,360,000.00 USD | 96,360,000.00 USD | 70,500.00 USD | 8,390.00 USD | 44,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 172,760,000.00 USD | 172,760,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 173,830,000.00 USD | 173,830,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 175,860,000.00 USD | 175,860,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 176,710,000.00 USD | 176,710,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 177,600,000.00 USD | 177,600,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 33,430.00 USD | 886,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 177,630,000.00 USD | 177,630,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 178,260,000.00 USD | 178,260,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 178,680,000.00 USD | 178,680,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 179,290,000.00 USD | 179,290,000.00 USD | 270,280.00 USD | 134,360.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 179,530,000.00 USD | 179,530,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 599,610.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 179,630,000.00 USD | 179,630,000.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 180,000,000.00 USD | 180,000,000.00 USD | 69,200.00 USD | 26,800.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 180,190,000.00 USD | 180,190,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 181,090,000.00 USD | 181,090,000.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 181,630,000.00 USD | 181,630,000.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.3050` | 3,110,000.00 USD | 0.00 USD | 147.62 USD | `-76.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3250` | 3,110,000.00 USD | 0.00 USD | 145.28 USD | `-74.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,110,000.00 USD | 0.00 USD | 139.12 USD | `-70.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 3,110,000.00 USD | 0.00 USD | 200.86 USD | `-67.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,110,000.00 USD | 0.00 USD | 408.51 USD | `-65.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,110,000.00 USD | 0.00 USD | 520.52 USD | `-64.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,110,000.00 USD | 0.00 USD | 151.12 USD | `-63.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,110,000.00 USD | 0.00 USD | 190.00 USD | `-63.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,110,000.00 USD | 0.00 USD | 145.50 USD | `-62.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,110,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,110,000.00 USD | 0.00 USD | 306.60 USD | `-59.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,110,000.00 USD | 0.00 USD | 6,750.00 USD | `-56.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,100,000.00 USD | 0.00 USD | 374.60 USD | `-56.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,100,000.00 USD | 0.00 USD | 100.62 USD | `-54.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,100,000.00 USD | 0.00 USD | 791.85 USD | `-50.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,100,000.00 USD | 0.00 USD | 573.40 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,100,000.00 USD | 0.00 USD | 3,450.00 USD | `-49.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,090,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,090,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,090,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,090,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,090,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,080,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 3,080,000.00 USD | 0.00 USD | 798.57 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 3,080,000.00 USD | 0.00 USD | 690.38 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 3,080,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 3,080,000.00 USD | 0.00 USD | 3,230.00 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 3,080,000.00 USD | 0.00 USD | 838.94 USD | `-29.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 3,080,000.00 USD | 0.00 USD | 188.49 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 3,080,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 3,070,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 3,070,000.00 USD | 0.00 USD | 112.46 USD | `-26.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 3,070,000.00 USD | 0.00 USD | 2,360.00 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 3,070,000.00 USD | 0.00 USD | 3,910.00 USD | `-25.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 3,070,000.00 USD | 0.00 USD | 546,370.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,520,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,510,000.00 USD | 0.00 USD | 897.49 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,510,000.00 USD | 0.00 USD | 15,070.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,500,000.00 USD | 0.00 USD | 4,330.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,490,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,490,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,450,000.00 USD | 0.00 USD | 3,970.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,450,000.00 USD | 0.00 USD | 7,090.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 2,440,000.00 USD | 0.00 USD | 3,230.00 USD | `-17.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 2,440,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 2,410,000.00 USD | 0.00 USD | 973.25 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 2,400,000.00 USD | 0.00 USD | 8,000.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 2,400,000.00 USD | 0.00 USD | 2,970.00 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 2,390,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 2,380,000.00 USD | 0.00 USD | 79,020.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 2,300,000.00 USD | 0.00 USD | 12,910.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 2,290,000.00 USD | 0.00 USD | 16,630.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 2,280,000.00 USD | 0.00 USD | 32,100.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 2,240,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 2,230,000.00 USD | 0.00 USD | 4,790.00 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 2,220,000.00 USD | 0.00 USD | 90,010.00 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,130,000.00 USD | 0.00 USD | 12,570.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 2,120,000.00 USD | 0.00 USD | 52,130.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 2,070,000.00 USD | 0.00 USD | 57,160.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 2,010,000.00 USD | 0.00 USD | 146,570.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 1,870,000.00 USD | 0.00 USD | 382,250.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,480,000.00 USD | 0.00 USD | 291,800.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,190,000.00 USD | 0.00 USD | 486,130.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 705,680.00 USD | 0.00 USD | 140,870.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 564,820.00 USD | 0.00 USD | 561,400.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.28` | 3,410.00 USD | 0.00 USD | 3,410.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 158,560.00 USD | 158,560.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 195,230.00 USD | 36,680.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 308,250.00 USD | 113,020.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 552,900.00 USD | 244,650.00 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 649,320.00 USD | 96,420.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 820,820.00 USD | 171,500.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 848,210.00 USD | 27,390.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,130,000.00 USD | 281,080.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,200,000.00 USD | 71,800.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,270,000.00 USD | 73,090.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,350,000.00 USD | 71,640.00 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,680,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,710,000.00 USD | 30,770.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,730,000.00 USD | 19,640.00 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,820,000.00 USD | 82,400.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,010,000.00 USD | 193,480.00 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,050,000.00 USD | 43,500.00 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,080,000.00 USD | 27,080.00 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,190,000.00 USD | 108,480.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,270,000.00 USD | 84,290.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,290,000.00 USD | 14,970.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,370,000.00 USD | 84,920.00 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,390,000.00 USD | 18,210.00 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,490,000.00 USD | 103,290.00 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,550,000.00 USD | 57,450.00 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,590,000.00 USD | 36,160.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,590,000.00 USD | 6,110.00 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,600,000.00 USD | 6,300.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,610,000.00 USD | 6,410.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,620,000.00 USD | 9,700.00 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,740,000.00 USD | 128,920.00 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,830,000.00 USD | 81,600.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,830,000.00 USD | 464.75 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,030,000.00 USD | 199,230.00 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,030,000.00 USD | 3,370.00 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,060,000.00 USD | 33,550.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,070,000.00 USD | 8,220.00 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,080,000.00 USD | 5,760.00 USD | 0.00 USD | `+30.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,150,000.00 USD | 70,850.00 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,160,000.00 USD | 8,570.00 USD | 0.00 USD | `+31.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,420,000.00 USD | 259,410.00 USD | 0.00 USD | `+32.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,430,000.00 USD | 14,030.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,450,000.00 USD | 14,560.00 USD | 0.00 USD | `+34.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,490,000.00 USD | 44,100.00 USD | 0.00 USD | `+34.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,490,000.00 USD | 4,710.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,500,000.00 USD | 6,330.00 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,520,000.00 USD | 21,720.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,640,000.00 USD | 122,650.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,740,000.00 USD | 96,900.00 USD | 0.00 USD | `+38.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,780,000.00 USD | 40,420.00 USD | 0.00 USD | `+39.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,780,000.00 USD | 254.51 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,780,000.00 USD | 2,530.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,790,000.00 USD | 1,830.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,790,000.00 USD | 7,630.00 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,800,000.00 USD | 1,900.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,800,000.00 USD | 8,390.00 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,810,000.00 USD | 4,550.00 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,810,000.00 USD | 591.89 USD | 0.00 USD | `+46.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,850,000.00 USD | 44,350.00 USD | 0.00 USD | `+47.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,860,000.00 USD | 10,020.00 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 7,870,000.00 USD | 7,410.00 USD | 0.00 USD | `+48.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,870,000.00 USD | 265.10 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,870,000.00 USD | 2,040.00 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,880,000.00 USD | 1,510.00 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,890,000.00 USD | 14,120.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,890,000.00 USD | 4,010.00 USD | 0.00 USD | `+53.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,890,000.00 USD | 325.54 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,900,000.00 USD | 7,020.00 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,040,000.00 USD | 138,900.00 USD | 0.00 USD | `+55.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,040,000.00 USD | 781.82 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,040,000.00 USD | 222.75 USD | 0.00 USD | `+57.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,040,000.00 USD | 862.84 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,040,000.00 USD | 3,490.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,050,000.00 USD | 3,940.00 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,050,000.00 USD | 661.93 USD | 0.00 USD | `+61.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,170,000.00 USD | 124,400.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,180,000.00 USD | 1,580.00 USD | 0.00 USD | `+63.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,190,000.00 USD | 13,900.00 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,210,000.00 USD | 24,840.00 USD | 0.00 USD | `+66.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,260,000.00 USD | 50,580.00 USD | 0.00 USD | `+67.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,270,000.00 USD | 1,710.00 USD | 0.00 USD | `+68.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,270,000.00 USD | 1,970.00 USD | 0.00 USD | `+70.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,420,000.00 USD | 151,380.00 USD | 0.00 USD | `+72.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,430,000.00 USD | 7,340.00 USD | 0.00 USD | `+73.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,430,000.00 USD | 3,120.00 USD | 0.00 USD | `+76.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,430,000.00 USD | 1,140.00 USD | 0.00 USD | `+77.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,440,000.00 USD | 12,150.00 USD | 0.00 USD | `+78.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,440,000.00 USD | 370.40 USD | 0.00 USD | `+79.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,440,000.00 USD | 733.19 USD | 0.00 USD | `+81.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,450,000.00 USD | 2,410.00 USD | 0.00 USD | `+83.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,450,000.00 USD | 475.00 USD | 0.00 USD | `+84.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,450,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,700,000.00 USD | 251,200.00 USD | 0.00 USD | `+86.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,700,000.00 USD | 1,370.00 USD | 0.00 USD | `+87.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,700,000.00 USD | 564.92 USD | 0.00 USD | `+89.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,710,000.00 USD | 8,110.00 USD | 0.00 USD | `+90.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,710,000.00 USD | 3,420.00 USD | 0.00 USD | `+93.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,710,000.00 USD | 124.75 USD | 0.00 USD | `+93.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,760,000.00 USD | 42,600.00 USD | 0.00 USD | `+94.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 8,760,000.00 USD | 378.75 USD | 0.00 USD | `+96.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 8,760,000.00 USD | 389.88 USD | 0.00 USD | `+99.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.15` | 198,300,000.00 USD | 0.00 USD | 198,300,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD |
| `7D` | `1.15` | 197,860,000.00 USD | 0.00 USD | 197,860,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.15` | 197,710,000.00 USD | 0.00 USD | 197,710,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 73,140,000.00 USD | 0.00 USD | 73,140,000.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 197,540,000.00 USD | 0.00 USD | 197,540,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 72,950,000.00 USD | 0.00 USD | 72,950,000.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD |
| `7D` | `1.16` | 196,810,000.00 USD | 0.00 USD | 196,810,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 72,680,000.00 USD | 0.00 USD | 72,680,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD |
| `7D` | `1.16` | 196,580,000.00 USD | 0.00 USD | 196,580,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 72,610,000.00 USD | 0.00 USD | 72,610,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.16` | 195,720,000.00 USD | 0.00 USD | 195,720,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 72,300,000.00 USD | 0.00 USD | 72,300,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.16` | 194,980,000.00 USD | 0.00 USD | 194,980,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.16` | 71,680,000.00 USD | 0.00 USD | 71,680,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.16` | 193,930,000.00 USD | 0.00 USD | 193,930,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.17` | 71,060,000.00 USD | 0.00 USD | 71,060,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.17` | 192,600,000.00 USD | 0.00 USD | 192,600,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD |
| `1D` | `1.17` | 70,850,000.00 USD | 0.00 USD | 70,850,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD |
| `7D` | `1.17` | 191,640,000.00 USD | 0.00 USD | 191,640,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 70,530,000.00 USD | 0.00 USD | 70,530,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 190,570,000.00 USD | 0.00 USD | 190,570,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 70,370,000.00 USD | 0.00 USD | 70,370,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 188,540,000.00 USD | 0.00 USD | 188,540,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `1D` | `1.17` | 70,200,000.00 USD | 0.00 USD | 70,200,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 187,690,000.00 USD | 0.00 USD | 187,690,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `1D` | `1.18` | 69,950,000.00 USD | 0.00 USD | 69,950,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 186,800,000.00 USD | 0.00 USD | 186,800,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 69,600,000.00 USD | 0.00 USD | 69,600,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 186,150,000.00 USD | 0.00 USD | 186,150,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `1D` | `1.18` | 69,480,000.00 USD | 0.00 USD | 69,480,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 185,720,000.00 USD | 0.00 USD | 185,720,000.00 USD | 270,280.00 USD | 134,360.00 USD | 209,010.00 USD |
| `1D` | `1.18` | 69,310,000.00 USD | 0.00 USD | 69,310,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD |
| `7D` | `1.18` | 185,110,000.00 USD | 0.00 USD | 185,110,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 69,280,000.00 USD | 0.00 USD | 69,280,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 184,870,000.00 USD | 0.00 USD | 184,870,000.00 USD | 119,620.00 USD | 65,900.00 USD | 286,750.00 USD |
| `1D` | `1.19` | 69,170,000.00 USD | 0.00 USD | 69,170,000.00 USD | 48,820.00 USD | 7,460.00 USD | 27,490.00 USD |
| `7D` | `1.19` | 184,400,000.00 USD | 0.00 USD | 184,400,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `1D` | `1.19` | 69,080,000.00 USD | 0.00 USD | 69,080,000.00 USD | 1,560.00 USD | 16,590.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 184,220,000.00 USD | 0.00 USD | 184,220,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD |
| `1D` | `1.19` | 69,050,000.00 USD | 0.00 USD | 69,050,000.00 USD | 29,730.00 USD | 103.33 USD | 13,230.00 USD |
| `7D` | `1.19` | 183,300,000.00 USD | 0.00 USD | 183,300,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD |
| `1D` | `1.19` | 69,000,000.00 USD | 0.00 USD | 69,000,000.00 USD | 28,290.00 USD | 10,480.00 USD | 48,340.00 USD |
| `7D` | `1.19` | 182,730,000.00 USD | 0.00 USD | 182,730,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD |
| `1D` | `1.19` | 68,920,000.00 USD | 0.00 USD | 68,920,000.00 USD | 48,530.00 USD | 27,990.00 USD | 102,020.00 USD |
| `7D` | `1.19` | 182,360,000.00 USD | 0.00 USD | 182,360,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD |
| `1D` | `1.20` | 68,740,000.00 USD | 0.00 USD | 68,740,000.00 USD | 83,580.00 USD | 33,950.00 USD | 31,680.00 USD |
| `7D` | `1.20` | 181,600,000.00 USD | 0.00 USD | 181,600,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD |
| `1D` | `1.20` | 68,590,000.00 USD | 0.00 USD | 68,590,000.00 USD | 109,050.00 USD | 6,620.00 USD | 18,500.00 USD |
| `7D` | `1.20` | 180,890,000.00 USD | 0.00 USD | 180,890,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD |
| `1D` | `1.20` | 68,450,000.00 USD | 0.00 USD | 68,450,000.00 USD | 25,830.00 USD | 21,290.00 USD | 1,700.00 USD |
| `7D` | `1.20` | 180,820,000.00 USD | 0.00 USD | 180,820,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 68,400,000.00 USD | 0.00 USD | 68,400,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 180,700,000.00 USD | 0.00 USD | 180,700,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD |
| `1D` | `1.20` | 68,370,000.00 USD | 0.00 USD | 68,370,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 180,390,000.00 USD | 0.00 USD | 180,390,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD |
| `7D` | `1.21` | 180,240,000.00 USD | 0.00 USD | 180,240,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD |
| `1D` | `1.21` | 68,260,000.00 USD | 0.00 USD | 68,260,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 180,220,000.00 USD | 0.00 USD | 180,220,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD |
| `1D` | `1.21` | 68,250,000.00 USD | 0.00 USD | 68,250,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 179,950,000.00 USD | 0.00 USD | 179,950,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD |
| `7D` | `1.21` | 178,980,000.00 USD | 0.00 USD | 178,980,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD |
| `7D` | `1.21` | 178,460,000.00 USD | 0.00 USD | 178,460,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD |
| `7D` | `1.22` | 178,290,000.00 USD | 0.00 USD | 178,290,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 178,190,000.00 USD | 0.00 USD | 178,190,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `1.22` | 178,160,000.00 USD | 0.00 USD | 178,160,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD |
| `7D` | `1.22` | 178,140,000.00 USD | 0.00 USD | 178,140,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD |
| `7D` | `1.22` | 177,920,000.00 USD | 0.00 USD | 177,920,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD |
| `7D` | `1.23` | 177,250,000.00 USD | 0.00 USD | 177,250,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD |
| `7D` | `1.23` | 176,460,000.00 USD | 0.00 USD | 176,460,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD |
| `1D` | `1.23` | 68,210,000.00 USD | 0.00 USD | 68,210,000.00 USD | 100,480.00 USD | 374.17 USD | 160,090.00 USD |
| `7D` | `1.23` | 175,780,000.00 USD | 0.00 USD | 175,780,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD |
| `1D` | `1.23` | 67,950,000.00 USD | 0.00 USD | 67,950,000.00 USD | 265,980.00 USD | 67,310.00 USD | 639,320.00 USD |
| `7D` | `1.23` | 174,640,000.00 USD | 0.00 USD | 174,640,000.00 USD | 706,530.00 USD | 355,960.00 USD | 940,390.00 USD |
| `1D` | `1.23` | 66,980,000.00 USD | 0.00 USD | 66,980,000.00 USD | 91,890.00 USD | 54,570.00 USD | 208,170.00 USD |
| `7D` | `1.23` | 172,640,000.00 USD | 0.00 USD | 172,640,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD |
| `1D` | `1.24` | 66,630,000.00 USD | 0.00 USD | 66,630,000.00 USD | 119,360.00 USD | 22,970.00 USD | 7,740.00 USD |
| `7D` | `1.24` | 169,600,000.00 USD | 0.00 USD | 169,600,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD |
| `1D` | `1.24` | 66,480,000.00 USD | 0.00 USD | 66,480,000.00 USD | 802,870.00 USD | 317,390.00 USD | 716,800.00 USD |
| `7D` | `1.24` | 165,110,000.00 USD | 0.00 USD | 165,110,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD |
| `1D` | `1.24` | 64,640,000.00 USD | 0.00 USD | 64,640,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD |
| `7D` | `1.24` | 160,200,000.00 USD | 0.00 USD | 160,200,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD |
| `1D` | `1.24` | 61,730,000.00 USD | 0.00 USD | 61,730,000.00 USD | 576,610.00 USD | 333,360.00 USD | 574,860.00 USD |
| `7D` | `1.24` | 154,290,000.00 USD | 0.00 USD | 154,290,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD |
| `1D` | `1.24` | 60,250,000.00 USD | 0.00 USD | 60,250,000.00 USD | 207,000.00 USD | 233,640.00 USD | 324,870.00 USD |
| `7D` | `1.24` | 151,240,000.00 USD | 0.00 USD | 151,240,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 59,480,000.00 USD | 0.00 USD | 59,480,000.00 USD | 546,970.00 USD | 84,110.00 USD | 349,560.00 USD |
| `7D` | `1.25` | 148,000,000.00 USD | 0.00 USD | 148,000,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD |
| `1D` | `1.25` | 58,500,000.00 USD | 0.00 USD | 58,500,000.00 USD | 384,220.00 USD | 90,850.00 USD | 261,580.00 USD |
| `7D` | `1.25` | 141,740,000.00 USD | 0.00 USD | 141,740,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.25` | 57,770,000.00 USD | 0.00 USD | 57,770,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD |
| `7D` | `1.25` | 132,290,000.00 USD | 0.00 USD | 132,290,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD |
| `1D` | `1.25` | 57,060,000.00 USD | 0.00 USD | 57,060,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD |
| `7D` | `1.25` | 125,870,000.00 USD | 0.00 USD | 125,870,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 56,290,000.00 USD | 0.00 USD | 56,290,000.00 USD | 471,210.00 USD | 17,220.00 USD | 531,190.00 USD |
| `7D` | `1.25` | 121,510,000.00 USD | 0.00 USD | 121,510,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD |
| `1D` | `1.25` | 55,270,000.00 USD | 0.00 USD | 55,270,000.00 USD | 607,050.00 USD | 98,250.00 USD | 1,120,000.00 USD |
| `7D` | `1.26` | 119,880,000.00 USD | 0.00 USD | 119,880,000.00 USD | 1,360,000.00 USD | 849,040.00 USD | 2,940,000.00 USD |
| `1D` | `1.26` | 53,440,000.00 USD | 0.00 USD | 53,440,000.00 USD | 640,510.00 USD | 336,810.00 USD | 1,030,000.00 USD |
| `7D` | `1.26` | 114,740,000.00 USD | 0.00 USD | 114,740,000.00 USD | 1,070,000.00 USD | 211,890.00 USD | 1,000,000.00 USD |
| `1D` | `1.26` | 51,440,000.00 USD | 0.00 USD | 51,440,000.00 USD | 327,310.00 USD | 3,600.00 USD | 313,690.00 USD |
| `7D` | `1.26` | 112,450,000.00 USD | 0.00 USD | 112,450,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD |
| `1D` | `1.26` | 50,790,000.00 USD | 0.00 USD | 50,790,000.00 USD | 437,560.00 USD | 218,760.00 USD | 631,850.00 USD |
| `7D` | `1.26` | 108,970,000.00 USD | 0.00 USD | 108,970,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD |
| `1D` | `1.26` | 49,500,000.00 USD | 0.00 USD | 49,500,000.00 USD | 1,470,000.00 USD | 545,220.00 USD | 1,080,000.00 USD |
| `7D` | `1.26` | 104,020,000.00 USD | 0.00 USD | 104,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD |
| `1D` | `1.26` | 46,410,000.00 USD | 0.00 USD | 46,410,000.00 USD | 2,670,000.00 USD | 1,350,000.00 USD | 1,980,000.00 USD |
| `7D` | `1.27` | 95,020,000.00 USD | 0.00 USD | 95,020,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD |
| `1D` | `1.27` | 40,410,000.00 USD | 0.00 USD | 40,410,000.00 USD | 1,620,000.00 USD | 666,960.00 USD | 1,860,000.00 USD |
| `7D` | `1.27` | 82,050,000.00 USD | 0.00 USD | 82,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD |
| `1D` | `1.27` | 36,270,000.00 USD | 0.00 USD | 36,270,000.00 USD | 1,520,000.00 USD | 733,250.00 USD | 3,270,000.00 USD |
| `7D` | `1.27` | 73,670,000.00 USD | 0.00 USD | 73,670,000.00 USD | 3,090,000.00 USD | 2,160,000.00 USD | 6,460,000.00 USD |
| `1D` | `1.27` | 30,750,000.00 USD | 0.00 USD | 30,750,000.00 USD | 1,480,000.00 USD | 431,480.00 USD | 1,690,000.00 USD |
| `7D` | `1.27` | 61,960,000.00 USD | 0.00 USD | 61,960,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD |
| `1D` | `1.27` | 27,140,000.00 USD | 0.00 USD | 27,140,000.00 USD | 1,410,000.00 USD | 341,030.00 USD | 735,730.00 USD |
| `7D` | `1.27` | 47,670,000.00 USD | 0.00 USD | 47,670,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD |
| `1D` | `1.27` | 24,650,000.00 USD | 0.00 USD | 24,650,000.00 USD | 2,290,000.00 USD | 848,600.00 USD | 2,800,000.00 USD |
| `7D` | `1.28` | 29,820,000.00 USD | 0.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD |
| `1D` | `1.28` | 18,720,000.00 USD | 0.00 USD | 18,720,000.00 USD | 4,640,000.00 USD | 2,800,000.00 USD | 3,960,000.00 USD |
| `7D` | `1.28` | 17,330,000.00 USD | 0.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.28` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 3,070,000.00 USD | 2,050,000.00 USD | 1,960,000.00 USD |
| `7D` | `1.28` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 234,790.00 USD | 0.00 USD | 234,790.00 USD | 0.00 USD | 234,790.00 USD | 0.00 USD |
| `7D` | `1.28` | 108,100.00 USD | 0.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD |
| `1D` | `1.28` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.28` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD |
| `7D` | `1.28` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD |
| `1D` | `1.28` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 1,250,000.00 USD | 488,880.00 USD | 0.00 USD |
| `7D` | `1.29` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD |
| `1D` | `1.29` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 365,870.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD |
| `7D` | `1.29` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD |
| `1D` | `1.29` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 388,000.00 USD | 0.00 USD | 1,860,000.00 USD |
| `7D` | `1.29` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD |
| `1D` | `1.29` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 1,060,000.00 USD | 449,340.00 USD | 2,790,000.00 USD |
| `7D` | `1.30` | 20,850,000.00 USD | 20,850,000.00 USD | 0.00 USD | 777,570.00 USD | 1,090,000.00 USD | 3,420,000.00 USD |
| `1D` | `1.30` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 278,090.00 USD | 626,520.00 USD | 829,060.00 USD |
| `7D` | `1.30` | 22,090,000.00 USD | 22,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 175,900.00 USD | 86,920.00 USD | 0.00 USD |
| `7D` | `1.30` | 23,060,000.00 USD | 23,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 193,920.00 USD | 81,320.00 USD | 1,170,000.00 USD |
| `7D` | `1.30` | 23,920,000.00 USD | 23,920,000.00 USD | 0.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD |
| `1D` | `1.30` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD |
| `7D` | `1.30` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 299,990.00 USD | 353,430.00 USD | 127,330.00 USD |
| `7D` | `1.31` | 27,810,000.00 USD | 27,810,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 594,820.00 USD | 120,350.00 USD | 1,040,000.00 USD |
| `7D` | `1.31` | 31,280,000.00 USD | 31,280,000.00 USD | 0.00 USD | 722,880.00 USD | 352,510.00 USD | 2,390,000.00 USD |
| `1D` | `1.31` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 785,890.00 USD | 186,820.00 USD | 1,610,000.00 USD |
| `7D` | `1.31` | 33,040,000.00 USD | 33,040,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD |
| `1D` | `1.31` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 767,720.00 USD | 688,780.00 USD | 450,450.00 USD |
| `7D` | `1.31` | 36,800,000.00 USD | 36,800,000.00 USD | 0.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 1,290,000.00 USD | 511,150.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 37,950,000.00 USD | 37,950,000.00 USD | 0.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD |
| `1D` | `1.31` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 372,630.00 USD | 572,040.00 USD | 2,530,000.00 USD |
| `7D` | `1.32` | 42,130,000.00 USD | 42,130,000.00 USD | 0.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 33,390,000.00 USD | 33,390,000.00 USD | 0.00 USD | 1,250,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD |
| `7D` | `1.32` | 46,980,000.00 USD | 46,980,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 38,880,000.00 USD | 38,880,000.00 USD | 0.00 USD | 1,990,000.00 USD | 977,080.00 USD | 2,520,000.00 USD |
| `7D` | `1.32` | 48,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 42,110,000.00 USD | 42,110,000.00 USD | 0.00 USD | 1,510,000.00 USD | 706,650.00 USD | 1,020,000.00 USD |
| `7D` | `1.32` | 51,770,000.00 USD | 51,770,000.00 USD | 0.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD |
| `1D` | `1.32` | 46,700,000.00 USD | 46,700,000.00 USD | 0.00 USD | 1,970,000.00 USD | 720,740.00 USD | 1,890,000.00 USD |
| `7D` | `1.32` | 54,390,000.00 USD | 54,390,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD |
| `1D` | `1.32` | 48,690,000.00 USD | 48,690,000.00 USD | 0.00 USD | 1,080,000.00 USD | 287,550.00 USD | 625,660.00 USD |
| `7D` | `1.33` | 56,200,000.00 USD | 56,200,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 51,180,000.00 USD | 51,180,000.00 USD | 0.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 57,250,000.00 USD | 57,250,000.00 USD | 0.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 53,430,000.00 USD | 53,430,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 58,870,000.00 USD | 58,870,000.00 USD | 0.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 56,270,000.00 USD | 56,270,000.00 USD | 0.00 USD | 848,670.00 USD | 298,620.00 USD | 1,700,000.00 USD |
| `7D` | `1.33` | 61,280,000.00 USD | 61,280,000.00 USD | 0.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD |
| `1D` | `1.33` | 58,480,000.00 USD | 58,480,000.00 USD | 0.00 USD | 979,210.00 USD | 152,260.00 USD | 1,080,000.00 USD |
| `7D` | `1.33` | 62,950,000.00 USD | 62,950,000.00 USD | 0.00 USD | 450,460.00 USD | 178,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.33` | 60,520,000.00 USD | 60,520,000.00 USD | 0.00 USD | 809,250.00 USD | 354,550.00 USD | 872,500.00 USD |
| `7D` | `1.34` | 64,490,000.00 USD | 64,490,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 62,590,000.00 USD | 62,590,000.00 USD | 0.00 USD | 876,830.00 USD | 219,260.00 USD | 976,640.00 USD |
| `7D` | `1.34` | 66,930,000.00 USD | 66,930,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 65,460,000.00 USD | 65,460,000.00 USD | 0.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD |
| `7D` | `1.34` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 69,050,000.00 USD | 69,050,000.00 USD | 0.00 USD | 1,780,000.00 USD | 821,890.00 USD | 996,320.00 USD |
| `7D` | `1.34` | 74,720,000.00 USD | 74,720,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD |
| `1D` | `1.34` | 73,780,000.00 USD | 73,780,000.00 USD | 0.00 USD | 2,510,000.00 USD | 785,850.00 USD | 1,440,000.00 USD |
| `7D` | `1.34` | 82,100,000.00 USD | 82,100,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 3,140,000.00 USD |
| `1D` | `1.34` | 76,230,000.00 USD | 76,230,000.00 USD | 0.00 USD | 918,290.00 USD | 629,160.00 USD | 904,690.00 USD |
| `7D` | `1.35` | 92,860,000.00 USD | 92,860,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 77,630,000.00 USD | 77,630,000.00 USD | 0.00 USD | 585,620.00 USD | 289,260.00 USD | 527,880.00 USD |
| `7D` | `1.35` | 101,690,000.00 USD | 101,690,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD |
| `1D` | `1.35` | 80,630,000.00 USD | 80,630,000.00 USD | 0.00 USD | 1,290,000.00 USD | 356,450.00 USD | 1,350,000.00 USD |
| `7D` | `1.35` | 110,900,000.00 USD | 110,900,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 81,720,000.00 USD | 81,720,000.00 USD | 0.00 USD | 507,940.00 USD | 127,500.00 USD | 452,540.00 USD |
| `7D` | `1.35` | 120,150,000.00 USD | 120,150,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 83,590,000.00 USD | 83,590,000.00 USD | 0.00 USD | 749,290.00 USD | 397,350.00 USD | 728,820.00 USD |
| `7D` | `1.35` | 127,690,000.00 USD | 127,690,000.00 USD | 0.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD |
| `1D` | `1.35` | 85,720,000.00 USD | 85,720,000.00 USD | 0.00 USD | 722,260.00 USD | 297,760.00 USD | 1,110,000.00 USD |
| `7D` | `1.36` | 134,860,000.00 USD | 134,860,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD |
| `1D` | `1.36` | 87,460,000.00 USD | 87,460,000.00 USD | 0.00 USD | 983,180.00 USD | 66,140.00 USD | 685,970.00 USD |
| `7D` | `1.36` | 137,390,000.00 USD | 137,390,000.00 USD | 0.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 88,170,000.00 USD | 88,170,000.00 USD | 0.00 USD | 396,550.00 USD | 150,540.00 USD | 163,660.00 USD |
| `7D` | `1.36` | 140,450,000.00 USD | 140,450,000.00 USD | 0.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 88,970,000.00 USD | 88,970,000.00 USD | 0.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD |
| `7D` | `1.36` | 144,240,000.00 USD | 144,240,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 90,070,000.00 USD | 90,070,000.00 USD | 0.00 USD | 452,880.00 USD | 103,540.00 USD | 545,930.00 USD |
| `7D` | `1.36` | 147,020,000.00 USD | 147,020,000.00 USD | 0.00 USD | 1,430,000.00 USD | 643,080.00 USD | 708,120.00 USD |
| `1D` | `1.36` | 90,120,000.00 USD | 90,120,000.00 USD | 0.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD |
| `7D` | `1.37` | 147,760,000.00 USD | 147,760,000.00 USD | 0.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 90,440,000.00 USD | 90,440,000.00 USD | 0.00 USD | 68,130.00 USD | 85,100.00 USD | 170,030.00 USD |
| `7D` | `1.37` | 148,870,000.00 USD | 148,870,000.00 USD | 0.00 USD | 544,160.00 USD | 181,820.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 90,830,000.00 USD | 90,830,000.00 USD | 0.00 USD | 159,370.00 USD | 1,410.00 USD | 229,350.00 USD |
| `7D` | `1.37` | 150,600,000.00 USD | 150,600,000.00 USD | 0.00 USD | 477,130.00 USD | 362,580.00 USD | 883,840.00 USD |
| `1D` | `1.37` | 91,020,000.00 USD | 91,020,000.00 USD | 0.00 USD | 1,740.00 USD | 66,370.00 USD | 119,540.00 USD |
| `7D` | `1.37` | 152,750,000.00 USD | 152,750,000.00 USD | 0.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD |
| `1D` | `1.37` | 91,170,000.00 USD | 91,170,000.00 USD | 0.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD |
| `7D` | `1.37` | 154,860,000.00 USD | 154,860,000.00 USD | 0.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD |
| `1D` | `1.38` | 91,290,000.00 USD | 91,290,000.00 USD | 0.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD |
| `7D` | `1.38` | 156,540,000.00 USD | 156,540,000.00 USD | 0.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD |
| `1D` | `1.38` | 91,620,000.00 USD | 91,620,000.00 USD | 0.00 USD | 112,910.00 USD | 50,330.00 USD | 164,490.00 USD |
| `7D` | `1.38` | 158,090,000.00 USD | 158,090,000.00 USD | 0.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD |
| `1D` | `1.38` | 92,180,000.00 USD | 92,180,000.00 USD | 0.00 USD | 271,120.00 USD | 72,410.00 USD | 212,560.00 USD |
| `7D` | `1.38` | 160,130,000.00 USD | 160,130,000.00 USD | 0.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD |
| `1D` | `1.38` | 92,660,000.00 USD | 92,660,000.00 USD | 0.00 USD | 264,080.00 USD | 108,980.00 USD | 109,920.00 USD |
| `7D` | `1.38` | 162,400,000.00 USD | 162,400,000.00 USD | 0.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD |
| `1D` | `1.38` | 93,060,000.00 USD | 93,060,000.00 USD | 0.00 USD | 304,540.00 USD | 24,460.00 USD | 77,390.00 USD |
| `7D` | `1.38` | 163,100,000.00 USD | 163,100,000.00 USD | 0.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 93,250,000.00 USD | 93,250,000.00 USD | 0.00 USD | 91,420.00 USD | 54,030.00 USD | 40,640.00 USD |
| `7D` | `1.39` | 164,020,000.00 USD | 164,020,000.00 USD | 0.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD |
| `1D` | `1.39` | 93,340,000.00 USD | 93,340,000.00 USD | 0.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD |
| `7D` | `1.39` | 164,880,000.00 USD | 164,880,000.00 USD | 0.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD |
| `1D` | `1.39` | 93,730,000.00 USD | 93,730,000.00 USD | 0.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD |
| `7D` | `1.39` | 165,620,000.00 USD | 165,620,000.00 USD | 0.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD |
| `7D` | `1.39` | 165,940,000.00 USD | 165,940,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.39` | 166,010,000.00 USD | 166,010,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 93,750,000.00 USD | 93,750,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 166,100,000.00 USD | 166,100,000.00 USD | 0.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD |
| `1D` | `1.40` | 93,850,000.00 USD | 93,850,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 166,110,000.00 USD | 166,110,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 166,170,000.00 USD | 166,170,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 166,250,000.00 USD | 166,250,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 166,540,000.00 USD | 166,540,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 166,700,000.00 USD | 166,700,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 166,860,000.00 USD | 166,860,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.41` | 94,050,000.00 USD | 94,050,000.00 USD | 0.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD |
| `7D` | `1.41` | 167,590,000.00 USD | 167,590,000.00 USD | 0.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD |
| `1D` | `1.41` | 94,310,000.00 USD | 94,310,000.00 USD | 0.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD |
| `7D` | `1.41` | 167,820,000.00 USD | 167,820,000.00 USD | 0.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.41` | 94,340,000.00 USD | 94,340,000.00 USD | 0.00 USD | 0.00 USD | 383.75 USD | 28,820.00 USD |
| `7D` | `1.41` | 168,120,000.00 USD | 168,120,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `1D` | `1.42` | 94,380,000.00 USD | 94,380,000.00 USD | 0.00 USD | 29,120.00 USD | 9,190.00 USD | 2,350.00 USD |
| `7D` | `1.42` | 168,680,000.00 USD | 168,680,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `1D` | `1.42` | 94,690,000.00 USD | 94,690,000.00 USD | 0.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.42` | 169,420,000.00 USD | 169,420,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.42` | 95,310,000.00 USD | 95,310,000.00 USD | 0.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.42` | 170,470,000.00 USD | 170,470,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.42` | 95,930,000.00 USD | 95,930,000.00 USD | 0.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.42` | 171,800,000.00 USD | 171,800,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.42` | 96,150,000.00 USD | 96,150,000.00 USD | 0.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.42` | 172,000,000.00 USD | 172,000,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `1D` | `1.43` | 96,230,000.00 USD | 96,230,000.00 USD | 0.00 USD | 29,370.00 USD | 27,060.00 USD | 28,790.00 USD |
| `1D` | `1.43` | 96,360,000.00 USD | 96,360,000.00 USD | 0.00 USD | 70,500.00 USD | 8,390.00 USD | 44,770.00 USD |
| `7D` | `1.43` | 172,760,000.00 USD | 172,760,000.00 USD | 0.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD |
| `7D` | `1.43` | 173,830,000.00 USD | 173,830,000.00 USD | 0.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `7D` | `1.43` | 175,860,000.00 USD | 175,860,000.00 USD | 0.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `7D` | `1.43` | 176,710,000.00 USD | 176,710,000.00 USD | 0.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `7D` | `1.43` | 177,600,000.00 USD | 177,600,000.00 USD | 0.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `7D` | `1.44` | 177,630,000.00 USD | 177,630,000.00 USD | 0.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD |
| `7D` | `1.44` | 178,260,000.00 USD | 178,260,000.00 USD | 0.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD |
| `7D` | `1.44` | 178,680,000.00 USD | 178,680,000.00 USD | 0.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `7D` | `1.44` | 179,290,000.00 USD | 179,290,000.00 USD | 0.00 USD | 270,280.00 USD | 134,360.00 USD | 209,010.00 USD |
| `7D` | `1.44` | 179,530,000.00 USD | 179,530,000.00 USD | 0.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `7D` | `1.45` | 179,630,000.00 USD | 179,630,000.00 USD | 0.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 180,000,000.00 USD | 180,000,000.00 USD | 0.00 USD | 69,200.00 USD | 26,800.00 USD | 278,000.00 USD |
| `7D` | `1.45` | 180,190,000.00 USD | 180,190,000.00 USD | 0.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `7D` | `1.45` | 181,090,000.00 USD | 181,090,000.00 USD | 0.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD |
| `7D` | `1.45` | 181,630,000.00 USD | 181,630,000.00 USD | 0.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `3.02B` | Total OI Tokens: `2,347,493,664.5 XRP`
  * 1h OI Change: `+1.32%` | 4h OI Change: `-0.41%` | 24h OI Change: `+1.32%`
  * Exchange Breakdown: Binance=`492.64M` | Bybit=`332.97M` | OKX=`101.30M` | Hyperliquid=`226.51M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `53.08K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0074%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0034%` | **USDT KuCoin** | `0.0089%` |
| **USDT MEXC** | `0.0074%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0036%` | **USDT Bitget** | `0.0035%` |
| **CoinM Binance** | `0.0094%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `57.62%` | `42.38%` | `1.36` | 204,780,000.00 USD |
| `15M` | `Binance` | `53.52%` | `46.48%` | `1.15` | 59,720,000.00 USD |
| `15M` | `OKX` | `58.25%` | `41.75%` | `1.40` | 39,000,000.00 USD |
| `15M` | `Bybit` | `77.38%` | `22.62%` | `3.42` | 15,040,000.00 USD |
| `15M` | `KuCoin` | `28.49%` | `71.51%` | `0.40` | 264,950.00 USD |
| `15M` | `Gate` | `52.84%` | `47.16%` | `1.12` | 28,030,000.00 USD |
| `15M` | `Bitget` | `60.56%` | `39.44%` | `1.54` | 5,900,000.00 USD |
| `15M` | `BingX` | `60.05%` | `39.95%` | `1.50` | 2,830,000.00 USD |
| `15M` | `MEXC` | `48.25%` | `51.75%` | `0.93` | 10,240,000.00 USD |
| `15M` | `Bitunix` | `57.76%` | `42.24%` | `1.37` | 7,480,000.00 USD |
| `15M` | `Hyperliquid` | `49.03%` | `50.97%` | `0.96` | 2,650,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `10%` | `90%` | `0.11` | 2,010,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.98%` | `0.02%` | `4999.00` | 9,420,000.00 USD |
| `15M` | `HTX` | `65.1%` | `34.9%` | `1.87` | 6,360,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `79.58%` | `20.42%` | `3.90` | 3,630,000.00 USD |
| `15M` | `Bitfinex` | `64.89%` | `35.11%` | `1.85` | 13,590.00 USD |
| `15M` | `Kraken` | `54.03%` | `45.97%` | `1.18` | 273,520.00 USD |
| `15M` | `Aster` | `20.06%` | `79.94%` | `0.25` | 1,790,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.53%` | `62.47%` | `0.60` | 10,130,000.00 USD |
| `15M` | `Whale Positions` | `53.52%` | `46.48%` | `1.15` | 59,720,000.00 USD |
| `15M` | `Global Accounts` | `57.62%` | `42.38%` | `1.36` | 204,780,000.00 USD |
| `1H` | `XRP` | `58.34%` | `41.66%` | `1.40` | 818,690,000.00 USD |
| `1H` | `Binance` | `55.35%` | `44.65%` | `1.24` | 222,770,000.00 USD |
| `1H` | `OKX` | `58.1%` | `41.9%` | `1.39` | 141,210,000.00 USD |
| `1H` | `Bybit` | `72.54%` | `27.46%` | `2.64` | 60,390,000.00 USD |
| `1H` | `KuCoin` | `50.41%` | `49.59%` | `1.02` | 287,470.00 USD |
| `1H` | `Gate` | `54.04%` | `45.96%` | `1.18` | 117,540,000.00 USD |
| `1H` | `Bitget` | `56.35%` | `43.65%` | `1.29` | 44,700,000.00 USD |
| `1H` | `BingX` | `60.61%` | `39.39%` | `1.54` | 19,580,000.00 USD |
| `1H` | `MEXC` | `55.39%` | `44.61%` | `1.24` | 35,870,000.00 USD |
| `1H` | `Bitunix` | `57.76%` | `42.24%` | `1.37` | 28,550,000.00 USD |
| `1H` | `Hyperliquid` | `47.72%` | `52.28%` | `0.91` | 10,840,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.68%` | `54.32%` | `0.84` | 5,860,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `73.27%` | `26.73%` | `2.74` | 70,080,000.00 USD |
| `1H` | `HTX` | `51.18%` | `48.82%` | `1.05` | 17,450,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `70.49%` | `29.51%` | `2.39` | 4,740,000.00 USD |
| `1H` | `Bitfinex` | `72.14%` | `27.86%` | `2.59` | 49,010.00 USD |
| `1H` | `Kraken` | `68.49%` | `31.51%` | `2.17` | 4,010,000.00 USD |
| `1H` | `Aster` | `47.96%` | `52.04%` | `0.92` | 5,990,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.57%` | `50.43%` | `0.98` | 28,750,000.00 USD |
| `1H` | `Whale Positions` | `55.35%` | `44.65%` | `1.24` | 222,770,000.00 USD |
| `1H` | `Global Accounts` | `58.34%` | `41.66%` | `1.40` | 818,690,000.00 USD |
| `4H` | `XRP` | `46.58%` | `53.42%` | `0.87` | 7,830,000,000.00 USD |
| `4H` | `Binance` | `44.37%` | `55.63%` | `0.80` | 2,320,000,000.00 USD |
| `4H` | `OKX` | `46.26%` | `53.74%` | `0.86` | 1,460,000,000.00 USD |
| `4H` | `Bybit` | `46.94%` | `53.06%` | `0.88` | 574,220,000.00 USD |
| `4H` | `KuCoin` | `53.29%` | `46.71%` | `1.14` | 20,650,000.00 USD |
| `4H` | `Gate` | `50.02%` | `49.98%` | `1.00` | 1,200,000,000.00 USD |
| `4H` | `Bitget` | `50.01%` | `49.99%` | `1.00` | 421,780,000.00 USD |
| `4H` | `BingX` | `46.98%` | `53.02%` | `0.89` | 108,060,000.00 USD |
| `4H` | `MEXC` | `50.69%` | `49.31%` | `1.03` | 332,530,000.00 USD |
| `4H` | `Bitunix` | `48.01%` | `51.99%` | `0.92` | 281,300,000.00 USD |
| `4H` | `Hyperliquid` | `56.87%` | `43.13%` | `1.32` | 186,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `46.77%` | `53.23%` | `0.88` | 23,120,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `38.89%` | `61.11%` | `0.64` | 488,650,000.00 USD |
| `4H` | `HTX` | `38.41%` | `61.59%` | `0.62` | 120,000,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.89%` | `49.11%` | `1.04` | 44,210,000.00 USD |
| `4H` | `Bitfinex` | `41.22%` | `58.78%` | `0.70` | 1,510,000.00 USD |
| `4H` | `Kraken` | `63.12%` | `36.88%` | `1.71` | 41,100,000.00 USD |
| `4H` | `Aster` | `40.52%` | `59.48%` | `0.68` | 79,230,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.98%` | `51.02%` | `0.96` | 121,210,000.00 USD |
| `4H` | `Whale Positions` | `44.37%` | `55.63%` | `0.80` | 2,320,000,000.00 USD |
| `4H` | `Global Accounts` | `46.58%` | `53.42%` | `0.87` | 7,830,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 8,857,459.31 USD | 3,136,112.07 USD | 5,721,347.24 USD | -2,585,235.17 USD | `-29.19%` | `5B / 22S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 11,824,590.46 USD | 6,782,340.79 USD | 5,042,249.67 USD | 1,740,091.12 USD | `+14.72%` | `12B / 8S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,908,299.96 USD | 2,545,215.27 USD | 2,363,084.69 USD | 182,130.57 USD | `+3.71%` | `7B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 30,348,241.89 USD | 10,177,546.51 USD | 20,170,695.38 USD | -9,993,148.87 USD | `-32.93%` | `4B / 38S` |
| `5:00 UTC` | `1.29` | `1.28` | `1.29` | `1.29` | `1.28` | 10,140,362.32 USD | 5,667,315.95 USD | 4,473,046.37 USD | 1,194,269.58 USD | `+11.78%` | `17B / 12S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,885,752.93 USD | 2,814,674.62 USD | 3,071,078.30 USD | -256,403.68 USD | `-4.36%` | `5B / 13S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,036,330.68 USD | 2,484,228.37 USD | 2,552,102.32 USD | -67,873.95 USD | `-1.35%` | `8B / 7S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.28` | 3,779,916.77 USD | 1,963,240.26 USD | 1,816,676.51 USD | 146,563.75 USD | `+3.88%` | `6B / 5S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 1,338,750.68 USD | 677,768.26 USD | 660,982.43 USD | 16,785.83 USD | `+1.25%` | `4B / 2S` |

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
| `5m` | 219,260.00 USD | 102,810.00 USD | **`ACCUMULATION`** |
| `15m` | 397,760.00 USD | 1,180,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,060,000.00 USD | 695,470.00 USD | **`ACCUMULATION`** |
| `1h` | 1,280,000.00 USD | 2,310,000.00 USD | **`ACCUMULATION`** |
| `2h` | -4,620,000.00 USD | -16,900,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,890,000.00 USD | -31,040,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,460,000.00 USD | -23,990,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,560,000.00 USD | -24,760,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,600,000.00 USD | -24,890,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -28,640,000.00 USD | -77,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -79,100,000.00 USD | -95,600,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -556,620,000.00 USD | -1,190,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+219.26K` | 15m=`+397.76K` | 1h=`+1.28M` | 24h=`-28.64M`
* Futures Capital Netflows: 5m=`+102.81K` | 15m=`+1.18M` | 1h=`+2.31M` | 24h=`-77.17M`
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0795` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `4.30`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.50` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-1.71`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
